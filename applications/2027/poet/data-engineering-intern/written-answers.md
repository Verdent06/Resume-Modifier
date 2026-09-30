# EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.**
Override any Workday parse / Autofill / last-application email. PDF header is already `verdent06@gmail.com`.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

---

# POET — Data Engineering Intern - Summer 2027 (R101787) · Written Application Answers

Draft answers for Workday `poet.wd1` / `POET` req **R101787**. Grounded in the **live Workday posting opened 2026-09-30**, CXS JSON, `/apply` SPA shell, `persona.md`, `grade.md` Interview angles, and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**Do not invent:** PowerShell, C#, Java, Snowflake, Databricks, Tableau, Copilot, Fusion, SCADA / industrial-historian internships, Microsoft Office as a technical skill.

**Form kit email MUST be `verdent06@gmail.com`.** Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship.

**Employment on the form: CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead are **extracurricular**. Lyndbrook: omit from the form (still on the PDF). Awards / honors: **None**.

Airtable: `reccH7C89YYWQoZOd` (In Progress — kit landing; **do not submit until the human apply**). Source: GitHub/SimplifyJobs.

Apply: https://poet.wd1.myworkdayjobs.com/POET/job/Sioux-Falls-SD/Data-Engineering-Intern_R101787/apply
Listing: https://poet.wd1.myworkdayjobs.com/POET/job/Sioux-Falls-SD/Data-Engineering-Intern_R101787
Resume: `applications/2027/poet/data-engineering-intern/Vedant Desai Resume.pdf`

**SHA-256 (PDF):** `e67c37fef7186099c7514596c0727e694c672ea095b55335e63c040932454e8b`

**THIS IS NOT** Process Engineering Intern **R101679**, **NOT** Research Intern **R101732**, **NOT** Finance Intern **R101668**, and **NOT** Procurement Intern **R101756**.

---

## Knockouts (read first)

1. Currently pursuing Associate's or Bachelor's in Computer Science, Information Systems, Data Science, Engineering, or related — **clears** (B.S. Computer Science and Economics, University of Michigan, Expected May 2028).
2. Class year — **clears**. Official intern FAQ: freshman, sophomore, junior, or senior. Summer 2027 = **rising junior** / after sophomore year; Fall 2027 junior. GPA **3.66** (JD prints no floor; FAQ: good academic standing).
3. Onsite Sioux Falls, SD, Summer 2027 (10–12 weeks, mid- to late May start) — **Yes** (relocate from Northville, MI).
4. Work authorization — JD prints **no** sponsorship line. Official FAQ: international students eligible only if **already legally entitled to work in the US**; student obtains visa. **US citizen; no sponsorship now or later.**
5. SQL / relational databases — **Yes** (on the PDF through use).
6. Python / PowerShell / C# / Java — **Python Yes.** PowerShell **No.** C# **No.** Java **No.** Do not check them.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on Sioux Falls onsite, Fall 2027 enrollment, or C#/PowerShell.

---

## What was extracted from the live page (2026-09-30)

Pulled without creating an account, without uploading a resume, and without submitting.

### Job posting (public CXS JSON + JSON-LD)

`GET https://poet.wd1.myworkdayjobs.com/wday/cxs/poet/POET/job/Sioux-Falls-SD/Data-Engineering-Intern_R101787` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Data Engineering Intern - Summer 2027** |
| Company | **POET** |
| Requisition | **R101787** · jobPostingId `Data-Engineering-Intern_R101787` · jobPostingInfo.id `01d23459aa721000c1f4be3a2fa20000` |
| Location | **Sioux Falls, SD** · United States of America |
| Time type | **Full time** |
| Posted | **Posted Today** · `startDate` **2026-09-30** · JSON-LD `datePosted` **2026-09-30** |
| Pay | **Not listed** |
| Apply | Workday `/apply`. `canApply: true`. `includeResumeParsing: true` |
| `questionnaireId` | `16d5b562c17410019d7dff2241910000` |

Campus boards (same req): recruitment began **2026-09-28**; listing expires **2027-01-01**. JD body: internships posted early September; **interns selected by November 1**.

### Start Your Application / wizard (live stop)

