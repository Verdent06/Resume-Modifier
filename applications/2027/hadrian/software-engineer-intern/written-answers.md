# Hadrian — Software Engineer Intern (Spring or Summer 2027) · Written Application Answers

Draft answers for Ashby `2b0423c6-947d-4226-8d23-90743bd5e63e`. Grounded in `persona.md` (full-stack spine + autonomous-factory / A&D manufacturing differentiator), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Go, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, ROS/CNC, factory-floor internships, Opus internals, or an MDC API traffic/latency number.

Apply: https://jobs.ashbyhq.com/hadrian-automation/2b0423c6-947d-4226-8d23-90743bd5e63e/application
Resume: `applications/2027/hadrian/software-engineer-intern/Vedant Desai Resume.pdf`

**Pulled from the live posting (Ashby GraphQL, 2026-09-03):** Hadrian · Software Engineer Intern · Los Angeles, CA · on-site · Engineering, Product, Design · $46.15–$50.71/hr · Fall 2026 / Spring 2027 / Summer 2027 on one req · expected graduation December 2027–June 2028 · ITAR U.S. Person.

This packet is **Spring 2027 and Summer 2027** only. Do not select Fall 2026.

Live form captured 2026-09-03 from Ashby GraphQL (`applicationForm.fieldEntries`). Seventeen fields. Two required long-text boxes. No cover letter field. No school/GPA fields.

**Email on the form and on the PDF must be `verdent06@gmail.com` only.** Do not use `vedantde@umich.edu`.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact titles on the Ashby form. `*` = required.

| Field (exact form wording) | Answer |
| --- | --- |
| First Name and Last Name * | Vedant Desai |
| Email * | **verdent06@gmail.com** |
| Phone number * | (248) 704-4852 |
| Current Company | Optional. Leave blank, or **University of Michigan**. If you want a current titled role: **Vylet**. Do not invent a manufacturing employer. |
| Current Location | Optional. **Ann Arbor, MI** (school). Mailing address used on other 2027 apps if a later step asks: 49032 Freestone Dr, Northville, MI (not in `context.md`). |
| Resume * | `applications/2027/hadrian/software-engineer-intern/Vedant Desai Resume.pdf` |
| Linkedin | https://linkedin.com/in/vedantde06 |
| Twitter/X | Leave blank. |
| Github | https://github.com/Verdent06 |
| Are you legally authorized to work in the United States? * | **I am authorized to work in the United States for any employer** — US citizen; no sponsorship now or later. Do **not** select present-employer-only, require-sponsorship, not-authorized, or unknown. |
| To conform to U.S. Government space technology export regulations, including the International Traffic in Arms Regulations (ITAR) you must be a U.S. citizen, lawful permanent resident of the U.S., protected individual as defined by 8 U.S.C. 1324b(a)(3), or eligible to obtain the required authorizations from the U.S. Department of State. Will you be able to obtain said authorization by date of work start? * | **U.S. person. This ITAR/EAR status includes U.S. citizens, U.S. nationals, lawful permanent residents (green card holders), and asylees and refugees with such status granted, not pending** |
| This job will be physically based in the office location indicated on this job description. Which of the following describes your current or future situation? * | **I do not currently live in the location mentioned, but would plan to relocate myself for this role.** On-site Los Angeles is required. Remote is a knockout. Housing support "may be available based on business need" — pick the Hadrian-assistance option only if you actually need it. |
| Where did you hear about Hadrian? | Optional. If you opened the Ashby posting directly: **Hadrian Career Website**. If that is not true, pick the true source. Listed options: Hadrian Career Website · Campus Job Board (Handshake, 12twenty, etc.) · Campus Event (Career Fair, Info Session, etc.) · LinkedIn · Employee Referral · Other. No Hadrian contact in `network.md` — do not pick Employee Referral. |
| Which term(s) are you interested in? Select all that apply. * | **Spring 2027** and **Summer 2027**. Do not select Fall 2026. |
| What is your graduation month and year? * | **May 2028** |
| Why are you interested in Hadrian? What excites you about the opportunity? * | Paste the short answer below. |
| Tell us about a project you're most proud of. It can be from a previous internship, a capstone, or something you built on your own. * | Paste the project answer below. |

