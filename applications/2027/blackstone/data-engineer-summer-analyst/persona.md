# Data Engineer Summer Analyst at Blackstone

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid Summer 2027 **full-time** intern as **2027 Blackstone Data Engineer Summer Analyst** (Workday req **45022**), posted on Blackstone campus careers. Employer: **Blackstone**. Location: **Miami, FL** — treat as **onsite**. Start June 2027. Compensation: expected annual base **$125,000–$125,000**. Posted 2026-08-21.

**This is not** SWE req **45021** and **not** a Data Science intern. Do not import a generic product-SWE spine or a notebook-ML spine.

The intern sits in **Blackstone Technology & Innovations (BXTI)** — the technology organization powering the world's largest alternative asset manager (~$1.3T AUM). Day-to-day: design, build, deploy, and support **ETL/ELT data pipelines and infrastructure** across business units, working with engineers and business analysts. Custom applications are mostly **Python**, hosted on **AWS**. The posting also names cloud-native containers/serverless, Snowflake for analysis/visualization, Prefect (or similar) for orchestration, Docker microservices, Terraform, Gitlab CI, and unit/integration/deployment tests. Interns are treated as engineers from day one.

JD surface is **applied data engineering** (pipelines, ETL/ELT, Python, Pandas, SQL, AWS data infra). Company identity for *this* req is BXTI data platforms inside alternative asset management — domain emphasis inside `ai-ml`, not a second track and not the PE/IB recruiting funnel.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** BXTI / alt-asset-management data platforms
- **track_divergence:** false

Required qualifications are current undergraduate enrollment, anticipated graduation **Fall 2027 – Spring 2028**, resume with expected graduation month/year and GPA, PDF format, plus: sound Python and Pandas (or equivalent), SQL / database query languages, familiarity with AWS (S3, RDS, streaming, ECS, Lambda, IaC), familiarity with Snowflake, Prefect, or similar orchestration, and OOP in any language (Python a plus). Duties mix in Docker microservices, Terraform, Prefect/Snowflake pipelines, data models persisted to a cloud warehouse, cloud messaging, Gitlab CI, automated tests, and tooling that automates repetitive work.

What the posting *literally tests* is data pipelines, ETL/ELT, Python, Pandas, SQL, and AWS data infrastructure. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data/ML workflow: ingest → transform → insight/serve, not `model.fit()` alone) and `recruiting.md` Part III §13 (applied ML / data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as IBM Intern Data Engineers and other applied data intern reqs in this system.

It is **not** `full-stack`: title is Data Engineer Summer Analyst, not SWE 45021; the JD does not test product UI or general software delivery. Not `dev-ops` as the spine (Docker/AWS/IaC are pipeline hosting, not SRE). Not `robotics`. Not Data Science.

The BXTI / alt-AM identity is **domain emphasis inside `ai-ml`**, not a second engineering track (`track_divergence: false`). Spine stays data pipelines / ETL-ELT / Python / Pandas / SQL / AWS data infra. Do not optimize as generic SWE because Blackstone also posts SWE 45021, and do not invent Snowflake, Databricks, Copilot, Fusion, Tableau, Prefect, Terraform, Gitlab, RDS, ECS, or Lambda claims.

## Team & Bar

Blackstone is B-TIER in `reference/companies.md`: world's largest alt AM; this intern is Miami onsite BXTI data engineering. Funnel: **Workday campus resume → recruiter/video screen → HackerRank (Python/SQL Easy–Med, candidate-reported for BXTI) → tech video → Superday**; light intern sys design; **bottleneck: resume + fit** (~5–8%). PE HireVue/LBO is a different funnel. `recruiting.md` Part II §8: intern eligibility is a hard gate; apply in the first wave. Recruiter voice: a BXTI campus/tech recruiter or data-platform hiring manager looking for an eligible CS student who can build Python/Pandas ETL and SQL-backed pipelines on AWS — not a SWE generalist, not a research-only ML intern, not someone claiming Snowflake/Prefect/Terraform they cannot defend.

Winning *kinds* of evidence: Python and Pandas shown inside real ETL/ELT (not Skills alone); ingest → transform / pipeline → validate or persist → serve (API, warehouse analog, or consumer) with a witness metric; SQL demonstrated in a data-access or quality step, not only the Languages line; AWS (honest EC2/S3) and Docker as hosting for pipelines; OOP visible in engineered Python (or another inventory language) through use; stakeholder or business-analyst-adjacent delivery. Cloud-native buzzwords without bullets fail. Math/stats coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Absence of Snowflake/Prefect/Terraform/Gitlab/RDS/ECS/Lambda is honest — do not invent them.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- Python and Pandas demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use).
- SQL / database query language demonstrated through use — a transform, DAL, freshness/validation, or persist step — not Skills-only.
- End-to-end data workflow: ingest messy or multi-source data → ETL/ELT / transform / normalize → validate or quality-check → database, API, or analytics consumer → measured outcome (`resume.md` §14; `recruiting.md` §13).
- Data pipelines and infrastructure as the lead story — analog to "design, build, deploy, and support ETL/ELT data pipelines" without claiming BXTI production ownership of Snowflake.
- AWS evidence limited to inventory (EC2, S3) through use; Docker containerization of a real pipeline or service.
- Object-oriented / engineered Python (services, APIs, structured pipeline stages) rather than a notebook dump.
- Stakeholder- or business-facing scoping — analog to partnering with data scientists, PMs, and business stakeholders.
- Quantitative coursework (stats, calc) visible in Education; class-year shows current enrollment (`Expected May 2028` is inside Fall 2027–Spring 2028). GPA on the page (JD requires it).

**Anti-patterns:**
- Generic SWE / full-stack product resume that never shows pipelines, ETL/ELT, Pandas, or SQL — wrong req (that is SWE 45021).
- Unmodified GenAI-agentic product lead with no data-engineering analog — this JD is ETL/ELT data platforms, not a product-agent persona.
- Notebook ML or `model.fit()` with no pipeline, no quality step, no measured outcome — that is Data Science, not this req.
- Skills-only Python/SQL/AWS/Docker/Snowflake with no bullet proof.
- Invented Snowflake, Databricks, Copilot, Fusion, Tableau, Prefect, Terraform, Gitlab, RDS, ECS, or Lambda claims (JD names several as familiarity; stuffing them is a fabrication smell — `resume.md` §8).
- Club-ops or community-growth filler occupying prime slots.
- Pure audio-DSP / embedded systems as the lead with no data-pipeline analog.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Claiming day-one ownership of firm-wide warehouse platforms.

## ATS Keywords

Python, Pandas, SQL, ETL, ELT, data pipelines, AWS, S3, Docker, object-oriented programming, data models, automation, cloud, microservices, data infrastructure, unit tests, REST API, PostgreSQL, Git, data quality
