# Software Engineering Intern (Modeling & Simulation) at Hermeus

## Verdict

- **Score:** 4.0 / 10 (6 demerits — 0 emergency, 1 major, 3 minor)
- **Eligibility:** eligible — JD requires a technical degree in progress and GPA ≥ 3.0 (3.66); no class-year gate on the posting. U.S. citizen meets export-control U.S. person. Apply-form junior-year question is not a JD filter (Spring 2027 still junior; Summer 2027 entering senior, Expected May 2028).
- **Track:** robotics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Thirty seconds register a C++ real-time numerical plugin (scheduler, zero-alloc audio thread, lock-free SPSC), then Pandas scientific computing, then a supporting real-time co-op — not PE GTM or LoRA finance.
- Physics (Mechanics) and Python/C++ through use are on the page; Julia is honestly absent.
- Binding ding: no vehicle dynamics, SITL, Monte Carlo, or sim-vs-flight-data. The lead is audio DSP, not 6DOF.

### Demerits

- **major** · `resume` · no 6DOF/SITL/aerospace simulation evidence — Mechanics is coursework only; the granular scheduler is audio DSP, not vehicle dynamics
- **minor** · `Granular Synthesizer Plugin` · metric-free — constrained-runtime C++ with no callback latency, CPU budget, or xrun figure
- **minor** · `Michigan Data Consulting (MDC)` · Flask API unquantified — ETL is sized; Flask/EC2 has no traffic or latency
- **minor** · `CaseStudyPrep.AI` · voice-AI product framing — last slot, validation-led, but the title is still Voice AI on an M&S packet

### Misreads

- An audio plugin plus a Voice AI co-op can still bucket as music/DSP rather than Flight Sciences SITL.
- Granular without a runtime number can read as hobby DSP rather than constrained-runtime systems.

### Interview angles

- **Lead with:** Granular fractional-accumulator scheduler, zero-alloc `processBlock`, lock-free SPSC, real-time safety audit; MDC Pandas ETL as scientific-computing Python; CSP silence-vs-audio filtering as model-vs-measured analog
- **Defend:** no Julia *(out of rails: not in inventory)*; no 6DOF/SITL/Monte Carlo/flight-data *(out of rails: no live pool entry; MatchStream is not selectable)*; Granular has no sized runtime *(out of rails: full 6-bullet pool has no allowlisted latency/CPU metric)*; Voice AI title *(out of rails: canonical header; entry cannot be dropped in the loop)*
- **Depth prep:** 6DOF / rigid-body / numerical integration from Physics (Mechanics); walk the granular scheduler and real-time constraints in C++; Python/Pandas for validation talk. Official intern loop: recruiter 20–30 min → technical/role 30–60 min → final team 15–30 min — no named OA. Do not prep as the Atlanta HIL intern.

## Likelihood

- **Resume screen:** Medium — C++ real-time leads; Python/Pandas in bullets; 6DOF/SITL still missing
- **Overall hire odds:** Low — Unrated defense-aviation intern, Lever human-read, unpublished OA, then recruiter plus technical/role interviews. Binding gap is domain evidence, not GTM filler
- **Funnel filters:** Lever resume screen · recruiter 20–30 min · technical/role-based 30–60 min (count unpublished) · final team 15–30 min · U.S. person export-control knockout · GPA 3.0 · no housing
- **Outside the resume:** Apply early on Lever; honest U.S. person / GPA / Spring-vs-Summer standing; first-principles numerical deep dive if the PDF clears — do not claim Julia
