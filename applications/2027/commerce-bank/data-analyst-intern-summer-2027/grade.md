# Intern - Data Analyst (Summer 2027) at Commerce Bank

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027 11-week term; JD prefers sophomore/junior; CS vs IS/CS/DA; US citizen / no sponsorship now or later
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of messy ingest → PAC ranking → scored shortlist → SQL freshness DAL → React dashboard. That is this EABI Data Analyst intern, not IT intern 38395 and not Data Science intern 38483.
- Binding ding: SQL is strongly preferred and listed as a language, but the only through-use is timestamp validation on a DAL, not a query that produced a ranking.
- Eligibility and hybrid Kansas City / no-sponsorship knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis query — The JD lead function is writing efficient data queries for products and customer analysis, and SQL is strongly preferred. Skills lists SQL, and Vylet leads with injection-safe timestamp validation on a DAL plus Postgres persistence (SignalWeaver). A Data Management screen looks for query/aggregate/insight SQL and does not find it.

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line and the leading Vylet DAL, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for viz; Vylet 30x scored pipeline if they ask for recurring reporting
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Power BI / Tableau / Excel-as-claimed-tool are not in inventory — walk the React/Postgres dashboard instead of inventing BI tools; this is Data Analyst intern 38484, not Data Science 38483 and not IT 38395
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-quality analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No confirmed OA on this DA posting — expect Python/SQL fluency, a project deep-dive, and STAR. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics, sophomore/junior window) and the top half is ingest → ranking/shortlist → dashboard
- **Overall hire odds:** Medium — Commerce Bank is C-tier with a resume then unpublished recruiter/HM bottleneck (~15–25%) and no confirmed OA, so this page should clear the binding intern gate; the loop still has to defend Python/SQL fluency, the BI-tool gap, and hybrid Kansas City for 11 weeks
- **Funnel filters:** Workday **38484** resume screen (rolling; posted 2026-09-21) → unpublished intern loop · intern OA unpublished · no intern sys design · Bottleneck: resume · ~15–25% **[directional, peer of CoBank / Fifth Third / Live Oak / Erie Data Intern]** (`companies.md`)
- **Outside the resume:** Apply in this first rolling wave. No Commerce Bank contact in `network.md`. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer. See `written-answers.md`
