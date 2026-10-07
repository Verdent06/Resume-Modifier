# EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.**
Override any Oracle HCM parse / Autofill / last-application email. PDF header is already `verdent06@gmail.com`. If a field shows `vedantde@umich.edu`, delete it and type `verdent06@gmail.com` before submit.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

---

# S&C Electric Company — Software Engineer Intern (Oracle CX 107374) · Written Application Answers

Draft answers for Oracle Cloud HCM Candidate Experience on `ejia.fa.us6.oraclecloud.com`, site **CX_1001**, job **107374**. Grounded in the **live posting opened 2026-10-07**, `recruitingCEJobRequisitionDetails` finder `ById;Id=107374,siteNumber=CX_1001`, guest `/apply` SPA, `persona.md`, `grade.md` Interview angles, and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**This is Software Engineer Intern 107374 (Chicago hybrid, Summer 2027, MES/MOM).** The JD body still says “Software Engineer Co-Op” / “Software Engineer I” in places — **same req**. It is **not** Electrical/Computer Engineer Intern, **not** the Early Talent FTE Software Engineer I rotation, **not** a protection-firmware intern.

**Do not invent:** C#, .NET, MySQL, MES, MOM, Raspberry Pi, shop-floor IoT, IntelliRupter/Vista product firmware, an S&C internship.

**Form kit email MUST be `verdent06@gmail.com`.** Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship. GPA **3.7** (unrounded 3.66 — do **not** type 3.66).

