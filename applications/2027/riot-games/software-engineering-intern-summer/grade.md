# Software Engineering Intern - Summer 2027 (Remote) at Riot Games

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 matches JD “graduating in the 2028 calendar year”; GPA 3.66 ≥ 2.5; US citizen, no sponsorship
- **Track:** full-stack + live-game / player-facing real-time services
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads with player-adjacent real-time work — sub-5ms UI thread, 60 FPS visualizer, 27% upload recovery, 40% inference-cost cut — so the live-game differentiator lands in the top half.
- Granular Synthesizer Plugin puts C++ OOP on the page (MemoryPool audio thread, lock-free SPSC) — the JD’s Java/C++/C# floor, hit honestly, without inventing Unity or Unreal.
- Vylet production services + MDC Flask REST on EC2 cover backend/API/ownership; SignalWeaver adds FastAPI + GitHub Actions CI for the desired SDLC flavor.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Both C++ real-time bullets are technically deep (zero-allocation MemoryPool audio thread; lock-free SPSC UI-to-audio) but carry no quantified latency, throughput, or performance delta; live-game teams size real-time work by numbers, not only constraint narratives.

### Misreads

- Granular without a number can skim as “audio hobby” rather than engine-grade real-time systems — the lock-free / zero-alloc depth is easy to underweight in 7 seconds.

### Interview angles

- **Lead with:** CaseStudyPrep Web Worker / 60 FPS / expired-S3 recovery; Granular MemoryPool + SPSC real-time safety; MDC sole-engineer Flask API on EC2
- **Defend:** Granular has no callback-latency / xrun / CPU number on the page *(out of rails: entire Granular pool is constraint engineering with no impact metric; swap sets cannot add one)* — narrate `processBlock()` rules and what you would measure. No Unity, Unreal, Java, or C# — do not invent a ranked League/VALORANT identity; product pick is engineering interest, not a fabricated main
- **Depth prep:** Timed HackerRank mediums (Riot intern study guide Vol. 4); C++ OOP + lock-free walkthrough; backend API/ownership stories (MDC, Vylet 79%→89%); behavioral / player-empathy without faking a ladder rank (`recruiting.md` §6 is a filter)

## Likelihood

- **Resume screen:** High — on-axis full-stack + real-time C++ + production shipping; 2028 / 2.5 gates clear; one minor ding
- **Overall hire odds:** Medium — B-tier ~8–12%; HackerRank OA then Easy–Med craft + values behavioral are the binding filters after the PDF
- **Funnel filters:** Greenhouse knockouts (2028 grad, US auth, no sponsorship, 40h remote, 18+) → HackerRank SWE craft test → recruiter screen → DS&A craft → behavioral/values · Bottleneck: OA then tech · close Nov 6 2026
- **Outside the resume:** Apply in this first wave (first_published 2026-10-01); no Riot contact in `network.md`; transcript upload is required on Greenhouse; do not submit from this agent
