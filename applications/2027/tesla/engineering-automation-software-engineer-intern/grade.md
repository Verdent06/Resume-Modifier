# Software Engineer Intern — Engineering Automation, Vehicle Engineering at Tesla

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 vs intern Jan–May 2027 is junior-year winter/spring with return to school; JD requires current enrollment only, no class-year cutoff
- **Track:** full-stack
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads as sole-engineer production Flask REST on AWS EC2 plus a Pandas ETL that killed ~800 hours of manual PAC research — web tools for non-SWE users, not a notebook.
- SignalWeaver shows the Design Technology stack on one project: React/TypeScript dashboard persisted to Postgres and FastAPI REST at 9.1s p50 / 15.2s p99; CaseStudyPrep.AI is the live-debug story (27% S3 failure recovery, sub-5ms / 60 FPS).
- Binding ding: Granular is the C++ proof (lock-free SPSC UI-to-audio) but never sizes the systems win — a Tesla skim can still file it as hobby DSP.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free DSP skim — SPSC/processBlock is real C++ systems work, but with no latency, xrun, or CPU number a 30-second skim files it as a synth hobby next to a React/Postgres intern req

### Misreads

- Granular without a number can read as an audio hobby rather than lock-free / zero-alloc discipline; a rushed screen may also miss that C++ is demonstrated there and not only on the Skills line.

### Interview angles

- **Lead with:** MDC Flask REST on EC2 and the 800-hour ETL as internal tools for researchers; SignalWeaver React/TypeScript + FastAPI + Postgres; CaseStudyPrep 27% upload-failure recovery and Web Worker / 60 FPS; Vylet asyncpg SQL DAL and 79%→89% production fix
- **Defend:** Granular has no latency/CPU metric *(out of rails: entire Granular pool is constraint engineering; swap sets cannot invent numbers)* — script audio-thread constraints and what you would measure next. Do not claim Next.js, Go, Kubernetes, Jenkins, Redux, Drizzle, or gRPC. Docker is Skills-only on this page (JD keyword, no Compose bullet). SolidWorks is not on the page — CAD is preferred familiarity, not a product claim. Vylet's PE/search-fund tagline is the product domain; pivot to SQL and the defect fix.
- **Depth prep:** HackerRank Medium (arrays/hash maps/trees/graphs) is the volume gate (`companies.md` bottleneck = tech rounds). Walk Flask vs FastAPI API design, Postgres persistence, Angular/RxJS live debug, and C++ SPSC/`processBlock` if they probe the language. Behavioral/ownership is a filter (`recruiting.md` §6). No intern sys-design.

## Likelihood

- **Resume screen:** High — one page, class year on the page, production Flask + FastAPI/React/Postgres + a live-debug co-op; one minor does not sink a Tesla intern screen
- **Overall hire odds:** Medium — B-tier ~5–8%; screen likely clears team-match onto Design Technology, then HackerRank Medium and tech rounds are the binding filters
- **Funnel filters:** 3 rds · Medium · HackerRank (Codility also reported by cycle) · No intern sys design · Bottleneck: tech rounds · ~5–8% · Palo Alto / Fremont on-site · Jan–May 2027 (min 12 weeks) · currently enrolled · CPT students must confirm 40 hr/week
- **Outside the resume:** Apply in the first wave; drill HackerRank Medium; no Tesla Design Technology contact assumed — a Vehicle Engineering / internal-tools referral still beats a cold ATS pile
