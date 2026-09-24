# Data Engineering Intern at Jabil

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — Currently pursuing B.S. Computer Science (JD: CS / Data Science / IS / related); Expected May 2028 vs Summer 2027 intern; JD has no class-year, GPA, citizenship, or visa gate
- **Track:** ai-ml
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings (Excel exports) → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation / normalize / PAC ranking → Flask REST on AWS EC2. Ingest → transform → serve for a NA Ops Data Engineering Intern, not Finance DE and not notebook ML.
- Lyndbrook is the operational/KPI analog: EPA/MassGIS → PWSID entity database + Review Velocity 800→280 at 35% precision. Vylet carries injection-safe SQL freshness/validation and a Dockerized LangGraph pipeline (30x) with Redis/Celery. CaseStudyPrep is the S3 half of inventory AWS (flat-file / object-store analog). SignalWeaver is FastAPI serve + React/TypeScript dashboard persisted to Postgres — reporting analog, not LoRA, not Power BI.
- Binding ding: none. SQL and Python are through use. No invented Snowflake, dbt, Alteryx, Azure Data Factory, Informatica, Power BI, Tableau, or Power Query.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML if the reader never reaches the FastAPI serve + Postgres persist + dashboard lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape and Dockerized pipeline lines.
- CaseStudyPrep’s Voice AI title can file as audio product work if the reader never reaches the S3 presigned-URL line.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular Excel filings and sole-engineer MCFN delivery on EC2 (documentation / non-technical stakeholder analog); Vylet injection-safe SQL freshness / re-scrape plus the Dockerized LangGraph pipeline (30x, Redis/Celery); Lyndbrook PWSID entity DB + Review Velocity (800 → 280) as messy operational data → tables / KPI analog; SignalWeaver FastAPI scores + React/TypeScript dashboard persisted to Postgres as the reporting analog — not Power BI
- **Defend:** Snowflake, dbt, Alteryx, Azure Data Factory, Informatica, Power BI, Tableau, and Power Query are tools they may *gain* — do not claim prior use. Say Python/SQL/Pandas/Postgres/AWS EC2/S3/Docker/Git and ramp on NA Ops warehouse/BI tooling. SQL on the page is freshness/validation, not a star-schema transform. Excel on this page is irregular exports ingested in Pandas, not Power Query. This is Workday **J2465581** NA Ops Data Engineering Intern, not Finance DE and not Enterprise Solutions Intern. CaseStudyPrep is S3 reliability, not the DE spine. Skip LoRA / ML-research framing.
- **Depth prep:** Recruiter/HR (enrollment, St. Petersburg Summer 2027 availability) then 1–2 interviews (project walk + STAR; Glassdoor intern ~30 min **[directional, Extern]**). Intern OA unpublished — do not invent HackerRank/CodeSignal. Walk one ingest → ETL → serve path (MDC) and one SQL/quality + container path (Vylet DAL + Docker). Confirm St. Pete relocate. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — Eligible CS student with applied SQL/Python pipeline spine on a resume-first C-tier DE intern req; GPA 3.66 on the page; no eligibility miss
- **Overall hire odds:** High — C-tier ~15–25% with resume as the bottleneck (`companies.md` peer of Howmet / CAI / Gulfstream intern). Residual risk is St. Petersburg relocate and a recruiter screen, not a published coding OA
- **Funnel filters:** Workday resume → recruiter/HR → 1–2 interviews · intern OA unpublished · no intern sys design · Bottleneck: resume + St. Pete relocate · ~15–25% (`companies.md` Jabil). Comp unlisted on this req (Extern intern band $16–$32/hr **[directional]**). This JD does not print dates or onsite vs remote; sibling St. Pete intern is onsite May 17 – August 6, 2027; US summer cohort is 12 weeks.
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-23). No Jabil contact in `network.md`. Confirm St. Pete onsite for the summer. Form email `verdent06@gmail.com`. Behavioral is a filter (`recruiting.md` §6)
