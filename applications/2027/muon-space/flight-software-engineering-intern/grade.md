# Flight Software Engineering Intern (Summer 2027) at Muon Space

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — no class-year or GPA gate on this JD; Expected May 2028; Summer 2027 after junior year with Fall 2027 remaining; U.S. citizen / ITAR U.S. Person
- **Track:** full-stack + aerospace / LEO-satellite / flight-software / real-time
- **Pipeline:** 1 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume: real-time co-op leads (Web Worker / sub-5ms / 60 FPS; 27% upload recovery), then a production Flask REST API on AWS EC2, then debug + hard-fail tests, then C++ lock-free / zero-alloc / CMake real-time **plugin** — on-axis for a FSW intern whose bottleneck is the resume, not a named OA.
- C++ and Python are proven in bullets; C, ROS, MCU firmware, orbital mechanics, rocket club, satellite internships, and a clearance are not invented.
- Binding ding: Granular has no sized runtime metric (latency / xrun / CPU).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — MemoryPool, lock-free SPSC, and the CMake processBlock audit prove real-time C++ discipline, but nothing sizes callback latency, xruns, or CPU — a skim can read hobby DSP instead of flight-software rigor
- **minor** · `Michigan Data Consulting (MDC)` · API bullet unquantified — the Flask REST API on AWS EC2 is the page's production Python-service claim and lands with no traffic, latency, or consumer metric; sole-engineer / 5-month scopes the role, not the system

### Misreads

- Granular without a number can file as "hobby audio intern, no flight software" before the lock-free C++ / release-gate checklist lands.
- MDC's unquantified Flask/EC2 line can be bucketed as "class project on a VM" instead of a shipped stakeholder API.
- Vylet's PE/search-fund tagline plus a Dockerized LangGraph closer can skim as GTM/agentic product work; the lead bullets are a name-collision defect fix and a pure-Python hard-fail gate.

### Interview angles

- **Lead with:** Granular CMake real-time safety audit, zero-allocation `MemoryPool`, lock-free SPSC (deterministic C++ / FSW-adjacent); CaseStudyPrep Web Worker / 27% upload-failure debug; Vylet name-collision (79% → 89%) and Node 3 hard-fail gate as test/debug
- **Defend:** Granular has no xrun/latency/CPU metric on the page. *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one.)* MDC API has no traffic/latency — point to the ETL scale (400 PACs / ~800 hours) and sole-engineer delivery. No C as a language. No ROS, MCU firmware, orbital mechanics, rocket club, aerospace internship, or clearance in-hand. Voice-AI co-op is intern delivery / real-time, not a flight-software claim. Vylet is founder debug + tests, not PE GTM
- **Depth prep:** C++ real-time (slab allocators, SPSC, `processBlock` constraints, CMake release gates); Python production (Flask/EC2); debug stories (27% upload, name-collision); unpublished intern coding analog — LC-mediums in C++ or Python. Do not fake RTOS, SIL/HIL, 6DOF, or MCU bring-up

## Likelihood

- **Resume screen:** High — eligible, C++ in bullets with lock-free/CMake depth, Python shipped on AWS, one clean page; two minors dent the skim, they do not flip it to a no
- **Overall hire odds:** Medium — no published OA, so most front-end elimination is this PDF, then an unpublished Easy–Med practical loop at a ~5–8% B-tier sat-startup intern accept rate. U.S. Person is a hard form knockout this page cannot show
- **Funnel filters:** Greenhouse apply (AI Talent Matching disclaimer) → resume screen (binding) → recruiter/HM (citizenship, CA onsite, Summer 2027) → unpublished tech · no named intern OA · ITAR/EAR U.S. Person
- **Outside the resume:** Apply in the first wave (posted 2026-09-30); form email `verdent06@gmail.com`; U.S. Citizen; on-site **Yes** for the posted CA intern (see Woodbridge leftover in `written-answers.md`). No Muon contact in `network.md`
