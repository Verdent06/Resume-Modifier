# MFS Investment Management

MFS (Massachusetts Financial Services Company, d/b/a MFS Investment Management) is a Boston-headquartered global active asset manager that launched the first U.S. open-end mutual fund in 1924. Legal posting employer: **001 Mass Financial Services**. Parent: **Sun Life Financial** (NYSE/TSX: **SLF**). Official fact sheet: **$643.5B** AUM as of **August 31, 2026**; more than **2,100** employees worldwide; ~**300** investment professionals in Boston plus Hong Kong, London, Singapore, São Paulo, Sydney, Tokyo, and Toronto. HQ **111 Huntington Avenue, Boston, MA 02199** (Prudential Center).

**Do not mix PDFs.** This folder holds two Spring 2027 Boston co-op packets:

- **MFS-231978** — Investment Data Engineer Co-op — Investment Data Management Office (`investment-data-engineer-coop/`)
- **MFS-231979** — Jr Software Engineer Co-op — LCERM (Legal, Compliance & Enterprise Risk Management) (`jr-software-engineer-coop-spring/`)

**Not** Digital Development **MFS-231972**, **not** Digital Workflow Automation **MFS-231977**, **not** Information Security **MFS-231951**, **not** a PM/research-analyst seat.

## Quick Facts

- **Tier:** C-TIER (`reference/companies.md` — Boston active AM intern/co-op; peer of Wellington Technology undergrad / American Century Enterprise Data / Audax DE co-op. Below Fidelity FIDTERN B-band pay/OA.)
- **HQ / offices:** Boston, MA HQ (**111 Huntington Avenue**, 02199). These co-ops: Workday location **Boston**. `#LI-HYBRID` (remote/onsite unless the posting says otherwise)
- **Valuation / signal:** Invented the mutual fund (1924); P&I 35th-largest AM worldwide (Dec 31 2024 data); ISS MI 9th-largest U.S. active long-term MF/ETF manager (Dec 31 2025); Sun Life subsidiary; 85 U.S. mutual funds + 8 actively managed ETFs through 2025
- **Product focus:** Active equity, fixed income, multi-asset, and client reporting. **MFS-231978** is **investment data engineering** (ingest/harmonize investment records). **MFS-231979** is **LCERM enterprise IT** (databases, data pipelines, multi-tier application code). Neither is a trading-desk quant intern
- **Intern comp (both Spring 2027 co-ops):** **$21.00–$25.00/hr** (each JD)
- **Work model:** Paid **6-month** co-op, **Monday–Friday**, **Wednesday January 13 – Friday June 25, 2027**, **35–40 hours/week**. Structured program: new-hire orientation, senior-leadership speaker series, social/networking, presentation challenges. Posted **2026-09-30**; Workday `endDate` **2026-10-30**
- **Clearance / eligibility:** Program is **designed for** undergraduates **currently enrolled in a co-op program** through their college. Do not invent UMich co-op-office enrollment. No visa/sponsorship line on either JD. **MFS-231978:** bachelor's in Computer Science, Data Science, or related (**junior or senior preferred**). **MFS-231979:** bachelor's in Computer Science, MIS, or Finance (or equivalent); no class-year exclusive

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human + Workday ATS | Bottleneck. Apply via `mfs.wd1.myworkdayjobs.com` / `MFS-Careers`. `includeResumeParsing: true`. `questionnaireId` `d8e4dfc372491000bd4e312ac5530000` (login-walled; HTTP 406 without account). Apply in the first wave (`recruiting.md` Part II §8). Posted 2026-09-30; apply-by **2026-10-30** |
| Recruiter / Early Career | Phone or video (unpublished) | Enrollment, Boston hybrid, Jan 13–Jun 25 2027, 35–40h, co-op-program radio if present, work auth. Glassdoor intern analog: **one Zoom with the team manager**, mostly behavioral **[directional]** |
| Interview | Unpublished intern loop | Easy Python/SQL + project walk + STAR **[directional, C-tier AM peers: American Century / Pacific Life / Audax / Wellington]**. Intern OA unpublished — do **not** invent HackerRank/CodeSignal |
| Behavioral | Filter throughout | Collaboration, strongest-idea culture, presentation challenge at end of program (`recruiting.md` §6) |

