# Kodiak Robotics — Winter 2027 Intern, Data Engineering (Mountain View, Greenhouse 4396622009 / R-401) · Written Application Answers

Draft answers for the public Greenhouse apply flow. Labels and dropdowns captured from `https://boards-api.greenhouse.io/v1/boards/kodiak/jobs/4396622009?questions=true` and the live apply page `https://job-boards.greenhouse.io/kodiak/jobs/4396622009` on 2026-09-06 (job `id` 4396622009; `first_published` 2026-09-04; `education` = `education_optional`; requisition **R-401**). Grounded in `persona.md` (data-platform DE: Python/SQL ETL, schema analog, quality/validation, custom dashboard — **not** AI/ML intern 4377407009, **not** Simulation 4378662009) and `context.md` metrics only.

**Do not invent:** Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, AuroraDB, Elasticsearch, QuickSight, Kibana, Terraform, ROS, radar, FRC, LoRA-as-the-job.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** Phone **248-704-4852**. US citizen, no sponsorship.

**Do not submit from this agent.** Paste pack only.

Apply: https://job-boards.greenhouse.io/kodiak/jobs/4396622009
Resume: `applications/2027/kodiak/data-engineering-intern-winter/Vedant Desai Resume.pdf`

**SHA-256:** `13934da141095191d816b5a22284cfa440e1c29ded9ece095c3f212180c9c23e`

**Form kit (this apply only):** email **verdent06@gmail.com**. Resume PDF header still uses the umich address from `context.md`; that is expected. Phone **248-704-4852**. U.S. citizen, no sponsorship. GPA **3.66**. Expected **May 2028**. Class standing on forms: **Junior**. Address **49032 Freestone Dr, Northville, MI 48168**. LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06. SAT **1510** if asked. DOB **12/16/2006** if asked. Valid US driver’s license: **Yes** if asked.

---

## Knockout / structured fields (fill exactly)

Exact Greenhouse labels. `*` = `required: true` on the API. Live page also shows **Country** next to Phone (not in the public `questions` array — fill it).

| Field (exact label) | Required | Answer |
| --- | --- | --- |
| First Name | * | Vedant |
| Last Name | * | Desai |
| Preferred First Name | | (leave blank) |
| Email | * | **verdent06@gmail.com** |
| Country | live page | **United States** |
| Phone | * | 248-704-4852 |
| Resume/CV | * | `applications/2027/kodiak/data-engineering-intern-winter/Vedant Desai Resume.pdf` (pdf/doc/docx/txt/rtf) |
| Cover Letter | | **No cover-letter field** on this Greenhouse job. Do not invent an upload. Paste the letter below only if a later step appears. |
| LinkedIn Profile | | https://linkedin.com/in/vedantde06 |
| Website | | https://github.com/Verdent06 |
| Will you now or in the future require sponsorship for employment in the US? | * | **No**. Live options: Yes, No. US citizen — none now or later. |

Greenhouse Education widget is **`education_optional`** (not a hard widget). Fill it anyway so school filters can see Michigan:

| Education widget | Answer |
| --- | --- |
| School | University of Michigan |
| Degree | Bachelor's / Bachelor of Science |
| Discipline | Computer Science (dual CS + Economics — pick CS if one) |
| End date / Expected | **May 2028** |
| Did you graduate? | **No** if asked |

If a later step asks fields not on this public form:

| If asked | Answer |
| --- | --- |
| Address | 49032 Freestone Dr, Northville, MI 48168 |
| GitHub | https://github.com/Verdent06 |
| GPA | **3.66 / 4.0** |
| Class standing | **Junior** (Expected May 2028). Winter 2027 intern term. |
| US citizen | **Yes** |
| Work authorized without sponsorship now and in the future | **Yes** |
| SAT | **1510** |
| Date of birth | **12/16/2006** |
| Valid US driver’s license | **Yes** |
| Willing to relocate / onsite Mountain View Jan 2027 | **Yes.** Intern housing is self-sourced. Returning to Michigan after the term. |
| Start date | **January 2027** (program start). If a day is required: **1/4/2027** (first Monday in January 2027) |
| End date | Flexible; **12–16 weeks** from January 2027 (JD). If a day is required: **4/16/2027** (~15 weeks) |
| How did you hear | Not on this form. If added: **Company website** / Greenhouse. Do **not** pick Employee Referral — no Kodiak contact in `network.md`. |
| Languages you can interview in | **Python, SQL.** Also TypeScript. Do **not** check Java, C++ (this is the DE intern, not Simulation/Controls), Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, Aurora, Elasticsearch, QuickSight, Kibana, Terraform, ROS. |
| US person / export-control / citizenship (if this seat is gated) | **Yes** — U.S. citizen. Do not claim a clearance. |

