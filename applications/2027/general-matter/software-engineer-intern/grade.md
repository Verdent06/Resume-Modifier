# Summer 2027 Internship - Software Engineering at General Matter

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027: current CS undergrad (rising senior / after junior year); JD requires current undergrad or grad in CS/Engineering/related with no sophomore/junior gate. Clearance eligibility is apply-form, not a resume class-year knockout.
- **Track:** full-stack + nuclear-enrichment / mission-critical hardware-adjacent
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on real-time constraints and fault-tolerant recovery (Web Worker / sub-5ms / 60 FPS; 27% upload recovery) — the generic SWE filter and the hardware-adjacent reliability signal both show in the top half.
- C++ and Python appear through use (Granular 16-voice / lock-free SPSC + Python delivery on Vylet/MDC); Flask/EC2 and Docker/Redis cover APIs and deployment.
- Binding ding: MDC's production Flask REST API has no traffic or latency number, so a skim can bucket it as a class project on a VM.

### Demerits

- **minor** · `Michigan Data Consulting (MDC)` · API bullet unquantified — the Flask REST API on AWS EC2 is the page's only production API-plus-cloud claim and lands with no traffic, latency, or consumer metric; sole-engineer / 5-month scopes the role, not the system

### Misreads

- MDC's unquantified Flask/EC2 line can be bucketed as "class project on a VM" instead of a shipped stakeholder API.

### Interview angles

- **Lead with:** CaseStudyPrep failure recovery and real-time UI-thread offload; Granular zero-alloc `processBlock`, lock-free SPSC, 16-voice polyphony / voice-stealing; Vylet name-collision defect (79% → 89%) as ownership / bias for action
- **Defend:** MDC API has no traffic/latency — point to the ETL scale (400 PACs / ~800 hours) and sole-engineer delivery *(out of rails: MDC pool has no API traffic/latency bullet; SignalWeaver FastAPI would size an API but adding it overflows the page)*; no CI/CD or observability on the page — CMake/release audit on Granular is the closest production-safety analog; clearance eligibility and South Bay commute are form answers, not resume lines
- **Depth prep:** walk Granular real-time constraints (zero-alloc audio thread, SPSC atomics, voice-stealing) for a systems/reliability screen; timed C++/Python DS&A (OA unpublished — do not assume HackerRank); mission / urgency / accountability behavioral plus proudest-accomplishment as a reliability story

## Likelihood

- **Resume screen:** High — C++ and Python through use, real-time plus operational recovery in the top half, one clean page with Expected May 2028
- **Overall hire odds:** Low — Unrated tiny-cohort Greenhouse intern; human PDF screen is the front-end filter, then an unpublished coding/systems loop and a mission bar closer to Anduril ~3–5% / SpaceX ~5–8% than a mid-size SWE intern
- **Funnel filters:** Greenhouse resume screen (PDF read early) · OA unpublished · tech loop unpublished (C++/Python + concurrency/system design flavor) · behavioral (urgency/accountability/Skunkworks) · form knockouts: U.S. clearance eligibility, South Bay commute for full 12 weeks, unofficial transcript
- **Outside the resume:** Warm Greenhouse referral; timed LC-style C++/Python plus concurrency walk-throughs; attach transcript; answer clearance and LA-commute honestly; frame proudest accomplishment as a reliability/real-time story
