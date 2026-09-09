# Software Engineering Internship (Summer 2027) at Two Sigma

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — JD requires only coursework toward a technical or quantitative degree; Expected May 2028 is a current B.S. CS + Economics student with no class-year knockout on the posting
- **Track:** full-stack + high-performance trading / data-ingestion (fintech-backend / low-latency)
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lock-free C++ (`processBlock()`, SPSC FIFO, MemoryPool slab) leads the page; SignalWeaver follows with measured Python search/API p50/p99; MDC is a real ingest + Flask/EC2 ship.
- Class year, CS + Economics, and stats coursework are in window. C++ and Python are in bullets, not Skills-only. No invented Java or trading desk.
- Binding dings: Granular is unsized (no latency/throughput number), and Lyndbrook still reads as search-fund deal-sourcing under a resume-bottleneck S-tier screen.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC and zero-alloc MemoryPool never close with a latency, throughput, or xrun number a performance shop can size.
- **minor** · `Lyndbrook Capital` · off-axis framing — PWSID entity database and a 35% search-fund shortlist read as acquisition-consulting, not trading-infra or 10k-source ingest.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than high-performance systems because the lead has no measured hot-path witness.
- Lyndbrook can get the page bucketed as “consulting / search-fund GTM” after a strong C++ open, which is the wrong pile at this firm.

### Interview angles

- **Lead with:** Granular lock-free SPSC / MemoryPool / `processBlock()` constraints; SignalWeaver pgvector 49ms p50 search and FastAPI scoring p50/p99; MDC Pandas ETL ingest + production Flask/EC2; CaseStudyPrep sub-5ms / 60 FPS real-time handoff and S3 retry path.
- **Defend:** No Java/C/Ruby/Perl — JD is an OR list; honest C++ and Python in bullets. No trading-desk internship — analogize from real-time constraints and ingest/API work, do not invent a desk. Granular has no latency/xrun number in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) and pivot measured latency to CaseStudyPrep / SignalWeaver *(out of rails: Granular metric-free — pool is architecture/capacity/release-audit only)*. Lyndbrook is a short search-fund data engagement — own the frame, do not dress it as a trading system *(out of rails: every Lyndbrook bullet is acquisition intelligence; anti-deletion kept the entry)*.
- **Depth prep:** Hard CodeSignal plus C++/Python DS&A until a medium is a ~20-minute solve; concurrency/memory-ordering and `processBlock()` constraints; official loop may add systems-design and OOP in C/C++/Java/Python; some candidate OA reports add stats/OLS/incremental-processing flavor — invitation text controls. Walk MDC ingest/API and SignalWeaver p50/p99 trade-offs.

## Likelihood

- **Resume screen:** Medium — C++ first-read plus Python ingest/API is the right shape; two minors dent polish at a firm whose published bottleneck is the resume.
- **Overall hire odds:** Low — S-tier quant intern funnel (<1%); Hard CodeSignal and a systems-capable loop eliminate most people who pass paper.
- **Funnel filters:** Avature apply → resume screen (bottleneck) → CodeSignal (Hard; official page does not name the platform) → technical loop (official: up to ~3 rounds; first block often three 60-min DS&A/OOP sessions in C/C++/Java/Python; systems-design possible) → project/experience conversations · Soho NYC · 10 weeks · $3,800/week Bachelor's.
- **Outside the resume:** Apply immediately (quant cycle is earliest). Engineer referral beats cold Avature. Timed C++/Python DS&A; stats/regression fluency if the OA invitation looks quantitative; do not invent Java for the form.
