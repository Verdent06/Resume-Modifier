# Data Analyst Intern at CAI (Computer Aid, Inc.)

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** ambiguous — JD requires Current Junior; intern term Summer 2027 maps to rising junior after sophomore year; GPA 3.66 vs 3.5, Economics listed, US citizen / no sponsorship, and remote US / EST hours June 7–August 6 2027 clear
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular Excel filings → Pandas ETL → PAC ranking → scored shortlist → SQL freshness DAL → React dashboard. That is this R8551 Data Analyst intern, not SWE intern R8462 and not sibling R8452 (data governance / enterprise reporting).
- Binding ding: SQL is a required working-knowledge floor (SELECT, filtering, aggregating, joining), but the only through-use is timestamp validation on a DAL, not a query that produced a ranking or KPI.
- No invented Power BI, Tableau, Excel-as-claimed-tool, Snowflake, Databricks, Copilot, Fusion, SAS, R, or stuffed HHS/social-services claims.

### Demerits

- **minor** · `resume` · SQL never used as an analysis query — JD requires working knowledge of SQL for querying and joining relational data (SELECT, filtering, aggregating, joining). Skills lists SQL; Vylet leads with injection-safe timestamp validation on an asyncpg DAL, and SignalWeaver persists scores to Postgres. An HHS program-reporting screen looks for query/aggregate/join SQL that produced a ranking or KPI and does not find it — the PAC ranking and Review Velocity shortlist read as Python/Pandas work.

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line and the leading Vylet DAL, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for viz; Vylet 79→89% quality catch plus 30x scored pipeline if they ask for data quality / recurring reporting
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Power BI / Tableau / Excel-as-claimed-tool are not in inventory — walk the React/Postgres dashboard instead of inventing BI tools; this is R8551 Data Analyst Intern, not R8452 and not SWE intern R8462; class-year: page shows Expected May 2028 vs JD Current Junior — do not relabel Education
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-quality analog; SignalWeaver 3.39% R² as "the score is not just fitting noise." No confirmed OA on this DA posting — expect SQL/Excel/dashboard fluency, a project deep-dive, and STAR. Behavioral is a filter (`recruiting.md` §6). Confirm June 7–August 6 2027, 40h, 8:30 a.m.–5:00 p.m. EST, work from the US.

## Likelihood

- **Resume screen:** High — eligibility GPA/degree/auth is clean and the top half is ingest → ranking/shortlist → dashboard; class-year radio (Current Junior vs rising junior) is the unresolved knockout
- **Overall hire odds:** Medium — CAI is C-tier with a resume then unpublished recruiter/phone/manager/client bottleneck (~20–30%) and no confirmed OA, so this page should clear the binding intern gate if the Current Junior gate is not auto-enforced; the loop still has to defend Python/SQL fluency, the BI-tool gap, and EST core hours
- **Funnel filters:** Workday **R8551** resume screen (posted 2026-09-22) → Talent Acquisition review → phone screen → manager / technical / client interview (`careers.cai.io/us/en/how-we-hire`) · intern OA unpublished · no intern sys design · Bottleneck: resume · ~20–30% **[directional, peer of ICF / Resultant / Wipfli D&A]** (`companies.md`). GPA 3.5+. No sponsorship now or later. Remote US. **Not** R8452
- **Outside the resume:** Apply in this first wave. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI/class-year answer. Confirm June 7–August 6 2027 remote US / 8:30–5 EST
