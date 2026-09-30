# Perchwell

Perchwell is the modern residential real-estate listings, data, and workflow platform for agents, brokerages, and MLS organizations — search, analytics, client collaboration, and admin tooling on one cloud-deployed stack rather than a stitched MLS-plus-point-solutions suite. Founded 2015 (Brendan Fairbanks) and headquartered in SoHo. Selected by the Real Estate Board of New York (REBNY) to operate the Residential Listing Service (RLS), NYC's de facto MLS; national expansion treats each new MLS as a new data source the analytics-engineering team must profile, warehouse, and instrument. **This packet is Data Analytics Engineering Intern only.** Do not mix with the Software Engineering Intern twin (same dates/location; Rails/TypeScript/React web app). Do not invent dbt, Snowflake, Redshift, BigQuery, Looker, Tableau, Mode, Metabase, MLS internships, or real-estate internships.

## Quick Facts

- **Tier:** C-TIER analog (`reference/companies.md` has no Perchwell row). Peer of Ibotta / Fable / early SaaS — startup SaaS, modest intern comp, resume-first Ashby
- **HQ / offices:** 110 Greene Street Suite 801, New York, NY 10012 (SoHo). This intern: **New York Office, 5 days/week onsite**
- **Valuation / signal:** Series A **$15M** Dec 2021 (Founders Fund lead; Lux Capital, Matterport, CRMLS). Series B **$25M** ~Jul 2024 (Lux Capital lead; Starwood, Flex Capital, Stellar MLS, REcolorado, CRMLS). Total ~**$40–44M**. Reported val ~**$84M** Jul 2024 **[directional]**
- **Product focus:** Residential listings / MLS data infrastructure (SaaS) — ingest new MLS feeds, transform into the warehouse, intelligence layer (metrics, semantic models, dashboards) for internal teams and customers
- **Intern comp (2027 Data Analytics Engineering Intern):** **$12,000 for 10 weeks** (minus taxes) — ~$30/hr. SWE intern sibling is a different Ashby req; do not import its stack or comp
- **Work model:** Paid; full-time **June 7 – August 13, 2027** (10 weeks); **5 days/week onsite** SoHo HQ; dedicated analytics-engineer mentor; intern owns a summer project (profiling/mapping a new non-MLS source is a named candidate); end-of-summer presentation to executive and data teams
- **Clearance / eligibility:** **Rising seniors** in CS, data science, statistics, or other STEM. **US work authorization required**; JD: only considering candidates authorized to work in the U.S.; no sponsorship implied. Posted **2026-09-29**. Application deadline **2026-10-18 11:00 PM ET** (Ashby `applicationDeadline` 2026-10-19T03:00:00.000Z). Offers by **2026-11-25**. Ashby **`9d34fc9d-e235-44fc-bdf9-42e75223839a`**

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Ashby ATS + human-read startup/mid-size | Binding intern gate. Ashby / startup = a human reads the PDF early (`recruiting.md` Part I §1 / §5). First-wave apply (`recruiting.md` Part II §8). Deadline Oct 18 2026 11pm ET |
| Recruiter / HM | Unpublished intern loop | Rising-senior standing, US work auth, 5-day SoHo onsite Jun 7–Aug 13 2027 |
| OA | Unpublished | Do **not** invent HackerRank/CodeSignal |
| Technical | Unpublished; FT SWE analog **[directional, Dataford]:** HR screen → coding / sys-design / behavioral → stakeholders | Intern loop unpublished. ~3 rounds / 3–5 weeks on the FT analog only — not confirmed for this intern. No intern sys design published |
| Behavioral | Filter throughout | Cross-functional with analytics engineers, data engineers, PMs, customer-facing teams; attention when a number looks wrong (`recruiting.md` §6) |

**Estimated funnel:** Ashby resume → unpublished intern loop · intern OA unpublished · No intern sys design published · Bottleneck: **resume** · ~15–25% **[directional, C-tier peer of Ibotta / Fable / early SaaS]**

## Stack & Hiring Signal

- **Languages:** JD required **SQL** (RDBMS, joins, aggregations, CTEs; window functions not required). Python/pandas is a **bonus**, not a required-language gate. Honest inventory analogs: **Python + SQL/PostgreSQL/asyncpg + Pandas ETL + Flask/React dashboard + Docker/Git**. Do **not** invent dbt, Snowflake, Redshift, BigQuery, Looker, Tableau, Mode, Metabase, Rails, or MLS/real-estate internships
- **Domains:** Analytics engineering on listings/MLS data: profile ingested feeds for new MLS clients; extend warehouse transforms (dbt named on JD — analog via tests/docs/ETL, not a claimed tool); metric definitions / semantic models / dashboards; own a summer project mapping a messy non-MLS source. Sibling SWE intern is Rails/TS/React product — wrong twin
- **What wins:** Because the bottleneck is the resume (`recruiting.md` startups / Ashby is resume-first), a one-page PDF that shows **SQL and Python through use**, messy-source → warehouse/usable analog, data-quality instinct (a wrong number caught), and a real dashboard or reporting surface — without claiming dbt/Snowflake/Looker or MLS-domain ownership

## Sources

- JD (this file's intern): https://jobs.ashbyhq.com/Perchwell/9d34fc9d-e235-44fc-bdf9-42e75223839a (Ashby **`9d34fc9d-e235-44fc-bdf9-42e75223839a`** Data Analytics Engineering Intern)
- SWE intern twin (do not mix): https://jobs.ashbyhq.com/Perchwell/194eec78-26db-4d8e-850f-a99ea2733e9f · packet `applications/2027/perchwell/software-engineer-intern/`
- Built In NYC mirror: https://www.builtinnyc.com/job/data-analytics-engineering-intern/11417756
- Press kit: https://www.perchwell.com/about/press-kit (founded 2015, NYC HQ, MLS/brokerage platform)
- Series A: https://www.perchwell.com/blog/perchwell-raises-15-million-series-a-to-scale-its-real-estate-data-and-workflow-platform-nationally (Founders Fund, Dec 2021; REBNY RLS)
- Series B: https://www.perchwell.com/blog/amidst-real-estate-industry-transformation-perchwell-raises-25m-series-b-to-further-empower-agents (Lux Capital, Jul 2024)
- HQ lease (110 Greene St): https://therealdeal.com/new-york/2017/12/06/olr-realplus-rival-perchwell-inks-lease-in-soho/
- REBNY RLS operator: https://therealdeal.com/new-york/2019/12/24/tales-of-turmoil-as-rebnys-rls-board-picks-perchwell-for-new-product/
- `reference/companies.md` — no Perchwell row; C-tier analog of Ibotta / Fable / early SaaS (interview shape, bottleneck, acceptance estimate)
- `reference/recruiting.md` Part I §1 / §5 (startup/mid-size human-read; Ashby analog to Greenhouse/Lever resume-first); Part II §8 (intern eligibility / first-wave); Part III §13 (applied data)
