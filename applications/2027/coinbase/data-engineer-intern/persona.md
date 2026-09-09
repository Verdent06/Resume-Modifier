# Data Engineer Intern at Coinbase

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid Summer 2027 **Data Engineer Intern** (Greenhouse **8175459** / req **P78146**) at Coinbase, posted on the Platform product group as an analytics-engineering partner. Location: **Hybrid — San Francisco, CA**. Term: **12-week internship during summer 2027**. Compensation: **$50–$50/hr**. Department: Internships & Emerging Talent. First published **2026-09-08**.

**This is Data Engineer Intern — not a generic product-SWE intern, not an ML-research intern, and not a matching-engine / Base-L2 systems seat.** Do not import a full-stack product spine or a notebook-`model.fit()` spine.

The intern partners with analytics engineering to build and maintain **data pipelines and infrastructure** that power insights across Coinbase: integrity and accessibility for **analytics and machine learning** workloads; scalable infra in **Python** and cloud; multi-source ingest (internal systems + external APIs); analytical deep dives with seniors (documentation and recommendations); data-engineering practices (governance, security, performance).

JD surface is **applied data engineering** (pipelines, SQL, Python, cloud, APIs, AI/LLMs for analytics/ML use cases). Company identity (`company.md` / `companies.md`): publicly traded crypto exchange / fintech-backend / exchange-platform data — not generic SaaS.

Work model: Coinbase is remote-first, not remote-only; this seat is hybrid SF with quarterly in-person "surges." Application cap: max 3 applications in 6 months. Greenhouse knockout: available to begin a potential full-time role **before September 2028**.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** crypto / fintech-backend / exchange-platform data
- **track_divergence:** true

Required qualifications: completed or in-progress CS / Data Engineering coursework (or equivalent) with demonstrated **Python** including data structures and algorithms; hands-on **SQL** and relational-database concepts; familiarity with cloud (AWS, GCP, or Azure); demonstrated interest in **AI, LLMs, or API integrations**; exposure to microservices, distributed systems, or cloud-native design; responsible generative AI with human oversight.

