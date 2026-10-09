# Data Engineer Internship - 2027 (US) at Amazon

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside Oct 2027–Dec 2030; Summer 2027 leaves Fall 2027 + Winter 2028; US-enrolled B.S. CS; 18+
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST on AWS EC2. Ingest → transform → serve for a Data Engineer intern, not the SDE intern packet (10552937) and not notebook ML.
- Vylet carries injection-safe SQL freshness / re-scrape, a Dockerized LangGraph pipeline (30x, Redis/Celery), and a 79%→89% name-collision RCA. Lyndbrook is a PWSID entity database plus 800→280 scoring. SignalWeaver now opens on the React/Postgres dashboard.
- Binding ding is minor: SQL is a DAL/freshness beat rather than a warehouse transform or query-tune.

### Demerits

- **minor** · `Vylet` · SQL is freshness/DAL not a warehouse transform — required SQL appears as asyncpg timestamp validation that triggers re-scrapes, not a query-tune, qualify, or warehouse transform on large-scale datasets

### Misreads

- A skim that stops on Vylet’s PE/search-fund founder tagline can file this as startup SaaS and miss the SQL DAL / Dockerized pipeline the DE screen wants.
- SignalWeaver’s financial-research descriptor can file as notebook ML if the reader never reaches the dashboard / Postgres persist lines.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the Dockerized pipeline (30x) and 79%→89% defect fix; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver React/TypeScript dashboard persisted to Postgres
- **Defend:** SQL is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next *(out of rails: only SQL bullet in the pool; llm-apis swap cannot bridge a SQL transform)*. Do not claim Scala, KornShell, Hadoop, Spark, Tableau, QuickSight, Redshift, Glue, EMR, Lambda, or DynamoDB. LangGraph is pipeline infra, not an ML-research lead. This is Job **10553907**, not SDE **10552937** and not final-year **10496769**.
- **Depth prep:** Amazon DE intern OA is **not confirmed** as the SDE coding OA. Practice timed **SQL** (joins, aggregations, window functions) and **Python** data transformation; complete any Workstyles / Leadership Principles survey the email names. Loop **[directional]**: 1–2 virtual rounds mixing SQL, warehouse/ETL concepts, and LP STAR. No intern sys design (`companies.md`). Map stories to Ownership, Dive Deep, Bias for Action, Customer Obsession from MDC production API and Vylet pipeline RCA.

## Likelihood

- **Resume screen:** High — one-page DE spine with Python/SQL through use, conferral in window; remaining ding is SQL flavor, not SQL absence
- **Overall hire odds:** Medium — A-tier ~1–2% large class; resume is not the first elimination; SQL/Python OA plus LP loop still drop most of the intern class
- **Funnel filters:** amazon.jobs resume → OA (SQL/Python data work + LPs **[directional for DE; official OA page is SDE]**) · 1–2 rds · Bottleneck: **OA** · ~1–2% · in-person US DE intern sites · conferral Oct 2027–Dec 2030 + remaining term after internship · Seattle listed pay **$106,590**
- **Outside the resume:** Timed SQL + Python data-transform practice; LP Work Style consistency; apply in this first wave; Summer 2027 first, Winter 2027 OK, do not select Fall 2027; keep distinct from the SDE intern already in OA. See `written-answers.md`
