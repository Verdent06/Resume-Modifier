# Resume Pipeline

An agent-based system that turns a job description into a role-specific resume, fast and honestly, with minimal stylistic drift. Doctrine lives in a markdown knowledge base; the rules are thin coordinators that reference it.

---

## The Two-Layer Design

**Knowledge (markdown, human-curated):**
- `knowledge.md` — how the field and recruiting work: funnel, timeline, networking, interview loop, negotiation, and the four industry tracks (general SWE, DevOps, AI/ML, robotics).
- `resume.md` — the resume document: ATS/AI parsing, structure/hierarchy, the DRAW/AR bullet doctrine, per-track resume emphasis.
- `companies.md` — company-specific operational data: tiers, interview process, OA platform, bottlenecks.
- `context.md` — candidate state only: identity, education, experiences/projects, the bullet pool, swap sets, skills inventory, targets.

**Behavior (`.cursor/rules/`, thin coordinators):**
- `career-coach.mdc` (always on) — the coordinator/coach. Answers strategy and resume questions by reading the knowledge base + current web data; dispatches the agents below.
- `resume-pipeline.mdc` — orchestrator: parse JD → build persona → dispatch → loop → persist.
- `resume-writing.mdc` — mechanical selector over `context.md`, grounded in `resume.md` doctrine.
- `resume-grading.mdc` — blind recruiter simulation, evaluates against `resume.md`, calibrates odds with `knowledge.md`.

**The rule of the system:** rules own process and mechanics; the markdown files own doctrine. Rules *reference* the files on demand and never inline or duplicate their content.

---

## Core Design Decisions

1. **Doctrine is referenced, not embedded.** Recruiting and resume knowledge live in `knowledge.md`/`resume.md`. Rules point at them; they hold no doctrine of their own. This keeps a single source of truth and prevents drift.

2. **Read-only doctrine.** `knowledge.md` and `resume.md` are **never edited by any agent** unless the user explicitly says so. Only `context.md` (candidate state) and `companies.md` (company data) are agent-writable.

3. **One skeleton template.** `applications/template.tex` is the single resume skeleton, sitting beside `applications/template.cls`. Track (full-stack / ai-ml / dev-ops / robotics) is a doctrine-routing label that selects which `resume.md`/`knowledge.md` section grounds the work — not a separate file. The writer fills the same skeleton for every track.

4. **Writer is mechanical, not creative.** Bullets are copied verbatim from `context.md`; tech changes only via explicit swap sets; no invented metrics or prose. *Which* selection is strongest is decided by `resume.md`, applied through selection only.

5. **Grader is blind to the pool, not to doctrine.** It reads the `.tex` + `persona.md` + `resume.md` + `knowledge.md`, and never `context.md`. It outputs one grade and a lean, executable task-action resolution list.

6. **Loop is short and harsh.** Max 3 iterations, exit at `8.25`. The grade gates; the resolution tasks are the product.

7. **Persona is the per-role briefing.** `persona.md` consolidates role facts, ATS terms, and recruiter framing, grounded in the doctrine files, and is read by both writer and grader.

---

## Repository Layout

```
resume/
├── README.md
├── context.md            ← candidate state (agent-writable: coach)
├── knowledge.md          ← field doctrine (read-only)
├── resume.md             ← resume doctrine (read-only)
├── companies.md          ← company data (agent-writable: coach)
│
└── applications/
    ├── template.cls        ← resume class (read-only)
    ├── template.tex      ← single skeleton; copied, never edited in place
    └── {year}/
        ├── TRACKER.md
        └── {company}/
            ├── company.md            ← write-once per company
            └── {role}/
                ├── persona.md
                ├── Ankur Desai Resume.tex
                ├── Ankur Desai Resume.pdf
                └── grade.md           ← final grading report only
```

---

## Agent Contracts

### Coach (`career-coach.mdc`)
Always-on coordinator. Reads the four markdown sources + the web; routes strategy → `knowledge.md`, resume questions → `resume.md`, company specifics → `companies.md`, candidate state → `context.md`. Dispatches the pipeline/grader; never writes or grades itself.

### Orchestrator (`resume-pipeline.mdc`)
Parses the JD (track + lifecycle stage from the posting), resolves `company.md`, builds the doctrine-grounded `persona.md`, copies `applications/template.tex` (fixing the class path for folder depth), runs the write/grade loop, compiles, persists, appends the tracker. Never edits content or scores.

### Writer (`resume-writing.mdc`)
Reads `context.md`, `resume.md`, `persona.md`, the working `.tex`, and (iteration > 1) the grading report. Fills the skeleton: selects bullets, swaps within sets, picks skills buckets, orders by impact density per `resume.md`. Cannot rewrite prose, invent anything, or edit the doctrine files, `template.tex`, `template.cls`, or education.

### Grader (`resume-grading.mdc`)
Reads `persona.md`, the `.tex`, `resume.md`, `knowledge.md`. Adopts the role persona, scores `0.0-10.0`, and emits a task-action resolution list. Blind to `context.md` and the bullet pool.

---

## End-to-End Flow

1. User provides a JD (or the coach detects one).
2. Orchestrator parses role → chooses track label + lifecycle stage.
3. Orchestrator builds the application folder, `company.md`, and a doctrine-grounded `persona.md`.
4. Writer fills the skeleton on the first pass.
5. Grader scores and emits resolution tasks.
6. Writer addresses in-rails tasks.
7. Repeat (max 3) until grade `>= 8.25` or cap.
8. Compile PDF, run fit checks, persist final `grade.md`.
9. Append the tracker entry.

---

## Data Boundaries

- `context.md`: timeless candidate state only. Policy/doctrine text here is a scoping bug.
- `knowledge.md` / `resume.md`: doctrine, read-only.
- `companies.md`: company data, coach-writable.
- `persona.md`: per-role framing, orchestrator-generated.
- `.mdc` files: behavior and control logic, no doctrine.

---

## Practical Limitations

- The writer can only close gaps representable via the existing pool + swap sets. Some role mismatches are structural and the loop caps out below threshold.
- A high score means the artifact is strong for the resume-screen stage; it does not guarantee an interview.
- The robotics track routes doctrine but fills the same skeleton; if robotics volume grows, consider a dedicated bullet emphasis in `context.md`.
- Manual review is still expected for final polish and page-fit edge cases.

---

## Usage

1. Paste a complete JD in chat (or ask a strategy/company/resume question — the coach routes it).
2. The pipeline runs in Agent mode.
3. Review the role folder: `persona.md`, `Ankur Desai Resume.tex`, `Ankur Desai Resume.pdf`, `grade.md`.
4. Confirm the tracker entry was appended.