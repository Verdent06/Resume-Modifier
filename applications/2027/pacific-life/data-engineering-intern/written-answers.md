# Pacific Life — Summer 2027 Data Engineering Internship (R17828) · Written Application Answers

Draft answers for Workday `pacificlife.wd1` / `PacificLifeCareers` req **R17828**. Grounded in `persona.md` (applied DE: ingest → ETL/transform → quality/persist → serve — **not** Actuarial intern, **not** Software Engineering intern, **not** Sales intern) and `context.md` identity/metrics. First-person, honest, defensible under "walk me through this."

**Do not invent:** R, Salesforce, Alteryx, SAS, Tableau, MSSQL, Mongo/NoSQL-as-claimed, Kaggle, Copilot, Fusion, insurance-admin platforms.

**Form kit email MUST be `verdent06@gmail.com` on every field. Never `vedantde@umich.edu`.** PDF header is **verdent06@gmail.com**. Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship. Work-authorized **Yes**.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Job (live ATS): https://pacificlife.wd1.myworkdayjobs.com/en-US/PacificLifeCareers/job/Newport-Beach-CA-700/Summer-2027-Data-Engineering-Internship_R17828

Apply: https://pacificlife.wd1.myworkdayjobs.com/en-US/PacificLifeCareers/job/Newport-Beach-CA-700/Summer-2027-Data-Engineering-Internship_R17828/apply

Resume: `applications/2027/pacific-life/data-engineering-intern/Vedant Desai Resume.pdf`

**SHA-256:** `e024a0ac6e71c71e0935c5f70ac6b390fdcf351ffedf9e9a2cd843980da1ddbf`

**THIS IS NOT** the Actuarial intern, **NOT** the Software Engineering intern, and **NOT** the Sales intern. This packet is **R17828** Data Engineering Internship only.

---

## What was extracted from the live page (2026-09-26)

Pulled without creating an account, without uploading a resume, and without submitting.

### Job posting (public CXS JSON + JSON-LD)

`GET /wday/cxs/pacificlife/PacificLifeCareers/job/Newport-Beach-CA-700/Summer-2027-Data-Engineering-Internship_R17828` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Summer 2027 Data Engineering Internship** |
| Company | **Pacific Life Insurance Company** |
| Requisition | **R17828** · jobPostingId `Summer-2027-Data-Engineering-Internship_R17828` · jobPostingInfo.id `69563ce65ec31002084151df36d80000` |
| Location | **Newport Beach CA-700** · United States of America |
| Time type | **Full time** |
| Posted | **Posted Today** · `startDate` **2026-09-25** · JSON-LD `datePosted` **2026-09-25** |
| Pay (JD body) | **$25.00/hr** undergraduates · **$30.00/hr** advanced degrees |
| Relocation | Stipend available if residence is outside a **50-mile** radius from the office |
| Apply | Workday `/apply`. `canApply: true`. `includeResumeParsing: true` |
| `questionnaireId` | `91620f70fc8a100167d577c4551a0000` |

### Start Your Application / wizard (live stop)

- `/apply` HTML is the Workday candidate-experience SPA (HTTP 200). Visible form widgets are JS-rendered.
- CXS `GET .../apply` returned **HTTP 406** without an account.
- CXS `POST .../apply/start` returned **HTTP 405** without an account.
- CXS `GET .../questionnaire/91620f70fc8a100167d577c4551a0000` returned **HTTP 406** without an account.
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

