# Boeing Summer 2027 Internship Program (Paid) – Data Analytics Intern at Boeing

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is after August 2027; GPA 3.66 ≥ 3.0 preferred; US citizen is a US Person and clearance-eligible; no sponsorship needed
- **Track:** ai-ml
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Vylet leads with a Dockerized LangGraph pipeline (30x), LangSmith eval (50%→90% faithfulness), and SQL in a production DAL — applied data/AI, not notebook ML.
- MDC Pandas ETL (~800 hours / 400 PACs) plus Flask/AWS and Lyndbrook's scoring shortlist (35% precision) read as messy-data pipelines and measured analytics; SignalWeaver closes with LoRA 81%→96% held-out and an out-of-sample regression.
- Binding ding: the SQL proof and the production API closer are unquantified.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact — an analytics screener cannot tell how much the DAL moved the pipeline.
- **minor** · `Michigan Data Consulting (MDC)` · API bullet metric-free — The Flask/EC2 delivery line is the production-platform closer after a strong ETL hook, but it has no throughput, latency, or adoption number — the 5-month sole-engineer frame sizes tenure, not impact.

### Misreads

- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Data Analytics screen is looking for, because it never sizes the freshness win.
- The Flask/EC2 closer can read as generic SWE delivery rather than the stakeholder-scoped analytics product analog, because tenure stands in for impact.

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval (20 adversarial cases, Pydantic consensus gates, 50%→90% faithfulness); MDC Requests+Pandas ETL on irregular filings; SignalWeaver LoRA + held-out accuracy and out-of-sample regression; Lyndbrook Review Velocity shortlist
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use)*. Flask/EC2 is tenure-and-stack — pair it verbally with the 800-hour ETL *(out of rails: MDC pool has no metric-bearing API bullet)*. No aerospace, Tableau, Power BI, Snowflake, Databricks, or clearance-in-hand — do not invent them; say industrial messy-data work (filings, EPA) is the analog
- **Depth prep:** LangSmith eval failure modes and consensus gates; LoRA data split / overfit story; SQL+Python talking points (no standard OA — still expect tool fluency); HireVue/live STAR on stakeholder-scoped delivery (MDC/Lyndbrook) and "why aerospace, why Boeing"; clearance/US Person form answers (eligible, not already cleared)

## Likelihood

- **Resume screen:** High — Python/SQL through use, Pandas ETL, LangGraph+eval, LoRA with held-out accuracy, scoring/precision, AWS, and GPA 3.66/stats coursework all register in one pass on a resume-first B-tier intern req
- **Overall hire odds:** Medium — Bottleneck is the resume and this page is on-axis for applied analytics, but 1–3 behavioral rounds plus occasional HireVue still eliminate, and the page never names aerospace interest the preferred qual asks for. B-tier ~15–20% is the ceiling analog
- **Funnel filters:** Workday resume screen (rolling through Oct 23, 2026). No standard OA; occasional HireVue or skill-alignment survey; 1–3 live behavioral (phone / Teams / Webex). US Person / no sponsorship; this posting requires Security Clearance (eligibility, not in-hand). Bottleneck: resume (`companies.md` Boeing B-tier)
- **Outside the resume:** Apply in the first rolling wave before the Oct 23, 2026 close; prep STAR for HireVue/live behavioral (why aerospace, why Boeing, stakeholder delivery); do not invent Tableau/Snowflake or clearance-in-hand on the form
