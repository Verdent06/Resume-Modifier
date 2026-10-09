# 2027 Summer Intern – Data Science at Papa John's

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — JD requires *"Currently enrolled in a college or university program or graduate within the past 6 months"*; page shows Expected May 2028 CS+Econ B.S., currently enrolled. No exclusive class year, no grad-only, no clearance.
- **Track:** ai-ml + QSR / pizza-delivery retail business analytics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN stakeholder delivery — data prep → ranked insight analog, not ML-research and not generic SWE.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision) is feature/score analog; SignalWeaver is held-out classification (LoRA 81% → 96%) plus an evaluated regression (predictive-model analog).
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL-through-use proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact

### Misreads

- A keyword-first pass for Databricks / PySpark / BigQuery / Tableau (tools a prior PJ DS co-op used, not this JD) can bucket this as "no QSR stack" even though prep, scoring, classification, and regression-with-eval are on the page.
- The SQL/DAL line can read as database plumbing rather than data-validation analog, because it never sizes the freshness win.
- Vylet's PE/search-fund founder tagline can read as startup SaaS rather than a scored-lead pipeline with a SQL DAL.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN researchers; ~800 hours / 400 PACs) as the business-question → analytical-question loop; Lyndbrook Review Velocity (35% precision) as feature/score; SignalWeaver LoRA classification + held-out eval and 3.39% R² regression if they ask for predictive models / ML; Vylet LangGraph 30x if they ask about a summer-project-shaped pipeline
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; Databricks / PySpark / BigQuery / Tableau / Power BI / Snowflake are not in inventory — walk Python+SQL+Pandas and the ranking/report analog instead of inventing them *(out of rails: those tools are not in the pool or swap sets)*; degree is CS + Economics — do not rewrite the major to Data Science; this is Data Science Intern, not Accounting intern and not restaurant crew
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); SignalWeaver 81% → 96% held-out classification and 3.39% R² as "the score is not just fitting noise"; Vylet stale-timestamp re-scrape as data-validation analog. No confirmed LeetCode OA — expect Easy applied-DS fluency, a project deep-dive, STAR, and a present-your-findings conversation. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.7, enrolled) and the top half is ingest → ranking/score → classification/regression with eval
- **Overall hire odds:** Medium — Papa John's is C-tier with a resume bottleneck (~20–30%) and no published OA, so this page should clear the binding intern gate; remaining cut is Atlanta HQ relocate for 10 weeks, defending Python/SQL without a named PJ warehouse/BI stack, and STAR with a business audience
- **Funnel filters:** Workday **R26_0000002157** resume screen (posted 2026-10-09) → recruiter/HM (Atlanta HQ, enrollment, 10 weeks) → unpublished intern loop (peer of Hy-Vee DA / Clarios DS: Easy applied-DS + STAR). No intern sys design. Bottleneck: resume (`companies.md`)
- **Outside the resume:** Apply in this first wave. Honest US citizen / Atlanta yes. Form email `verdent06@gmail.com`. Airtable `reck1zyNFfw7XAgge` stays In Progress until a human submits
