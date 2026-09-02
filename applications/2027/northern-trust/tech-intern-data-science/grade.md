# Technology Intern – Data Science and Analytics at Northern Trust

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs JD December 2027 through Summer 2028; GPA 3.66 ≥ 3.0; B.S. CS + Economics (related with Analytics/DS); US citizen / no sponsorship
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: messy campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → ranking → Flask API on AWS EC2. Applied DS intern, not ML research and not generic SWE.
- Lyndbrook is multi-source EPA/MassGIS targeting plus Review Velocity (800 → 280 at 35% precision). Vylet is a Dockerized LangGraph pipeline with SQL through use (asyncpg timestamp validation). SignalWeaver is a React dashboard plus OOS linear regression (3.39% $R^{2}$) on financial research scores.
- Binding dings are both minor: CaseStudyPrep.AI is a one-line voice-AI co-op; SQL on the page is DAL freshness, not query/aggregation inside the ETL.

### Demerits

- **minor** · `CaseStudyPrep.AI` · single-bullet off-axis voice-AI — Silero VAD / ONNX silence-filter cutting Whisper cost 40%; audio inference, not ingest → pipeline → served analytics
- **minor** · `Vylet` · SQL through-use is validation not analytics — Skills lists SQL; the lead Vylet bullet is injection-safe timestamp validation in an asyncpg DAL; MDC ETL and Lyndbrook scoring never show a query or aggregation

### Misreads

- A skim that stops on CaseStudyPrep.AI's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL, Lyndbrook scoring, and SignalWeaver dashboard/regression.
- Vylet's PE/search-fund founder tagline can read as startup SaaS rather than a scored-lead pipeline with a SQL DAL.
- SQL-in-Skills plus a DAL bullet can be over-read as warehouse SQL (Snowflake/Databricks) — it is not.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and MCFN delivery on EC2; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver dashboard + OOS regression; Vylet LangGraph pipeline + SQL freshness
- **Defend:** CaseStudyPrep.AI is on-device VAD cost-cut from a voice-AI co-op, not DS&A *(out of rails: pool is VAD / S3 / Web Workers; min_entries=5 blocks omit; Granular Synth is worse C++ DSP)*. SQL on the page is asyncpg timestamp validation, not a warehouse JOIN *(out of rails: MDC/Lyndbrook/SignalWeaver pools have no query/join bullet; dropping the DAL recreates a SQL skills-only major)*. Do not claim R, Tableau, Power BI, Snowflake, Databricks, Copilot, Fusion, or Sentry — JD BI tools are an OR, not a must-have
- **Depth prep:** Superday analog ~2 Teams interviews, mixed behavioral + Easy–Med Python/SQL/project (`company.md`). No standard LeetCode OA published for this DS intern. Walk one ingest → score → stakeholder path (MDC or Lyndbrook) and one dashboard/stats path (SignalWeaver). STAR for explaining a ranking/score to a non-builder. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — eligible May 2028, 3.66 GPA, CS+Econ, Python-through-use ETL and scoring with a finance-adjacent dashboard/regression project; applied-DS page for a resume-gated C-tier intern
- **Overall hire odds:** Medium — C-TIER ~10–20% with resume + 3-app cap as bottleneck; this PDF can clear the human screen, then recruiter knockout and Superday Python/SQL/project still eliminate. Remaining risk is Chicago hybrid logistics, defending SQL as DAL-not-warehouse, and the 3-posting cap crowding out this req
- **Funnel filters:** Workday resume (rolling; bottleneck: resume + 3-app cap) → recruiter screen (work-auth / GPA / grad window) → Superday (~2 Teams, mixed behavioral + technical). No standard LeetCode OA published. Comp $35/hr; 10-week Chicago hybrid Summer 2027; req **R160865**. Close 2026-10-09 11:59pm CT unless filled
- **Outside the resume:** Apply in this first wave (posted ~2026-09-01). Drill Easy–Med Python/SQL walkthroughs. Spend the 3-app cap deliberately — this is one of three NA postings. Use form-kit email `verdent06@gmail.com` on Workday. A Chicago/UMich wealth-management alum referral still beats cold Workday
