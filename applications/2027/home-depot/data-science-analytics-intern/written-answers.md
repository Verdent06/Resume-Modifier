# The Home Depot — 2027 Summer Internship - Data Science & Analytics (Atlanta) · Written Application Answers

Draft answers for the Workday CareerDepot apply flow (**Req191968**). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Snowflake, Databricks, Copilot, Fusion, Tableau, BigQuery, or Sentry.** Trim to the form's length limit before submitting.

This posting is the **undergrad / applied college-student Data Science & Analytics intern** at Store Support Center, Atlanta - 9090 — **not** the Master's/PhD Data Science intern and **not** the SWE intern.

Apply: https://homedepot.wd5.myworkdayjobs.com/careerdepot/job/STORE-SUPPORT-CENTER-ATLANTA---9090/XMLNAME-2027-Summer-Internship---Data-Science---Analytics_Req191968

Posted ~Aug 31 / Sep 1 2026. Resume is the bottleneck (`persona.md` / `companies.md`). Apply in this first rolling wave.

**Workday Application Questions were behind account creation.** The JD page exposes the apply steps (Create Account → My Information → My Experience → Application Questions → Voluntary Disclosures → Review) but not the question text. Do not invent screening questions. Fill identity fields below; if the live form asks something not listed here, answer from `persona.md` + `context.md` only.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/home-depot/data-science-analytics-intern/Vedant Desai Resume.pdf` |
| Location | **Willing to work onsite in Atlanta** at the Store Support Center, five days a week (Monday–Friday). Housing assistance is posted for eligible interns. |
| Work model | Full-time, 11 weeks, **May 17 – July 30, 2027**, onsite Atlanta |
| Currently enrolled college student? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (returns Fall 2027 after this internship) |
| Returning to school after internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| Ability to work full-time May 17 – July 30, 2027? | **Yes** |
| GPA | **3.66 / 4.0** (preferred floor is 3.0) |
| Authorized to work in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship? | **No** — none needed. This req has no sponsorship language; do not volunteer a visa story. |
| How did you hear about this role? | **Other** / the job board you actually used. No Home Depot contact in `network.md`. |
| Languages / tools you can interview in | **Python, SQL, Pandas, Flask, PostgreSQL.** Do **not** check Tableau, BigQuery, Snowflake, Databricks, Copilot, Fusion, or Sentry. |

---

## Cover letter / "Why Home Depot / why Data Science & Analytics?" (paste if the form has a box)

I am applying to the 2027 Summer Internship - Data Science & Analytics at The Home Depot Store Support Center in Atlanta (Req191968) — the undergrad / applied college-student seat, not the PhD Data Science intern and not the software-engineering intern.

I want to spend the 11 weeks (May 17 – July 30, 2027) on the work this program actually assigns: take a business question on a Services, e-Commerce, Merchandising, Operations, or Finance team, turn messy data into an insight, and present a recommendation to people who are not the builders. That is this intern, not a research-methods paper.

What I can defend:

- **Messy ingest → ranking → stakeholder delivery.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and a deterministic PAC-ranking engine, then shipped a Flask REST API on AWS EC2 to Michigan Campaign Finance Network researchers, eliminating ~800 hours of manual pulls across 400 tracked PACs. That is ingest → insight → report-out.
- **Scoring a shortlist against a business rule.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a unified PWSID entity database, delivered 800+ Day-1 acquisition targets, and built a Review Velocity score that filtered those to a 280-lead shortlist at 35% precision against the fund's revenue criteria.
- **Applied modeling with a held-out check.** On SignalWeaver I combined fundamentals and sentiment into an out-of-sample regression (3.39% R²) so the score was not just fitting noise, then built a React dashboard over scores persisted in Postgres. Research assistant, not investment advice.
- **SQL I can walk.** On Vylet I own a production asyncpg DAL with injection-safe SQL timestamp checks that trigger re-scrapes. That is freshness plumbing, not JOIN/aggregate insight SQL. Python and Pandas are the analysis languages on my page.

I have not used Tableau, Google BigQuery, Snowflake, Databricks, Copilot, or Fusion. I would ramp on the team's approved stack rather than pretend I already have it.

I can be onsite in Atlanta five days a week for the posted term. I return to Michigan afterward (Expected May 2028). I am a U.S. citizen and I do not need sponsorship.

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Tell us about a project" / messy data / SQL / Python / presenting findings

**MDC (messy filings → Pandas ETL → ranking shipped to researchers).** Irregular Excel exports and portal caps; ~800 hours / 400 PACs. This is the grounded messy-dataset story and the senior-leader report-out analog. Do not invent a retail SKU dataset.

**Lyndbrook (entity DB + scored shortlist).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision. Operational public data, not merchandising. Say the domain out loud if they ask.

**SignalWeaver (predictive-modeling analog).** Out-of-sample 3.39% R²; React dashboard. Do not call this Tableau.

**Vylet (SQL).** asyncpg freshness / re-scrape DAL. If they ask for JOIN/window SQL, say the pool does not have that bullet — Python/Pandas did the analysis work (`grade.md` out of rails).

---

## Availability

Full-time, onsite Atlanta, May 17 – July 30, 2027. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **This is not the PhD DS intern and not the SWE intern.** Use this folder's PDF. Do not paste a C++/audio-DSP or generic full-stack resume.
- **Do not claim Tableau, BigQuery, Snowflake, Databricks, Copilot, Fusion, or Sentry.** Preferred on the JD or nearby stack; not in the pool. Honest Python/SQL/Pandas/ETL beats a keyword lie (`persona.md` anti-pattern).
- **SQL on the page is the unquantified DAL line.** If they ask for analysis SQL, walk re-scrape/freshness and point to Pandas rankings — there is no JOIN/GROUP BY metric in the pool (`grade.md`).
- **Atlanta is 5 days onsite.** Housing assistance is posted for eligible interns. Do not self-reject on location.
- **No Home Depot contact in `network.md`.** A UMich alum at Atlanta SSC still beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Cover letter:** skip unless the form asks; paste from above if it does.
- **Funnel:** Workday resume screen (rolling). No OA on this DS intern req. Recruiter phone then hiring-manager behavioral + Python/SQL/project. Prep STAR against Action Oriented / Collaboration / Communication / Drives Results, not LeetCode.
- **Application Questions:** not visible without a CareerDepot account. Do not invent them. If the live form asks GPA, student status, Atlanta onsite, return-to-school, or work authorization, use the table above.
