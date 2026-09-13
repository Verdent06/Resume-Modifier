# Data Analyst Intern (Summer 2027) at Lyft

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside the required December 2027–June 2028 window; B.S. Computer Science and Economics; Summer 2027 NYC hybrid is feasible; US citizen
- **Track:** ai-ml + urban mobility / bikeshare ops analytics for city partners
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular filings → Pandas ETL → PAC ranking shipped to a research stakeholder. That is this Urban Solutions DA intern, not a SWE intern and not ML-research.
- Lyndbrook Review Velocity (fleet expansion / operational scale, 800 → 280 at 35% precision) plus a React dashboard keep the ops-KPI / city-partner analog in the first half.
- Binding ding: SQL is required and appears only as an unquantified asyncpg freshness DAL — not analysis SQL.

### Demerits

- **minor** · `Vylet` · SQL through-use is unquantified DAL plumbing — SQL is a JD-required floor; the only through-use is injection-safe timestamp validation that triggers re-scrapes, with no sized freshness win and no JOIN/aggregate that produced a ranking or KPI

### Misreads

- A keyword-first pass for Tableau / Looker / Mode can no-pile a page that actually has a React dashboard, PAC rankings, and a fleet-scale score.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a SQL-required DA screen is looking for, because it never sizes the freshness win or shows a query that produced a KPI.

### Interview angles

- **Lead with:** MDC (Excel-export ETL → PAC funding rankings for MCFN researchers; ~800 hours / 400 PACs) as the city-partner reporting analog; Lyndbrook Review Velocity (fleet expansion / operational scale, 35% precision) as the ops-KPI analog; Vylet SQL freshness + 79→89% name-collision catch as data-quality / process-to-reduce-error; SignalWeaver React dashboard as the dashboard analog
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; swapping the DAL drops SQL-through-use)*. No Tableau, Looker, Mode, Snowflake, Databricks, Copilot, or Fusion — ramp on Lyft's stack; do not invent them. This is Urban Solutions DA, not a SWE intern and not ML-research. No bikeshare internship — analog is campaign-finance / search-fund operational scoring, not Citi Bike production systems
- **Depth prep:** Unpublished DA technical — treat SQL (joins, window functions, KPI diagnosis) as the bar; do **not** assume the `companies.md` CodeSignal SWE OA. Walk one ingest → KPI path (MDC) and one quality/anomaly path (Vylet). STAR for presenting a finding to Ops or a city partner (`recruiting.md` §6 behavioral is a filter). Confirm NYC hybrid Mon/Wed/Thu and Spring/Summer 2028 grad window on the form

## Likelihood

- **Resume screen:** High — eligibility is clean and the top half is ingest → ranking/shortlist → stakeholder delivery with SQL on the page
- **Overall hire odds:** Medium — B-tier Urban Solutions intern; knockouts clear; unpublished SQL/metrics technical (not confirmed CodeSignal) and NYC hybrid relocate still eliminate
- **Funnel filters:** Greenhouse **8802198002** / req **111177** + human resume screen; OA unpublished for this DA intern (`companies.md` CodeSignal is adjacent SWE only). Grad window Dec 2027–June 2028. Hybrid 3 days/week NYC. Bottleneck after knockouts: resume, then SQL/technical **[directional]**
- **Outside the resume:** Apply 2026-09-13 (posted 2026-09-11). No Lyft contact in `network.md`. Do not pick employee referral. Prep SQL + a KPI-diagnosis case. See `written-answers.md`
