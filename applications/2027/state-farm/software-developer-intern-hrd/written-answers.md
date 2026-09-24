# State Farm — Summer 2027 Intern - HR&D - Software Developer (Jibe/iCIMS 45689) · Written Application Answers

Draft answers for the live Jibe listing and iCIMS apply. Grounded in `persona.md` (full-stack intern lens: TypeScript / SQL / REST / Angular through use — **not** Power Apps / Power Automate / Power BI / Dataverse) and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**This is Summer 2027 Intern - HR&D - Software Developer (HR&D Workforce Technology).** Not Innovation Group Software Engineer. Not Enterprise Technology Mainframe. Not generic ET Software/Data/Infrastructure intern.

**Do not invent:** Power Apps, Power Fx, Power Automate, Power BI, DAX, Dataverse, Azure AD / Entra ID, ALM, Copilot, Snowflake, Databricks, Tableau, Fusion, State Farm HRIS / Workday-HCM internships.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu`.** Phone **248-704-4852**. US citizen, no sponsorship. Address **49032 Freestone Dr, Northville, MI 48168**. Junior, Expected May 2028, GPA **3.66**. LinkedIn https://www.linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06. DOB **12/16/2006**. SAT **1510**. UMich start **08/31/2025**. HS **Northville High School**, graduated **05/19/2025**. **~96 credits** by Summer 2027.

**Employment on the form: CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead are **extracurricular**. Awards / honors: **None**. Lyndbrook Capital: omit as a job (not on this PDF).

**Do not submit from this agent.** Paste pack only. App Man downloads via gh. Never email this pack.

Job (user URL): https://jobs.statefarm.com/jobs/45689?icims=1  
Canonical: https://jobs.statefarm.com/jobs/45689?lang=en-us  
Apply (iCIMS login): https://careers-statefarm.icims.com/jobs/45689/login  
Resume: `applications/2027/state-farm/software-developer-intern-hrd/Vedant Desai Resume.pdf`

**SHA-256:** `37ed36192096a155c83329e7d2d60b9e5740be83447c8ed3795f853222fd040d`

Posted **2026-09-23T15:25:00+0000**. Jibe `posting_expiry_date` **2026-10-30T04:00:00+0000**. Apply now (`recruiting.md` §8 first wave). Comp: **$28/hour** + **$2,000** stipend.

---

## Knockouts (read first)

1. Current **junior or senior**; undergraduate CS / Software Engineering / Software Development / IT / Systems Engineering; graduation **December 2027 or later** — **clears** (B.S. Computer Science and Economics; **Junior**; Expected **May 2028**).
2. GPA **3.25 preferred** (print on resume) — **clears** (**3.66 / 4.0**; already on the PDF).
3. Full-time student throughout the internship — **clears** (returns to UMich Fall 2027; Expected May 2028).
4. Reside in the continental U.S. for the summer term — **clears** if you relocate to a hub for **June 2 – August 11, 2027**.
5. Lawful US work immediately; employer **will not sponsor** (e.g. H-1B) — **clears** (US citizen; no sponsorship now or later).
6. Available **June 2, 2027 – August 11, 2027**, Monday–Friday **38.75 hours/week**, little to no schedule disruption — **Yes**.
7. Hybrid at **Bloomington, IL / Richardson, TX / Dunwoody, GA / Tempe, AZ**. Relocation benefits **will not apply** — **Yes**. Prefer **Bloomington, IL** (HQ; closest hub to Northville, MI). Also willing: Richardson (Axis 110, 110 W CityLine Dr Ste 100), Dunwoody, Tempe. Do **not** spoof a hub as home address.
8. Power Apps / Power Automate / Power BI / Dataverse — **not knockouts.** Do **not** check them.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on class year, sponsorship, hub relocate, or Power Platform.

---

## Exact form questions visible on the live page (captured 2026-09-24)

Inspected **without submitting** and **without creating an iCIMS account**.

### Job page (public Jibe SPA)

Pulled from `https://jobs.statefarm.com/jobs/45689?icims=1` (JSON-LD `JobPosting` + Jibe `/api/jobs` object `req_id` **45689**). Public listing has **no candidate input fields** besides Apply chrome.

