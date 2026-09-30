# Spring 2027 Investment Data Engineer Co-op at MFS

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid Winter/Spring 2027 **Investment Data Engineer Co-op** (Workday **MFS-231978**) at MFS Investment Management (hiring org **001 Mass Financial Services**). Tenant: `mfs` / `MFS-Careers`. Location: Workday **Boston**. Time type: Full time. Posted **2026-09-30** (`startDate`; CXS `postedOn` **Posted Today** on capture). Workday `endDate` **2026-10-30**. Compensation: **$21.00–$25.00/hr**. Term: **Wednesday January 13 – Friday June 25, 2027**, Monday–Friday, **35–40 hours/week**. `#LI-HYBRID`.

**This is not** a portfolio-manager / research-analyst intern, **not** a generic product-SWE intern, and **not** a notebook-ML intern. Do not import a trading-desk quant spine or a full-stack product spine.

The co-op sits in the **Investment Data Management Office** on a long-term initiative to unify and harmonize investment data for the multi-asset platform — consistent, timely, accurate, user-friendly data for investors, risk teams, and clients. Day-to-day: scalable pipelines that ingest and process investment data records from internal and external sources; coding to meet business requirements; data quality, resiliency, control, efficiency, and monitoring; deploy data products to the investment data platform; integrate ingestion, delivery, transformation, and orchestration tools; help during unexpected outages.

JD surface is **applied data engineering** (Python, SQL, pipelines, quality/monitoring, modern warehouse tools as a plus). Company identity is a Boston active asset manager (invented the mutual fund, 1924) — this seat is **investment-data platform engineering**, not a PM coverage intern.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** investment-data platform at a Boston active asset manager (Investment Data Management Office / multi-asset)
- **track_divergence:** false

Required qualifications: currently pursuing a bachelor's in Computer Science, Data Science, or related (**junior or senior preferred**); coursework or project experience in data engineering, data integration, or data analytics; familiarity with **Python, SQL, or similar**; interest in financial services and willingness to learn financial instruments and data; problem-solving and teamwork. Plus: Agile (Scrum/Kanban); Snowflake, Redshift, or BigQuery. Program is designed for students **enrolled in a college co-op program**.

What the posting *literally tests* is applied data engineering: ingest internal/external records → transform → quality/monitoring → data products on a unified platform. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data workflow: ingest → transform → insight/serve, **not** `model.fit()` as the lead) and `recruiting.md` Part III §13 (applied data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as American Century Enterprise Data, Pacific Life DE, Jabil DE, Audax DE co-op.

It is **not** `full-stack`: title is Investment Data Engineer Co-op; the JD does not test product UI as the primary bar. Not `dev-ops` as the spine (orchestration/monitoring are pipeline hosting, not SRE). Not `robotics`. Not PM/research.

The AM / investment-data identity is **domain emphasis inside `ai-ml`**, not a second engineering track (`track_divergence: false`). Spine stays ingest → ETL/transform → quality/validation → serve. Do not lead with notebook LoRA, voice-AI, or C++ DSP. Do not invent Snowflake, Redshift, BigQuery, Databricks, Tableau, Copilot, or Fusion.

**Languages JD names:** Python, SQL, or similar. Candidate inventory has Python and SQL.

**Class-year / eligibility (computed, not argued):** Co-op term **January 13 – June 25, 2027**. Candidate Expected **May 2028** → Junior during the term (junior/senior preferred). Currently pursuing B.S. Computer Science (listed major). No visa line. University co-op-program enrollment is a **program-design** sentence, not a printed binary on the public page — treat as **eligible** on class year/major; if a later radio requires formal co-op-office enrollment, that is a separate honest answer. Verdict: **eligible**.

## Team & Bar

MFS is **C-tier** in `reference/companies.md` (~15–25% **[directional, peer of Wellington Technology undergrad / American Century Enterprise Data / Audax DE co-op]**; bottleneck: **resume**). Funnel: **Workday resume → recruiter → unpublished intern loop** (Easy Python/SQL + project walk + STAR). Intern OA unpublished — do **not** invent HackerRank/CodeSignal. No intern sys design. Recruiter voice: a Boston Early Career / Investment Data hiring manager looking for an eligible CS junior who can write Python/SQL, ship ingest→quality→serve pipelines, sit Boston hybrid Jan–Jun 2027, and learn financial instruments — not a SWE generalist, not a research-only ML intern, not someone claiming Snowflake/Redshift/BigQuery they cannot defend. Behavioral is a filter (`recruiting.md` §6). Apply in the first wave (`recruiting.md` Part II §8); posted 2026-09-30; apply-by 2026-10-30. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §5). Header email stays the gmail in Education/contact.

Winning *kinds* of evidence: Python and SQL through use in ingest → ETL → quality or freshness → serve with a witness metric; messy multi-source analog (internal/external filings, APIs); Docker as orchestration analog; AWS if inventory; stakeholder-facing delivery; financial-data curiosity through a served research product, not a claimed production warehouse. Math/econ coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Absence of Snowflake, Redshift, BigQuery is honest — do not invent them.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- Python and SQL demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use).
- End-to-end data workflow: ingest messy or multi-source records → ETL / transform / normalize → quality-check or freshness/validation → API, database, or reporting consumer → measured outcome (`resume.md` §14; `recruiting.md` §13). Analog to “ingest and process investment data records” without claiming MFS production warehouses.
- Data quality / resiliency / monitoring analog with a witness metric (JD: quality, resiliency, control, efficiency, monitoring; outage support).
- Docker / pipeline-orchestration analog through use — analog to “orchestration tools,” not a claimed Airflow/Prefect/Snowflake job.
- Cloud (AWS) through use if inventory — hosting for pipelines, not invented Redshift.
- Stakeholder / presentation analog — structured co-op includes presentation challenges; partner with investment professionals.
- Financial-services interest shown by a served financial-research or investment-adjacent data product — research assistant, not advice, not a PM intern.
- Quantitative coursework (calc, econ) visible in Education; class-year shows current enrollment (`Expected May 2028` vs Jan–Jun 2027 junior term). GPA on the page is a genuine signal (no GPA floor on this JD). Header contact email is gmail.

**Anti-patterns:**
- Generic SWE / full-stack product resume that never shows pipelines, ETL, SQL, or data quality.
- LoRA-as-lead / notebook ML / `model.fit()` with no pipeline, no quality step, no measured serve outcome.
- Voice-AI, audio-DSP, or embedded C++ as the lead with no data-pipeline analog.
- Skills-only Python/SQL/Snowflake/Redshift/BigQuery with no bullet proof.
- Invented Snowflake, Redshift, BigQuery, Databricks, Tableau, Copilot, Fusion, or MFS internal platforms (`resume.md` §8 fabrication smell).
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Treating this as a PM/research-analyst intern or a summer-only intern when the term is Jan–Jun 2027.
- Keyword-stuffing “mutual fund / Aladdin / Snowflake” into bullets that are not about that work.
- Changing the header email off gmail.
- Inventing university co-op-office enrollment.

## ATS Keywords

Python, SQL, ETL, data pipelines, data engineering, data quality, Pandas, PostgreSQL, AWS, Docker, Flask, FastAPI, Git, orchestration, monitoring, investment data, intern, co-op
