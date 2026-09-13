# Klaviyo

Klaviyo (NYSE: **KVYO**) is a Boston B2C CRM and marketing-automation platform: first-party customer data plus email, SMS, WhatsApp, push, and analytics for ~180K+ paying commerce brands. The data plane is the Klaviyo Data Platform (KDP); channels sit on MCM (mobile + messaging infra). Engineering owns high-scale messaging infrastructure and customer-facing product across Data Infrastructure, MCM, Core Infrastructure, Growth Marketing Platform, AI & Analytics, and Autonomous Services. Two campus SWE seats live under this folder — **do not mix them:**

- **Software Engineer Co-op (Spring 2027)** Greenhouse **7989365003** / **R-103005** — Boston HQ 5 days/week, **Jan 4–Jun 25 2027**.
- **Software Engineer Intern (Summer 2027)** Greenhouse **7989364003** — 11 weeks **Jun 1–Aug 13 2027**.

Both are team-agnostic: placement ~30 days before start onto full-stack, back-end, or front-end inside any pillar, after Klaviyo Base Camp. Company identity is e-commerce marketing automation at 180K+ paying-customer scale, not an ML-research lab and not a Go/Django knockout. Do not invent Django, Go, Kafka, Cassandra, ClickHouse, Terraform, Aurora, Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Redshift, or Kinesis on the resume.

## Quick Facts

- **Tier:** B-TIER (`reference/companies.md`)
- **HQ / offices:** Boston, MA — **125 Summer Street** (this intern/co-op: **Boston HQ, 5 days/week in office**).
- **Valuation / signal:** Public since Sep 2023 (NYSE: KVYO). Q2 FY26 ~$1.5B ARR (26% YoY; official 2026-08-05). Market cap ~**$4.6B** (Sep 2026, PitchBook **[directional]**). ~2.3k–2.4k employees. Founded 2012; CEO Andrew Bialecki. JD: 180K+ paying customers.
- **Product focus:** Autonomous B2C CRM / marketing automation + CDP (email, SMS, WhatsApp, push) for e-commerce
- **Intern comp (2027 Software Engineer Co-op and Intern):** **$49.50–$60.50 USD/hr** (Base Pay Range For US Locations) on both JDs
- **Work model (Spring co-op 7989365003):** Paid; **Jan 4–Jun 25 2027**; in office **5 days/week**; full-time 40h; Base Camp; team-agnostic offer
- **Work model (Summer intern 7989364003):** Paid **11-week** Summer Internship Program, **June 1–August 13 2027**, full-time, in office 5 days/week; Base Camp; team-agnostic offer
- **Clearance / eligibility (both):** Graduating **December 2027 or May/June 2028**. ≥1 prior SWE internship or co-op. Pursuing CS, Engineering, Data Science, Math/Statistics, or related. **Not eligible for immigration sponsorship.** Apply by **2026-10-07** if possible (rolling). Company_name field: "Klaviyo Campus" — folders and TRACKER use **Klaviyo**. Former intern project examples: Share Inbox Preview; Invite Expiration Extension in IAM; real-time delivery stats dashboard; Jenkins → Buildkite migration; WhatsApp Templates image/carousel support.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Greenhouse ATS + human | Campus board `klaviyocampus`. **7989365003** Spring co-op · **7989364003** Summer intern. Apply by **2026-10-07** if possible; rolling. First wave (`recruiting.md` §8). Prior SWE intern/co-op is a hard JD must-have. |
| Recruiter | Phone / video | Work auth / no sponsorship, Boston 5 days/week, term dates (Jan 4–Jun 25 **or** Jun 1–Aug 13), graduation window, prior SWE intern/co-op |
| OA | **CodeSignal** ~90 min | Official CodeSignal customer. Scenario debug / iterative impl / API design — **not** classic LC **[directional]**. **Bottleneck** after resume |
| Superday | ~3h (Boston HQ or virtual) | Behavioral + API/pair + light intern sys design; weather-app/API+FE analog reported **[directional]** |
| Behavioral | Filter throughout | Ownership, shipping, always-learning / in-person culture — filter round (`recruiting.md` §6) |

