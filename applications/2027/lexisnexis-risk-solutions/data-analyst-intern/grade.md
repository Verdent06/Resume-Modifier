# Data Analyst Intern at LexisNexis Risk Solutions

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — enrolled undergrad Expected May 2028 matches JD; B.S. Computer Science and Economics is related to BA/DA; US citizen; no clearance knockout
- **Track:** ai-ml + enterprise BI / risk-data (AML, identity, fraud, customer-data) for BTO transformation & migration reporting
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.7, Expected May 2028, and a lead spine of irregular filings → Pandas ETL → PAC ranking → Vylet SQL freshness / identity-collision catch → Lyndbrook multi-source entity shortlist → React dashboard. That is this R119377 BTO Data Analyst intern, not the Data Science Intern sibling, not Insurance Data Analytics intern, and not a SWE intern.
- Binding ding: foundational SQL is a JD floor, but the only through-use is timestamp validation on a DAL, not a query that produced a ranking or a reconciled migration-style table.
- No invented Power BI, DAX, Excel-as-claimed-tool, Tableau, Snowflake, Databricks, Copilot, Fusion.

### Demerits

- **minor** · `resume` · SQL never used as an analysis query — JD floor is foundational SQL to extract/transform/analyze. Skills lists SQL; Vylet in the second slot makes injection-safe timestamp validation visible, and SignalWeaver persists scores to Postgres. A BTO BI screen looks for query/aggregate/join SQL that produced a ranking, reconciliation, or KPI and does not find it — PAC rankings and Review Velocity read as Python/Pandas work.

### Misreads

- A keyword-first pass for Power BI / DAX / Excel can bucket this as "wrong stack" even though Pandas-on-Excel-exports, PAC rankings, entity reconciliation, and a React dashboard are on the page.
- SQL on the Languages line plus the leading Vylet DAL can file as analysis SQL, then bounce in the case round when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- Flask REST / founder MRR on Vylet can file as product-SWE if the reader never reaches the ETL, ranking, identity-collision, and dashboard lines.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN; ~800 hours / 400 PACs) as the ingest → KPI → report loop this seat tests; Vylet SQL freshness + 79%→89% name-collision catch as the identity / data-quality analog; Lyndbrook EPA/MassGIS entity database → Review Velocity shortlist (800 → 280, 35% precision) as the multi-source validation / migration-tracking analog; SignalWeaver React/Postgres dashboard if they ask for viz
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Power BI / DAX / Excel-as-claimed-tool are not in inventory — walk the React/Postgres dashboard and Pandas-on-Excel-exports instead of inventing BI tools; this is R119377 Data Analyst Intern on BTO Data, not the Data Science Intern sibling and not Insurance Data Analytics intern; Alpharetta on-site May 24–July 30 2027 with no relocation assistance — confirm housing plan
- **Depth prep:** Directional loop is recruiter/HireVue → SQL/Excel/data-interpretation or take-home case → behavioral (`company.md`; intern OA unpublished — do not assume HackerRank/CodeSignal). Walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist). Prep honest SQL joins/aggregates even though the page's SQL is plumbing. Behavioral is a filter (`recruiting.md` §6). Confirm 10-week on-site Alpharetta (Alderman), $20/hr, no benefits, no relocation.

## Likelihood

- **Resume screen:** High — eligible Expected May 2028, GPA 3.7, and an ingest → ranking/shortlist → SQL freshness → dashboard spine on a resume-first C-tier intern req
- **Overall hire odds:** Medium — LNRS intern bottleneck is the resume (~15–25% directional, Thomson Reuters peer) with no published coding OA; residual cut is the Alpharetta on-site / no-relocation commit, a SQL/Excel/data-interpretation or take-home case, and STAR
- **Funnel filters:** Workday **R119377** (`relx.wd3` / `RiskSolutions`) resume → recruiter/HireVue screen **[directional]** → SQL/Excel/data-interpretation or take-home case **[directional]** → behavioral · intern OA unpublished · no intern sys design · Bottleneck: **resume** · ~15–25% **[directional, C-tier peer of Thomson Reuters]** (`company.md`). Posted 2026-10-05; `endDate` 2026-10-24. **$20/hr**. On-site Alpharetta May 24–July 30 2027. **Not** Data Science Intern sibling
- **Outside the resume:** Apply on Workday this first-wave window. Confirm US work auth and Alpharetta housing. Prep STAR plus an honest SQL walk. Do not mix this req with the Data Science Intern sibling
