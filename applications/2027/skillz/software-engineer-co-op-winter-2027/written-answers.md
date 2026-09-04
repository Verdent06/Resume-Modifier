# Skillz Inc — Co-op, Software Engineer, Winter 2027 (Las Vegas, Greenhouse 8168006 / TAH-296) · Written Application Answers

Draft answers for the public Greenhouse apply flow. Labels and dropdowns captured from `https://boards-api.greenhouse.io/v1/boards/skillzinc/jobs/8168006?questions=true` on 2026-09-04 (job `id` 8168006; `requisition_id` TAH-296; `first_published` 2026-09-03; `education` = `education_required`). Grounded in `persona.md` (full-stack SWE co-op on payment-infra / real-money player flows — **not** RZR ads, **not** Beamable LiveOps, **not** a game-client seat) and `context.md` metrics only.

**Do not invent:** Java, Go, Kubernetes, Jenkins, Terraform, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, PCI, payment-processor SDKs, Skillz platform, card rails.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** Phone **248-704-4852**. US citizen, no sponsorship.

**Do not submit from this agent.** Paste pack only.

Apply: https://job-boards.greenhouse.io/skillzinc/jobs/8168006
Resume: `applications/2027/skillz/software-engineer-co-op-winter-2027/Vedant Desai Resume.pdf`

---

## Knockouts (read first)

1. **Binding — graduation window.** "Will you be enrolled as a student at the start of the program and graduate no more than 1 year after the program begins?" Program begins **January 11, 2027** → graduate by **January 11, 2028**. Expected **May 2028** is after that date. Answer **No**. Do not answer Yes. Binary knockouts auto-reject (`recruiting.md` Part I §1; `WORTH_IT.md`).
2. GPA 3.66 ≥ 3.3 — clears.
3. CS bachelor's enrolled — clears.
4. Onsite Las Vegas 5 days / 40h for Jan 11–Aug 20 2027 — **Yes** (relocate from Northville, MI).
5. Work authorization / no future sponsorship — **Yes** / **No**.

Country on the public board (HTML): **United States**.

---

## Knockout / structured fields (fill exactly)

Exact Greenhouse labels. `*` = `required: true` on the API.

| Field (exact label) | Required | Answer |
| --- | --- | --- |
| First Name | * | Vedant |
| Last Name | * | Desai |
| Email | * | **verdent06@gmail.com** |
| Phone | * | 248-704-4852 |
| Resume/CV | * | `applications/2027/skillz/software-engineer-co-op-winter-2027/Vedant Desai Resume.pdf` |
| Will you be enrolled as a student at the start of the program and graduate no more than 1 year after the program begins? Please note this is the requirement of the program. | * | **No** (May 2028 is after Jan 11 2028). This is the binding knockout. Do not answer Yes. Live options: Yes, No. |
| LinkedIn Profile | * | https://linkedin.com/in/vedantde06 |
| This Co-Op requires being onsite 5 days a week (40 hours/week) at our Las Vegas office for the full duration of the program. Are you able to meet this requirement? Please also confirm with your university before your initial call with us that you're able to complete the full program. | * | Yes — I can be onsite in Las Vegas 5 days/week, 40 hours/week, January 11–August 20, 2027. I will confirm with the University of Michigan before any initial call. Relocation: Yes. |
| University name | * | University of Michigan |
| Current GPA | * | 3.66 / 4.0 |
| How did you hear about us? | * | **Job Boards (e.g., LinkedIn, Indeed, Monster, Glassdoor)** — no Skillz contact in `network.md`. Do **not** pick Employee Referral. Live options include Recruiter Reached Out, Company Website, Job Boards, Company’s Social Media, Employee Referral, University/College Career Fair, Industry Conference/Event, Online Advertisement, Print Advertisement, Email Newsletter, Word of Mouth. |
| Why are you interested in joining our team? | * | Paste the short “why Skillz” below. Helper text: they review this with the hiring manager. |
| Do you currently know or have a personal connection with anyone who works here? If so please specify who. (Optional) | | **No** / leave blank — none in `network.md` |
| What is your desired compensation? | * | **$32/hour** (posted starting compensation; do not bid above) |
| Are you open to working onsite as specified on the job posting? | * | **Yes** |
| Do you currently reside in the required location as listed in the job posting? | * | **No** (Northville, MI) |
| If you do not reside in the required location, are you open to relocating to the required location? | | **Yes** |
| Are you legally authorized to work in the country where this role is located? | * | **Yes** |
| Will you now or in the future require sponsorship for an employment visa? | * | **No** |

Greenhouse also requires the **Education** widget (`education_required`):

