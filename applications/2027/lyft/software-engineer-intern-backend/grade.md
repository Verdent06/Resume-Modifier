# Software Engineer Intern, Backend (Summer 2027) at Lyft

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside the JD window December 2027–Summer 2028; B.S. CS; available Summer 2027 in SF (relocates)
- **Track:** full-stack + rideshare-marketplace / realtime-backend
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Flask REST API on AWS EC2 and a Requests/Pandas ETL (~800 hours off 400 PACs) — backend spine a generic SWE intern screen will accept.
- CaseStudyPrep sits second with real-time constraints (Web Worker, under 5ms, 60 FPS) plus a 27% upload-failure recovery — marketplace-adjacent reliability without pretending rideshare domain work.
- Binding dings: Granular (the C++ real-time differentiator) has no sized outcome, and testing on the page is pytest inside GitHub Actions, not unit/integration/load on the Flask or Redis services.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — slab allocator and lock-free SPSC are the real-time proof, but no latency/throughput/failure number a recruiter can size
- **minor** · `resume` · testing evidence is CI-only — JD treats unit, integration, and load tests as how reliability ships; only pytest in a CI pipeline appears

### Misreads

- Granular without a number can read as hobby DSP rather than the systems/real-time signal this backend req is hunting.
- Vylet’s LangGraph launch line can get the page bucketed as an ML/agent intern; the Redis/Celery workers and asyncpg DAL are the backend read.

### Interview angles

- **Lead with:** MDC sole-engineer Flask REST on EC2; CaseStudyPrep real-time Web Worker (under 5ms / 60 FPS) and 27% S3-upload recovery; Vylet Redis/Celery cycle plus injection-safe SQL freshness; Granular C++ zero-alloc audio thread and lock-free SPSC; SignalWeaver FastAPI p50/p99 plus GitHub Actions pytest
- **Defend:** Granular has no callback-latency number on the page *(out of rails: pool bullets 1–6 have no impact metric; swap sets cannot invent one)* — script the audio-thread rules and what you would measure. Load/integration tests are not on Flask or Redis *(out of rails: live pool’s only test mention is SignalWeaver pytest CI; adding a third bullet overflowed the page)* — talk pytest on SignalWeaver and how you would add load tests on a matching service. Do not claim Go, mobile, or rideshare-domain internships. LangGraph is pipeline infra, not an ML-research lead.
- **Depth prep:** CodeSignal-class OA (companies.md; Extern also reports CoderPad/HackerRank variance) — graphs, intervals, geospatial; laptop round (correctness / clean code / performance); Redis/Celery backpressure; Flask REST + EC2; lock-free atomics; one STAR on Vylet name-collision (79%→89%) and one on CaseStudyPrep fault-tolerant uploads; Why Lyft = transportation marketplace reliability, not a generic web intern seat

## Likelihood

- **Resume screen:** High — one page, class year in window, shipped APIs, databases, real-time evidence in the top half, pytest/CI present
- **Overall hire odds:** Medium — B-tier ~3–5%; resume is not the binding filter; tech rounds (OA + laptop) still eliminate most of a ~15–20 intern class
- **Funnel filters:** CareerPuck/Greenhouse resume → recruiter ~30 min → CodeSignal (row) / CoderPad or HackerRank **[directional]** → laptop/coding rounds · Light intern sys design · Bottleneck: tech rounds · ~3–5% · hybrid SF Mon/Wed/Thu
- **Outside the resume:** Apply in this first-wave window (posted ~2026-09-11, rolling, tiny cohort); no Lyft contact in `network.md` — do not mark referral; timed DSA plus laptop-round clean-code practice; intern behavioral is a filter (`recruiting.md`)
