# ICF — intern notes (2027 Summer Intern, Data Engineer, Reston VA or Remote)

Intern-facing packet notes for Workday **R2603380**. Not a rewrite of `company.md` (that file is the Software Developer intern brief and is write-once). Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What ICF builds

ICF (Nasdaq: ICFI) is a Reston-headquartered advisory and technology consulting firm: energy/environment, health and social programs, disaster recovery, and digital transformation (IT modernization, cloud, cybersecurity, data). This intern sits on a **data-engineer** seat — ingest, transform, quality, documentation — not product-engineering at a software company and **not** Software Developer **R2603002**. Work quality varies by engagement (Accenture / Deloitte Tech / Booz Allen caveat in `companies.md`).

## This req

- **Title:** 2027 Summer Intern, Data Engineer (Reston, VA or Remote) · Reston, VA (VA30) **or** Nationwide Remote Office (US99)
- **Term:** 10-week full-time · June–August 2027 · **no housing or relocation**
- **ATS:** Workday **R2603380** · apply: https://icf.wd5.myworkdayjobs.com/ICFExternal_Career_Site/job/Reston-VA/XMLNAME-2027-Summer-Intern--Data-Engineer--Reston--VA-or-Remote-_R2603380/apply
- **JD:** https://icf.wd5.myworkdayjobs.com/icfexternal_career_site/job/Reston-VA/XMLNAME-2027-Summer-Intern--Data-Engineer--Reston--VA-or-Remote-_R2603380
- **CXS:** https://icf.wd5.myworkdayjobs.com/wday/cxs/icf/icfexternal_career_site/job/Reston-VA/XMLNAME-2027-Summer-Intern--Data-Engineer--Reston--VA-or-Remote-_R2603380 (`canApply: true`, `posted: true`, `startDate` 2026-10-07, `questionnaireId` `3883510046131001ddc058c1eb820000`)
- **Posted:** 2026-10-07 · live `postedOn` **Posted 2 Days Ago** at capture **2026-10-09** · no Workday `endDate` — first wave (`recruiting.md` Part II §8)
- **Work:** defined project on data ingestion, transformation, quality, and documentation; SQL + code; source-to-target mappings; Agile / code review
- **Comp:** **$37,855–$77,869** annualized FTE
- **Not:** Software Developer intern **R2603002**; not an ML-research seat
- **Apply path:** Workday only. JD: bot/third-party applications may be excluded.
- **Phenom overlay:** `careers.icf.com/.../R2603380` showed "the job you are trying to apply for has been filled." Official Workday CXS still `canApply: true`. Apply on Workday, not the Phenom "filled" page.

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| SQL | SQL through use (Vylet asyncpg DAL freshness / re-scrape). Not warehouse SQL |
| Python | Python through use (MDC Pandas ETL, Vylet, SignalWeaver FastAPI) |
| Java / Scala | **Not in inventory.** Do not invent |
| ETL/ELT / databases / data structures | Pandas ETL, PostgreSQL, Redis, entity DB. Honest |
| Azure, GCP, Databricks, Snowflake, Spark | **Not in inventory.** AWS EC2 + Docker only. Do not invent |
| Git, APIs, data warehouses, orchestration | Git; Flask REST / FastAPI; Docker/Celery. No warehouse, no Airflow |
| Master's / 9 grad credits | **Preferred only.** Undergrad Junior; do not claim |

## Funnel

C-TIER (`companies.md`): Workday resume → recruiter (auth, Reston-or-remote, 30 credits) → unpublished intern loop · intern OA unpublished · no intern sys design · **bottleneck: resume** · ~20–30%. Interviews: **no AI-assisted answers** unless accommodated.

## Knockouts

1. US citizenship or permanent work authorization (federal contract) — **clears** (US citizen).
2. 30 college credits by start in CS / DE / IS / SE or related — **clears** (96 by Summer 2027; B.S. CS + Economics).
3. Class year — **clears** (no exclusive gate; Junior; May 2028). Master's is preferred, not basic.
4. GPA — unstated; **3.7** is fine.
5. Reston or remote, June–August / no relocation help — **Yes** (Reston relocate from Northville *or* remote US; valid US DL).
6. Java / Scala / Databricks / Snowflake / Spark — **not knockouts**.

## What to lead with

MDC Pandas ETL + Flask REST on EC2 scoped with MCFN. Lyndbrook PWSID entity database + scoring. Vylet SQL freshness + Docker pipeline + quality RCA. Then say you will ramp Spark/Databricks/Snowflake rather than invent them (`persona.md`).

## Do not invent

Java, Scala, Databricks, Snowflake, Spark, Azure, GCP, Airflow, Kafka, Hadoop, Tableau, Copilot, Fusion. Do not apply this packet as Software Developer **R2603002**. Skip ML-research framing. **No MatchStream.**

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. UMich start **08/31/2025**. HS **Northville High School** graduated **05/19/2025**. Credits by Summer 2027: **96**. GPA **3.7 / 4.0**. No ICF contact in `network.md` — pick **Company website / LinkedIn**, not Employee Referral, not a bot apply.

Airtable record: `rec02BGayt10HFYlT`.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/icf/data-engineer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `b837105eee9c8fc0f5a200339ffe6074392f29b5ac320dfcb91b7f5b91a1e007`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same. GPA on the PDF is **3.7**.
