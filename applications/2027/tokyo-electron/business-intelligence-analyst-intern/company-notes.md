# Tokyo Electron — intern notes (Summer 2027 Business Intelligence Analyst Intern, Austin)

Intern-facing packet notes for Workday **R26-01504**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What TEL builds

Public semiconductor **capital-equipment** company (TSE: 8035; FY2026 net sales ¥2,443.5B): etch, deposition, coater/developer, cleaning tools fabs use — not the chips. US HQ is Austin **RiverSouth**. This intern is **BI for Service and Sales Support operations** (validate source data, reports/dashboards, workflows) — not an ATG research intern, not a process-engineer intern, and not the Data Engineer sibling.

## This req

- **Title:** Business Intelligence Analyst Summer 2027 Intern · Austin RiverSouth · onsite · full time
- **Term:** Monday, May 17 – August 20, 2027
- **ATS:** Workday **R26-01504** · https://tel.wd3.myworkdayjobs.com/tel-careers/job/Austin-RiverSouth/Business-Intelligence-Analyst-Summer-2027-Intern_R26-01504
- **Posted:** 2026-09-07 · no public Workday `endDate` — first wave (`recruiting.md` Part II §8)
- **Work:** data validation/integrity; basic reports and dashboards; monitor reports/apps/workflows; foundational data prep for Sales and Service; Lean training provided
- **Comp:** unpublished on this JD. Analog only: TEL US intern **$21.06–$28.16/hr** (BuiltIn Automation intern 2026) **[directional]**

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Power BI / Excel / Power Pivot (*e.g.* viz) | **Not in inventory.** Analog: irregular Excel *exports as source data* at MDC; React/Postgres dashboard on SignalWeaver. Do not check the BI product names |
| Data validation / integrity / source data | Vylet SQL timestamp freshness / re-scrape; Lyndbrook 800+ validated targets. **Not** analyst JOIN SQL |
| Reports / dashboards / workflows / applications | MDC Flask REST to researchers; SignalWeaver React dashboard + FastAPI scores; Vylet Dockerized recurring pipeline |
| Python / SQL (unnamed on this JD; expected on a BI screen) | Python through use (MDC Pandas ETL). SQL through use as DAL freshness (Vylet). Do not invent analysis SQL |
| Snowflake / Databricks / Tableau / Copilot / Fusion / Sentry | **Not in inventory.** Do not invent |
| Lean | Training provided. **No Lean cert** — do not claim one |

## Funnel

B-TIER (`companies.md`): Workday resume → unpublished OA (**not** confirmed for this BI) → recruiter → Easy practical + STAR · no intern sys design · **bottleneck: resume** · ~8–12%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Listed majors — **clears** (CS + Economics).
2. Class year — **clears** (Expected May 2028; Junior; ~96 credits by Summer 2027; returns Fall 2027).
3. GPA — unstated — **clears** (3.66).
4. Austin onsite May 17–August 20 2027 — **Yes** (relocate from Northville, MI).
5. Power BI / Excel / Power Pivot — **not knockouts** if unclaimed; inventing them is worse.
6. Work auth — unstated on this JD; sibling process intern: no sponsorship. **US citizen; no sponsorship.**

## What to lead with

MDC Pandas ETL + PAC ranking. Lyndbrook Review Velocity shortlist. SignalWeaver React dashboard as the viz analog. Vylet SQL freshness if they ask how you know a source is still true. Then say you will ramp TEL's BI stack rather than invent Power BI (`persona.md`).

## Do not invent

Snowflake, Databricks, Copilot, Tableau, Power BI, Excel-as-BI, Power Pivot, Fusion, Sentry, Lean Six Sigma certs, TEL CRM/Field Solutions platforms, wafer/process tools.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168 ZIP **48168**. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. High school: Northville High School, graduated **05/19/2025**. UMich start **08/31/2025**. Junior, Expected May 2028, GPA 3.66, **96 credits by Summer 2027**. No TEL contact in `network.md` — pick **Job board / LinkedIn**, not Employee Referral.

Workday questionnaires were **HTTP 406** without an account (`questionnaireId` `6906243b16e410017821c3dacdb50000`). Full paste table: `written-answers.md`.

**Do not submit from this agent.** Packet only.

## PDF

`applications/2027/tokyo-electron/business-intelligence-analyst-intern/Vedant Desai Resume.pdf`

**SHA-256:** `dce4eb9f9e9cd48c3f0d3478b6d413977eb91e3bedc673416e379914433ff28e`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **8.0 / 10** (2 minor: SQL not analysis SQL; Power BI/Excel/Power Pivot unnamed). See `WORTH_IT.md` and `grade.md`.
