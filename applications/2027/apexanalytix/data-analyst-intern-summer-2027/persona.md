# Data Analyst Intern (Summer 2027) at apexanalytix

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A Summer 2027 **Data Analyst Intern** (Rippling **e275fd70-45a3-4a64-8688-cace8a3f87ef**) at **apexanalytix** (R&D – Archimedes). Reports to Manager, Automation Architect. **Onsite Greensboro, N.C.** Term on the form: **May 2027 through August 2027**. Comp unlisted; paid intern implied. Pulled 2026-09-16.

The intern is a detail-oriented, technically minded analyst in an **on-premise data environment** whose job is the accuracy and reliability of data used for business decisions. A significant portion is **data quality assurance (QA)**: source-to-target validation (source systems vs Data Warehouse extract/transform correctness), regression testing after system or pipeline changes so reports/dashboards stay accurate, SQL integrity checks (nulls, duplicates, schema mismatches), and bug reporting tracked to resolution with engineers.

Analysis and technical operations: complex SQL for ad-hoc business requests; Linux command line (navigate servers, run validation scripts, grep logs); Kubernetes support as a plus (pod status / kubectl logs — not a floor); Data Catalog and Business Glossary documentation so metric definitions match technical reality; supplier n-tier mapping (research sources to map Tier 1 → Tier 2/3 sub-suppliers).

JD surface is **applied analytics / Python / SQL / on-prem DW QA**, not ML research, not generic SWE, and **not Apex Space**. Company identity (`company.md` / `companies.md`) is private procure-to-pay / supplier-management software (apexportal; Gartner 2026 Leader, Supplier Risk Management).

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** procure-to-pay / supplier-management on-prem DW QA (source-to-target, integrity, n-tier supplier maps)
- **track_divergence:** true

Required qualifications: currently pursuing Bachelor's or Master's in Computer Science, Information Systems, Mathematics, or related. What the posting *literally tests* is SQL (essential — set differences, counting variances), Linux/bash, data warehousing (star schema) + ETL, basic Python (Pandas), and a QA mindset ("Does this number actually make sense?"). Kubernetes/kubectl is a plus. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data workflow: ingest → transform → insight / quality check → measured outcome, not `model.fit()` research) and `recruiting.md` Part III §13 (applied ML/data — ship pipelines and analytics; intern MLOps is a bonus). Same routing as analog applied-analytics intern reqs (Hy-Vee DA, Applied Materials GTLC DA, Tokyo Electron BI, Wellmark DA&G, DICK'S DA&E). Stay **applied analytics / Python+SQL / data QA** — not research scientist.

It is **not** `full-stack`: title is Data Analyst Intern, not SWE. Not `dev-ops` (kubectl is a plus on a QA intern, not an SRE floor). Not `robotics`. Not ML-research.

The company's dominant identity is **procure-to-pay / supplier-management on-prem DW QA**. That identity implies a warehouse-quality / source-to-target / supplier-analytics track other than a generic applied-ML spine, so divergence is true: the resume leads with the `ai-ml` spine (Python+SQL through use, ETL, integrity/freshness, stakeholder reporting) **and** keeps DW-QA / multi-source validation / entity-mapping analog prominent and deep. Do not optimize as generic SWE. Do not lead with LoRA / paper-style modeling / voice-AI / C++ DSP.

## Team & Bar

apexanalytix is C-tier in `companies.md` (~20–30% **[directional]**;  unpublished intern loop · bottleneck: **resume**). Recruiter voice: an Automation Architect / R&D hiring manager in Greensboro scanning Rippling for an eligible CS/IS/Math undergrad who will distrust a dashboard number, write the SQL that proves it, and file a clear bug — not a research scientist, not a satellite intern, not a generic SWE intern.

**Process (doctrine + JD):**
- Front door is Rippling + human resume screen. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §5). Binding intern gate is the **resume** (`companies.md`). Apply in the first wave (`recruiting.md` Part II §8).
- Short loop: resume → recruiter/HM (Greensboro onsite May–August 2027, enrollment) → unpublished Easy SQL/QA + STAR (`companies.md` peer of Hy-Vee DA / Wellmark DA&G). No published intern OA. No intern sys design.
- Eligibility knockouts: CS/IS/Math or related in progress. No GPA floor. No exclusive class-year gate. No sponsorship sentence on this JD.
- Behavioral is a filter (`recruiting.md` §6).

Winning *kinds* of evidence: SQL and Python shown inside real data work (not Skills alone); end-to-end ingest → transform/ETL → integrity, freshness, duplicate/collision, or source-to-target analog → stakeholder report or ranked output → measured outcome (`resume.md` §14; `recruiting.md` §13); warehouse/pipeline thinking; Linux/Docker as an infra analog without inventing kubectl; skepticism of numbers (diagnosed defect, validation check, "does this make sense"). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Math/stats/econ coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Dual CS + Economics is on-axis. Class-year on the page: `Expected May 2028` vs Summer 2027. Preferred JD tools not evidenced in real work (kubectl, Kubernetes, Snowflake, Databricks, Tableau, SAP/Oracle, Power BI, Looker, Airflow) stay off the page.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- SQL demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use). SQL is essential on this JD. PostgreSQL/asyncpg through use is the honest analog; do not invent a named warehouse (Snowflake, Databricks) or BI tool.
- Python / Pandas ETL through use: messy or multi-source data → gather/merge/aggregate → served or ranked output.
- Data-quality / integrity / freshness / duplicate-or-collision catch as first-class work — analog to nulls, duplicates, schema mismatch, and "does this number make sense?"
- Source-to-target or multi-source validation analog: two systems or two public sources reconciled onto one entity or one served table.
- Stakeholder reporting: ranked output, API, or dashboard delivered to a non-builder customer.
- Warehouse / pipeline thinking: ETL, DAL, freshness jobs, regression-style re-checks after a change.
- Linux / Docker as infra analog (servers, containers, scripts) without inventing kubectl production experience.
- Quantitative coursework (stats, calc, econ) visible in Education; GPA on the page; `Expected May 2028`.

**Anti-patterns:**
- LoRA-as-lead / ML-research / notebook `model.fit()` with no delivery, no QA, no measured business outcome.
- Voice-AI as the lead; C++ DSP as the lead; generic SWE with no SQL/QA.
- Skills-only SQL (or Skills-only Python/Pandas) with no bullet proof.
- Invented Snowflake, Databricks, Tableau, Copilot, Fusion CAD, kubectl production, SAP/Oracle, Power BI, Looker, or Airflow (`resume.md` §8 fabrication smell). Kubernetes/kubectl is a plus — do not claim it.
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Treating this as a software-engineer intern screen (OA-first, systems-design, generic SWE keywords) or as Apex Space.

## ATS Keywords

SQL, Python, Pandas, ETL, data warehouse, star schema, data quality, source-to-target, regression testing, data integrity, Linux, bash, Docker, data pipelines, validation, duplicates, schema, Data Catalog, Business Glossary, supplier mapping, ad-hoc analysis
