# Rubrik — Software Engineering Winter Internship (Palo Alto, Greenhouse 8171088 / req 11373) · Written Application Answers

Draft answers for the public Greenhouse apply flow. Labels and dropdowns recaptured from `https://boards-api.greenhouse.io/v1/boards/rubrik/jobs/8171088?questions=true` and the live JD `https://www.rubrik.com/company/careers/departments/job.8171088?gh_jid=8171088` on **2026-09-20** (job `id` **8171088**; `requisition_id` **11373**; `internal_job_id` **3536373**; `first_published` **2026-09-18**; `education` = `education_required`). Grounded in `persona.md` (generic full-stack SWE intern on a zero-trust data-security platform — **not** malware-research, **not** an ML-training intern) and `context.md` metrics only.

**Do not invent:** Java, Go, Golang, Objective-C, Scala, C-as-primary, Kubernetes, Snowflake, Databricks, Tableau, Copilot, Fusion, Rubrik Security Cloud, Zero Trust product work, malware research.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** Phone **248-704-4852**. US citizen, no sponsorship.

**Employment on the form: CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead Ambassador are **extracurricular**. Awards / honors: **None**. Lyndbrook Capital: omit.

**Do not submit from this agent.** Paste pack only.

Apply: https://job-boards.greenhouse.io/rubrik/jobs/8171088
Resume: `applications/2027/rubrik/software-engineering-intern-winter/Vedant Desai Resume.pdf`

**SHA-256:** `1aa73873aa0bc90344fb5756d6fee07300d682ced92005a970b1dc29a4901c7b`

**Form kit (this apply only):** email **verdent06@gmail.com**. Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168** (ZIP **48168**). U.S. citizen, no sponsorship. GPA **3.66**. Expected **May 2028**. Class standing on forms: **Junior**. LinkedIn https://www.linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06. SAT **1510** if asked. DOB **12/16/2006** if asked. Valid US driver’s license: **Yes** if asked. Work-authorized: **Yes**.

---

## Knockouts (read first)

1. **Graduation window.** JD: December 2027 or Spring 2028. Form dropdown: pick **May/June 2028**. Expected **May 2028**. **Clears.** Do not pick December 2027, December 2028, May/Spring 2029, or Other.
2. **Full-time onsite Palo Alto Jan–May 2027.** Form: "Are you able to commit to a full-time, on-site internship at our Palo Alto headquarters from January to May 2027?" Dates on the JD: **January 11, 2027 – May 7, 2027**. Answer **Yes**. Relocate from Northville, MI. Confirm with Michigan that you can sit the winter/spring term in Palo Alto before any recruiter call.
3. **90-min HackerRank OA.** Form requires confirmation. Answer **Yes**. This is the binding funnel filter (`persona.md` / `companies.md`).
4. **US university.** University of Michigan, Ann Arbor. **Yes**.
5. **Sponsorship.** US citizen. **No** ("Will you require visa sponsorship to work for Rubrik?").
6. **CS degree.** B.S. Computer Science and Economics. **Clears.**

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on dates, OA, university, or sponsorship.

Country on the public board: **United States**. Location: **Northville, Michigan, United States** (current city, not Palo Alto).

---

## Form-kit reminders (read before any experience / honors field)

- **Prior experience (jobs / internships):** CaseStudyPrep.AI SWE co-op and founder of Vylet **only**.
- **MDC = extracurricular only.** Still on the PDF under Experience. Do not list Michigan Data Consulting as a job on the form.
- **SpaceXAI Campus Lead Ambassador = extracurricular.** Not on this PDF. Never list as an employer.
- **Lyndbrook:** omit (not on this PDF).
- **Awards / honors:** **None.** Do not invent Dean's List, scholarships, or hackathon wins.
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66. Standing: **Junior** (Winter 2027 intern = during junior year).
- Do not invent Java, Go, Objective-C, Kubernetes, Snowflake, Databricks, Copilot, Fusion.

---

## Knockout / structured fields (fill exactly)

