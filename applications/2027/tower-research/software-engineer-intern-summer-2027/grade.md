# Software Engineer Intern (Summer 2027) at Tower Research Capital

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — current B.S. CS student (Expected May 2028); JD requires Bachelor's/Master's/PhD in CS or related; no class-year knockout; returns to school after Summer 2027
- **Track:** full-stack + low-latency / HFT trading-systems / market-data infra
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lock-free C++ (Granular — SPSC FIFO, zero-allocation MemoryPool, `processBlock()` constraints) leads; SignalWeaver follows with 49ms p50 search and FastAPI p50/p99; MDC is a real ingest + Flask/EC2 ship.
- SQL is in a Vylet asyncpg DAL bullet, not Skills-only. CS + Economics and May 2028 class year are in window. No invented Go, Java, Rust, FPGA, or trading desk.
- Binding dings: Granular is unsized (no latency/xrun/CPU number), and CaseStudyPrep.AI is a one-line co-op.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC and MemoryPool never close with a latency, throughput, or xrun number a latency firm can size.
- **minor** · `CaseStudyPrep.AI` · single bullet — titled Voice AI co-op is one 5ms / 60 FPS line; the role looks thinner than the title.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than trading-tech-adjacent real-time systems because the lead has no measured hot-path witness.
- CaseStudyPrep’s “Voice AI” title on a single bullet can misfile the middle of Experience as a thin ML co-op if the reader skips the 5ms / 60 FPS hook.

### Interview angles

- **Lead with:** Granular lock-free SPSC / zero-allocation MemoryPool / `processBlock()` constraints; SignalWeaver pgvector 49ms p50 search and FastAPI scoring p50/p99; MDC Pandas ETL ingest + production Flask/EC2; CaseStudyPrep sub-5ms / 60 FPS as the measured real-time number; Vylet injection-safe SQL + 79%→89% correctness fix.
- **Defend:** Granular has no processBlock latency/CPU/xrun in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) and pivot measured latency to CaseStudyPrep / SignalWeaver *(out of rails: Granular hot-path timing — full 6-bullet pool is architecture/capacity/DSP/release-audit only)*. CaseStudyPrep stays one bullet — adding the RxJS 27% retry overflowed the page *(out of rails: second CaseStudyPrep bullet vs one-page budget; anti-deletion blocks cutting other iter-1 lines)*. No Go/Java/Rust — JD is an or-list; interview in C++ or Python. No Linux line in the inventory — do not claim it. No trading-desk internship — CS + Economics plus SignalWeaver is the honest markets story. Do not lead with LoRA/agent pipelines or invent FPGA.
- **Depth prep:** Timed DS&A in C++ (preferred) or Python until a medium is a ~20-minute solve; SQL (OA includes a SQL question). HackerRank **[directional]** ~90 min: CS MCQ + SQL + 2 coding (India-campus analog 2h / 10 MCQ + 3 coding). Tech: 1–2 rounds DSA + probability; project deep-dive on Granular threading/memory and MDC ingest. Behavioral: markets interest without fake desk experience.

## Likelihood

- **Resume screen:** High — C++ and Python are in bullets, SQL is in a real DAL bullet, class year is in window; two minors dent polish, they do not flip the screen.
- **Overall hire odds:** Low — S-tier quant intern funnel (<1–2%); the resume buys the OA invite, not the offer. Binding filters are a Med–Hard OA then 1–2 tech rounds.
- **Funnel filters:** Greenhouse 8212158 resume → OA (~90 min CS MCQ + SQL + 2 coding; HackerRank **[directional]**) → 1–2 tech (DSA + probability) → behavioral · NYC Equitable Building / FiDi onsite · Summer 2027 · $3,500–$4,200/wk anticipated + housing + meals.
- **Outside the resume:** Apply in the first wave (quant/HFT earliest cycle). Drill timed C++/Python DS&A plus SQL and probability. Honest language depth — do not invent Go, Java, Rust, or FPGA on the form.
