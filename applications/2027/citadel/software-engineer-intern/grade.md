# Software Engineer – Intern (US) at Citadel

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028; current student returning to school after a summer internship
- **Track:** full-stack (hedge-fund investment-tech: high-performance research platforms + statistical rigor + production APIs; no track divergence)
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ lock-free / zero-allocation audio-thread work (SPSC FIFO, MemoryPool slab) plus an out-of-sample regression research platform sit on the page — the two differentiators this hedge-fund SWE screen actually tests.
- Titled production work carries metrics (MDC ETL ~800 hours / 400 PACs; Vylet 30x / 79%→89%; SignalWeaver FastAPI 9.1s p50 / 15.2s p99 and 3.39% OOS R²).
- Binding ding: the C++ lead is design-dense but unsized (no callback/xrun/latency number), and the Flask/EC2 API is unsized.

### Demerits

- **minor** · `MDC` · metric-free production API — Flask REST on AWS EC2 never lands latency, throughput, or scale.
- **minor** · `Granular Synthesizer Plugin` · metric-free systems depth — SPSC FIFO and MemoryPool bullets never land a latency, callback-budget, or xrun number.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than investment-tech-adjacent real-time systems because the lead has no measured performance witness.
- MDC's unsized API can re-bucket the production-platform claim as nonprofit ETL rather than the web-framework work this intern job actually is.

### Interview angles

- **Lead with:** Granular lock-free SPSC / zero-allocation MemoryPool / processBlock constraints; SignalWeaver OOS 3.39% R² regression + FastAPI p50/p99; MDC sole-ownership Flask/EC2 production pipeline; Vylet Docker/Redis/Celery 30x Python ship.
- **Defend:** Granular has no latency/xrun number in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) as the ship gate *(out of rails: Granular latency/callback/xrun metric — pool has architecture/capacity/release-audit only)*. MDC Flask/EC2 has no traffic number — pivot sized APIs to SignalWeaver FastAPI instrumentation *(out of rails: MDC API latency/throughput/users — pool has ETL scale and ownership only)*. No trading-desk internship — CS + Economics, stats coursework, and a research platform; do not invent desk experience. SignalWeaver has no GitHub in the pool — walk the OOS validation and FastAPI instrumentation from the page; send granular-synth for a code link.
- **Depth prep:** Timed HackerRank / LeetCode mediums until a medium is a ~20-minute solve (binding OA); C++ MemoryPool/SPSC/memory-ordering; probability/stats and the SignalWeaver OOS-R² story for the math-and-systems loop; Python production (FastAPI, Flask/EC2, ETL).

## Likelihood

- **Resume screen:** High — C++ lock-free systems + statistically validated research platform + production Python; two minors dent polish, they do not flip the screen.
- **Overall hire odds:** Low — S-tier quant intern funnel (<1%); resume buys the HackerRank, not the offer. OA and math-and-systems rounds are the binding filters.
- **Funnel filters:** Application (150–300 word personal-story essay + technical links) → resume screen → hard HackerRank OA → 3–5 technical rounds · NYC onsite · 11-week summer. Core intern languages: Python and C++.
- **Outside the resume:** Timed OA/DS&A plus probability drill; warm referral; apply in the opening wave (quant opens earliest); submit the personal-story essay — the resume is not the gate that hires you here. This posting is Citadel the hedge fund, not Citadel Securities.
