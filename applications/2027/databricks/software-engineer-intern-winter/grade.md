# Software Engineering Intern (2027 Start) – Winter at Databricks

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 = spring 2028; JD window is fall 2027 or spring 2028; Winter 2027 (Jan–Apr) is junior-year with return to school
- **Track:** full-stack + data/AI infrastructure / lakehouse platform
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python Requests/Pandas ETL (~800 hours across 400 PACs) plus a sole-owned Flask REST API on AWS EC2 — data-pipeline + backend, not a lakehouse-product name-drop.
- SignalWeaver carries FastAPI p50/p99 scores, 49ms pgvector search, and Docker Compose / GitHub Actions; Granular shows C++ zero-alloc MemoryPool and lock-free SPSC FIFO for the concurrency-round adjacency.
- Binding ding: Granular never sizes the systems win (no callback latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc MemoryPool and lock-free SPSC FIFO are the C++/concurrency signal this intern loop actually probes, but neither bullet sizes callback latency, xruns, or CPU — a skim still buckets it as hobby DSP rather than systems software.

### Misreads

- Granular without a number can read as an audio hobby rather than the lock-free / zero-alloc discipline Databricks's concurrency round actually probes.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (shipped data pipeline / API); SignalWeaver async FastAPI + pgvector search + Docker Compose (storage/query-adjacent platform); Granular MemoryPool / lock-free SPSC (single-machine concurrency — the `companies.md` bottleneck, not Spark)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints (no heap, no mutex on `processBlock`) and what you would measure. Java is not in inventory — do not invent it; Python and C++ are the honest JD languages. Do not claim Databricks products (Lakehouse, Unity Catalog, Spark-as-employer, Genie, Lakebase, Agent Bricks, Lakeflow) or Snowflake/Tableau/Copilot/Fusion. Vylet's PE/search-fund title is a lead-sourcing product with SQL DAL + 79%→89% defect fix — pivot to pipeline/data-quality, not GTM.
- **Depth prep:** CodeSignal mediums (intern reports: ~70 min / 4Q, data-processing slant); single-machine concurrency (mutexes, atomics, lock-free SPSC, memory ordering) for the bottleneck round; MDC ETL→REST ownership; SignalWeaver p50 vs p99 and pgvector cosine search. Behavioral is a filter round (`recruiting.md`), not the differentiator.

## Likelihood

- **Resume screen:** High — Python ETL + Flask REST leads, C++ lock-free and FastAPI/pgvector/Docker on the page, Expected May 2028 visible; one minor does not sink a Greenhouse intern screen
- **Overall hire odds:** Medium — A-tier <3%, CodeSignal then a genuinely hard concurrency round (`companies.md`); the PDF can clear, then OA + concurrency decide it. Winter 2027 eligibility matches spring 2028 graduation
- **Funnel filters:** Greenhouse 8732364002 / P-1588 → resume screen → CodeSignal OA → CoderPad tech → 3–4 rds Med–Hard including concurrency (single-machine) + light sys design · Bottleneck: concurrency · <3%; Bellevue this apply; Winter 2027 Jan–Apr only; export-control license at employer discretion
- **Outside the resume:** Apply in the first wave of this Winter req (posted as of 2026-08-21); a Databricks engineer/HM referral past the cold Greenhouse pile; drill CodeSignal mediums and single-machine concurrency before the bottleneck round; intern behavioral is a filter