Exact Greenhouse labels. `*` = `required: true` on the API. Live page also shows **Country** next to Phone and **Location** / Locate me (API `location_questions`: Location, Latitude, Longitude — not in the public `questions` array). Some labels have a trailing space or trailing newline on the API; the visible text is what is shown here.

| Field (exact label) | Required | Answer |
| --- | --- | --- |
| First Name | * | Vedant |
| Last Name | * | Desai |
| Email | * | **verdent06@gmail.com** |
| Country | live page | **United States** |
| Phone | * | 248-704-4852 |
| Location | live page / `Location` * | **Northville, Michigan, United States** (current city). Do **not** put Palo Alto here — that is the job site. |
| Resume/CV | * | `applications/2027/rubrik/software-engineering-intern-winter/Vedant Desai Resume.pdf` (pdf/doc/docx/txt/rtf) |
| Cover Letter | | Optional. Paste the letter below if you attach or “Enter manually.” Skip if speed-applying — the PDF is the screen; **OA is the binding filter**. |
| What is your Legal Name? | * | **Vedant Desai** |
| Are you able to commit to a full-time, on-site internship at our Palo Alto headquarters from January to May 2027? | * | **Yes**. Live options: Yes, No. |
| Graduation date | * | **May/June 2028**. Live options: December 2027, May/June 2028, December 2028, May/Spring 2029, Other. |
| As part of your application, you will need to complete a 90 min Hackerrank assessment. Can you confirm if you are comfortable with that next step? | * | **Yes**. Live options: Yes, No. Trailing space on the API label. |
| Is the university you are currently attending located in the United States? | * | **Yes**. Live options: Yes, No. |
| LinkedIn Profile | * | https://www.linkedin.com/in/vedantde06 |
| Are you currently or have you ever been employed by Rubrik or contracted to provide services to Rubrik? | * | **I have never been employed by Rubrik or contracted to provide services to Rubrik**. Appears **twice** on the API — same answer both times. Live options: never employed/contracted; currently full/part-time; currently a contractor; previously full/part-time; previously a contractor. |
| How did you hear about this job? | * | **Company Website** — no Rubrik contact in `network.md`. Do **not** pick Employee Referral. Live options: Company Website, LinkedIn, Glassdoor, Indeed, We Work Remotely, Github, Employee Referral, Other. |
| What is your preferred coding language? | * | **C++** and **Python**. Multi-select. Then list TypeScript under Other. Do **not** check C, Java, Golang, or Scala. |
| If you selected "other" programing language, please list here: | | **TypeScript** (inventory; JS-family analog for the JD JavaScript or-list). Optional field; fill it because TypeScript is real and not on the checkbox list. |
| Will you require visa sponsorship to work for Rubrik? | * | **No**. Live options: Yes, No. US citizen — none now or later. |
| Please Review the NDA and indicate your agreement by typing your full name below | * | **Vedant Desai** |
| I acknowledge that I have read Rubrik’s Candidate Privacy Notice and understand that the information I submit as part of this application will be used in accordance with this policy. | * | **Yes**. Single live option. |
| What is your home Zip Code? | * | **48168** (trailing newline on the API label). |

Greenhouse also requires the **Education** widget (`education_required`):

| Education widget | Answer |
| --- | --- |
| School | University of Michigan (typeahead: Michigan → **University of Michigan** / Ann Arbor. Do not pick Dearborn/Flint/MSU.) |
| Degree | Bachelor's / Bachelor of Science |
| Discipline | Computer Science (dual CS + Economics — pick CS if one) |
| Start date | **August 2025** (if a day is required: **08/31/2025**) |
| End date year | **May 2028** (expected; Did you graduate? **No**) |

If a second education row is required: **Northville High School**, Northville MI, graduated **05/19/2025**.

If a later step asks fields not on this public form:

