# Intern - Data Engineer at Acxiom

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** ineligible — JD anticipates May 2027–December 2027 grads; candidate Expected May 2028 (Winter OK override: packet shipped anyway; PDF date unchanged)
- **Track:** ai-ml
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation / normalize → Flask REST on AWS EC2. Ingest → transform → serve for an Intern - Data Engineer, not Data Scientist intern JR014459 and not generic SWE.
- Lyndbrook is the multi-source / identity analog: EPA/MassGIS → PWSID entity database + Review Velocity 800→280 at 35% precision. Vylet carries injection-safe SQL freshness/validation, a 79→89% name-collision quality fix, and a Dockerized LangGraph pipeline (30x, Redis/Celery). SignalWeaver is FastAPI serve (9.1s p50 / 15.2s p99) plus Docker Compose + GitHub Actions CI — Git/CI/CD analog, not LoRA.
- Binding ding: none on the page. Python and SQL are through use. No invented Snowflake, Databricks, Tableau, Kubernetes, Spark, Airflow, dbt, Kafka, or BigQuery. Separate knockout: Expected May 2028 vs printed May–Dec 2027 window.

### Demerits

No demerits — clean screen.

### Misreads

- SignalWeaver’s financial-research descriptor can file as notebook ML or the Data Scientist intern sibling if the reader never reaches the FastAPI serve + Docker Compose + GitHub Actions lines.
- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape, 79→89% quality, and Dockerized pipeline lines.
- Workday / keyword-first ATS may miss Databricks / Snowflake / Spark / Airflow that this PDF honestly does not name.
- A recruiter who only reads Education will bucket this as a grad-window miss before the DE spine registers.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the 79→89% quality fix and Dockerized LangGraph pipeline (30x, Redis/Celery); Lyndbrook PWSID entity DB + Review Velocity (800 → 280) as the identity-resolution analog; SignalWeaver FastAPI scores + Docker Compose / GitHub Actions as the serve + CI/CD analog
- **Defend:** Grad window — Expected May 2028 vs JD May–Dec 2027; junior year, returns after a part-time winter term, user said Winter OK; do not rewrite the PDF date. No Databricks, Snowflake, Spark, Airflow, dbt, Kafka, BigQuery, K8s, or Tableau — say Python/SQL/Pandas/Postgres/AWS EC2/S3/Docker/Git and ramp on their lakehouse. SQL on the page is freshness/validation, not a production warehouse transform — walk the asyncpg DAL. No customer-identity internship — analog is messy multi-source entity data (MDC/Lyndbrook), not Audience Cloud / Real ID production. Do not claim day-one ownership of identity graphs. Skip LoRA / ML-research framing (that is JR014459). Agent/LLM is supporting (LangGraph / embeddings), not the spine. Remote/Homebased this req — do not volunteer Conway onsite (that was the Summer 2026 twin).
- **Depth prep:** Unpublished intern loop — recruiter + technical 1:1/panel, ~2 rounds, ~2–4 weeks (`company.md`; Dataford FT SWE analog). Intern OA unpublished — do not invent HackerRank/CodeSignal; treat Easy–Med SQL/Python as possible. Walk one ingest → ETL → serve path (MDC) and one SQL/quality + container path (Vylet DAL + Docker). STAR for collaboration/documentation (`recruiting.md` §6). Privacy/PII curiosity without claiming GDPR/CCPA production programs.

## Likelihood

- **Resume screen:** Medium — on-axis DE page for a resume-gated C-tier intern; Workday can still auto-reject on the May 2028 vs May–Dec 2027 window before bullets
- **Overall hire odds:** Low — even with a Winter OK waiver, unpublished intern OA plus a practical SQL/Python loop still eliminate most of a ~15–25% C-tier funnel; preferred lakehouse tools are honestly absent
- **Funnel filters:** Workday (`acxiomllc` / AcxiomUSA) resume → recruiter → technical 1:1/panel · ~2 rounds · ~2–4 weeks **[directional, Dataford FT SWE analog]** · intern OA unpublished · no intern sys design · Bottleneck: resume + printed grad-window knockout · ~15–25% **[directional, C-tier peer of Ibotta / Audax DE]** (`company.md`). Start Jan 11 2027; 20–25 h/wk semester / up to 40 h/wk breaks; CXS Remote/Homebased (not the Summer 2026 Conway onsite twin). Comp unlisted. Not JR014459.
- **Outside the resume:** Apply in this first-wave Workday window (posted 2026-09-15). No Acxiom contact in `network.md` — do not pick Employee Referral. Script one honest sentence on the May 2028 date vs the printed window. Prep a Python/SQL pipeline walkthrough. Do not invent Databricks/Snowflake on a screen call.
