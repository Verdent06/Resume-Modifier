# Software Engineer Backend Intern (Summer 2027) at Astranis

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — JD requires currently pursuing B.S./M.S. CS; UMich CS+Econ Expected May 2028, still enrolled at Summer 2027. No class-year knockout. US person / 55hr / SF onsite are apply-form gates.
- **Track:** full-stack + aerospace / GEO-satellite / mission-critical / fleet-ops ground software
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads on a sole-owned Flask REST API on EC2 plus an 800-hour PAC ETL — Python backend shipped to a real stakeholder, not a class project.
- SignalWeaver FastAPI + pgvector (49ms) and Vylet Redis/Celery workers cover Postgres and pub/sub-adjacent queues; CaseStudyPrep (<5ms / 60 FPS) plus Granular lock-free C++ carry the satellite-ops real-time identity. No invented Kubernetes/RabbitMQ/Flink.
- Binding dings: Granular never sizes the real-time win, and Vylet still reads as PE/LangGraph lead-gen under the Founder tagline.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Lock-free SPSC, zero-alloc processBlock, and a real-time safety audit are the systems signal this satellite-ops shop wants, but none of the three bullets sizes the outcome (callback latency, xruns, CPU)
- **minor** · `Vylet` · off-axis product — Redis/Celery workers and a pure-Python consensus gate are real backend, but the Founder tagline still frames a PE/search-fund LangGraph lead-gen product — a Platform skim can bucket it as GTM/agentic rather than satellite-ops engineering

### Misreads

- Granular without a number can read as hobby DSP rather than mission-critical real-time discipline — a skim may underrate the C++ systems evidence Platform/telemetry wants.
- Vylet's Founder/PE tagline can bucket the resume as agentic GTM rather than backend/infra, even though Redis/Celery is the queue proof this JD asks for.

### Interview angles

- **Lead with:** MDC Flask REST on EC2 (sole engineer, 5-month contract); SignalWeaver async FastAPI + pgvector 49ms p50; Vylet Redis/Celery workers + pure-Python consensus gate; CaseStudyPrep Web Worker <5ms / 60 FPS and 27% S3 upload recovery; Granular zero-alloc `processBlock` and lock-free SPSC
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool bullets 1–6 are architecture-only; swap sets cannot invent a witness)* — script the audio-thread constraints and what you would measure next. Vylet PE/LangGraph framing *(out of rails: product identity is the pool header; Node 3 swap still flagged; cannot drop the entry)* — pivot to Redis/Celery workers and the pure-Python gate, not the GTM story. Do not claim Kubernetes, RabbitMQ, Flink, ROS, a satellite internship, fleet-management title, or clearance.
- **Depth prep:** Python DS&A (Coderbyte ~50m C++/Python is directional from a sibling FSW round; this backend intern OA is unpublished); Postgres/pgvector query path; Redis/Celery as the honest pub/sub analog; lock-free / zero-alloc real-time rules; REST + EC2/Docker deploy walkthrough. Light intern sys design possible on telemetry/command services.

## Likelihood

- **Resume screen:** High — Flask/FastAPI + Postgres/pgvector + Redis/Celery + pure-Python in bullets, real-time in the top half, no invented K8s/RabbitMQ/Flink
- **Overall hire odds:** Medium — B-tier Greenhouse funnel is resume-then-tech (~5–8% directional); unpublished Coderbyte/live coding plus a 55hr/SF onsite form still have to clear, and the PE/DSP frames can steal a few seconds from the backend story
- **Funnel filters:** Greenhouse resume (AI Talent Matching disclaimer) → recruiter (US-person + SF 5-day + 55hr knockouts) → Coderbyte/live coding **[directional, FSW 2024]** → tech/loop · Medium · light intern sys design. Bottleneck: resume then tech. Export-controlled US person.
- **Outside the resume:** Apply in the first wave of this 2026-09-22 posting; answer US-person + SF 5-day + 55hr honestly on Greenhouse; a Platform-team referral (HM > recruiter > engineer); prep Python DS&A plus a Postgres + worker-queue walkthrough
