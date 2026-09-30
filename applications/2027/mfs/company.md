# MFS Investment Management

MFS (Massachusetts Financial Services Company, d/b/a MFS Investment Management) is a Boston-headquartered global active asset manager that launched the first U.S. open-end mutual fund in 1924. It is an indirect majority-owned subsidiary of Sun Life Financial (NYSE/TSX: **SLF**). Official fact sheet: **$643.5B** AUM as of **August 31, 2026**; more than **2,100** employees worldwide; ~**300** investment professionals in Boston plus Hong Kong, London, Singapore, São Paulo, Sydney, Tokyo, and Toronto. This co-op is Workday **MFS-231978** **Spring 2027 Investment Data Engineer Co-op** on the **Investment Data Management Office** — unify/harmonize investment data for the multi-asset platform (investors, risk, client reporting) — **not** a PM/research-analyst seat and **not** a generic product-SWE intern.

## Quick Facts

- **Tier:** C-TIER (`reference/companies.md` — Boston active AM intern/co-op; peer of Wellington Technology undergrad / American Century Enterprise Data / Audax DE co-op. Below Fidelity FIDTERN B-band pay/OA.)
- **HQ / offices:** Boston, MA HQ (**111 Huntington Avenue**, 02199). This co-op: Workday location **Boston**. `#LI-HYBRID` (remote/onsite unless the posting says otherwise)
- **Valuation / signal:** Invented the mutual fund (1924); P&I 35th-largest AM worldwide (Dec 31 2024 data); ISS MI 9th-largest U.S. active long-term MF/ETF manager (Dec 31 2025); Sun Life subsidiary; 85 U.S. mutual funds + 8 actively managed ETFs through 2025
- **Product focus:** Active equity, fixed income, multi-asset, and client reporting. This co-op is **investment data engineering** — ingest/process internal and external investment records onto a unified data platform — not a trading-desk quant intern
- **Intern comp (2027 Investment Data Engineer Co-op, MFS-231978):** **$21.00–$25.00/hr** (JD)
- **Work model:** Paid **6-month** co-op, **Monday–Friday**, **Wednesday January 13 – Friday June 25, 2027**, **35–40 hours/week**. Structured program: new-hire orientation, senior-leadership speaker series, social/networking, presentation challenges. Posted **2026-09-30**; Workday `endDate` **2026-10-30**
- **Clearance / eligibility:** Currently pursuing a bachelor's in Computer Science, Data Science, or related (**junior or senior preferred**). Program is **designed for** undergraduates **currently enrolled in a co-op program** through their college. No visa/sponsorship line on this JD. **Not** a summer intern twin if one exists later

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human + Workday ATS | Bottleneck. Apply via `mfs.wd1.myworkdayjobs.com` / `MFS-Careers`. `includeResumeParsing: true`. `questionnaireId` `d8e4dfc372491000bd4e312ac5530000` (login-walled). Apply in the first wave (`recruiting.md` Part II §8). Posted 2026-09-30; apply-by **2026-10-30** |
| Recruiter / Early Career | Phone or video (unpublished) | Enrollment, Boston hybrid, Jan 13–Jun 25 2027, 35–40h, co-op-program radio if present, work auth |
| Interview | Unpublished intern loop | Easy Python/SQL + project walk + STAR **[directional, C-tier AM DE peers: American Century Enterprise Data / Pacific Life DE / Audax DE]**. Intern OA unpublished — do **not** invent HackerRank/CodeSignal |
| Behavioral | Filter throughout | Collaboration, strongest-idea culture, presentation challenge at end of program (`recruiting.md` §6) |

**Estimated funnel:** Workday resume → recruiter → 1–2 STAR + pipeline walk · intern OA unpublished · No intern sys design · Bottleneck: **resume** · ~15–25% **[directional, C-tier peer of Wellington / American Century Enterprise Data / Audax DE co-op]**

## Stack & Hiring Signal

- **Languages:** JD names **Python, SQL, or similar**. Candidate inventory has Python and SQL. Plus (not required): Snowflake, Redshift, or BigQuery — **do not invent**. Agile (Scrum/Kanban) is a plus, not a knockout.
- **Domains:** Investment Data Management Office — scalable ingest from internal/external investment sources; quality, resiliency, control, efficiency, monitoring; data products on a unified platform; ingestion / delivery / transformation / orchestration tools; outage support.
- **What wins:** Python and SQL through use in ingest → ETL/transform → quality or freshness → serve (API, tables, dashboard analog) with a witness metric; Docker as orchestration analog; AWS if inventory; stakeholder-facing delivery. Resume is the gate (`recruiting.md`: mid-size / non-tech-tech is resume-first). Dual CS + Economics is on-axis flavor for an asset manager. Do not invent warehouse tools. Do not optimize as generic product-SWE or notebook LoRA.

## Sources

- JD: https://mfs.wd1.myworkdayjobs.com/en-US/MFS-Careers/job/Boston/Spring-2027-Investment-Data-Engineer-Co-op--January---June-_MFS-231978 (Workday **MFS-231978**; CXS pulled 2026-09-30)
- Corporate fact sheet (AUM $643.5B as of 2026-08-31; 2,100+ employees; ~300 investment professionals): https://www.mfs.com/en-global/investment-professional/about-mfs/newsroom/corporate-fact-sheet.html
- HQ / legal: Massachusetts Financial Services Company, 111 Huntington Avenue, Boston, MA 02199 — Form ADV brochure
- `reference/companies.md` C-TIER MFS row (interview format, bottleneck, acceptance estimate)
- `reference/recruiting.md` Part I §5 (mid-size / non-tech-tech resume-first); Part II §8 (intern eligibility/timing); Part III §13 (applied ML/data: ship pipelines); §6 (behavioral as filter)
