#!/usr/bin/env python3
"""
validate.py — deterministic resume gates for the resume pipeline.

Runs between the writer and the grader, on the compiled artifact. Produces a
pass/fail gate report plus computed values (metric-density ratio, clamp
ceiling) that the grader is HANDED rather than asked to compute. The
orchestrator treats this report as ground truth:

  - it does not let the write/grade loop exit while a hard gate fails, and
  - it caps the grader's number at the computed ceiling.

The model never runs these checks. That is the entire point. Every regression
this thread produced — C++ vanishing from Skills, the metric clamp not firing,
the writer deleting bullets to satisfy a metric task — is a pure function of
(resume, JD, pool) and therefore belongs here, in code, not in an .mdc prose
instruction a stochastic agent can fudge.

USAGE
    python validate.py \
        --tex "applications/2027/anduril-industries/software-engineer-intern/Ankur Desai Resume.tex" \
        --inputs gate_inputs.json \
        --pdf  "applications/2027/anduril-industries/software-engineer-intern/Ankur Desai Resume.pdf" \
        --phase loop \
        --out  gate_report.json

  exit 0  -> all HARD gates pass (loop may proceed to grading)
  exit 1  -> at least one HARD gate failed (orchestrator must re-dispatch writer)

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


def gate_page_fit(pdf_path) -> GateResult:
    if not pdf_path:
        return GateResult("page_fit", True, True, "Skipped (no PDF supplied).")
    p = Path(pdf_path)
    if not p.exists():
        return GateResult("page_fit", True, True, f"Skipped (PDF not found: {pdf_path}).")
    pages = None
    try:
        from pypdf import PdfReader  # type: ignore
        pages = len(PdfReader(str(p)).pages)
    except Exception:
        try:
            import subprocess
            out = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True)
            for line in out.stdout.splitlines():
                if line.lower().startswith("pages:"):
                    pages = int(line.split(":")[1].strip())
        except Exception:
            return GateResult("page_fit", True, True,
                              "Skipped (no pypdf and no pdfinfo available).")
    if pages is None:
        return GateResult("page_fit", True, True, "Skipped (could not read page count).")
    if pages != 1:
        return GateResult("page_fit", True, False, f"Resume is {pages} pages; must be exactly 1.")
    return GateResult("page_fit", True, True, "One page.")


def compute_metric_density(pr: ParsedResume, exempt_entries):
    """Soft gate: returns (ratio, ceiling, metric_free, exempt_used). Does not
    block the loop; the orchestrator hands `ceiling` to the grader as a hard cap
    it cannot exceed. Edit-H arithmetic, now actually arithmetic."""
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
    ceiling = 8.0 if ratio < 0.5 else 10.0
    return round(ratio, 3), ceiling, metric_free, exempt_used


# ============================================================================
#  MAIN
# ============================================================================

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tex", required=True)
    ap.add_argument("--inputs", required=True, help="gate_inputs.json")
    ap.add_argument("--pdf", default="")
    ap.add_argument("--phase", default="loop", choices=["loop", "fit"])
    ap.add_argument("--out", default="gate_report.json")
    args = ap.parse_args()

    tex = Path(args.tex).read_text(encoding="utf-8")
    gi = json.loads(Path(args.inputs).read_text(encoding="utf-8"))
    pr = parse_resume(tex)

    gates = [
        gate_required_languages(pr, gi.get("jd_languages", []), gi.get("candidate_languages", [])),
        gate_no_orphans(pr, gi.get("jd_required_keywords", [])),
        gate_no_bullet_deletion(pr, gi.get("iter1_counts", {}), args.phase),
        gate_min_entries(pr, gi.get("min_entries", 4)),
        gate_protected_depth(pr, gi.get("protected_entries", [])),
        gate_fit_protection(pr, gi.get("prefit_counts", {}), gi.get("protected_entries", []), args.phase),
        gate_page_fit(args.pdf),
    ]
    ratio, ceiling, metric_free, exempt_used = compute_metric_density(pr, gi.get("exempt_entries", []))

    hard_pass = all(g.passed for g in gates if g.hard)
    report = {
        "hard_gates_pass": hard_pass,
        "metric_density": {
            "ratio": ratio,
            "clamp_ceiling": ceiling,
            "metric_free_entries": metric_free,
            "exempt_entries_applied": exempt_used,  # logged so exemption can't hide
        },
        "gates": [asdict(g) for g in gates],
        "entries_parsed": [{"name": e.name, "section": e.section, "bullets": len(e.bullets)}
                           for e in pr.entries],
        "skills_parsed": pr.skills,
    }
    Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Human-readable summary to stderr (orchestrator reads the JSON).
    print(f"hard_gates_pass = {hard_pass}", file=sys.stderr)
    for g in gates:
        print(f"  [{'PASS' if g.passed else 'FAIL'}] {g.name}: {g.detail}", file=sys.stderr)
    print(f"  metric ratio = {ratio}  ->  grader ceiling = {ceiling}", file=sys.stderr)
    if metric_free:
        print(f"  metric-free entries: {metric_free}", file=sys.stderr)

    return 0 if hard_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())