Voluntary EEO / disability / veteran (API `compliance` + live “U.S. Standard Demographic Questions”): **I do not want to answer** / **I don't wish to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

---

## Cover Letter (no upload on this Greenhouse job — paste only if a later box appears)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Kodiak Robotics — Winter 2027 Intern, Data Engineering
Mountain View, CA · Greenhouse 4396622009 / R-401

I am applying to Winter 2027 Intern, Data Engineering (Greenhouse 4396622009 / R-401) — not AI/ML intern 4377407009 and not Simulation 4378662009. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen. I do not need visa sponsorship now or later. I can be onsite in Mountain View from January 2027 for 12–16 weeks and I return to Michigan afterward. I will arrange housing.

I want this seat because the work is stores, pipelines, and reporting for robotics and safety datasets — not training Driver models and not a generic SWE rotation. What I can defend:

- **Ingest → ETL → serve.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and a production Flask REST API on AWS EC2, eliminating ~800 hours of manual pulls across 400 tracked PACs.
- **Schemas / entity resolution.** At Lyndbrook I aggregated EPA ECHO and MassGIS into a PWSID entity database and delivered 800+ Day-1 targets; a Review Velocity score cut that list to 280 leads at 35% precision.
- **Quality / SQL / pipelines.** On Vylet I own an asyncpg layer with injection-safe SQL timestamp checks that trigger re-scrapes, and I fixed a name-collision defect that lifted lead-qualification from 79% to 89%. The pipeline is Dockerized (Redis/Celery), 30 scored leads in 30 minutes.
- **Custom dashboards.** SignalWeaver is a React/TypeScript dashboard with scores persisted to Postgres — the analog I have to QuickSight/Kibana, not those products.

I have not used AuroraDB, Elasticsearch, QuickSight, Kibana, Snowflake, Databricks, Tableau, or Terraform. I would ramp on Kodiak’s stores and reporting factory rather than pretend I already have them. I care about dependable data next to a safety-critical system; I interview in Python and SQL.

Vedant Desai

---

## Short “why Kodiak / why this intern” (if a box is shorter than a letter)

I want a Winter 2027 intern writing SQL and Python pipelines next to robotics and safety datasets — ingest, quality, stores, reporting — not training models and not Simulation/C++.

MDC: Requests + Pandas ETL + Flask on EC2 (~800 hours / 400 PACs). Lyndbrook: EPA/MassGIS → PWSID entity DB, 800 → 280 at 35% precision. Vylet: SQL freshness checks, 79% → 89% anomaly fix, Dockerized pipeline. SignalWeaver: custom React/TypeScript dashboard persisted to Postgres.

No Aurora, Elasticsearch, QuickSight, Kibana, Snowflake, or Databricks in my pool. Mountain View onsite, January 2027, 12–16 weeks, housing self-sourced. US citizen; no sponsorship. Expected May 2028.

---

## Availability / location

Winter 2027, full-time, **onsite Mountain View, CA**, January 2027 start, 12–16 weeks. Willing to relocate from Northville, MI. Intern housing is self-sourced (JD). Returning to the University of Michigan after the internship (Expected May 2028). Class standing: **Junior**. Valid US DL: **Yes**.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Greenhouse field.** Do not type `vedantde@umich.edu`.
- **This is Data Engineering 4396622009 / R-401 only.** Do not apply this packet to AI/ML intern 4377407009 or Simulation 4378662009.
- **Do not claim AuroraDB, Elasticsearch, QuickSight, Kibana, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, Terraform, ROS, or FRC.** Custom dashboard + Postgres/AWS EC2 is the honest analog (`persona.md`).
- **Skip ML-research framing.** Do not lead with LoRA / SignalWeaver sentiment models. Lead with MDC ETL and Vylet SQL/quality.
- **Cover letter is not on this form.** Skip unless a later step asks; paste from above if it does.
- **Sponsorship = No.** US citizen. Export-control language on some Kodiak seats — citizenship is a plus; do not claim a clearance.
- **No Kodiak contact in `network.md`.** Randy Starr is Greenhouse HM metadata, not a referral.
- **Endorsed** assists the initial screen (AEDT since 2026-01-01). Humans decide. Optional separate review: careers@kodiak.ai with subject “Separate Review Request”.
- **Funnel:** resume-first (`company.md`); unpublished Python/SQL/pipeline conversation after recruiter. Apply in this first-wave window (posted 2026-09-04).
- **Housing is on you.** Mountain View. Confirm you can be there January 2027 before you submit.
- **WORTH_IT.md is YES.** Do not overwrite.