1. Currently enrolled in a Bachelor’s or Master’s in CS / Data Science / SWE / IT / Math / **Economics** / Business / ML / Applied Math / Statistics / quantitative — **clears.** B.S. Computer Science and Economics, University of Michigan, Expected May 2028.
2. Newport Beach, CA for Summer 2027 — **Yes.** Relocate from Northville, MI (outside 50 miles → stipend applies). Return to Michigan afterward.
3. Full-time intern, return to school after — **clears.** Expected May 2028.
4. Work authorization — **no visa line on this JD.** Answer **US citizen / no sponsorship**.
5. Python or R — **Python Yes.** R **No** — do not check R.
6. Alteryx / Salesforce / SAS / Tableau / MSSQL — **preferred, not knockouts.** Honest **No**.
7. Post-offer background (Extern intern guide: criminal, education, employment after offer) — **Yes** if asked.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on location, dates, or Alteryx/Tableau/R.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular if asked.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66, Junior, 96 credits by Summer 2027.
- Languages you can defend: **Python, SQL** (on this PDF). TypeScript/React if they ask about the dashboard. **Do not check R, Alteryx, Salesforce, SAS, Tableau, MSSQL.**

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
| How Did You Hear About Us? | The board you actually used. **No Pacific Life contact in `network.md` — do not pick Employee Referral.** If you opened pacificlife.wd1: **Career Websites** / Company website. If LinkedIn: **Job Board → LinkedIn**. |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### My Experience · Education

| Exact label | Answer |
| --- | --- |
| School or University * | **University of Michigan** (University of Michigan-Ann Arbor if the typeahead has it) |
| Degree * | **Bachelor of Science (BS)** |
| Field of Study | **Computer Science** (add **Economics** if a second row / dual-degree field is required — Economics is a listed major on this JD) |
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

Workday `questionnaireId` `91620f70fc8a100167d577c4551a0000` was **HTTP 406**. If a later step shows these (or the JD qualifications restated as radios), use:

| If the live label is | Answer |
| --- | --- |
| Currently enrolled in CS / Data Science / Economics / quantitative? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Available Summer 2027 full-time? | **Yes** |
| Can you work onsite in Newport Beach, CA? | **Yes** — relocate from Northville, MI (outside 50 miles) |
| Are you legally authorized to work in the United States? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| Returning to school after the internship? | **Yes** — Expected May 2028 |
| Class standing | **Junior** |
| Graduation date | **May 2028** |
| Ever worked for Pacific Life? | **No** |
| Relatives at Pacific Life? | **No** (unless true) |
| Python | **Yes** — on the PDF through use |
| R | **No** — do not check |
| SQL / Postgres | **Yes** — SQL freshness on Vylet; Postgres persist on SignalWeaver |
| Data modeling | **Yes** — entity database + scoring at Lyndbrook; PAC ranking at MDC. Do not claim a warehouse star schema |
| Alteryx / Salesforce / SAS / Tableau / MSSQL | **No** — do not check. Walk Pandas ETL + React/Postgres dashboard |
| AWS | **Yes** — EC2 (MDC) and S3 (CaseStudyPrep) on the PDF |
| Kaggle / hackathons | **No**. Curiosity analog is coursework (stats) + SignalWeaver (served scores). Do not invent a Kaggle rank |
| How did you hear | Company website / the board you used. **Not** Employee Referral |
| Willing to complete post-offer background? | **Yes** |

Voluntary Disclosures / Self Identify: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

Review: check email is **verdent06@gmail.com**, Newport Beach, dates, PDF attached. Do not submit from this agent.

---

## Cover letter / additional information (paste if Workday has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Pacific Life — Summer 2027 Data Engineering Internship (R17828)
Newport Beach, CA

I am applying for the Summer 2027 Data Engineering Internship on Workday R17828 in Newport Beach — not the Actuarial intern, not the Software Engineering intern, and not Sales. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work full-time in Newport Beach for Summer 2027 and return to Michigan afterward. I am a U.S. citizen and do not need sponsorship. Northville, MI is outside the 50-mile radius, so the posted relocation stipend applies.

I have not used R, Alteryx, Salesforce, SAS, Tableau, or MSSQL. What I can defend is messy business data → ranking/KPI → a report or API a non-builder used.

What I would bring:

