# Summer 2027 Internship - Embedded Software Engineering at General Matter

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027: current CS undergrad (rising senior / after junior year); JD requires current undergrad or grad in CS/CE/EE/similar with no sophomore/junior gate. Clearance eligibility and South Bay commute are apply-form knockouts, not resume class-year filters.
- **Track:** full-stack + nuclear-enrichment / safety-critical embedded-adjacent
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Granular opens on lock-free C++ (zero-alloc `processBlock`, SPSC atomics, CMake real-time safety audit) — the Embedded title's low-level signal is in slot 1, not buried under Voice AI.
- Python shows through use (MDC Flask/ETL, Vylet pure-Python gate + 79%→89% debug); CaseStudyPrep adds sized real-time (sub-5ms / 60 FPS) and fault-tolerant recovery (27% upload failures).
- Binding dings: Granular never sizes whether the audio thread held load; MDC's production Flask API has no traffic or latency number.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — three lock-free / zero-alloc C++ bullets plus a CMake real-time safety checklist never size callback time, xruns, CPU, or load; a systems screener cannot tell whether the real-time claims held
- **minor** · `Michigan Data Consulting (MDC)` · API bullet unquantified — the Flask REST API on AWS EC2 is the page's only production API-plus-cloud claim and lands with no traffic, latency, or consumer metric; sole-engineer / 5-month scopes the role, not the system

### Misreads

- An undated GitHub in Granular's date slot can read as a hobby VST even though it is the C++ real-time hook for this req.
- MDC's unquantified Flask/EC2 line can be bucketed as a class project on a VM instead of a shipped stakeholder API.
- A firmware-first screener who wants MCU/RTOS/lab instrumentation will not find it — the page is honest C++/Python systems, not fabricated embedded hardware.

### Interview angles

- **Lead with:** Granular zero-alloc `processBlock`, lock-free SPSC, CMake real-time safety checklist; CaseStudyPrep sub-5ms / 60 FPS and 27% upload recovery; Vylet name-collision defect (79% → 89%) and pure-Python consensus gate; MDC sole-engineer Flask REST on EC2
- **Defend:** Granular has no callback/xrun/CPU number *(out of rails: full 6-bullet pool is architecture-only; swap sets cannot invent a runtime metric)* — narrate the real-time safety checklist and what you would measure. MDC API has no traffic/latency *(out of rails: MDC pool has no API traffic bullet; SignalWeaver FastAPI would size an API but adding it overflows and is LoRA/ML off-axis)* — point to ETL scale (400 PACs / ~800 hours). No C, Rust, firmware, MCU, PLC, oscilloscope, or clearance on the page — do not claim them. Clearance eligibility and South Bay commute are form answers, not resume lines.
- **Depth prep:** walk Granular real-time constraints (zero-alloc audio thread, SPSC atomics, CMake audit) for a systems/reliability screen; timed C++/Python DS&A (OA unpublished — do not assume HackerRank); mission / urgency / accountability behavioral plus proudest-accomplishment as a reliability story

## Likelihood

- **Resume screen:** High — C++ under a hard real-time constraint opens the page, Python shows through production ETL/API and a debug fix, Expected May 2028 is a current student, and nothing claims firmware the page cannot defend
- **Overall hire odds:** Low — Unrated tiny-cohort Greenhouse intern; human PDF screen is the front-end filter, then an unpublished coding/systems loop and a mission bar closer to Anduril ~3–5% / SpaceX ~5–8% than a mid-size SWE intern. Honest C++ adjacency clears a human read; it does not invent MCU/lab time the loop may still probe
- **Funnel filters:** Greenhouse resume screen (PDF read early) · OA unpublished · tech loop unpublished (C++/Python + systems/reliability flavor) · behavioral (urgency/accountability/Skunkworks) · form knockouts: U.S. clearance eligibility (Yes/No), South Bay commute for full 12 weeks, unofficial transcript
- **Outside the resume:** Warm Greenhouse referral; timed LC-style C++/Python plus concurrency walk-throughs; attach transcript; answer clearance Yes and LA-commute Yes honestly; frame proudest accomplishment as a reliability/real-time story
