# Data Analytics Engineering Intern at Perchwell

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid Summer 2027 **Data Analytics Engineering Intern** (Ashby **`9d34fc9d-e235-44fc-bdf9-42e75223839a`**) at Perchwell, SoHo HQ (**110 Greene Street**). **Full-time, 5 days/week onsite**, New York Office. Term **June 7 – August 13, 2027** (10 weeks). Comp **$12,000 for 10 weeks** (minus taxes) — ~$30/hr. Posted **2026-09-29**. Application deadline **2026-10-18 11:00 PM ET**. Offers by **2026-11-25**. **US work authorization required**; JD: only considering candidates authorized to work in the U.S.

**This is Data Analytics Engineering — not the Software Engineering Intern twin** (same dates/location; Rails/TypeScript/React web app). Do not import a product-SWE spine.

The intern sits on the **Data Analytics Engineering** team that owns what happens after a new MLS client lands: understand what is actually in that data, transform it into the warehouse, and build the intelligence layer on top. Day-to-day: profile ingested data for new MLS clients and partner with engineering to onboard into standard reporting; extend dbt models that transform raw MLS data (tests + documentation); strengthen metric definitions, semantic models, and dashboards for internal teams and customers; own a summer project (profiling/mapping a new **non-MLS** data source is a named candidate); collaborate with analytics engineers, data engineers, PMs, and customer-facing teams; ship scalable solutions from broadly defined problems into production. Dedicated 1:1 analytics-engineer mentor. End-of-summer presentation to executive and data teams.

JD surface is **applied analytics engineering / data-pipeline work** — SQL/RDBMS, ingest/profile → transform (warehouse) → metrics/semantic models/dashboards. Company identity (`company.md`) is **proptech / MLS listings-data infrastructure** (SaaS listings platform; REBNY RLS operator; each new MLS is a new data source). Domain flavor inside `ai-ml`, not a second engineering track.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** proptech / MLS listings-data infrastructure (SaaS listings platform)
- **track_divergence:** false

Required: rising seniors in CS, data science, statistics, or other STEM; working familiarity with RDBMS and SQL (joins, aggregations, CTEs); curiosity about where data comes from; attention to detail / instinct when a number looks wrong; strong communication and problem solving; excitement to learn. Window functions not required. Preferred: cloud warehouse (Redshift, Snowflake, or BigQuery); dbt or another transformation framework; Python for data (pandas); Git; BI tool (Looker, Tableau, Mode, or Metabase); a project taking messy source data and making it usable; college leadership.

