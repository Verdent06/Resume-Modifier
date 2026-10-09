# Data Engineering Intern, Summer 2027 at Mastercard

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside Dec 2027–June 2028; currently enrolled B.S.; prior SWE co-op satisfies previous internship; US citizen so the F-1/CPT/OPT sponsorship bar does not apply
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST on AWS EC2. Ingest → transform → serve for a Commerce Media / Offers Data Engineering intern, not SWE R-287618 and not notebook ML.
- Vylet carries injection-safe SQL freshness / re-scrape plus a Dockerized LangGraph pipeline (30x, Redis/Celery). Lyndbrook is a PWSID entity database plus 800→280 scoring. SignalWeaver serves FastAPI scores and pgvector retrieval.
- Binding dings are both minor: CaseStudyPrep is a one-line Voice AI / S3 co-op (required prior internship), and SQL is a DAL/freshness beat rather than a warehouse transform.

### Demerits

- **minor** · `CaseStudyPrep.AI` · single-bullet Voice AI, not a pipeline — required prior-internship slot is a Voice AI co-op whose only bullet is S3 audio-upload retries; no ETL, SQL, Pandas, or data model
- **minor** · `Vylet` · SQL is freshness/DAL not a transform — SQL appears as asyncpg timestamp validation that triggers re-scrapes, not a warehouse-style query, qualify, or persist step

### Misreads

- A skim that stops on CaseStudyPrep’s Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL and Vylet SQL/Docker pipeline the DE screen wants.
- Vylet’s PE/search-fund founder tagline can read as startup SaaS rather than a closed-loop data pipeline with a SQL DAL.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the Dockerized LangGraph pipeline (30x); Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver FastAPI scores + pgvector retrieval
- **Defend:** SQL is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next *(out of rails: only SQL bullet in the pool; llm-apis swap cannot bridge a SQL transform)*. CaseStudyPrep is S3 retry logic from a voice-AI co-op, kept because the JD requires a prior technical internship *(out of rails: pool is VAD / S3 / Web Workers; loop cannot omit this Experience entry)*. Do not claim PySpark, Databricks, Azure, Snowflake, Spark, Kafka, or Java
- **Depth prep:** HackerRank Easy–Med (doctrine; Extern also names Codility) **[directional]** — arrays/strings plus Python data work. Walk one ingest → transform → serve path (MDC) and one SQL-quality path (Vylet DAL). STAR for sole-engineer delivery and why Commerce Media / Offers data engineering (pipelines, not generic SWE R-287618). Decency Quotient behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — one-page Python/Pandas ETL → AWS EC2 serve spine with a prior co-op; remaining dings are flavor, not missing filters
- **Overall hire odds:** Medium — B-TIER ~8–12%; resume is the intern bottleneck and this page clears it, then Easy–Med HackerRank and DQ still drop most of the class. San Francisco onsite and no-PySpark honesty are residual risks
- **Funnel filters:** Workday Campus resume + unofficial transcript (bottleneck: resume) → HackerRank Easy–Med **[directional]** → recruiter phone ~15–30 min **[directional]** → 1–2 tech rounds → Decency Quotient behavioral · no intern sys design · ~8–12% · no visa sponsorship (F-1/CPT/OPT ineligible) · San Francisco · $35–$46/hr · rolling fill
- **Outside the resume:** Apply in this first wave (posted 2026-10-07); unofficial UMich transcript at submit; timed HackerRank; confirm San Francisco for Summer 2027; do not invent PySpark/Databricks. See `written-answers.md`
