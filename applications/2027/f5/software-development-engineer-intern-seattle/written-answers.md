# EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY. Never `vedantde@umich.edu`.**
Override any Workday parse / Autofill / last-application email. The PDF header is already `verdent06@gmail.com`. If a field shows `vedantde@umich.edu`, delete it and type `verdent06@gmail.com` before submit.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

---

# F5 — Software Development Engineer Intern (Seattle, WA) · RP1039073 · Written Application Answers

Draft answers for Workday `ffive.wd5` / `f5jobs` req **RP1039073**. Grounded in the **live Workday posting and Apply SPA opened 2026-10-07**, CXS JSON, headless Chrome dump-dom of the public job URL + `/apply` + `/apply/applyManually`, `persona.md`, `grade.md` Interview angles, and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**This is Software Development Engineer Intern (Seattle, WA), Summer 2027, 12 weeks, F5 Tower / Seattle onsite.** It is **not** San Jose twin **RP1039076**, **not** Cork Software Engineering Intern **RP1038785**, **not** Tel Aviv WAF & WAAP **RP1038705**, **not** Tel Aviv DevOps & Cloud Infrastructure **RP1038691**.

**Do not invent:** Go, Java, C#, C (as distinct from C++), Kubernetes, Linux-as-a-required-skill, BIG-IP, NGINX (product), Shape, Distributed Cloud ops, an F5 internship or employment, a referral.

**Form-kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** PDF header is already **verdent06@gmail.com**. Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship. GPA **3.7** (do not write 3.66).

**Form-kit work history (this apply flow):**
- **Prior experience (jobs):** CaseStudyPrep.AI Software Engineer Co-op **and** founder of **Vylet** only.
- **MDC** = extracurricular only (student org / client project). Do not list as an internship/job even though it is Experience on the PDF.
- **Lyndbrook** = omit from the form (not on this PDF).
- **SpaceXAI Campus Lead Ambassador** = extracurricular if asked.
- **Awards / honors:** **None**.

**Do not submit from this agent.** Packet only.

Job (live ATS): https://ffive.wd5.myworkdayjobs.com/en-US/f5jobs/job/Seattle/Software-Development-Engineer-Intern--Seattle--WA-_RP1039073

Apply: https://ffive.wd5.myworkdayjobs.com/en-US/f5jobs/job/Seattle/Software-Development-Engineer-Intern--Seattle--WA-_RP1039073/apply

Resume: `applications/2027/f5/software-development-engineer-intern-seattle/Vedant Desai Resume.pdf`

**SHA-256:** `5082959d6309729e14414c05e61a92effaf876e2cec85ea1445178f91c2671f0`

Posted **2026-10-06** (`startDate`). Live chrome **Posted Today** at capture **2026-10-07**. Workday `includeResumeParsing: true`. `canApply: true`. `questionnaireId` `cb52c124859b10012f333a5d35360000`. `secondaryQuestionnaireId` `4aecc0de8a6a10012e39283ad6e50000` (matches progress-bar **Application Questions 1 of 2** and **2 of 2**). CXS `/apply` and `/questionnaire/{id}` returned **HTTP 406** without an account. **This agent did not create an account and did not submit.**

Apply now (`recruiting.md` Part II §8 first wave). Official US intern hiring usually starts September; interviews October–November; recruitment continues January–March until filled.

