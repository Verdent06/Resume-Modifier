# Software Engineering Intern III, Summer 2027 (Onsite) at BAE Systems

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 maps to transitioning into senior year at Summer 2027; JD wants junior or senior (or graduate). U.S. citizenship is an apply-form knockout, not a class-year miss.
- **Track:** full-stack (mission-critical system stability / resilience flavor; no track divergence)
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on a 27% upload-failure fix in Angular/RxJS plus a Web Worker / sub-5ms / 60 FPS real-time path — stability and a listed JS framework in the first glance.
- Python full-stack is visible: MDC Flask REST on AWS EC2, Vylet Docker/Redis/Celery with a 79%→89% production-defect fix, SignalWeaver FastAPI + React with p50/p99.
- Binding ding: Granular C++ is one MemoryPool line; lock-free threading and VST3/AU live only in the subtitle.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · single bullet, no metric — header claims a from-scratch C++/JUCE granular engine with lock-free threading and release-ready VST3/AU, but the body is one MemoryPool slab with no sized outcome

### Misreads

- A skim can file Granular as hobby DSP because the lock-free / release-binary claims are in the tagline, not the bullet — underrating the C++ systems proof Electronic Systems actually wants.

### Interview angles

- **Lead with:** CaseStudyPrep 27% upload-failure recovery (Angular/RxJS, expired S3 URLs) as the stability story; Granular zero-allocation `processBlock` / `MemoryPool<Grain, 64>` as the C++ real-time constraint; MDC sole-owned Flask REST on EC2 as Python production delivery
- **Defend:** Granular has no xrun/latency/CPU number and no second bullet on lock-free SPSC or VST3 *(out of rails: adding pool #2 SPSC or #6 CMake overflowed to 2 pages; no metric-bearing Granular pool bullet; iter-1 floors block dropping other entries)*. Java is on the JD list and absent — say Python + C++ + TypeScript are the interview languages; do not claim Java. Vylet’s title is PE lead-sourcing — if asked, pivot to the 79%→89% defect fix and Docker/Redis/Celery, not the deal-flow headline *(out of rails: tagline is verbatim from context.md; rewriting is original prose)*
- **Depth prep:** fault-tolerant frontend (RxJS retry, presigned URLs); C++ audio-thread rules (no alloc, no lock, slab allocator, SPSC); Flask/FastAPI ownership and Docker/CI; light DS&A — this loop is not an OA gauntlet; STAR for a possible HireVue

## Likelihood

- **Resume screen:** High — listed languages in bullets, reliability-led first role, preferred Angular/AWS/Docker/Postgres/Redis through use, one clean page, no OA so the PDF is the gate
- **Overall hire odds:** Medium — B-tier defense-prime funnel (~15–20%, 2–3 easy rounds, resume bottleneck); the page should clear the screen, then citizenship/clearance form knockouts and a behavioral filter still bind
- **Funnel filters:** Brassring apply → resume screen (binding) → possible HireVue → hiring-manager · Easy technical · No standard OA · No system design · U.S. citizen; eligibility to obtain (not currently possess) clearance
- **Outside the resume:** Answer U.S. citizenship YES and existing clearance NO honestly; a San Diego / Electronic Systems referral (HM > recruiter > engineer); apply in the first wave; prep STAR plus a live walkthrough of the upload-failure fix and the MemoryPool audio-thread constraint
