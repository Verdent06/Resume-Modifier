# 2027 Summer Internship Program — Data Science Intern (Engineering) at BNY

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs JD Dec 2027 or May 2028 (U.S.); GPA 3.66 ≥ 3.0; US citizen / no sponsorship
- **Track:** ai-ml
- **Pipeline:** 4 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: messy campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → ranking → Flask API on AWS EC2. Applied DS on the Engineering program, not ML research and not Java/Spring SWE.
- Lyndbrook is multi-source EPA/MassGIS targeting plus Review Velocity (800 → 280 at 35% precision). Vylet is a Dockerized LangGraph pipeline with SQL through use (asyncpg timestamp validation). SignalWeaver is LoRA with held-out eval (81%→96%) and out-of-sample regression.
- Binding dings are both minor: CaseStudyPrep.AI is a one-line voice-AI co-op; SQL on the page is DAL freshness, not query/aggregation inside the ETL.

### Demerits

- **minor** · `CaseStudyPrep.AI` · single-bullet off-axis voice-AI — Silero VAD / ONNX silence-filter cutting Whisper cost 40%; audio inference, not ingest → method → business-readable analytics
- **minor** · `Vylet` · SQL through-use is validation not analytics — Skills lists SQL; the only through-use is injection-safe timestamp validation in an asyncpg DAL; MDC ETL and Lyndbrook scoring never show a query or aggregation

### Misreads

- A skim that stops on CaseStudyPrep.AI's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL, Lyndbrook scoring, and SignalWeaver held-out LoRA.
- Vylet's PE/search-fund founder tagline can read as startup SaaS rather than a scored-lead pipeline with a SQL DAL.
- SQL-in-Skills plus a DAL bullet can be over-read as warehouse SQL (Snowflake/Databricks) — it is not.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and MCFN delivery on EC2; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver LoRA 81%→96% held-out plus OOS $R^{2}$; Vylet LangGraph pipeline + SQL freshness
- **Defend:** CaseStudyPrep.AI is on-device VAD cost-cut from a voice-AI co-op, not Engineering DS *(out of rails: pool is VAD / S3 / Web Workers; min_entries=5 blocks omit; Granular Synth is worse C++ DSP)*. SQL on the page is asyncpg timestamp validation, not a warehouse JOIN *(out of rails: MDC/Lyndbrook pools have no query/join bullet; dropping the DAL recreates a SQL skills-only major)*. Do not claim Java, Spring, Node, Snowflake, Databricks, Tableau, Copilot, Fusion, or Sentry
- **Depth prep:** Timed HackerRank Easy–Med (Engineering 4Q **[directional]**), including SQL. Walk one ingest → score → stakeholder path (MDC or Lyndbrook) and one eval path (SignalWeaver held-out LoRA). STAR for explaining a ranking/score to a non-builder. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — eligible May 2028, 3.66 GPA, CS+Econ, Python-through-use ETL and scoring with measured outputs; applied-DS page for a resume-gated Engineering DS intern
- **Overall hire odds:** Medium — B-TIER ~8–12%; this PDF can clear the human screen, then HackerRank 4Q Easy–Med **[directional]** and tech+behavioral still eliminate. Remaining risk is OA fluency, defending SQL as DAL-not-warehouse, and NYC onsite
- **Funnel filters:** Oracle HCM resume (bottleneck: resume) → short assessment / HackerRank 4Q Easy–Med **[directional]** → tech + behavioral. No intern sys design published. Comp $52–110k annualized; 10-week Summer 2027; req **81240** NYC (siblings 81238 / 81241 / 81239)
- **Outside the resume:** Apply in this first wave (posted 2026-08-24). Drill HackerRank Easy–Med including SQL. No BNY contact in `network.md` — a referral still beats cold Oracle. Use form-kit email `verdent06@gmail.com` on the apply wizard