What the posting *literally tests* is SQL/RDBMS plus ingest/profile → transform (dbt/warehouse) → metrics/semantic models/dashboards. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data/ML workflow: ingest → transform → insight/KPI or score → measured outcome, not `model.fit()` alone) and `recruiting.md` Part III §13 (applied ML / data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as analog applied-analytics intern reqs (DICK'S DA&E, Zipline IQME DA, Citizens DE, NXP DAE). Stay **applied Python+SQL / ETL / warehouse analog / dashboards** — not research scientist, not generic SWE.

It is **not** `full-stack`: title is Data Analytics Engineering Intern; the sibling SWE intern is a different Ashby req. Not `dev-ops` (Git/Docker are supporting hygiene). Not `robotics`. Not ML research.

Company identity is **domain** (residential listings / MLS data), not a different engineering track, so `track_divergence` is false. Spine stays SQL + ingest → transform → metrics/dashboards. Do not optimize as generic product-SWE. Do not lead with LoRA / notebook modeling or Rails/React feature work. Do not invent dbt, Snowflake, Redshift, BigQuery, Looker, Tableau, Mode, Metabase, MLS internships, or real-estate internships. Python is a plus, not a required-language gate beyond SQL — but Python is in inventory and should appear through use. Honest analogs: Python + SQL/PostgreSQL/asyncpg + Pandas ETL + Flask/React dashboard + Docker/Git.

## Team & Bar

Perchwell is **C-TIER analog** (`companies.md` has no row; peer of Ibotta / Fable / early SaaS). Recruiter voice: a SoHo analytics-engineering hiring manager or Ashby campus screen scanning for an eligible **rising senior** in CS/STEM who can write SQL (joins/aggregations/CTEs), profile messy source data without claiming they already ran an MLS warehouse, and notice when a number looks wrong — not a Rails/React SWE intern, not a research scientist, not someone claiming dbt/Snowflake/Looker they cannot defend.

**Process (doctrine + `company.md`):**
- Front door is Ashby + human resume screen (`recruiting.md` Part I: startups/mid-size, a human reads the PDF early; Ashby analog to Greenhouse/Lever resume-first). Apply in the first wave (`recruiting.md` Part II intern). Deadline Oct 18 2026 11pm ET; posted 2026-09-29; offers by Nov 25 2026.
- Intern OA unpublished — do **not** invent HackerRank/CodeSignal.
- FT SWE analog **[directional, Dataford]:** HR screen → coding / sys-design / behavioral → stakeholders; ~3 rounds / 3–5 weeks. Not confirmed for this intern. No intern sys design published.
- Eligibility knockouts first: rising senior in listed majors; **US work auth / no sponsorship**. Class-year on the page: `Expected May 2028` vs Summer 2027 term = rising senior. US citizen / authorized clears the visa gate.
- Bottleneck: **resume**. Acceptance ~15–25% directional C-tier peer of Ibotta / Fable / early SaaS.

Winning *kinds* of evidence: SQL demonstrated through use in bullets, not Skills alone (`resume.md` keyword-through-use); Python/Pandas ETL as the honest transform analog (dbt named on JD — do not invent it); end-to-end ingest/profile messy or multi-source data → transform/validate → metric, ranking, or dashboard → measured outcome (`resume.md` §14; `recruiting.md` §13); data-quality instinct (caught a wrong number, stale record, or failed join before it hit a report); Git / Docker as version-control and shipping hygiene; a real dashboard or reporting UI already in inventory (React/report UIs count — do not invent Looker/Tableau/Mode/Metabase); stakeholder-facing delivery (PMs, customer-facing analog). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Math/stats/econ coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Dual CS + Economics is on-axis. Skip ML-research framing. Named JD warehouse/BI/dbt tools not evidenced in real work stay off the page.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- SQL and RDBMS demonstrated through use in bullets (joins, aggregations, CTEs as the JD floor — honest PostgreSQL/asyncpg analog is enough; do not invent window functions, dbt tests, or a warehouse brand). Skills-only SQL fails.
- Python/Pandas through use as the transformation analog — preferred on the JD, in inventory, should appear inside real ETL, not only Skills.
- End-to-end applied-analytics workflow: messy or new source data → profile/ingest/merge → transform/normalize/aggregate → metric, score, ranking, or dashboard → measured outcome. Analog to "profile ingested data → extend warehouse models → intelligence layer" without claiming MLS or dbt.
- Data-quality analog: catching a wrong number, stale timestamp, name collision, or bad record before it hits a report — the JD's "instinct when a number looks wrong."
- Visualizations / dashboards / ranked reports as a first-class artifact — analog to Looker/Tableau/Mode/Metabase without inventing those tools.
- Messy-source → usable analog (preferred): irregular exports, multi-source joins, entity resolution, or a new feed made reportable.
- Git through use or inventory; Docker/AWS as supporting production hygiene — not the lead story.
- Quantitative coursework (stats, calc, econ) visible in Education; GPA on the page; class-year `Expected May 2028`.
- College-leadership analog is preferred color (founder/owner, sole-engineer contract), not a second track.

**Anti-patterns:**
- Generic SWE / full-stack product resume (Rails, React feature work, voice-AI as the lead) that never shows SQL, pipelines, KPIs, data quality, or a viz/report analog — that is the SWE intern twin, wrong req.
- ML-research / LoRA-as-lead / notebook `model.fit()` with no delivery, no pipeline, no measured operational outcome.
- Voice-AI, audio-DSP, or embedded C++ as the **lead** with no analytics analog.
- Skills-only SQL/Python/dbt/Snowflake/Looker with no bullet proof.
- Invented dbt, Snowflake, Redshift, BigQuery, Looker, Tableau, Mode, Metabase, MLS internships, or real-estate internships (`resume.md` §8 fabrication smell).
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Treating this as a software-engineer intern screen (OA-first, systems-design, generic SWE keywords).
- Keyword-stuffing "MLS / proptech / listings" into bullets that are not about that work.

## ATS Keywords

SQL, RDBMS, joins, aggregations, CTEs, Python, Pandas, ETL, data warehouse, data quality, metrics, dashboards, PostgreSQL, Git, analytics engineering, semantic models, data pipelines
