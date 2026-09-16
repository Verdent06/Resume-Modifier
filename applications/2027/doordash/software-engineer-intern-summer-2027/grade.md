# Software Engineer, Intern (Summer 2027) - US at DoorDash

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside JD window Fall 2027–Summer 2028; B.S. CS; May/June 2027 start
- **Track:** full-stack + on-demand logistics / three-sided marketplace
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Flask REST API on AWS EC2 plus a Requests/Pandas ETL (~800 hours off 400 PACs) — full-stack spine a generic SWE intern screen will accept.
- CaseStudyPrep sits second with real-time constraints (Web Worker, under 5ms, 60 FPS) plus a 27% upload-failure recovery — logistics-adjacent reliability without pretending Dasher/marketplace employment.
- Binding dings: Granular (the C++ real-time differentiator) has no sized outcome, and testing on the page is pytest inside GitHub Actions, not unit tests on the Flask or Redis services.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — slab allocator and lock-free SPSC are the real-time proof, but no latency/throughput/failure number a recruiter can size
- **minor** · `resume` · testing evidence is CI-only — JD treats unit testing as how work ships; only pytest in a CI pipeline appears

### Misreads

- Granular without a number can read as hobby DSP rather than the systems/real-time signal this logistics req is hunting.
- Vylet’s LangGraph launch line can get the page bucketed as an ML/agent intern; the Redis/Celery workers and injection-safe SQL DAL are the backend read.

### Interview angles

- **Lead with:** MDC sole-engineer Flask REST on EC2; CaseStudyPrep real-time Web Worker (under 5ms / 60 FPS) and 27% S3-upload recovery; Vylet Redis/Celery cycle plus injection-safe SQL freshness; SignalWeaver FastAPI p50/p99 plus GitHub Actions pytest; Granular C++ zero-alloc audio thread and lock-free SPSC
- **Defend:** Granular has no callback-latency number on the page *(out of rails: pool bullets 1–6 have no impact metric; swap sets cannot invent one)* — script the audio-thread rules and what you would measure. Unit tests are not on Flask or Redis *(out of rails: live pool’s only test mention is SignalWeaver pytest CI)* — talk pytest on SignalWeaver and how you would add tests on a matching service. Do not claim Java, Kotlin, Copilot, or DoorDash/logistics employment. LangGraph is pipeline infra, not an ML-research lead.
- **Depth prep:** HackerRank Med–Hard (`companies.md`; brute force penalized; graphs, intervals, simulation) then tech onsite — no intern sys design. Redis/Celery backpressure; Flask REST + EC2; lock-free atomics; one STAR on CaseStudyPrep fault-tolerant uploads and one on Vylet SQL freshness. Why DoorDash = three-sided marketplace reliability, not a generic web intern seat.

## Likelihood

- **Resume screen:** High — one page, class year in window, shipped APIs, databases, real-time evidence in the top half, pytest/CI present
- **Overall hire odds:** Medium — A-tier Selective; resume is not the binding filter; HackerRank then tech onsite still eliminate most of a small intern class
- **Funnel filters:** Greenhouse resume → HackerRank OA · 2–3 rds Med–Hard · no intern sys design (L4+ only) · Bottleneck: tech onsite · Selective · in-person NY/SF/Sunnyvale/LA/Seattle · U.S. work auth (F-1 CPT OK, no J-1)
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-14, rolling); timed HackerRank mediums with simulation/graphs; intern behavioral is a filter (`recruiting.md`)
