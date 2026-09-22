# Decision Science Undergraduate Intern, Spring 2027 at The Walt Disney Company

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs Jan–Jun 2027 maps to junior year; B.S. CS and Economics vs listed majors; 18+; US citizen / unrestricted work auth; enrolled
- **Track:** ai-ml + disney-ddsi / yield-revenue-forecasting-pricing-optimization
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of messy ingest → PAC ranking → scored shortlist → regression/dashboard. That is this DDSI undergrad intern, not Parks labor-web SWE and not Streaming SDE.
- Binding dings: SQL is listed as a language but never used as analysis SQL, and the only SQL-through-use line is an unquantified DAL freshness check.
- Eligibility and Lake Buena Vista onsite / junior-or-senior knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a Decision Science screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL-through-use proof, but it closes on architecture with no sized impact *(out of rails: only SQL pool bullet has no metric; adding a metric Vylet bullet overflowed to 2 pages)*

### Misreads

- A rushed DS recruiter may bucket SQL as a real analysis skill from the Languages line, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- A screener filtering on Tableau / PowerBI / R may no-pile a page that is actually ingest → score → dashboard, because those product names are missing (JD familiarity is an or-list; React dashboard is the viz analog).

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision; 15 hours/week saved) as the ingest → insight loop this seat tests; SignalWeaver 3.39% R² + React dashboard if they ask for modeling or viz
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Tableau / PowerBI / R / SAS / CPLEX / Gurobi are not in inventory — walk the React/Postgres dashboard instead of inventing BI or solvers *(out of rails: none of those in pool or swap sets)*; this is DDSI 10159998, not Parks PI, not Labor Systems $31/hr, not Streaming SWE
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-validation analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No confirmed LeetCode OA on this DDSI posting — expect Python/SQL/pandas fluency, a stats/case analog **[directional]**, and STAR. Confirm Lake Buena Vista Jan–Jun 2027, reliable transportation, unrestricted work auth

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → regression/dashboard, which is this req's screen
- **Overall hire odds:** Medium — Disney DDSI is B-tier with a resume then recruiter bottleneck (~5–10%) and no confirmed OA on this posting, so this page should clear the binding intern gate; the loop still has to defend Python/SQL fluency, the BI/R gap, and Orlando onsite with own transport
- **Funnel filters:** Workday `disneycareerdc` resume (posted 2026-09-21; close **2026-09-30**) → recruiter (auth, junior/senior, enrolled prior semester, 18+, unrestricted work auth, one-year Disney intern cap, Florida logistics) → unpublished intern OA (do not assume HackerRank) → project walk + STAR. No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this close window. No Disney contact in `network.md`. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6). See `written-answers.md`
