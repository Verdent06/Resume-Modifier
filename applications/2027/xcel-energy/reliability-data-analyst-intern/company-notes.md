# Xcel Energy — intern notes (Reliability Data Analyst Intern- CO, EDSP)

Intern-facing packet notes for Workday **JR115833**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Xcel Energy builds

Fortune 500 (#286, 2026) **[directional — us500.com]** (NASDAQ: XEL) Minneapolis-based regulated electric and gas utility. JD: 3.4M electric / 1.9M gas customers across eight states (FY2025 10-K: 3.9M / 2.2M). Colorado ops sit under PSCo. This intern is **EDSP reliability analytics at Lipan Distribution Center in Denver** — outage, reliability-metric, and asset-performance reporting — not Distribution Modeling & Analytics, not Gas Data Intern, and not generic utility IT.

## This req

- **Title:** Reliability Data Analyst Intern- CO · Denver, CO 80223 · Lipan Distribution Center, 1123 W 3rd Ave · hybrid commute · **$19.00–$20.90/hr**
- **Term:** Start **May 31, 2027**; full-time summer (up to 40h) / part-time school year (up to 20h) if extended
- **ATS:** Workday **JR115833** · https://xcelenergy.wd1.myworkdayjobs.com/External/job/Denver-CO-80223/Reliability-Data-Analyst-Intern--CO_JR115833
- **Posted:** 2026-09-07 · Deadline **10/16/26** · Workday `endDate` **2026-10-17** — first wave (`recruiting.md` Part II §8)
- **Work:** analyze outage / reliability / asset-performance data; dashboards/reports in Excel, Power BI, Databricks; multi-source validation/cleansing; present findings to EDSP

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python | Python through use (MDC Pandas ETL, Vylet, SignalWeaver) |
| SQL | SQL through use as DAL freshness (Vylet asyncpg timestamps). **Not** analyst JOIN/aggregate SQL — do not invent it |
| Excel / Power BI / Databricks | **Not in inventory.** Analog: irregular Excel *exports as source data* at MDC; React/Postgres dashboard on SignalWeaver. Do not check the BI/lakehouse product names |
| Snowflake / Tableau / Copilot / Fusion / Sentry | **Not in inventory.** Do not invent |
| Electric distribution / OMS / SAIDI | Analog only: water-utility operator targeting + fleet scoring (Lyndbrook). **Not** Xcel outage systems |

## Funnel

C-TIER (`companies.md`): Workday resume → recruiter/HM → panel (2–3; STAR + basic grid knowledge) · intern OA unpublished · no intern sys design · **bottleneck: resume** · ~20–30%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech). Glassdoor intern-track: no standardized coding test **[directional]**.

## Knockouts

1. Sophomore+ as of Fall 2027 — **clears** (Junior; Expected May 2028).
2. Listed majors — **clears** (CS + Economics).
3. GPA sibling convention ~3.5 commercial — **clears** (3.66).
4. Denver LDC hybrid commute May 31 2027 — **Yes** (relocate).
5. Valid US DL — **Yes**.
6. Power BI / Databricks / Excel-as-BI — **not knockouts** if unclaimed; inventing them is worse.

## What to lead with

MDC Pandas ETL + PAC ranking. Lyndbrook water-utility entity DB + Review Velocity. Vylet SQL freshness. SignalWeaver React dashboard as the Power BI analog. Then say you will ramp EDSP tools rather than invent them (`persona.md`).

## Do not invent

Power BI, Excel-as-tool, Databricks, Snowflake, Tableau, Copilot, Fusion, Sentry, OMS, SAIDI/SAIFI internships, Xcel EDSP platforms.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510**. School start **08/31/2025**. HS Northville High School **05/19/2025**. **96 credits by Summer 2027.** No Xcel contact in `network.md` — pick **Job board / Simplify**, not Employee Referral.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/xcel-energy/reliability-data-analyst-intern/Vedant Desai Resume.pdf`

**SHA-256:** `a73bd373f54212e521cbab129cbca6945a97b3f44a8f9c38d8407e25495ee8a3`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **10.0 / 10** (0 demerits). Pay is D-tier band ($19–$20.90/hr) on C-tier work. See `WORTH_IT.md` and `grade.md`.
