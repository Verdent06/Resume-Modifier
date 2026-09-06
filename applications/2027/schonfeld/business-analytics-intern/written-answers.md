# Schonfeld — 2027 Business Analytics Intern · Screening Answers

Draft answers for Schonfeld’s Greenhouse application (job **8171703**). Grounded in `persona.md` (applied BA / Data Analyst: Python + SQL through use, pipelines, reports, Redis + Postgres — **not Power BI**, **not** a trading-desk internship, **not** LoRA/LangGraph lead, **not** the SWE sibling) and the live form. First-person, honest, defensible under “walk me through this.” Trim to each field’s length limit before submitting.

Apply (do **not** submit from this agent):

- ATS: https://job-boards.greenhouse.io/schonfeld/jobs/8171703
- Embed: https://boards.greenhouse.io/embed/job_app?token=8171703

**This agent did not submit.** Form fields captured from the live Greenhouse jobs API + apply page (2026-09-06).

**SHA-256:** `a6417a4ce6b7046fd05334b05262e8fdc5352e2c9120c2d57d6bf519752aa8ca`

**Form-kit identity (use on Greenhouse — never `vedantde@umich.edu`):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · Address **49032 Freestone Dr, Northville, MI 48168** ZIP **48168** · US citizen, no sponsorship · work-authorized **Yes** · GPA **3.66** · Expected **May 2028** · Junior · 96 credits by Summer 2027 · LinkedIn https://www.linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06 · SAT **1510** if asked · DOB **12/16/2006** if asked · valid US DL **Yes** if asked · UMich start **08/31/2025** · Northville High School graduated **05/19/2025**.

The resume PDF header uses **verdent06@gmail.com**. The **form** uses the same.

---

## Identity (live Greenhouse)

| Exact label | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | **verdent06@gmail.com** |
| Phone * | **248-704-4852** |
| Location * | **Northville, Michigan, United States** (Locate me if it resolves to Northville; not Ann Arbor) |
| Resume/CV * | attach `applications/2027/schonfeld/business-analytics-intern/Vedant Desai Resume.pdf` (pdf) |
| Cover Letter | optional — paste the draft below, or attach as pdf/docx |
| LinkedIn Profile | https://www.linkedin.com/in/vedantde06 |
| Website | leave blank (no portfolio URL in `context.md`). GitHub is on the PDF. |

---

## Education widget (required)

Greenhouse typeahead (`Select...`). This agent did not create an account or exhaust the school catalog.

| Exact label | Answer |
| --- | --- |
| School | Type **University of Michigan**. Also try **University of Michigan-Ann Arbor** / **University of Michigan - Ann Arbor**. If the catalog misses it, pick the closest official row — do not invent a school. |
| Degree | **Bachelor's** / **Bachelor of Science** if listed |
| Discipline | **Computer Science** (dual CS + Economics is on the PDF; do not invent a second row unless required) |
| Start date month / year | **August** **2025** (UMich start 08/31/2025) |
| End date month / year | **May** **2028** (expected; not graduated) |

If a second education row is required: Northville High School, Northville MI, graduated **05/19/2025**.

---

## Knockouts (required Yes/No)

| Exact label | Answer | Why |
| --- | --- | --- |
| What is your current cumulative GPA? * | **3.66** | `context.md` |
| What degree are you currently pursuing? * | **Bachelor's** | Options: Bachelor's / Master's / PhD / Other |
| Will you graduate from January 2028-Summer 2028? | **Yes** | Expected **May 2028**. This is **not** the SWE sibling’s “graduating summer or fall of 2027?” question. **Do not answer No.** |
| Are you authorized to work in the United States? * | **Yes** | US citizen |
| Do you now require sponsorship for employment visa status to work legally in the United States? * | **No** | US citizen; no sponsorship |
| Will you in the future require sponsorship for employment visa status to work legally in the United States? * | **No** | US citizen; no sponsorship |

---

## If asked (not on this embed)

| Exact label / prompt | Answer |
| --- | --- |
| Street address / ZIP | **49032 Freestone Dr, Northville, MI 48168** |
| Class standing | **Junior** |
| Credits completed by Summer 2027 | **96** |
| SAT | **1510** |
| Date of birth | **12/16/2006** |
| Valid US driver’s license | **Yes** |
| High school | **Northville High School**, graduated **05/19/2025** |
| University start | **08/31/2025** |
| GitHub | https://github.com/Verdent06 |
| Work authorized | **Yes** |

---

## Cover letter (optional)

I want to spend ten weeks turning messy business data into something a stakeholder can use. Schonfeld’s 2027 Business Analytics Intern role is that job: New York, on the Business Analytics team, as a Data Analyst next to a manager and a mentor. The work is data acquisition and processing for risk, trading, accounting, operations, and business development — improve data quality, streamline manual processes, build reports, propose analytics, and support reporting infrastructure. I am applying as an applied analytics intern. I do not have a trading-desk internship, and I have not used Power BI; I will ramp on the team’s reporting stack rather than pretend I already have it.

The work I already do sits on that axis. In Python I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL for Michigan Campaign Finance Network researchers, eliminating ~800 hours of manual pulls across 400 tracked PACs, then ranked PACs by funding volume and shipped a Flask REST API on AWS EC2 as the sole engineer on a five-month contract. At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a PWSID entity database, delivered 800+ Day-1 acquisition targets, cut 15 hours of manual prospecting per week, and built a Review Velocity score that filtered those targets to a 280-lead shortlist at 35% precision. I also run Vylet, a live PE/search-fund lead product ($1,500 MRR): a Dockerized pipeline that turns a ~30-minute manual process into 30 scored leads in 30 minutes (Redis/Celery), plus an asyncpg data layer with injection-safe SQL timestamp validation so stale records re-scrape themselves. I am a US citizen. I have CS + Economics at Michigan (Expected May 2028, GPA 3.66, Junior, 96 credits by Summer 2027). SignalWeaver is a financial-research dashboard (not investment advice) with scores persisted to Postgres and pgvector search at 49ms p50.

I can work onsite in New York for the 10-week Summer 2027 program and I return to Michigan after (Expected May 2028 — I **will** graduate in the January 2028–Summer 2028 window). I want a summer next to analysts who treat data quality and reporting as the job.

---

## Demographics (voluntary)

Skip, or complete only if you want. Not used in this packet. Options: gender (Male / Female / Prefer not to say); Hispanic/Latino Yes/No; race (EEOC list). Whatever you choose, it is not a knockout.

---

## Notes for the applicant (not for submission)

- **This is not Greenhouse 8180089 SWE.** Do not paste the C++/Treasury packet. Use this folder’s PDF.
- **Do not invent Power BI, Snowflake, Databricks, Copilot, Tableau, Fusion, Sentry, KDB, or a trading-desk / OMS internship.** Interview in Python and SQL. Power BI is exposure-on-the-job.
- **Do not lead with LoRA / LangGraph / agent pipelines.** This is BA / Data Analyst.
- **Jan–Summer 2028 grad = Yes.** Expected May 2028. The SWE sibling’s 2027-grad question is a different field.
- **Sponsorship is two questions** (now + future). Both **No**.
- **SignalWeaver GitHub is real:** https://github.com/Verdent06/SignalWeaver
- No Schonfeld contact in `network.md` — do not claim an employee referral.
- Comp: $100,000–$115,000 annualized, prorated to 10 weeks (JD).