| Exact text / fact on the posting | Answer |
| --- | --- |
| Title | **Summer 2027 Intern - HR&D - Software Developer** |
| Req / Job ID | **45689** · tags8 **2026-45689** · iCIMS uuid `fd03ecfd-6616-49d4-b1dd-4b021ef5ce8b` |
| Employer | **State Farm** (hiringOrganization State Farm; legal: State Farm Mutual Automobile Insurance Company) |
| Locations | **Richardson, Texas; Bloomington, Illinois; Dunwoody, Georgia; Tempe, Arizona** (Richardson street: Axis 110, 110 W CityLine Dr Ste 100, 75082) |
| Category / tags | Intern · Intern - Summer · Multi-Hub · Temporary Work Arrangement · Professional · Hybrid |
| Employment type | **INTERN** |
| Posted | **2026-09-23** |
| validThrough / expiry | **2026-10-30** |
| Pay | **$28/hour** + **$2,000** stipend — **Yes** |
| Dates | **June 2, 2027 – August 11, 2027** (10 weeks) — **Yes** |
| Hours | Monday–Friday, **38.75 hours per week** — **Yes** |
| Work arrangement | **HYBRID**. Relocation benefits **will not apply** |
| Pre-screen | Competitive candidates invited to a **pre-screening video** — acknowledge |
| Interview | Selected candidates progress through **two rounds of interviewing** — acknowledge |
| Apply CTA | **Apply** / `apply-now-btn` |

Jibe apply chrome strings on this client (exact labels in the SPA bundle; Apply **redirects** rather than collecting fields on Jibe):

| Exact label | What to do |
| --- | --- |
| Apply With Cover Letter | Optional. Prefer **without** cover letter unless iCIMS later requires one. If you pick this, paste the letter below |
| Apply Without Cover Letter | **Preferred** on the Jibe chrome |
| Apply without Resume | **Do not use.** Upload this packet PDF |
| LinkedIn apply (`li_easy_applyable: true`) | Optional. If used, overwrite email to **verdent06@gmail.com** |
| Indeed icon is in the bundle | `icims.config.web.indeed.easy.apply` is **0** — do not assume Indeed Easy Apply |

`meta_data.redirectOnApply: true`. `apply_url`: **https://careers-statefarm.icims.com/jobs/45689/login**. `ats_code`: **icims**.

### iCIMS login (live capture 2026-09-24 — blocked)

GET `https://careers-statefarm.icims.com/jobs/45689/login` (and iframe/mobile variants) returned **HTTP 405** AWS WAF **Human Verification**. No email / privacy / password labels were visible from this agent. **Do not invent State Farm-only essay prompts.**

Typical iCIMS login (Constellation / Principal analog — confirm live):

| If the live label is | Answer |
| --- | --- |
| Email | **verdent06@gmail.com** (never vedantde@umich.edu) |
| Privacy policy / data-collection consent | **Check** if you consent |
| Password / Re-enter | **Your real password.** Not stored in this repo |
| CAPTCHA | Solve it yourself. This agent could not pass AWS WAF |
| Social login | Optional: LinkedIn / Google / Microsoft. Prefer email so the address stays gmail |

**Do not submit from this agent.** Account creation is required.

### Wizard steps after login (NOT visible — do not invent essays)

Later iCIMS pages (profile, education, knockouts, EEO) were **behind login / WAF**. If the live wording differs, answer the actual question with the same facts.

---

## Identity / contact (typical iCIMS — later pages not captured)

Use these facts. Autofill may parse Ann Arbor from Education → use **Northville**.