| If asked | Answer |
| --- | --- |
| Address | 49032 Freestone Dr, Northville, MI 48168 |
| ZIP | **48168** |
| GitHub | https://github.com/Verdent06 |
| GPA | **3.66 / 4.0** |
| Class standing | **Junior** (Expected May 2028; Jan 2027 is junior-year winter) |
| US citizen | **Yes** |
| Work authorized | **Yes** — US citizen; authorized for any US employer; no CPT/OPT/H-1B now or later |
| SAT | **1510** |
| Date of birth | **12/16/2006** |
| Valid US driver’s license | **Yes** |
| High school | Northville High School, graduated **05/19/2025** |
| University start | **08/31/2025** |
| Country | United States |
| Availability | Winter 2027 term **available**. Jan 11–May 7 2027, full-time onsite Palo Alto |
| Relocate Palo Alto | **Yes** |
| Website | https://github.com/Verdent06 |
| Awards / honors | **None** |
| Desired compensation | If forced: **$60/hour** (Levels.fyi Winter 2026 Palo Alto intern **[directional]**; unlisted on this JD). Do not invent a higher bid. |

Voluntary EEO / disability / veteran / U.S. Standard Demographic Questions: **I do not want to answer** / **I don't wish to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

---

## Employment on the form (if Autofill / profile has work history)

Resume upload first, then **fix email** if parse yields anything other than **verdent06@gmail.com**. After Autofill: if MDC lands under Work Experience, **move it to extracurricular / organizations**. If SpaceXAI Campus Lead Ambassador autofills from LinkedIn as a job, **move it to extracurricular**. Awards stay empty.

### Work Experience — only these two

#### 1. Vylet (current)

| Field | Answer |
| --- | --- |
| Job Title | Founder |
| Company | Vylet |
| Location | Northville, MI |
| I currently work here | **Checked** |
| From | **05/2026** |
| To | Present |
| Description | Founded Vylet (vyletdata.com) — live PE/search-fund lead-sourcing product ($1,500 MRR, three clients). Dockerized LangGraph pipeline with Redis/Celery workers (30 scored leads in 30 minutes, 30x). RCA on a name-collision defect that lifted qualification 79%→89%. Python. Not Java/Go. |

#### 2. CaseStudyPrep.AI

| Field | Answer |
| --- | --- |
| Job Title | Software Engineer Co-op (Voice AI) |
| Company | CaseStudyPrep.AI |
| Location | Remote |
| I currently work here | Unchecked |
| From | **12/2025** |
| To | **05/2026** |
| Description | Titled SWE co-op. Recovered a 27% audio-upload failure rate with RxJS + expired S3 presigned URLs. Web Worker audio path under 5ms / 60 FPS. Angular/TypeScript. Routine AWS S3. |

| Extra row that Autofill may create | Action |
| --- | --- |
| Michigan Data Consulting (MDC) | **Extracurricular only.** Move off Work Experience. Campus consulting / Flask REST on AWS EC2 for MCFN. Not prior professional employment. |
| SpaceXAI Campus Lead Ambassador | **Extracurricular only.** Campus ambassador. Do **not** list as SWE / internship / employment. Not on this PDF. |
| Lyndbrook Capital | **Omit.** Not on this PDF. |
| Granular Synthesizer Plugin / SignalWeaver | **Projects, not jobs.** |
| Awards / honors | **None.** Leave empty. |

---

## Cover Letter (optional on Greenhouse — paste if you attach or “Enter manually”)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Rubrik — Software Engineering Winter Internship (Greenhouse 8171088 / req 11373)
Palo Alto, CA · January 11, 2027 – May 7, 2027

I am applying to the Winter 2027 Software Engineering Internship at Palo Alto HQ — a generic product-SWE seat that ships on Rubrik Security Cloud, not a malware-research rotation and not an ML-training intern. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen and will not need visa sponsorship. I can be onsite in Palo Alto full-time January 11–May 7, 2027.

I want this seat because the work is shipped backend/frontend systems next to data integrity and recovery, not a notebook-ML project. What I can defend:

