# 2027 Data Engineer Summer Internship at Lazard

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 + Summer 2027 term = still enrolled Junior; JD requires June 7–August 13 2027 in NYC and CS / Data Engineering / related — no exclusive class-year gate
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on MDC: irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST on AWS EC2. Ingest → transform → serve for Data Engineer intern **6605**, not SWE **6603** and not AI Engineer **6606**.
- Lyndbrook is multi-source modeling (EPA/MassGIS → PWSID entity DB; 800→280 at 35% precision). Vylet carries a Dockerized pipeline (30x, Redis/Celery), injection-safe SQL freshness, and a 79%→89% quality defect. SignalWeaver is FastAPI serve (9.1s p50) plus Docker Compose + GitHub Actions.
- Binding ding: Databricks / Spark / Delta never appear. Python/SQL ETL and Docker pipelines are the intern analog; a keyword-first DE screen can still miss a lakehouse token.

### Demerits

- **minor** · `resume` · Databricks/Spark unnamed — The JD asks for working knowledge of Databricks (Delta formats, workflows, cataloging) or equivalent Spark platforms. The page shows Pandas ETL, SQL freshness, Docker pipelines, and FastAPI/Postgres serving as intern pipeline analogs, but never names Spark, Delta, or a lakehouse orchestrator a DE screen may scan for.

### Misreads

- A keyword-first Oracle/HCM parse can no-pile this for missing Databricks/Spark even though ETL, SQL, Docker, and CI/CD are through use.
- Vylet’s founder / LangGraph tagline can file as SWE **6603** agent-product if the reader never reaches the SQL DAL, freshness checks, and 79%→89% quality lines.
- SignalWeaver’s financial-research descriptor can file as notebook ML or AI Engineer **6606** if the reader never reaches FastAPI serve + Docker Compose + GitHub Actions.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer Flask REST on EC2; Vylet Dockerized pipeline + SQL freshness/re-scrape + 79%→89% quality defect; Lyndbrook PWSID entity DB as onboard/model analog; SignalWeaver FastAPI + Docker/CI as serve + Git/CI/CD analog.
- **Defend:** No Databricks, Spark, Delta, Snowflake, Airflow, or dbt — say Python/SQL/Pandas/Postgres/AWS EC2/Docker/Git and ramp on their lakehouse *(out of rails: pool has no Databricks/Spark/Delta bullet; swap sets cannot bridge)*. This is **6605 DE**, not **6603 SWE** — do not lead with MCP/agent product or LoRA. SignalWeaver is research-assistant serving, not investment advice. CaseStudyPrep is omitted on purpose (voice-AI, not DE).
- **Depth prep:** Timed Python/SQL even though intern OA platform is unpublished (`companies.md`). Walk one ingest → ETL → serve path (MDC) and one SQL/quality + container path (Vylet DAL + Docker). ETL vs Spark; freshness/consensus vs Great Expectations; FastAPI vs inventing a warehouse. Behavioral: why Data Engineer vs IBD vs SWE **6603**; NYC June 7 start.

## Likelihood

- **Resume screen:** Medium — eligibility is on the page, Python/SQL ETL in the top half; one lakehouse-token ding keeps this from High.
- **Overall hire odds:** Medium — B-tier ~5–8%; Easy–Med Python/SQL after the PDF; intern OA unpublished so the page carries unusual weight, but the loop is still a real filter (`recruiting.md` intern funnel; `companies.md` bottleneck: resume).
- **Funnel filters:** Oracle HCM resume (**6605**) → recruiter/video screen → coding assessment (intern OA unpublished; do not treat HackerRank as confirmed) · Easy–Med Python/SQL · light intern sys design · Bottleneck: resume · ~5–8% · NYC hybrid June 7–August 13 2027
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-21). Confirm NYC for the full term. Timed Python/SQL. Honest Databricks ramp sentence — do not invent it. No Lazard contact in `network.md` — do not pick Employee Referral. Form-kit: CaseStudyPrep.AI + Vylet only (MDC/SpaceXAI extracurricular; Awards None). See `written-answers.md`.
