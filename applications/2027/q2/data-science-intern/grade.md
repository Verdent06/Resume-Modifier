# 2027 Summer Internship - Data Science at Q2 Software, Inc.

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — B.S. Computer Science is on the JD degree list (currently pursuing Data Science, Statistics, Computer Science, or related); US citizen (authorized to work for any US employer; no visa sponsorship); Expected May 2028 vs Summer 2027 (still enrolled after the term; no class-year knockout on this JD)
- **Track:** ai-ml + fintech-backend
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → PAC ranking engine → Flask REST on AWS EC2. Ingest → operational ranking → served output — the intern team's pipeline analog, not generic product-SWE and not notebook ML.
- Lyndbrook is the finance-adjacent scoring analog in the lead window (EPA ECHO + MassGIS → 800+ Day-1 targets → Review Velocity 800→280 at 35% precision). Vylet carries SQL through use (asyncpg freshness) plus a Dockerized LangGraph scored pipeline.
- Binding ding: none. SignalWeaver closes the ML-algorithms/packages bar (LoRA 81%→96% held-out; out-of-sample regression) and the intern dashboard example (React + Postgres). Python/SQL through use. No Tableau, Power BI, scikit-learn, R, Java, Snowflake, Databricks, Spark, Kubernetes, or Q2 product names.

### Demerits

No demerits — clean screen.

### Misreads

- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape and 30x scored-pipeline lines.
- SignalWeaver's financial-research descriptor can read as notebook ML; the on-page work is held-out LoRA, out-of-sample regression, and a React dashboard, not `model.fit()`.
- A keyword-first pass for Tableau / Power BI / scikit-learn can bucket this as "no DS stack" even though Python/SQL/Pandas ETL, ranked PAC reports, and a React/Postgres dashboard are the honest inventory.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and PAC rankings for MCFN (pipeline + operational-insight analog); Lyndbrook PWSID entity DB + Review Velocity (800 → 280, 35% precision) as the finance-adjacent scoring analog; SignalWeaver LoRA 81%→96% held-out plus OOS regression plus React dashboard; Vylet SQL freshness plus the 30x Dockerized scored pipeline
- **Defend:** No Tableau, Power BI, scikit-learn, R, Java, Snowflake, Databricks, Spark, Kubernetes, or Q2 product names — say Python/SQL/Pandas/Postgres/Docker/AWS EC2 and a React dashboard, then ramp. SQL on the page is freshness/validation, not a warehouse JOIN that produced a ranking — walk the asyncpg DAL. LoRA is held-out eval on Financial PhraseBank, not a production Q2 model. This is the Data Science intern (REQ-12799), not a Software Engineering intern sibling. Cary NC onsite, 12-week official U.S. intern term, US citizen / no sponsorship. Linear Algebra for Machine Learning is on Education — do not claim a completed junior year.
- **Depth prep:** Walk one ingest → rank/score → served output path (MDC or Lyndbrook) and one eval path (SignalWeaver held-out LoRA / OOS $R^{2}$). STAR for defining a problem with a stakeholder and gathering feedback (`recruiting.md` §6 — behavioral is a filter). Official loop is TA then one or two hiring-team interviews — project walk + Python/SQL/ML-coursework, not an invented HackerRank OA. Git/GitHub is on the page; be ready to open SignalWeaver.

## Likelihood

- **Resume screen:** High — on-axis applied-DS intern page with Python/SQL through use, held-out ML, pipelines, and a dashboard on a resume-gated Workday intern req
- **Overall hire odds:** Medium — Unrated mid-size public fintech SaaS; resume is the binding gate and this page clears it, then TA plus one or two hiring-team interviews still eliminate. Intern OA unpublished; no intern sys design. Analog ~15–25% for C-tier-like banking-software intern funnels, not a BNY/Fidelity B-tier bar
- **Funnel filters:** Workday `q2ebanking.wd5` **REQ-12799** resume (bottleneck) → Talent Acquisition (auth, Cary/term, student status) → 1–2 hiring-team interviews → offer (~2-week response). Intern OA unpublished — do not assume HackerRank/CodeSignal. No intern sys design. English fluency. **No visa sponsorship.** Official U.S. program: 12-week summer; postings in September (`company.md`; `recruiting.md` intern)
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-29). Honest Cary onsite / 12-week yes and `verdent06@gmail.com`. No Q2 contact in doctrine — Workday cold apply, not an invented employee referral
