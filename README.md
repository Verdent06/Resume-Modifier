# Resume Pipeline

An agent-based system that turns a job description into a role-specific resume and a structured pre-interview grade report — fast, honestly, with minimal stylistic drift. Doctrine lives in markdown; behavior lives in thin Cursor rules; deterministic checks live in Python.

---

## Repository Layout

```
resume/
├── README.md
├── context.md              ← your experiences, bullet pool, swap sets (you edit)
├── network.md              ← contacts for referrals and outreach (you edit)
│
├── reference/              ← curated knowledge agents read
│   ├── recruiting.md       ← how hiring works (read-only)
│   ├── resume.md           ← resume doctrine (read-only)
│   └── companies.md        ← company tiers, processes, notes
│
├── scripts/
│   ├── validate.py         ← artifact gates, demerit scoring, report check
│   └── cleanup.py          ← LaTeX junk, .pipeline/, legacy JSON
│
├── .cursor/rules/          ← thin agent coordinators (no doctrine inline)
│   ├── career-coach.mdc
│   ├── resume-pipeline.mdc
│   ├── resume-writing.mdc
│   └── resume-grading.mdc
│
└── applications/
    ├── template.tex
    ├── template.cls
    └── {year}/
        ├── TRACKER.md
        └── {company}/
            ├── company.md
            └── {role}/
                ├── persona.md
                ├── Ankur Desai Resume.tex
                ├── Ankur Desai Resume.pdf
                └── grade.md          ← canonical screen review + likelihood
```

**What you touch:** `context.md` and `network.md`.

**What ships per application:** `persona.md`, `.tex`, `.pdf`, and `grade.md` only — no `.aux`/`.log`, no `.pipeline/`, no standalone JSON.

---

## The Two-Layer Design

**Reference (markdown):** agents read on demand; rules never inline doctrine.

**Behavior (`.cursor/rules/`):** coordinators that dispatch work and run scripts.

**Determinism (`scripts/`):** anything that is a pure function of (resume, JD, pool) is code, not LLM judgment.

| Agent | Role |
|-------|------|
| `career-coach.mdc` | Always-on coordinator; strategy, company questions, dispatches pipeline/grader |
| `resume-pipeline.mdc` | Parse JD → persona → write/validate/grade loop → `grade.md` |
| `resume-writing.mdc` | Mechanical bullet selection from `context.md`; no invented prose |
| `resume-grading.mdc` | Blind recruiter; emits severity-tagged defect list |

---

## Core Design Decisions

1. **Doctrine is referenced, not embedded.** `reference/recruiting.md` and `reference/resume.md` are read-only unless you explicitly say otherwise.

2. **Writer is mechanical.** Bullets are copied verbatim from `context.md`; tech changes only via swap sets.

3. **Grader is blind to the pool.** It reads the `.tex` + `persona.md` (recruiter lens) + `reference/` — never `context.md`. It judges the shipped page against abstract screen criteria, not a hidden targeting plan.

4. **Writer has two modes.** **Initial:** construct from `context.md` lanes + persona lens (no defects yet). **Grading-response:** defects JSON is primary; persona only interprets grader language.

5. **Demerit model, not anchored grades.** Emergencies (veto), majors (×3), minors (×1). Weighted total and display score (`10 − weighted`) are informational in `grade.md`. Loop exits on zero demerits, writer peak, or timeout — no pass threshold.

6. **Prose and score cannot diverge.** Every observation in the grader report must appear in the scored defects JSON. `check-report` enforces 1:1 before scoring.

7. **`grade.md` is the deliverable.** Verdict, screen review (demerits, misreads, interview angles), and likelihood — folded from what used to be four JSON files. Mechanical gates and persona stay out of the report (`persona.md`; validator audit in `.pipeline/` until ship).

8. **One skeleton.** `applications/template.tex` for every track; track is a routing label into `reference/` sections.

---

## End-to-End Flow