- **Production REST on AWS.** At Michigan Data Consulting (campus consulting — extracurricular on this form) I was the sole engineer on a 5-month MCFN contract: a Requests + Pandas ETL that cut ~800 hours of manual pulls across 400 tracked PACs, served through a Flask REST API on AWS EC2.
- **Named production defect + pipeline.** On Vylet I own a Dockerized Redis/Celery product (30 scored leads in 30 minutes) and fixed a name-collision defect that lifted lead-qualification from 79% to 89%. Three paying clients; $1,500 MRR.
- **Frontend production debug + C++ concurrency.** At CaseStudyPrep I recovered a 27% S3 upload-failure rate (expired presigned URLs) and moved audio off the UI thread (under 5ms / 60 FPS). Granular is lock-free C++ (SPSC FIFO, zero-heap `processBlock()`). SignalWeaver ships React/TypeScript + FastAPI REST (9.1s p50 / 15.2s p99) with Docker Compose and GitHub Actions.

I have not used Java, Go, or Objective-C. The JD is one-or-more languages; I interview in Python, TypeScript, and C++. I will complete the 90-minute HackerRank assessment.

Vedant Desai

---

## Short “why Rubrik” (if a later box appears)

I want a Winter 2027 intern writing shipped product software next to data protection and recovery — APIs, production debug, and honest C++/concurrency — not malware research and not a model-training rotation.

MDC (extracurricular): Requests + Pandas ETL + Flask REST on AWS EC2 (~800 hours / 400 PACs). Vylet: 79%→89% defect fix, Docker/Redis/Celery (30x). CaseStudyPrep: 27% S3 upload-failure recovery. Granular: lock-free C++ SPSC. SignalWeaver: React/TypeScript + FastAPI + GitHub Actions.

No Java, Go, or Objective-C in my inventory — I interview in Python, TypeScript, and C++. US citizen; no sponsorship. Onsite Palo Alto January 11–May 7, 2027. Junior; Expected May 2028 (GPA 3.66). Comfortable with the 90-min HackerRank OA.

---

## Availability / location

Winter 2027, full-time, **onsite Palo Alto, CA HQ (3495 Deer Creek Rd)**, January 11, 2027 – May 7, 2027. Willing to relocate from Northville, MI. Returning to the University of Michigan after the internship (Expected May 2028). Class standing: **Junior**. Valid US DL: **Yes**. Confirm with Michigan before the recruiter screen that the Jan–May window is workable (this term spans winter + into spring).

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Greenhouse field.** Autofill will try `vedantde@umich.edu` if a parser hallucinates it — change it. This PDF header is already `verdent06@gmail.com`.
- **Employment widget = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). SpaceXAI Campus Lead = extracurricular, not on the PDF. Awards = **None**.
- **Graduation date = May/June 2028.** Do not pick Other and type May 2028.
- **Location is Northville, MI.** Job site is Palo Alto. Do not spoof a California address.
- **How you heard:** Company Website. No Rubrik contact in `network.md`.
- **Preferred languages: C++ and Python**, plus TypeScript under Other. Do not check Java, Golang, Scala, or C.
- **HackerRank 90 min = Yes.** That OA is the real filter (`companies.md`; `recruiting.md` Part I §1). Prep timed LC mediums with some hards before you submit if you cannot sit the test immediately.
- **Cover letter is optional.** Skip it if you are speed-applying; the PDF is the screen. Paste the letter if you attach one.
- **NDA + privacy = type Vedant Desai / Yes.** Required to submit.
- **Do not claim Java, Go, Objective-C, Kubernetes, Snowflake, Databricks, Copilot, Fusion, or Rubrik/Zero Trust product experience.** JD languages are an or-list; absence of Java/Go is honest (`persona.md`).
- **Funnel:** Greenhouse resume + knockouts → 90-min HackerRank → recruiter → 1h algo → 1h practical/LLD → 45-min people-leader (`company.md`). first_published 2026-09-18. Apply in this first-wave window.
- **Jan–May 2027 is a long winter intern.** Confirm you can be in Palo Alto the full window before you submit.