- **Irregular Excel → pipeline → ranked output for a stakeholder.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month contract. Closest analog to clarifying requirements, mining a large dataset, and serving it to a business partner.
- **Data modeling / scoring in an engagement window.** At Lyndbrook Capital I built a PWSID entity database from EPA ECHO and MassGIS and a Review Velocity score that filtered 800 acquisition targets to a 280-lead shortlist (35% precision).
- **SQL freshness + pipeline reliability.** On Vylet I wrote injection-safe SQL timestamp checks that re-scrape stale records, and automated a ~30-minute process into a 30-scored-lead / 30-minute Dockerized pipeline (30x). If you ask for SQL as analysis (JOIN that produced a ranking): Pandas/Python did that work; SQL on this resume is freshness.
- **Postgres + a dashboard you can click — not Tableau.** SignalWeaver: FastAPI scores and a React/TypeScript dashboard over 90 tickers persisted in Postgres (9.1s p50). Research assistant, not advice.

Vedant Desai

---

## Short paste blurb (if the form has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to Summer 2027 Data Engineering Internship R17828 in Newport Beach — not Actuarial intern and not SWE intern. I ship Python/SQL pipelines: a Pandas ETL on irregular Excel filings that cut ~800 hours of pulls across 400 PACs, a Flask report API on EC2, SQL freshness checks on Vylet, and a React/Postgres dashboard. I have not used R, Alteryx, Salesforce, SAS, or Tableau. U.S. citizen; no sponsorship. I can relocate to Newport Beach for Summer 2027.

---

## "Why Pacific Life / why this intern?"

I want Summer 2027 onsite in Newport Beach on R17828: ship pipelines a life-insurer’s actuarial, CX, and analytics partners can actually use — not an SOA-exam rotation and not a generic product-SWE intern. I have not interned on Alteryx or Tableau. The analog I can defend is MDC (messy Excel → PAC ranking → Flask report for a nonprofit) plus Lyndbrook if they ask how I model an entity and score a list. I will not invent a childhood-insurance story the page cannot support.

---

## "Tell us about a project" / experience with data / Python / modeling

**MDC (messy Excel → pipeline → ranking → stakeholder report).** Irregular filings; Pandas ETL; PAC ranking; ~800 hours / 400 PACs; Flask REST on EC2 to researchers. Best analog to evaluate business needs + mine a large dataset + communicate results. Form-kit: extracurricular.

**Lyndbrook (data-modeling analog).** EPA + MassGIS → PWSID entity DB; Review Velocity 800 → 280 at 35% precision. Water-utility operators, not life/annuity. Say that out loud if they ask about domain.

**Vylet (process improvement + data freshness).** 30x scored-lead pipeline; SQL timestamp / re-scrape. Closest analog to reliability / data quality. If they ask for analyst SQL, walk freshness — ranking was Pandas (`grade.md`).

**SignalWeaver (Postgres + dashboard analog).** FastAPI + React/Postgres; 90 tickers; 9.1s p50. Not Tableau. Research assistant, not advice. Do not lead with LoRA.

---

## Availability

Full-time intern, **onsite Newport Beach, CA**, Summer 2027. This JD does not print start/end dates. Prior DE intern LinkedIn: **~12 weeks** **[directional]**. Returning to the University of Michigan (Expected May 2028). Housing: posted relocation stipend if outside 50 miles — Northville qualifies; do not claim company housing beyond that. Comp: **$25/hr** undergrad as printed. Post-offer background: **Yes**.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field and on the PDF header.** Do not type `vedantde@umich.edu`.
- **Do not claim R, Salesforce, Alteryx, SAS, Tableau, MSSQL, or Kaggle.** Walk Pandas-on-Excel-exports and SignalWeaver as the dashboard analog (`persona.md` anti-pattern).
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). Awards = **None**.
- **Newport Beach onsite is not a skip.** Say yes. Relocation stipend applies (Northville is outside 50 miles).
- **Referral:** none in `network.md`. Early Careers names on the careers page (Isabel, Mel, Nicci) are TA — that is not a referral. A fake employee name is a knockout.
- **Cover letter:** skip unless the form asks; paste from the letter above if it does.
- **Resume is the intern bottleneck** (`companies.md` C-tier, no published OA, ~15–25%). Posted **2026-09-25** — apply this wave (`recruiting.md` §8).
- **Transcript:** upload unofficial UMich transcript if a later step requires it. Not stored in this repo.
- **Do not apply from this agent. Do not email this packet.**
