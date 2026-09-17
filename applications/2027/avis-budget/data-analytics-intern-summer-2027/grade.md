# Accelerate - Data Analytics Intern Summer 2027 at Avis Budget Group

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 1 emergency, 0 major, 1 minor)
- **Eligibility:** ineligible — Expected May 2028 vs JD May/June 2027 Rising Seniors
- **Track:** ai-ml + fleet / mobility ops analytics (rental debt, damage, risk; stakeholder data profiling on a vehicle-rental network)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs) and PAC rankings shipped to MCFN on a Flask REST API / AWS EC2 — ingest → profile/rank → stakeholder delivery, not ML-research and not the IT DA sibling.
- Lyndbrook EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision; fleet-expansion proxy from compliance data) is the mobility-ops / risk-KPI analog in the lead window.
- Binding ding: Education prints **Expected May 2028**. This req's class-year gate is **graduating May or June 2027 — Rising Seniors**. That is an auto-reject before the Python/SQL proof is read.

### Demerits

- **emergency** · `Education` · graduation window miss — JD requires graduating May or June 2027 — Rising Seniors; the page prints Expected May 2028. Binary class-year knockout before Python/SQL/fleet-ops proof is read.
- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; an applied-analytics screen looks for query/aggregate/insight SQL and does not find it.

### Misreads

- A rushed screener who skips the Education date might bucket this as a strong C-tier DA intern PDF (Pandas ETL, PAC rankings, fleet-expansion score, TypeScript dashboard) and still fail it on the Workday knockout two screens later.
- A keyword-first pass for Tableau / Power BI / R / Oracle can bucket this as "wrong stack" even though a React/TypeScript dashboard and ranked PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC rankings shipped to MCFN on EC2; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision, fleet-expansion proxy) as the ingest → profile/score → insight loop this seat tests; SignalWeaver out-of-sample regression + React/TypeScript dashboard if they ask for stats or viz; Vylet SQL freshness / 79%→89% qualification if they ask for data quality or SQL
- **Defend:** Graduation is **May 2028**, not June 2027 — say so; do not move the date *(out of rails: Education block is fixed; no pool bullet can rewrite Expected May 2028)*. SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*. No R, Tableau, Power BI, Snowflake, Databricks, Oracle, PL/SQL — walk React/Postgres and Pandas instead of inventing them *(out of rails: those tools are not in inventory or swap sets)*. This is **R0190389** $30 DA intern, not the $35 IT DA sibling.
- **Depth prep:** InterviewSense **[directional]**: SQL/case + stats + STAR, not LC OA. Walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist / fleet-expansion proxy). Vylet stale-timestamp re-scrape as data-validation analog. SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. Parsippany 10-week / 40h in-office relocate is a yes.

## Likelihood

- **Resume screen:** Low — May 2028 vs May/June 2027 Rising Seniors is a binary knockout; the rest of the page would otherwise clear this C-tier resume-first DA intern screen
- **Overall hire odds:** Low — intern eligibility windows auto-reject before a SQL/case or STAR loop (`recruiting.md` Part I §1, Part II §8). Among *eligible* applicants the accept analog is ~15–25%; this packet is not in that set unless ABG confirms the class-year line was copy-forward error
- **Funnel filters:** Workday **R0190389** + human resume screen (posted 2026-09-17) → recruiter/HM (Parsippany onsite, class-year) → unpublished intern loop (InterviewSense **[directional]**: SQL/case + stats + STAR, not LC OA; 2–6 weeks). No intern sys design. Bottleneck: resume · ~15–25% (`companies.md` C-tier). $30/hr; 10-week full-time in-office Parsippany HQ.
- **Outside the resume:** Honest **May 2028** on every date field. Do not apply expecting the knockout to be ignored unless a recruiter confirms. No Avis contact in `network.md` — do not pick Employee Referral. See `written-answers.md`.
