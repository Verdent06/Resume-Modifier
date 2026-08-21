# Software Engineer Intern (Winter 2027) at Figma

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 + January 4 2027 start is junior-year winter with return to school; JD has no class-year filter (dropdown includes Spring 2028)
- **Track:** full-stack + real-time collaborative design platform / product engineering
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep.AI leads as a titled SWE co-op: Web Worker / sub-5ms / 60 FPS real-time visualizer plus a 27% fault-tolerant S3 upload recovery — user-facing client performance, not a Voice-AI product pitch.
- Full-stack spine is visible in the same pass: Vylet Docker/Redis/Celery launch with a named 79%→89% defect fix, MDC production Flask REST on AWS EC2, SignalWeaver FastAPI + React/TypeScript dashboard at 9.1s p50 / 15.2s p99.
- Binding ding: Granular is the C++ proof (SPSC UI-to-audio, CMake/VST3 release audit) but never sizes the systems win — a skim can still file it as hobby DSP.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — SPSC UI-to-audio plus a CMake/VST3 release-build real-time safety audit is shipping-shaped C++, but neither bullet sizes callback latency, xruns, or CPU — a 30-second skim can still file it as hobby DSP

### Misreads

- Granular without a number can read as an audio hobby rather than lock-free / zero-alloc discipline a multiplayer-canvas team would actually probe.

### Interview angles

- **Lead with:** CaseStudyPrep Web Worker / <5ms / 60 FPS and 27% upload-failure recovery as user-facing real-time; SignalWeaver FastAPI + React/TypeScript dashboard; MDC sole-engineer Flask REST on EC2; Vylet Docker/Celery launch and 79%→89% defect fix
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: entire Granular pool is constraint engineering; swap sets cannot invent numbers)* — script audio-thread constraints and what you would measure next. TypeScript is not JavaScript — do not claim JS. Do not claim Copilot, Java, Snowflake, Databricks, Fusion, or Tableau. Vylet's PE/search-fund tagline is the product domain, not the engineering story — pivot to workers and the defect fix.
- **Depth prep:** Byteboard (~90 min: ~30 min design-doc read + ~60 min implement) — reading speed under pressure is the bottleneck (`companies.md`); C++ lock-free SPSC / `processBlock` walkthrough; FastAPI p50/p99 and React dashboard trade-offs; Angular/RxJS fault-tolerance. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — one page, class year on the page, real-time co-op lead, Flask/FastAPI/React shipping, C++ and Python through use; one minor does not sink a Greenhouse human screen
- **Overall hire odds:** Medium — A-tier Very low acceptance; screen likely clears, then Byteboard reading crunch and a 3–4 round Easy–Med loop are the binding filters
- **Funnel filters:** 3–4 rds · Easy–Med · Byteboard · Rare sys design · Bottleneck: Byteboard reading crunch · Very low · Winter 2027 SF or NY Hub · January 4 2027 start · $55/hr + housing stipend + travel reimbursement · no class-year gate
- **Outside the resume:** Apply in the first wave; timed reading + implementation drills for Byteboard; no Figma contact in `network.md` — a UMich alum on a product team still beats a cold Greenhouse pile
