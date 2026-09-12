# Enterprise Analytics Intern at The Toro Company

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Economics is on the JD degree list; CS+Econ is related to Analytics; no exclusive junior/senior gate; Expected May 2028 vs May 17–August 6 2027 (returns Fall 2027); US citizen vs JD no-sponsor. Excel is a listed floor the page does not claim as a tool.
- **Track:** ai-ml + outdoor-equipment OEM enterprise insights (markets/customers/economic trends across Toro brand portfolio)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel-export → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN stakeholder delivery — ingest → insight/KPI → report analog, not SWE and not ML-research.
- Lyndbrook multi-source EPA+MassGIS+Maps merge plus Review Velocity (800 → 280, 35% precision; 15 hours/week saved) is the economic/industry-trend and multi-source synthesis analog; SignalWeaver opens on a React dashboard with macro breakdowns.
- Binding dings: the only SQL-through-use proof is an unquantified asyncpg freshness DAL, and Excel/Power BI/Tableau never appear as claimed tools.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL-through-use proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; an enterprise-insights screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `resume` · named Excel / Power BI / Tableau stack absent — JD lists Excel proficiency (formulas, pivot tables, charts) as a need-to-have and Power BI/Tableau as a plus; the page shows Pandas ETL, PAC rankings, and a React/Postgres dashboard analog plus "irregular Excel exports" as a data source, but never demonstrates Excel formulas/pivots/charts or names those BI tools

### Misreads

- A keyword-first pass for Excel / Power BI / Tableau can bucket this as "no reporting stack" even though a React dashboard and PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL insights screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision; 15 hours/week saved) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for viz; Vylet 30x scored pipeline if they ask for AI-enabled tools
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*. Excel/Power BI/Tableau are not in inventory — walk the React/Postgres dashboard and MDC ranking-report instead of inventing them *(out of rails: no Excel/Power BI/Tableau in pool or swap sets)*. This is Enterprise Insights Analyst intern, not Embedded Software & Telematics SWE, not IT, and not ML research.
- **Depth prep:** walk a non-builder / senior-leadership analog through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as multi-source freshness; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No published OA — expect an insights walk + STAR (`company.md`). Confirm Bloomington May 17–August 6 2027 start and no sponsorship on the form. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder delivery, which is this req's screen
- **Overall hire odds:** Medium — The Toro Company is C-tier with a resume bottleneck (~20–30%) and no published OA (`companies.md`), so this page should clear the binding intern gate; the loop still has to defend the Excel floor, Bloomington relocate May 17–August 6 2027, and walk an insights story in plain language
- **Funnel filters:** Workday **JR17104** (`ttc.wd1` / Toro_External_Careers) + hiring-team review → interview (official intern FAQ). No published intern OA. No intern sys design. Bottleneck: resume · ~20–30%. Visa: no sponsor (cleared). Must start May 17 and stay through August 6 2027.
- **Outside the resume:** Apply 2026-09-12 (posted 2026-09-11; first wave). No Toro contact assumed in `network.md`. Honest Excel gap for written answers — coach owns `written-answers.md`. Behavioral is a filter (`recruiting.md` §6).
