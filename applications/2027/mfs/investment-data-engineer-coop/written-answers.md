# MFS — Spring 2027 Investment Data Engineer Co-op (MFS-231978) · Written Application Answers

Draft answers for Workday `mfs.wd1` / `MFS-Careers` req **MFS-231978**. Grounded in the **live posting and CXS JSON captured 2026-09-30**, `persona.md` (Investment Data Management Office: Python/SQL ingest → ETL → quality/monitoring → data products — **not** a PM intern, **not** generic product-SWE), `grade.md` Interview angles, and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Snowflake, Redshift, BigQuery, Databricks, Tableau, Copilot, Fusion, Aladdin, Airflow, Prefect, dbt, Kafka.

**Form kit email MUST be `verdent06@gmail.com` on every field. Never `vedantde@umich.edu`.** PDF header is **verdent06@gmail.com**. Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship. Work-authorized **Yes**.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Job (live ATS): https://mfs.wd1.myworkdayjobs.com/en-US/MFS-Careers/job/Boston/Spring-2027-Investment-Data-Engineer-Co-op--January---June-_MFS-231978

Apply: https://mfs.wd1.myworkdayjobs.com/en-US/MFS-Careers/job/Boston/Spring-2027-Investment-Data-Engineer-Co-op--January---June-_MFS-231978/apply

Resume: `applications/2027/mfs/investment-data-engineer-coop/Vedant Desai Resume.pdf`

**SHA-256:** `68dbe9b30d6f9c068611d0e4cb5e6ba3ced34cdaca3d5491fc918daa162b5e64`

**THIS IS NOT** a portfolio-manager intern, **NOT** a research-analyst intern, and **NOT** a generic product-SWE intern. This packet is **MFS-231978** Investment Data Engineer Co-op only.

Airtable: `rechgQyKDBSh3SHDZ` (GrokBot Applications). Do not mark Applied in Airtable until a human actually submits.

---

## What was extracted from the live page (2026-09-30)

Pulled without creating an account, without uploading a resume, and without submitting.

### Job posting (public CXS JSON + JSON-LD)

`GET /wday/cxs/mfs/MFS-Careers/job/Boston/Spring-2027-Investment-Data-Engineer-Co-op--January---June-_MFS-231978` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Spring 2027 Investment Data Engineer Co-op (January - June)** |
| Company | **001 Mass Financial Services** (MFS Investment Management) |
| Requisition | **MFS-231978** · jobPostingId `Spring-2027-Investment-Data-Engineer-Co-op--January---June-_MFS-231978` · jobPostingInfo.id `46270135cf5010015028e2bee9730000` |
| Location | **Boston** · United States of America |
| Time type | **Full time** |
| Posted | **Posted Today** · `startDate` **2026-09-30** · JSON-LD `datePosted` **2026-09-30** |
| End date | Workday `endDate` **2026-10-30** · JSON-LD `validThrough` **2026-10-30** |
| Pay (JD body) | **$21.00–$25.00/hr** |
| Term (JD body) | **Wednesday, January 13 through Friday June 25, 2027** · Monday–Friday · **35–40 hours** |
| Work model | `#LI-HYBRID` — hybrid (remote/onsite) unless otherwise stated |
| Apply | Workday `/apply`. `canApply: true`. `includeResumeParsing: true` |
| `questionnaireId` | `d8e4dfc372491000bd4e312ac5530000` |

### Start Your Application / wizard (live stop)

- `/apply` HTML is the Workday candidate-experience SPA (HTTP 200). Visible form widgets are JS-rendered (`<div id="root"></div>`).
- CXS `GET .../apply` returned **HTTP 406** without an account.
- CXS `POST .../apply/start` returned **HTTP 405** without an account.
- CXS `GET .../questionnaire/d8e4dfc372491000bd4e312ac5530000` returned **HTTP 406** without an account.
- **No essay prompts, knockout radios, or My Information fields were visible on the public page.** Do not invent extra essays. If later pages differ, answer the actual question.

