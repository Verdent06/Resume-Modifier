# Data Engineer Intern at Coinbase

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027 intern (JD has no class-year filter); Greenhouse knockout "available to begin a potential full-time role before September 2028" — May 2028 is before September 2028
- **Track:** ai-ml + crypto / fintech-backend / exchange-platform data
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST on AWS EC2. Ingest → transform → serve for a Platform data-engineer intern, not a generic SWE seat and not notebook ML.
- Lyndbrook sits in the lead window as the finance / high-integrity-data analog: EPA/MassGIS → PWSID entity database + 800→280 scoring at 35% precision. Vylet carries injection-safe SQL freshness/validation, a 79→89% name-collision quality fix, and a Dockerized LangGraph pipeline (30x) with Redis/Celery.
- Binding ding: none. Python (Pandas/Flask/LangGraph) and SQL are through use. FastAPI + React/Postgres dashboard is the analytics/API analog. No invented Snowflake, Databricks, Copilot, Fusion, Tableau, Spark, GCP, or Azure.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML if the reader never reaches the FastAPI serve + Postgres persist + dashboard lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape and 79→89% quality lines.
- Greenhouse/ATS may keyword-miss Snowflake / Databricks / Spark / GCP that this PDF honestly does not name.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the 79→89% anomaly fix and Dockerized LangGraph pipeline (30x, Redis/Celery); Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver FastAPI scores + React/TypeScript dashboard persisted to Postgres as the analytics/API analog
- **Defend:** No Snowflake, Databricks, Tableau, Spark, Kafka, Airflow, GCP, or Azure — JD cloud is AWS/GCP/Azure and inventory is AWS EC2; say Python/SQL/Pandas/Postgres/AWS and ramp on their warehouse. SQL on the page is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next. No crypto-exchange or matching-engine work — the analog is finance / high-integrity multi-source data, not on-chain keyword stuffing. Do not claim day-one ownership of Coinbase Platform pipelines. Skip LoRA / ML-research framing.
- **Depth prep:** CodeSignal Easy–Med (`companies.md`; ~90-min proctored, practical/fintech-flavored **[directional]**). Walk one ingest → ETL → serve path (MDC) and one quality/governance path (Vylet DAL + name-collision). Python DS&A as the JD floor. STAR for ownership (MDC sole engineer; Vylet founder). Behavioral is a filter (`recruiting.md` §6). Hybrid SF + quarterly surges and the FT-before-Sep-2028 knockout are operational — confirm logistics. Max 3 applications in 6 months.

## Likelihood

- **Resume screen:** Medium — on-axis DE spine (ETL → API on EC2, SQL freshness, Dockerized pipeline) but Coinbase's resume gate rejects ~95% even when the paper is clean
- **Overall hire odds:** Low — B-tier Very selective; CodeSignal Easy–Med still eliminates after a pass, hybrid SF + quarterly surges and the FT-before-Sep-2028 knockout add process drop-off. A clean intern DE page is necessary and not sufficient
- **Funnel filters:** Greenhouse resume (bottleneck; ~95% reject) → CodeSignal OA (Easy–Med) → recruiter → 3–4 rds, light intern sys design (`companies.md`). FT availability before September 2028 is a Greenhouse knockout. Comp $50/hr; 12-week Summer 2027; Hybrid SF; max 3 applications in 6 months. CEO reviews every offer
- **Outside the resume:** Apply in this first-wave window (first published 2026-09-08). Treat CodeSignal as the next real filter (`recruiting.md` OA-gated intern). Do not burn the 3-applications-in-6-months cap on off-axis Coinbase reqs. Confirm hybrid SF / surge travel and no sponsorship on the form
