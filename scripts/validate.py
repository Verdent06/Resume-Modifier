#!/usr/bin/env python3
"""
validate.py — deterministic resume gates for the resume pipeline.

Runs between the writer and the grader, on the compiled artifact. Produces a
pass/fail gate report. The orchestrator treats this report as ground truth and
does not let the write/grade loop exit while a hard gate fails.

USAGE (from repo root)
    python scripts/validate.py gates \
        --tex "applications/…/Ankur Desai Resume.tex" \
        --inputs applications/…/.pipeline/gate_inputs.json \
        --pdf "applications/…/Ankur Desai Resume.pdf" --phase loop \
        --out applications/…/.pipeline/gate_report.json

    python scripts/validate.py demerits \
        --demerits applications/…/.pipeline/demerits.json \
        --out applications/…/.pipeline/demerit_score.json

    python scripts/validate.py check-report --report grader_output.txt

  gates        exit 0 -> all HARD gates pass;  exit 1 -> a hard gate failed
  demerits     exit 0 -> scored; loop target is weighted == 0 and no emergency
  writer-loop  exit 0 -> writer_loop_status.json valid
  check-report exit 0 -> JSON and wishlist match;  exit 1 -> diverged

LaTeX / pipeline file cleanup lives in scripts/cleanup.py.

gate_inputs.json (assembled by the orchestrator from the Step 1 state object +
context.md inventory) is the single structured input. Shape:

    {
      "jd_languages":        ["C++", "Go", "Rust", "Java", "Python"],
      "jd_required_keywords":["ROS2", "computer vision", ...],
      "candidate_languages": ["C++", "Python", "Go", "Java", "SQL", "Bash"],
      "exempt_entries":      ["Secure and Efficient Autonomous Systems Lab"],
      "iter1_counts":        {"Robostangs (FRC Team 548)": 3, "WizViz": 2, ...}
    }

  - jd_languages          : languages the JD lists (any phrasing).
  - candidate_languages   : the master language inventory from context.md. Used
                            to compute "JD languages the candidate actually has"
                            — never require a language he doesn't possess.
  - exempt_entries        : entries whose every bullet is genuinely metric-
                            resistant (research / robustness). EXEMPTION IS
                            LOGGED in the report so it cannot be gamed silently.
  - iter1_counts          : per-entry bullet count after iteration 1. Drives the
                            anti-deletion gate. Empty/omitted on iteration 1.

The validator reading context-derived inputs does NOT break grader-blindness:
this is code producing mechanical true/false, not the grader LLM forming a
qualitative judgment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path


# ============================================================================
#  CONFIG — taxonomy and the one fuzzy edge (impact-metric detection)
# ============================================================================

# Skills-line items that are NEVER orphans and NEVER probe-worthy: a recruiter
# does not ask "where did you use Git". Languages are handled separately (they
# are exempt from the orphan gate AND eligible for the required-language gate).
EXEMPT_SKILL_TOKENS = {
    "git", "github", "gitlab", "linux", "unix", "macos", "windows",
    "bash", "shell", "zsh", "vim", "vs code", "vscode", "rosbag",
}
# Skill buckets whose every item is treated as a baseline tool (orphan-exempt).
EXEMPT_BUCKET_LABELS = {"languages", "tools"}

# IMPACT-METRIC ALLOWLIST (this is the only non-crisp gate; see module note).
# A bullet "carries an impact metric" iff it matches one of these. The design is
# deliberately an allowlist of genuine impact signals, not a denylist of vanity
# ones: a bare "5 gestures" / "three architectures" simply fails to match and is
# (correctly) not counted. Conservative and deterministic. The grader still owns
# the finer impact-vs-vanity judgment in prose; this only sets the hard ceiling.
_IMPACT_UNIT = re.compile(
    r"\b\d+(?:\.\d+)?\s?"
    r"(?:%|x|×|hz|khz|mhz|ms|µs|us|ns|fps|gb|mb|kb|tb|rps|qps|qpm|"
    r"k|m|×faster|x\b)"
    r"\b",
    re.IGNORECASE,
)
_IMPACT_SCALE = re.compile(
    r"\b(?:top\s+\d+|"
    r"\d+\s*\+?\s*(?:members|users|customers|requests|nodes|services|teams)|"
    r"\d+\s*(?:engineers|developers|contributors)|"
    r"\d+(?:\.\d+)?\s?(?:second|seconds|minute|minutes|hour|hours)\b|"
    r"reduc\w*\s+\w+\s+by\s+\d+|"
    r"\d+\s?(?:×|x)\s+(?:faster|throughput|speedup))\b",
    re.IGNORECASE,
)


def bullet_has_impact_metric(text: str) -> bool:
    return bool(_IMPACT_UNIT.search(text) or _IMPACT_SCALE.search(text))


# ============================================================================
#  LaTeX PARSING — against the real macros in applications/template.cls
#    \begin{rSection}{<1st letter>}{<rest of title>} ... \end{rSection}
#    \begin{rSectionEntry}{name}{dates}{tagline}{tech}{loc} \item ... \end{...}
#    \begin{rSet}{label}{comma, separated, items} \end{rSet}
# ============================================================================

def _take_braced_groups(s: str, start: int, n: int):
    """From index `start` (at or before the first '{'), return (groups, end_idx)
    for n balanced-brace groups. Brace-aware, so \\href{a}{b} inside a param does
    not break extraction."""
    groups, i, length = [], start, len(s)
    for _ in range(n):
        while i < length and s[i] != "{":
            i += 1
        if i >= length:
            break
        depth, j, buf = 0, i, []
        while j < length:
            c = s[j]
            if c == "{":
                depth += 1
                if depth > 1:
                    buf.append(c)
            elif c == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
                buf.append(c)
            else:
                buf.append(c)
            j += 1
        groups.append("".join(buf).strip())
        i = j
    return groups, i


def _split_top_level_commas(s: str) -> list[str]:
    """Split on commas not inside parentheses, so 'AWS (EC2, S3, RDS), Terraform'
    yields ['AWS (EC2, S3, RDS)', 'Terraform']."""
    out, depth, buf = [], 0, []
    for c in s:
        if c == "(":
            depth += 1
        elif c == ")":
            depth = max(0, depth - 1)
        if c == "," and depth == 0:
            out.append("".join(buf).strip())
            buf = []
        else:
            buf.append(c)
    if "".join(buf).strip():
        out.append("".join(buf).strip())
    return out


_TEX_CLEAN = re.compile(r"\\[a-zA-Z]+\*?|[{}]|\$")


def _strip_tex(s: str) -> str:
    return _TEX_CLEAN.sub(" ", s).replace("--", " ").strip()


@dataclass
class Entry:
    name: str
    section: str
    bullets: list[str] = field(default_factory=list)
    tech_line: str = ""


@dataclass
class ParsedResume:
    entries: list[Entry] = field(default_factory=list)          # experience + projects only
    skills: dict[str, list[str]] = field(default_factory=dict)  # bucket label -> items

    def body_text(self) -> str:
        parts = []
        for e in self.entries:
            parts.extend(e.bullets)
            if e.tech_line:
                parts.append(e.tech_line)
        return "  ".join(parts)


def _section_blocks(tex: str):
    """Yield (full_section_title, inner_body) for each rSection."""
    for m in re.finditer(r"\\begin\{rSection\}", tex):
        params, after = _take_braced_groups(tex, m.end(), 2)
        title = ("".join(params)).strip().lower()  # 'E'+'xperience' -> 'experience'
        end = tex.find(r"\end{rSection}", after)
        if end == -1:
            end = len(tex)
        yield title, tex[after:end]


def _entries_in(section_title: str, body: str) -> list[Entry]:
    entries = []
    for m in re.finditer(r"\\begin\{rSectionEntry\}", body):
        params, after = _take_braced_groups(body, m.end(), 5)
        raw_name = _strip_tex(params[0]) if params else "(unnamed)"
        name = re.split(r"\s*(?:---|—|\s-\s)\s*", raw_name, maxsplit=1)[0].strip()
        tech = _strip_tex(params[3]) if len(params) > 3 else ""
        end = body.find(r"\end{rSectionEntry}", after)
        if end == -1:
            end = len(body)
        chunk = body[after:end]
        bullets = []
        for raw in re.split(r"\\item", chunk):
            raw = raw.strip()
            if not raw or raw.startswith("["):   # skip the \item[] spacer
                continue
            bullets.append(re.sub(r"\s+", " ", raw))
        entries.append(Entry(name=name, section=section_title, bullets=bullets, tech_line=tech))
    return entries


def parse_resume(tex: str) -> ParsedResume:
    pr = ParsedResume()
    for title, body in _section_blocks(tex):
        if title.startswith("experience") or title.startswith("project"):
            pr.entries.extend(_entries_in(title, body))
        if title.startswith("technical skills") or title == "skills":
            for m in re.finditer(r"\\begin\{rSet\}", body):
                params, _ = _take_braced_groups(body, m.end(), 2)
                if len(params) < 2:
                    continue
                label = _strip_tex(params[0]).strip().lower()
                items = [_strip_tex(x) for x in _split_top_level_commas(params[1]) if x.strip()]
                pr.skills[label] = items
    return pr


# ============================================================================
#  GATES
# ============================================================================

@dataclass
class GateResult:
    name: str
    hard: bool
    passed: bool
    detail: str


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9+#. ]", "", s.lower()).strip()


def gate_required_languages(pr: ParsedResume, jd_langs, cand_langs) -> GateResult:
    """Every JD-listed language the candidate possesses MUST appear in Skills.
    Languages are never reconciled away and are never orphans (the inverse bug
    that deleted C++/Java). A JD language the candidate lacks is not required."""
    skills_langs = {_norm(x) for x in pr.skills.get("languages", [])}
    cand = {_norm(x) for x in cand_langs}
    required = {_norm(x) for x in jd_langs} & cand            # has + JD-listed
    missing = sorted(l for l in required if l not in skills_langs)
    if missing:
        return GateResult(
            "required_languages", True, False,
            f"JD-listed languages the candidate has but Skills omits: {missing}. "
            f"Mandatory inclusion — add to the Languages bucket.",
        )
    return GateResult("required_languages", True, True,
                      f"All JD languages the candidate has are present: {sorted(required)}.")


def gate_no_orphans(pr: ParsedResume, jd_required) -> GateResult:
    """A probe-worthy skill (framework / library / named technique) must appear
    in a bullet or tech-stack line, or be a JD-required keyword. Languages, OS,
    and VCS are exempt. Catches the orphaned PyTorch / RAG case."""
    body = _norm(pr.body_text())
    jd_req = {_norm(x) for x in jd_required}
    orphans = []
    for label, items in pr.skills.items():
        if label in EXEMPT_BUCKET_LABELS:
            continue
        for it in items:
            base = _norm(it.split("(")[0])           # 'AWS (EC2, S3, RDS)' -> 'aws'
            if not base or base in EXEMPT_SKILL_TOKENS:
                continue
            if base in body or base in jd_req:
                continue
            orphans.append(it)
    if orphans:
        return GateResult(
            "no_orphans", True, False,
            f"Skills-line items with no supporting bullet and not JD-required: "
            f"{orphans}. Drop them or select a backing entry.",
        )
    return GateResult("no_orphans", True, True, "No orphaned framework/library skills.")


def gate_no_bullet_deletion(pr: ParsedResume, iter1_counts, phase) -> GateResult:
    """No entry may drop below its iteration-1 bullet count, and no entry present
    at iteration 1 may be removed entirely. Stops the writer's degenerate response
    to a metric task (delete the metric-free bullet) AND the subtler exploit where
    deleting a whole metric-free entry RAISES the ratio (smaller denominator). The
    earlier `if name in cur` check silently skipped removed entries — that was the
    hole. Active in the loop only; the page-fit phase is allowed to drop one."""
    if phase != "loop" or not iter1_counts:
        return GateResult("no_bullet_deletion", True, True,
                          "Skipped (iteration 1 or fit-check phase).")
    cur = {e.name: len(e.bullets) for e in pr.entries}
    cur_norm = {_norm(k): v for k, v in cur.items()}
    shrunk, removed = [], []
    for name, base in iter1_counts.items():
        nk = _norm(name)
        if nk not in cur_norm:
            removed.append(name)
        elif cur_norm[nk] < base:
            shrunk.append(f"{name}: {base}->{cur_norm[nk]}")
    if shrunk or removed:
        parts = []
        if removed:
            parts.append(f"entries removed entirely: {removed}")
        if shrunk:
            parts.append(f"entries shrunk below baseline: {shrunk}")
        return GateResult(
            "no_bullet_deletion", True, False,
            "; ".join(parts) + ". Fix metric gaps by SWAPPING in a metric-bearing "
            "pool bullet, never by deleting a bullet or an entry. Removing a weak "
            "entry to lift the ratio is the exact exploit this gate exists to stop. "
            "If a pool has no metric, restore the content and mark it out-of-rails.",
        )
    return GateResult("no_bullet_deletion", True, True, "No entry shrank below baseline.")


def gate_min_entries(pr: ParsedResume, min_entries: int) -> GateResult:
    """Ratio floor. The metric ratio = metric-bearing / counted entries, so the
    field can be 'improved' by shrinking the denominator. A hard minimum on entry
    count removes that incentive at the root, including on iteration 1 where there
    is no baseline to compare against."""
    n = len(pr.entries)
    if n < min_entries:
        return GateResult(
            "min_entries", True, False,
            f"{n} Experience+Projects entries; floor is {min_entries}. A thin field "
            f"can game the metric-density ratio — restore entries to meet the floor.",
        )
    return GateResult("min_entries", True, True, f"{n} entries (floor {min_entries}).")


def gate_protected_depth(pr: ParsedResume, protected) -> GateResult:
    """Fix 3a: a role-critical entry may not be hollowed out to a single bullet.
    Directly catches the SEAS-lab-reduced-to-one-bullet regression. Protected
    entries are named by the orchestrator/persona (e.g. the autonomy lab on the
    robotics track) and must carry >= 2 bullets in any phase."""
    if not protected:
        return GateResult("protected_depth", True, True, "Skipped (no protected entries named).")
    prot = {_norm(x) for x in protected}
    cur = {_norm(e.name): len(e.bullets) for e in pr.entries}
    thin = []
    for name in protected:
        nk = _norm(name)
        if nk in cur and cur[nk] < 2:
            thin.append(f"{name}: {cur[nk]} bullet")
        elif nk not in cur:
            thin.append(f"{name}: absent")
    if thin:
        return GateResult(
            "protected_depth", True, False,
            f"Role-critical entries reduced below 2 bullets or dropped: {thin}. "
            f"These carry the role's core signal — keep them deep, cut elsewhere.",
        )
    return GateResult("protected_depth", True, True, "Protected entries retain depth.")


def gate_lead_signal(pr: ParsedResume, protected, window: int) -> GateResult:
    """Tuple/divergence gate. When the company's engineering identity diverges
    from the JD's screen track (e.g. a generic SWE req at an autonomy company),
    the orchestrator marks the differentiator-aligned entries as protected and
    sets `lead_signal_window` > 0. At least one protected entry must then appear
    within the top `window` entries (document order). This is the deterministic
    floor under the company-fit differentiator — it stops a full-stack spine from
    burying the autonomy entry at the bottom, which is exactly how the track flip
    produced an off-axis resume last round. The grader still judges *which*
    generalist entry leads; this only guarantees the differentiator is prominent,
    not buried."""
    if not window or not protected:
        return GateResult("lead_signal", True, True, "Skipped (no divergence / window=0).")
    prot = {_norm(x) for x in protected}
    top = pr.entries[:window]
    if any(_norm(e.name) in prot for e in top):
        present = [e.name for e in top if _norm(e.name) in prot]
        return GateResult("lead_signal", True, True,
                          f"Differentiator entry in top {window}: {present}.")
    return GateResult(
        "lead_signal", True, False,
        f"No differentiator/protected entry in the top {window} slots "
        f"(top {window}: {[e.name for e in top]}). The company-fit signal is buried; "
        f"move a protected entry up. Spine may lead, but the differentiator sits near it.",
    )


def gate_fit_protection(pr: ParsedResume, prefit_counts, protected, phase) -> GateResult:
    """Fix 3b: during the page-fit pass, drops must come from Projects only, and a
    protected entry may not shrink. Without this, a fit pass scoped to 'weakest
    project' can silently cut an Experience or lab bullet (which is what happened
    to the SEAS lab last round). Needs prefit_counts snapshotted by the
    orchestrator immediately before the fit pass."""
    if phase != "fit":
        return GateResult("fit_protection", True, True, "Skipped (loop phase).")
    if not prefit_counts:
        return GateResult("fit_protection", True, True, "Skipped (no pre-fit snapshot).")
    section = {_norm(e.name): e.section for e in pr.entries}
    cur = {_norm(e.name): len(e.bullets) for e in pr.entries}
    prot = {_norm(x) for x in (protected or [])}
    violations = []
    for name, base in prefit_counts.items():
        nk = _norm(name)
        shrank = (nk not in cur) or (cur[nk] < base)
        if not shrank:
            continue
        if section.get(nk, "").startswith("experience"):
            violations.append(f"experience entry cut in fit: {name}")
        elif nk in prot:
            violations.append(f"protected entry cut in fit: {name}")
    if violations:
        return GateResult(
            "fit_protection", True, False,
            f"{violations}. Page-fit drops come from non-protected PROJECT entries "
            f"only — never Experience, never a protected entry.",
        )
    return GateResult("fit_protection", True, True, "Fit drops were project-scoped and protected entries intact.")


def gate_page_fill(pr: ParsedResume, pdf_path, min_fill=0.85) -> GateResult:
    """Replaces the binary 1-page check. A resume can be one page and still waste
    a third of it — that reads as thin. Measure actual fill: exactly 1 page, and
    page-1 text must reach at least `min_fill` of the way down. Uses pdfplumber to
    find the lowest text baseline; falls back to a bullet-count floor when neither
    pdfplumber nor a PDF is available (length varies per bullet, so the count is a
    coarse proxy, used only when real measurement can't run)."""
    if pdf_path and Path(pdf_path).exists():
        try:
            import pdfplumber  # type: ignore
            with pdfplumber.open(pdf_path) as pdf:
                npages = len(pdf.pages)
                if npages != 1:
                    return GateResult("page_fill", True, False,
                                      f"{npages} pages; must be exactly 1 (overflow).")
                page = pdf.pages[0]
                bottoms = [c["bottom"] for c in page.chars] or [0]
                fill = max(bottoms) / float(page.height)
                if fill < min_fill:
                    return GateResult("page_fill", True, False,
                                      f"Page only {fill:.0%} filled (floor {min_fill:.0%}); "
                                      f"add a bullet to a strong entry's pool.")
                return GateResult("page_fill", True, True, f"One page, {fill:.0%} filled.")
        except ImportError:
            pass  # fall through to bullet-count proxy
        except Exception as e:
            return GateResult("page_fill", True, True, f"Skipped (PDF read error: {e}).")
    # Fallback: bullet-count floor (no pdfplumber / no PDF).
    total = sum(len(e.bullets) for e in pr.entries)
    floor = 10
    if total < floor:
        return GateResult("page_fill", True, False,
                          f"Only {total} bullets (floor {floor}); page likely underfilled. "
                          f"Install pdfplumber for true fill measurement.")
    return GateResult("page_fill", True, True,
                      f"{total} bullets (no pdfplumber; bullet-count proxy).")


def compute_metric_density(pr: ParsedResume, exempt_entries):
    """Informational only now. The 0-10 ceiling was retired with the demerit
    model — metric-free entries surface as `minor` defects in the grader instead.
    Still reported because the ratio and the metric-free list are useful for the
    writer and for debugging."""
    exempt = {_norm(x) for x in (exempt_entries or [])}
    counted, with_metric, metric_free, exempt_used = 0, 0, [], []
    for e in pr.entries:
        if _norm(e.name) in exempt:
            exempt_used.append(e.name)
            continue
        counted += 1
        if any(bullet_has_impact_metric(b) for b in e.bullets):
            with_metric += 1
        else:
            metric_free.append(e.name)
    ratio = (with_metric / counted) if counted else 1.0
    return round(ratio, 3), metric_free, exempt_used


# ============================================================================
#  DEMERIT SCORER  (merged from the former score_demerits.py)
#  Same deterministic layer as the artifact gates: takes the recruiter grader's
#  severity-tagged defect list and computes weighted demerits + display score.
#  No pass/fail threshold — the loop exits on zero demerits, writer peak, or timeout.
# ============================================================================

DEMERIT_WEIGHTS = {"emergency": None, "major": 3, "minor": 1}  # emergency = veto; no unscored tier
_DEMERIT_SEVERITIES = set(DEMERIT_WEIGHTS)
_DEPRECATED_SEVERITIES = {"patch"}  # legacy grader output; coerced to minor with warning


def score_demerits(defects, weights=DEMERIT_WEIGHTS):
    """Rules, all here and none in the model:
      - weighted = major*3 + minor*1
      - loop_target_met = no emergency AND weighted == 0
      - display score = max(0, 10 - weighted), cosmetic only.
    Unknown severity is coerced to `major` (fail-safe); deprecated `patch` -> `minor`.
    Both are surfaced in coerced_defects, never silent."""
    buckets = {k: [] for k in _DEMERIT_SEVERITIES}
    coerced = []
    for d in defects:
        sev = str(d.get("severity", "")).strip().lower()
        if sev in _DEPRECATED_SEVERITIES:
            coerced.append({**d, "original_severity": sev, "coerced_to": "minor"})
            sev = "minor"
        elif sev not in _DEMERIT_SEVERITIES:
            coerced.append({**d, "original_severity": sev or "(missing)", "coerced_to": "major"})
            sev = "major"
        buckets[sev].append(d)

    emergency = len(buckets["emergency"])
    weighted = (weights["major"] * len(buckets["major"])
                + weights["minor"] * len(buckets["minor"]))
    loop_target_met = emergency == 0 and weighted == 0
    return {
        "loop_target_met": loop_target_met,
        "weighted_demerits": weighted,
        "display_score": max(0.0, 10.0 - weighted),
        "counts": {k: len(v) for k, v in buckets.items()},
        "coerced_defects": coerced,
    }


def check_writer_loop_status(status: dict, defect_count: int) -> dict:
    """Validate writer_loop_status.json after a grading-response pass.
    `peak` is only valid when the writer documents what remains unfixable."""
    action = str(status.get("action", "")).strip().lower()
    if action not in ("continue", "peak"):
        return {
            "passed": False,
            "detail": f"action must be 'continue' or 'peak', got {action!r}",
        }
    oor = status.get("out_of_rails")
    if not isinstance(oor, list):
        return {"passed": False, "detail": "out_of_rails must be an array"}
    for i, item in enumerate(oor):
        if not isinstance(item, dict):
            return {"passed": False, "detail": f"out_of_rails[{i}] must be an object"}
        missing = [k for k in ("entry", "defect", "why") if k not in item]
        if missing:
            return {
                "passed": False,
                "detail": f"out_of_rails[{i}] missing keys: {missing}",
            }
    if action == "peak" and defect_count > 0 and not oor:
        return {
            "passed": False,
            "detail": "action is peak but out_of_rails is empty while defects remain",
        }
    return {"passed": True, "detail": f"action={action}, out_of_rails={len(oor)}"}


# ============================================================================
#  GRADER REPORT CHECK  (prose/JSON 1:1 — no unscored observations)
# ============================================================================

_WISHLIST_HEADER = "WHAT WOULD TAKE THIS TO THE NEXT LEVEL"
_DEFECTS_HEADER = "DEFECTS"


def _extract_json_block(text: str, after_header: str) -> dict:
    idx = text.upper().find(after_header.upper())
    if idx < 0:
        raise ValueError(f"missing {_DEFECTS_HEADER} section")
    fence = text.find("```json", idx)
    if fence < 0:
        raise ValueError("missing ```json fence in DEFECTS section")
    start = fence + len("```json")
    end = text.find("```", start)
    if end < 0:
        raise ValueError("unclosed ```json fence")
    return json.loads(text[start:end].strip())


def _extract_wishlist_bullets(text: str) -> list[str]:
    idx = text.upper().find(_WISHLIST_HEADER.upper())
    if idx < 0:
        raise ValueError(f"missing {_WISHLIST_HEADER} section")
    body = text[idx + len(_WISHLIST_HEADER):]
    stop_markers = ["LIKELIHOOD ESTIMATE", "━━━━━━━━"]
    stop = len(body)
    for marker in stop_markers:
        pos = body.upper().find(marker.upper())
        if pos >= 0:
            stop = min(stop, pos)
    section = body[:stop]
    return [ln.strip()[2:].strip() for ln in section.splitlines()
            if ln.strip().startswith("- ")]


def check_grader_report(text: str) -> dict:
    """Validate grader output: valid severities, wishlist count matches JSON defects."""
    data = _extract_json_block(text, _DEFECTS_HEADER)
    defects = data.get("defects", data if isinstance(data, list) else [])
    if not isinstance(defects, list):
        raise ValueError("defects must be a JSON array")

    invalid = []
    for i, d in enumerate(defects):
        sev = str(d.get("severity", "")).strip().lower()
        if sev in _DEPRECATED_SEVERITIES:
            invalid.append({"index": i, "severity": sev, "reason": "deprecated — use minor or omit"})
        elif sev not in _DEMERIT_SEVERITIES:
            invalid.append({"index": i, "severity": sev or "(missing)", "reason": "unknown severity"})

    wishlist = _extract_wishlist_bullets(text)
    mismatch = len(wishlist) != len(defects)
    return {
        "ok": not invalid and not mismatch,
        "defect_count": len(defects),
        "wishlist_count": len(wishlist),
        "invalid_severities": invalid,
        "wishlist_mismatch": mismatch,
    }


def run_check_report(args) -> int:
    text = Path(args.report).read_text(encoding="utf-8") if args.report != "-" else sys.stdin.read()
    try:
        result = check_grader_report(text)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL  check-report: {exc}", file=sys.stderr)
        return 1

    if result["ok"]:
        print(f"PASS  {result['defect_count']} defect(s), wishlist matches", file=sys.stderr)
        if args.out:
            Path(args.out).write_text(json.dumps(result, indent=2), encoding="utf-8")
        return 0

    print("FAIL  check-report:", file=sys.stderr)
    if result["invalid_severities"]:
        for item in result["invalid_severities"]:
            print(f"  invalid severity at index {item['index']}: "
                  f"{item['severity']} ({item['reason']})", file=sys.stderr)
    if result["wishlist_mismatch"]:
        print(f"  wishlist/JSON mismatch: {result['wishlist_count']} bullets vs "
              f"{result['defect_count']} defects", file=sys.stderr)
    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    return 1


# ============================================================================
#  MAIN  (subcommands: gates, demerits, check-report)
# ============================================================================

def run_gates(args) -> int:
    tex = Path(args.tex).read_text(encoding="utf-8")
    gi = json.loads(Path(args.inputs).read_text(encoding="utf-8"))
    pr = parse_resume(tex)

    gates = [
        gate_required_languages(pr, gi.get("jd_languages", []), gi.get("candidate_languages", [])),
        gate_no_orphans(pr, gi.get("jd_required_keywords", [])),
        gate_no_bullet_deletion(pr, gi.get("iter1_counts", {}), args.phase),
        gate_min_entries(pr, gi.get("min_entries", 4)),
        gate_protected_depth(pr, gi.get("protected_entries", [])),
        gate_lead_signal(pr, gi.get("protected_entries", []), gi.get("lead_signal_window", 0)),
        gate_fit_protection(pr, gi.get("prefit_counts", {}), gi.get("protected_entries", []), args.phase),
        gate_page_fill(pr, args.pdf, gi.get("min_fill", 0.85)),
    ]
    ratio, metric_free, exempt_used = compute_metric_density(pr, gi.get("exempt_entries", []))

    hard_pass = all(g.passed for g in gates if g.hard)
    report = {
        "hard_gates_pass": hard_pass,
        "metric_density": {
            "ratio": ratio,
            "metric_free_entries": metric_free,            # grader turns these into minors
            "exempt_entries_applied": exempt_used,          # logged so exemption can't hide
        },
        "gates": [asdict(g) for g in gates],
        "entries_parsed": [{"name": e.name, "section": e.section, "bullets": len(e.bullets)}
                           for e in pr.entries],
        "skills_parsed": pr.skills,
    }
    Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"hard_gates_pass = {hard_pass}", file=sys.stderr)
    for g in gates:
        print(f"  [{'PASS' if g.passed else 'FAIL'}] {g.name}: {g.detail}", file=sys.stderr)
    print(f"  metric ratio = {ratio} (metric-free: {metric_free or 'none'})", file=sys.stderr)
    return 0 if hard_pass else 1