**Estimated funnel:** Workday resume → recruiter → 1–2 STAR + pipeline/project walk · intern OA unpublished · No intern sys design · Bottleneck: **resume** (+ possible "enrolled in a co-op program" knockout) · ~15–25% **[directional, C-tier peer of Wellington / American Century / Audax]**

## Stack & Hiring Signal

### MFS-231978 — Investment Data Engineer Co-op

- **Languages:** JD names **Python, SQL, or similar**. Candidate inventory has Python and SQL. Plus (not required): Snowflake, Redshift, or BigQuery — **do not invent**. Agile (Scrum/Kanban) is a plus, not a knockout.
- **Domains:** Investment Data Management Office — scalable ingest from internal/external investment sources; quality, resiliency, control, efficiency, monitoring; data products on a unified platform; ingestion / delivery / transformation / orchestration tools; outage support.
- **What wins:** Python and SQL through use in ingest → ETL/transform → quality or freshness → serve (API, tables, dashboard analog) with a witness metric; Docker as orchestration analog; AWS if inventory; stakeholder-facing delivery. Resume is the gate (`recruiting.md`: mid-size / non-tech-tech is resume-first). Dual CS + Economics is on-axis flavor for an asset manager. Do not invent warehouse tools. Do not optimize as generic product-SWE or notebook LoRA.

### MFS-231979 — Jr Software Engineer Co-op (LCERM)

- **Languages:** JD or-list **SQL, JAVA, python, Power Apps or React**. Candidate inventory has Python, SQL, React — **not** Java, **not** Power Apps, **not** Azure. Do not invent them.
- **Domains:** LCERM junior SWE — interpret requirements with BAs/users, code/debug/unit-test, data pipelines and multi-tier apps, configure cloud vendor apps, document, agile. Financial-industry knowledge and Azure are pluses.
- **What wins:** A generic SWE co-op page with Python + SQL + React through use, a shipped API or data pipeline, and a named defect/test analog, plus finance-adjacent shipping as the MFS differentiator. Java / Power Apps / Azure are training-on-the-job, not fabrication targets. Resume is the gate (`recruiting.md` Part I §5 mid-size / non-tech-tech). Northeastern-style co-op enrollment is a real form risk — answer honestly.

## Sibling (do not mix)

- **MFS-231978:** Workday **Spring 2027 Investment Data Engineer Co-op (January - June)** — `applications/2027/mfs/investment-data-engineer-coop/`
- **MFS-231979:** Workday **Spring 2027 Jr Software Engineer Co-op (January - June)** — `applications/2027/mfs/jr-software-engineer-coop-spring/`
- **Not this folder:** Digital Development **MFS-231972**, Digital Workflow Automation **MFS-231977**, Information Security **MFS-231951**

## Sources

- JD MFS-231978: https://mfs.wd1.myworkdayjobs.com/en-US/MFS-Careers/job/Boston/Spring-2027-Investment-Data-Engineer-Co-op--January---June-_MFS-231978 (CXS pulled 2026-09-30)
- JD MFS-231979: https://mfs.wd1.myworkdayjobs.com/en-US/MFS-Careers/job/Boston/Spring-2027-Jr-Software-Engineer-Co-op--January---June-_MFS-231979 (CXS `jobPostingInfo` captured 2026-09-30)
- Apply MFS-231979: https://mfs.wd1.myworkdayjobs.com/en-US/MFS-Careers/job/Boston/Spring-2027-Jr-Software-Engineer-Co-op--January---June-_MFS-231979/apply
- Corporate fact sheet (AUM $643.5B as of 2026-08-31; 2,100+ employees; ~300 investment professionals): https://www.mfs.com/en-global/investment-professional/about-mfs/newsroom/corporate-fact-sheet.html
- HQ / legal: Massachusetts Financial Services Company, 111 Huntington Avenue, Boston, MA 02199 — Form ADV brochure; contact page https://www.mfs.com/en-global/investment-professional/about-mfs/contact-us.html
- Glassdoor intern/co-op interview analog **[directional]**: https://www.glassdoor.co.uk/Interview/MFS-Interview-Questions-E9607.htm
- `reference/companies.md` C-TIER **MFS** (MFS-231979) and **MFS Investment Management** (MFS-231978) rows
- `reference/recruiting.md` Part I §5 (mid-size / non-tech-tech resume-first); Part II §8 (intern eligibility/timing); Part III §11 (general SWE); Part III §13 (applied ML/data: ship pipelines); §6 (behavioral as filter)
