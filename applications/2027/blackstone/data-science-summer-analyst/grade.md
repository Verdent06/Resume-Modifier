# 2027 Data Science Summer Analyst at Blackstone

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside JD window Fall 2027–Spring 2028; currently enrolled undergraduate; GPA 3.66 and month/year on the page; PDF
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: messy campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → ranking → Flask API on AWS EC2. Ingest → method → served output for applied DS, not BXTI SWE 45021 and not BXTI DE 45022.
- Lyndbrook is multi-source EPA/MassGIS deal targeting plus an 800→280 scoring closer — PE/search-fund analog next to BXDS investment analytics. Vylet carries SQL through use (asyncpg freshness) plus a Dockerized LangGraph pipeline; SignalWeaver is LoRA with held-out eval (81%→96%) and out-of-sample regression.
- Binding ding is minor: CaseStudyPrep.AI is a one-line voice-AI / S3-upload co-op at the bottom of Experience.

### Demerits

- **minor** · `CaseStudyPrep.AI` · off-axis voice-AI co-op — last Experience slot is S3 presigned-URL retry for WAV uploads; real reliability work, not Python/SQL analytics, deal scoring, or ML-with-eval

### Misreads

- A skim that stops on CaseStudyPrep.AI's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL, Lyndbrook deal-scoring, and SignalWeaver held-out LoRA the BXDS screen wants.
- Vylet's PE/search-fund founder tagline can read as startup SaaS rather than a scored-lead pipeline with a SQL DAL.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and MCFN delivery on EC2; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver LoRA 81%→96% held-out plus OOS $R^{2}$; Vylet SQL freshness + LangGraph pipeline
- **Defend:** CaseStudyPrep.AI is S3 retry logic from a voice-AI co-op, not BXDS applied DS *(out of rails: pool is VAD / S3 / Web Workers; min_entries=5 blocks omit; Granular Synth is worse C++ DSP)*. SQL on the page is asyncpg timestamp validation, not a warehouse JOIN — walk the DAL and what you would query next. Do not claim Snowflake, Databricks, Tableau, Copilot, or Fusion
- **Depth prep:** Applied analytics (Python/SQL/stats), not the PE HireVue/LBO funnel and not BXTI HackerRank-as-this-req. Walk one ingest → score → stakeholder output path (Lyndbrook or MDC) and one eval path (SignalWeaver held-out LoRA / OOS regression). STAR for independent workstreams and explaining technical work to non-builders. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — applied-DS page for a resume-gated BXDS intern; eligible class year, GPA, Python/SQL through use, genAI with eval
- **Overall hire odds:** Medium — B-TIER ~5–8%; screen is a hard gate and this page clears it, then first-round video and Superday still eliminate. Remaining risk is stats fluency, commercial communication, NYC onsite, and defending an honest stack without Snowflake/Databricks/Tableau
- **Funnel filters:** Workday campus resume (bottleneck: resume) → first-round video (official students page) → face-to-face/Superday. BXDS DS is applied analytics, not PE HireVue/LBO and not BXTI SWE/DE. Comp $110k annualized; NYC onsite; ~10 weeks; req 44862; apply by 9/20/2026. Posting uses AI resume screening as one factor
- **Outside the resume:** Apply in this first-wave window (posted 2026-08-21, apply by 9/20/2026); a BXDS/alumni referral if available; 2–3 STAR stories for independent workstreams and translating technical results for deal teams (`recruiting.md` §4, §6)
