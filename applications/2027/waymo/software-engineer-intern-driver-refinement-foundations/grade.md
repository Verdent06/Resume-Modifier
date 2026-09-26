# 2027 Summer Intern, BS, Software Engineer, Driver Refinement Foundations at Waymo

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — pursuing B.S. Computer Science (Expected May 2028) matches "Bachelor's in software engineering or a related field"; Summer 2027 = rising senior with Fall 2027 + Winter 2028 remaining; U.S. citizen (no sponsorship; export-license **No**)
- **Track:** full-stack + autonomy / AV reasoning-platform (C++ autolabeler / driver-refinement)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ leads: Granular zero-alloc `processBlock`, lock-free SPSC, real-time safety audit — the language floor this req screens for is unmissable.
- Data and quality-eval show next: CaseStudyPrep mines useful audio frames (VAD) and recovers a 27% upload failure; Vylet lifts eval faithfulness 50%→90% and qualification 79%→89%; MDC ETL is 400 PACs / ~800 hours plus a Flask/EC2 API; SignalWeaver ships pytest CI.
- Binding ding: Granular is audio DSP with no sized runtime outcome, so a Waymo skim can still read "plugin hobby" instead of autolabeler-grade C++.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — MemoryPool, SPSC FIFO, and the processBlock audit prove real-time C++, but nothing sizes the plugin
- **minor** · `Michigan Data Consulting (MDC)` · API bullet unquantified — Flask REST API on AWS EC2 has no traffic, latency, or consumer metric; 400 PACs / ~800 hours size the ETL, not the API

### Misreads

- Granular without a number can read as weekend DSP rather than hot-path C++ this team will probe.
- MDC's unquantified Flask/EC2 line can be bucketed as a class project on a VM instead of a shipped stakeholder API.

### Interview angles

- **Lead with:** Granular zero-alloc `processBlock`, lock-free SPSC, CMake/real-time audit (the C++ floor); CaseStudyPrep VAD as the honest analog to "mine useful events from a stream"; Vylet LangSmith eval + 79%→89% qualification as quality-metrics / experiment-and-report
- **Defend:** no ROS, no AV internship, no Linux claim *(inventory does not have them)*; Granular has no callback-latency / xrun / CPU number *(out of rails: full 6-bullet pool has no allowlisted runtime impact metric)*; MDC API has no traffic/latency — point at 400 PACs / ~800 hours and sole-engineer delivery *(out of rails: pool has no API metric)*; SignalWeaver is finance research + pytest CI, not driving logs
- **Depth prep:** timed C++ DS&A (Med–Hard; geometry / sensor-stream flavor **[directional]**); confirm OA vs live CoderPad on the invite (`companies.md` HackerRank vs Extern no-OA); walk testing (pytest CI + processBlock audit) without inflating it into unit/integration/regression coverage theater

## Likelihood

- **Resume screen:** Medium — C++ through use in the lead, data/metrics and a CI testing signal on one page; no AV/robotics and the C++ proof is audio
- **Overall hire odds:** Low — A-tier ~3–5%; bottleneck is tech rounds, not the PDF
- **Funnel filters:** Greenhouse knockouts (sponsorship, export license, Alphabet history, no-unauthorized-AI ack) → human resume screen → recruiter ~30 min **[directional]** → HackerRank (`companies.md`) or live CoderPad **[directional, Extern]** → 4 rds Med–Hard · bottleneck tech rounds
- **Outside the resume:** Apply this week (rolling, `first_published` 2026-09-25); no Waymo contact in `network.md` — do not invent a referral; C++ timed practice; honest "I have not shipped robot software" with Granular + VAD + eval-harness as the substitute
