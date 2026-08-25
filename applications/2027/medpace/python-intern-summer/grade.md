# Python Intern - Summer 2027 at Medpace

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — Expected May 2028 + Summer 2027 = rising senior; JD asks rising junior or senior; B.S. Computer Science and Economics is a related degree
- **Track:** full-stack + enterprise BI / CRO data products (APIs + ingestion pipelines + SQL at a clinical CRO)
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → Flask REST on AWS EC2. Ingest → transform → serve, not Jupyter and not the 12922 validation/test-case co-op.
- Vylet in the lead window carries a Dockerized LangGraph pipeline (30x), injection-safe SQL freshness/re-scrape, and a named quality fix (79%→89%) — maintainable Python services plus SQL, not a notebook intern.
- SignalWeaver + Lyndbrook close the BI analog: FastAPI REST + React dashboard + Postgres + GitHub Actions/pytest, and EPA/MassGIS entity resolution with 800→280 scoring at 35% precision. Binding ding: none.

### Demerits

No demerits — clean screen.

### Misreads

- A PE/search-fund founder tagline on Vylet can file as startup SaaS if the reader never reaches the SQL DAL / re-scrape and 79→89% quality lines.
- SignalWeaver’s financial-research descriptor can read as notebook ML; the on-page work is FastAPI serve + dashboard + Docker/CI.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL and sole-engineer Flask REST on EC2; Vylet injection-safe SQL freshness / re-scrape plus the 79→89% name-collision fix and Dockerized LangGraph pipeline (30x); Lyndbrook PWSID entity DB + Review Velocity (800 → 280 at 35%); SignalWeaver FastAPI + Postgres persist + GitHub Actions/pytest
- **Defend:** No Azure, Terraform, Bicep, ARM, MCP servers, LangChain, Copilot, Java, Spring, Node, Snowflake, Databricks, Tableau, Fusion, Sentry, chemistry-lab, or CRO domain internship — pluses, not gates; say Python/SQL/Pandas/Postgres/Flask/FastAPI and ramp on their stack. Flask API line has no QPS/latency — walk the 5-month sole-engineer MCFN contract. SignalWeaver 9.1s p50 is batch research latency, not an interactive serving SLA. Do not claim day-one ownership of Medpace enterprise BI platforms. LangGraph is on the page; do not relabel it LangChain.
- **Depth prep:** Verbal Python/SQL + project walkthrough (`company.md`; no standard LeetCode OA). Walk one ingest → ETL → serve path (MDC) and one quality/freshness path (Vylet DAL + name-collision). pytest/GitHub Actions on SignalWeaver. STAR for cross-functional translation (MDC/MCFN researchers). Behavioral is a filter (`recruiting.md` §6). Confirm fully office-based Cincinnati Summer 2027 — logistics knockout.

## Likelihood

- **Resume screen:** High — one-page Python/SQL/API/ingestion page with class year, GPA 3.66, Flask REST, FastAPI, Pandas ETL, injection-safe SQL, GitHub Actions CI; C-tier resume bottleneck should not bounce this
- **Overall hire odds:** Medium — C-tier ~15–25% with resume as the intern gate; this page clears the screen, then recruiter phone (Cincinnati onsite Summer 2027, class standing, Python/SQL) and a verbal project/SQL walkthrough still eliminate. Remaining risk is onsite logistics and talking the systems without CRO-domain invention
- **Funnel filters:** iCIMS resume (bottleneck) → recruiter phone → verbal Python/SQL + project walkthrough + behavioral · 2–3 rds · Easy · no standard LeetCode OA · no intern sys design · ~15–25% · fully office-based Cincinnati Summer 2027
- **Outside the resume:** Apply in the first-wave iCIMS window. Timed Python/SQL walkthrough of MDC ingest→serve and Vylet DAL/quality. Confirm Cincinnati onsite Summer 2027 on the form. No Medpace contact assumed — a Cincinnati/UMich alum in Analytics & BI still beats cold apply
