# Data Analytics Intern (Spring 2027, Full-time Hours) at Transamerica

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 > internship end late April 2027 (still enrolled); Junior; B.S. CS + Economics is an IT-type degree; US citizen (no sponsorship needed)
- **Track:** ai-ml + finance-transformation / insurance-retirement enterprise data (Aegon US)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular Excel-export filings → Pandas ETL → PAC ranking shipped to a research stakeholder. That is this Finance Transformation / Data Analytics intern, not SWE, not ML-research, not a sibling reporting intern.
- Lyndbrook Review Velocity (800 → 280 at 35% precision) plus a React dashboard keep finance-adjacent scoring and visualization in the first half. Vylet carries the required SQL through-use plus a 30x manual-process automation.
- Binding ding: SQL is required and appears only as an unquantified asyncpg freshness DAL — not analysis SQL that produced a ranking or KPI.

### Demerits

- **minor** · `Vylet` · SQL through-use is unquantified DAL plumbing — SQL is a JD-required floor; the only through-use is injection-safe timestamp validation that triggers re-scrapes, with no sized freshness win and no JOIN/aggregate that produced a ranking or KPI
- **minor** · `Michigan Data Consulting (MDC)` · delivery closer metric-free — The Flask/EC2 MCFN closer is the stakeholder-facing reporting analog, but it has no throughput, adoption, or report-usage number, so the insight delivered to that customer is unsized

### Misreads

- A keyword-first pass for Alteryx / Excel-as-tool / Tableau / Power BI can no-pile a page that actually has Pandas ETL, PAC rankings, a search-fund score, and a React dashboard.
- The SQL/DAL line can read as database plumbing rather than the language proof a data-analytics intern screen is looking for, because it never sizes the freshness win or shows a query that produced a KPI.
- Vylet’s PE/search-fund founder tagline can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape line.

### Interview angles

- **Lead with:** MDC (Excel-export ETL → PAC funding rankings for MCFN researchers; ~800 hours / 400 PACs) as the finance-data / systems-mapping analog; Lyndbrook Review Velocity (800 → 280, 35% precision) as the scored-insight analog; Vylet SQL freshness + 30x manual-process automation; SignalWeaver React dashboard + held-out regression as the visualization / predictive-modeling analog
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; swapping the DAL drops SQL-through-use)*. MCFN closer is ownership, not an insight metric — pair it verbally with the 800-hour ETL *(out of rails: MDC delivery/closer pool bullets are both metric-free)*. No Alteryx, Excel-as-claimed-tool, Tableau, Power BI, Snowflake, Databricks, Copilot, or Fusion — ramp on Transamerica’s stack; do not invent them. This is Finance Transformation / Data Analytics, not SWE, not ML-research, not Investment/Financial Reporting.
- **Depth prep:** Unpublished intern OA (`company.md`; do not assume HackerRank). Walk one ingest → ranked insight path (MDC) and one quality/freshness path (Vylet). STAR for explaining a data flow to a finance stakeholder (`recruiting.md` §6 behavioral is a filter). Confirm Cedar Rapids Tue–Thu hybrid, 14-week late-Jan–late-Apr 2027 full-time hours, and no-sponsorship on the Workday form.

## Likelihood

- **Resume screen:** High — top half is Excel-export ETL → PAC ranking plus Review Velocity scoring for a search-fund principal; SQL appears in a bullet; React dashboard is the visualization analog
- **Overall hire odds:** Medium — C-tier ~15–25% with a resume bottleneck and no published OA, so this page is the main filter and the work is on-axis for finance-transformation analytics. Remaining cut is Cedar Rapids 14-week full-time hybrid logistics and a short intern-program HR + possible HM screen
- **Funnel filters:** Workday **R20062776** resume → intern-program HR behavioral (~20–30 min) + resume tech walk **[Glassdoor intern, directional]** → possible HM Zoom. Intern OA unpublished. No intern sys design. Bottleneck: resume. ~15–25% **[directional, peer of Nationwide / Northwestern Mutual ID&A / GAIG CAT DA intern]**. No sponsorship. Posted **2026-09-18**.
- **Outside the resume:** Apply in this first-wave window. Confirm Cedar Rapids hybrid Tue–Thu, 14-week spring full-time (semester off), and legal US work auth without sponsorship. Prep STAR on walking a finance stakeholder through one ingest → insight path. Do not claim Alteryx, Excel modeling, Tableau, or Power BI.
