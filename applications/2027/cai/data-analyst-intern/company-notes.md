# CAI — intern notes (Data Analyst Intern R8551)

Intern-facing packet notes for Workday **R8551**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What CAI builds

Privately held global IT services / consulting (founded 1981; JD: 40+ years). JD: ~9,000 associates, yearly revenue **$1.3B+**. Public + commercial sectors; neurodiversity-in-the-enterprise program. HQ Allentown, PA (1390 Ridgeview Drive, 18104). This intern is **HHS program analytics** (behavioral health, child welfare, child support): clean data, dashboards, quality review — not SWE intern R8462 and not sibling R8452 (data governance / enterprise reporting).

## This req

- **Title:** Data Analyst Intern
- **Req:** Workday **R8551** · posting id `Data-Analyst-Intern_R8551`
- **Term:** **June 7, 2027 – August 6, 2027** (9 weeks; JD HTML truncates "August 6, 202")
- **Work:** remote; 40h/wk; **8:30 a.m.–5:00 p.m. EST**; all work in the US
- **ATS:** `cai.wd5` / `computer_aid` · `includeResumeParsing: true` · `questionnaireId` `81f883d4e009100203d6dad787620000`
- **JD:** https://cai.wd5.myworkdayjobs.com/computer_aid/job/PA-CLIENT-STATE/Data-Analyst-Intern_R8551
- **Apply (do not submit from this packet):** https://cai.wd5.myworkdayjobs.com/en-US/computer_aid/job/PA-CLIENT-STATE/Data-Analyst-Intern_R8551/apply
- **Posted:** 2026-09-22 — first wave (`recruiting.md` Part II §8)
- **Comp:** unpublished on CXS. C-tier intern **$22–38/hr** band **[directional]**
- **Not:** R8452 · R8422 · R8421 · R8462

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| SQL (SELECT / filter / aggregate / join) | SQL through use as DAL freshness (Vylet asyncpg timestamps). **Not** analyst JOIN/aggregate SQL — do not invent it |
| Python | Not named on this JD. Python through use (MDC Pandas ETL, Vylet, SignalWeaver) |
| Excel / Word / PowerPoint; pivot, VLOOKUP/XLOOKUP | **Not in inventory as a claimed tool.** Analog: irregular Excel *exports as source data* at MDC. Do not check pivot/XLOOKUP |
| Power BI / Tableau | **None.** React dashboard + PAC rankings as analog. Do not invent them |
| Data cleansing / quality / KPIs / dashboards | MDC PAC rankings + Flask to MCFN; Lyndbrook Review Velocity; SignalWeaver React dashboard; Vylet 79→89% quality catch |
| Social services / family support (preferred) | **Not in pool.** Do not invent HHS |
| Snowflake / Databricks / Copilot / Fusion | **Not in pool. Do not invent** |

## Funnel

C-TIER (`companies.md`): Workday resume → Talent Acquisition review → phone screen → manager / technical / client interview (`careers.cai.io/us/en/how-we-hire`) · intern OA unpublished · Easy STAR + SQL/Excel/dashboard walk · no intern sys design · **bottleneck: resume** · ~20–30% **[directional, peer of ICF / Resultant / Wipfli D&A]**. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech). Onboarding later: background check + drug screen.

## Knockouts

1. Work auth / no sponsorship now or later — **clears** (US citizen).
2. GPA 3.5+ — **clears** (3.66).
3. Economics / related — **clears** (CS + Economics).
4. Current Junior — **ambiguous** (Expected May 2028; Summer 2027 = rising junior / after sophomore year).
5. Remote US / June 7–August 6 2027 / 40h / 8:30–5 EST — **Yes**.
6. Power BI / Tableau / Excel-as-BI — **not knockouts** if unclaimed; inventing them is worse.

## What to lead with

MDC Pandas ETL + PAC ranking. Lyndbrook Review Velocity shortlist. SignalWeaver React dashboard as the viz analog. Vylet SQL freshness + 79→89% if they ask how you know a source is true / data quality. Then say you will ramp CAI's BI stack rather than invent Tableau/Power BI (`persona.md`).

## Do not invent

Power BI, Tableau, Excel-as-BI, Snowflake, Databricks, Copilot, Fusion, SAS, R, CAI HHS systems, behavioral-health / child-welfare / child-support internships, LoRA-as-lead / ML-research framing.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168 ZIP **48168**. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. High school: Northville High School, graduated **05/19/2025**. UMich start **08/31/2025**. Junior, Expected May 2028, GPA 3.66. No CAI contact in `network.md` — pick **Career Websites** / Job board, not Employee Referral.

Workday questionnaires were **HTTP 406** without an account. Full paste table: `written-answers.md`.

## PDF

`applications/2027/cai/data-analyst-intern/Vedant Desai Resume.pdf`

**SHA-256:** `90fdc4fa84d616592d092e0df21e464e54ff0ac43dd52435544eb20d60a9bf59`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES** on skill/project fit. Pipeline score **9.0 / 10** (1 minor: SQL not analysis SQL). Class-year radio remains the unresolved knockout. See `WORTH_IT.md` and `grade.md`.
