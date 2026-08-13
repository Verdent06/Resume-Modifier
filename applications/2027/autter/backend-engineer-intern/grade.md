# Backend Engineer Intern (Agentic AI) at Autter

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — current U-Michigan CS + Economics undergrad, Expected May 2028, returning to school after a Summer 2027 internship; no sponsorship needed. IST full-time hours are a logistics expectation, not a class-year knockout, and a summer window avoids the academic-calendar conflict.
- **Track:** full-stack / backend + agentic-AI / LLM-orchestration (developer-tooling differentiator; track_divergence = false)
- **Pipeline:** 3 graded cycle(s) + final · exit: writer_peak (remaining defects out-of-rails — cannot be closed without inventing experience)

## Screen Review

### First read

- Leads on-axis: a shipped, Dockerized LangGraph agentic pipeline (Redis/Celery workers) with a LangSmith adversarial-eval harness + Pydantic consensus gates lifting faithfulness 50%→90%, and a defect fix lifting lead-qualification 79%→89% — directly maps to "agentic orchestration over LLM APIs" and "improve accuracy of detection engines."
- Backend service ownership is real: a Flask REST API on AWS EC2 (MDC) and a FastAPI async-REST + LoRA-fine-tune (81%→96%) + Docker Compose + GitHub Actions CI project (SignalWeaver).
- Binding dings are structural, not fixable on the page: no GitHub-API/webhook or code-review bullet (a JD *preferred*), and every entry is greenfield/self-authored (no inherited-codebase signal). Neither can be closed without inventing experience.

### Demerits

- **minor** · `CaseStudyPrep.AI` · thin single-bullet, tangential axis — a titled co-op reduced to one line on client-side audio VAD reads thinner than the role was, and voice-DSP is off the agentic-backend axis.
- **minor** · `resume` · GitHub API / webhooks not demonstrated — the JD-preferred GitHub-App/webhook literacy has no direct bullet; GitHub Actions CI only gestures at it.
- **minor** · `resume` · all work is greenfield / self-authored — every entry is Founder, sole engineer, or personal project; no signal of reading and extending an existing codebase, which improving existing detection engines requires.

### Misreads

- A founder skimming for "GitHub App / webhooks" may under-read the developer-tooling fit even though the agentic-backend and CI signal is strong.
- The single off-axis `CaseStudyPrep.AI` line can make a rushed reader briefly bucket the page as voice/frontend-adjacent before the backend spine lands.
- An all-greenfield page can be misread as "only builds from scratch," under-weighting the Vylet defect-diagnosis-and-fix work that is genuinely debugging into complex existing logic.

### Interview angles

- **Lead with:** Vylet as the agentic-backend flagship — Dockerized LangGraph pipeline with Redis/Celery workers, the LangSmith adversarial-eval + Pydantic consensus gate (50%→90% faithfulness), and the name-collision defect fix (79%→89%); then SignalWeaver's FastAPI async REST + LoRA fine-tune (81%→96%) + Docker Compose/GitHub Actions CI, and MDC's Flask REST API on EC2 as production service ownership.
- **Defend:** GitHub-API/webhook gap — narrate REST + GitHub Actions CI fluency and how you'd wire GitHub-App webhook events into a backend service *(out of rails: no pool bullet demonstrates GitHub API or webhook handling)*; all-greenfield gap — frame the Vylet name-collision defect diagnosis-and-fix and the LoRA/eval work as evidence you can read into and extend complex, unfamiliar logic, not only build from scratch *(out of rails: no pool entry carries inherited-codebase / extend-existing-engine signal)*; off-axis CaseStudyPrep line — recast the Silero-VAD/ONNX work as ML-inference cost/latency engineering (40% cloud-inference cost cut).
- **Depth prep:** Pydantic consensus-gate + LangSmith adversarial-eval design (the closest analog to improving a detection engine's accuracy/speed); LoRA fine-tuning + held-out evaluation methodology; async queue/worker (Redis/Celery) and asyncpg data-layer design; Docker containerization mapped to Autter's sandboxed PR execution; skim Autter's product surface (native GitHub App, runtime-observability SDK, AI-vs-human line attribution) before any founder call.

## Likelihood

- **Resume screen:** High — shipped LangGraph agentic pipeline with consensus/eval gates, production REST/queue/data-layer backends, Docker, and multiple before/after accuracy and latency numbers hit nearly every screen criterion on-axis.
- **Overall hire odds:** Medium — the founder-direct, resume-first funnel plays to this page's strengths, so clearing the screen is likely; but a 1–10-person startup runs a tiny loop with few seats, and the decision shifts to live depth — narrating trade-offs behind the self-built systems and showing you can extend the team's existing code.
- **Funnel filters:** 2–3 rounds · practical backend/agent screen (not LC-hard) · no named OA platform · founder resume-first read · IST-hours availability is the binding logistics expectation.
- **Outside the resume:** Warm founder-direct intro or referral (recruiting.md §4: HM > recruiter > engineer; startups reward founder DMs) and apply within ~72h of the req opening (recruiting.md §8) — early, warm reads convert disproportionately at this funnel stage.