Typical Workday apply chrome after Apply (confirm live; not rendered without login on this capture):

1. **Create Account/Sign In** ← live stop
2. **Autofill with Resume** / **Apply Manually** / **Use My Last Application**
3. **My Information**
4. **My Experience**
5. **Application Questions**
6. **Voluntary Disclosures**
7. **Self Identify**
8. **Review**

### Create Account (typical Workday — confirm live labels)

Do **not** create an account from this agent.

| If the live label is | Answer |
| --- | --- |
| Email Address * | **verdent06@gmail.com** (never vedantde@umich.edu) |
| Password * | **Your real password.** Not stored in this repo |
| Verify New Password * | Same as Password |
| Terms / I Agree | **Check** if you consent |
| Already have an account? | Sign In if you already created one |

---

## Knockouts (read first)

1. Currently pursuing a Bachelor’s in Computer Science, Data Science, or related (junior or senior preferred) — **clears.** B.S. Computer Science and Economics, University of Michigan, Expected May 2028. Jan–Jun 2027 = Junior year.
2. Boston hybrid, January 13 – June 25 2027, Monday–Friday, 35–40 hours — **Yes.** Relocate from Northville, MI for the term; return to Michigan afterward.
3. Program designed for students **currently enrolled in a co-op program** through their college — **do not invent UMich co-op-office enrollment.** If a Yes/No asks “Are you currently enrolled in a university co-op program?” answer **No** unless UMich actually enrolls this term. Availability is a gap-term Jan–Jun 2027. A Yes would be a fabrication (`recruiting.md` Part I §1).
4. Work authorization — **no visa line on this JD.** Answer **US citizen / no sponsorship**.
5. Python or SQL — **Python Yes. SQL Yes** — through use on the PDF. Do not check Snowflake / Redshift / BigQuery.
6. Agile (Scrum/Kanban) — plus, not a knockout. Honest: informal sprints on Vylet / MDC; do not claim a certified Scrum Master.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on co-op-program enrollment, location, dates, or Snowflake/Redshift/BigQuery.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular if asked.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66, Junior, 96 credits by Summer 2027.
- Languages you can defend: **Python, SQL** (on this PDF). TypeScript/React if they ask about the dashboard. **Do not check Snowflake, Redshift, BigQuery, Databricks, Tableau.**

---

## Knockout / structured fields (fill exactly)

### My Information (login wall — standard Workday; confirm live labels)

| Exact label (typical Workday) | Answer |
| --- | --- |
| Country * | **United States of America** |
| First Name * | Vedant |
| Last Name * | Desai |
| Address Line 1 | **49032 Freestone Dr** |
| City | **Northville** (not Ann Arbor) |
| State | **Michigan** |
| Postal Code | **48168** |
| Email Address | **verdent06@gmail.com** |
| Phone Device Type * | **Mobile** |
| Country Phone Code | **United States of America (+1)** |
| Phone Number | **(248) 704-4852** |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub / Website | https://github.com/Verdent06 · https://vyletdata.com if a second URL |
| How Did You Hear About Us? | The board you actually used. **No MFS contact in `network.md` — do not pick Employee Referral.** If you opened mfs.wd1: **Career Websites** / Company website. If LinkedIn: **Job Board → LinkedIn**. |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### My Experience · Education

| Exact label | Answer |
| --- | --- |
| School or University * | **University of Michigan** (University of Michigan-Ann Arbor if the typeahead has it) |
| Degree * | **Bachelor of Science (BS)** |
| Field of Study | **Computer Science** (add **Economics** if a second row / dual-degree field is required) |
| Overall Result (GPA) | **3.66** |
| From | **08/2025** (started **08/31/2025**) |
| To (Actual or Expected) | **05/2028** |
| Currently enrolled | **Yes** |
| High School | **Northville High School** |
| High School graduation date | **05/19/2025** |

