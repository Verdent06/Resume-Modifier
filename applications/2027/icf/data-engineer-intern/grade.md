# 2027 Summer Intern, Data Engineer (Reston, VA or Remote) at ICF International

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** Eligible — 96 college credits by Summer 2027 vs **30**-credit floor in CS/related. Pursuing B.S. Computer Science (related field). Expected May 2028; Summer 2027 is after sophomore year / Junior. US citizen (federal-contract citizenship / permanent work-auth). No GPA floor; **3.7** is a plus. Master's enrollment is **Preferred**, not Basic. No in-hand clearance required. Official Workday CXS `canApply: true` (posted 2026-10-07).
- **Track:** ai-ml + consulting / client-facing data delivery
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular filings → Requests+Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask REST on AWS EC2, scoped with a nonprofit stakeholder. Ingest → transform → serve for a Data Engineer intern, not Software Developer **R2603002** and not notebook ML.
- Lyndbrook is a multi-source PWSID entity database plus 800→280 scoring (consulting analog in the lead window). Vylet carries injection-safe SQL freshness / re-scrape, a Dockerized LangGraph pipeline (30x, Redis/Celery), and a 79%→89% name-collision RCA. SignalWeaver is FastAPI scores plus 49ms pgvector retrieval.
- Binding dings are minor: preferred Databricks / Snowflake / Spark / Java / Scala are absent, and SQL is a DAL freshness beat rather than a warehouse transform.

### Demerits

- **minor** · `resume` · preferred warehouse stack and Java/Scala absent — Preferred quals name Databricks, Snowflake, Spark, Java, or Scala as exposure. The page demonstrates Python, SQL, Pandas ETL, AWS EC2, and Docker with zero Spark / Databricks / Snowflake / Java / Scala in bullets or Skills.
- **minor** · `Vylet` · SQL is freshness/DAL not a warehouse transform — Required SQL appears as asyncpg timestamp validation that triggers re-scrapes, not a query-tune, qualify, or warehouse transform on large-scale datasets.

### Misreads

- A screener hunting Spark / Databricks / Snowflake on a keyword pass could file this as a Python product intern and miss the ETL + quality + stakeholder delivery.
- Vylet's LangGraph line can read as an AI-research resume if the skimmer never reaches the Flask REST + Pandas ETL bullets. It is a Dockerized pipeline on a live product, not a LoRA paper.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); Vylet injection-safe SQL freshness / re-scrape plus the Dockerized pipeline (30x) and 79%→89% defect fix; SignalWeaver FastAPI + 49ms pgvector search.
- **Defend:** No Java, Scala, Databricks, Snowflake, Spark, Azure, or GCP in the pool — say so, then map Pandas ETL + SQL DAL + AWS/Docker onto "or similar." Do not check those boxes. SQL is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next. LangGraph is pipeline infra, not an ML-research lead. This is **R2603380**, not Software Developer **R2603002**. Reston *or* remote June–August with no housing stipend is a yes, not a skip. *(out of rails: pool has no Java / Scala / Databricks / Snowflake / Spark bullet; only SQL bullet is Vylet freshness; swap sets cannot bridge)*
- **Depth prep:** Walk the MCFN ETL edge cases and API contract; PWSID entity resolution; SQL timestamp validation / re-scrape; 79%→89% name-collision bug. Timed SQL (joins, aggregations) if a live screen appears — intern OA unpublished. STAR for stakeholder communication. **No AI-assisted interview answers** unless ICF grants an accommodation (`candidateaccommodation@icf.com`).

## Likelihood

- **Resume screen:** High — one-page DE spine with Python/SQL through use, client-scoped ETL, quality RCA, live GitHub, 3.7 GPA. Remaining dings are preferred warehouse stack and SQL flavor, not absence.
- **Overall hire odds:** Medium — ICF intern loops are Easy and resume-weighted (`companies.md` C-tier ~20–30%; `recruiting.md` mid-size / non-tech-tech). Clearing the PDF is most of the front end; a recruiter still eliminates if they want day-one Spark/Databricks, if they prefer a master's (preferred only), or if Reston/remote logistics fail.
- **Funnel filters:** Workday ATS **R2603380**. No published intern OA. Recruiter → unpublished Easy tech/project + behavioral (FT analog). US citizenship / work-auth knockout (met). 30-credit floor (met). Posted 2026-10-07. Reston (VA30) or Nationwide Remote (US99); no housing/relocation.
- **Outside the resume:** Apply **on Workday this week** — JD says bot/third-party applications may be excluded. No ICF contact in `network.md`. See `written-answers.md`.
