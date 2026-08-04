# Software Engineer — Technology Internship Program (Summer 2027) at Capital One

**Note:** Screen grade of the JD-tailored `resume.tex` in this folder (MatchStream swapped in for Java/Spring/SQL coverage, per `full-stack-track.tex` base). Single grading pass, no writer loop run.

## Verdict

- **Score:** 0.0 / 10 (13 weighted demerits — 0 emergency, 2 major, 7 minor) — see note below; the grader's own qualitative read is materially more favorable than this cosmetic number.
- **Eligibility:** Eligible — basic quals are degree-timeline/continuing-enrollment only; no sponsorship needed, no stated conflict.
- **Track:** full-stack (general SWE); JD adds a soft AI-tooling-fluency differentiator, no divergence from the base track.
- **Pipeline:** 1 grading pass (no writer loop run) — this is the already-tailored Capital One resume, not the base track.

**On the 0.0 display score:** `scripts/validate.py`'s demerit weighting floors at 0 once weighted demerits ≥ 10, and this list hits 13 (2×major=6 + 7×minor=7) purely on volume of *minor* dings, not severity. The doctrine itself flags this number as cosmetic-only. The grader rated **Resume Screen Pass: High** — every named screen criterion is hit at least minimally and there is zero emergency-tier defect. Read the defect list, not the number.

## Screen Review

### First read

- Every named screen criterion (frontend, backend/API, database, Java, cloud/CI-CD, trade-off fluency, GitHub proof) is hit at least minimally — no criterion is wholly absent.
- The two majors are both **dates/consistency** issues, not content gaps: Vylet carries the resume's biggest claims (live product, revenue, client count) with no date field anywhere in the entry, and CaseStudyPrep.AI's co-op title overlaps four months with MDC's "sole engineer" framing with no part-time indication on either.
- The minors cluster around under-substantiation on the newest entry (MatchStream): PostgreSQL named in the tech line but never used in a bullet, no repo link to back the load-test numbers, and a raw JUnit test count standing in for an impact metric.

### Demerits

- **major** · `Vylet` · no date/duration anywhere in the entry — the resume's most heavily weighted entry (lead position, live-revenue claims) is the only experience entry with no timeframe, leaving the flagship claim's window unverifiable next to two dated entries beside it.
- **major** · `resume` · CaseStudyPrep.AI (Dec 2025 – May 2026) and MDC (Jan 2026 – May 2026, "sole engineer") fully overlap four months with no part-time indication on either — reads as an internal inconsistency the reader has to resolve unaided.
- **minor** · `Vylet` · zero frontend/client-facing evidence in the lead entry — an all-backend/data/infra lead entry means the frontend signal this JD screens for doesn't surface until the second experience entry.
- **minor** · `MatchStream` · PostgreSQL named in the tech-stack line with no supporting bullet — no bullet describes a schema, query, or persistence decision, so it reads as a keyword.
- **minor** · `MatchStream` · no GitHub or live link — the load-test numbers (2,500 msg/sec, sub-8ms p99, zero data loss across dropout events) are unverifiable without one.
- **minor** · `MatchStream` · "Wrote 52 JUnit tests" is a count metric, not an impact metric — reads closer to the rejected vanity-metric category than the latency/throughput numbers elsewhere in the same entry.
- **minor** · `Education` · coursework line includes Calc III and Intro to Statistics — irrelevant to a full-stack JD with no ML/data-science ask; reads as a course dump.
- **minor** · `resume` · zero evidence of AI-assisted development tooling — the JD distinctively and repeatedly calls this out as a differentiator ("beyond basic code completion"); the page shows AI *products* being built (Gemini embeddings, LangGraph) but never the candidate using AI tooling in their own workflow.
- **minor** · `resume` · bullets routinely exceed the two-line economy standard — Vylet, MatchStream, and CaseStudyPrep bullets chain clauses into 3+ line blocks, slowing the 7-second scan on the entries doing the most work.

### Misreads

- A reader could read the Vylet/CaseStudyPrep/MDC date picture as three overlapping full-time claims rather than a defensible course-load-compatible schedule, since nothing on the page states otherwise.
- MatchStream's PostgreSQL + no-link combination could read as "database name-dropped for the JD," even though the entry's other two bullets are genuinely metric-dense.

### Interview angles

- **Lead with:** Vylet's Dockerized LangGraph pipeline + Gemini-embeddings asyncpg data layer — real persistence-layer and backend-ownership signal that directly answers this JD's "backend services... Big Data" framing, plus the $1,500 MRR/3-client growth as concrete product ownership.
- **Defend:** be ready to state Vylet's actual timeframe verbally (the grader flagged its absence on the page) and to explain the CaseStudyPrep/MDC overlap as a deliberate concurrent part-time schedule — have the real hours/week ready rather than letting the interviewer infer overcommitment.
- **Depth prep:** MatchStream's NetworkTables4 ingestion service (2,500 msg/sec, p99 <8ms) as the Java/Spring backend-rigor story if pressed on the JD's Java/Big-Data language; be ready to describe the (currently unstated) PostgreSQL schema/query pattern by name, since the resume doesn't show it.

## Likelihood

- **Resume screen:** High — every named screen criterion is hit at least minimally and there is no emergency-tier defect at a screen the persona (grounded in `companies.md`) describes as school-blind hygiene, not a stack-rank.
- **Overall hire odds:** Low-Medium — per `recruiting.md` Part I §1 and the Capital One row in `companies.md` (CodeSignal OA, ~8–12% overall conversion), the binding gate at this scale is the OA, not the resume; the resume mainly buys team-match after clearing it. `TRACKER.md` has zero logged applications, so this is doctrine-driven, not track-record-calibrated.
- **Funnel filters:** School-blind screen, CodeSignal OA, bottleneck at OA per `companies.md`.
- **Outside the resume:** OA prep (pattern-based DS&A, timed mediums) is the highest-leverage spend given the OA is the dominant filter here; apply in the first wave per `recruiting.md` §8 — this matters more for getting the OA invite at all than further resume polish.
