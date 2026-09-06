# Summer 2027 Global Technical Learning Center Data Analyst Intern- Bachelor's/Master's (Albany, NY) at Applied Materials

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027 (students FAQ analog: graduate after December 2027); UMich CS bachelor's vs listed majors; US citizen
- **Track:** ai-ml + semiconductor capital equipment / GTLC training-ops analytics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of messy ingest → PAC ranking → scored shortlist → dashboard. That is this GTLC Data Analyst intern, not a process co-op and not an ML intern.
- Binding dings: SQL is listed as a language but never used as analysis SQL, and Tableau / Power BI / Excel are named on the JD and absent on the page (React dashboard analog only).
- Eligibility and Albany onsite / travel-10% knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a Data Analyst screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `resume` · named BI stack absent (Tableau / Power BI / Excel) — JD Key Skills Required lists SQL, Excel, Python, PowerBI, Tableau, Powerpoint; the page shows a React/Postgres dashboard analog and Python/Pandas ETL, but never names those BI tools

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- A screener filtering on Power BI / Tableau may no-pile a page that is actually ingest → KPI → dashboard, because those product names are missing.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision; 15 hours/week saved) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for viz
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Tableau / Power BI / Excel are not in inventory — walk the React/Postgres dashboard instead of inventing BI tools *(out of rails: no Tableau/Power BI/Excel in pool or swap sets)*; Copilot is a plus, not claimed; this is GTLC DA, not process engineering and not ML research
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-quality / "source is true" analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No confirmed LeetCode OA on this DA posting — expect Python/SQL fluency, a project deep-dive, and STAR on a panel

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder delivery, which is this req's screen
- **Overall hire odds:** Medium — Applied Materials is B-tier with a resume then panel bottleneck (~8–12%) and no confirmed OA on this DA posting, so this page should clear the binding intern gate; the panel still has to defend Python/SQL fluency, the BI-tool gap, and Albany onsite with Relocation Eligible: No
- **Funnel filters:** Workday resume screen (rolling; posted 2026-09-04; apply by 2026-11-30; may close early) → unpublished OA on some other intern tracks (not confirmed here) → recruiter → behavioral + technical, often a panel (students FAQ). Travel 10%. No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this first rolling wave. No Applied Materials contact in `network.md`. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6). See `written-answers.md`