- `/apply` HTML is the Workday candidate-experience SPA (HTTP 200). Visible form widgets are JS-rendered.
- CXS `GET .../apply` and `GET .../questionnaire/16d5b562c17410019d7dff2241910000` returned **HTTP 406** without an account.
- CXS `POST .../apply/2/initialize` returned **HTTP 405** without an account.
- **No essay prompts, knockout radios, or My Information fields were visible on the public page.** Do not invent extra essays. If later pages differ, answer the actual question.

Typical Workday apply chrome after Apply (confirm live; not rendered without login on this capture):

1. **Create Account/Sign In** ← live stop
2. **Autofill with Resume** / **Apply Manually** / **Use My Last Application** / **Apply With LinkedIn**
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

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular if asked.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66, Junior / rising junior, 96 credits by Summer 2027.
- Languages you can defend: **Python, SQL** (on this PDF). **Do not check PowerShell, C#, Java.**
- How you heard: **GitHub / Simplify** (Airtable source). **No POET contact in `network.md`.** Do not pick Employee Referral.

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
| How Did You Hear About Us? | **Job Board** / **Simplify** / **GitHub** — the board you actually used. Airtable source is **GitHub/SimplifyJobs**. **No POET contact in `network.md` — do not pick Employee Referral.** If you opened poet.wd1 directly: **Company website**. |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### My Experience · Education

| Exact label | Answer |
| --- | --- |
| School or University * | **University of Michigan** (University of Michigan-Ann Arbor if the typeahead has it) |
| Degree * | **Bachelor of Science (BS)** |
| Field of Study | **Computer Science** (add **Economics** if a second row is required) |
| Overall Result (GPA) | **3.66** |
| From | **08/2025** (started **08/31/2025**) |
| To (Actual or Expected) | **05/2028** |
| Currently enrolled | **Yes** |
| Class standing | **Junior** (rising junior for Summer 2027; Fall 2027 junior) |
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

Workday `questionnaireId` `16d5b562c17410019d7dff2241910000` was **HTTP 406**. If a later step shows these (or the JD qualifications restated as radios), use:

| If the live label is | Answer |
| --- | --- |
| Currently pursuing Associate's or Bachelor's in CS / IS / Data Science / Engineering / related? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Available Summer 2027 full-time? | **Yes** — 10–12 weeks from mid- to late May 2027 |
| Can you work onsite in Sioux Falls, SD? | **Yes** — relocate from Northville, MI |
| Are you legally authorized to work in the United States? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| Valid US driver's license (if asked) | **Yes** |
| Returning to school after the internship? | **Yes** — Expected May 2028; enrolled Fall 2027 |
| Class standing | **Junior** (rising junior / after sophomore year) |
| Graduation date | **May 2028** |
| Freshman / sophomore / junior / senior (FAQ) | **Junior** |
| Ever worked for POET? | **No** |
| Relatives at POET? | **No** (unless true) |
| SQL / relational databases | **Yes** — SQL freshness on Vylet; Postgres persist on SignalWeaver |
| Python | **Yes** — on the PDF through use |
| PowerShell | **No** — do not check |
| C# | **No** — do not check |
| Java | **No** — do not check |
| Microsoft Office | **Yes, working knowledge as a student** (docs/sheets). Do **not** list Office or Excel-as-BI on Skills. Excel on the resume is irregular filings ingested in Pandas |
| Snowflake / Databricks / Tableau | **No** — do not check |
| Willing to relocate to Sioux Falls for the summer? | **Yes** |
| How did you hear | **Simplify / GitHub** (or Company website). **Not** Employee Referral |
| Willing to complete post-offer background / drug screen if asked? | **Yes** |

Voluntary Disclosures / Self Identify: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

Review: check email is **verdent06@gmail.com**, Sioux Falls, dates, PDF attached. Do not submit from this agent.

---

## Cover letter / additional information (paste if Workday has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

POET — Data Engineering Intern - Summer 2027 (R101787)
Sioux Falls, SD

I am applying to Data Engineering Intern - Summer 2027 on Workday R101787 in Sioux Falls — not Process Engineering Intern, not Research Intern, and not Finance Intern. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work full-time onsite in Sioux Falls for the 10–12 week Never Satisfied term (mid- to late May through August 2027) and return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

I have not used PowerShell, C#, Java, Snowflake, Databricks, or Tableau. What I can defend is messy operational data → a pipeline → a quality check → an API or table a stakeholder used.

What I would bring:

