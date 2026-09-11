# Systematic Trading Technology Software Engineer (Summer 2027, New York) at Brevan Howard

## Verdict

- **Score:** 6.0 / 10 (4 demerits — 0 emergency, 1 major, 1 minor)
- **Eligibility:** eligible — JD requires penultimate-year undergraduate/junior (or 1st-year master's/PhD) with degree awarded before July 2028; Expected May 2028 is before July 2028 and is junior / penultimate year for Summer 2027
- **Track:** full-stack
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lock-free C++ (`processBlock()`, SPSC FIFO, MemoryPool slab, real-time safety audit) leads; SignalWeaver follows with measured Python search/API p50/p99 and a TypeScript dashboard; MDC is a real ingest + Flask/EC2 ship.
- Class year, CS + Economics, and stats/econ coursework are in window. Python, TypeScript, and SQL are on the page. No invented Java, Excel/VBA/R, or trading desk.
- Binding ding: Java is a JD-required language and is wholly absent. Granular is architecturally strong but unsized (no latency/throughput number).

### Demerits

- **major** · `resume` · Java absent — JD requires programming experience in Java as a floor skill; the page has zero Java in Skills or bullets. At STT that is a filter-shaped gap, not a plus-list miss.
- **minor** · `Granular Synthesizer Plugin` · metric-free — SPSC FIFO, zero-alloc MemoryPool, and the real-time safety audit never close with a latency, throughput, or xrun number a trading-platform team can size.

### Misreads

- A Java-first screener can no-pile the packet before reading the C++ hot-path, because the required language is missing.
- Granular can get bucketed as hobby audio DSP rather than production-style low-latency systems because the lead has no measured hot-path witness.

### Interview angles

- **Lead with:** Granular lock-free SPSC / MemoryPool / `processBlock()` constraints and the real-time safety audit; SignalWeaver pgvector 49ms p50 search and FastAPI scoring p50/p99; MDC Pandas ETL ingest + production Flask/EC2; CaseStudyPrep sub-5ms / 60 FPS real-time handoff and S3 retry path.
- **Defend:** No Java — JD lists it as required; honest Python/TypeScript/SQL/C++ in bullets, will ramp, will not fake a Spring interview *(out of rails: Java not in the active pool; MatchStream is commented out)*. No Excel/VBA/R — training week covers Excel/Python; do not claim them. No trading-desk internship — analogize from real-time constraints and ingest/API work. Granular has no latency/xrun number in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) and pivot measured latency to CaseStudyPrep / SignalWeaver *(out of rails: Granular metric-free — pool is architecture/capacity/release-audit only)*.
- **Depth prep:** Unpublished intern OA/loop (generic sketch: recruiter + 45–60m tech + behavioral — **[directional, not confirmed for JR101597]**). DS&A until a medium is a ~20-minute solve in Python or C++; concurrency/memory-ordering and `processBlock()` constraints; walk MDC ingest/API and SignalWeaver p50/p99 trade-offs. Do not prep a Java interview you cannot sit. Markets/Excel/Python training week is taught — do not pretend prior desk experience.

## Likelihood

- **Resume screen:** Medium — lock-free C++ first-read plus Python ingest/API is the right shape; the Java floor is the binding paper ding at a firm whose published bottleneck is resume + tech.
- **Overall hire odds:** Low — A-tier macro intern funnel (~2–5% **[directional]**); unpublished tech screen plus the Java gap eliminate most people who pass paper.
- **Funnel filters:** Workday (`BH_ExternalCareers`) JR101597 → resume screen (bottleneck with tech) → unpublished intern OA/loop · no intern sys design published · New York 10 weeks · $150,000 annualized + housing stipend + completion bonus · degree awarded before July 2028 · one global SIP application.
- **Outside the resume:** Apply immediately (posted 2026-09-10). No Brevan Howard contact in `network.md` — do not claim a referral. Timed Python/C++ DS&A; do not invent Java on the form.
