# 2027 Undergraduate Summer Internship – Enterprise Data & Analytics at Dallas Fort Worth International Airport

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — dual CS+Economics (both on the JD major list); Expected May 2028 vs Summer 2027 is an active bachelor’s student; 18+; GPA 3.66 vs desired 3.0; US citizen vs no-sponsor line
- **Track:** ai-ml + airport enterprise analytics CoE
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs) and PAC rankings shipped to MCFN on a Flask REST API / AWS EC2 — ingest → rank → stakeholder delivery, not ML-research and not a SWE intern.
- Lyndbrook Review Velocity (fleet expansion / operational scale; 800 → 280, 35% precision) is the ops-adjacent scoring analog in the lead window; SignalWeaver is a React/Postgres dashboard plus an evaluated composite score.
- Binding ding is small: the only on-page SQL proof (Vylet asyncpg freshness) never sizes the win. GPA 3.66 and Expected May 2028 clear this posting’s active-student + CS/Econ knockouts.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; an applied-analytics screen looks for query/aggregate/insight SQL and does not find it.

### Misreads

- A keyword-first pass for Tableau / Power BI / Snowflake can bucket this as "wrong stack" even though a React/TypeScript dashboard and ranked PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- A rushed screener who sees Flask REST / founder MRR might bucket this as SWE and miss the enterprise-analytics analog in MDC/Lyndbrook.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC rankings shipped to MCFN on EC2; ~800 hours / 400 PACs) and Lyndbrook (Review Velocity fleet-expansion shortlist at 35% precision; EPA/MassGIS entity database) as the ingest → score → insight loop this CoE seat tests; SignalWeaver React/Postgres dashboard if they ask for viz; Vylet 79%→89% qualification / SQL freshness if they ask for data quality
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*. No Tableau, Power BI, Snowflake, Databricks, SPSS, Excel-as-BI, Copilot, Fusion — walk React/Postgres and Pandas instead of inventing them *(out of rails: those tools are not in inventory or swap sets)*. This is Workday **JR102162** Analytics CoE intern, not CX Insights **JR102114**, not Geospatial Data **JR102119**, not SWE.
- **Depth prep:** Unpublished intern loop (peer of CHS DA / Verizon BI / Toro EA: Easy SQL/Python + dashboard/insight walk, not LC OA). Walk a non-builder ops stakeholder through one finding (MDC ranking or Lyndbrook shortlist). Vylet stale-timestamp re-scrape as validation analog. SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. DFW Airport onsite is a yes (relocate from Northville for the term). STAR is the culture filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — eligible Junior with GPA 3.66, Pandas ETL + PAC rankings in the lead, fleet/ops scoring analog next, dashboard + SQL on the page; one unquantified SQL line does not sink a C-tier CoE intern screen
- **Overall hire odds:** Medium — resume-first C-tier intern (~20–30%); unpublished Easy SQL/Python + STAR loop, not an OA gauntlet. DFW Airport onsite relocate is the operational filter after the PDF
- **Funnel filters:** Workday `dfwairport.wd5` / `External` **JR102162** + human resume screen → recruiter (active bachelor’s, CS/Econ-or-related, 18+, no sponsor, Texas onsite) → unpublished intern loop (STAR; Easy SQL/Python + insight walk analog). No intern sys design. Bottleneck: resume · ~20–30% (`companies.md`). Comp unlisted.
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-30). No DFW contact in `network.md` — do not pick Employee Referral. Honest US citizen / no sponsorship and DFW relocate yes. Form email **`verdent06@gmail.com`**. Do not invent Tableau/Power BI/Snowflake on the form. Packet only from this agent — see `written-answers.md`
