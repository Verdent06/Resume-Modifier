# WEC Energy Group / We Energies — Intern - Renewables Data Analytics (Summer 2027) · Written Application Answers

Draft answers for the WEC Career finder apply flow (Req **7118**). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Power BI, Tableau, Snowflake, Databricks, VBA, Athena, T-SQL, SCADA, or renewable-energy operations experience.** Trim to the form's length limit before submitting.

Apply: https://careers.wecenergygroup.com/We_Energies/job/Milwaukee-Intern-Renewables-Data-Analytics-WI-53203/1419740100/

Applications reviewed rolling; interviews start after a qualified submit. Listed end date **11/15/2026**. Apply now.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/wec-energy/renewables-data-analytics-intern/Vedant Desai Resume.pdf` |
| Location | **Willing to work hybrid in Milwaukee, WI or Green Bay, WI.** First choice: Milwaukee (closer travel from Ann Arbor). Accept Green Bay. |
| Work model | Hybrid Summer 2027; willing to travel to generation sites in WI, MI, MN, IA, IL, or IN |
| Currently pursuing Bachelor's in DS / DA / CS / Engineering or related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (after June 2027) |
| Returning to school after internship? | **Yes** — Fall 2027 and Winter 2028 remain. Open to the posted part-time fall extension if offered |
| GPA | **3.66 / 4.0** (minimum 2.8) |
| Valid driver's license? | **Confirm before submit** — required on the JD; not recorded in `context.md`. If you have one: **Yes**. If not: do not apply until you do |
| Authorized to work in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship (incl. OPT/CPT)? | **No** — posting excludes temporary visas and offers no sponsorship |
| How did you hear about this role? | **Other** / Job board you actually used. Do not invent a referral — none in `network.md` |
| Pay $23.10–$27.55/hr | **Yes** — accept the posted intern range |

---

## Cover letter / "Why WEC / why Renewables Data Analytics?" (paste if the form has a box)

I am applying to the Summer 2027 Intern - Renewables Data Analytics seat (Req 7118) on the We Energies / Wisconsin Public Service Renewables Analytics team — Milwaukee or Green Bay, hybrid.

I want to spend the summer on the work this team actually does: ingest operational data, keep the pipelines and metadata databases honest, and turn that into fleet-level metrics people can use. I have not interned on wind, solar, or battery hardware. I have shipped the data path — messy sources in, a database or API out, a number on what it saved.

What I can defend:

- **Messy ingest → ETL → serve.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and shipped a Flask REST API on AWS EC2 to Michigan Campaign Finance Network researchers, eliminating ~800 hours of manual pulls across 400 tracked PACs. That is the analog to SCADA-to-repository work. I have not used SCADA.
- **Entity databases and fleet-style scoring.** At Lyndbrook I aggregated EPA ECHO and MassGIS into a PWSID entity database for a search fund targeting water-utility operators and delivered 800+ Day-1 targets. A Review Velocity score proxied fleet expansion from public compliance data and cut that list to 280 leads at 35% precision against their revenue criteria.
- **SQL, pipelines, and a dashboard.** On Vylet I own a production asyncpg DAL with injection-safe SQL freshness checks that trigger re-scrapes. On SignalWeaver I built a React dashboard over scores persisted in Postgres and served them through FastAPI.

I have not used Power BI, Tableau, Snowflake, Databricks, or VBA. I would ramp on the team's approved stack rather than pretend I already have it.

I can be hybrid in Milwaukee or Green Bay for Summer 2027 and travel to generation sites. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Tell us about a project" / data pipelines / SQL / messy data

**MDC (messy filings → Pandas ETL → Flask API).** Irregular Excel exports and portal caps; ~800 hours / 400 PACs. This is the grounded messy-dataset story — do not invent a second one or call it SCADA.

**Lyndbrook (entity DB + fleet scoring).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision. Water-utility operators, not renewables generation. Say that out loud if they ask about domain.

**Vylet (SQL + pipeline).** asyncpg DAL; stale-timestamp checks; automatic re-scrapes. Dockerized LangGraph pipeline, 30 scored leads in 30 minutes. If they ask DevOps/GitHub: Docker + the public GitHub on the resume — do not inflate it into a platform-engineering story.

**SignalWeaver (dashboard / KPI analog).** React dashboard; FastAPI; pgvector search (49ms p50). Research assistant, not investment advice. Do not call this Power BI.

---

## Availability

Summer 2027, hybrid Milwaukee or Green Bay. Available to start May/June 2027. Returning to the University of Michigan after the internship (Expected May 2028). Open to the posted part-time fall extension.

---

## Notes for the applicant (not for submission)

- **Driver's license is a hard minimum.** Confirm you have a valid one before you click submit. It is not in `context.md`.
- **Do not claim Power BI, Tableau, Snowflake, Databricks, VBA, Athena, T-SQL, SCADA, or renewables-ops experience.** Preferred on the JD; not in the pool. Honest Python/SQL/Pandas/ETL beats a keyword lie (`persona.md` anti-pattern).
- **Do not invent a messy-dataset bullet.** MDC irregular filings is the real one.
- **Location is not a skip.** Say yes to Milwaukee or Green Bay and to site travel.
- **No WEC / We Energies contact in `network.md`.** A UMich alum in Milwaukee still beats cold Career finder (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Cover letter:** skip unless the form asks; paste from above if it does.
- **Funnel:** rolling resume screen; no standard intern OA; behavioral + possible job-specific test (`company.md`).
