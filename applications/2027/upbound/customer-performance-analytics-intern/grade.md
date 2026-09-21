# Customer Performance Analytics Intern at Upbound Group

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — enrolled bachelor's; Junior / Summer 2027 after sophomore = completed second year vs first-or-second-year line; GPA 3.66 vs 3.2 preferred; US citizen / no OPT-CPT; Plano 10-week onsite yes
- **Track:** ai-ml + customer-lifecycle / journey analytics (transaction + clickstream + CRM) for lease-to-own / consumer-finance (Acima, RAC, Brigit)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs) and PAC rankings shipped to MCFN on a Flask REST API / AWS EC2 — ingest → rank → stakeholder delivery, not ML-research and not SWE intern R-100761.
- Lyndbrook EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision) is the customer-scoring / KPI analog in the lead window.
- Binding ding is small: the only on-page SQL proof (Vylet asyncpg freshness) never sizes the win. GPA 3.66 and Expected May 2028 clear this posting's gates.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; an applied-analytics screen looks for query/aggregate/insight SQL and does not find it.

### Misreads

- A keyword-first pass for Tableau / Power BI / Snowflake / Salesforce can bucket this as "wrong stack" even though a React/TypeScript dashboard and ranked PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- A rushed screener who sees Flask REST / founder MRR might bucket this as the sibling SWE intern spine (R-100761) and miss the customer-analytics analog in MDC/Lyndbrook.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC rankings shipped to MCFN on EC2; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → score → insight loop this seat tests; SignalWeaver out-of-sample regression + React/TypeScript dashboard if they ask for viz or eval; Vylet SQL freshness / 79%→89% qualification if they ask for data quality
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*. No Tableau, Power BI, Snowflake, Databricks, SAS, Salesforce, or Oracle — walk React/Postgres and Pandas instead of inventing them *(out of rails: those tools are not in inventory or swap sets)*. This is **R-100769** Customer Performance Analytics, not SWE intern **R-100761**.
- **Depth prep:** Unpublished intern loop (peer of Avis DA / Hy-Vee DA: Easy SQL/Python + STAR, not LC OA). Walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist). Vylet stale-timestamp re-scrape as data-validation analog. SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. Plano 10-week in-office relocate is a yes. Sibling SWE dates May 25–July 30 2027 are analog only.

## Likelihood

- **Resume screen:** High — eligible Junior with GPA 3.66, Pandas ETL + PAC rankings in the lead, scoring/KPI analog next, dashboard + SQL on the page; one unquantified SQL line does not sink a C-tier DA intern screen
- **Overall hire odds:** Medium — resume-first C-tier intern (~20–30%); unpublished Easy SQL/Python + STAR loop, not an OA gauntlet. Plano 10-week relocate is the operational filter after the PDF
- **Funnel filters:** Workday **R-100769** + human resume screen (posted 2026-09-21) → recruiter/HM (Plano onsite, no OPT/CPT, GPA 3.2 preferred) → unpublished intern loop (Easy SQL/Python + STAR analog, not LC OA). No intern sys design. Bottleneck: resume · ~20–30% (`companies.md` C-tier). Comp unlisted; sibling SWE **$22.00/hr** analog.
- **Outside the resume:** Apply in this first-wave window. No Upbound contact in `network.md` — do not pick Employee Referral. See `written-answers.md`.
