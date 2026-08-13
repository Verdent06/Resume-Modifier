# Software Engineering Intern — Summer 2027 at Collins Aerospace (RTX)

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 maps to enrolled rising senior at Summer 2027; JD requires pursuing Bachelor's+ and enrollment through the internship (U.S. citizenship is an apply-form knockout, not a page class-year miss)
- **Track:** full-stack + real-time C++ / threaded application development
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on Web Worker / sub-5ms / 60 FPS real-time systems; Granular sits #2 with C++ lock-free SPSC, zero-alloc `processBlock`, and a real-time safety audit — the threaded/OOP differentiator is in the top half.
- Python full-stack spine is visible: MDC Flask REST on AWS EC2 with an ~800-hour ETL win, plus SignalWeaver FastAPI p50/p99 instrumentation.
- Binding ding: Granular has no sized runtime outcome (latency, xruns, CPU), so the C++/threading depth is described rather than measured.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Lock-free SPSC, zero-alloc processBlock, and a real-time safety audit are the threaded/OOP signal this shop wants, but none of the three bullets sizes the outcome (callback latency, xruns, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than mission-critical real-time discipline — a skim may underrate the C++/threaded application-development evidence Collins lists as a preferred qual.

### Interview angles

- **Lead with:** Granular Synthesizer — zero-alloc `processBlock`, lock-free SPSC FIFO, atomics, real-time safety checklist; CaseStudyPrep Web Worker / <5ms / 60 FPS as production real-time under latency constraints; MDC sole-owned Flask REST on EC2 as the Python delivery the JD lists first
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure next. Java is listed as a relevant language and is absent *(out of rails: Java is not in the candidate language inventory)* — frame Python + C++ as the demonstrated pair and OOP/threading as transferable. Vylet still carries LangGraph/PE framing — if asked, pivot to the 79%→89% defect fix and Docker/Celery workers, not the agentic product story
- **Depth prep:** lock-free concurrency, C++ memory/audio-thread rules, OOP class modeling (MemoryPool, SPSC, atomics); light practical/OOP questions (no OA); Flask/FastAPI ownership and the Web Worker real-time story

## Likelihood

- **Resume screen:** High — Python and C++ in bullets, lock-free C++ in the top two, Flask/FastAPI behind them, one clean page, no OA so the PDF is the gate
- **Overall hire odds:** Medium — C-tier RTX/Collins funnel is resume-gated then an easy 2–3 round loop (~20–25% offer); the page clears the screen, but citizenship is a binary apply-form knockout and the mentor interview still has to defend OOP and threading live
- **Funnel filters:** 2–3 rounds · Easy practical · No OA · No system design · Bottleneck: resume · ~20–25% offer · U.S. citizenship apply-form knockout
- **Outside the resume:** Confirm U.S. citizenship honestly on the Workday knockout; apply in the first wave; a Cedar Rapids/Collins or RTX referral (HM > recruiter > engineer); prep lock-free/OOP walkthroughs of the synthesizer and the Web Worker real-time story
