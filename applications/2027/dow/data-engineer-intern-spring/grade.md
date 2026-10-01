# Data Engineer / Data Platform Engineer Intern — Spring 2027 at Dow Chemical Company

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** ineligible — JD Required: currently enrolled at the University of Illinois Urbana Champaign; candidate is enrolled at the University of Michigan (Expected May 2028). Years-to-grad (~15 months vs Spring 2027) would clear "within one to three years"; work-auth and CS field would clear
- **Track:** ai-ml
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings (Excel exports) → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation / PAC ranking → Flask REST on AWS EC2. Ingest → persist/curate → serve for an Enterprise Data & Analytics intern, not Midland SWE and not notebook ML.
- Vylet carries injection-safe SQL freshness/validation, a Dockerized pipeline (30x, Redis/Celery), and a data-quality defect (79% → 89%). Lyndbrook is the multi-source analog: EPA/MassGIS → PWSID entity database + Review Velocity 800→280 at 35% precision. SignalWeaver is FastAPI serve + Docker Compose (API + Postgres) + GitHub Actions — CI/platform analog, not LoRA, not Power BI.
- Binding ding is **off the page**: UIUC enrollment is a printed Must. Education says University of Michigan. A Champaign Delivery Center recruiter will no-pile on school before stack.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML if the reader never reaches the FastAPI serve + Docker Compose + GitHub Actions lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape, Dockerized pipeline, and 79%→89% quality lines.
- Education (UMich, Ann Arbor) will be read as a school-gate fail even when the pipeline spine matches the DE seat.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular Excel filings and sole-engineer MCFN delivery on EC2 (ingestion + stakeholder analog); Vylet injection-safe SQL freshness / re-scrape plus the Dockerized pipeline (30x, Redis/Celery) and the 79%→89% name-collision quality fix; Lyndbrook PWSID entity DB + Review Velocity (800 → 280) as messy multi-source persist analog
- **Defend:** Azure, ADF, Databricks, Snowflake, Scala, PowerShell, Terraform, Bicep, ARM, Entra, and Power BI are tools they may *gain* — do not claim prior use. Say Python/SQL/Pandas/Postgres/AWS EC2/Docker/Git and ramp on Dow’s Azure lakehouse. SQL on the page is freshness/validation, not a star-schema transform. **Do not claim UIUC enrollment.** This is Workday **R2068792** Delivery Center DE / Data Platform intern, not a Midland SWE intern. Skip LoRA / ML-research framing.
- **Depth prep:** Only relevant if they waive the UIUC Must (unlikely). Unpublished recruiter/HM walk + STAR. Intern OA unpublished — do not invent HackerRank/CodeSignal. Walk one ingest → ETL → serve path (MDC) and one SQL/quality + container/CI path (Vylet DAL + SignalWeaver Docker Compose / GHA). Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** Low — Page is a clean applied-DE spine, but the Required UIUC-enrollment line is a binary knockout (`recruiting.md` Part I §1)
- **Overall hire odds:** Low — C-tier ~20–30% **if eligible** (`companies.md` Dow / Plastipak). Residual risk is the school Must, then Champaign in-person 15–20 hrs/week with no housing, not a published coding OA
- **Funnel filters:** Workday resume + UIUC Must → unpublished Easy project walk + STAR · intern OA unpublished · no intern sys design · Bottleneck: **UIUC enrollment** then resume · close **2026-10-22** · **$26.25–$35.00/hr** bachelor's
- **Outside the resume:** Packet only. **Do not submit a Yes on UIUC enrollment.** Form email `verdent06@gmail.com`. No Dow contact in `network.md`. See `written-answers.md`
