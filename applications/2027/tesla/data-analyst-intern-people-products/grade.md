# Data Analyst Intern – People Products (Winter/Spring 2027) at Tesla

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — pursuing B.S. Computer Science (listed STEM) and Economics, Expected May 2028; JD requires a bachelor's in CS/data/stats/STEM plus 12+ weeks Spring onsite; no class-year, GPA, clearance, or citizenship knockout on the posting
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.7, Expected May 2028, and a lead spine of irregular Excel filings → Pandas ETL → PAC ranking → SQL freshness DAL → scored shortlist → React/Postgres dashboard. That is this People Analytics intern (req 286085), not People Products SWE, not Autopilot, and not Service Tooling.
- Binding ding: SQL is a write-queries floor, but the only through-use is timestamp validation on a DAL, not a query that produced a ranking or KPI.
- No invented Tableau, Power BI, Looker, SQL Server, MySQL, Snowflake, Databricks, Copilot, Fusion, or stuffed Tesla HRIS claims.

### Demerits

- **minor** · `resume` · SQL never used as an analysis query — JD requires writing SQL to collect, clean, analyze, and interpret data from multiple systems. Skills lists SQL; Vylet sits second and leads with injection-safe timestamp validation on an asyncpg DAL, and SignalWeaver persists scores to Postgres. A People Analytics screen looks for query/aggregate/join SQL that produced a ranking or KPI and does not find it — PAC ranking and Review Velocity shortlist read as Python/Pandas work.

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line and the second-entry Vylet DAL, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for viz; Vylet 79→89% quality catch plus 30x scored pipeline if they ask for data quality / recurring reporting
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Tableau / Power BI / Looker / SQL Server / MySQL are not in inventory — walk the React/Postgres dashboard and PostgreSQL DAL instead of inventing BI/SQL-Server; this is People Analytics 286085, not People Products SWE, not Autopilot, not Service Tooling; Winter/Spring onsite is Palo Alto **or** Austin — pick one you can actually relocate to
- **Depth prep:** walk a non-builder (recruiting/HR analog) through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-quality analog; SignalWeaver 3.39% R² as "the score is not just fitting noise." Tesla intern OA is HackerRank Medium (Codility on some cycles). Behavioral is a filter (`recruiting.md` §6). Confirm January–April 2027, 40h onsite, remain enrolled.

## Likelihood

- **Resume screen:** High — CS/STEM degree and student status clear the printed knockouts; the top half is ingest → ranking/shortlist → dashboard without BI-tool fabrication
- **Overall hire odds:** Medium — Tesla is B-tier with a HackerRank then tech-round bottleneck (~5–8%); this page should win People Analytics team-match if the OA is passed; the loop still has to defend Python/SQL fluency, the BI-tool gap, and Winter/Spring 40hr onsite logistics
- **Funnel filters:** Tesla ATS resume screen → HackerRank Medium (Codility on some intern cycles) → tech rounds (bottleneck) → behavioral / ownership (`companies.md` Tesla; `recruiting.md` intern OA-gated). Comp **$24–$42/hr** on aggregator copies of this req. No intern sys design.
- **Outside the resume:** Apply this wave (posted ~2026-10-07/08). Prep timed HackerRank Easy–Medium and an honest SQL/BI/site-choice answer. Referral: none in `network.md`. Confirm Jan–April 2027 onsite at Palo Alto or Austin and remaining enrolled (Winter 2027 semester off / co-op).
