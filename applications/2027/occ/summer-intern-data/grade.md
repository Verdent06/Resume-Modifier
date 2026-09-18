# Summer Intern - Data at The Options Clearing Corporation (OCC)

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside the printed window (Dec 2027 or May/Aug 2028); Summer 2027 after junior year is rising senior
- **Track:** ai-ml + sifmu-clearing / market-infrastructure / fintech-backend
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- UMich CS + Economics, GPA 3.66, Expected May 2028 — class-year and quantitative coursework clear the printed rising-senior window.
- Lead window is applied data, not SWE or notebook ML: messy campaign-finance filings → Pandas ETL → ranked PAC report; EPA/MassGIS → entity DB → scored shortlist.
- Binding ding: warehouse-style SQL (joins/aggregates on a multi-source store) is implied by Python ETL, not shown; Tableau is an honest preferred gap.

### Demerits

- **minor** · `resume` · SQL/warehouse analog is ETL not analytical SQL — the intern writes/optimizes SQL on large multi-source datasets; the page's only explicit SQL is Vylet timestamp validation, while MDC and Lyndbrook are Pandas ETL and an entity database
- **minor** · `SignalWeaver` · semantic-search latency on n=90 — 49ms p50 / 99ms p99 over 90 queries is a microbenchmark and does not size dashboard, KPI, or warehouse impact

### Misreads

- Recruiter buckets this as a Python ETL / scoring intern who cannot write warehouse SQL — the live loop will probe JOINs and query-tuning the page does not pre-answer.
- SignalWeaver's p50/p99 line reads as a tiny full-stack latency flex, not analytics delivery, if the dashboard hook is skipped.

### Interview angles

- **Lead with:** MDC ingest → Pandas ETL → ranked PAC report (~800 hours / 400 PACs) and Flask on AWS EC2; Lyndbrook EPA ECHO + MassGIS → PWSID entity DB, 800 → 280 at 35% precision; Vylet name-collision quality fix (79% → 89%) as the production-pressure / data-correctness STAR.
- **Defend:** No Tableau — preferred, not in inventory; ramp on OCC's BI stack rather than stuffing it. Warehouse SQL — only SQL-through-use is Vylet's asyncpg freshness DAL; aggregations live in Pandas (MDC) and Review Velocity (Lyndbrook). Walk a JOIN/aggregate on those datasets live. *(out of rails: no pool bullet has JOIN/aggregate SQL against a warehouse-shaped store.)* Claude Code is JD curiosity — do not claim production AI-coding. SignalWeaver n=90 latency — pivot to the dashboard + Postgres persist analog.
- **Depth prep:** SQL (joins, GROUP BY/HAVING, window functions, indexing talk vs claimed pooling expertise); ETL vs ELT and warehouse grain; AWS EC2 as the cloud analog (not invented Glue/Redshift); STAR for a wrong number in production (Vylet 79% → 89%); SIFMU / CCP / Ovation as company fluency without claiming OCC systems.

## Likelihood

- **Resume screen:** High — on-axis applied-data spine, Python+SQL+AWS+Postgres through use, matching class year and dual CS+Econ; Tableau is an honest preferred gap
- **Overall hire odds:** Medium — C-tier resume-first with no published OA on this Data req, so the page likely clears the human screen; hire still turns on a short loop proving warehouse-SQL fluency the page only implies, and behavioral remains a filter
- **Funnel filters:** Workday (`theocc.wd5`) resume → confirmation email → if selected, OCC representative schedules interview; intern OA unpublished; no intern sys design published; no visa sponsorship; Chicago hybrid (Tue/Wed anchors)
- **Outside the resume:** Apply in this first wave (posted 2026-09-17). No OCC contact in `network.md` — do not claim a referral. Drill SQL on messy multi-source sets plus a behavioral journal for a regulated shop.
