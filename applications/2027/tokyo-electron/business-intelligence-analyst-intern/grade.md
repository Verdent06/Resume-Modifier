# Business Intelligence Analyst Summer 2027 Intern at Tokyo Electron (TEL)

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs May 17–August 20 2027 (still enrolled; returns Fall 2027); UMich CS bachelor's vs listed majors; US citizen
- **Track:** ai-ml + semiconductor capital equipment / Sales and Service operations BI
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of messy ingest → PAC ranking → scored shortlist → dashboard. That is this Service/Sales Support BI intern, not a process co-op and not an ML intern.
- Binding dings: SQL is listed as a language but never used as analysis SQL, and Power BI / Excel / Power Pivot are named on the JD and absent on the page (React dashboard analog only).
- Eligibility and Austin RiverSouth onsite May 17–August 20 2027 knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a BI screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `resume` · named BI stack absent (Power BI / Excel / Power Pivot) — JD lists basic knowledge of data visualization tools (e.g., Power BI, Excel, Power Pivot); the page shows a React/Postgres dashboard analog and Python/Pandas ETL, but never names those BI tools

### Misreads

- A rushed BI recruiter may bucket SQL as a real analysis skill from the Languages line, then bounce when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- A screener filtering on Power BI / Excel may no-pile a page that is actually ingest → KPI → dashboard, because those product names are missing.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision; 15 hours/week saved) as the ingest → insight loop this seat tests; SignalWeaver dashboard if they ask for viz
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; Power BI / Excel / Power Pivot are not in inventory — walk the React/Postgres dashboard instead of inventing BI tools *(out of rails: no Power BI/Excel/Power Pivot in pool or swap sets)*; this is Sales/Service BI, not process engineering, not ATG simulation, and not ML research
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-validation / integrity analog; SignalWeaver FastAPI score product if they ask about "reports, applications, workflows." No confirmed LeetCode OA on this BI posting — expect Python/SQL fluency, a project deep-dive, and STAR. Lean training is provided; do not invent a Lean cert.

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder delivery, which is this req's screen
- **Overall hire odds:** Medium — Tokyo Electron is B-tier with a resume bottleneck (~8–12%) and no confirmed OA on this BI posting, so this page should clear the binding intern gate; the loop still has to defend Python/SQL fluency, the Power BI/Excel gap, and Austin onsite May 17–August 20 2027
- **Funnel filters:** Workday resume screen (posted 2026-09-07; first wave; no public endDate) → unpublished OA (not confirmed here) → recruiter → Easy practical + STAR. No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this first wave. No TEL contact in `network.md`. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6). See `written-answers.md`