**Estimated funnel:** Greenhouse campus resume → recruiter → ~90-min CodeSignal → 3-hr superday · Medium · CodeSignal · Light intern sys design on superday · Bottleneck: **OA** after resume · ~3–8% **[directional, peer of Shopify / Salesforce / Dropbox]** (`reference/companies.md`)

Web vs doctrine: InterviewQuery / Extern / Blind 2026 intern reports match the CodeSignal non-LC shape (debug, iterative feature add, API design). Extern also cites ~23-day apply-to-decision and a Feb 15 recommended cutoff from *prior* cycles — **these JDs' apply-by is October 7**; lead with the JD. Do not treat Extern's $53/hr midpoint as replacing the JD band.

## Stack & Hiring Signal

- **Languages:** Both JDs list *some of*: Python, Django, TypeScript, React, Go; MySQL, Cassandra, ClickHouse, Kafka, Redis; AWS (EC2, RDS, Aurora), Terraform. Screen tests polyglot proof in what the candidate actually ships — **do not invent Go, Django, Terraform, Cassandra, ClickHouse, Kafka, Aurora, Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Redshift, or Kinesis.** Python / TypeScript / React / Redis / AWS through use; PostgreSQL is the honest MySQL analog when a selected bullet has PostgreSQL.
- **Domains:** Generic intern/co-op SWE that may land full-stack, back-end, or front-end on Data Infra, MCM/messaging, Core Infra, Growth Marketing Platform, AI & Analytics, or Autonomous Services. High-scale customer-facing features, data platform, and messaging/queue infra are company flavor — not an ML-training seat. AI-first / Copilot on the JD is a **workflow** expectation, not a skill to invent.
- **What wins:** Because the bottleneck is the **CodeSignal OA** after a Greenhouse resume screen (`companies.md`; `recruiting.md` Part I §1 / Part II §8), a one-page PDF that shows **finished** full-stack or backend software (API + UI or a shipped backend), production debug, JD languages in bullets, and data-pipeline / Redis / AWS flavor as the CDP-and-messaging differentiator — not notebook ML, not CI/CD-as-primary (`resume.md` Part III §12 / `recruiting.md` Part III §11). Prior titled SWE intern/co-op is a hard JD filter. Apply before 2026-10-07.

## Sources

- Spring co-op JD: https://job-boards.greenhouse.io/klaviyocampus/jobs/7989365003 (job id **7989365003**; requisition **R-103005**; first_published / updated_at 2026-09-12T08:05:17-04:00)
- Summer intern JD: https://job-boards.greenhouse.io/klaviyocampus/jobs/7989364003 (job id **7989364003**)
- `reference/companies.md` B-TIER Klaviyo row (tier, interview format, bottleneck, acceptance estimate, stack bans)
- `reference/recruiting.md` Part I §1 (binary knockouts); Part I §5 (Greenhouse human-reads-PDF); Part II §8 (intern eligibility/timing); Part III §11 (full-stack bar)
- CodeSignal customer page: https://codesignal.com/customers/klaviyo
- InterviewQuery Klaviyo SWE guide 2026 (OA/superday shape) **[directional]**: https://www.interviewquery.com/interview-guides/klaviyo-software-engineer
- Extern intern-guide (cohort size, ~23-day funnel; apply-by and pay stale vs these JDs) **[directional]**: https://www.extern.com/post/klaviyo-internship-guide
- Blind CodeSignal thread **[directional]**: https://www.teamblind.com/post/klaviyo-codesignal-ia7e257m
- Public company facts: Yahoo Finance / StockAnalysis / PitchBook (HQ 125 Summer St, IPO 2023, ~$4.6B mkt cap Sep 2026 **[directional]**, ~2.4k employees)
