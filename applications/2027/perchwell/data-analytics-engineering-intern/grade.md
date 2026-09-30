# Data Analytics Engineering Intern at Perchwell

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027 term = rising senior; JD wants rising seniors in CS/STEM; US citizen / authorized, no sponsorship needed
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), a PAC ranking aggregation, and a production Flask REST API on AWS EC2 shipped to MCFN — ingest → transform → reporting, not the Rails/React SWE twin and not ML-research.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision) is the messy-source → usable analog; SignalWeaver closes on a React/Postgres dashboard, then FastAPI-served scores.
- Binding dings: the only SQL-through-use proof is an unquantified asyncpg freshness DAL, and Experience slot 4 is a Voice AI co-op.

### Demerits

- **minor** · `Vylet` · SQL/DAL is freshness plumbing not query/aggregate SQL — The only SQL-through-use line is asyncpg timestamp validation and re-scrapes; it never shows a join, aggregation, or CTE producing a metric. A Data Analytics Engineering screen treats RDBMS SQL as the floor and this reads as database plumbing with no sized freshness win.
- **minor** · `CaseStudyPrep.AI` · voice-AI product framing in last Experience slot — Fourth Experience is a Voice AI co-op whose only bullet is expired-S3 WAV upload recovery. Real production number, but this req screens ingest/profile → warehouse analog → dashboards, and a rushed reader buckets the page as a product-SWE intern on the wrong twin.

### Misreads

- A keyword-first pass for dbt / Snowflake / Looker / Tableau can bucket this as "no analytics-engineering stack" even though Pandas ETL, PAC rankings, a scored shortlist, and a React/Postgres dashboard are on the page.
- The SQL/DAL line can read as database plumbing rather than the RDBMS floor this JD names (joins, aggregations, CTEs), because it never sizes the freshness win and never shows a query.
- A rushed screener may bucket CaseStudyPrep.AI as a product-SWE intern applying to the Software Engineering Intern twin and miss the 27% upload-failure quality analog.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC rankings shipped to MCFN on EC2) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the profile-new-source → transform → intelligence loop this seat tests; SignalWeaver React dashboard if they ask for BI; Vylet Dockerized 30x pipeline and stale-timestamp re-scrape if they ask for warehouse tests / data quality
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN/CTE that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; CaseStudyPrep is a Voice AI co-op kept for a production-quality number, not a listings-data story *(out of rails: every CSP pool bullet is voice-AI; no fifth on-axis data Experience to swap in; anti-deletion blocked omit)*; no dbt, Snowflake, Redshift, BigQuery, Looker, Tableau, Mode, Metabase — walk React/Postgres and Pandas ETL instead of inventing them *(out of rails: those tools are not in inventory or swap sets)*; this is Data Analytics Engineering, not the Software Engineering Intern twin
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as "instinct when a number looks wrong"; SignalWeaver dashboard as the intelligence-layer analog. Intern OA unpublished — do not assume HackerRank/CodeSignal; expect SQL fluency (joins/aggregations/CTEs live), a project deep-dive, and STAR. SoHo 5 days/week Jun 7–Aug 13 2027

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is messy-source ETL → PAC rankings → scored shortlist → dashboard, which is this req's screen
- **Overall hire odds:** Medium — Perchwell is a C-tier analog with a resume bottleneck (~15–25%) and no published intern OA, so this page should clear the binding human Ashby read; the remaining cut is 5-day SoHo onsite for Jun 7–Aug 13, defending SQL fluency beyond asyncpg, and not being mistaken for the SWE intern twin
- **Funnel filters:** Ashby **`9d34fc9d-e235-44fc-bdf9-42e75223839a`** + human resume screen (posted 2026-09-29; deadline 2026-10-18 11pm ET; offers by 2026-11-25) → unpublished intern loop. Intern OA unpublished — do not invent HackerRank/CodeSignal. No intern sys design. Bottleneck: resume · ~15–25% (C-tier analog of Ibotta / Fable / early SaaS). US work auth only. Rising senior / STEM.
- **Outside the resume:** Apply before Oct 18 2026 11pm ET (first wave; posted 2026-09-29). Prep joins/CTEs and one messy-source walkthrough. Packet only — do not submit the Ashby form from this run.
