# Software Development Co-op - AI Assisted at Nokia

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 1 major, 0 minor)
- **Eligibility:** eligible — currently pursuing UMich B.S. CS (Expected May 2028) during Jan–May 2027; JD has no GPA or class-year floor; US citizen (JD offers no sponsorship)
- **Track:** full-stack + Core Networks / telecom / AI-assisted PDLC
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- A 30-second Core Networks screen sees a founder-led LangGraph/LangSmith/eval pipeline, a FastAPI + Docker/GitHub Actions project, and Python on the stack line — on-axis for AI-assisted SWE tooling, not router C++ and not TensorFlow research.
- Binding ding: Go is a JD-required language and is nowhere on the page.
- Education parses cleanly (`Expected May 2028`, GPA 3.66); one Winter 2027 seat, onsite Sunnyvale, no reloc.

### Demerits

- **major** · `resume` · Go absent — JD names basic programming skills in Python and Go as a pair; Python appears in Skills and on the SignalWeaver stack line, Go does not appear anywhere on the page, so the second required language is a complete miss at screen.

### Misreads

- A rushed screener can bucket this as a PE/search-fund founder resume (Vylet lead-sourcing) and miss that the same entry is the agent-workflow / eval / Docker proof the co-op actually tests.

### Interview angles

- **Lead with:** Vylet — Dockerized LangGraph pipeline (30 scored leads / 30 min, 30x), LangSmith eval (faithfulness 50% → 90% on 20 adversarial cases), named defect 79% → 89% qualification. SignalWeaver — 5-node LangGraph + FastAPI (9.1s p50 / 15.2s p99) + Docker Compose / GitHub Actions pytest. MDC — Flask REST on AWS EC2 and Pandas ETL (~800 hours / 400 PACs) as the shipped-service analog.
- **Defend:** Go gap → honest: interview in Python; do not claim Go *(out of rails: pool has no Go bullet; swap sets cannot bridge; Skills cannot list it)*. No Kubernetes, B-MAD, Loop Engineering, Copilot, or Nokia employment. CaseStudyPrep is voice-AI cost/reliability, not agentic PDLC — keep it as a supporting production-debug story. Sunnyvale Jan–May 2027 is self-relocate; JD has no reloc stipend. Winter term is OK because enrollment is Fall-only.
- **Depth prep:** Agent loop (planner, tools, memory, stop conditions) and eval/consensus gates; LangGraph node design; CI as pytest + image build, not Kubernetes; Python Easy–Med / practical coding for a possible 30-min virtual (`companies.md` directional). Do not prep as C++ DCN or PyTorch AI R&D.

## Likelihood

- **Resume screen:** Medium — agent/eval/CI and Python are visible in the top half; the Go miss is the binding ding on a 1-seat B-tier screen.
- **Overall hire odds:** Medium — published loop is a short virtual after resume; directional extra coding is LC-easy/Python. One Winter seat, Sunnyvale onsite with no reloc, and unproven Go cap conversion.
- **Funnel filters:** Oracle HCM 40535 resume (bottleneck) → recruiter/HM screen → typically 1-step ~30 min virtual (official Early Careers US; intern OA unpublished for this req) · no intern sys design · ~8–12% **[directional, Cisco / Motorola Solutions peer]** · currently pursuing CS at a US school · **no visa sponsorship** · **no reloc** · onsite Sunnyvale.
- **Outside the resume:** Apply in the first wave (posted 2026-09-18, HCM end ~2026-11-13). Confirm self-relocate to Sunnyvale. Prep an honest language story (Python interview-ready; do not claim Go) and a 90-second agent-loop plus eval-gate walkthrough for the virtual. No Nokia contact in `network.md` — do not mark Employee Referral.
