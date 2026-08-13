# Summer 2027 Software Engineering Intern at PDT Partners

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is after Fall 2027 and maps to FT start in 2028
- **Track:** full-stack (quant trading-lifecycle systems flavor; no track divergence)
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ lock-free / zero-allocation `processBlock()` work (SPSC FIFO, MemoryPool slab, real-time audit) sits in the first-read window; Python ETL/API (MDC Flask/EC2) and a no-LLM consensus gate (Vylet) cover data/batch.
- Class year and CS + Economics are in window; no invented trading-desk internship.
- Binding ding: the C++ lead is architecture-dense but unsized — no latency, CPU, jitter, or throughput number.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC, slab MemoryPool, and zero-alloc/zero-lock `processBlock()` never close with a measured hot-path number; efficiency stays qualitative.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than trading-lifecycle-adjacent real-time systems because the lead has no measured performance witness.

### Interview angles

- **Lead with:** Granular lock-free SPSC / MemoryPool / `processBlock()` constraints; MDC Pandas ETL + production Flask/EC2; Vylet pure-Python consensus gate and 79%→89% name-collision fix; CaseStudyPrep sub-5ms / 60 FPS real-time handoff.
- **Defend:** Granular has no latency/CPU/xrun number in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) as the ship gate, pivot measured latency to CaseStudyPrep *(out of rails: Granular latency/CPU/xrun metric — pool has architecture/capacity/release-audit only; 16-voice swap overflowed the page)*. No trading-desk internship — analogize from real-time constraints and financial-data pipelines, do not invent a desk. SignalWeaver is not on this page; if asked for more financial-data work, walk it honestly as a research assistant with no GitHub in the pool.
- **Depth prep:** Timed C++ and Python DS&A until a medium is a ~20-minute solve (unpublished remote coding assessment is the binding gate); MemoryPool/SPSC/memory-ordering; Python production (Flask/EC2, Pandas ETL); correctness vocabulary (resource management, thread safety, exception safety) for the project deep-dive.

## Likelihood

- **Resume screen:** High — C++ and Python in bullets, real-time systems in the first-read window, Python data/batch behind it; one minor dents polish, it does not flip the screen.
- **Overall hire odds:** Low — S-tier systematic quant intern funnel (<1–2%); resume buys the coding assessment, not the offer.
- **Funnel filters:** Greenhouse application (GPA, why quant finance, GitHub) → rolling resume screen (~3-week feedback) → unpublished remote coding (C++/Python/Java per FT loop reports) → technical/behavioral loop · NYC onsite · 10 weeks early June–mid August · $180k annualized.
- **Outside the resume:** Timed C++/Python DS&A; a concrete Greenhouse “why quant finance” (see `written-answers.md`); warm referral if available; apply in this listing window (reported through ~August 30 2026).
