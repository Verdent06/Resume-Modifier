# 2027 Summer Internship - Data Science & Analytics at The Home Depot

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 vs intern term May 17 – July 30 2027 (rising senior; returns Fall 2027); college-student program with no class-year gate; GPA 3.66 ≥ 3.0 preferred
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular Excel ETL → PAC ranking shipped to a nonprofit, then a scored 35% precision shortlist. That is this undergrad Data Science & Analytics intern, not the PhD/Master's DS intern and not SWE.
- Binding ding: SQL is listed as a language, but the only through-use is a DAL freshness check and a Postgres persist — not JOIN/aggregate insight SQL.
- Eligibility and Atlanta 5-day onsite / college-student knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a Data Science & Analytics intern screen looks for query/aggregate/insight SQL and does not find it

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line, then bounce in the hiring-manager round when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → insight → stakeholder loop this seat tests; SignalWeaver dashboard + out-of-sample score if they ask for viz or predictive-modeling analog
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say that plainly; Python/Pandas is the analysis language *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; this is the undergrad/applied DS intern, not the PhD research intern; no Tableau, Snowflake, Databricks, Copilot, Fusion, BigQuery, or Sentry
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist) as the senior-leader report-out analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice; STAR against Action Oriented / Collaboration / Communication / Drives Results — no OA on this req

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder delivery, which is this req's screen
- **Overall hire odds:** Medium — Home Depot is C-tier with a resume bottleneck and no OA on this DS intern req (~15–25%), so this page should clear the binding intern gate; the live round still has to defend Python/SQL fluency and present findings to non-builders, and Atlanta is 5 days onsite
- **Funnel filters:** Workday CareerDepot resume screen (rolling; posted ~Aug 31 / Sep 1 2026) → recruiter phone → hiring-manager behavioral + SQL/Python/project. No OA on this DS intern req (`companies.md`). Bottleneck: resume. Housing assistance for eligible interns.
- **Outside the resume:** Apply in this first rolling wave. Prep STAR against the Great Intern competencies — behavioral is a filter (`recruiting.md` §6). Be ready to walk one messy-data finding as if to senior leaders.
