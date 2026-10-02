# Data Analyst Intern (Summer 2027) at SeatGeek

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — B.S. Computer Science and Economics, Expected May 2028 (JD: currently enrolled, graduate spring/summer 2028); NYC hybrid ≥3 days/week is feasible; US citizen, no sponsorship
- **Track:** ai-ml + live-events ticketing marketplace / fan+venue product analytics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular filings → Pandas ETL → PAC ranking shipped to a research stakeholder. That is this Analytics intern, not the new-grad SWE req and not ML-research.
- Lyndbrook Review Velocity (800 → 280 at 35% precision against a revenue filter) plus a React dashboard keep the KPI / stakeholder-narrative analog in the first half.
- Binding ding: SQL is required and appears only as an unquantified asyncpg freshness DAL — not analysis SQL.

### Demerits

- **minor** · `Vylet` · SQL through-use is unquantified DAL plumbing — SQL is a JD-required floor; the only through-use is injection-safe timestamp validation that triggers re-scrapes, with no sized freshness win and no JOIN/aggregate that produced a ranking or KPI

### Misreads

- A keyword-first pass for Looker / Mixpanel / Redshift / dbt can bucket this as "no reporting stack" even though a React dashboard, PAC rankings, and a business-tied score are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a SQL-required analytics screen is looking for, because it never sizes the freshness win or shows a query that produced a KPI.
- Vylet's PE/search-fund founder tagline can file as a generic agentic product if the reader never reaches the SQL DAL and 79→89% quality lines.
- Flask on MDC can file this as the Software Engineer - New Grad PDF if the reader skips the ETL / ranking / scoring spine.

### Interview angles

- **Lead with:** MDC (Excel-export ETL → PAC funding rankings for MCFN researchers; ~800 hours / 400 PACs) as the stakeholder KPI/report analog; Lyndbrook Review Velocity (35% precision against a business revenue filter) as the product-analytics scoring analog; Vylet SQL freshness + 79→89% name-collision catch as data-quality; SignalWeaver React dashboard + out-of-sample $R^{2}$ as the Looker/Mixpanel and A/B analogs
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; swapping the DAL drops SQL-through-use)*. No Looker, Mixpanel, Redshift, dbt, Snowflake, Databricks, Tableau, Copilot, or Fusion — ramp on SeatGeek's stack; do not invent them. This is Analytics intern, not Software Engineer - New Grad (8227548). No ticketing internship — analog is campaign-finance / search-fund operational scoring, not SeatGeek Deal Score
- **Depth prep:** Unpublished intern technical — treat SQL (joins, aggregations, window functions) and a KPI / A/B readout case as the bar (`company.md` FT DA analog; do **not** assume LeetCode). Walk one ingest → KPI path (MDC) and one quality/anomaly path (Vylet). STAR for presenting a finding to Product or Business (`recruiting.md` §6 behavioral is a filter). Confirm NYC ≥3 days/week, graduation **2028**, US citizen / no sponsorship on the form

## Likelihood

- **Resume screen:** High — eligibility is clean and the top half is ingest → ranking/shortlist → stakeholder delivery with SQL on the page
- **Overall hire odds:** Medium — B-tier Analytics intern (~8–12% analog); knockouts clear; unpublished SQL/take-home and NYC 50% relocate still eliminate; named Looker/Mixpanel are a plus this page does not claim
- **Funnel filters:** Greenhouse **8247554** / internal **2975710** + human resume screen; OA unpublished (`companies.md`). Grad spring/summer 2028. NYC hybrid ≥3 days/week. Bottleneck after knockouts: resume, then SQL/take-home **[directional]**
- **Outside the resume:** Apply 2026-10-02 (posted 2026-10-01). No SeatGeek contact in `network.md`. Do not pick employee referral. Skip optional cover letter and EEO for volume unless you want the letter in `written-answers.md`. Prep SQL + a KPI-diagnosis case
