# 2027 Summer Intern, MS/PhD, Data Science - Commercialization Testing at Waymo

## Verdict

- **Score:** 3.0 / 10 (7 demerits — 1 emergency, 2 major, 1 minor)
- **Eligibility:** ineligible — JD requires enrollment in a Master's or PhD; page shows B.S. CS + Economics, Expected May 2028 (rising senior at Summer 2027)
- **Track:** ai-ml + autonomy
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: messy campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → ranking → Flask API on AWS EC2. Applied DS spine, not SWE and not perception research.
- Lyndbrook is multi-source EPA/MassGIS targeting plus Review Velocity that proxies fleet expansion (800 → 280 at 35% precision). SignalWeaver is OOS linear regression plus LoRA held-out eval (81%→96%). Vylet is a Dockerized LangGraph pipeline with SQL through use (asyncpg timestamp validation).
- Binding ding is on Education: B.S. Expected May 2028 against an MS/PhD-only req. Secondary: no Bayesian/small-sample inference; SQL is DAL freshness, not log query; CSP is a one-line voice-AI co-op.

### Demerits

- **emergency** · `Education` · stated eligibility miss — Page shows B.S. Computer Science and Economics, Expected May 2028. The JD requires enrollment in a Master's or PhD program. Binary intern knockout before the applied-DS spine is weighed.
- **major** · `resume` · Bayesian / statistical inference absent — JD names Bayesian modeling and statistical inference. The page has ETL, ranking, scoring, OOS regression, and LoRA — not Bayesian, small-sample inference, uncertainty, or stated statistical limitations.
- **major** · `Vylet` · SQL is validation not large-scale query — Skills lists SQL; the only through-use is injection-safe timestamp validation in an asyncpg DAL. JD requires querying and synthesizing large-scale databases. MDC ETL and Lyndbrook scoring never show a query, join, or aggregation.
- **minor** · `CaseStudyPrep.AI` · single-bullet off-axis voice-AI — Silero VAD / ONNX silence-filter cutting Whisper cost 40%; audio inference, not fleet/test analytics.

### Misreads

- A skim that stops on the B.S. line correctly bins this as ineligible for an MS/PhD req — that is not a misread.
- A skim that ignores Education and stops on CaseStudyPrep.AI's Voice AI title can file this as a product/audio intern and miss MDC Pandas ETL, Lyndbrook fleet scoring, and SignalWeaver OOS regression.
- SQL-in-Skills plus a DAL bullet can be over-read as warehouse SQL (Snowflake/Databricks) — it is not.
- Lyndbrook "fleet expansion" is a scoring proxy from public compliance data, not AV fleet telemetry.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and MCFN delivery on EC2; Lyndbrook PWSID entity DB + Review Velocity (800 → 280, fleet-scale proxy); SignalWeaver OOS regression + LoRA 81%→96% held-out; Vylet production Python pipeline + SQL freshness
- **Defend:** Not enrolled in a graduate program — B.S. May 2028, rising senior Summer 2027 *(out of rails: Education is fixed; no MS/PhD in the pool)*. No Bayesian or small-sample inference on the page — closest is OOS regression and scoring *(out of rails: no pool bullet names Bayesian/posterior; Node 3 scoring overflowed the page)*. SQL is asyncpg timestamp validation, not a vehicle-log JOIN *(out of rails: MDC/Lyndbrook pools have no query/join bullet)*. CaseStudyPrep.AI is on-device VAD cost-cut, not Commercialization Testing DS *(out of rails: CSP pool is VAD/S3/Web Workers; min_entries=5 blocks omit; Granular Synth is worse C++ DSP)*. Do not claim Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, SIL/HIL, or survival analysis
- **Depth prep:** Only relevant if applying to a **non-gated** Waymo intern req. Doctrine funnel: Greenhouse resume → recruiter → HackerRank (companies.md) / live CoderPad (intern reports) → 2–5 round virtual onsite. DS loops weight Python+SQL+stats. Walk one ingest → score path (MDC or Lyndbrook) and one eval path (SignalWeaver). Behavioral is a filter (`recruiting.md` §6). Correctness and statistical limitations matter because the product is safety-critical

## Likelihood

- **Resume screen:** Low — graduate-enrollment knockout is on the education line; a strong applied-DS spine does not reopen an MS/PhD filter
- **Overall hire odds:** Low — A-TIER ~3–5% with tech rounds as bottleneck (`companies.md`). The PDF is an honest applied-Python/SQL page, but this req is graduate-only and the loop still tests stats + SQL + live coding. An undergraduate rising senior is not in the class this posting names
- **Funnel filters:** Greenhouse (8167323) resume → recruiter ~30 min → HackerRank (doctrine) / live CoderPad (intern-report delta) → 2–5 round virtual onsite (coding, stats/SQL, project deep-dive, behavioral). Bottleneck: tech rounds · ~3–5%. Hybrid onsite San Francisco. Masters $70/hr / PhD $85/hr. Rolling until filled
- **Outside the resume:** Do not spend a Waymo top-3 slot on this MS/PhD req. Apply to Waymo intern postings that name BS (or BS/MS/PhD). No Waymo contact in `network.md`. A referral does not bypass the enrollment gate
