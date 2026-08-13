# Software Engineer – Intern (US) at Citadel Securities

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028; current student returning to school after a summer internship
- **Track:** full-stack (quant/HFT low-latency systems + statistical research flavor; no track divergence)
- **Pipeline:** 4 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ lock-free / zero-allocation audio-thread work (SPSC FIFO, MemoryPool slab) plus an out-of-sample regression research platform sit in the top half — the two differentiators this screen actually tests.
- Titled production work carries metrics (CaseStudyPrep sub-5ms / 40% cost cut; MDC ETL ~800 hours / 400 PACs; Vylet 30x speedup).
- Binding ding: the C++ lead is design-dense but unsized (no callback/xrun/latency number), and Vylet’s closer is a GTM anecdote.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — SPSC FIFO and MemoryPool bullets never land a latency, callback-budget, or xrun number; the HFT-adjacent differentiator cannot be sized.
- **minor** · `Vylet` · off-axis product closer — geography-first / custard-shops bullet is GTM, not systems or quantitative engineering.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than trading-tech-adjacent real-time systems because the lead has no measured performance witness.
- Vylet’s bowling-alley closer can re-bucket the page as a founder/GTM story after a strong systems top half.

### Interview angles

- **Lead with:** Granular lock-free SPSC / zero-allocation MemoryPool / processBlock constraints; SignalWeaver OOS 3.39% R² regression + FastAPI p50/p99; CaseStudyPrep sub-5ms / 60 FPS and 40% inference-cost cut; MDC sole-ownership Flask/EC2 production pipeline.
- **Defend:** Granular has no latency/xrun number in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) as the ship gate, pivot measured latency to CaseStudyPrep *(out of rails: Granular latency/callback/xrun metric — pool has architecture/capacity/release-audit only)*. SignalWeaver has no GitHub in the pool — walk the OOS validation and FastAPI instrumentation from the page. Vylet geography bullet is filler for this loop — if asked, pivot to the 30x Docker/Redis/Celery ship.
- **Depth prep:** Timed HackerRank / LeetCode mediums until a medium is a ~20-minute solve (binding OA); C++ MemoryPool/SPSC/memory-ordering; probability/stats and the SignalWeaver OOS-R² story for the math-and-systems loop; Python production (FastAPI, Flask/EC2, ETL).

## Likelihood

- **Resume screen:** High — C++ lock-free systems + statistically validated research platform + production metrics; two minors dent polish, they do not flip the screen.
- **Overall hire odds:** Low — S-tier quant intern funnel (<1%); resume buys the HackerRank, not the offer. OA and math-and-systems rounds are the binding filters.
- **Funnel filters:** Application (required 150–300 word personal-story essay) → resume screen → hard HackerRank OA → 3–5 technical rounds · NYC or Miami onsite · 11-week summer.
- **Outside the resume:** Timed OA/DS&A plus probability drill; warm referral; apply in the opening wave (quant opens earliest); submit the personal-story essay — the resume is not the gate that hires you here.
