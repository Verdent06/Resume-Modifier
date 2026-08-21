# 2027 Blackstone Data Engineer Summer Analyst at Blackstone

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside JD window Fall 2027–Spring 2028; currently enrolled undergraduate; GPA 3.66 and month/year on the page; PDF
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST API on AWS EC2. Ingest → transform → serve for BXTI data engineering, not SWE 45021 and not Data Science.
- Vylet carries SQL freshness (asyncpg timestamp validation / re-scrape) plus a Dockerized LangGraph pipeline (30x). Lyndbrook is multi-source entity resolution and an 800→280 scoring closer — search-fund data work next to alt-AM.
- Binding dings are both minor: CaseStudyPrep is a one-line Voice AI / S3 upload co-op, and SQL is a DAL/freshness beat rather than a warehouse transform.

### Demerits

- **minor** · `CaseStudyPrep.AI` · single-bullet Voice AI, not a pipeline — Experience slot is a Voice AI co-op whose only bullet is S3 audio-upload retries; no ETL/ELT, SQL, Pandas, or data model
- **minor** · `Vylet` · SQL is freshness/DAL not a transform — required SQL appears as asyncpg timestamp validation that triggers re-scrapes, not a warehouse-style query, qualify, or persist step

### Misreads

- A skim that stops on CaseStudyPrep's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL and Vylet SQL/Docker pipeline the BXTI screen wants.
- Vylet's PE/search-fund founder tagline can read as startup SaaS rather than a closed-loop data pipeline with a SQL DAL.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the Dockerized LangGraph pipeline (30x); Lyndbrook PWSID entity DB + Review Velocity (800 → 280)
- **Defend:** SQL is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next *(out of rails: only SQL bullet in the pool; llm-apis swap cannot bridge a SQL transform)*. CaseStudyPrep is S3 retry logic from a voice-AI co-op, not a BXTI pipeline *(out of rails: pool is VAD / S3 / Web Workers; loop cannot omit this Experience entry)*. Do not claim Snowflake, Prefect, Terraform, Gitlab, RDS, ECS, or Lambda
- **Depth prep:** HackerRank Python/SQL Easy–Med (BXTI candidate-reported; bottleneck is resume + fit then OA). Walk one ingest → transform → serve path (MDC) and one SQL-quality path (Vylet DAL). STAR for entrepreneurial/self-starting (Vylet founder, MDC sole engineer). Behavioral is a filter (`recruiting.md` §6). Light intern sys design on the tech video / Superday

## Likelihood

- **Resume screen:** High — pipeline/ETL/AWS-Docker page for a resume-gated BXTI data-engineer intern; eligible class year, GPA, Python/SQL through use
- **Overall hire odds:** Medium — B-TIER ~5–8%; screen is a hard gate and this page clears it, then HackerRank Python/SQL Easy–Med, tech video, and Superday still eliminate. Remaining risk is the OA, Superday fit, Miami onsite, and defending AWS limited to EC2/S3
- **Funnel filters:** Workday campus resume (bottleneck: resume + fit) → recruiter/video screen → HackerRank (Python/SQL Easy–Med) → tech video → Superday; light intern sys design. Not the PE HireVue/LBO funnel. Comp $125k annualized; Miami onsite; start June 2027; req 45022
- **Outside the resume:** Apply in this first-wave window (posted 2026-08-21); timed HackerRank Python/SQL; a BXTI/alumni referral if available; 2–3 entrepreneurial STAR stories for the behavioral filter (`recruiting.md` §4, §6)