| Education widget | Answer |
| --- | --- |
| School | University of Michigan |
| Degree | Bachelor's |
| Discipline | Computer Science (dual CS + Economics — pick CS if one) |
| End date year | 2028 |

If a later step asks fields not on this public form:

| If asked | Answer |
| --- | --- |
| Address | 49032 Freestone Dr, Northville, MI 48168 |
| GitHub | https://github.com/Verdent06 |
| GPA | **3.66 / 4.0** |
| Class standing | Junior (Expected May 2028; Jan 2027 is junior-year winter) |
| US citizen | **Yes** |
| SAT | **1510** |
| Date of birth | **12/16/2006** |
| Country | United States |
| Work authorization | US citizen; authorized for any US employer; no CPT/OPT/H-1B now or later |
| Availability | Winter 2027 term **available** (not Fall). Jan 11–Aug 20 2027 |
| Relocate Las Vegas | **Yes** |

Voluntary EEO / disability / veteran (if shown): **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

---

## Cover Letter (optional on Greenhouse — paste if you attach or “Enter manually”)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Skillz Inc — Co-op, Software Engineer (TAH-296 / Greenhouse 8168006)
Las Vegas, NV · January 11, 2027 – August 20, 2027

I am applying to the Winter 2027 Software Engineer co-op on Skillz’s payment and platform backend — APIs and services for real-money player flows, not a game-client seat and not RZR/Beamable. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen and will not need visa sponsorship. I can be onsite in Las Vegas 5 days/week, 40 hours/week, for the full January 11–August 20, 2027 term.

I want this seat because the work is backend APIs, production debug, and data integrity on money-moving systems. What I can defend:

- **Production REST on AWS.** At Michigan Data Consulting I was the sole engineer on a 5-month MCFN contract: a Requests + Pandas ETL that cut ~800 hours of manual pulls across 400 tracked PACs, served through a Flask REST API on AWS EC2.
- **Data integrity + a named production defect.** On Vylet I own an asyncpg layer with injection-safe SQL timestamp checks that trigger re-scrapes, and I fixed a name-collision defect that lifted lead-qualification from 79% to 89%. The pipeline is Dockerized (Redis/Celery), 30 scored leads in 30 minutes.
- **Production debug + CI.** At CaseStudyPrep I recovered a 27% S3 upload-failure rate (expired presigned URLs). SignalWeaver ships async FastAPI REST (9.1s p50 / 15.2s p99) with a React/TypeScript dashboard, Docker Compose, and GitHub Actions (frontend build, pytest, API image).

I have not used Java or Go. I would ramp on the team’s server-side stack rather than pretend I already have it. I also do not meet the program rule that graduation must fall within one year of January 11, 2027 — my expected date is May 2028 — and I am answering that Greenhouse question honestly.

Vedant Desai

---

## Short “why Skillz” (paste into the required textarea)

I want a Winter 2027 co-op writing backend services and APIs next to a payments/platform team — deposit/withdrawal/payout analog is REST, data integrity, and production debug, not a game-client rotation.

MDC: Requests + Pandas ETL + Flask REST on AWS EC2 (~800 hours / 400 PACs). Vylet: injection-safe SQL freshness, 79% → 89% defect fix, Docker/Redis/Celery pipeline (30x). CaseStudyPrep: 27% S3 upload-failure recovery. SignalWeaver: FastAPI REST + React/TypeScript + GitHub Actions/pytest.

No Java or Go in my inventory — I would ramp on the team’s server-side languages. US citizen; no sponsorship. I can be onsite in Las Vegas 5 days/week, 40 hours/week, January 11–August 20, 2027. Expected May 2028 (GPA 3.66). I do not meet the “graduate no more than 1 year after the program begins” rule; I am answering that question No.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Greenhouse field.** Do not type `vedantde@umich.edu`.
- **Graduation window is No.** May 2028 > Jan 11 2028. Do not “clarify in the essay” into a Yes.
- **Comp is $32/hour.** Posted starting compensation; do not bid above.
- **How you heard:** Job Boards. No Skillz contact in `network.md`.
- **Do not claim Java, Go, Kubernetes, Jenkins, Terraform, PCI, card rails, or Skillz platform experience.** Java/Go are “or similar”; absence is honest (`persona.md`).
- **Cover letter is optional.** Skip it if you are speed-applying; the PDF is the screen (`recruiting.md` Greenhouse/human-read). Paste the letter if you attach one.
- **Funnel:** resume-first (`company.md`); unpublished intern OA (HackerRank is a full-time analog). Apply in this first-wave window (posted 2026-09-03) only if still submitting despite the knockout.
