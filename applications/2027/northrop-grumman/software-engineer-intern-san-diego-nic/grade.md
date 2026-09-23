# 2027 Software Engineer Intern - San Diego CA at Northrop Grumman

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 ⇒ enrolled full-time Fall 2027; CS major; U.S. citizen / Secret-eligible; can do 10 weeks Summer 2027. Citizenship and Program Special access are apply-form knockouts, not a class-year miss.
- **Track:** full-stack + mission-systems / NIC / real-time-embedded-adjacent
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on real-time constraints (Web Worker / sub-5ms / 60 FPS) and a 27% upload-failure recovery — generic SWE plus test/debug in the first glance.
- Granular sits in slot two with zero-allocation C++ `MemoryPool` and lock-free SPSC — the NIC differentiator is visible in the top half; Python production follows (MDC Flask/EC2, SignalWeaver FastAPI + Docker/GHA).
- Binding dings: Granular has no sized latency/CPU/voice number; Vylet's founder tagline still says PE/search-fund.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-allocation MemoryPool and lock-free SPSC prove real-time C++ discipline, but nothing sizes the plugin — no latency budget, voice count, or CPU figure a Mission Systems screener can use to scale the work.
- **minor** · `Vylet` · PE/search-fund framing — Tagline leads with PE/search-fund lead-sourcing at a NIC mission-systems intern req; the Docker/defect bullets are on-axis but a skim can bucket the founder role as GTM rather than production software.

### Misreads

- Granular without a number can read as hobby DSP rather than the lock-free / zero-alloc systems proof NIC wants.
- Vylet's PE/search-fund tagline can file the founder role as deal-sourcing GTM instead of Dockerized production delivery.

### Interview angles

- **Lead with:** CaseStudyPrep 27% upload-failure recovery and sub-5ms / 60 FPS real-time path; Granular zero-allocation `processBlock` / `MemoryPool<Grain, 64>` and lock-free SPSC; MDC sole-owned Flask REST on EC2 as Python production
- **Defend:** Granular has no xrun/latency/CPU number *(out of rails: full 6-bullet pool has no allowlisted impact metric; 16-voice swap overflowed to 2 pages)*. Java / C / Rust / MATLAB / RTOS / Rhapsody / GreenHills are on the preferred list and absent — interview languages are Python + C++ + TypeScript; do not claim them. Vylet's title is PE lead-sourcing — if asked, pivot to the 79%→89% defect fix and Docker/Redis/Celery, not the deal-flow headline *(out of rails: tagline is verbatim from context.md; rewriting is original prose; Node 3 swap overflowed)*
- **Depth prep:** C++ audio-thread rules (no alloc, no lock, slab allocator, SPSC); fault-tolerant frontend (RxJS retry, presigned URLs); Flask/FastAPI ownership and Docker/CI; STAR for recruiter + HM — this loop has no standard OA (`recruiting.md` intern funnel; B-tier resume bottleneck)

## Likelihood

- **Resume screen:** High — C++ and Python through use, real-time DSP in the top two slots, Flask/EC2 plus Docker/CI on a clean one-pager; no OA so this PDF should clear
- **Overall hire odds:** Medium — B-tier prime intern funnel (~15–20%, 2–3 easy–med rounds, resume bottleneck). The page is on-axis; citizenship/Secret-eligibility form knockouts and a behavioral/project walk still bind after the screen
- **Funnel filters:** Workday resume screen (binding) → recruiter (~20–30 min, citizenship / Fall 2027 / San Diego) → HM/panel STAR + project walk · Easy–Med · No standard OA · No intern sys design · U.S. citizen; able to obtain Secret + Program Special access (not in-hand at start)
- **Outside the resume:** Apply in this short Workday window (posted 2026-09-22, endDate 2026-09-25); answer U.S. citizen YES and existing clearance NO honestly; a Mission Systems / San Diego referral if one exists; STAR plus a live walkthrough of `processBlock` zero-alloc and the 27% upload-failure fix
