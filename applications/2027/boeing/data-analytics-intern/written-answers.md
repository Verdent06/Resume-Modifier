# Boeing — Summer 2027 Internship Program (Paid) – Data Analytics Intern · Written Application Answers

Draft answers for the Workday / jobs.boeing.com apply flow. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent aerospace experience, Tableau, Power BI, Snowflake, Databricks, or a clearance already held.** Trim to the form's length limit before submitting.

This posting is the **IT / Data & Analytics** intern family — **not** the SWE/embedded Engineering track. Title is Data Analytics Intern. Job ID **JR2026520976**.

Apply: https://jobs.boeing.com/job/everett/boeing-summer-2027-internship-program-paid-data-analytics-intern/185/98720782192

IT internships hub: https://jobs.boeing.com/it-internships

Rolling through **Oct 23, 2026**. Apply in this wave (`persona.md`: resume is the bottleneck).

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/boeing/data-analytics-intern/Vedant Desai Resume.pdf` |
| Locations | **Willing to work at any listed US site** (hybrid / onsite / virtual as the team assigns). **First choice: Chicago** (Midwest from Ann Arbor). Everett / Seattle / Dallas also fine. Do not self-reject on location. |
| Work model | Summer 2027, 10–12 weeks, full-time. Onsite / hybrid / virtual as assigned. First shift. Relocation if the seat offers it. |
| Currently enrolled student? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (on or after August 2027) |
| Returning to school after internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| Ability to work full-time 10–12 weeks Summer 2027? | **Yes** |
| GPA | **3.66 / 4.0** (preferred floor is 3.0) |
| US Person (22 C.F.R. § 120.15) / Export Control | **Yes** — US citizen (citizen, LPR, refugee, or asylee all qualify; you are a citizen) |
| Authorized to work in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship? | **No** — posting offers none; none needed |
| Do you currently hold a U.S. government security clearance? | **No** |
| Eligible to obtain and maintain a Security Clearance? | **Yes** — US citizen. This posting requires a clearance; eligibility is the honest line, not Secret/TS in hand. |
| Drug-free workplace / post-offer testing | **Yes** — I can comply |
| How did you hear about this role? | **Other** → Jobright / this JD, unless a listed source matches. No Boeing contact in `network.md`. |
| Pay (if asked) | Accept the posted intern range ($44,000–$89,000) |
| Languages / tools you can interview in | **Python, SQL, Pandas, PyTorch, Flask, AWS (EC2), Docker.** Do **not** check Tableau, Power BI, Snowflake, Databricks, CATIA, or clearance-in-hand. |

---

## Cover letter / "Why Boeing / why Data Analytics?" (paste if the form has a box)

I am applying to the Summer 2027 Internship Program as a Data Analytics Intern (JR2026520976) — the IT / Data & Analytics path, not the software-engineering or embedded track.

I want to spend Summer 2027 on applied data work that a business user can measure: ingest messy sources, build a pipeline, and ship an insight or model. That is Boeing Analytics — data science, analytics, applied ML/AI, and software delivering solutions to the business, partners, and customers. I do not have aerospace internships. The analog I can defend is industrial messy-data work already shipped to non-builder stakeholders.

What I can defend:

- **Pipelines and messy source data.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and shipped a Flask REST API on AWS EC2 to Michigan Campaign Finance Network researchers, eliminating ~800 hours of manual pulls across 400 tracked PACs. That is ingest → normalize → serve, not a notebook.
- **Scoring and operational shortlists.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a unified PWSID entity database, delivered 800+ Day-1 acquisition targets, and built a Review Velocity score that filtered those to a 280-lead shortlist at 35% precision against the fund's revenue criteria.
- **Applied ML with a held-out number.** On SignalWeaver I LoRA-fine-tuned Llama 3.1 8B on 3,454 Financial PhraseBank entries and lifted sentiment accuracy from 81% to 96% on a held-out test set, then combined fundamentals and sentiment into an out-of-sample regression (3.39% R²) so the score was not just fitting noise. Research assistant, not investment advice.
- **LLM systems with an eval loop.** I run Vylet, a live PE/search-fund lead-sourcing product ($1,500 MRR, three paying clients). I shipped a Dockerized LangGraph pipeline (30 scored leads in 30 minutes, a 30x speedup) and a LangSmith eval over 20 adversarial cases that lifted extraction faithfulness from 50% to 90% with Pydantic consensus gates. SQL is in the production DAL (asyncpg, injection-safe timestamp checks, automatic re-scrapes).

I have not used Tableau, Power BI, Snowflake, or Databricks. I would ramp on the team's approved stack rather than pretend I already have it.

I can work full-time Summer 2027 at any listed site (Chicago preferred; Everett / Seattle / Dallas fine). I return to Michigan afterward (Expected May 2028). I am a U.S. citizen, I do not need sponsorship, and I do not currently hold a clearance — I am eligible to obtain one if this seat requires it.

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Why aerospace / why Boeing?"

I want to apply data pipelines and measured models to an industrial product company, not a consumer app. Boeing Analytics is that seat: enterprise data used by the business, partners, and customers around commercial and defense programs.

I have not interned on aircraft or flight ops. The closest analog is MDC (irregular filings → Pandas ETL → API for researchers) and Lyndbrook (public regulatory data → scored shortlist). I can talk about that work in STAR. I will not invent CATIA, shop-floor IoT, or a childhood-airport story the page cannot support.

---

## "Tell us about a project" / experience with large or complex datasets / ML

**MDC (messy filings → pipeline → API).** Irregular Excel exports and portal caps; Pandas ETL; Flask on EC2; ~800 hours / 400 PACs. This is the grounded "messy dataset" story — do not invent a second one or an aerospace dataset.

**Lyndbrook (scoring experiment).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision against revenue criteria. Public operational data, not a notebook.

**SignalWeaver (model + experiment).** LoRA 81%→96% held-out; out-of-sample regression; financial news + fundamentals. Do not inflate it into a Snowflake-scale claim.

**Vylet (LLM pipeline + eval + SQL).** LangGraph + LangSmith eval; SQL freshness/re-scrape DAL. If they ask about SQL impact, walk re-scrape/freshness — the resume line has no sized metric (`grade.md` out of rails).

---

## Availability

Summer 2027, 10–12 weeks, full-time. Available to start mid-May / June 2027. Returning to the University of Michigan after the internship (Expected May 2028). Willing to relocate to any listed site.

---

## Notes for the applicant (not for submission)

- **This is not the SWE/embedded Engineering intern.** Do not paste a C++/audio-DSP or generic full-stack resume. Use this folder's PDF.
- **Do not claim Tableau, Power BI, Snowflake, Databricks, or aerospace internships.** Preferred "passion for aerospace" is a STAR answer, not a skills lie (`persona.md` anti-pattern).
- **Citizenship YES, clearance in-hand NO.** Eligible-to-obtain is the honest line. Do not write Secret/TS.
- **SQL on the page is the unquantified DAL line.** If they ask for SQL impact, walk re-scrape/freshness — there is no sized metric in the pool (`grade.md`).
- **Flask/EC2 is tenure-and-stack.** Pair it verbally with the 800-hour ETL.
- **No Boeing contact in `network.md`.** A UMich alum in Boeing Analytics / IT still beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Funnel:** Workday resume screen (rolling through Oct 23). No standard OA. Occasional HireVue or skill-alignment survey, then 1–3 live behavioral (why aerospace, why Boeing, stakeholder delivery). Prep STAR (MDC/Lyndbrook), not LeetCode.
- **Cover letter:** skip unless the form asks; paste from above if it does.
