# Catastrophe Modeling & Data Analytics Intern (Spring 2027) at Great American Insurance Company

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — currently pursuing CS + Economics with stats coursework (related field); Expected May 2028 vs Spring 2027 (returns to school); US citizen / no sponsorship; no printed GPA or class-year window
- **Track:** ai-ml + P&C reinsurance / catastrophe-risk modeling (geospatial)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead window is on-axis for this Reinsurance CAT intern: EPA ECHO + MassGIS entity database, Google Maps location join, Review Velocity scoring (800 → 280 at 35% precision) — geospatial / high-risk-region analog without inventing RMS/AIR.
- MDC is Python data engineering: irregular Excel → Requests+Pandas ETL → PAC ranking shipped to a research stakeholder (~800 hours / 400 PACs); SignalWeaver opens on a React/Postgres dashboard, then an evaluated regression.
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof this data-engineering intern seat treats as core wrangling work, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; the screen looks for query/aggregate/insight SQL and does not find it

### Misreads

- A keyword-first pass for Tableau / Power BI / Excel / RMS can bucket this as "no CAT stack" even though a React/Postgres dashboard, MassGIS/Maps location scoring, and Excel-as-the-problem-replaced are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL CAT-analytics screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** Lyndbrook (EPA ECHO + MassGIS → PWSID entity DB; Google Maps cross-ref; Review Velocity 800 → 280 at 35% precision) as the geospatial / region-scoring analog; MDC (irregular filings → Pandas ETL → PAC ranking; ~800 hours / 400 PACs) as Python data engineering and reference-table cleanup analog; Vylet 30x pipeline if they ask for process automation; SignalWeaver dashboard if they ask for viz
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; Tableau / Power BI / Excel-as-skill are JD learn/look-for, not in inventory — walk the React/Postgres dashboard and Excel-replaced-by-ETL instead of inventing BI tools *(out of rails: no Tableau/Power BI/Excel/RMS/AIR in pool or swap sets)*; modeling software is taught — do not claim RMS/AIR/Touchstone; this is CAT data analytics, not SWE and not ML research
- **Depth prep:** walk a non-builder modeler through one finding (Lyndbrook shortlist or MDC ranking); Vylet stale-timestamp re-scrape as data-validation analog; SignalWeaver 3.39% R² as "the score is not just fitting noise." No confirmed LeetCode OA — expect Easy SQL/Python fluency, a project deep-dive, and STAR. Cincinnati 4-day hybrid (Tue–Thu core) is not optional.

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is location-entity scoring + Python ETL + a dashboard analog, which is this req's screen
- **Overall hire odds:** Medium — GAIG is C-tier with a resume bottleneck (~15–25%) and no published OA, so this page should clear the binding intern gate; the remaining cut is Cincinnati relocate, defending Python/SQL fluency, and STAR with a Reinsurance modeling audience
- **Funnel filters:** Workday **R9576** (`gaig.wd1`) resume screen (posted 2026-09-17) → recruiter (no sponsorship, Cincinnati 4-day hybrid, Spring 2027) → unpublished intern loop (peer of Nationwide / Northwestern Mutual ID&A / Republic DA: Easy SQL/Python + STAR). No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this first wave. Honest US citizen / no sponsorship and Cincinnati relocate. Prep STAR (Lyndbrook/MDC) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6)