Voluntary EEO / pronouns: not on this form. Skip if a later step adds them (`recruiting.md` Part I §2).

---

## Why are you interested in Hadrian? What excites you about the opportunity? *

I want to write software operators actually run — internal tools, APIs, pipelines, dashboards — on a factory that ships hardware, not a CRUD internship. That is this posting: the software backbone of Hadrian's autonomous factories for aerospace and defense, on-site in Los Angeles.

Closest analog I have is not CNC. It is production software for non-engineer stakeholders. At Michigan Data Consulting I was the only engineer on a five-month Michigan Campaign Finance Network contract: a Requests + Pandas ETL that replaced ~800 hours of manual pulls across 400 PACs, then a production Flask REST API on AWS EC2 wired into their research workflow. At Vylet (live product, $1,500 MRR) I Dockerized a LangGraph pipeline on Redis/Celery and diagnosed a name-collision defect that lifted lead-qualification from 79% to 89%. SignalWeaver is the dashboard half: React/TypeScript over async FastAPI REST, instrumented at 9.1s p50 / 15.2s p99, Docker Compose + GitHub Actions.

I have not shipped Go. I interview in Python and TypeScript. I can be on-site in Los Angeles for Spring 2027 or Summer 2027, I return to Michigan afterward (B.S. Computer Science and Economics, Expected May 2028, GPA 3.66), and I am a U.S. citizen / U.S. Person. I do not need sponsorship.

---

## Tell us about a project you're most proud of. *

Michigan Data Consulting for the Michigan Campaign Finance Network — the closest analog to "internal tools and a data pipeline that a non-SWE team actually uses."

Researchers were doing portal searches the Bureau of Elections capped, irregular Excel exports, and ~2 hours of hand normalization per committee. I replaced that with a Requests + Pandas ETL that ingested filings directly (~800 hours of manual pulls across 400 tracked PACs), then shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract so rankings and filings sat in their public research workflow. No backend team to share API design or deploy.

If you want the production-debug story instead: at Vylet I diagnosed a name-collision defect in ownership-verification that was rejecting valid targets; the fix lifted qualification from 79% to 89% with no change in sourcing volume. I will not invent an API QPS or latency number for the Flask/EC2 service — the sized claims are the ETL and the sole-engineer delivery.

---

## Notes for the applicant (not for submission)

- **Lead with MDC ETL + Flask/EC2, then Vylet 79%→89%, then SignalWeaver FastAPI + React dashboard** (`grade.md` Interview angles). CaseStudyPrep 27% S3 recovery is the other owned-failure story.
- **Do not claim Go.** JD lists Python, TypeScript, or Go; inventory is Python + TypeScript. Ramp if the team is Go-heavy; do not check it.
- **Do not claim Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, ROS, or CNC.** Differentiator on the page is production APIs/pipelines/dashboards + C++ systems depth (Granular), not factory hardware.
- **MDC Flask/EC2 has no traffic/latency number** (1 minor; out of rails). If asked, say so and point to 400 PACs / ~800 hours and sole-engineer delivery.
- **Granular has no xrun/CPU number.** Walk 16-voice / processBlock discipline if they probe systems; do not call it factory software.
- **Internship count if asked:** 1 titled co-op (CaseStudyPrep.AI). MDC is consulting; Vylet is founder. Do not inflate.
- **Referral:** none in `network.md`. A Torrance/factory-software intro still beats cold Ashby (`recruiting.md` §4–5).
- **Loop:** Ashby PDF screen → unpublished intern loop (no named OA; do not invent HackerRank). Binding early filter is the human-read resume (`company.md`). Prep DS&A mediums and a factory-ops narrative anyway.
- **ITAR / work auth are knockouts.** U.S. person + authorized for any employer. Remote is a knockout.
- **Company/role cap:** this is the first Hadrian 2027 packet (SWE intern). Live board also has Robotics Engineer Intern and Data Science/Data Engineer Intern — do not submit those from this packet.
