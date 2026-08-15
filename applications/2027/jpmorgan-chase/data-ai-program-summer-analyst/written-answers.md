# JPMorgan Chase — 2027 Data & AI Program Summer Internship – Analyst · Written Application Answers

Draft answers for the Workday / careers apply flow. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Snowflake, Databricks, Copilot, Fusion, Tableau, Spark, or a messy-dataset bullet that is not already in the pool.** Trim to the form's length limit before submitting.

This posting is the **Data & AI Program Analyst** intern seat — **not** the NAMR Software Engineer Program, **not** Code for Good. Title is Analyst.

Program page: https://www.jpmorganchase.com/careers/explore-opportunities/programs/data-analytics-opportunities

Apply early (rolling classes). Exact Workday req ID was not in the public posting dump — use the live careers listing.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/jpmorgan-chase/data-ai-program-summer-analyst/Vedant Desai Resume.pdf` |
| Locations | **Willing to work onsite at any listed site:** New York Metro, Columbus OH, Chicago IL, Delaware Metro, Plano TX, Palo Alto CA. **First choice: Chicago** (Jobright showed Chicago; Midwest from Ann Arbor). Accept assignment to any of the six. |
| Work model | Onsite, Summer 2027 |
| Currently pursuing Bachelor's in a quantitative/technical discipline? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028. Program page also lists Economics as a valued discipline. |
| Graduation date | **May 2028** (inside December 2027–August 2028) |
| Returning to school after internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** (only if asked) |
| Authorized to work permanently in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship (incl. OPT/CPT)? | **No** — this posting offers none; none needed |
| Prior work experience required? | Form may ask; JD says **no prior work experience required**. Do not undersell real internships — they are allowed. |
| How did you hear about this role? | **Jobright**. If Jobright is not listed: **Other** → Jobright |
| Pay (if asked) | Accept posted intern rates (Chicago $45.67/hr; NYC/Jersey City $52.88/hr; Palo Alto $55.28/hr) |

---

## Cover letter / "Why JPMorgan Chase / why Data & AI?" (paste if the form has a box)

I am applying to the 2027 Data & AI Program Summer Internship – Analyst, not the Software Engineer Program.

I want to spend Summer 2027 building end-to-end data and AI work that a business user can measure — pipelines, models, and experiments — inside a bank that actually ships technology at scale. That is this Analyst program: data platforms and pipelines on one side, production-shaped ML and LLMs on the other, with governance and business context in between.

What I can defend:

- **Pipelines and messy source data.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and shipped a Flask REST API on AWS EC2 to Michigan Campaign Finance Network researchers, eliminating ~800 hours of manual pulls across 400 tracked PACs. That is ingest → normalize → serve, not a notebook.
- **Applied ML with a held-out number.** On SignalWeaver I LoRA-fine-tuned Llama 3.1 8B on 3,454 Financial PhraseBank entries and lifted sentiment accuracy from 81% to 96% on a held-out test set, then combined fundamentals and sentiment into an out-of-sample regression (3.39% R²) so the score was not just fitting noise. Research assistant, not investment advice.
- **LLM systems with an eval loop.** I run Vylet, a live PE/search-fund lead-sourcing product ($1,500 MRR, three paying clients). I shipped a Dockerized LangGraph pipeline (30 scored leads in 30 minutes, a 30x speedup) and a LangSmith eval over 20 adversarial cases that lifted extraction faithfulness from 50% to 90% with Pydantic consensus gates. SQL is in the production DAL (asyncpg, injection-safe timestamp checks, automatic re-scrapes).

I have not used Snowflake, Databricks, Copilot, Fusion, or Tableau. I would ramp on the firm's approved stack rather than pretend I already have it.

I can be onsite Summer 2027 (Chicago preferred; any listed location). I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Tell us about a project" / experience with large or complex datasets / ML

**MDC (messy filings → pipeline → API).** Irregular Excel exports and portal caps; Pandas ETL; Flask on EC2; ~800 hours / 400 PACs. This is the grounded "messy dataset" story — do not invent a second one.

**SignalWeaver (model + experiment).** LoRA 81%→96% held-out; out-of-sample regression; financial news + fundamentals. Market data is diverse; do not inflate it into a Snowflake-scale claim.

**Vylet (LLM pipeline + eval + SQL).** LangGraph + LangSmith eval; SQL freshness/re-scrape DAL. Say "agentic / LangGraph" out loud if they ask about agent-based solutions — the resume never uses the word "agent."

**Lyndbrook (scoring experiment).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision against revenue criteria.

---

## Availability

Summer 2027, onsite. Available to start May 2027. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **This is not NAMR SWE.** Do not paste the Code for Good / SWE resume. Use this folder's PDF.
- **Do not claim Snowflake, Databricks, Copilot, Fusion, Tableau, or Spark.** Preferred on the JD; not in the pool. Honest Pandas + AWS EC2 + LangGraph + LoRA beats a keyword lie (`persona.md` anti-pattern).
- **Do not invent a messy-dataset bullet.** MDC irregular filings and SignalWeaver financial news/fundamentals are the real stories.
- **SQL on the page is the unquantified DAL line.** If they ask for SQL impact, walk re-scrape/freshness — there is no sized metric in the pool.
- **No JPMorgan Chase contact in `network.md`.** A UMich alum in the Data & AI program still beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Funnel:** 2027 posting names no OA. Predecessor Data Science Analyst loops reported HackerRank + HireVue. Prep STAR (MDC/Lyndbrook stakeholder delivery) and Easy–Med SQL/Python; do not assume Code for Good is this path.
- **Cover letter:** skip unless the form asks; paste from above if it does.