### Work history on the form (not the PDF)

| Employer | How to enter |
| --- | --- |
| Vylet | **Job.** Founder. May 2026 – Present. Remote / Northville, MI. |
| CaseStudyPrep.AI | **Job.** Software Engineer Co-op (Voice AI). Dec 2025 – May 2026. Remote. |
| Michigan Data Consulting (MDC) | **Extracurricular / organization / project only.** |
| Lyndbrook Capital | **Omit from the form** (still on the PDF). |
| SpaceXAI Campus Lead Ambassador | **Extracurricular only.** |
| Granular Synthesizer / SignalWeaver | **Not jobs.** |
| Awards / honors | **None.** |

### Application questions (login wall — confirm live labels; do not invent wording)

Workday `questionnaireId` `d8e4dfc372491000bd4e312ac5530000` was **HTTP 406**. If a later step shows these (or the JD qualifications restated as radios), use:

| If the live label is | Answer |
| --- | --- |
| Currently pursuing CS / Data Science / related? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Class standing / junior or senior preferred | **Junior** (Expected May 2028; term is Jan–Jun 2027) |
| Available January 13 – June 25, 2027, Monday–Friday, 35–40 hours? | **Yes** |
| Can you work hybrid in Boston, MA? | **Yes** — relocate from Northville, MI for the term; return to Michigan afterward |
| Currently enrolled in a university co-op program? | **No** unless UMich actually enrolls this term. Do not invent co-op-office enrollment |
| Are you legally authorized to work in the United States? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| Returning to school after the co-op? | **Yes** — Expected May 2028 |
| Graduation date | **May 2028** |
| Ever worked for MFS? | **No** |
| Relatives at MFS? | **No** (unless true) |
| Python | **Yes** — on the PDF through use |
| SQL | **Yes** — SQL freshness on Vylet; Postgres persist on SignalWeaver |
| Snowflake / Redshift / BigQuery | **No** — do not check. Walk Pandas ETL + Postgres + Docker |
| Agile / Scrum / Kanban | Informal sprints only. Do not claim a Scrum certification |
| AWS | **Yes** — EC2 (MDC) on the PDF |
| Docker | **Yes** — Vylet Dockerized pipeline |
| How did you hear | Company website / the board you used. **Not** Employee Referral |
| Willing to complete post-offer background? | **Yes** |

Voluntary Disclosures / Self Identify: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

Review: check email is **verdent06@gmail.com**, Boston, Jan 13–Jun 25 2027, PDF attached. Do not submit from this agent.

---

## Cover letter / additional information (paste if Workday has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

MFS — Spring 2027 Investment Data Engineer Co-op (MFS-231978)
Boston, MA · January 13 – June 25, 2027

I am applying for the Spring 2027 Investment Data Engineer Co-op on the Investment Data Management Office (Workday MFS-231978) — not a PM intern and not a generic product-SWE intern. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work Monday–Friday, 35–40 hours, hybrid in Boston from January 13, 2027 through June 25, 2027 and return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

I have not used Snowflake, Redshift, or BigQuery. What I can defend is messy multi-source records → quality/ranking → a report or API a non-builder used.

What I would bring:

- **Irregular files → pipeline → ranked output for a stakeholder.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month contract. Closest analog to ingesting internal/external records and serving them.
- **Multi-source entity resolution / scoring.** At Lyndbrook Capital I built a PWSID entity database from EPA ECHO and MassGIS and a Review Velocity score that filtered 800 acquisition targets to a 280-lead shortlist (35% precision).
- **SQL freshness + pipeline quality.** On Vylet I wrote injection-safe SQL timestamp checks that re-scrape stale records, fixed a name-collision defect that lifted lead-qualification from 79% to 89%, and automated a ~30-minute process into a 30-scored-lead / 30-minute Dockerized pipeline (30x). Closest analog to quality, resiliency, and orchestration.
- **Postgres + a dashboard you can click — not Snowflake.** SignalWeaver: FastAPI scores and a React/TypeScript dashboard over 90 tickers persisted in Postgres (9.1s p50). Research assistant, not advice.

