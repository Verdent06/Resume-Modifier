# Summer 2027 Internship Program – Data Analyst Intern at Dow Jones

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs graduating Dec 2027–July 2029; 4-year UMich CS + Economics (quantitative); ≥2 years completed (junior); US citizen / no sponsorship; NYC June 7–August 13 2027
- **Track:** ai-ml + news/business-information Data Management
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.7, Expected May 2028, and a lead spine of messy ingest → PAC ranking → scored shortlist → dashboard. That is this Data Management intern, not a reporter intern and not an SWE intern.
- Binding dings: SQL is listed as a language but never used as analysis SQL, and Tableau / Adobe Analytics / Google Analytics / advanced Excel are named on the JD and absent as claimed tools (React dashboard + Excel-as-source analog only).
- Eligibility and NYC in-office June 7–August 13 2027 knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a Data Analyst screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `resume` · named BI / advanced-Excel stack absent — JD requires strong Microsoft Excel (advanced formulas) and names Adobe, Tableau, or Google Analytics for dashboards; the page shows a React/Postgres dashboard analog and Python/Pandas ETL on irregular Excel exports, but never names those BI tools or Excel formulas

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- A screener filtering on Tableau / advanced Excel may no-pile a page that is actually ingest → KPI → dashboard, because those product names are missing.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision; 15 hours/week saved) as the ingest → report/insight loop this seat tests; SignalWeaver dashboard if they ask for viz / user-facing scores
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Tableau / Adobe / GA / advanced Excel are not in inventory — walk the React/Postgres dashboard and the Excel-exports → Pandas path instead of inventing BI tools *(out of rails: no Tableau/Adobe/GA/Excel-formulas in pool or swap sets)*; this is Data Management intern, not a WSJ reporter intern and not ML research
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-quality analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No confirmed LeetCode OA — expect Python/SQL fluency, a project deep-dive, and STAR on a panel

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.7, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder delivery, which is this req's screen
- **Overall hire odds:** Medium — Dow Jones is C-tier with a resume then panel bottleneck (~15–25%) and no confirmed OA on this DA posting, so this page should clear the binding intern gate; the panel still has to defend Python/SQL fluency, the Excel/Tableau gap, and NYC full-time in-office June 7–August 13 2027
- **Funnel filters:** Workday resume screen (rolling; posted 2026-10-07; apply by 2026-11-13) → unpublished intern OA → recruiter → group panel and/or 1:1 **[directional, Extern]**. No intern sys design. Bottleneck: resume + NYC dates (`companies.md`)
- **Outside the resume:** Apply in this first rolling wave. No Dow Jones contact in `network.md`. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6). See `written-answers.md`
