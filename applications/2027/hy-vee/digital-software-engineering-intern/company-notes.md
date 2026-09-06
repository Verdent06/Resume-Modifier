# Hy-Vee — intern notes (Digital Software Engineering Intern, Summer 2027)

Intern-facing packet notes for Workday **R250133**. Not a rewrite of `company.md` (covers both R250133 Digital SWE and R250146 Data Analytics). Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Hy-Vee builds

Employee-owned Midwest grocer (West Des Moines HQ): 550+ units, nine states, ~$12B sales, 70k employees. Digital/IT sits at Helpful Smiles Technology (HST) in Grimes, IA — e-commerce, mobile, supply chain, finance, DW/BI. This intern is **grocery digital business-application SWE**, not a store job and **not** the Data Integration Intern sibling (WDM corporate pipelines).

## This req

- **Title:** Digital Software Engineering Intern - Summer 2027 · HST Grimes, IA (ATS: Corporate Office, Westown Pkwy, West Des Moines) · in person · paid, up to 40h/wk · comp unlisted
- **Term:** Summer 2027
- **ATS:** Workday **R250133** · https://hyvee.wd1.myworkdayjobs.com/HyVeeCareers/job/Corporate-Office-Westown-Pkwy-West-Des-Moines-IA/Digital-Software-Engineering-Intern---Summer-2027_R250133
- **Posted:** 2026-09-04 · Workday `endDate` **2026-10-31** — first wave (`recruiting.md` Part II §8)
- **Work:** Agile business apps, unit tests, Microsoft Reporting Services, Microsoft SQL Server data retrieval, coding standards. Pre-employment drug screen.

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Software development / business applications | Flask REST on EC2 (MDC); React dashboard (SignalWeaver); Dockerized product (Vylet) |
| Unit tests | GitHub Actions + pytest (SignalWeaver). Named production debug exists in the pool (Vylet 79%→89%) but is not on this PDF |
| Microsoft SQL Server | SQL through use (Vylet asyncpg timestamp validation). **No** SQL Server |
| Microsoft Reporting Services | React/TypeScript dashboard over Postgres. **No** SSRS |
| Agile / cross-functional | MDC stakeholder-scoped contract |
| C# / .NET / Java / e-commerce platforms | **Not** in inventory. Do not invent |

## Funnel

C-TIER (`companies.md`): Workday resume → recruiter phone → likely Easy tech + behavioral · intern OA unpublished · no intern sys design · **bottleneck: resume** · ~15–25%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Work authorization / sponsorship — **clears** (US citizen; no sponsorship now or later).
2. Class year / degree — **clears** (working toward CS; Expected May 2028; Junior; 96 credits by Summer 2027). No exclusive window on this JD.
3. GPA — unstated. **3.66** is a plus.
4. Grimes / West Des Moines onsite Summer 2027 — **Yes** (relocate from Northville, MI).
5. Pre-employment drug screen — acknowledge; do not treat as a resume fail.
6. SSRS / SQL Server / C# — **not knockouts**.

## What to lead with

MDC Flask REST + Pandas ETL. Vylet SQL freshness. SignalWeaver dashboard + pytest. Then say you will ramp SSRS/SQL Server rather than invent them (`persona.md`).

## Do not invent

Microsoft SQL Server, SSRS, C#, .NET, Java, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, Hy-Vee Aisle/POS platforms, grocery internships.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. High school Northville High School graduated **05/19/2025**. UMich start **08/31/2025**. No Hy-Vee contact in `network.md` — do not pick Employee Referral.

Later Workday wizard pages were **not visible without creating an account**. Do not invent extra essay prompts.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/hy-vee/digital-software-engineering-intern/Vedant Desai Resume.pdf`

**SHA-256:** `99493462ebe367e88ab2d421f8fe46509d68d97275bae85cea783f0637e2c4e0`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **9.0 / 10** (1 minor: grocery-digital differentiator absent). See `WORTH_IT.md` and `grade.md`.
