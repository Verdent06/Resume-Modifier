# Data Analytics & Engineering - Summer 2027 Internship at DICK'S Sporting Goods

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 matches JD May 2028 window; B.S. Computer Science is a listed major; US citizen
- **Track:** ai-ml + omni-channel retail / digital transformation / Fortune 400 retail data+BI platforms
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs) and a production Flask REST API on AWS EC2 shipped to MCFN — pipeline + stakeholder + production, not Product Analyst and not ML-research.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision) is the data-model / KPI analog; SignalWeaver closes on a React dashboard, then an evaluated regression.
- Binding dings: the only SQL-through-use proof is an unquantified asyncpg freshness DAL, and Experience slot 4 is a Voice AI co-op.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; a Data Analytics & Engineering screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `CaseStudyPrep.AI` · voice-AI product framing — Fourth Experience slot is a Voice AI co-op whose bullets are expired-S3 upload recovery and Silero VAD/Whisper dead-air — real production-troubleshooting numbers, but a D&A intern screener reads audio-product engineering before data platforms, pipelines, or BI

### Misreads

- A keyword-first pass for Tableau / Power BI / Snowflake can bucket this as "no BI stack" even though a React dashboard and PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- A rushed screener may bucket CaseStudyPrep.AI as a voice-AI SWE intern applying to the wrong req and miss the 27% upload-failure production-troubleshooting analog.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC rankings shipped to MCFN on EC2; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → pipeline/data model → insight loop this seat tests; SignalWeaver React dashboard if they ask for BI; Vylet Dockerized 30x pipeline if they ask for production processes; CSP 27% S3 fix if they ask for troubleshooting
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; CaseStudyPrep is a Voice AI co-op kept for production-troubleshooting numbers, not a retail-data story *(out of rails: every CSP pool bullet is voice-AI; no fifth on-axis data Experience to swap in)*; no Tableau, Power BI, Snowflake, Databricks, Linux-as-skill — walk React/Postgres and Docker/EC2 instead of inventing them *(out of rails: those tools are not in inventory or swap sets)*; this is DA&E, not Product Analyst and not generic SWE
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as data-validation analog; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice; Agile collaboration analog is MCFN/Lyndbrook stakeholder scoping — do not invent Scrum/Jira. No confirmed intern OA — expect Python/SQL fluency, a project deep-dive, STAR, cameras on, no AI tools

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → pipeline/API → scored shortlist → dashboard, which is this req's screen
- **Overall hire odds:** Medium — DICK'S is C-tier with a resume bottleneck (~15–25%) and no published intern OA, so this page should clear the binding intern gate; the remaining cut is Pittsburgh hybrid relocate for May 17–July 29, defending Python/SQL fluency, and why this is a DA&E seat rather than Product Analyst or voice-AI SWE
- **Funnel filters:** Workday **202608778** + human resume screen (posted 2026-09-08) → recruiter → unpublished intern loop. Intern OA unpublished. No intern sys design. Bottleneck: resume · ~15–25% (`companies.md` C-tier). Cameras on; no AI tools in interviews/assessments; background check / ID verification. Hybrid Pittsburgh CSC; housing for non-local interns.
- **Outside the resume:** Apply this opening week. No DICK'S contact in `network.md` — do not pick Employee Referral. See `written-answers.md`.
