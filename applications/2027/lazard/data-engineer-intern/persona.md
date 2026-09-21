# 2027 Data Engineer Summer Internship at Lazard (AI & Data Team)

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid **~10-week** intern as **2027 Data Engineer Summer Internship** (Oracle Cloud job **6605**), posted **2026-09-21** on Lazard Professional Careers. Employer: **Lazard**. Location: **New York, United States (Hybrid)** — 30 Rockefeller Plaza; must be in NYC for the duration. Term: **June 7, 2027 – August 13, 2027**. Compensation: ~**$135,000** USD annualized (prorated).

**This is not** Software Engineer intern **6603** and **not** AI Engineer intern **6606**. Do not import a generic product-SWE spine, an LLM/agent product spine, or a notebook-`model.fit()` spine.

The intern sits on the **AI & Data Team** inside Lazard's AI and Data Group (data scientists, data engineers, AI engineers, software engineers). Primary responsibility: **onboard and model datasets on modern cloud data platforms**, delivering **reliable pipelines and high-quality data layers** that serve analytics, reporting, and ML/AI workloads for Financial Advisory bankers and Asset Management portfolio managers. Cloud-first; agency across the product-development cycle.

JD surface is **applied data engineering** (Python, SQL, ETL/ELT, cloud platforms, relational + NoSQL, data quality, Git/CI/CD, containers). Company identity is elite IB internal AI & Data — data platforms for bankers and PMs — **not** ML research, **not** an IBD analyst seat, **not** SWE **6603**.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** IB internal cloud data platforms (FA bankers + AM PMs)
- **track_divergence:** false

What the posting *literally tests* is data pipelines, ETL/ELT, Python, SQL, quality, and cloud data-platform work. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data workflow: ingest → transform → insight/serve, **not** `model.fit()` alone) and `recruiting.md` Part III §13 (applied data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as Acxiom DE, Citizens DE, Audax DE, Blackstone DE **45022**, Kodiak DE.

It is **not** `full-stack`: title is Data Engineer; the JD does not test product UI or general SDLC as the primary bar (that is **6603**). Not `dev-ops` as the spine (cloud/Git/CI-CD/containers are pipeline hosting, not SRE). Not `robotics`. Not ML research and not AI Engineer **6606**.

The FA/AM data-platform identity is **domain emphasis inside `ai-ml`**, not a second engineering track (`track_divergence: false`). Spine stays ingest → ETL/transform → quality/validation → store/serve. Agent/LLM is supporting (pipelines that feed ML/AI workloads), not the lead. Do not invent Databricks, Spark, Delta Lake, Snowflake, Airflow, dbt, Kubernetes, MCP-as-used, MongoDB, or Java.

**Languages JD names:** Python, SQL.

**Class-year / eligibility (computed, not argued):** Internship term Summer 2027 (June 7–August 13) during junior year; Expected May 2028; still enrolled after. JD requires start/end dates and NYC for the term; bachelor or advanced in Computer Science, Data Engineering, or related. Verdict: **eligible**. No published GPA or exclusive class-year knockout.

## Team & Bar

Lazard is B-TIER in `reference/companies.md`: independent FA + AM; this intern is NYC hybrid AI & Data **Data Engineer**. Funnel: **Oracle HCM resume → recruiter/video screen → coding assessment (intern OA unpublished; HackerRank-style is directional FTE only) → tech + behavioral**; Easy–Med Python/SQL **[directional]**; light intern sys design; **bottleneck: resume** (~5–8% directional, Goldman/Blackstone IB-tech peer). `recruiting.md` Part II §8: intern eligibility is a hard gate; apply in the first wave (posted 2026-09-21). Recruiter voice: a campus/tech recruiter or AI & Data hiring manager looking for an eligible CS student who writes Python/SQL ETL, quality checks, and cloud ingest — not a SWE generalist (**6603**), not a research-only ML intern, not someone claiming Databricks/Spark/Delta they cannot defend. Header email stays the gmail in Education/contact.

Winning *kinds* of evidence: Python and SQL shown inside real ingest → transform / ETL → quality or validation → serve (database, API, or analytics consumer) with a witness metric; AWS and Docker as hosting for pipelines if inventory; Git / CI/CD through use; relational and NoSQL through use; data-quality analog (freshness, consensus, named defect) without claiming Great Expectations/dbt; finance-user adjacency (shipping to operators who make decisions) is a plus; banking-analyst storytelling is a miss. Databricks/Spark is "or equivalent" — honest absence, not a fabrication. Math/stats coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Absence of Databricks, Spark, Delta, Snowflake, Airflow, dbt, Kubernetes, MCP is honest — do not invent them.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- Python and SQL demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use). Both are required and both are in inventory.
- End-to-end data workflow: ingest messy or multi-source data → ETL/ELT / transform / model → validate or quality-check → database, warehouse analog, API, or analytics consumer → measured outcome (`resume.md` §14; `recruiting.md` §13).
- Data pipelines as the lead story — analog to "onboard and model datasets on modern cloud data platforms" and "reliable pipelines and high-quality data layers" without claiming Lazard production Databricks/Spark.
- Data quality checks, validation rules, or a named quality defect with a witness metric — analog to "Data Quality check frameworks."
- Cloud evidence limited to inventory (AWS EC2/S3) through use. Docker containerization of a real pipeline or service is the container analog; do not invent Kubernetes/orchestration platforms.
- Relational and NoSQL through use (SQL/Postgres-class and Redis-class), not Skills-only.
- Git and CI/CD through use — analog to "Comfortable working with Git, CI/CD tools."
- Finance-adjacent delivery (operators who make decisions) without IBD-analyst storytelling.
- AI/ML as supporting (pipelines that serve ML/AI workloads, embeddings stored beside source records) — not LoRA-as-lead, not notebook ML, not AI Engineer **6606**.
- Class-year on page: `Expected May 2028` shows still enrolled for a Summer 2027 intern. GPA 3.66 is a genuine signal (`resume.md` GPA ≥ 3.5). Header contact email is gmail.

**Anti-patterns:**
- Generic SWE / full-stack product resume that never shows pipelines, ETL/ELT, SQL, or data quality — that is **6603**, wrong req.
- Unmodified GenAI-agentic product lead with no data-engineering analog — this JD is cloud data platforms + ETL, not SWE **6603** agent/MCP framing.
- LoRA-as-lead / notebook ML / `model.fit()` with no pipeline, no quality step, no measured outcome — that is research / AI Engineer **6606**, not this req.
- IBD-analyst resume: deal-flow, pitch-book, or markets storytelling with no engineering the role tests.
- Voice-AI, audio-DSP, or embedded C++ as the lead with no data-pipeline analog.
- Skills-only Python/SQL/AWS/Docker/Databricks/Spark with no bullet proof.
- Invented Databricks, Spark, Delta Lake, Snowflake, Airflow, Prefect, dbt, Kubernetes, MCP-as-used, MongoDB, Java, Copilot, Fusion, Tableau (`resume.md` §8 fabrication smell).
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Claiming day-one ownership of Lazard lakehouses or FA/AM production warehouses.
- Changing the header email off gmail.

## ATS Keywords

Python, SQL, ETL, ELT, data pipelines, AWS, data quality, Git, CI/CD, Docker, PostgreSQL, Redis, Pandas, Flask, FastAPI, data modeling, cloud, batch, relational databases
