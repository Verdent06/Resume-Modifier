# American Express — Campus Undergraduate Summer Internship Program - 2027 Data Analytics, Global Servicing (NYC) · Written Application Answers

Draft answers for Oracle Cloud HCM req **26012627** (AMEX World Financial Center, New York, NY, hybrid). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Snowflake, Databricks, Copilot, Fusion, Tableau, Power BI, SAS, Hive, or AML/sanctions production tools.** Trim to the form's length limit before submitting.

**This is not** the ETS Software Engineer intern (Sunrise, FL; 26011015) and **not** an AI Engineer seat. Title on this req: Financial Crimes Data Analytics and Reporting Intern on the **1LOD Financial Crimes Risk & Controls** team inside **Global Servicing (GS)**. Use this folder's PDF, not the SWE intern packet.

Apply: https://egug.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/26012627

Posted 2026-08-18. Apply before 10/02/2026. Rolling review — class may fill first (`company.md` / `recruiting.md` §8). Apply in this wave.

Live apply flow required an email before any essay boxes appeared. No cover-letter prompt was visible without starting an application. Paste the letter only if HCM asks. HireVue (3 recorded behavioral questions) is the published campus next step (`company.md`): why Amex, teamwork, commercial awareness.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/american-express/data-analytics-intern-global-servicing/Vedant Desai Resume.pdf` |
| Location | **Willing to work hybrid in New York, NY** (AMEX World Financial Center, 10285). Amex Flex. |
| Work model | Hybrid Summer 2027 (~10 weeks; analog from sister ETS intern `company.md`) |
| Currently enrolled in a bachelor's in data science, analytics, CS, stats, economics, finance, mathematics, or related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (inside December 2027–June 2028) |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** (only if asked; no hard GPA floor on this JD) |
| Authorized to work with American Express in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship? | **No** — posting will not pursue sponsorship; none needed |
| Willing to work hybrid NYC for the Summer 2027 program? | **Yes** |
| How did you hear about this role? | **Jobright** (or **Other** → Jobright if Jobright is not listed). No Amex contact in `network.md` |
| Pay (if asked) | Accept posted intern range: **$24.05–$63/hr + sign-on bonus** |
| Languages / tools you can interview in | **Python, SQL, Pandas, Flask, PostgreSQL, React.** Do **not** check Tableau, Power BI, Snowflake, Databricks, Copilot, Fusion, SAS, Hive, or AML platforms |

---

## Cover letter / "Why Amex / why Global Servicing Data Analytics?" (paste if the form has a box)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

American Express — Global Servicing, 1LOD Financial Crimes Risk & Controls
New York, NY

Re: Campus Undergraduate Summer Internship Program — 2027 Data Analytics, Global Servicing (Job 26012627)

Dear 1LOD Financial Crimes Risk & Controls hiring team,

I am applying for the Summer 2027 Financial Crimes Data Analytics intern seat on Global Servicing's First Line of Defense Financial Crimes Risk & Controls team in New York — not the ETS Software Engineer intern in Sunrise, and not an AI-research rotation. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am authorized to work in the United States without visa sponsorship, and I can work the hybrid Amex Flex term in New York.

The intern job is applied data analytics: SQL and Python on large, messy datasets; trends, anomalies, and control-gap analogs; recommendations that a non-technical stakeholder can use. That is the work I already do. I have not interned in AML, sanctions, or anti-corruption operations. I have shipped the data path — irregular sources in, a scored or ranked artifact out, a number on what it changed.

What I can defend:

- **Messy filings → Pandas ETL → ranked monitoring.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs, and I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract. Analog to ingest → clean → report; not AML tooling.
- **Regulatory entity data → scoring → shortlist.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a PWSID entity database (800+ Day-1 targets) and built a Review Velocity score from public compliance data that cut the list to 280 leads at 35% precision against the fund's revenue criteria. Analog to control-effectiveness / ranked risk, not a claimed sanctions engine.
- **Broken control, then a fix.** On Vylet I diagnosed a name-collision in ownership verification that was rejecting valid targets. The fix lifted qualification from 79% to 89% with no change in sourcing volume. The production DAL is asyncpg with injection-safe SQL timestamp checks that trigger re-scrapes. If you ask for a SQL impact number: the pool has none on that line — the outcome is freshness without manual intervention.
- **Dashboard for non-builders.** On SignalWeaver I built a React dashboard over composite financial-research scores persisted in Postgres and served through FastAPI (9.1s p50 / 15.2s p99 across 90 tickers). Research assistant, not investment advice. Do not call this Tableau.

I have not used Snowflake, Databricks, Copilot, Fusion, Tableau, or Power BI. I would ramp on the team's approved stack rather than pretend I already have it.

I can be hybrid in New York for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

Sincerely,
Vedant Desai

---

## Short paste blurb (if HCM has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028) applying to the Global Servicing Financial Crimes Data Analytics intern seat in New York (req 26012627) — not the ETS Software Engineer intern. I ship Python/SQL analytics: a Pandas ETL on irregular campaign-finance filings that cut ~800 hours of pulls across 400 PACs, a compliance-data scoring model that shortlisted 800 targets to 280 at 35% precision, and a production SQL freshness check plus a React dashboard over Postgres scores. I have not used Tableau, Snowflake, or AML platforms; I will ramp. I do not need visa sponsorship.

---

## Likely HCM "job-specific" / short-answer boxes

Exact HCM essay text was not visible without starting an application. If a box appears, paste a trimmed version of the matching block. Do not invent a second messy-dataset story.

### Why this role / why Financial Crimes Risk & Controls / why Global Servicing?

I want the 1LOD analytics seat, not a generic SWE rotation. Global Servicing sits on customer, merchant, and commercial servicing data; 1LOD is supposed to find emerging risk and weak controls before the second line does. The analog I can defend is operational: irregular filings in, a ranked or scored artifact out, a stakeholder who is not an engineer. Campaign-finance PAC rankings (MDC) and EPA/MassGIS compliance scoring (Lyndbrook) are public-regulatory data work, not AML. Preferred JD interest in financial crime risk is real; a claimed AML internship is not.

### Tell us about a time you analyzed a large or messy dataset (SQL / Python)

**MDC.** Portal caps and irregular Excel exports; ~2 hours per committee by hand. Requests + Pandas ETL; PAC funding rankings; Flask API on EC2; ~800 hours / 400 PACs. This is the grounded messy-dataset story.

**Lyndbrook.** EPA ECHO + MassGIS → PWSID entity DB → 800 targets → 280-lead shortlist at 35% precision.

**Vylet SQL.** asyncpg DAL; injection-safe SQL timestamp validation; automatic re-scrapes. If they ask how much freshness improved: there is no sized metric in the pool — walk the control (stale row → re-scrape) honestly.

### Tell us about presenting findings to a non-technical audience

MDC: scoped ingestion through REST endpoints directly with MCFN researchers (nonprofit, not engineers). The ranking engine existed so they would stop rebuilding spreadsheets. SignalWeaver's React dashboard is the reporting analog for composite scores — research assistant, not investment advice.

### Tell us about a time you found a gap / defect in a process and improved it

Vylet name-collision: ownership verification rejected valid targets that shared a name with an unrelated business. Fix lifted qualification 79% → 89% with zero change in sourcing volume. That is a false-reject control, not a financial-crime case.

### Interest in financial services (if asked)

CS + Economics at Michigan. Worked campaign-finance filings (MDC), regulatory water-utility compliance data (Lyndbrook), and a financial-research dashboard (SignalWeaver). Payments / servicing / 1LOD controls are the seat I am applying to. I have not worked a card network, AML case, or sanctions list.

---

## HireVue recorded behavioral (3 questions; 30s prep / ~3 min each)

Behavioral is a filter (`recruiting.md` §6). Use STAR. Do not recycle the ETS SWE "I want to design/test/ship on a scrum team" story.

### Why American Express? / Why this internship?

Situation: applying to campus internships; chose this req on purpose. Task: pick a seat where I already do the work. Action: I applied to 26012627 because GS 1LOD wants SQL/Python on messy operational data and recommendations for Technology / Business / Servicing / Compliance — the same shape as MDC (filings → rankings → API for researchers) and Lyndbrook (compliance data → score → shortlist). Amex is a payments and consumer-finance company whose servicing org has to keep financial-crime controls honest; that is more interesting to me than a generic product-SWE intern. Result: eligible May 2028 grad, NYC hybrid, no sponsorship. Gap to name: I have not done AML operations; I am applying for the analytics intern job, not a BSA officer seat.

### Teamwork / collaboration with people who are not engineers

Situation: five-month MCFN contract; I was the only engineer. Task: ship something researchers would actually use. Action: scoped ingestion through endpoints with MCFN; replaced ~2-hour committee pulls; delivered PAC rankings into their public research workflow via Flask on EC2. Result: ~800 hours of manual pulls eliminated across 400 PACs. Lesson: the ranking was the product, not the API.

Backup: Lyndbrook Principal — 15 hours/week of manual prospecting removed by entity matching; score had to match *their* revenue criteria (35% precision), not mine.

### Commercial awareness / how Amex makes money (keep this honest)

Amex is a global payments and consumer-finance company: cards, merchant acquiring, and servicing — not a trading desk (`company.md`). Global Servicing runs travel/concierge and card customer service for consumer, banking, merchant, and commercial customers. 1LOD Financial Crimes Risk & Controls is first-line monitoring and control design (AML, sanctions, payments, anti-corruption) inside that servicing org. I am not going to fake card-unit economics I have not studied on the job; I will talk about why dirty data and weak controls are expensive in a payments network, then point at MDC/Lyndbrook as the work sample.

### Extra STAR bank (if a fourth prompt appears)

- **Attention to detail / data quality:** Vylet SQL freshness checks; name-collision false rejects.
- **Learn quickly:** sole engineer on MDC — no backend team behind me.
- **Failure:** Vylet 79% qualification before the collision fix — say what was wrong, what you changed, 89% after.

---

## Availability

Summer 2027, **hybrid New York, NY** (World Financial Center). Available to start the campus 10-week window (typically June). Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Wrong PDF is a real miss.** Do not upload `software-engineer-intern/Vedant Desai Resume.pdf`. This req's screen_track is `ai-ml`, not `full-stack` (`persona.md`).
- **Do not claim Snowflake, Databricks, Copilot, Fusion, Tableau, Power BI, SAS, Hive, or AML tools.** JD names SQL, Python, and generic analysis/visualization. Stuffing named platforms is a fabrication smell (`persona.md` anti-pattern; `resume.md` §8).
- **Do not keyword-stuff AML / sanctions / anti-corruption into bullets that are not about that work.** Interest is preferred; a fake domain is a screen-call collapse (`resume.md` defensibility).
- **SQL is on the page only in the unquantified Vylet DAL bullet** (`grade.md` minor). If they ask for a number, walk re-scrape/freshness — there is no sized metric in the pool.
- **Lead with MDC + Lyndbrook.** Interview angles in `grade.md`. SignalWeaver is the dashboard analog; do not open with LoRA or Granular DSP.
- **No Amex / GS / 1LOD contact in `network.md`.** Cold HCM apply. A GS or Amex alum referral still beats cold (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Funnel:** resume is the bottleneck (`companies.md` B-tier, ~10–15%). Then HireVue recorded behavioral; two ~30-minute live interviews. HackerRank Easy is the Tech-program analog — unpublished for this Corporate Functions req (`persona.md`). Do not skip behavioral prep because this is "just analytics."
- **Cover letter:** skip unless the form asks; paste from above if it does.
- **Do not apply from this file automatically.** Resume + answers only unless you choose to submit.
