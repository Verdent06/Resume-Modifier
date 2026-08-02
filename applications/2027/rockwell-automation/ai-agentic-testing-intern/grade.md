# AI Center of Excellence Intern (Agentic AI for PLC Testing) at Rockwell Automation

**Note:** This is a screen-only grade of the existing base `ai-ml-track` resume (not a JD-tailored pipeline run) — no writer loop, no `TRACKER.md` entry unless this becomes an actual application.

## Verdict

- **Score:** 4.0 / 10 (6 weighted demerits — 0 emergency, 1 major, 3 minor)
- **Eligibility:** Eligible — only stated requirement is active enrollment in a bachelor's/advanced degree program; candidate meets this.
- **Track:** ai-ml + industrial-automation/safety-critical differentiator (track_divergence)
- **Pipeline:** 1 grading pass (no writer loop run) · this is the base track resume, unmodified for this JD

## Screen Review

### First read

- The Vylet lead entry is an unusually strong direct hit — a LangGraph pipeline plus a genuine adversarial eval harness with a faithfulness metric (50% → 90%) — which is close to exactly what "generate test plans and validate" looks like in miniature.
- The resume never uses the words "agent" or "agentic" anywhere, despite the role's title and every responsibility bullet being built around agentic AI — the match is there in substance but not stated.
- The third Experience entry (Michigan Data Consulting) is pure ETL/backend work with zero AI, testing, or fault-reasoning content, diluting an otherwise on-target page.

### Demerits

- **major** · `Michigan Data Consulting (MDC)` · off-axis entry, no AI/testing signal — pure ETL/backend data engineering with zero agentic AI, LLM, evaluation, or fault-reasoning content, in the weakest slot of a 3-entry Experience section for a role that screens almost entirely on AI research substance.
- **minor** · `resume` · "agentic"/"agent" terminology never appears — the role is literally titled "Agentic AI" and the screen tests for that exact construction, but the strongest entry describes a LangGraph pipeline without ever naming it as agentic work.
- **minor** · `Granular Synthesizer Plugin` · single bullet, no metric — deep real-time audio-thread engineering detail with no quantification (latency, buffer size, CPU load), reading softer than the quantified entries above it.
- **minor** · `resume` · industrial/safety-critical differentiator has weak, indirect evidence — the closest analogs to PLC/simulation/safety-critical work are audio real-time constraints and web-app fault-tolerance; the reader has to infer the transfer rather than see it stated.

### Misreads

- A rushed recruiter skimming for "agentic" as a literal keyword could miss that the Vylet entry is agentic work at all, since the term never appears on the page.
- The MDC entry could read as "this candidate does generic data engineering," diluting the otherwise research-relevant signal from the other two entries.

### Interview angles

- **Lead with:** the Vylet LangGraph pipeline + LangSmith eval harness (20 adversarial test cases, 13 archetype labels, 50%→90% faithfulness) — directly analogous to "generate test plans, identify corner cases, evaluate against non-obvious failure modes."
- **Defend:** no PLC/industrial/simulation exposure — be ready to name the transferable skill explicitly (agentic pipeline design + adversarial eval construction generalizes to fault-injection/corner-case test generation regardless of domain) rather than waiting for the interviewer to make that leap.
- **Depth prep:** how the Pydantic consensus gates and asyncpg data layer would extend to formal-verification-style reasoning; the granular synthesizer's real-time constraint work as a proxy for safety-critical/fault-tolerant systems thinking if pressed on "safety-critical systems" experience.

## Likelihood

- **Resume screen:** High — the lead entry is an unusually strong direct hit on both core screen criteria (agentic LLM pipeline + genuine adversarial eval harness with a faithfulness metric), and nothing on the page contradicts that beyond one off-axis third entry.
- **Overall hire odds:** Medium — this is a small, research-flavored team reading resumes directly (not a high-volume OA funnel), so the document carries most of the weight versus at big-tech pipelines, but a niche CoE research seat likely draws candidates with grad-adjacent or formal-methods backgrounds this resume doesn't claim; the interview loop will probe agentic-system depth and fault/safety reasoning hard given the explicit research framing.
- **Funnel filters:** No stated OA — Rockwell doctrine row does not exist in `reference/companies.md`; treat as a small technical-team read, not a high-volume ATS funnel.
- **Outside the resume:** A warm intro to the Director of AI or a team member would matter disproportionately for a small research team; since there's no OA gate, prep "walk me through the eval pipeline's failure modes" over DS&A grinding.