- **Manual pulls → ETL → ranked output for a stakeholder.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month contract.
- **SQL freshness + data quality.** On Vylet I wrote injection-safe SQL timestamp checks that re-scrape stale records, and I fixed a name-collision defect that lifted lead-qualification from 79% to 89%. Closest analog to "identify and resolve data quality issues."
- **Automation of a repetitive process.** Same product: a ~30-minute manual process per business into a Dockerized LangGraph pipeline generating 30 scored leads in 30 minutes (30x) with Redis/Celery workers.
- **Multi-source entity data.** At Lyndbrook I aggregated EPA ECHO and MassGIS into a PWSID entity database and a Review Velocity score that filtered 800 targets to 280 at 35% precision.

I interview in Python and SQL.

Vedant Desai

---

## Short paste blurb (if the form has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to POET Data Engineering Intern R101787 in Sioux Falls — not Process Engineering and not Research Intern. I ship Python/SQL pipelines: a Pandas ETL on irregular Excel filings that cut ~800 hours of pulls across 400 PACs, injection-safe SQL freshness checks, a 79%→89% quality fix, and a Dockerized 30x pipeline. I have not used PowerShell, C#, Java, Snowflake, or Tableau. U.S. citizen; no sponsorship. I can relocate to Sioux Falls for Summer 2027.

---

## "Why POET / why this intern?"

I want Summer 2027 onsite in Sioux Falls on R101787: ship pipelines the Data Engineering team uses on plant, commodity, financial, and logistics data — not a process-engineering rotation and not a lab seat. I have not interned on industrial historians or C#. The analog I can defend is MDC (messy Excel → PAC ranking → Flask report) plus Vylet if they ask how I catch stale or wrong records. I will not invent a childhood-ethanol story the page cannot support.

---

## "Tell us about a project" / experience with data / SQL / quality

**MDC (messy Excel → pipeline → ranking → stakeholder report).** Irregular filings; Pandas ETL; PAC ranking; ~800 hours / 400 PACs; Flask REST on EC2 to researchers. Best analog to automate a manual data process and document it for a non-builder. Form-kit: extracurricular.

**Vylet (SQL freshness + quality defect).** Injection-safe SQL timestamp / re-scrape; 79% → 89% name-collision fix; Dockerized 30x pipeline with Redis/Celery. Closest analog to quality + orchestration. If they ask for analyst SQL (JOIN that produced a ranking): Pandas/Python did that work; SQL on this resume is freshness.

**Lyndbrook (multi-source entity / quality filter).** EPA + MassGIS → PWSID entity DB; Review Velocity 800 → 280 at 35% precision. Water-utility operators, not bioethanol. Say that out loud if they ask about domain.

**SignalWeaver (API + Docker Compose).** FastAPI scores + Postgres; Docker Compose. Not Tableau. Research assistant, not advice. Do not lead with LoRA.

---

## Availability

Full-time intern, **onsite Sioux Falls, SD**, Summer 2027. Never Satisfied term **10–12 weeks** from **mid- to late May**. Returning to the University of Michigan (Expected May 2028; enrolled Fall 2027). Housing: not listed on this JD — do not claim company housing; still say yes to the site. Comp: unlisted (C-tier intern band). Selected by **November 1** — apply this wave.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field and on the PDF header.** Do not type `vedantde@umich.edu`. Never email this packet — App Man pulls via `gh`.
- **Do not claim PowerShell, C#, Java, Snowflake, Databricks, Tableau, Copilot, or Fusion.** Walk Pandas-on-Excel-exports, Vylet SQL freshness, and Docker/Redis-Celery as the orchestration analog (`persona.md` anti-pattern).
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). Awards = **None**.
- **Sioux Falls onsite is not a skip.** Say yes. Relocate from Northville, MI.
- **Referral:** none in `network.md`. How you heard = **Simplify / GitHub** (Airtable). A fake employee name is a knockout.
- **Cover letter:** skip unless the form asks; paste from the letter above if it does.
- **Resume is the intern bottleneck** (`companies.md` C-tier, no published OA, ~15–25%). Posted **2026-09-30** — selected by **November 1** (`recruiting.md` §8).
- **Transcript:** upload unofficial UMich transcript if a later step requires it. Not stored in this repo.
- **Do not apply from this agent. Do not email this packet.**
