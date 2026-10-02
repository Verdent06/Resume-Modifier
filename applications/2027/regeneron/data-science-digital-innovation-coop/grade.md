# 2027 Co-op Data Science & Digital Innovation (Preclinical Manufacturing & Research IT) at Regeneron

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — B.S. Computer Science is on the JD major list; Expected May 2028 vs January–August 2027 co-op (returns Fall 2027). GPA 3.66 vs 3.0 preferred. US citizen. Tarrytown onsite is a yes-relocate, not an eligibility miss on the page.
- **Track:** ai-ml + preclinical manufacturing / research IT
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → PAC ranking engine → Flask REST on AWS EC2. Ingest → operational ranking → served production app — the manufacturing-IT apps/dashboards/automation analog, not generic product-SWE and not notebook ML.
- Lyndbrook is the ops-data scoring analog in the lead window (EPA ECHO + MassGIS → entity DB → 800+ Day-1 targets → Review Velocity 800→280 at 35% precision). Vylet carries automation + SQL through use (Dockerized LangGraph scored pipeline; asyncpg freshness).
- Binding ding: none. SignalWeaver closes the bioreactor-ML analog (LoRA 81%→96% held-out; out-of-sample regression) and the dashboard line (React + Postgres). Python/SQL through use. No MATLAB, R, CFD, Snowflake, Databricks, Tableau, Power BI, Copilot, or Fusion.

### Demerits

No demerits — clean screen.

### Misreads

- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches LangGraph / SQL DAL.
- SignalWeaver's financial-research descriptor can read as notebook ML or as the wrong industry; the on-page work is held-out LoRA, out-of-sample regression, and a React dashboard, not `model.fit()` and not a bioreactor model.
- A keyword-first pass for MATLAB / R / CFD / Tableau can bucket this as "no manufacturing DS stack" even though Python/SQL/Pandas ETL, a Flask app, ranked reports, LangGraph, and a React/Postgres dashboard are the honest inventory.
- Lyndbrook is water-utility *operators as acquisition targets*, not Regeneron preclinical manufacturing — say that out loud if they map it to bioreactors too tightly.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and PAC rankings for MCFN (pipeline + scientist/engineer-facing app analog); Lyndbrook entity DB + Review Velocity (ops/regulatory-shaped data, 800 → 280, 35% precision); Vylet Dockerized LangGraph 30x scored pipeline plus SQL freshness (automation); SignalWeaver LoRA 81%→96% held-out plus OOS regression plus React dashboard (AI/ML + dashboards)
- **Defend:** No MATLAB, R, ANSYS/Fluent/CFD, Snowflake, Databricks, Tableau, Power BI, Copilot, or Regeneron VelociSuite/IOPS names — say Python/SQL/Pandas/Postgres/Docker/AWS EC2/LangGraph and a React dashboard, then ramp. SQL on the page is freshness/validation, not a warehouse JOIN that produced a ranking. LoRA is held-out eval on Financial PhraseBank, not a production bioreactor model. CFD is a named workstream in the JD — out of inventory; do not fake it. This is R51031 Preclinical Manufacturing & Research IT DS/Digital Innovation, not a 10-week summer intern, not a biology bench co-op, not MBA BuiLD. Tarrytown onsite January–August 2027, 40h/week, US citizen / no sponsorship. Linear Algebra for Machine Learning is on Education — do not claim a completed junior year before Jan 2027 (started Aug 2025; Expected May 2028).
- **Depth prep:** Walk one ingest → rank/score → served app path (MDC Flask REST) and one eval path (SignalWeaver held-out LoRA / OOS $R^{2}$ + React dashboard). Walk LangGraph + SQL freshness if they probe automation / data-platform analog. STAR for presenting to scientists/engineers (`recruiting.md` §6 — behavioral is a filter). Official intern OA unpublished — project walk + Python, not an invented HackerRank OA. GitHub is on the page; be ready to open SignalWeaver.

## Likelihood

- **Resume screen:** High — on-axis applied-DS intern/co-op page with Python/SQL through use, held-out ML, production API, automation pipeline, and a dashboard on a resume-gated Workday req
- **Overall hire odds:** Medium — B-tier ~8–12% with resume as the bottleneck; this page clears the screen. Residual risk is Tarrytown January–August onsite yes and a verbal Python/project walk without claiming CFD or bioreactors
- **Funnel filters:** Workday `regeneron.wd1` **R51031** resume (bottleneck) → recruiter (auth, Tarrytown onsite, Jan–Aug 2027, enrolled/return-to-school) → possible HireVue **[directional, Extern — not confirmed]** → project-manager interviews. Intern OA unpublished — do not assume HackerRank/CodeSignal. No intern sys design. This JD prints no visa line; answer US citizen / no sponsorship
- **Outside the resume:** Apply in this official August–November window (posted 2026-10-02). Honest Tarrytown Jan–Aug 2027 yes and `verdent06@gmail.com`. No Regeneron contact in `network.md` — Workday cold apply, not an invented employee referral. Packet only from this agent — see `written-answers.md`
