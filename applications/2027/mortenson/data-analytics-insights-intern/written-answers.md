# Mortenson — 2027 Data Analytics & Insights Intern · Written Application Answers

Draft answers for the Oracle Cloud HCM apply flow. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Power BI, Tableau, Snowflake, Databricks, R, or construction-domain experience.** Trim to the form's length limit before submitting.

This posting is the **Data Analytics & Insights Intern** seat — **not** a software-engineer intern, **not** help-desk IT. Title is Data Analytics intern. Onsite Robbinsdale, MN. Summer 2027 (May–August).

Apply: https://fa-esgu-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/23342

Simplify: https://simplify.jobs/p/5acb5ba5-b61d-4432-922b-9dea91c7815d

College intern program: https://www.mortenson.com/careers/college

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/mortenson/data-analytics-insights-intern/Vedant Desai Resume.pdf` |
| Location | **Robbinsdale, Minnesota — in person.** Willing to relocate for May–August 2027. |
| Work model | Onsite, Summer 2027 (May–August) |
| Currently pursuing a four-year undergraduate degree in Data Science, Statistics, Economics, Math, or related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028. Economics is explicitly listed; CS is related. |
| Class standing | **Entering junior year** at application (August 2026). Internship term is after junior year (rising senior / completed junior year). Preferred: "currently enrolled as an undergraduate junior." |
| Graduation date | **May 2028** |
| Returning to school after internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** (only if asked) |
| Authorized to work in the United States without sponsorship? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship (incl. H-1B, O-1, TN, CPT, OPT)? | **No** — this posting offers none; none needed |
| Previous related internship? | **Yes** — Data Engineer (MDC / MCFN); Data Engineering Consultant (Lyndbrook Capital); Software Engineer Co-op (CaseStudyPrep.AI). Use MDC + Lyndbrook as the related pair. |
| Pay (if asked) | Accept posted intern rate: **$18/hr starting** (higher by year in school) |
| How did you hear about this role? | **Simplify** (or Jobright / campus listing if that is the actual source). If not listed: **Other** → Simplify |

---

## Cover letter / "Why Mortenson / why Data Analytics & Insights?" (paste if the form has a box)

I am applying to the Summer 2027 Data Analytics & Insights Intern role in Robbinsdale — not a software-engineering intern seat.

I want to spend May–August 2027 supporting internal customers with dashboards, reports, customized KPIs, and predictive-analysis tools that move business and financial performance. That is this team: operational analytics inside a top-25 builder/developer/EPC, not notebook ML and not help-desk IT.

What I can defend:

- **Excel/operational data → pipeline → ranked insight.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I scoped delivery directly with MCFN stakeholders as the only engineer on the contract.
- **Customized scoring / KPI analog.** At Lyndbrook Capital I built a Review Velocity score from EPA ECHO and MassGIS compliance data that filtered 800 acquisition targets to a 280-lead shortlist at 35% precision against the fund's revenue criteria.
- **Predictive analysis with a held-out number.** On SignalWeaver I LoRA-fine-tuned Llama 3.1 8B on 3,454 Financial PhraseBank entries and lifted sentiment accuracy from 81% to 96% on a held-out test set, then combined fundamentals and sentiment into an out-of-sample regression (3.39% R²) and a React dashboard over 90 tickers. Research assistant, not investment advice.
- **SQL in a live pipeline.** I run Vylet, a PE/search-fund lead-sourcing product ($1,500 MRR, three paying clients). The production DAL is asyncpg with injection-safe SQL timestamp checks that trigger automatic re-scrapes. The Dockerized LangGraph pipeline turns a ~30-minute manual process into 30 scored leads in 30 minutes.

I have not used Power BI, Tableau, Snowflake, Databricks, or R, and I do not have construction-site experience. I would ramp on the team's approved stack and on Mortenson's business context rather than pretend I already have them.

I can be onsite in Robbinsdale for Summer 2027 (start May 2027). I return to Michigan afterward (Expected May 2028). I do not need sponsorship. I accept the posted intern rate ($18/hr starting).

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Tell us about a project" / experience with data analysis, visualization, or reporting

**MDC (Excel/filings → ETL → ranked report).** Irregular Excel exports and portal caps; Pandas ETL; PAC funding rankings for a nonprofit research workflow; ~800 hours / 400 PACs. This is the grounded "internal customer + messy operational data" story — do not invent a construction dataset.

**Lyndbrook (customized KPI / scoring).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision against revenue criteria.

**SignalWeaver (predictive + dashboard).** LoRA 81%→96% held-out; out-of-sample regression; React dashboard for composite scores. Do not inflate this into Power BI or a construction-ops dashboard.

**Vylet (SQL + scored pipeline).** asyncpg DAL; SQL freshness/re-scrape; 30 scored leads in 30 minutes. If they ask for SQL impact, walk re-scrape/freshness — there is no sized metric in the pool.

---

## Availability

Summer 2027, **onsite Robbinsdale, MN**. Available to start May 2027. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **This is not a SWE intern req.** Do not paste a generic full-stack resume. Use this folder's PDF.
- **Do not claim Power BI, Tableau, Snowflake, Databricks, R, or construction experience.** Preferred on the JD; not in the pool. Honest Pandas + SQL + React dashboard + LoRA beats a keyword lie (`persona.md` anti-pattern).
- **Do not invent a construction-domain bullet or a new metric.** MDC irregular Excel filings and Lyndbrook scoring are the real operational-analytics stories.
- **SQL on the page is the unquantified DAL line.** If they ask for SQL impact, walk re-scrape/freshness — there is no sized metric in the pool.
- **No Mortenson contact in `network.md`.** A UMich alum in Minneapolis / at Mortenson still beats cold Oracle Cloud HCM (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Funnel:** no published OA. Bottleneck is the resume (`companies.md` D-tier, ~20–30%). Prep STAR (MDC/Lyndbrook stakeholder delivery) and construction-curiosity questions; do not assume a HackerRank.
- **Cover letter:** skip unless the form asks; paste from above if it does.
- **Pay:** $18/hr starting is the posted intern floor; do not negotiate the posting.
