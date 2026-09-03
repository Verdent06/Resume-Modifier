# Data Science/ Data Engineer Intern at Hadrian

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside JD window December 2027–June 2028; current CS student; U.S. citizen / U.S. person (ITAR); can be onsite LA
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST on AWS EC2. Ingest → transform → serve for the factory data-backbone intern, not SWE intern and not Robotics intern.
- Vylet carries injection-safe SQL freshness (asyncpg timestamp validation / re-scrape) plus a Dockerized LangGraph pipeline (30x). Lyndbrook is multi-source entity resolution and an 800→280 scoring closer (yield analog). SignalWeaver is the dashboard + FastAPI serve analog.
- Binding dings are both minor: CaseStudyPrep is a one-line Voice AI / S3 upload co-op, and SQL is a DAL/freshness beat rather than a warehouse transform.

### Demerits

- **minor** · `CaseStudyPrep.AI` · single-bullet Voice AI, not a pipeline — Experience slot is a Voice AI co-op whose only bullet is S3 audio-upload retries; no ETL/ELT, SQL, Pandas, dashboard, or factory-data analog
- **minor** · `Vylet` · SQL is freshness/DAL not a transform — required SQL appears as asyncpg timestamp validation that triggers re-scrapes, not a warehouse-style query, qualify, or persist step

### Misreads

- A skim that stops on CaseStudyPrep's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL and Vylet SQL/Docker pipeline the factory data screen wants.
- Vylet's PE/search-fund founder tagline can read as startup SaaS rather than a closed-loop data pipeline with a SQL DAL.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the Dockerized LangGraph pipeline (30x); Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver React dashboard + FastAPI serve
- **Defend:** SQL is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next *(out of rails: only SQL bullet in the pool; llm-apis swap cannot bridge a SQL transform)*. CaseStudyPrep is S3 retry logic from a voice-AI co-op, not a factory pipeline *(out of rails: pool is VAD / S3 / Web Workers; loop cannot omit this Experience entry — min_entries 5)*. Do not claim Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, Prefect, dbt, Airflow, or Spark. Do not claim MatchStream / FRC telemetry (not in the live pool). Do not claim day-one ownership of Hadrian's warehouse.
- **Depth prep:** Unpublished intern OA (`company.md`; new-grad LC-medium is directional, not intern-canonical). Walk one ingest → ETL → serve path (MDC) and one SQL-quality path (Vylet DAL). If they ask for a stats/ML prototype: SignalWeaver held-out LoRA (81%→96%) and regression R² live in the project even if the page leads dashboard/FastAPI. STAR for ops/quality-adjacent delivery (MDC/MCFN researchers). Behavioral is a filter (`recruiting.md` §6). Onsite LA self-relocate and ITAR U.S. Person are form knockouts.

## Likelihood

- **Resume screen:** High — pipeline/ETL/dashboard page for a resume-gated A-tier factory DS/DE intern; eligible class year, GPA, Python/SQL through use
- **Overall hire odds:** Medium — A-TIER ~3–5% **[directional; tiny intern cohort]**; screen is the hard gate and this page clears it, then unpublished Python/SQL/project and onsite LA still eliminate. Remaining risk is the loop, defending no named warehouse stack, and not being mistaken for the SWE or Robotics sibling req
- **Funnel filters:** Ashby resume (bottleneck) → unpublished intern OA → tech/project + behavioral; light intern sys design. ITAR U.S. Person; onsite Los Angeles; $46.15–$50.71/hr. Not SWE intern `2b0423c6-947d-4226-8d23-90743bd5e63e`, not Robotics intern `02e33109-08c5-4db7-8881-67294c172584`
- **Outside the resume:** Apply in this first-wave window (published 2026-09-02). Timed Python/SQL walkthrough if an OA is assigned. No Hadrian contact in `network.md` — a Torrance/UMich intro still beats cold Ashby. Confirm Summer 2027 on the single-select term field; self-relocate (do not pick remote or "need relocation assistance")
