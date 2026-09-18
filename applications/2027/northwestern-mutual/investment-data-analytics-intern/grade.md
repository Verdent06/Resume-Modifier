# Investment Data & Analytics Intern, Summer 2027 at Northwestern Mutual

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** ambiguous — Expected May 2028 vs June–August 2027 intern (still enrolled; Junior; JD prints no graduation window). Printed major is business/finance/accounting vs B.S. Computer Science and Economics (finance-adjacent; not Ross; not investment-program enrollment). US citizen; sponsorship not available — clears. User instructed to apply.
- **Track:** ai-ml + investment-management reporting / cross-asset analytics for a mutual insurer's Managed Investment Business
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular Excel-export filings → Pandas ETL → PAC ranking shipped to research stakeholders. That is this ID&A reporting intern, not SWE, not ML-research, not CFR, not PDE/Quant/Credit.
- Lyndbrook Review Velocity (800 → 280 at 35% precision) plus a React dashboard keep the investment-adjacent KPI / dashboard analog in the first half.
- Binding ding: SQL is desirable and appears only as an unquantified asyncpg freshness DAL — not analysis SQL. Printed major is not business/finance/accounting.

### Demerits

- **minor** · `Vylet` · SQL through-use is unquantified DAL plumbing — SQL is a JD-desirable ATS keyword; the only through-use is injection-safe timestamp validation that triggers re-scrapes, with no sized freshness win and no JOIN/aggregate that produced a ranking or KPI
- **minor** · `Michigan Data Consulting (MDC)` · delivery closer metric-free — The Flask/EC2 MCFN closer is the stakeholder-facing reporting analog, but it has no throughput, adoption, or report-usage number, so the insight delivered to that customer is unsized

### Misreads

- A keyword-first pass for Power BI / Excel models / Aladdin / Bloomberg can no-pile a page that actually has a React dashboard, PAC rankings, and a search-fund score.
- The SQL/DAL line can read as database plumbing rather than the language proof a reporting intern screen is looking for, because it never sizes the freshness win or shows a query that produced a KPI.
- CS + Economics can read as the wrong major against a business/finance/accounting line even though econ is finance-adjacent.

### Interview angles

- **Lead with:** MDC (Excel-export ETL → PAC funding rankings for MCFN researchers; ~800 hours / 400 PACs) as the trusted-reporting analog; Lyndbrook Review Velocity (800 → 280 at 35% precision) as the cross-asset/KPI analog; Vylet SQL freshness + 30x manual-process automation; SignalWeaver React dashboard as the Power BI analog (research assistant, not investment advice)
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; swapping the DAL drops SQL-through-use)*. MCFN closer is ownership, not an insight metric — pair it verbally with the 800-hour ETL *(out of rails: MDC delivery/closer pool bullets are both metric-free)*. No Power BI, Excel-as-claimed-tool, Tableau, Snowflake, Databricks, Copilot, Fusion, Aladdin, Bloomberg, or dbt — ramp on NM's stack; do not invent them. Not enrolled in an investment program. This is ID&A reporting, not SWE, not ML-research, not CFR, not PDE/Quant/Credit. Major is CS + Economics, not Ross finance/accounting.
- **Depth prep:** No intern OA (`companies.md`). Walk one ingest → trusted figure path (MDC) and one quality/freshness path (Vylet). STAR for explaining a report to an investment-business end user (`recruiting.md` §6 behavioral is a filter). Confirm Milwaukee onsite June–August 2027 / local-for-summer and no-sponsorship on the Workday form.

## Likelihood

- **Resume screen:** High — top half is Excel-export ETL → PAC ranking plus Review Velocity scoring for a search-fund principal; SQL appears in a bullet; React dashboard is the Power BI analog
- **Overall hire odds:** Medium — C-tier ~15–25% with a resume bottleneck and no OA, so this page is the main filter and the work is on-axis for ID&A reporting. Remaining cut is the printed business/finance/accounting major vs CS + Economics, Milwaukee onsite/local-for-summer, and a short Emerging Talent + team screen — not a coding gauntlet
- **Funnel filters:** Workday **JR-46050** resume (`includeResumeParsing: true`) → Emerging Talent screening conversation (can redirect to another req) → team interviews. Intern OA unpublished. No intern sys design. Bottleneck: resume. ~15–25% **[directional, peer of Nationwide / Principal / National Life]**. No sponsorship. Closes **2026-10-01**.
- **Outside the resume:** Apply before 2026-10-01 (posted 2026-09-17). Confirm Milwaukee local-for-summer. Prep STAR on walking a non-builder through a trusted figure. Do not claim Power BI, Excel modeling, Aladdin, or Bloomberg.
