# Data Engineering Intern - Summer 2027 at POET

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — Currently pursuing B.S. Computer Science (JD: CS / IS / Data Science / Engineering / related); Expected May 2028 vs Summer 2027 intern; JD has no class-year, GPA, or visa gate; official intern FAQ is freshman–senior and legally entitled to work in the US
- **Track:** ai-ml
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings (Excel exports) → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation / PAC ranking → Flask REST on AWS EC2. Ingest → transform → serve for a Sioux Falls Data Engineering intern, not Process Engineering and not notebook ML.
- Lyndbrook is the multi-source / quality analog: EPA/MassGIS → PWSID entity database + Review Velocity 800→280 at 35% precision. Vylet carries injection-safe SQL freshness/validation, a Dockerized LangGraph pipeline (30x, Redis/Celery), and a data-quality defect (79% → 89%). SignalWeaver is FastAPI serve + Docker Compose (API + Postgres) — orchestration analog, not LoRA, not Tableau.
- Binding ding: none. SQL and Python are through use. No invented PowerShell, C#, Java, Snowflake, Databricks, or Tableau.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML if the reader never reaches the FastAPI serve + Docker Compose lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape, Dockerized pipeline, and 79%→89% quality lines.
- Lyndbrook’s water-utility domain can file as finance/PE if the reader never reaches the EPA/MassGIS entity table and precision filter.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular Excel filings and sole-engineer MCFN delivery on EC2 (automation + stakeholder analog); Vylet injection-safe SQL freshness / re-scrape plus the Dockerized LangGraph pipeline (30x, Redis/Celery) and the 79%→89% name-collision quality fix; Lyndbrook PWSID entity DB + Review Velocity (800 → 280) as messy operational data → tables / quality analog
- **Defend:** PowerShell, C#, Java, Snowflake, Databricks, and Tableau are tools they may *gain* — do not claim prior use. Say Python/SQL/Pandas/Postgres/AWS EC2/Docker/Git and ramp on POET’s plant-sensor / commodity / logistics stack. SQL on the page is freshness/validation, not a star-schema transform. Excel on this page is irregular exports ingested in Pandas, not Microsoft Office-as-a-skill. This is Workday **R101787** Data Engineering Intern, not Process Engineering Intern **R101679**, not Research Intern **R101732**, not Finance Intern **R101668**. Skip LoRA / ML-research framing.
- **Depth prep:** Recruiter or hiring-manager **phone** (official intern FAQ: fall review, phone interview, offers by year-end) then STAR. Intern OA unpublished — do not invent HackerRank/CodeSignal. Walk one ingest → ETL → serve path (MDC) and one SQL/quality + container path (Vylet DAL + Docker). Confirm Sioux Falls onsite for mid-May through August (10–12 weeks). Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — Eligible CS student with applied SQL/Python pipeline spine on a resume-first C-tier DE intern req; GPA 3.66 on the page; no eligibility miss
- **Overall hire odds:** High — C-tier ~15–25% with resume as the bottleneck (`companies.md` peer of Jabil DE / CHS DA / Gulfstream intern). Residual risk is Sioux Falls relocate and a recruiter phone screen, not a published coding OA
- **Funnel filters:** Workday resume → recruiter/HM phone · intern OA unpublished · no intern sys design · Bottleneck: resume + Sioux Falls onsite relocate · ~15–25% (`companies.md` POET). Comp unlisted (C-tier $22–38/hr band). Selected by **November 1**. Term **10–12 weeks** from mid- to late May
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-30; selected by November 1; campus listing expires 2027-01-01). No POET contact in `network.md`. Confirm Sioux Falls onsite. Form email `verdent06@gmail.com`. Behavioral is a filter (`recruiting.md` §6)
