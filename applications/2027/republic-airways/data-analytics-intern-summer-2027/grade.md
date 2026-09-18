# Data Analytics Intern - Summer 2027 at Republic Airways

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — pursuing bachelor's (no exclusive class-year window) vs Expected May 2028; GPA 3.66 vs 3.0; B.S. Computer Science and Economics vs CS/DS/Statistics or related; US citizen / no sponsorship
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN stakeholder delivery — ingest → transform → report analog, not ML-research and not generic SWE.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision; fleet-expansion proxy) and 15 hours/week saved is ops-analytics / scoring analog; SignalWeaver opens on a React/Postgres dashboard, then an evaluated regression.
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof this finance-reporting analytics seat treats as core wrangling work, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; the screen looks for query/aggregate/insight SQL and does not find it

### Misreads

- A keyword-first pass for Power BI / Tableau / Excel / R can bucket this as "no reporting stack" even though a React/Postgres dashboard and PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision; 15 hours/week saved) as the ingest → insight / ops-reporting loop this seat tests; SignalWeaver dashboard if they ask for viz; Vylet 30x pipeline if they ask for automation
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; Power BI / Tableau / Excel / R are preferred familiarity, not in inventory — walk the React/Postgres dashboard instead of inventing BI tools *(out of rails: no Power BI/Tableau/Excel/R in pool or swap sets)*; this is Data Analytics Intern sitting with finance, not SWE and not ML research
- **Depth prep:** walk a non-builder finance stakeholder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-validation analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No confirmed LeetCode OA — expect Easy SQL/Python fluency, a project deep-dive, and STAR. Do not prep cabin-crew HireVue.

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder delivery, which is this req's screen
- **Overall hire odds:** Medium — Republic is C-tier with a resume bottleneck (~20–30%) and no published OA, so this page should clear the binding intern gate; the remaining cut is Carmel onsite relocate, defending Python/SQL fluency, and STAR with a non-builder finance audience
- **Funnel filters:** Workday **JR-007628** resume screen (posted 2026-09-18) → recruiter/HM (Carmel onsite, GPA 3.0, no sponsorship) → unpublished intern loop (peer of Avis DA / Hy-Vee DA / DICK'S DA&E: Easy SQL/Python + STAR; do not copy cabin-crew HireVue). No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this first wave. Honest US citizen / no sponsorship and Carmel relocate (relocation assistance if applicable). Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6)
