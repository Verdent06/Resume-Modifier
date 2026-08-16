# 2027 Software Engineer Intern at Anduril Industries

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** ambiguous — Expected May 2028 vs Summer 2027: Fall 2027 + Winter 2028 remain (returning-to-school pass); B.S. Computer Science matches listed degrees; U.S. Person is not recorded in `context.md` (gate uncomputable)
- **Track:** full-stack + autonomy / mission-critical defense
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on real-time constraints and operational root-cause (Web Worker / sub-5ms / 60 FPS; 27% upload recovery; 40% inference-cost cut) — the generic SWE filter and the differentiator both show in the top half.
- C++ and Python appear through use (Granular + Python delivery); Flask/EC2, Redis/Docker, and Angular/RxJS cover API, cloud, and frontend.
- Binding ding: Granular is deep real-time C++ with no sized runtime outcome, so a skim can read hobby DSP instead of mission-critical discipline.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — MemoryPool, SPSC FIFO, and the processBlock audit prove real-time C++ discipline, but nothing sizes the plugin — no voice count, no latency budget, no users
- **minor** · `MDC` · API bullet unquantified — the Flask REST API on AWS EC2 is the page's only production API-plus-cloud claim and lands with no traffic, latency, or consumer metric; sole-engineer / 5-month scopes the role, not the system

### Misreads

- Granular without a number can read as weekend DSP rather than the lock-free / zero-alloc systems proof an autonomy screener wants.
- MDC's unquantified Flask/EC2 line can be bucketed as "class project on a VM" instead of a shipped stakeholder API.

### Interview angles

- **Lead with:** CaseStudyPrep failure recovery and real-time UI-thread offload; Granular zero-alloc `processBlock`, lock-free SPSC, real-time safety audit; Vylet name-collision defect (79% → 89%) as ownership / bias for action
- **Defend:** Granular has no callback-latency / xrun / CPU number on the page *(out of rails: full 6-bullet pool has no allowlisted runtime impact metric; sized-looking swaps overflowed)*; MDC API has no traffic/latency — point to the ETL scale (400 PACs / ~800 hours) and sole-engineer delivery; JD names Go/Rust/Java the inventory does not have — do not fake them
- **Depth prep:** timed HackerRank mediums (graphs/DP/DS; vague prompts; pathfinding / sensor-network framing); walk Granular real-time constraints for the practical loop; mission / ownership behavioral for Super Day

## Likelihood

- **Resume screen:** High — C++ and Python through use, real-time plus operational debugging in the top half, one clean page with Expected May 2028
- **Overall hire odds:** Low — A-tier ~3–5%; binding filters are a Medium HackerRank and a 4-hour practical onsite, not the PDF
- **Funnel filters:** Greenhouse resume screen · recruiter (~30 min, mission) · HackerRank Medium (~60 min) · 4-hr Super Day (coding + practical/systems + behavioral) · U.S. Person apply-form knockout
- **Outside the resume:** Warm Greenhouse referral; timed LC-mediums; mocks aimed at the practical onsite and defense-mission conviction — confirm U.S. Person on the form honestly
