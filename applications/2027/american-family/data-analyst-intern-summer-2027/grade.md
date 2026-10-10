# Summer 2027 Intern - Data Analyst at American Family Insurance

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — student at an accredited 4-year during the internship, Expected May 2028 (after August 2027); B.S. Computer Science and Economics aligns with Data Analyst; US citizen so the no-sponsorship clause clears; posting open (`canApply: true`)
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.7, Expected May 2028, and a lead spine of irregular filings → Pandas ETL → PAC ranking → scored shortlist → 30x scored pipeline → React dashboard. That is this R39404 Data Analyst intern, not a SWE intern and not sibling R39401.
- Binding ding: SQL is preferred, but the only through-use is timestamp validation on a DAL, not a query that produced a ranking or KPI.
- No invented Tableau, Power BI, Excel-as-claimed-tool, SAS, R, Snowflake, Databricks, Copilot, Fusion, or Microsoft Office as a claimed skill line.

### Demerits

- **minor** · `Vylet` · SQL through-use is DAL freshness, not analysis SQL — JD prefers SQL for a Data Analyst intern who collects, analyzes, and reports KPIs. Skills lists SQL; the only through-use is injection-safe timestamp validation and automatic re-scrapes on an asyncpg DAL. PAC rankings and Review Velocity read as Python/Pandas.

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line and the Vylet DAL, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for reports/viz; Vylet 30x scored pipeline plus 79→89% quality catch if they ask for KPIs / data quality
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no sized freshness metric)*; Tableau / Power BI / Excel-as-claimed-tool / Microsoft Office skill line are not in inventory — walk the React/Postgres dashboard instead of inventing BI tools; this is R39404 Data Analyst Intern, not R39401 Internal Data and Analytics; class-year: page shows Expected May 2028 vs Summer 2027 — graduating August 2027 or later clears
- **Depth prep:** STAR on presenting a ranking or shortlist to a non-builder (MDC/Lyndbrook); walk ingest → score → dashboard on SignalWeaver (3.39% R² as "the score is not just fitting noise"); honest SQL answer (timestamp freshness, not analysis SQL). No published intern OA — expect Easy Python/SQL fluency + STAR (`companies.md` peer of Nationwide / NM ID&A). Madison hybrid + in-person first-week NEO.

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.7, CS + Economics, US citizen) and the top half is ingest → ranking/shortlist → dashboard; one unquantified SQL-plumbing line does not sink a C-tier DA intern screen
- **Overall hire odds:** Medium — American Family is C-tier with a resume bottleneck (~15–25%) and no published intern OA, so the PDF is the binding filter. The remaining cut is Madison hybrid + in-person NEO, defending Python/SQL fluency without analysis-SQL, and STAR on presenting findings
- **Funnel filters:** Workday **R39404** resume screen (posted 2026-10-09) → recruiter (auth, Madison hybrid + in-person NEO, enrollment, no sponsorship) → unpublished intern loop. Intern OA unpublished. No intern sys design. Bottleneck: resume · ~15–25% (`companies.md` C-tier, peer of Nationwide / State Farm / Great American / Northwestern Mutual). Comp **$25–$39/hr**. **Not** R39401
- **Outside the resume:** Apply in this first wave. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer. Form email **`verdent06@gmail.com`**. Do not invent Tableau/Power BI/Excel/Microsoft Office on the form
