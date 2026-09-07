# NXP — intern notes (Data Analytics Engineer Intern - Summer 2027, Austin Oakhill)

Intern-facing packet notes for Workday **R-10065538**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What NXP builds

Public semiconductor (NASDAQ: NXPI; FY2025 rev $12.27B): secure connectivity and edge-processing chips for automotive, industrial & IoT, mobile, and comms infrastructure — the silicon, not fab equipment. Austin (Oakhill) is a major US site. This intern is **engineering-ops analytics** (project metrics, dashboards, resource/effort planning, automation scripts) — not DFT, not Demand Planning intern R-10064588, and not embedded ML.

## This req

- **Title:** Data Analytics Engineer Intern - Summer 2027 · Austin (Oakhill Office), TX · onsite · full time
- **Term:** Summer 2027; must return to school or graduate at intern end; if graduating prior to **July 2027**, apply FT
- **ATS:** Workday **R-10065538** · https://nxp.wd3.myworkdayjobs.com/en-US/careers/job/Austin-Oakhill-Office/Data-Analytics-Engineer-Intern---Summer-2027_R-10065538
- **Posted:** 2026-09-07 · Workday `endDate` **2026-10-02** — first wave (`recruiting.md` Part II §8); short window
- **Work:** metrics/reporting for engineering project planning; dashboards for project status / resource utilization / engineering performance; data collection/validation; automation scripts; analytics models
- **Comp:** unpublished on this JD. Analog only: Levels.fyi Hardware Engineer Intern Austin Summer 2026 **$45/hr** + $1k housing **[directional]**

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python | Python through use (MDC Pandas ETL, Vylet, SignalWeaver) |
| SQL | SQL through use as DAL freshness (Vylet asyncpg timestamps). **Not** analyst JOIN/aggregate SQL — do not invent it |
| Excel / Power BI (plus, *or similar*) | **Not in inventory.** Analog: irregular Excel *exports as source data* at MDC; React/Postgres dashboard on SignalWeaver. Do not check the BI product names |
| Dashboards / reports / metrics | PAC ranking + Flask API (MDC); Review Velocity shortlist (Lyndbrook); React dashboard (SignalWeaver) |
| Automation scripts | Vylet 30x Dockerized pipeline; Lyndbrook 15 hours/week; MDC ~800 hours |
| Snowflake / Databricks / Tableau / Copilot / Fusion / Sentry | **Not in inventory.** Do not invent |

## Funnel

B-TIER (`companies.md`): Workday resume → unpublished OA on some *other* intern tracks (not confirmed for this DA) → recruiter/HM → tech + behavioral · Easy–Med practical · no intern sys design · **bottleneck: resume** · ~8–12%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Listed majors — **clears** (CS + Economics).
2. Return-to-school / July 2027 FT cutoff — **clears** (Expected May 2028; Junior; 96 credits by Summer 2027).
3. GPA unstated — **3.66**.
4. Austin Oakhill onsite — **Yes** (relocate).
5. Power BI / Excel / Tableau — **not knockouts** if unclaimed; inventing them is worse.

## What to lead with

MDC Pandas ETL + PAC ranking. Lyndbrook Review Velocity shortlist + 15 hours/week. SignalWeaver React dashboard as the viz analog. Vylet SQL freshness if they ask how you validate a source; Vylet 30x if they ask for automation. Then say you will ramp NXP's BI stack rather than invent Power BI (`persona.md`).

## Do not invent

Tableau, Power BI, Excel-as-BI, Copilot, Snowflake, Databricks, Fusion, Sentry, MATLAB, JMP, NXP project systems, DFT/RTL internships.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168 ZIP **48168**. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. High school: Northville High School, graduated **05/19/2025**. UMich start **08/31/2025**. Junior, Expected May 2028, GPA 3.66, **96 credits by Summer 2027**. No NXP contact in `network.md` — pick **Job board / Company website**, not Employee Referral.

Workday questionnaires were **HTTP 406** without an account. Full paste table: `written-answers.md`.

## PDF

`applications/2027/nxp/data-analytics-engineer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `218294fb4a1a37484300ffa0e138cf0e9f18b02968548183d34293aefa310a03`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **9.0 / 10** (1 minor: SQL/DAL unquantified). See `WORTH_IT.md` and `grade.md`.