def run_demerits(args) -> int:
    raw = json.loads(Path(args.demerits).read_text(encoding="utf-8"))
    defects = raw.get("defects", raw if isinstance(raw, list) else [])
    result = score_demerits(defects)
    Path(args.out).write_text(json.dumps(result, indent=2), encoding="utf-8")

    c = result["counts"]
    print(f"weighted={result['weighted_demerits']}  "
          f"display={result['display_score']:.1f}  "
          f"loop_target={'met' if result['loop_target_met'] else 'open'}", file=sys.stderr)
    print(f"  emergency={c['emergency']} major={c['major']} "
          f"minor={c['minor']}", file=sys.stderr)
    if result["coerced_defects"]:
        print(f"  WARNING: {len(result['coerced_defects'])} defect(s) had an unknown "
              f"severity, scored as major", file=sys.stderr)
    return 0


def run_writer_loop(args) -> int:
    status = json.loads(Path(args.status).read_text(encoding="utf-8"))
    defect_count = 0
    if args.demerits:
        raw = json.loads(Path(args.demerits).read_text(encoding="utf-8"))
        defect_count = len(raw.get("defects", raw if isinstance(raw, list) else []))
    result = check_writer_loop_status(status, defect_count)
    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{'PASS' if result['passed'] else 'FAIL'}  {result['detail']}", file=sys.stderr)
    return 0 if result["passed"] else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic resume checks: artifact gates and demerit scoring.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("gates", help="run the artifact gates against the .tex/.pdf")
    g.add_argument("--tex", required=True)
    g.add_argument("--inputs", required=True, help="gate_inputs.json")
    g.add_argument("--pdf", default="")
    g.add_argument("--phase", default="loop", choices=["loop", "fit"])
    g.add_argument("--out", default="gate_report.json")
    g.set_defaults(func=run_gates)

    d = sub.add_parser("demerits", help="score the grader's defect list (informational)")
    d.add_argument("--demerits", required=True, help="grader-emitted defect JSON")
    d.add_argument("--out", default="demerit_score.json")
    d.set_defaults(func=run_demerits)

    c = sub.add_parser("check-report", help="verify grader prose matches defect JSON")
    c.add_argument("--report", required=True,
                   help="grader report path, or '-' for stdin")
    c.add_argument("--out", default="", help="optional JSON result path")
    c.set_defaults(func=run_check_report)

    w = sub.add_parser("writer-loop", help="validate writer_loop_status.json after a grading pass")
    w.add_argument("--status", required=True, help="writer_loop_status.json")
    w.add_argument("--demerits", default="", help="current demerits.json (for peak validation)")
    w.add_argument("--out", default="", help="optional JSON result path")
    w.set_defaults(func=run_writer_loop)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())