# Software Engineering Intern (Summer 2027) at Niantic Spatial

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 B.S. CS+Econ; JD requires currently pursuing BS/MS in CS or related (no class-year cap); US citizen / no sponsorship; SF 4x/week relocate
- **Track:** full-stack + physical-AI / geospatial mapping / VPS
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume aimed at **Product Engineering**: MDC Pandas ETL (~800 hours / 400 PACs) into a Flask REST API on AWS EC2 for a nonprofit; CaseStudyPrep titled SWE co-op recovering a 27% S3 upload-failure path (Angular/RxJS) plus ONNX VAD (40% inference-cost cut); Vylet Docker/Redis/Celery product with a named 79%→89% defect.
- Projects carry C++ systems (Granular MemoryPool + lock-free SPSC) and the product-API analog (SignalWeaver FastAPI REST 9.1s p50 + React/TypeScript dashboard). Python, TypeScript, and C++ through use. Go, CUDA, Kubernetes, NeRF, COLMAP, and a Niantic internship are not invented.
- Binding dings: Granular has no sized runtime metric; SignalWeaver still reads as fintech research at a geospatial company.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — MemoryPool and lock-free SPSC prove real-time C++ discipline, but nothing sizes callback latency, xruns, or CPU *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)*
- **minor** · `SignalWeaver` · financial-research identity — FastAPI REST and React/TypeScript are the Product Engineering analog, but the name and descriptor still read as a fintech research assistant *(out of rails: every pool bullet is finance-domain; descriptor is fixed)*

### Misreads

- Granular without a number can file as "hobby audio intern" before the zero-allocation / lock-free story lands.
- SignalWeaver's financial-research descriptor can file the page as a quant intern if the reader never reaches MDC REST or CaseStudyPrep upload recovery.
- Vylet's PE/search-fund tagline plus LangGraph can skim as GTM/agentic product work; the bullets are a 30x owned pipeline and a name-collision defect fix.
- Voice-AI co-op is upload reliability + on-device inference, not a spatial/CV internship.

### Interview angles

- **Lead with:** MDC ETL → Flask REST on EC2 (product APIs / data workflows); CaseStudyPrep 27% upload-failure recovery (upload → process path the Product Engineering track names); SignalWeaver FastAPI + React/TypeScript (APIs that other surfaces consume); Granular C++ zero-alloc / lock-free (Backend Systems language proof, not the apply track)
- **Defend:** No Go, CUDA, Kubernetes, Terraform, Ray, Spark, COLMAP, OpenCV, NeRF, Gaussian Splatting, ROS, or a Niantic internship. Granular has no xrun/latency/CPU metric on the page *(out of rails)*. SignalWeaver is a REST/TS stack, not a 3D reconstruction project *(out of rails)*. Primary track is **Product Engineering**, not ML/AI Infrastructure (no distributed training / GPU story) and not Backend Systems as the identity (C++ is audio-thread systems, not VPS microservices). SF is a term relocate from Northville, MI — do not spoof an SF home address.
- **Depth prep:** Python production (Flask/EC2, Docker/Redis); TypeScript/Angular/React; REST/API design; C++ real-time (slab allocators, SPSC, `processBlock` constraints) if they probe Backend. CoderByte ~60 min DSA **[directional, 2026 intern]** then 60-min live coding + 60-min behavioral. Physical-world curiosity: honest mapping is on-device inference (ONNX VAD) and hard real-time C++, not 3D reconstruction. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** Medium — eligibility is clean (Expected May 2028, CS+Econ, 3.7) and the top half is product APIs + upload reliability + TypeScript/Python; two minors dent the physical-AI skim
- **Overall hire odds:** Medium — B-tier Ashby then CoderByte OA (`company.md`); resume is not the binding filter after knockouts; OA and live coding will be
- **Funnel filters:** Ashby knockouts (work auth, sponsorship, SF 4x/week, track pick) → resume → CoderByte ~60 min **[directional, Summer 2026]** → 60-min live coding + 60-min behavioral. Bottleneck: resume then OA · ~3–8%. Visa: no sponsorship (cleared — US citizen). No class-year cap (cleared).
- **Outside the resume:** Apply in the first wave (posted 2026-10-06). Track = **Product Engineering**. Form email `verdent06@gmail.com`. GPA **3.7**. No Niantic contact in `network.md`. Packet only — see `written-answers.md`