Airtable: [`rec9CEabmUt1zzuf9`](https://airtable.com/appkjmb1lqI38B5dG/tbld48HBTeRo4WpcG/rec9CEabmUt1zzuf9) (In Progress — kit landing; **do not submit until the human apply**). Source logged: **GitHub/SimplifyJobs**.

Listing: https://ejia.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/107374

Apply: https://ejia.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/107374/apply

Resume: `applications/2027/sc-electric/software-engineer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `4e0e0dbd197a6afef97aad64d076beab222fb33c9c0648ce606028ba349c2537`

Posted **2026-10-07T13:45:32Z**. `ExternalPostedEndDate` **2026-10-09T05:00:00Z**. `ApplyWhenNotPostedFlag` **false** — apply before the posting ends. RequisitionId **300001561253973**. Primary location **Chicago, IL, United States**. WorkplaceType **Hybrid**. Pay **$22–$30/hr**. Shift **8:00 am – 4:30 pm, Monday–Friday**. **This agent did not create an Oracle draft, did not create an account, and did not submit.**

---

## Knockouts (read first)

1. In-progress degree from an accredited university with a concentration in **Computer Science, Computer Engineering, Electrical Engineering, or other related field** **and returning to school full-time after the work session** — **clears.** B.S. Computer Science and Economics, University of Michigan. Expected May 2028; Fall 2027 and Winter 2028 remain after Summer 2027.
2. Chicago, IL hybrid, 1st shift 8:00 am–4:30 pm, Monday–Friday, Summer 2027 — **Yes** if you actually take the seat. Relocate from Northville, MI for the term; return to Michigan afterward. Exact start/end dates **not printed** on this JD.
3. Work authorization — **clears** (US citizen; no sponsorship now or later). This JD prints **no** visa or clearance line. If a later radio asks sponsorship: **No**.
4. Pay **$22–$30/hour** — **Yes** if you accept the posted intern range.
5. Physical demands (occasional shop-floor standing; lifting production parts/tooling **<50 pounds**; frequent walking indoors/outdoors) — **Yes** if you will do that for this intern. Not a degree/class-year/clearance gate.
6. Basic knowledge of .NET C# **or related** technologies, SQL/MySQL, REST, HTML/CSS/Javascript — **related: yes** (Python, TypeScript, SQL, REST, Angular, HTML/CSS on the PDF). **C# / .NET / MySQL / Raspberry Pi as claimed skills: No.** Do not check C#.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on sponsorship, GPA, class year, return-to-school, or invented C#/.NET/MES.

Quoted eligibility (live `ExternalDescriptionStr`, 2026-10-07): *"In-progress degree program from an accredited university/college program with a concentration in Computer Science, Computer Engineering, Electrical Engineering, or other related field and returning to school full-time after the work session."*

---

## What was extracted from the live page (2026-10-07)

Pulled without creating an account, without creating an apply draft, without uploading a resume, and without submitting.

### Job posting (public REST + apply SPA chrome)

`GET https://ejia.fa.us6.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails?finder=ById;Id=107374,siteNumber=CX_1001` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Software Engineer Intern** |
| Job Identification | **107374** |
| RequisitionId | **300001561253973** |
| Category | **003 - Intern** |
| RequisitionType | **Campus** |
| JobFunction | Intern (`SC_ELECTRIC_INTERN`) |
| StudyLevel | Some College |
| Primary location | **Chicago, IL, United States** |
| WorkplaceType | **Hybrid** (`ORA_HYBRID`) |
| JobSchedule | Full time |
| JobShift | 1 |
| Posted | **2026-10-07T13:45:32Z** |
| End date | **2026-10-09T05:00:00Z** (`ApplyWhenNotPostedFlag` false) |
| Pay (JD body) | **$22–$30 per hour** based on experience |
| Shift (JD body) | 1st shift: **8:00 am – 4:30 pm, Monday – Friday (Hybrid)** |
| Term | **Full-Time Summer 2027 Internship** |
| Apply | `/hcmUI/CandidateExperience/en/sites/CX_1001/job/107374/apply` **HTTP 200** (SPA shell, `oj-hcm-ce` **2607.26**) |

Guest `recruitingCEApplyFlows` returned **empty** (`count: 0`) without a saved draft. `recruitingCEQuestionnaires` **HTTP 404** as a guest. Finder `findByRequisitionNumber` rejected without a valid guest session. **Do not POST a job application or draft from this agent.**

### Exact form questions visible without an account

The apply route is an Oracle CE SPA (`oj-hcm-ce` 2607.26, site **S&C Minimal Career Site** / `CX_1001`). Visible without login / without a draft:

**Job page chrome (public):**

- Title **Software Engineer Intern**
- Location **Chicago, IL, United States**
- Apply control that routes to `/job/107374/apply`

**Apply SPA first screen (Oracle CE guest chrome — i18n keys in this tenant’s CE bundle):**

| Exact label (CE i18n / guest chrome) | Answer |
| --- | --- |
| Email Address * (`apply-flow.authentication-screen.email.label`) | **verdent06@gmail.com** |
| Helper (typical CE copy) | Guest apply — do **not** create a second account with the UMich email |
| I agree with the terms and conditions * (`apply-flow.legal-disclaimer.i-agree-with-terms-and-conditions`) | Check **Yes** only after reading the live T&Cs (required to proceed; not an employment yes) |

Cookie banner: accept or reject as you prefer.

**Later wizard pages (personal info, resume, education, experience, application questions, EEO, e-sign) were not returned as questionnaire items without a draft.** CE bundle keys confirm later sections *exist as chrome* (not S&C-specific essays): Drop Resume / Drop Cover Letter, First/Last name, phone, address, education, experience, optional cover letter, optional “more about you” / disqualification questions **if configured for this req**. **S&C-specific knockout radios and any free-text essay were not visible.** Do **not** invent extra essay prompts. If the signed-in form differs, answer the actual question with the same facts below.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI Software Engineer Co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular only.**
- **SignalWeaver = project, not a job.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA **3.7**, Junior.
- Languages you can defend on **this** PDF: **Python, TypeScript, SQL, HTML/CSS, Angular.** Do **not** check C#, .NET, MySQL, MES, MOM, Raspberry Pi.

---

## Knockout / structured fields (fill exactly)

### Contact / identity (after email + T&Cs)

| Field | Answer |
| --- | --- |
| Last Name * | Desai |
| First Name * | Vedant |
| Title | **Mr.** if required; else blank |
| Middle Name | leave blank |
| Preferred First Name | blank unless required |
| Email Address | **verdent06@gmail.com** (pre-fill; overwrite school email if it appears) |
| Phone Number * | **248-704-4852** · country **United States (+1)** · **Mobile** |
| Country * | United States |
| Address Line 1 * | **49032 Freestone Dr** |
| Address Line 2 / 3 | blank |
| Postal Code * | **48168** |
| City * | **Northville** (not Ann Arbor, not Chicago — current home) |
| State * | **Michigan** |

### Documents and URLs

| Field | Answer |
| --- | --- |
| Drop Resume Here * / Upload Resume (`apply-flow.profile-import.drop-your-resume-here`) | `applications/2027/sc-electric/software-engineer-intern/Vedant Desai Resume.pdf` (match SHA-256 above) |
| Drop Cover Letter Here | Optional. Use the letter below if attaching. Skip if speed-applying — the PDF is the screen (`companies.md`: bottleneck is the resume) |
| Link 1 | https://linkedin.com/in/vedantde06 |
| + Add Another Link | https://github.com/Verdent06 · optional third: https://vyletdata.com |

### Education

| Field | Answer |
| --- | --- |
| School | **University of Michigan** / Ann Arbor — not Dearborn/Flint. If typeahead misses it: **Other** → University of Michigan |
| Degree | B.S. Computer Science and Economics (pick **Computer Science** if one major; add **Economics** as a second major row if required) |
| Highest level of education obtained | **High School Diploma / GED** (bachelor's in progress; do **not** pick Bachelor's Degree) |
| Did you graduate? | **No** |
| Start | **08/31/2025** |
| Graduation / expected | **May 2028** (picker day: **05/01/2028** if needed) |
| GPA | **3.7 / 4.0** — do **not** type 3.66 |
| Currently enrolled | **Yes** |
| Class standing | **Junior** (Expected May 2028; Summer 2027 = after sophomore year / rising junior) |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |

High school row only if a second education line is required: Northville High School, Northville MI, graduated **05/19/2025**.

### Work history on the form (not the PDF)

| Role | How to enter |
| --- | --- |
| Vylet · Founder | **Job.** May 2026 – Present. Automated lead-sourcing platform; $1,500 MRR, three clients. vyletdata.com |
| CaseStudyPrep.AI · Software Engineer Co-op (Voice AI) | **Job.** Dec 2025 – May 2026. Remote. Titled prior co-op. |
| Michigan Data Consulting (MDC) | **Extracurricular only.** Data Engineer project for Michigan Campaign Finance Network, Jan 2026 – May 2026. Do **not** list as an internship/job even though it is Experience on the PDF |
| Lyndbrook Capital | **Do not add as a job.** Consulting engagement; essays only if they ask |
| SignalWeaver | **Project**, not a job |

### Typical Oracle CE application questions (not visible as a guest — confirm live labels)

If a later step shows these (or the JD qualifications restated as radios), use:

| If the live label is | Answer |
| --- | --- |
| Currently pursuing CS / CE / EE or related? | **Yes** — B.S. Computer Science and Economics |
| Returning to school full-time after the work session? | **Yes** — Fall 2027 and Winter 2028 remain |
| Are you legally authorized to work in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship (H-1B, CPT, OPT, etc.)? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| GPA | **3.7 / 4.0** |
| Expected graduation | **May 2028** |
| Class standing | **Junior** |
| Willing / able to work hybrid in Chicago, IL, 8:00 am–4:30 pm, Monday–Friday, Summer 2027? | **Yes** — relocate from Northville, MI for the term |
| Desired pay / salary | Posted intern range **$22–$30/hr**. If a dropdown is annualized summer pay, pick the band that covers ~$22–$30 × hours, not a $100k+ FTE band |
| Ever worked for S&C Electric? | **No** |
| Relatives at S&C Electric? | **No** |
| Employee referral? | **No.** `network.md` has **no S&C contact**. Do **not** invent a name |
| How did you hear about this position? | **Vedant must pick the true source.** Airtable source is **GitHub/SimplifyJobs**. If you opened the Oracle CX URL directly: company website / Oracle CE. If LinkedIn: Job Board → LinkedIn. **Not** Employee Referral |
| C# / .NET | **No** as a claimed skill. Do not check. Related stack on the PDF: Python, TypeScript, SQL, REST, Angular |
| SQL | **Yes** — Vylet injection-safe SQL timestamp / re-scrape on the PDF |
| HTML / CSS / Javascript | **HTML/CSS yes.** Javascript-family: **TypeScript + Angular** on the PDF. Do not claim vanilla JS years you cannot defend |
| Angular | **Yes** — CaseStudyPrep Angular MIME/S3 recovery on the PDF |
| Python | **Yes** — through use on the PDF. Do **not** claim Raspberry Pi / shop-floor IoT |
| MySQL / MES / MOM / Raspberry Pi | **No** |
| Willing to submit a drug and background test? | **Yes** if you will take the seat (manufacturing campus; marijuana can still disqualify) |
| Occasional lifting <50 lb / shop-floor walking | **Yes** if you will do the intern’s physical demands |
| I consent to SMS recruiting | **No, I do not consent** unless you actually want texts (answer is required if shown; consent is optional) |

Voluntary EEO / disability / veteran: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Skip for volume (`recruiting.md` Part I §2).

### E-signature

| Field | Answer |
| --- | --- |
| Full Name * | **Vedant Desai** |
| Submit | **Do not click.** Human submits after paste-check |

---

## If a later step asks a free-text “why this role” (wording NOT on the guest page)

**Confirm the live prompt.** Do not paste this if the question is different. Do not invent a prompt that was not on the page.

Short answer (2–3 sentences) if the live question is interest in **this** Software Engineer Intern / MES seat:

I want Summer 2027 writing full-stack software that manufacturing teams actually run — REST APIs, a SQL-backed store, and a named frontend — not a research rotation. S&C’s intern seat is that job: in-house MES/MOM under senior engineers, Angular exposure, and shop-floor context in Chicago hybrid. I have not used C#/.NET or Raspberry Pi; what I can defend is a Flask REST API I shipped as the sole engineer, Angular/RxJS production-defect recovery, and a named pipeline RCA (79%→89%). I return to Michigan afterward (B.S. CS + Economics, Expected May 2028). US citizen; no sponsorship.

---

## Cover letter (optional upload)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

S&C Electric Company — Software Engineer Intern
6601 N Ridge Blvd, Chicago, IL 60626

Re: Software Engineer Intern (Oracle CX 107374) — Chicago hybrid, Summer 2027

I am applying for the Summer 2027 Software Engineer Intern seat in Chicago — in-house Manufacturing Execution Software / MOM under senior engineers, not Electrical/Computer Engineer intern and not the Early Talent FTE Software Engineer I rotation. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.7). I am a U.S. citizen and do not need visa sponsorship. I can relocate from Northville, MI to Chicago for the internship term (hybrid, 8:00 am–4:30 pm) and return to Michigan afterward.