Vedant Desai

---

## Short paste blurb (if the form has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to Spring 2027 Investment Data Engineer Co-op MFS-231978 in Boston — not a PM intern. I ship Python/SQL pipelines: a Pandas ETL on irregular Excel filings that cut ~800 hours of pulls across 400 PACs, a Flask report API on EC2, SQL freshness checks and a 79%→89% quality fix on Vylet, and a React/Postgres dashboard. I have not used Snowflake, Redshift, or BigQuery. U.S. citizen; no sponsorship. I can be in Boston hybrid January 13 – June 25, 2027.

---

## "Why MFS / why this co-op?"

I want January–June 2027 in Boston on MFS-231978: ship pipelines the Investment Data Management Office can actually use for investors, risk, and client reporting — not a PM coverage intern and not a generic product-SWE rotation. I have not interned on Snowflake or Redshift. The analog I can defend is MDC (messy Excel → PAC ranking → Flask report for a nonprofit) plus Vylet if they ask how I keep data fresh and fix a quality defect. Dual CS + Economics is why I’m interested in learning financial instruments and data on the job. I will not invent a childhood-mutual-fund story the page cannot support.

---

## "Tell us about a project" / experience with data / Python / quality

**MDC (messy Excel → pipeline → ranking → stakeholder report).** Irregular filings; Pandas ETL; PAC ranking; ~800 hours / 400 PACs; Flask REST on EC2 to researchers. Best analog to ingest internal/external records and serve them. Form-kit: extracurricular.

**Lyndbrook (multi-source entity analog).** EPA + MassGIS → PWSID entity DB; Review Velocity 800 → 280 at 35% precision. Water-utility operators, not mutual-fund holdings. Say that out loud if they ask about domain.

**Vylet (quality + orchestration).** SQL timestamp / re-scrape; 79% → 89% name-collision fix; Dockerized 30x pipeline with Redis/Celery. Closest analog to data quality, resiliency, monitoring, and orchestration tools.

**SignalWeaver (Postgres + dashboard analog).** FastAPI + React/Postgres; 90 tickers; 9.1s p50. Not Snowflake. Research assistant, not advice. Do not lead with LoRA.

---

## Availability

Full-time co-op, **Boston hybrid**, **January 13 – June 25, 2027**, Monday–Friday, **35–40 hours**. Returning to the University of Michigan (Expected May 2028). Housing: self-sourced; JD does not print a stipend. Comp: **$21–$25/hr** as printed. Post-offer background: **Yes**.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field and on the PDF header.** Do not type `vedantde@umich.edu`.
- **Do not claim Snowflake, Redshift, BigQuery, Databricks, or Tableau.** Walk Pandas-on-Excel-exports and SignalWeaver as the dashboard analog (`persona.md` anti-pattern).
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). Awards = **None**.
- **Boston hybrid Jan 13–Jun 25 is not a skip.** Say yes. Relocate from Northville for the term.
- **Co-op-program radio:** if they ask whether you are enrolled in a university co-op program, answer **No** unless UMich actually enrolls you. Do not invent it.
- **Referral:** none in `network.md`. A fake employee name is a knockout.
- **Cover letter:** skip unless the form asks; paste from the letter above if it does.
- **Resume is the intern bottleneck** (`companies.md` C-tier, no published OA, ~15–25%). Posted **2026-09-30** — apply this wave (`recruiting.md` §8). Workday `endDate` **2026-10-30**.
- **Transcript:** upload unofficial UMich transcript if a later step requires it. Not stored in this repo.
- **Airtable:** `rechgQyKDBSh3SHDZ`. Do not apply from this agent. Do not email this packet.
