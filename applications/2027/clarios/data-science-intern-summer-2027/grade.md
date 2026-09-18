# Data Science Intern (Summer 2027) at Clarios

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — currently enrolled full-time US undergrad vs Expected May 2028 (returns after Summer 2027); B.S. Computer Science and Economics is related to the printed Data Science major (EEO close-match; sibling intern JDs accept CS/related); US citizen / no sponsorship; Milwaukee hybrid relocate
- **Track:** ai-ml + automotive energy-storage / battery-OEM applied DS
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN stakeholder delivery — data prep → ranked insight analog, not ML-research and not generic SWE.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision) is feature/score analog; SignalWeaver is classification (LoRA 81% → 96% held-out) plus an evaluated regression (forecast analog).
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof this applied-DS seat treats as a language floor, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact

### Misreads

- A keyword-first pass for Snowflake / Copilot Studio / Power BI / Azure Data Factory can bucket this as "no Clarios stack" even though Python, SQL, Pandas ETL, scoring, classification, and a LangGraph gen-AI pipeline are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL data-science screen is looking for, because it never sizes the freshness win.
- Education says Computer Science and Economics, not Data Science — a title-match filter can miss the related stats/econ coursework and applied-DS work.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) as the business-challenge → analytical-question loop; Lyndbrook Review Velocity (35% precision) as feature/score; SignalWeaver LoRA classification + held-out eval if they ask for model development; Vylet LangGraph 30x if they ask for generative AI / open-source LLMs
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; Snowflake / Copilot Studio / Power BI / Azure Data Factory / Matillion / VLMs are named tools, not in inventory — walk Python+SQL+Pandas and the React-less ranking/report analog instead of inventing them *(out of rails: those tools are not in the pool or swap sets)*; degree is CS + Economics, not "Data Science" — do not rewrite the major; this is Data Science Intern, not IT Digital/AI Intern and not SWE
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); SignalWeaver 81% → 96% held-out classification and 3.39% R² as "the score is not just fitting noise," not investment advice; Vylet stale-timestamp re-scrape as data-validation analog. No confirmed LeetCode OA — expect Easy Python/SQL fluency, a project deep-dive, STAR, and a capstone-style present-your-findings conversation.

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics related) and the top half is ingest → ranking/score → classification with eval, which is this req's screen
- **Overall hire odds:** Medium — Clarios is C-tier with a resume bottleneck (~20–30%) and no published OA, so this page should clear the binding intern gate; remaining cut is Milwaukee hybrid relocate, defending Python/SQL without Snowflake/Power BI, and STAR with a business audience
- **Funnel filters:** Workday **WD50211** resume screen (posted 2026-09-17) → recruiter/HM (Milwaukee hybrid, enrollment, no sponsorship) → unpublished intern loop (peer of Hy-Vee DA / Republic DA / Toro EA: Easy Python/SQL + STAR; intern program capstone presentation). No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this first wave. Honest US citizen / no sponsorship and Milwaukee hybrid yes. Prep STAR (MDC/Lyndbrook) and an honest SQL/BI answer — behavioral is a filter (`recruiting.md` §6)
