# Software Engineering Intern/Co-op — Spring 2027 at SpaceX

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — enrolled bachelor's (Expected May 2028 → junior in Spring 2027); JD has no class-year filter; GPA 3.66 ≥ 3.5 preferred (ITAR citizenship is an apply-form gate, not a resume class-year knockout)
- **Track:** full-stack + aerospace / real-time / mission-critical / embedded-adjacent systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on Web Worker / sub-5ms / 60 FPS real-time systems; Granular sits #2 with C++ lock-free / zero-alloc audio-thread depth — differentiator is visible in the top half.
- Full-stack spine (MDC Flask/AWS ownership + SignalWeaver FastAPI/Docker/CI) backs the generic SWE screen; Python and C++ show in bullets, not Skills alone.
- Binding dings: Granular has no sized outcome metric; unit-testing is a CI `pytest` nod rather than owned test design.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Strongest company-fit entry (zero-alloc audio thread, SPSC FIFO, atomics) has no quantified outcome (xruns, latency, CPU), so the screen cannot size impact
- **minor** · `SignalWeaver` · thin unit-testing signal — JD prefers unit-testing discipline; pytest appears only as one token inside a CI pipeline line, with no test design or failure-catching outcome

### Misreads

- Granular without a number can read as hobby DSP rather than mission-critical real-time discipline — skim may underrate the C++/embedded adjacency SpaceX rewards.
- SignalWeaver's CI/`pytest` token can be bucketed as "deployed a side project" rather than testing ownership the preferred quals ask for.

### Interview angles

- **Lead with:** Granular Synthesizer — zero-alloc `processBlock`, SPSC FIFO, atomics, real-time safety audit; CaseStudyPrep Web Worker / <5ms / 60 FPS as production real-time systems under latency constraints
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no allowlisted impact metrics)*; unit-testing depth is CI/`pytest` only *(out of rails: no stronger test-ownership bullet; MatchStream JUnit unavailable)* — script honest answers from design decisions and what you would measure next
- **Depth prep:** lock-free concurrency, real-time constraints, C++ memory/threading; HackerRank mediums under time; debugging and performance optimization stories from CaseStudyPrep upload failures and Granular RT checklist

## Likelihood

- **Resume screen:** High — real-time lead, C++/systems adjacency in the top half, JD languages in bullets, production metrics elsewhere, one clean page
- **Overall hire odds:** Medium — SpaceX is OA- then tech-loop gated; resume clears the screen, but HackerRank Med–Hard and 3–4 tech rounds (~5–8% funnel) decide the offer
- **Funnel filters:** HackerRank OA · Med–Hard coding/systems rounds · bottleneck: tech rounds · ITAR apply-form eligibility
- **Outside the resume:** Timed HackerRank/LC mediums; 2–3 mocks/week on debugging, concurrency, and defending Granular RT design; warm referral if available
