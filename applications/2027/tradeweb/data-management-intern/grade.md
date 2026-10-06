# Summer 2027 Data Management Internship at Tradeweb

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — currently pursuing a bachelor's in Computer Science and Economics (both named on the JD); Expected May 2028 vs Summer 2027; posting open (`ExternalPostedEndDate` null); no GPA, class-year, visa, or clearance line on 301946
- **Track:** ai-ml + electronic-trading / securities-reference-data / security-master
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is Michigan Data Consulting: irregular Excel/portal filings → Requests + Pandas ETL (~800 hours / 400 PACs) → PAC ranking → production Flask REST on AWS EC2. That is ingest → normalize/validate → served table for a non-builder — the security-master analog this req tests.
- Vylet is in the lead window: injection-safe SQL timestamp freshness, a name-collision RCA that lifted qualification 79% → 89%, and a Dockerized LangGraph pipeline (30x). Lyndbrook adds multi-source EPA/MassGIS entity unification plus Review Velocity (800 → 280, 35% precision). SignalWeaver is a React/Postgres dashboard over 90 tickers plus an out-of-sample regression.
- Binding ding is minor: SQL is on Skills and in freshness/persist bullets, not a query/aggregate/join that produced a ranking.

### Demerits

- **minor** · `resume` · SQL never used as an analysis query — JD prefers SQL/Python for validation and discrepancy work. Skills lists SQL; Vylet shows injection-safe timestamp validation and SignalWeaver persists scores to Postgres. A reference-data screen looks for query/aggregate/join SQL that produced a ranking or a reconciled table and does not find it — PAC rankings and Review Velocity read as Python/Pandas *(out of rails: pool has no verbatim JOIN/window/GROUP BY analytics bullet; swap sets cannot bridge SQL freshness to analysis SQL)*

### Misreads

- A skim that stops on Vylet's PE/search-fund founder tagline can file this as startup SaaS and miss the SQL freshness layer and 79% → 89% collision catch.
- SignalWeaver's financial-research dashboard can read as a Quantitative intern sibling; this packet is Data Management 301946, not quant research.

### Interview angles

- **Lead with:** MDC Requests + Pandas ETL → PAC ranking → Flask on EC2 as the ingest → validate → served-table analog; Vylet SQL timestamp freshness + 79% → 89% name-collision RCA as discrepancy investigation; Lyndbrook PWSID entity DB + Review Velocity (800 → 280, 35% precision) as multi-source reconciliation; SignalWeaver dashboard if they ask for a readout a non-builder used
- **Defend:** SQL on the page is asyncpg timestamp validation / re-scrape, not a warehouse JOIN — walk freshness and what you would query next *(out of rails: no analysis-SQL bullet in the pool)*. Excel is preferred on the JD and is **not** claimed on Skills; Pandas-on-irregular-Excel-exports is the honest analog. Do not claim Bloomberg, vendor security-master tools, Snowflake, Databricks, Tableau, Copilot, Fusion, or a Tradeweb internship. This is **301946** Data Management, not Data Product Manager **301932**, not Data Platform **301904**, not Quant intern
- **Depth prep:** Walk one ingest → quality-catch → served artifact (MDC or Lyndbrook) and one discrepancy RCA (Vylet 79% → 89%). Drill messy-data SQL (joins, windows) if a take-home appears — intern OA unpublished (`company.md`). STAR for detail and investigating a break. Behavioral is a filter (`recruiting.md` §6). Confirm NYC onsite Summer 2027, $22–$25/hr, Expected May 2028, US citizen / no sponsorship

## Likelihood

- **Resume screen:** High — eligible Expected May 2028, GPA 3.7, dual CS+Economics on the printed major list, and an ingest → normalize → quality-catch → served API/dashboard spine on a resume-first C-tier intern req
- **Overall hire odds:** Medium — bottleneck is the resume (~15–25% directional, `companies.md`); residual cut is NYC onsite for Summer 2027, a data-quality / SQL-Python project walk, and STAR. Intern OA unpublished
- **Funnel filters:** Oracle CE (`ecnf.fa.us2.oraclecloud.com` / site CX / job **301946**) resume (bottleneck) → recruiter phone → team-lead → business-head **[directional, sibling intern JDs; not printed on 301946]** · intern OA unpublished — do not invent HackerRank/CodeSignal · no intern sys design · ~15–25%
- **Outside the resume:** Apply this first-wave window (posted 2026-10-06; no printed close). Confirm NYC relocate. Walk SQL as freshness, not a fake JOIN. Form email `verdent06@gmail.com`. No Tradeweb contact in `network.md`
