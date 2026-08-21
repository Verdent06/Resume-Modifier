# Blackstone

Blackstone is the world's largest alternative asset manager (~$1.3T AUM; firm site), investing across real estate, private equity, credit, infrastructure, life sciences, growth equity, secondaries, and hedge funds. Blackstone Technology & Innovations (BXTI) is the internal technology organization: platforms, applications, data systems, and automation that run firm operations, investment decisions, risk, and investor/portfolio delivery. This intern req (**45022**, 2027 Data Engineer Summer Analyst) is BXTI data engineering — Python/SQL ETL–ELT pipelines on AWS — **not** SWE **45021** and **not** Data Science. Custom apps are mostly Python, hosted on AWS; the posting names Snowflake for warehouse/analytics and Prefect for orchestration. Honest candidate inventory does not include Snowflake, Prefect, Terraform, Gitlab, RDS, ECS, or Lambda — do not invent them.

## Quick Facts

- **Tier:** B-TIER (`reference/companies.md`)
- **HQ / offices:** New York HQ; this intern is **Miami, FL** onsite
- **Valuation / signal:** World's largest alt AM (~$1.3T AUM); BXTI is the internal tech org, not the PE/IB recruiting funnel
- **Product focus:** BXTI data platforms — ETL/ELT pipelines, Python services on AWS, warehouse-backed analysis for investment and operations
- **Intern comp (2027 Data Engineer Summer Analyst):** Expected annual base salary $125,000–$125,000 (JD)
- **Work model:** Paid full-time Summer Analyst; start June 2027; Miami onsite. Interns treated as engineers from day one alongside developers, architects, and product teams
- **Clearance / eligibility:** Currently enrolled undergraduate; anticipated graduation **Fall 2027 – Spring 2028**; resume must include expected graduation month/year and GPA; resume must be PDF. No sponsorship/citizenship language on the public posting. Not SWE 45021; not Data Science

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Workday campus ATS + recruiter | Binding intern gate with fit; apply in the first-wave window (`recruiting.md` Part II intern) |
| Recruiter / video screen | Recruiter or HireVue-style screen | Background, motivation, logistics. PE HireVue/LBO is a **different** (investment) funnel — do not coach this req as banking |
| OA | HackerRank | Python/SQL Easy–Med; candidate-reported for BXTI (~four questions). Official HackerRank blog: Blackstone uses HackerRank as a bookend for developer hiring |
| Tech video | ~1 hour with a senior engineer | Python, SQL, pragmatic AWS/data-architecture discussion; light intern sys design |
| Superday | Multi-session final | Senior engineers + hiring manager; coding + project walkthrough + behavioral fit / why Blackstone |
| Behavioral | Filter throughout | Entrepreneurial / self-starting culture; behavioral is a filter (`recruiting.md` §6) |

**Estimated funnel:** Workday campus resume → recruiter/video screen → HackerRank (Python/SQL Easy–Med) → tech video → Superday · Light intern sys design · Bottleneck: resume + fit · ~5–8% (`reference/companies.md` B-TIER Blackstone row)

## Stack & Hiring Signal

- **Languages:** Python is the intern floor (Pandas or equivalent). SQL / database query languages are required. OOP in any language (Python a plus). Do not invent Java/.NET.
- **Domains:** ETL/ELT data pipelines across business units; AWS-hosted Python services; containerized microservices (Docker); warehouse-backed analysis. JD also names Snowflake, Prefect, Terraform, Gitlab, RDS, ECS, Lambda, IaC — familiarity/preferred. Honest inventory is Python, Pandas, SQL, AWS (EC2, S3), Docker only for those clouds/tools.
- **What wins:** Because the bottleneck is resume + fit (`companies.md`; `recruiting.md` intern funnel), a one-page PDF that shows ingest → transform (ETL/ELT, Pandas) → SQL/quality → serve on AWS/Docker, with OOP and pipeline ownership visible in bullets, not Skills-only. Do not lead as generic SWE (that is req 45021) or notebook ML / Data Science. Do not claim Snowflake, Prefect, Terraform, Gitlab, RDS, ECS, or Lambda.

## Sources

- JD: https://blackstone.wd1.myworkdayjobs.com/blackstone_campus_careers/job/Miami/XMLNAME-2027-Blackstone-Technology-and-Innovations--Data-Engineer-Summer-Analyst_45022 (req 45022; pulled 2026-08-21)
- https://www.blackstone.com/ (AUM, strategies)
- `reference/companies.md` B-TIER Blackstone row (interview format, bottleneck, acceptance estimate, Miami / $125k / not 45021)
- `reference/recruiting.md` Part II §8 (intern eligibility / timing), Part III §13 (applied data / ML; pipelines)
- HackerRank blog: Blackstone uses HackerRank for developer hiring (directional process confirmation)
- techinterview.org Blackstone BXTI 2026 guide (directional: recruiter → HackerRank Easy–Med → tech video → Superday; Python/SQL)
