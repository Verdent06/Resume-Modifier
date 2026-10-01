# EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.**
Override any Workday parse / Autofill / last-application email. PDF header is already `verdent06@gmail.com`. If a field shows `vedantde@umich.edu`, delete it and type `verdent06@gmail.com` before submit.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

---

# Dow Chemical Company — Data Engineer / Data Platform Engineer Internship Spring 2027 (R2068792) · Written Application Answers

Draft answers for Workday `dow` / `ExternalCareers` req **R2068792**. Grounded in the **live Workday posting opened 2026-10-01**, CXS JSON, `/apply` SPA, `/apply/applyManually`, `/apply/autofillWithResume`, `persona.md`, `grade.md` Interview angles, and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Azure, Azure Data Factory, Azure SQL, Azure OpenAI, Azure Function Apps, Azure Logic Apps, Azure Databricks, ARM, Bicep, Terraform, Azure DevOps, Entra, Scala, PowerShell, Snowflake, Power BI, Copilot, Fusion.

**Form kit email MUST be `verdent06@gmail.com`.** Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship.

**Employment on the form: CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead are **extracurricular**. Lyndbrook: omit from the form (still on the PDF). Awards / honors: **None**.

Airtable: [`recphm1R20sz7F5Nt`](https://airtable.com/appkjmb1lqI38B5dG/tbld48HBTeRo4WpcG/recphm1R20sz7F5Nt) (In Progress — kit landing; **do not submit until the human apply**). Source: **GitHub/SimplifyJobs**.

Job (live ATS): https://dow.wd1.myworkdayjobs.com/ExternalCareers/job/Kankakee-IL-USA/Data-Engineer---Data-Platform-Engineer-Internship-Spring-2027-Semester-at-the-Dow-Delivery-Center-at-UIUC--Champaign--IL-_R2068792

Apply: https://dow.wd1.myworkdayjobs.com/ExternalCareers/job/Kankakee-IL-USA/Data-Engineer---Data-Platform-Engineer-Internship-Spring-2027-Semester-at-the-Dow-Delivery-Center-at-UIUC--Champaign--IL-_R2068792/apply

Resume: `applications/2027/dow/data-engineer-intern-spring/Vedant Desai Resume.pdf`

**SHA-256:** `37af45917720887176c1b824b134c98005b745a66a4b3534c25770fd9188cb9e`

**THIS IS NOT** a Midland SWE intern and **NOT** a plant process-engineering intern. Combined posting: Data Engineer intern **and** Data Platform Engineer intern at the Dow Delivery Center at UIUC.

Posted **2026-09-30** (`startDate` / live `postedOn` **Posted Today** at capture **2026-10-01**). Workday `endDate` **2026-10-22** (`timeLeftToApply`: **21 days left to apply**). `includeResumeParsing: true`. `questionnaireId` `3aec2e31abdb0153c1c2f1808d0b221d`. `secondaryQuestionnaireId` `21f6db95ccda10010b9aee94eb650000`. CXS `/apply` **406**, `/questionnaire/{id}` **422**, `/apply/2/initialize` **406** without an account. **This agent did not create an account and did not submit.**

---

## Knockouts (read first)

1. **Currently enrolled at the University of Illinois Urbana Champaign** — **FAILS.** Enrolled at the **University of Michigan**, Ann Arbor. Answer **No**. Do not lie. This is a printed Required Must (`recruiting.md` Part I §1).
2. Working towards a Bachelor's or Master's in a related technical field — **clears** (B.S. Computer Science and Economics).
3. Within one to three years of graduation — **clears.** Expected **May 2028**. Spring 2027 is ~15 months out.
4. Ability to work legally in the United States; **no visa sponsorship/support** including green card — **clears.** **US citizen; no sponsorship now or later.**
5. In-person Champaign, IL, **15–20 hours/week**, **14–15 weeks** spring semester; **no relocation or housing**; must have transportation to the Delivery Center — **No.** I will be in Ann Arbor / Northville for UMich Winter 2027. Champaign is not a commute. Do not check Yes.
6. Preferred GPA 3.0+ — **clears** (3.66). Preferred CS / CIS / engineering — **clears** (CS).
7. Cloud / Databricks / Snowflake / Scala / PowerShell / Power BI / Terraform — **Python and SQL: Yes.** AWS: Yes (EC2/S3 on the PDF). **Azure / ADF / Databricks / Snowflake / Scala / PowerShell / Power BI / Terraform / Bicep / ARM / Entra: No.** Do not check them.

Binary knockouts auto-reject. The school Must and the Champaign in-person term are both stops. **Do not submit unless Dow waives UIUC enrollment in writing.**

---

## What was extracted from the live page (2026-10-01)

Pulled without creating an account, without uploading a resume, and without submitting. Headless Chrome of the posting + `/apply` + `/apply/applyManually` + `/apply/autofillWithResume`. CXS job JSON `canApply: true`. `userAuthenticated: false`.

### Job posting (public CXS JSON + live chrome)

`GET https://dow.wd1.myworkdayjobs.com/wday/cxs/dow/ExternalCareers/job/Kankakee-IL-USA/Data-Engineer---Data-Platform-Engineer-Internship-Spring-2027-Semester-at-the-Dow-Delivery-Center-at-UIUC--Champaign--IL-_R2068792` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Data Engineer / Data Platform Engineer Internship Spring 2027 Semester at the Dow Delivery Center at UIUC (Champaign, IL)** |
| Company | **THE DOW CHEMICAL COMPANY** |
| Requisition | **R2068792** · jobPostingId `Data-Engineer---Data-Platform-Engineer-Internship-Spring-2027-Semester-at-the-Dow-Delivery-Center-at-UIUC--Champaign--IL-_R2068792` · jobPostingInfo.id `21c4394b72e810015c9e9b744b540000` |
| locations | **Kankakee (IL, USA)** (Workday chrome). JD body: **Champaign, IL** — Dow Delivery Center at UIUC Research Park (**2021 S. First St.**) |
| remote type | **Onsite** |
| time type | **Part time** |
| posted on | **Posted Today** · `startDate` **2026-09-30** · JSON-LD `datePosted` **2026-09-30** |
| time left to apply | **End Date: October 22, 2026 (21 days left to apply)** |
| Apply | Workday `adventureButton` **Apply**. `includeResumeParsing: true`. `canApply: true` |
| Term (JD body) | Typically **14–15 weeks** during the spring academic semester; **15–20 hours per week**; in-person mentorship |
| Pay (JD body, Illinois) | **Bachelor's $26.25–$35.00/hr**; **Master's $37.12–$39.57/hr** |
| `questionnaireId` | `3aec2e31abdb0153c1c2f1808d0b221d` (HTTP **422** without an account) |
| `secondaryQuestionnaireId` | `21f6db95ccda10010b9aee94eb650000` |
| JSON-LD `jobLocationType` | `TELECOMMUTE` (schema.org); Workday `remoteType` is **Onsite** — treat as **onsite Champaign** |

Nav on the live site: **Sign In** · **Search for Jobs**. Footer: **Privacy Policy**. `similarJobs`: **[]**.

### Start Your Application (verbatim live labels)

URL: `/en-US/ExternalCareers/job/Kankakee-IL-USA/Data-Engineer---Data-Platform-Engineer-Internship-Spring-2027-Semester-at-the-Dow-Delivery-Center-at-UIUC--Champaign--IL-_R2068792/apply`

Heading: **Start Your Application** · **Data Engineer / Data Platform Engineer Internship Spring 2027 Semester at the Dow Delivery Center at UIUC (Champaign, IL)**

| Exact control (`data-automation-id`) | What to do |
| --- | --- |
| Autofill with Resume (`autofillWithResume`) | Preferred if you apply. Upload this packet PDF. Then confirm email is **verdent06@gmail.com** after parse |
| Apply Manually (`applyManually`) | Use if Autofill fails. Same facts below |
| Use My Last Application (`useMyLastApplication`) | Only if a prior Dow Candidate Home app exists. Still override email to gmail |
| Apply with LinkedIn (`applyWithLinkedIn`) | Present as an automation id. Skip unless it actually shows. Manual / Autofill is more reliable |
| Sign In (`utilityButtonSignIn`) | If you already have a Dow Workday account |

Do **not** click Create Account from this agent.

### Workday apply chrome (progress bar — verbatim)

**Apply Manually** (`/apply/applyManually`) — **current step 1 of 7**:

1. **Create Account/Sign In** ← live stop (login wall)
2. **My Information**
3. **My Experience**
4. **Application Questions 1 of 2**
5. **Application Questions 2 of 2**
6. **Voluntary Disclosures**
7. **Review**

**Autofill with Resume** (`/apply/autofillWithResume`) — **current step 1 of 8** (inserts Autofill as step 2):

1. **Create Account/Sign In**
2. **Autofill with Resume**
3. **My Information**
4. **My Experience**
5. **Application Questions 1 of 2**
6. **Application Questions 2 of 2**
7. **Voluntary Disclosures**
8. **Review**

No **Self Identify** step and no **Take Assessment** step on this tenant’s progress bar.

### Create Account (verbatim live fields, 2026-10-01)

Exact labels on `/apply/applyManually` and `/apply/autofillWithResume`. Did **not** create an account.

Password Requirements (verbatim bullets; order differed slightly on Autofill vs Manual; same six rules):

- An alphabetic character
- A minimum of 8 characters
- A lowercase character
- A numeric character
- A special character
- An uppercase character

| Exact label | Answer |
| --- | --- |
| Email Address * | **verdent06@gmail.com** (never vedantde@umich.edu) |
| Password * | **Your real password.** Not stored in this repo. Must meet the six rules |
| Verify New Password * | Same as Password |
| **Yes, I have read and consent to the terms and conditions** (`createAccountCheckbox`) | **Check** only if you consent |
| **Create Account** | Click after the above. Do not submit the job from this agent |
| Already have an account? **Sign In** | Use if you already have a Dow Workday account |
| **Forgot your password?** | Only if you already have an account |
| Enter website. This input is for robots only, do not enter if you're human. | **Leave blank** (honeypot, `beecatcher`) |

Consent chrome (verbatim excerpt): *Please read this Terms of Use and Consent Statement carefully before creating your account with The Dow Chemical Company and/or its affiliates (“Dow”). If you do not agree to this Terms of Use and Consent Statement, you may not apply for a job with (or otherwise submit your professional profile to) Dow. A comprehensive Terms of Use and Consent Statement will be presented for your consent before completing your application.* Links named on the page: **Dow’s Privacy Statement** and **Workday Service Privacy Policy**.

### Questionnaire API

- `questionnaireId`: `3aec2e31abdb0153c1c2f1808d0b221d`
- `secondaryQuestionnaireId`: `21f6db95ccda10010b9aee94eb650000`
- CXS `/questionnaire/{id}` returned **HTTP 422** without an account
- CXS `/apply` returned **HTTP 406** / **422** without an account
- **Application Questions 1 of 2, Application Questions 2 of 2, My Information, My Experience, Voluntary Disclosures, Review were not visible.** Do not invent extra essay prompts. If later pages differ, answer the actual question. The JD Required / Preferred list is the best preview of those two questionnaire steps.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular if asked.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66, Junior / rising junior. **Not UIUC.**
- Languages you can defend: **Python, SQL** (on this PDF). **Do not check Scala, PowerShell, Azure, Databricks, Snowflake, Power BI, Terraform.**
- How you heard: **GitHub / Simplify** (Airtable source). **No Dow contact in `network.md`.** Do not pick Employee Referral.

---

## Knockout / structured fields (fill exactly)

### My Information (login wall — standard Workday; confirm live labels)

| Exact label (typical Workday) | Answer |
| --- | --- |
| Country * | **United States of America** |
| First Name * | Vedant |
| Last Name * | Desai |
| Address Line 1 | **49032 Freestone Dr** |
| City | **Northville** (not Ann Arbor, not Champaign — current home) |
| State | **Michigan** |
| Postal Code | **48168** |
| Email Address | **verdent06@gmail.com** |
| Phone Device Type * | **Mobile** |
| Country Phone Code | **United States of America (+1)** |
| Phone Number | **(248) 704-4852** |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub / Website | https://github.com/Verdent06 · https://vyletdata.com if a second URL |
| How Did You Hear About Us? | **Job Board** / **Simplify** / **GitHub** — the board you actually used. Airtable source is **GitHub/SimplifyJobs**. **No Dow contact in `network.md` — do not pick Employee Referral.** If you opened dow.wd1 directly: **Career Websites** / Company website. |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### My Experience · Education

| Exact label | Answer |
| --- | --- |
| School or University * | **University of Michigan** (University of Michigan-Ann Arbor if the typeahead has it). **Do not type University of Illinois.** |
| Degree * | **Bachelor of Science (BS)** |
| Field of Study | **Computer Science** (add **Economics** if a second row / dual-degree field is required) |
| Overall Result (GPA) | **3.66** |
| From | **08/2025** (started **08/31/2025**) |
| To (Actual or Expected) | **05/2028** |
| Currently enrolled | **Yes** — at Michigan, not UIUC |
| Did you graduate? | **No** |
| Class standing | **Junior** |
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
| SignalWeaver / Granular Synthesizer | **Not jobs.** |
| Awards / honors | **None.** |

Skills tags if shown: only **Python, SQL, Pandas, Flask, FastAPI, PostgreSQL, Redis, Docker, Git, AWS**. **Do not** tag Azure, Databricks, Snowflake, Scala, PowerShell, Power BI, Terraform, Bicep, ARM, Entra, Copilot.

### Application Questions 1 of 2 / 2 of 2 (login wall — confirm live labels; do not invent wording)

Two questionnaire IDs were **HTTP 422 / 406**. If a later step restates the JD qualifications as radios, use:

| If the live label is | Answer |
| --- | --- |
| Are you currently enrolled at the University of Illinois Urbana Champaign? | **No** — University of Michigan, Ann Arbor |
| Currently enrolled in a Bachelor's or Master's in a related technical field? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Within one to three years of graduation? | **Yes** — Expected **May 2028** |
| Graduation date | **May 2028** (if a day is required: **05/01/2028**) |
| Class standing | **Junior** |
| GPA 3.0 or higher? | **Yes** — **3.66 / 4.0** |
| Major Computer Science / CIS / Engineering? | **Yes** — Computer Science |
| Available part-time 15–20 hours/week, in-person Champaign, Spring 2027 (14–15 weeks)? | **No** — enrolled at UMich in Ann Arbor for Winter 2027; Champaign is not a commute; JD offers no housing |
| Must have transportation to the Dow Delivery Center at UIUC? | **No** — I will not be living in Champaign |
| Are you legally authorized to work in the United States? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| Will you return to school after the internship? | **Yes** — Expected May 2028 (this is moot if you do not submit) |
| Ever worked for Dow? | **No** |
| Relatives at Dow? | **No** (unless true) |
| Python | **Yes** — on the PDF through use |
| SQL | **Yes** — Vylet freshness / re-scrape |
| Scala | **No** |
| PowerShell | **No** |
| AWS / GCP / Azure | **AWS: Yes** (EC2, S3 on the PDF). **GCP: No. Azure: No** |
| Databricks | **No** |
| Snowflake | **No** |
| Power BI | **No** |
| Terraform / ARM / Bicep | **No** |
| Agile / Scrum / Kanban | **No** as a claimed certification. I ship in short cycles; do not check a formal Scrum credential |
| Version control / code review | **Yes** — Git; SignalWeaver GitHub Actions CI |
| How did you hear | **Simplify / GitHub** (or Company website). **Not** Employee Referral |
| Expected hourly / salary | Accept posted Illinois scale **$26.25–$35.00/hr** bachelor's. Prefer leave blank if optional |
| Start you could join | **Do not invent a Champaign start.** If forced and you are applying anyway: Spring 2027 is the posted term — still answer the UIUC and onsite questions **No** |

Voluntary Disclosures: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

Review: check email is **verdent06@gmail.com**, school is **Michigan not UIUC**, PDF attached, sponsorship **No**. Do not submit from this agent.

---

## Cover letter / additional information (paste if Workday has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Dow Chemical Company — Data Engineer / Data Platform Engineer Internship Spring 2027 (R2068792)
Dow Delivery Center at UIUC · Champaign, IL

I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen and will not need visa sponsorship.

I am **not** enrolled at the University of Illinois Urbana Champaign. I will be in Ann Arbor / Northville for the University of Michigan Winter 2027 term. I cannot sit a 15–20 hour in-person week at the Champaign Delivery Center without housing, and this JD does not offer relocation. I am sending this only if you will consider a non-UIUC applicant; otherwise please stop here.

I have not used Azure Data Factory, Databricks, Snowflake, Scala, PowerShell, Terraform, or Power BI. What I can defend is messy operational data → a pipeline → a quality check → an API or table a stakeholder used.

What I would bring if the school gate is waived:

- **Ingest → persist → serve.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, ranked PACs by funding volume, and shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month MCFN contract. That eliminated ~800 hours of manual pulls across 400 tracked PACs.
- **SQL freshness + data quality.** On Vylet I wrote injection-safe SQL timestamp checks that re-scrape stale records, and I fixed a name-collision defect that lifted lead-qualification from 79% to 89%. Closest analog to platform RCA.
- **Automation + containers.** Same product: a ~30-minute manual process into a Dockerized pipeline generating 30 scored leads in 30 minutes (30x) with Redis/Celery. SignalWeaver is Docker Compose (API + Postgres) plus GitHub Actions CI.

I interview in Python and SQL. I would ramp Azure / Databricks on the team’s stack rather than pretend I already have them.

Vedant Desai

---

## Short paste blurb (if the form has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to R2068792 — Data Engineer / Data Platform Engineer intern at the Dow Delivery Center. I am **not** a UIUC student and I cannot sit Champaign 15–20 hrs/week in Spring 2027 while enrolled in Ann Arbor. I ship Python/SQL pipelines: Pandas ETL on irregular Excel filings that cut ~800 hours of pulls across 400 PACs, injection-safe SQL freshness, a 79%→89% quality fix, and Docker/GitHub Actions. I have not used Azure, Databricks, Scala, PowerShell, or Power BI. U.S. citizen; no sponsorship.

---

## "Why Dow / why this intern?"

I want the Enterprise Data & Analytics seat (R2068792): ingest, persist, and curate data, or help run the Azure data platform — not a Midland generic SWE rotation and not a plant process-engineering intern. I am not enrolled at UIUC. If that Must is real, I should not take a slot. If it is waivable, the analog I can defend is MDC (messy Excel → PAC ranking → Flask on EC2) plus Vylet SQL freshness / 79%→89% quality and SignalWeaver Docker Compose + GitHub Actions. I will not invent an Illinois enrollment or an Azure internship.

---

## "Tell us about a project" / pipelines / SQL / cloud / quality

**MDC (messy Excel → pipeline → ranking → stakeholder API).** Irregular filings; Pandas ETL; PAC ranking; ~800 hours / 400 PACs; Flask REST on EC2. Best analog to ingestion, persistence, curation. Form-kit: extracurricular.

**Vylet (SQL freshness + quality defect + containers).** Injection-safe SQL timestamp / re-scrape; 79% → 89% name-collision fix; Dockerized 30x pipeline with Redis/Celery. Closest analog to quality + orchestration. If they ask for warehouse SQL: ranking was Pandas; SQL on this resume is freshness.

**Lyndbrook (multi-source persist).** EPA + MassGIS → PWSID entity DB; Review Velocity 800 → 280 at 35% precision. Water-utility operators, not materials science. Say that out loud.

**SignalWeaver (serve + CI analog).** FastAPI scores + Postgres; Docker Compose; GitHub Actions. Not Power BI, not Azure DevOps. Research assistant, not advice. Do not lead with LoRA.

---

## Availability

Part-time intern, **onsite Champaign, IL**, Spring 2027, **15–20 hours/week**, **14–15 weeks**. **I cannot commit to that term** while enrolled at UMich in Ann Arbor. No housing / relocation on this JD. Returning to Michigan (Expected May 2028). Pay: accept posted bachelor's **$26.25–$35.00/hr** if they waive the school gate.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field and on the PDF header.** Do not type `vedantde@umich.edu`.
- **Do not claim UIUC enrollment.** School = University of Michigan. The Required Must is a knockout.
- **Do not claim Champaign in-person Spring 2027** unless you actually take Winter 2027 off and move there at your own cost. Context does not support that. Default **No**.
- **Do not claim Azure, ADF, Databricks, Snowflake, Scala, PowerShell, Terraform, Bicep, ARM, Entra, or Power BI.** Walk Pandas-on-Excel-exports, Vylet SQL freshness, and Docker / GitHub Actions as the platform analog (`persona.md` anti-pattern).
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). Awards = **None**.
- **Referral:** none in `network.md`. How you heard = **Simplify / GitHub** (Airtable). A fake employee name is a knockout. `jquinlan@dow.com` is the published Delivery Center contact on the Research Park page — that is **not** a referral.
- **Cover letter:** skip unless the form asks; paste from the letter above if it does. The letter states the school gap in the first screen.
- **Resume is a clean DE spine** (`grade.md` 10.0) and still loses to the UIUC Must (`companies.md` C-tier, no published OA, ~20–30% **if eligible**).
- **Transcript:** upload unofficial UMich transcript if a later step requires it. Not stored in this repo. It will confirm Michigan, not Illinois.
- **Airtable `recphm1R20sz7F5Nt`:** do not mark Applied until a human submits.
- **Do not apply from this agent. Do not email this packet.**