What the posting *literally tests* is data pipelines, SQL, Python, cloud data infra, and AI/LLMs or APIs for analytics/ML consumers. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data/ML workflow: ingest → transform/pipeline → insight/serve, not `model.fit()` alone) and `recruiting.md` Part III §13 (applied data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as Blackstone DE **45022**, Audax DE **4722779005**, Kodiak DE **4396622009**, and IBM Intern Data Engineers. Do **not** default to `full-stack`: title is Data Engineer Intern; the JD does not test product UI or general software delivery as the primary bar. Not `dev-ops` as the spine (cloud is pipeline hosting, not SRE). Not `robotics`.

The company's dominant identity in `reference/companies.md` and `company.md` is **crypto / fintech-backend / exchange-platform data** (retail + institutional trading, custody, Base — not a generic SaaS data warehouse). That identity implies a finance/markets / high-integrity backend track other than the applied-data screen spine, so divergence is true: the resume leads with the `ai-ml` spine (ingest → pipeline → quality/governance → serve for analytics/ML) **and** keeps finance-adjacent or markets-data analog prominent and deep. Do not optimize as generic SWE, do not lead as notebook ML research, and do not invent Snowflake, Databricks, Copilot, Fusion, or Tableau. Do not invent GCP, Azure, Spark, Kafka, or Airflow.

## Team & Bar

Coinbase is B-tier in `companies.md` (Very selective; **95% resume rejection**; CEO reviews every offer; intern OA **CodeSignal**; bottleneck: **resume**). Recruiter voice: a Platform / analytics-engineering recruiter scanning Greenhouse for an eligible CS undergrad who can write Python pipelines and SQL, keep data accurate and accessible, and talk cloud + APIs — not a crypto-twitter essayist, not a research scientist, not a generic SWE intern.

**Process (doctrine + JD):**
- Front door is Greenhouse + human resume screen. Binding gate is the resume (`companies.md`; `recruiting.md` Greenhouse/human-read). Apply in the first wave (`recruiting.md` Part II §8). Posted 2026-09-08.
- Funnel: resume → CodeSignal OA (Easy–Med) → recruiter → 3–4 rds total, light intern sys design (`companies.md`).
- Eligibility knockouts first: current-student intern; **FT availability before September 2028** (Expected May 2028 clears). Max 3 applications in 6 months. Hybrid SF + surges.
- Intern sys design is light, not a published DE take-home. FT Data Engineer analog reports SQL/pipeline depth **[directional, sibling — not confirmed for this intern]**.

Winning *kinds* of evidence: Python and SQL shown inside real ingest → transform → validate/governance → persist/serve work (not Skills alone); data pipelines and infrastructure with a witness metric; multi-source or API ingest; cloud evidence limited to inventory (AWS EC2/S3, Docker); AI/LLM or API-integration analog through use; microservices / queue / cloud-native analog (workers, containers) without inventing Kafka; stakeholder-facing documentation or ranked/analytics output. Warehouse buzzwords without bullets fail. Math/stats/econ coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Dual CS + Economics is on-axis for an exchange-platform data seat. Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Class-year on the page: `Expected May 2028` vs Summer 2027. Absence of Snowflake, Databricks, Tableau, Spark, GCP is honest — do not invent them.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- Python and SQL demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use). Both are required and both are in inventory.
- End-to-end data workflow: ingest messy or multi-source data → pipeline / ETL / transform → integrity, freshness, or quality-check → API, database, or analytics/ML consumer → measured outcome (`resume.md` §14; `recruiting.md` §13).
- Data pipelines and infrastructure as the lead story — analog to "build and maintain data pipelines" and "scalable data infrastructure" without claiming Coinbase production ownership.
- Multi-source ingest and external-API integration analog — the JD's "internal systems and external APIs" line.
- Cloud evidence limited to inventory (AWS EC2/S3, Docker) through use — analog to AWS/GCP/Azure; do not invent GCP or Azure.
- AI, LLM, or API-integration analog through use (orchestration, embeddings, or model-in-the-loop with human-gated / eval discipline) — not a Skills-only "interested in AI" line.
- Data-governance / integrity analog: validation, freshness, anomaly or defect fix with a witness metric.
- Distributed or cloud-native analog (containers, queues/workers, async services) without inventing microservices platforms not in inventory.
- Finance-, markets-, or high-integrity-data analog kept visible in the lead window because of track divergence — exchange-platform identity, not generic SaaS CRUD.
- Quantitative coursework (DS&A, stats, calc, econ) visible in Education; class-year on the page: `Expected May 2028` vs Summer 2027. GPA 3.66 is a genuine signal.

**Anti-patterns:**
- Generic SWE / full-stack product resume that never shows pipelines, SQL, or data integrity — wrong role.
- Notebook ML / LoRA-as-lead / `model.fit()` with no pipeline, no quality step, no analytics consumer.
- Voice-AI, audio-DSP, or embedded C++ as the lead with no data-pipeline analog.
- Skills-only Python/SQL/AWS/AI with no bullet proof.
- Invented Snowflake, Databricks, Copilot, Fusion, Tableau, Spark, Kafka, Airflow, GCP, Azure, or warehouse-platform claims (`resume.md` §8 fabrication smell).
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Crypto-keyword stuffing ("on-chain," "matching engine," "Base") into bullets that are not about that work.
- Treating this as a software-engineer intern screen (generic SWE keywords, no pipeline spine).

## ATS Keywords

Python, SQL, data pipelines, data infrastructure, AWS, cloud, ETL, Pandas, API, LLMs, microservices, distributed systems, data governance, relational databases, data integrity, analytics, PostgreSQL, Docker, Git, data structures
