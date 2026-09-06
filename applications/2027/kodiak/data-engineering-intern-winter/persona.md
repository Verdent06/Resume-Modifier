# Winter 2027 Intern, Data Engineering at Kodiak Robotics

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid Winter 2027 intern as **Winter 2027 Intern, Data Engineering** (Greenhouse **4396622009** / **R-401**), posted on Kodiak’s Greenhouse board. Employer: **Kodiak** (Kodiak Robotics / Kodiak AI, Inc.). Location: **Mountain View, CA — onsite**. Term: **January 2027** start, **12–16 weeks** (end date flexible). Compensation (CA): **$10,000/month** listed base. Housing: intern-responsible.

**This is not** AI/ML intern **4377407009** and **not** Simulation intern **4378662009**. Do not import a perception/foundation-model spine, a C++ autonomy-SWE spine, or a generic product-SWE spine.

The intern supports the data platform behind robotics and safety datasets: optimize and maintain **AuroraDB, Elasticsearch, and other data stores**; design, build, and maintain **ETL/ELT pipelines** (cleanliness, reliability, efficient ingestion); explore, evaluate, and scale **QuickSight and modular dashboarding frameworks/factories** (or custom visualization) so the org can report and act.

JD surface is **applied data engineering** (relational/object DBs, schema, query optimization, AWS data stores, ETL/ELT, dashboards). Company identity is dual-use autonomous trucking (Kodiak Driver; commercial freight + defense). That identity is a **differentiator**, not the screen track — the posting does not test ROS, C++, perception, or research.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** autonomous trucking / robotics-and-safety data platform
- **track_divergence:** true

Required qualifications are current pursuit of a BS/MS/PhD in Computer Science, Data Engineering, Statistics, or a related quantitative technical field; strong working knowledge of relational and/or object database design, query optimization, and schema management; experience or strong familiarity with cloud data platforms such as AWS Aurora DB and Elasticsearch and associated ETL/ELT; familiarity with BI / dashboarding / automated reporting (QuickSight, Kibana, **or custom visualization**); a safety mindset and interest in autonomous systems or robotics; ownership + collaboration; Git and modern software workflows. Bonus: intern/project automated pipelines or cloud DB infra; IaC or automated data integration.

What the posting *literally tests* is data pipelines, ETL/ELT, schema/query, cloud data stores, and dashboarding. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data workflow: ingest → transform → insight/serve, not `model.fit()` alone) and `recruiting.md` Part III §13 (applied data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as Audax DE **4722779005** and Blackstone DE **45022**.

It is **not** `full-stack`: title is Data Engineering Intern, not SWE. Not `dev-ops` as the spine (cloud DB hosting is pipeline infrastructure, not SRE). Not `robotics` as the screen: this JD does not test ROS/controls/sim. Robotics interest is a **preference**, not a C++/FRC filter.

The autonomy/safety-dataset identity **diverges** from the DE screen (`track_divergence: true`). Spine stays ingest → ETL → quality → store/serve **and** a custom-dashboard analog. Do not lead with audio-DSP, voice-AI, or LoRA/research. Do not invent Elasticsearch, AuroraDB, QuickSight, Kibana, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, Terraform, ROS, or radar.

JD names **no programming languages**. Python and SQL are ATS keywords for this work even though the JD did not name them — they are **not** required-language hard gates. Show them through use when the work is real.

## Team & Bar

Kodiak is B-TIER in `reference/companies.md`: public dual-use AV trucking (Nasdaq KDK); intern DE is data-platform, not Driver software. Funnel: **Greenhouse resume + Endorsed AEDT → recruiter → likely Python/SQL/pipeline (OA unpublished)**; no intern sys design published; **bottleneck: resume** (~5–8%). `recruiting.md` Part II §8: intern eligibility is a hard gate; apply in the first wave (first_published 2026-09-04). Recruiter voice: a data-platform hiring manager or talent recruiter looking for an eligible CS student who can write SQL and Python ETL, keep a store clean, and ship a reporting analog — not an ML-research intern, not a C++ autonomy intern, not someone claiming Aurora/Elasticsearch/QuickSight they cannot defend.

Winning *kinds* of evidence: SQL and Python shown inside real ingest → transform → validate → persist/serve work (not Skills alone); ETL/ELT with a witness metric; schema or entity-resolution analog; data-quality / freshness / anomaly checks; cloud or on-prem database use limited to inventory (PostgreSQL, AWS EC2/S3, Docker); **custom visualization / dashboard** as the QuickSight/Kibana analog; Git/modern workflow through use. Warehouse/search-engine buzzwords without bullets fail. Math/stats coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Absence of Aurora, Elasticsearch, QuickSight, Kibana, Snowflake, Databricks, Tableau, Terraform is honest — do not invent them. Developmental bar: intern on a data platform beats claiming ownership of Kodiak’s production robotics stores.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- Python and SQL demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use). JD names neither language; they still fail if orphaned as ATS keywords.
- End-to-end data workflow: ingest messy or multi-source data → ETL/ELT / transform / normalize → validate or quality-check → database, API, or analytics consumer → measured outcome (`resume.md` §14; `recruiting.md` §13).
- Data pipelines and store/schema work as the lead story — analog to “optimize data stores” and “robust data pipelines” without claiming AuroraDB or Elasticsearch.
- Data validation, quality assessments, freshness checks, or anomaly resolution with a witness metric.
- Schema design or entity-resolution analog on structured/public data — analog to “relational/object database design, query optimization, and schema management.”
- Cloud evidence limited to inventory (AWS EC2/S3, Docker) through use — analog to cloud data platforms, not invented RDS/Aurora.
- Custom dashboard / reporting / visualization analog — the JD allows custom frameworks alongside QuickSight/Kibana.
- Git / CI / containerized delivery as modern workflow proof.
- Quantitative coursework (stats, calc) visible in Education; class-year shows current enrollment (`Expected May 2028` is in window for a Winter 2027 intern who returns after the term). GPA on the page.
- Interest in autonomous systems is a cover-letter / form signal, not a requirement to invent ROS or FRC.

**Anti-patterns:**
- Generic SWE / full-stack product resume that never shows pipelines, ETL, SQL, schema, or a dashboard analog — wrong req.
- Unmodified GenAI-agentic product lead with no data-engineering analog — this JD is stores + ETL + reporting, not a product-agent persona.
- Notebook ML, LoRA, or `model.fit()` as the lead with no pipeline, no quality step, no reporting analog — that is AI/ML intern **4377407009**, not this req.
- C++ audio-DSP or voice-AI as the lead with no data-pipeline analog.
- Skills-only Python/SQL/AWS/Docker/Aurora/Elasticsearch/QuickSight with no bullet proof.
- Invented Elasticsearch, AuroraDB, QuickSight, Kibana, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, Terraform, ROS, radar, or FRC claims (`resume.md` §8 fabrication smell).
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Claiming day-one ownership of production robotics/safety stores.

## ATS Keywords

Python, SQL, ETL, ELT, data pipelines, data quality, schema, query optimization, AWS, PostgreSQL, Docker, Git, Pandas, REST API, dashboard, data visualization, data engineering, data stores, ingestion, data cleanliness, robotics