1. Paste a JD (or ask the coach — it routes to the pipeline).
2. Orchestrator parses role → `screen_track` + `differentiator` → eligibility (computed, not reasoned).
3. Resolve `company.md`, build `persona.md`, copy skeleton template.
4. Writer **initial** pass from persona lens + `context.md` lanes + doctrine; orchestrator snapshots `iter1_counts` and writes `.pipeline/gate_inputs.json`.
5. **Loop** (cap 10 — timeout if neither zero demerits nor writer peak):
   - `xelatex` → `cleanup.py clean`
   - `validate.py gates` — hard gates must pass before grading
   - `@resume-grading` → `check-report` → `validate.py demerits`
   - Writer **grading-response** (defects JSON primary) → `writer_loop_status.json` → `validate.py writer-loop`
   - Exit only on `loop_target_met`, writer `peak`, or timeout at 10
6. **Fit checks** (if hard gates pass — skills wrap, page fill).
7. Final grade pass → assemble `grade.md` → `cleanup.py clean --ship`.
8. Append `TRACKER.md` (new row + recomputed summary stats).

---

## Scripts

Run from repo root:

```bash
.venv/bin/python scripts/validate.py …
```

### `scripts/validate.py`

| Subcommand | Purpose |
|------------|---------|
| `gates` | Required languages, orphans, anti-deletion, protected depth, lead signal, page fill |
| `demerits` | Score grader defect JSON → weighted total, `loop_target_met`, display score |
| `writer-loop` | Validate `writer_loop_status.json` after a grading-response pass |
| `check-report` | Wishlist bullet count must match JSON defects; no deprecated severities |

```bash
.venv/bin/python scripts/validate.py gates \
  --tex "applications/2027/foo/bar/Ankur Desai Resume.tex" \
  --inputs applications/2027/foo/bar/.pipeline/gate_inputs.json \
  --pdf "applications/2027/foo/bar/Ankur Desai Resume.pdf" \
  --phase loop \
  --out applications/2027/foo/bar/.pipeline/gate_report.json

.venv/bin/python scripts/validate.py check-report --report grader_output.txt
.venv/bin/python scripts/validate.py demerits \
  --demerits applications/2027/foo/bar/.pipeline/demerits.json \
  --out applications/2027/foo/bar/.pipeline/demerit_score.json

.venv/bin/python scripts/validate.py writer-loop \
  --status applications/2027/foo/bar/.pipeline/writer_loop_status.json \
  --demerits applications/2027/foo/bar/.pipeline/demerits.json
```

### `scripts/cleanup.py`

| Subcommand | Purpose |
|------------|---------|
| `clean --tex` | Remove `.aux`, `.log`, `.out`, etc.; keep `.tex` and `.pdf` |
| `clean --tex --ship` | Above + `.pipeline/` + legacy standalone JSON |
| `clean-tree --root applications` | Recursive maintenance across all role folders |

```bash
.venv/bin/python scripts/cleanup.py clean --tex "applications/…/Ankur Desai Resume.tex"
.venv/bin/python scripts/cleanup.py clean-tree --root applications
```

---

## Setup

- **TeX:** `xelatex` on PATH
- **Python:**

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

---

## Data Boundaries

| File | Contents |
|------|----------|
| `context.md` | Candidate state only — policy text here is a bug |
| `network.md` | Contacts |
| `reference/recruiting.md` | Field + recruiting doctrine (read-only) |
| `reference/resume.md` | Resume doctrine (read-only) |
| `reference/companies.md` | Company operational data |
| `persona.md` | Per-role recruiter lens — bar, track, abstract screen criteria (no entry names) |
| `grade.md` | Final verdict, screen review, likelihood |

---

## Practical Limitations

- The writer can only close gaps representable via the bullet pool + swap sets. Structural mismatches surface inline under **Defend** in `grade.md` as *(out of rails: …)*.
- Weighted demerits and display score in `grade.md` describe resume-screen quality — not a guarantee past OA/onsite.
- Historical `grade.md` / `company.md` files may cite old paths (`companies.md`); live rules use `reference/companies.md`.

---

## Usage

1. Paste a complete JD in chat, or ask a strategy / company / resume question.
2. The pipeline runs in Agent mode.
3. Review the role folder: `persona.md`, `.tex`, `.pdf`, **`grade.md`**.
4. Confirm the tracker entry was appended and summary stats were updated.