Airtable: [`recDx2Of8oiSqeGmm`](https://airtable.com/appkjmb1lqI38B5dG/tbld48HBTeRo4WpcG/recDx2Of8oiSqeGmm) (GrokBot Applications; Source **GitHub/SimplifyJobs**; Status stays **In Progress** until a human submits).

---

## Knockouts (read first)

1. Currently pursuing a bachelor's or master's at an accredited college or university in the United States — **clears.** University of Michigan, B.S. Computer Science and Economics.
2. Planning to graduate between **December 2027 and June 2029** — **clears.** **Expected May 2028**.
3. No more than 2 years of full-time professional tech industry experience in a similar role — **clears.** Under 2 years.
4. At least **two additional quarters/semesters** of school remaining after the internship — **clears.** Fall 2027 and Winter 2028 remain.
5. Enrolled in CS, Software Engineering, Information Technology, Computer Engineering, or related — **clears.** Computer Science (Economics is the dual).
6. Object-oriented language (examples: Python, Go, Java, C#, C) — **Python yes.** **Go no. Java no. C# no. C no.** Do not check them. C++ exists in the pool but is **not on this PDF**.
7. Able to work **onsite Seattle** for a **12-week** summer intern on one of: **May 24 – August 13 2027**, **June 1 – August 20 2027**, **June 21 – September 10 2027** — **Yes to all three windows** if the form is yes/no. If the form is pick-one, that is Vedant's pick (flagged below). Relocating from Northville / Ann Arbor, MI. Fully remote is **not** available.
8. Work authorization — no visa line on this JD. **US citizen; no sponsorship now or later.**

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on graduation window, remaining terms, Seattle onsite, or Go/Java/C#/C/Kubernetes.

---

## What was extracted from the live page (2026-10-07)

Pulled without creating an account, without uploading a resume, and without submitting. Live SPA: job posting + **Apply** → **Start Your Application** → **Apply Manually** `/apply/applyManually`. Cookie banner: **none** on this session. `userAuthenticated: false`.

### Job posting (public CXS JSON + live chrome)

`GET https://ffive.wd5.myworkdayjobs.com/wday/cxs/ffive/f5jobs/job/Seattle/Software-Development-Engineer-Intern--Seattle--WA-_RP1039073` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Software Development Engineer Intern (Seattle, WA)** |
| Company / hiringOrganization | **205 F5, Inc. (United States)** · careers chrome **Careers at F5** |
| Requisition | **RP1039073** · jobPostingId `Software-Development-Engineer-Intern--Seattle--WA-_RP1039073` · jobPostingInfo.id `34983845c35e10011a6c0e95f0ab0000` |
| locations | **Seattle** · jobRequisitionLocation **F5 Tower** |
| time type | **Full time** |
| posted on | **Posted Today** · `startDate` **2026-10-06** |
| Apply | Workday **Apply**. `includeResumeParsing: true` · `canApply: true` |
| Sign In | chrome **Sign In** |
| Nav | **Life at F5** · **Search for Jobs** · **Join Our Talent Community!** |
| `questionnaireId` | `cb52c124859b10012f333a5d35360000` (HTTP **406** without an account) |
| `secondaryQuestionnaireId` | `4aecc0de8a6a10012e39283ad6e50000` (HTTP **406** without an account) |
| Pay (JD body) | **42 USD – 55 USD** hourly |
| Term (JD body) | **12-week** intern: **May 24 – August 13 2027** · **June 1 – August 20 2027** · **June 21 – September 10 2027** |
| Work model (JD body) | Onsite for the summer; F5 **hybrid** environment; **fully remote not available**; relocate to **Seattle, WA** |

Verbatim eligibility (JD):

- **"Open to students currently pursuing a bachelor's or master's degree at an accredited college or university in the United States."**
- **"Planning to graduate between December 2027 and June 2029."**
- **"No more than 2 years of full-time professional tech industry experience in a similar role."**
- **"Must have at least two additional quarters/semesters of school remaining following the completion of the internship."**

No on-page screening radios on the job view. Knockouts live in the JD **Eligibility** / **Qualifications** lists.

Sidebar **Join Our Talent Community!** is not this apply. **Do not use it instead of Apply.**

### Similar Jobs on the intern facet (do **not** apply this PDF to them)

Software Development Engineer Intern (San Jose, CA) **RP1039076** · Software Engineering Intern **RP1038785** (Cork) · Software Development Intern - WAF & WAAP **RP1038705** (Tel Aviv) · DevOps & Cloud Infrastructure Intern **RP1038691** (Tel Aviv).

### Start Your Application (verbatim live labels)

Heading: **Start Your Application**

Subtitle: **Software Development Engineer Intern (Seattle, WA)**

| Exact control | What to do |
| --- | --- |
| **Autofill with Resume** | Preferred. Upload this packet PDF. Then confirm email is **verdent06@gmail.com** after parse |
| **Apply Manually** | Use if Autofill fails. Same facts below |
| **Use My Last Application** | Only if a prior F5 Candidate Home app exists. Still override email to gmail |

Footer on this page: **Follow Us** · **F5 Recruiting Privacy Notice** · © 2026 Workday, Inc. All rights reserved.

Do **not** click Create Account from this agent.

### Workday apply chrome (progress bar — verbatim)

Visible on `/apply/applyManually` **before** any later fields (`current step 1 of 8`):

1. **Create Account/Sign In** ← live stop (login wall)
2. **My Information**
3. **My Experience**
4. **Application Questions 1 of 2**
5. **Application Questions 2 of 2**
6. **Voluntary Disclosures**
7. **Self Identify**
8. **Review**

Also on this page: **Back to Job Posting**.

### Create Account (verbatim live fields, 2026-10-07)

Exact labels on `/apply/applyManually`. Did **not** create an account.

Password Requirements (verbatim bullets, this order):

- An alphabetic character
- A lowercase character
- A minimum of 8 characters
- A special character
- A numeric character
- An uppercase character

Consent text (verbatim): *By creating a candidate account, you agree to allow F5 to process your data in accordance with the F5 Recruiting Privacy Notice.* Also: *Please review F5's Generative AI (GenAI) guidance which outlines how GenAI can be appropriately used during the job application and selection process.* **Read More**

| Exact label | Answer |
| --- | --- |
| Email Address * | **verdent06@gmail.com** (never `vedantde@umich.edu`) |
| Password * | **Your real password.** Not stored in this repo. Must meet the six rules |
| Verify New Password * | Same as Password |
| ☐ I have reviewed the F5 Recruiting Privacy Notice and Generative AI guidance. | **Check** after you actually read both |
| **Create Account** | Click after the above. Do not submit the job from this agent |
| Already have an account? **Sign In** | Use if you already have an F5 Candidate Home account on `ffive.wd5` |
| **Forgot your password?** | Only if you already have an account |
| Enter website. This input is for robots only, do not enter if you're human. | **Leave blank** (honeypot) |

### Questionnaire API

- `questionnaireId`: `cb52c124859b10012f333a5d35360000`
- `secondaryQuestionnaireId`: `4aecc0de8a6a10012e39283ad6e50000`
- CXS `/apply` and `/questionnaire/{id}` returned **HTTP 406** without an account
- **My Information, My Experience, Application Questions 1 of 2, Application Questions 2 of 2, Voluntary Disclosures, Self Identify, Review were not visible.** Do **not** invent those question wordings. If later pages differ, answer the actual live label.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = omit from the form** (not on this PDF).
- **SpaceXAI Campus Lead Ambassador = extracurricular if asked.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA **3.7**, Junior.
- Languages/frameworks you can defend on this PDF: **Python, TypeScript, SQL, HTML/CSS, Angular, React, FastAPI, Flask, PostgreSQL, Redis, AWS, Docker, Git, GitHub Actions.** **Do not check Go, Java, C#, C, Kubernetes, BIG-IP, NGINX, Linux as a claimed required skill.**

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
| How Did You Hear About Us? | **Needs Vedant.** The board you actually used. Airtable source is **GitHub/SimplifyJobs**. **No F5 contact in `network.md` — do not pick Employee Referral.** If you opened this Workday URL from App Man / a job board: that board's option, or **Company website / Career site**. Do not invent LinkedIn vs Handshake vs other. |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### My Experience · Education

| Exact label | Answer |
| --- | --- |
| School or University * | **University of Michigan** (University of Michigan-Ann Arbor if the typeahead has it) |
| Degree * | **Bachelor of Science (BS)** |
| Field of Study | **Computer Science** (add **Economics** if a second row / dual-degree field is required) |
| Overall Result (GPA) | **3.7** (never 3.66) |
| From | **08/2025** (started **08/31/2025**) |
| To (Actual or Expected) | **05/2028** |
| Currently enrolled | **Yes** |
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
| Lyndbrook Capital | **Omit.** |
| SpaceXAI Campus Lead Ambassador | **Extracurricular only.** |
| SignalWeaver / Granular Synthesizer | **Not jobs.** |
| Awards / honors | **None.** |

Skills tags if shown: only **Python, TypeScript, SQL, HTML/CSS, Angular, React, Flask, FastAPI, PostgreSQL, Redis, AWS, Docker, Git, GitHub Actions**. Do not tag Go, Java, C#, C, Kubernetes, BIG-IP, NGINX.

### Application Questions 1 of 2 and 2 of 2 (login wall — wording NOT captured)

These two wizard steps were visible **only as progress-bar labels**. Question text was behind Create Account. Do **not** invent essay prompts. If a later step restates the JD minimums as radios, use:

| If the live label is | Answer |
| --- | --- |
| Available for a 12-week intern starting May 24, June 1, or June 21 2027? | **Yes** — available for **any** of the three full windows |
| Which start window? | **Needs Vedant** if the form is pick-one. All three windows are honest summers. Do not invent May vs June. |
| Graduating December 2027 – June 2029? | **Yes** — B.S. Computer Science and Economics, **Expected May 2028** |
| Two additional quarters/semesters remaining after the intern? | **Yes** — Fall 2027 and Winter 2028 |
| Willing to relocate to Seattle, WA? | **Yes** |
| Fully remote? | **No** — JD: fully remote not available. Onsite Seattle for the summer |
| ≤2 years full-time professional tech experience in a similar role? | **Yes** |
| Enrolled at an accredited US college? | **Yes** — University of Michigan |
| OOP language: Python? | **Yes** — FastAPI / Flask / Pandas / LangGraph through use on the PDF |
| OOP language: Go / Java / C# / C? | **No.** Do not check. |
| DSA / CS fundamentals? | **Yes** — coursework Data Structures & Algorithms |
| Linux / Shell / Kubernetes? | **Do not claim Kubernetes or a Linux internship.** Honest: Docker + GitHub Actions on the PDF. |
| AI/ML experience? | Honest if asked: shipped LangGraph/eval and FastAPI research-assistant work. This is **not** an ML intern identity. |
| Legally authorized to work in the United States? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| Returning to school after the internship? | **Yes** — Fall 2027 remains; Expected May 2028 |
| Ever worked for F5? | **No** |
| Why F5 / additional information / cover letter | **Needs Vedant** if a free-text box actually appears. **Not on the live pre-login pages.** Do not paste a fabricated essay as if it were extracted. |

If Application Questions 1 of 2 or 2 of 2 contain **any other free-text prompt**, stop and answer the live wording. Do not reuse another company's "why us" letter.

### Voluntary Disclosures / Self Identify (login wall)

Skip optional gender / race / ethnicity / veteran / disability unless a field is required (`recruiting.md` Part I §2 volume). If a required "I decline to answer" exists, use that. Do not invent EEO option lists.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field and on the PDF header.** Do not type `vedantde@umich.edu`. Never email this packet to that inbox — App Man pulls via `gh`.
- **GPA is 3.7.** Do not type 3.66.
- **This is Seattle RP1039073**, not San Jose RP1039076.
- **Do not claim Go, Java, C#, C, Kubernetes, BIG-IP, or NGINX.** Honest: Python, TypeScript, Docker, GitHub Actions, FastAPI, Flask, AWS.
- **Jobs on the form = Vylet + CaseStudyPrep only.** MDC stays extracurricular.
- **No F5 contact in `network.md`.** How you heard: GitHub / Simplify or the board you actually used. Not employee referral.
- **Funnel:** resume → HackerRank OA **[directional]** → recruiter + 1–2 tech (`persona.md` / `companies.md`). Prep STAR (CaseStudyPrep 27% upload; Vylet 79%→89% RCA; SignalWeaver pytest/Docker CI) and a Flask/EC2 + FastAPI walkthrough. Confirm US citizen, GPA 3.7, May 2028, Seattle 12-week window, sponsorship **No**.
- **Airtable `recDx2Of8oiSqeGmm` stays In Progress until a human submits.**
- **This agent did not submit.**
