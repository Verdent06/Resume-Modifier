# Intern Robotics Software Engineering at Smith+Nephew

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — currently matriculated UMich CS undergrad (Expected May 2028); Summer 2027 = rising junior; GPA 3.66 ≥ 3.0 preferred; US citizen (no visa sponsorship)
- **Track:** full-stack + surgical-robotics NPD / medical-device QMS
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume: C++ zero-alloc / lock-free / CMake `processBlock` audit leads, then a Voice-AI co-op (27% upload-failure recovery), then a founder product with a named defect (79%→89%) and a hard-fail gate — on-axis for Pittsburgh CORI NPD whose JD prefers C++/OOP/SDLC, not ROS.
- C++ and Python are proven in bullets; UML tools, ROS, surgical-robot internships, firmware, Snowflake/Databricks/Tableau/Copilot/Fusion are not invented. Class year and GPA are in window.
- Binding ding: Granular has no sized runtime metric (latency / xrun / CPU).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — MemoryPool, lock-free SPSC, and CMake/processBlock audit are the C++/QMS-adjacent signal, but none sizes callback latency, xruns, or CPU

### Misreads

- A rushed robotics skim can file this as "hobby audio intern, no robots" before the lock-free C++ / release-gate checklist and the co-op test/debug land.

### Interview angles

- **Lead with:** Granular CMake real-time safety audit, zero-allocation `MemoryPool`, lock-free SPSC (deterministic C++ under a hard deadline); CaseStudyPrep 27% upload-failure debug + Web Worker real-time; Vylet named defect (79%→89%) and Node 3 hard-fail gate; SignalWeaver pytest + GitHub Actions
- **Defend:** Granular has no xrun/latency/CPU metric on the page. *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one.)* No ROS/Gazebo/SLAM. No UML-tool experience (class diagrams of MemoryPool/SPSC if asked). No surgical-robot, medical-device, or firmware internship. MDC and SpaceXAI Campus Lead Ambassador are extracurricular, not employers. Awards/honors: none
- **Depth prep:** C++ OOP (slab allocators, atomics, `processBlock` constraints, CMake release gates); unit/integration-test stories (safety checklist, pytest CI, named production defect); QMS documentation analog without claiming device software; STAR for presenting to senior leaders (Vylet clients / intern readout). Light DS&A if they add a coding screen. Do not fake CORI/NAVIO internals or UML certification

## Likelihood

- **Resume screen:** High — eligible class year and GPA, C++ in bullets with lock-free/CMake depth in the lead slot, a real co-op, Python OOP, pytest CI; one minor dents the scan, it does not flip it to a no
- **Overall hire odds:** Medium — no published coding OA, so most front-end elimination is this PDF plus the no-sponsorship knockout, then 2–3 Easy–Med practical/competency rounds at a ~10–15% B-tier medical-device intern accept rate (peer Medtronic). Pittsburgh 12-week onsite May 2027 is a logistics filter this page cannot show
- **Funnel filters:** Workday apply (closes **2026-09-25**) → TA resume screen → possible technical questioning / HireVue / Modern Hire psychometric per official careers page **[directional]** → HM + teammate competency interview · no named intern OA · no intern sys design · no visa sponsorship · CS/CE undergrad · GPA 3.0 preferred
- **Outside the resume:** Apply in this window (posted 2026-09-17, `endDate` 2026-09-25); form email `verdent06@gmail.com`; US citizen **Yes**, sponsorship **No**; confirm Pittsburgh May–August 2027 (12 weeks) and Fall 2027 return to Michigan. No Smith+Nephew contact in `network.md`
