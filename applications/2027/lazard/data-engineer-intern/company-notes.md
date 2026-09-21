# Lazard — intern notes (2027 Data Engineer Summer Internship)

Intern-facing packet notes for Oracle Cloud job **6605**. Not a rewrite of `company.md` (that file is write-once for SWE **6603**). Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Lazard builds

Independent financial advisory + asset management (NYSE **LAZ**). Internal **AI and Data Group** (data scientists, data engineers, AI engineers, SWE) builds data products for FA bankers and AM PMs. This intern is a **Data Engineer** seat on that team — onboard/model datasets, pipelines, quality, served data layers — **not** SWE **6603**, **not** AI Engineer **6606**, **not** IBD.

## This req

- **Title:** 2027 Data Engineer Summer Internship · New York, United States (Hybrid) · **~$135,000** annualized prorated
- **Term:** **June 7, 2027 – August 13, 2027** (~10 weeks); must be in NYC
- **ATS:** Oracle HCM `LazardProfessionalCareers` job **6605** · https://icbpjb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/LazardProfessionalCareers/job/6605
- **Posted:** 2026-09-21T13:08:31Z — first wave (`recruiting.md` Part II §8)
- **Work:** Onboard and model datasets on modern cloud data platforms; reliable pipelines and high-quality data layers for analytics, reporting, and ML/AI workloads

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python and SQL (required) | Python + SQL through use (MDC Pandas ETL; Vylet injection-safe SQL) |
| Hands-on ETL/ELT | MDC Requests+Pandas ETL; Vylet Dockerized pipeline |
| Databricks (Delta, workflows, cataloging) **or equivalent Spark** | **Not in pool.** Analog = Pandas ETL + Docker/Celery batch. Do not invent Databricks/Spark/Delta |
| AWS / Azure / GCP | AWS EC2, S3 through use. Do not check Azure/GCP |
| Relational and NoSQL | PostgreSQL + Redis through use |
| Database as Code | **Not in pool.** Do not invent dbt/Liquibase |
| Data quality frameworks | Vylet SQL freshness + 79%→89% name-collision fix. Do not invent Great Expectations |
| Git / CI/CD / containers | GitHub Actions + Docker Compose (SignalWeaver); Dockerized Vylet |
| Snowflake, Airflow, Kubernetes, MCP, Java | **Not** in the pool |

## Funnel

B-TIER (`companies.md`): Oracle HCM resume → recruiter/video → coding assessment (intern OA unpublished) → tech + behavioral · Easy–Med Python/SQL **[directional]** · **bottleneck: resume** · ~5–8% **[directional, Goldman/Blackstone IB-tech peer]**. Resume-first intern (`recruiting.md` Part I §5 mid-size / non-tech-tech).

## Knockouts

1. CS / Data Engineering / related — **clears**.
2. June 7–August 13 2027 in NYC — **Yes** (relocate from Northville, MI; return after).
3. Work authorization — **US citizen / no sponsorship**. JD prints no sponsorship line; still answer honestly.
4. Databricks/Spark — **not a form knockout.** Honest gap on the PDF. Do not check it.

## What to lead with

MDC Pandas ETL + Flask REST on EC2. Vylet SQL freshness + named quality defect + Docker/Celery pipeline. Lyndbrook entity DB. SignalWeaver FastAPI + Docker/CI. Then say you will ramp Databricks rather than invent it (`persona.md` / `grade.md` Defend).

## Do not invent

Databricks, Spark, Delta, Snowflake, Airflow, dbt, Kubernetes, MCP-as-used, MongoDB, Java, Copilot, Fusion, Tableau, LoRA-as-the-job, IBD.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu`). Phone 248-704-4852. US citizen. Address **49032 Freestone Dr, Northville, MI 48168**. GPA **3.66**. Expected **May 2028**. LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06. No Lazard contact in `network.md`.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/lazard/data-engineer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `b39f53944fa6c258f162a790b75fbb2e5841028d0c34a0f7d474d6de741b64da`

Header email on the PDF is **verdent06@gmail.com**. Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **9.0 / 10** (1 minor: Databricks/Spark unnamed — out of rails). See `WORTH_IT.md` and `grade.md`.
