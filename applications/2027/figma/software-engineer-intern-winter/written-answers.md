# Figma — Software Engineer Intern (Winter 2027) · Written Application Answers

Draft answers for Greenhouse job `6131089004`. Grounded in `context.md`, user-supplied facts, and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented Figma internals, no Copilot, no Java, no JavaScript-as-TypeScript, no Snowflake/Databricks/Fusion/Tableau. Trim to each form’s length limit before submitting.

Apply: https://job-boards.greenhouse.io/figma/jobs/6131089004
Jobright: https://jobright.ai/jobs/info/6a7a2528b17cba5690365a31
Resume: `applications/2027/figma/software-engineer-intern-winter/Vedant Desai Resume.pdf`

Location is not a skip: San Francisco, CA or New York, NY Hub, in-person onboarding if hired, January 4, 2027 start.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First name | Vedant |
| Last name | Desai |
| Email | vedantde@umich.edu |
| Country | United States |
| Phone | (248) 704-4852 |
| Location (City) | Northville, MI |
| Resume/CV | `applications/2027/figma/software-engineer-intern-winter/Vedant Desai Resume.pdf` |
| Full legal name | Vedant Desai |
| Preferred First Name | *(optional — leave blank unless you use a nickname)* |
| Pronouns | *(optional — UNKNOWN; do not invent)* |
| How did you connect with us? | **Other** — Jobright (https://jobright.ai/jobs/info/6a7a2528b17cba5690365a31). Jobright is not in the listed options (FigFest / RTC-ColorStack-Talentboard / on-campus / virtual). |
| Expected graduation date? | **Spring 2028** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| First choice engineering work? | **Product Engineering** |
| Second choice? | **Backend/Infrastructure** |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Other Website | https://github.com/Verdent06 |
| Authorized to work in the country for which you applied? | **Yes** — US citizen; no visa sponsorship needed |
| Worked for Figma before (employee or contractor/consultant)? | **No** |
| Voluntary EEO | Decline / skip — do not invent |

Mailing address used on other apps (if the form asks): 49032 Freestone Dr, Northville, MI.

---

## Cover letter (if the form offers an upload / paste; skip if optional)

I am applying for Figma’s Software Engineer Intern (Winter 2027) role in San Francisco or New York. I want to spend the term embedded on a product team shipping user-facing features on a real-time collaborative design platform — not a research rotation and not a remote “AI tools” internship.

That is the work I already do. At CaseStudyPrep.AI I moved audio processing off the UI thread into a Web Worker so the real-time visualizer stayed at 60 FPS (main-thread blocking under 5ms) and cut a 27% audio-upload failure rate with fault-tolerant RxJS/S3 recovery. I founded Vylet, a live lead-sourcing product ($1,500 MRR, three clients): a Dockerized LangGraph pipeline with Redis/Celery workers and a named defect fix that lifted qualification from 79% to 89%. At Michigan Data Consulting I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract. SignalWeaver is a FastAPI + React/TypeScript dashboard I can defend layer by layer.

I have not worked at Figma and I do not claim Figma’s editor internals. I am a US citizen. I return to Michigan after Winter 2027 (Expected May 2028). I can start January 4, 2027 in the SF or NY Hub.

---

## 1. How did you connect with us?

**Other.** Jobright — https://jobright.ai/jobs/info/6a7a2528b17cba5690365a31

(FigFest, RTC/ColorStack/Talentboard, on-campus, and virtual event do not apply.)

---

## 2. Expected graduation date?

**Spring 2028.** University of Michigan, B.S. in Computer Science and Economics, Expected May 2028. Winter 2027 (January 4 start) is junior-year winter; I return to school for Fall 2027 and Winter 2028.

---

## 3. First choice engineering work?

**Product Engineering** — full-stack user-facing features, collaboration tools, product workflows.

---

## 4. Second choice engineering work?

**Backend/Infrastructure** — APIs, performance, developer-adjacent tooling. Not Security Engineering.

---

## 5. Based on the engineering work you listed above, briefly (2–4 sentences) describe a past project or experience that best reflects your interest in those areas.

At CaseStudyPrep.AI I was a Software Engineer Co-op on a voice product where the UI had to stay live while audio ran. I moved processing off the main thread into a Web Worker with an async stream handoff so the visualizer held 60 FPS and main-thread blocking stayed under 5ms, then fixed a 27% upload-failure rate by detecting expired S3 URLs mid-flight in RxJS and recovering without dropping the session. That is the product-engineering shape I want at Figma: user-facing performance plus a reliability fix you can measure. On the backend/infrastructure side, at Michigan Data Consulting I was the sole engineer on a five-month contract that shipped a production Flask REST API on AWS EC2 — ingestion through public endpoints, no backend team to share the design.

---

## 6. Why do you want to join Figma? (3–4 sentences)

I want to intern where the product *is* real-time collaboration — a canvas teams actually share — and where interns are embedded to ship a feature, not shadow. Figma’s posting is that job: product, platform, or open, matched to skills, with past intern work on FigJam diagramming, smart selection, and shared fonts. I already spend my time on user-facing performance and shipped APIs (CaseStudyPrep 60 FPS / 27% recovery; MDC Flask/EC2; SignalWeaver FastAPI + React). I have not used Figma’s editor as an engineer and I am not claiming your internals; I am applying because I want to learn that stack on a team that ships with PMs, designers, and QA. I can start January 4, 2027 in San Francisco or New York and I return to Michigan afterward.

---

## 7. LinkedIn, other website, work authorization, prior Figma employment

- **LinkedIn:** https://linkedin.com/in/vedantde06
- **Other website / GitHub:** https://github.com/Verdent06
- **Work authorization:** US citizen; authorized to work in the United States without sponsorship.
- **Worked at Figma before:** No
- **Sponsorship:** No

---

## Notes for the applicant (not for submission)

- **Lead with CaseStudyPrep + SignalWeaver React + MDC.** First-choice Product Engineering; second Backend/Infrastructure. Do not select Security.
- **Do not claim JavaScript, Java, Copilot, or Figma editor internals.** Inventory is Python / TypeScript / C++. TypeScript is not JavaScript.
- **Location is not a skip.** SF or NY Hub, January 4, 2027, cameras on, in-person onboarding if hired.
- **EEO / pronouns:** UNKNOWN — decline rather than invent.
- **Referral:** no Figma contact in `network.md`. A UMich alum on a product team still beats a cold Greenhouse pile.
- **Loop:** Greenhouse resume + essays → recruiter → Byteboard (~90 min reading crunch) → HM deep-dive → virtual onsite. Prep timed design-doc reading plus DS&A Easy–Med; behavioral is a filter.
