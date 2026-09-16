# Data Engineering Intern (Summer 2027) at apexanalytix

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — currently pursuing B.S. CS + Economics (Expected May 2028); no class-year exclusive beyond currently pursuing bachelor's or higher; no GPA floor on this JD
- **Track:** ai-ml
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation / normalize → Flask REST on AWS EC2. Ingest → transform → serve for an Archimedes Data Engineering intern, not the Data Science Intern sibling and not generic SWE.
- Lyndbrook is the messy multi-source / entity analog: EPA/MassGIS → PWSID entity database + Review Velocity 800→280 at 35% precision. Vylet carries a Dockerized LangGraph pipeline (30x, Redis/Celery), injection-safe SQL freshness/validation, and a 79→89% name-collision quality fix. SignalWeaver is FastAPI serve (9.1s p50 / 15.2s p99) plus Docker Compose — containerized data app analog, not LoRA.
- Binding ding: none. Python and SQL are through use. Docker is through use. No invented Snowflake, Databricks, Tableau, Copilot, Fusion, Kubernetes-as-ops, or Streamlit.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML or the Data Science Intern sibling if the reader never reaches the FastAPI serve + Docker Compose lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape, 79→89% quality, and Dockerized pipeline lines.
- Rippling / keyword-first ATS may miss Kubernetes / Streamlit that this PDF honestly does not name.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet Dockerized LangGraph pipeline (30x, Redis/Celery) plus injection-safe SQL freshness / re-scrape and the 79→89% quality fix; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver FastAPI scores + Docker Compose as the containerized data-app analog
- **Defend:** No Kubernetes, Streamlit, Snowflake, Databricks, or Tableau — Docker is inventory and on the page; K8s/Streamlit are JD tools not in inventory — say Python/SQL/Pandas/Postgres/AWS EC2/S3/Docker and ramp on their cluster/UI. SQL on the page is freshness/validation, not a P2P warehouse transform — walk the asyncpg DAL. No procure-to-pay internship — the analog is messy multi-source entity data (MDC/Lyndbrook), not apeexportal production. Do not claim day-one ownership of Archimedes Kubernetes. Skip LoRA / ML-research framing (that is the Data Science Intern sibling). LLMs are supporting product-AI (LangGraph / embeddings), not the spine.
- **Depth prep:** Unpublished intern loop — project walk + STAR (`company.md`; intern OA unpublished — do not invent HackerRank/CodeSignal). Walk one ingest → ETL → serve path (MDC) and one SQL/quality + container path (Vylet DAL + Docker). STAR for stakeholder delivery (MDC/MCFN) and documentation to non-technical users. Behavioral is a filter (`recruiting.md` §6). Confirm Greensboro, NC onsite May–August 2027 on the form.

## Likelihood

- **Resume screen:** High — pipeline/ETL/SQL/Docker page for a resume-gated C-tier Data Engineering intern; eligible class year, GPA, Python/SQL through use
- **Overall hire odds:** Medium — C-tier ~15–25%; screen is the binding intern gate and this page clears it, then an unpublished project-walk loop and Greensboro May–August onsite still eliminate
- **Funnel filters:** Rippling ATS resume → unpublished intern loop (project walk + STAR) · intern OA unpublished · no intern sys design · Bottleneck: resume · ~15–25% (`companies.md` apexanalytix, peer of ENFOS / Innovative Systems). Comp unlisted (C-tier $22–38/hr band). Onsite Greensboro May–August 2027. R&D Archimedes. Not Data Science Intern, not Data Analyst Intern, not IT & Cloud Intern
- **Outside the resume:** Apply in this first-wave Rippling window. No apexanalytix contact in `network.md` — do not pick Employee Referral. Confirm Greensboro housing/logistics yourself (JD does not list relocation). Prep a Python/SQL pipeline walkthrough
