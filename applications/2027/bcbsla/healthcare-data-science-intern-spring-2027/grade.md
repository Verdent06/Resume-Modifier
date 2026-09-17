# CW Healthcare Data Science Intern (Spring 2027) at Blue Cross Blue Shield of Louisiana (Louisiana Blue)

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 1 emergency, 0 major, 2 minor)
- **Eligibility:** ineligible — JD requires Senior undergraduate / recent graduate / graduate student; candidate is Junior at Spring 2027 (Expected May 2028). Separately, remote WFH-state list does not include Michigan.
- **Track:** ai-ml + healthcare-payer analytics / medical cost, risk adjustment, member outcomes, provider performance
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is Vylet: Dockerized LangGraph scored-lead pipeline (30x), LangSmith eval 50%→90%, injection-safe SQL freshness — applied scoring + eval + SQL, not ML-research and not generic SWE.
- MDC in Activities is the wrangling/stakeholder analog (Requests + Pandas ETL ~800 hours / 400 PACs; PAC ranking). SignalWeaver is held-out regression (3.39% R²) plus a React dashboard. GPA 3.66 and stats/econ coursework are on-axis.
- Binding ding: Education prints **Expected May 2028**. This req wants **Senior / recent grad / grad student** for Spring 2027. That is an auto-reject before the models are scored. Michigan is also absent from the approved WFH-state list (form, not the PDF).

### Demerits

- **emergency** · `Education` · class-year / Senior miss — JD requires Senior undergraduate, recent graduate, or graduate student; the page prints Expected May 2028, which is Junior at Spring 2027. Binary class-year knockout before Python/SQL proof is weighed.
- **minor** · `CaseStudyPrep.AI` · voice-AI product framing — Second Experience is a Voice AI co-op whose bullets are Silero VAD/Whisper dead-air and expired-S3 upload recovery — real production numbers, but a Healthcare Data Science screener reads audio-product engineering before wrangling, regression, or payer-analytics.
- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof required by the JD, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; a DS screen looks for query/aggregate/insight SQL and does not find it.

### Misreads

- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape and LangSmith gate lines.
- SignalWeaver’s financial-research descriptor can read as notebook ML; the on-page work is an out-of-sample regression plus a React dashboard, not a clinical model.
- A keyword-first pass for Databricks / Tableau / Power BI / scikit-learn can bucket this as “no DS stack” even though Python, SQL, Pandas ETL, regression eval, and LangGraph/LangSmith are on the page.
- A form reviewer who never opens the PDF will still auto-reject on Senior and on Michigan WFH.

### Interview angles

- **Lead with:** Vylet scored pipeline (30 leads / 30 minutes) + LangSmith eval (20 adversarial cases, 50%→90%) as predictive scoring + model evaluation; MDC Requests + Pandas ETL and PAC rankings as wrangling / EDA / stakeholder insight; SignalWeaver out-of-sample regression (3.39% R²) if they ask for stats/ML; Vylet SQL freshness if they ask for SQL; CSP 27% S3 recovery only if they ask for production/IT collaboration.
- **Defend:** Class year is **Junior / Expected May 2028**, not Senior — say so; do not move the date *(out of rails: Education block is fixed; no pool bullet can rewrite Expected May 2028)*. Work location is **Northville, MI** — Michigan is not an approved WFH state; do not claim Louisiana residency *(form knockout, not a PDF line)*. No Databricks, Tableau, Power BI, Snowflake, scikit-learn, Excel-as-skill, NumPy-as-skill, or Jupyter-as-skill — walk Pandas / Python / SQL / PyTorch-adjacent LoRA-eval only if asked, and ramp on their lakehouse. SQL on the page is freshness/validation, not a JOIN that produced a ranking — say Pandas did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*. CaseStudyPrep is a Voice AI co-op kept as form-kit employment, not a healthcare-DS story *(out of rails: every CSP pool bullet is voice-AI)*. No payer/claims internship — analog is messy filings (MDC) and scored operational pipelines (Vylet), not Louisiana Blue warehouses.
- **Depth prep:** Walk ingest → wrangle → score → eval on Vylet (consensus gates, faithfulness lift) and MDC (irregular Excel → PAC rank). SignalWeaver 3.39% R² as “the score is not just fitting noise,” not investment advice. STAR for translating a finding to a non-technical stakeholder (MDC researchers). Easy Python/SQL/applied-DS walk; intern OA unpublished. Background + pre-employment drug screen. End-of-cohort executive presentation.

## Likelihood

- **Resume screen:** Low — May 2028 vs Senior-required is a binary knockout; among eligible applicants this applied-DS page would otherwise be High at a resume-first C-tier screen.
- **Overall hire odds:** Low — class-year and Michigan-not-on-WFH-list knockouts auto-reject before a phone/video/panel (`recruiting.md` Part I §1, Part II §8). Among eligible applicants the accept analog is ~20–30% (`companies.md`); this packet is not in that set.
- **Funnel filters:** Workday Generation_Blue **R12151** → Talent Acquisition review (Spring: Oct 1–Nov 1) → phone / video / panel Nov 1–Dec 1 (`careers.lablue.com/college-internships`). Intern OA unpublished. No intern sys design. Bottleneck: resume (+ class-year and WFH-state knockouts) · ~20–30% among eligible. GPA 3.0 min / 3.5+ preferred (3.66 clears). CS+Econ clears. 20h/wk remote Spring 2027. CW paid by a third-party staffing vendor. Background + drug screen.
- **Outside the resume:** Answer Junior and Northville, MI honestly. Do not apply expecting the knockouts to be ignored unless a recruiter confirms. No Louisiana Blue / BCBSLA contact in `network.md`. Apply window closes **Sep 30**. See `written-answers.md`.
