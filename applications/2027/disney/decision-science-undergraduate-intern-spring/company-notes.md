# Disney DDSI — intern notes (Spring 2027 Decision Science Undergraduate Intern, Lake Buena Vista)

Intern-facing packet notes for Workday **10159998**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What DDSI builds

Disney Decision Science and Integration supports yield management, revenue planning, forecasting, pricing, and optimization across Disney Experiences, Disney Entertainment, and ESPN. Interns prep/validate/report data, support ML and optimization models, and do guided modeling — not Parks labor-web SWE and not Streaming SDE.

Legal employer: **1008 Disney Worldwide Services, Inc.** ATS: **`disneycareerdc`** (corporate — not Parks `disneycareer`). Site: **USA - FL - Team Disney - Florida**. Comp **$42/hr**. Same dollar band as Disney Streaming SWE is coincidence.

## This req

- **Title:** Decision Science Undergraduate Intern, Spring 2027
- **Term:** January–June 2027, full-time, Mon–Fri 40 hours; primarily on-site / occasionally from home
- **ATS:** Workday **10159998** · https://disney.wd5.myworkdayjobs.com/disneycareerdc/job/Lake-Buena-Vista-FL-USA/Decision-Science-Undergraduate-Intern--Spring-2027_10159998
- **Posted:** 2026-09-21 · Workday `endDate` **2026-09-30** — first wave (`recruiting.md` Part II §8)
- **Work:** data prep/exploration/validation/reporting; support analysis/validation/maintenance of ML and optimization models; modeling infrastructure; guided RM/pricing/marketing/finance modeling
- **Comp:** **$42/hr** (Florida). Limited ACC Florida housing; reliable transportation required
- **Not:** Parks PI WDW CS/CE **10158145**, Labor Systems **10158184** ($31/hr Parks), Decision Science Graduate Associate, Disney Streaming SWE

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python, R, or SQL (or-list) | Python through use (MDC Pandas ETL, Vylet, SignalWeaver). SQL through use as DAL freshness (Vylet asyncpg timestamps). **Not** analyst JOIN/aggregate SQL — do not invent it. **No R** |
| Tableau / PowerBI / other viz (familiarity) | **Not Tableau/PowerBI.** Analog: React/Postgres dashboard on SignalWeaver. Do not check the BI product names |
| Excel / Word / PowerPoint | **Not claimed as BI tools.** Irregular Excel *exports as source data* at MDC only |
| Forecasting / ML / NLP / simulation / optimization / econometrics (one or more) | Linear regression + held-out R² (SignalWeaver); PAC ranking (MDC); Review Velocity scoring (Lyndbrook). **No CPLEX, Gurobi, SAS, scikit-learn** |
| Snowflake / Databricks / Copilot / Fusion | **Not in inventory.** Do not invent |

## Funnel

B-TIER (`companies.md`): Workday `disneycareerdc` resume → recruiter → unpublished OA for **this** DDSI undergrad intern (do not assume HackerRank; generic DS intern reports SQL/Python/pandas + stats + case **[directional]**) · Easy–Med practical · no intern sys design · **bottleneck: resume** · ~5–10%. Mid-size / non-tech-tech-shaped intern loops are resume-first (`recruiting.md` Part I). Close **2026-09-30**.

## Knockouts

1. Junior or senior bachelor’s in CS / Economics / Stats / OR / STEM — **clears** (CS + Economics; junior during Spring 2027).
2. Enrolled taking a class semester prior — **clears**.
3. 18+ — **clears** (DOB 12/16/2006).
4. Unrestricted work authorization — **clears** (US citizen).
5. One-year Disney intern/program cap — **clears** (never a Disney intern or College Program).
6. Tableau / PowerBI / R — **not knockouts** if unclaimed; inventing them is worse.

## What to lead with

MDC Pandas ETL + PAC ranking. Lyndbrook Review Velocity shortlist. SignalWeaver regression + React dashboard as the modeling/viz analog. Vylet SQL freshness if they ask how you validate a source. Then say you will ramp DDSI's BI/solver stack rather than invent Tableau or CPLEX (`persona.md`).

## Do not invent

Tableau, PowerBI, Snowflake, Databricks, Copilot, Fusion, R, SAS, CPLEX, Gurobi, Disney RM internships, MagicBand / yield systems.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168 ZIP **48168**. US citizen. DOB **12/16/2006**. SAT **1510** if asked. UMich Expected May 2028, GPA 3.66. No Disney contact in `network.md` — pick **Company website / job board**, not Employee Referral.

Workday questionnaires were **HTTP 406** without an account (`questionnaireId` `80e74446762e100116719c7d84430000`, secondary `9c0a0b63e6b710010b4897fd22ca0000`). Full paste table: `written-answers.md`.

## PDF

`applications/2027/disney/decision-science-undergraduate-intern-spring/Vedant Desai Resume.pdf`

**SHA-256:** `fba5b17150d6ed54664b7805c319fe6e3bd47c015f0361ada7d02196e297aed6`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **8.0 / 10** (2 minor: SQL not analysis SQL; Vylet SQL/DAL metric-free). See `WORTH_IT.md` and `grade.md`.
