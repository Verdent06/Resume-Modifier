# Summer 2027 Data Engineering Internship at Pacific Life

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — Currently enrolled B.S. Computer Science and Economics (JD lists both); Expected May 2028 vs Summer 2027 intern; JD has no class-year, GPA, citizenship, or visa gate
- **Track:** ai-ml
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings (Excel exports) → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation / PAC ranking → Flask REST on AWS EC2. Ingest → transform → serve for a Newport Beach Data Engineering intern, not the Actuarial intern and not notebook ML.
- Lyndbrook is the data-modeling analog: EPA/MassGIS → PWSID entity database + Review Velocity 800→280 at 35% precision. Vylet carries injection-safe SQL freshness/validation and a Dockerized LangGraph pipeline (30x) with Redis/Celery. CaseStudyPrep is the S3 half of inventory AWS. SignalWeaver is FastAPI serve + React/TypeScript dashboard persisted to Postgres — RDBMS + UX analog, not LoRA, not Tableau.
- Binding ding: none. Python, SQL, and Postgres are through use. No invented R, Salesforce, Alteryx, SAS, Tableau, MSSQL, or Kaggle.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML if the reader never reaches the FastAPI serve + Postgres persist + dashboard lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape and Dockerized pipeline lines.
- CaseStudyPrep’s Voice AI title can file as audio product work if the reader never reaches the S3 presigned-URL line.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular Excel filings and sole-engineer MCFN delivery on EC2 (stakeholder analog for actuarial/CX partners); Vylet injection-safe SQL freshness / re-scrape plus the Dockerized LangGraph pipeline (30x, Redis/Celery); Lyndbrook PWSID entity DB + Review Velocity (800 → 280) as data-modeling analog; SignalWeaver FastAPI scores + React/TypeScript dashboard persisted to Postgres as the reporting/UX analog — not Tableau
- **Defend:** R, Salesforce, Alteryx, SAS, Tableau, and MSSQL are tools they may *gain* — do not claim prior use. Say Python/SQL/Pandas/Postgres/AWS EC2/S3/Docker/Git and ramp on Pacific Life’s approved analytics stack. SQL on the page is freshness/validation, not a star-schema transform. This is Workday **R17828** Data Engineering Internship, not Actuarial intern and not Software Engineering intern. CaseStudyPrep is S3 reliability, not the DE spine. Skip LoRA / ML-research framing. Do not invent Kaggle.
- **Depth prep:** Early Careers recruiter (enrollment, Newport Beach Summer 2027, relocate from Northville — outside 50 miles so stipend applies) then 1–2 interviews (project walk + STAR; Glassdoor intern 2.8/5 **[directional, Extern]**). Intern OA unpublished — do not invent HackerRank/CodeSignal. Walk one ingest → ETL → serve path (MDC) and one SQL/quality + Postgres path (Vylet DAL + SignalWeaver persist). Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — Eligible CS + Economics student with applied Python/SQL pipeline spine on a resume-first C-tier DE intern req; GPA 3.66 on the page; no eligibility miss
- **Overall hire odds:** High — C-tier ~15–25% with resume as the bottleneck (`companies.md` peer of Northwestern Mutual ID&A / Transamerica DA / Nationwide intern). Residual risk is Newport Beach relocate and a recruiter screen, not a published coding OA
- **Funnel filters:** Workday resume → Early Careers recruiter → possible recorded video/assessment (Extern intern guide **[directional]**; not confirmed on this DE req) → 1–2 interviews · intern OA unpublished · no intern sys design · Bottleneck: resume + Newport Beach relocate · ~15–25% (`companies.md` Pacific Life). Comp **$25/hr** undergrad. Relocation stipend if outside 50 miles.
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-25). No Pacific Life contact in `network.md`. Confirm Newport Beach onsite for the summer. Form email `verdent06@gmail.com`. Behavioral is a filter (`recruiting.md` §6)