| Typical label | Answer |
| --- | --- |
| Legal First Name | Vedant |
| Legal Last Name | Desai |
| Email | **verdent06@gmail.com** |
| Phone | **248-704-4852** · device **Mobile** · country **United States (+1)** |
| Address | **49032 Freestone Dr**, Northville, MI 48168, United States |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/state-farm/software-developer-intern-hrd/Vedant Desai Resume.pdf` |
| How did you hear about us? | **Company website** if you opened jobs.statefarm.com. **Job board** if Handshake/Indeed/LinkedIn. **Do not pick Employee Referral** — no State Farm contact in `network.md` |

### Education (typical iCIMS)

| Typical label | Answer |
| --- | --- |
| Highest Level of Education Completed | **High School Diploma/GED** (bachelor's not done). Do **not** pick Bachelor's Degree |
| School | **University of Michigan** |
| Degree | **Bachelor of Science** / B.S. |
| Major | **Computer Science** (dual CS + Economics is on the PDF; add Economics only if a second row is required) |
| Did You Graduate? | **No** |
| Graduation Year | **2028** (Expected May 2028) |
| GPA | **3.66 / 4.0** |
| Class standing | **Junior** (Expected May 2028). Summer 2027 = after sophomore year |
| From | **08/2025** (started **08/31/2025**) |
| High School | **Northville High School**, graduated **05/19/2025** if a second row is required |

### Work history if later steps ask (newest first; form jobs only)

| Employer | Title | Dates | Notes |
| --- | --- | --- | --- |
| Vylet | Founder | 05/2026 – Present | vyletdata.com. Current. **Form job.** |
| CaseStudyPrep.AI | Software Engineer Co-op (Voice AI) | 12/2025 – 05/2026 | Remote. Co-op ended. **Form job.** |
| Michigan Data Consulting (MDC) | — | — | **Extracurricular only.** On the PDF; not a form job |
| SpaceXAI Campus Lead Ambassador | — | — | **Extracurricular only.** |
| Lyndbrook / Granular / SignalWeaver | — | — | Not form jobs. SignalWeaver is a GitHub project |

Awards / honors: **None.** Internships completed: **1** titled co-op (CaseStudyPrep) plus founder work — do not inflate.

---

## Knockout / structured fields (fill exactly)

Later pages were behind login. Use these facts.

| If the live label is | Answer |
| --- | --- |
| Are you legally authorized to work in the United States? | **Yes** — US citizen |
| Will you now or in the future require sponsorship (incl. F-1 OPT/CPT, H-1B)? | **No**. JD: employer will not sponsor |
| Are you a current junior or senior? | **Yes — Junior**, Expected May 2028 |
| Graduation date | **May 2028** (if a day is required: **05/01/2028**) |
| GPA | **3.66** |
| Available June 2 – August 11, 2027 / 38.75 h/wk / little disruption | **Yes** |
| Willing to work hybrid at Bloomington IL / Richardson TX / Dunwoody GA / Tempe AZ | **Yes**. Prefer **Bloomington, IL**. Relocation self-funded (benefits will not apply) |
| Location preference | **Bloomington, IL for Summer 2027 only. Returning to the University of Michigan afterward (Expected May 2028).** Home remains Northville, MI |
| Selected interns must reside in the continental U.S. | **Yes** |
| Ever employed by State Farm? | **No** |
| Desired pay | **USD $28 / Hr.** (posted rate). Stipend is **$2,000** if they ask separately — do not add it into hourly |
| Pay negotiable | **Yes** if asked |
| Power Apps / Power Automate / Power BI / Dataverse / Power Fx | **No.** Do not check |
| SQL | **Yes** |
| JavaScript / TypeScript | **TypeScript Yes.** JavaScript-family via TypeScript / Angular / React. Do not claim Power Apps JS |
| Git / Agile | **Git Yes.** Agile analog: scoped delivery + GitHub Actions CI. Do not invent Jira/Azure DevOps |
| Skills tags if offered | Python, TypeScript, SQL, HTML/CSS, Angular, React, Flask, FastAPI, PostgreSQL, AWS, Docker, Git. **Do not tag Power Platform tools** |
| SAT | **1510** only if asked |
| DOB | **12/16/2006** only if asked |
| Gender / race / veteran / disability | Kit if you self-ID: Male; Asian; not a veteran; no disability. Else Prefer not to answer where allowed |

Voluntary EEO: **I do not want to answer** unless you choose to self-ID. Not used in hiring.

---

## Cover letter / "Why State Farm HR&D?" (paste only if a later step has a box)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

I am applying to Summer 2027 Intern - HR&D - Software Developer (Jibe/iCIMS 45689) on State Farm Human Resources & Development Workforce Technology. I want a 10-week hybrid seat building custom internal apps and process automation with an experienced developer team — sprint estimates, peer code review, and UI review with business areas — not Innovation Group, not Mainframe, and not an ML-research rotation.

What I can defend, in the languages I actually use:

- **REST APIs and stakeholder delivery.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I delivered a production Flask REST API on AWS EC2 and replaced portal searches plus irregular Excel exports with a Requests + Pandas ETL, eliminating ~800 hours of manual pulls across 400 tracked PACs. I scoped that delivery directly with MCFN stakeholders.
- **Process automation.** On Vylet I turned a ~30-minute manual process per business into a Dockerized pipeline (30 scored leads in 30 minutes — a 30x speedup) with Redis/Celery workers, then diagnosed a name-collision defect that lifted qualification from 79% to 89%. The data layer is injection-safe SQL with freshness checks.
- **JavaScript/TypeScript and UI.** At CaseStudyPrep.AI I recovered a 27% S3 upload-failure rate with RxJS URL regeneration for WAV files Angular silently rejected, and moved audio work off the UI thread (under 5ms / 60 FPS). SignalWeaver is FastAPI REST + React/TypeScript over Postgres, with GitHub Actions pytest.

I have not used Power Apps, Power Fx, Power Automate, Power BI, DAX, or Dataverse. Those are the shop I would ramp on rather than claim. I interview in Python, TypeScript, and SQL.

I am a US citizen. I do not need visa sponsorship now or in the future. GPA 3.66. I can be in **Bloomington, IL** (or Richardson / Dunwoody / Tempe) hybrid for June 2 – August 11, 2027, without relocation benefits, and I return to Michigan afterward (Expected May 2028). Class standing: Junior.

---

## Availability

**June 2, 2027 – August 11, 2027**, full-time **38.75 h/wk**, **hybrid**. Prefer **Bloomington, IL**. Also yes: Richardson, TX; Dunwoody, GA; Tempe, AZ. Self-funded relocate from Northville, MI. Returning to the University of Michigan after the internship (Expected May 2028). Class standing: **Junior**.

---

## Notes for the applicant (not for submission)

- **Do not apply from this agent.** Packet only. iCIMS wizard not seen (AWS WAF + login). Create Profile is required.
- **Email is verdent06@gmail.com everywhere.** Never `vedantde@umich.edu`.
- **Do not invent Power Apps / Power Automate / Power BI / Dataverse / Entra ID.** Honest analogs: REST, SQL, TypeScript/Angular, process automation (Vylet 30x), stakeholder UI-adjacent delivery (MDC).
- **Highest education completed = High School**, not Bachelor's. Did You Graduate = No. Graduation year 2028. Junior.
- **Pay = $28 / Hr.** plus acknowledge the **$2,000** stipend. Do not invent a different posted range.
- **How hear:** Company website / Job board. **No Employee Referral** (`network.md` empty for State Farm).
- **Form jobs:** CaseStudyPrep.AI + Vylet only. MDC extracurricular. SpaceXAI Campus Lead extracurricular. Awards None.
- **Hub:** Bloomington, IL first. Home address stays Northville. No relocation benefits.
- **This PDF is 45689 only.** Do not reuse on Innovation Group or Mainframe intern reqs.
- **Resume is the intern bottleneck** (`persona.md` / `companies.md` C-tier ~15–20%). Pre-screening video then two rounds. Do not invent a coding OA.
- **Cover letter:** skip unless a later step asks; paste from above if it does.
- **No State Farm contact in `network.md`.**