I have not used C#, .NET, MySQL as a claimed dialect, MES/MOM product internals, or Raspberry Pi shop-floor IoT. What I can defend is full-stack delivery a non-builder used: REST, SQL, a named frontend, and a named production defect with a before/after.

What I can defend:

- **REST + stakeholder workflow.** At Michigan Data Consulting I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month Michigan Campaign Finance Network contract, after replacing portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL that eliminated ~800 hours of manual pulls across 400 tracked PACs.
- **Angular frontend + named defect.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with RxJS logic that regenerated expired S3 URLs and negotiated MIME types for WAV files Angular silently rejected, then moved processing off the UI thread (under 5ms; 60 FPS visualizer).
- **Application maintenance analog.** I run Vylet (vyletdata.com; $1,500 MRR, three clients): a Dockerized pipeline that turned a ~30-minute manual process into 30 scored leads in 30 minutes, a name-collision defect I diagnosed (qualification 79% → 89%), and injection-safe SQL timestamp checks that re-scrape stale records.

I want Summer 2027 on 107374 learning S&C’s MES/MOM stack on the job — Python/TypeScript/SQL/Angular I can defend today, C# I will not fake on the form.

Sincerely,
Vedant Desai

---

## Do not submit checklist

- Email is **verdent06@gmail.com** on every field and matches the PDF
- GPA **3.7** (not 3.66)
- C# / .NET / MySQL / Raspberry Pi / MES / MOM **unchecked**
- Return-to-school **Yes**
- Chicago hybrid **Yes** only if you will actually relocate
- No employee referral
- Apply before **2026-10-09 05:00 UTC**
- **Do not click Submit from this agent**
