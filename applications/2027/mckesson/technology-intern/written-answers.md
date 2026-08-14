# McKesson (CoverMyMeds) — CMM Technology Intern, Summer 2027 · Cover letter & Workday answers

Draft answers for Workday req `JR0151979`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented healthcare internships, no Ruby/Elixir/MSSQL, no invented metrics. Trim to the form's length limit before submitting.

This posting is a **catch-all**. Recruiting may route you to Software Development, Platform, Infrastructure/SRE, Data Engineering, Security, or Technology Business Analyst. Prefer **Software Development** and **Data Engineering**. Platform / cloud-and-database only as Flask/FastAPI + AWS/Docker/Postgres/Redis work. Do **not** volunteer Security or Tech BA unless they ask. Do **not** claim SRE/Kubernetes.

Apply: https://mckesson.wd3.myworkdayjobs.com/sourcer_on_req/job/USA-OH-Columbus/CMM-Technology-Intern---Summer-2027_JR0151979

**Deadline:** 17 Aug 2026. No housing, relocation, student visa, or Green Card help. Hybrid, Columbus OH (CMM Main Campus, 910 John Street).

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/mckesson/technology-intern/Vedant Desai Resume.pdf` |
| Location | **Columbus, OH** — hybrid at CMM Main Campus. Yes, I can be there for Summer 2027. |
| Housing / relocation | Company does **not** provide housing or relocation. I will arrange my own housing in Columbus. |
| Currently enrolled in CE / CS / EE bachelor's? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduate Spring 2028 or sooner? | **Yes** — Expected May 2028 |
| GPA | **3.66 / 4.0** (cutoff is 3.0) |
| Work authorization / sponsorship | **U.S. citizen.** Authorized to work in the U.S. without visa sponsorship now or in the future. McKesson early talent does not sponsor. |
| Age 18+ | **Yes** |
| How did you hear about this role? | **Simplify** (https://simplify.jobs/p/8b699e41-5c53-4b40-aaf9-57a6bd162427). If Simplify is not listed: **LinkedIn Jobs** / Other → Simplify. |
| Pay $16.50–$27.50/hr | **Yes** — accept the posted intern range |
| Languages you can interview in | **Python, SQL, TypeScript/JavaScript (Angular, React), C++.** Do **not** check Ruby, Elixir, Java, C#, MSSQL, Kubernetes, Splunk, or Sidekiq. |

---

## Cover letter (paste into Workday "Cover Letter" / additional information)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

McKesson / CoverMyMeds — Technology Internship
Columbus, OH (hybrid)

Re: CMM Technology Intern — Summer 2027 (JR0151979)

Dear CoverMyMeds hiring team,

I am applying for the CMM Technology Intern role in Columbus for Summer 2027. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen, authorized to work without sponsorship, and I can work hybrid at the CMM Main Campus for the 10-week program. I will arrange my own housing.

CoverMyMeds builds partner-facing software that gets patients their medication. That is the same shape of work I already do: analyze a messy partner workflow, design and document a solution, then ship and automate it.

What I would bring to a Software Development or Data Engineering seat:

- **Partner-facing analysis, design, and delivery.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and delivered a production Flask REST API on AWS EC2 into their public research workflow. I scoped ingestion through REST endpoints directly with MCFN — no backend team behind me. That is the closest analog I have to "analysis, design, documentation, engineering, and automation of solutions we build for partners."
- **Automation with a database and a deploy.** I founded Vylet (vyletdata.com), a live lead-sourcing product at $1,500 MRR across three paying clients. I turned a ~30-minute manual process into a Dockerized pipeline with Redis/Celery workers (30 scored leads in 30 minutes — a 30x speedup) and an asyncpg data layer with injection-safe SQL freshness checks. On SignalWeaver I served research scores through FastAPI REST, Postgres, Docker Compose, and a GitHub Actions pipeline (frontend build, pytest, API image).
- **Multi-stack, honestly scoped.** I ship Python (Flask, FastAPI) and TypeScript (Angular/RxJS, React). At CaseStudyPrep.AI I cut a 27% audio-upload failure rate by regenerating expired S3 URLs mid-flight. I have not interned in Ruby, Elixir, or MSSQL; I would ramp onto CoverMyMeds' stack the same way I ramped onto Flask, FastAPI, and Angular — by shipping on the team's platforms.

I want this seat because it is embedded engineering on partner solutions, not a generic rotation. Prefer Software Development or Data Engineering. If you place me on Platform or cloud/database work, the Flask/EC2, Docker, Postgres, and Redis delivery is what I can defend on day one.

Sincerely,
Vedant Desai

---

## "Why CoverMyMeds / why this internship?"

I want a summer embedded on a team that ships partner-facing software — analysis, design, engineering, automation — not a notebook or a help-desk intern seat. CoverMyMeds is the prior-auth / medication-access platform inside McKesson. That is more interesting to me than another generic web rotation because the user of the software is a partner with a real workflow.

The work I can defend:

- **Software Development / Data Engineering.** MCFN: sole engineer, Python ETL, Flask REST on EC2, stakeholder scoping. Vylet: Dockerized automation, Redis/Celery, SQL freshness. SignalWeaver: FastAPI + Postgres + CI.
- **Platform / cloud / database, honestly scoped.** AWS EC2, Docker Compose, GitHub Actions, PostgreSQL, Redis. I have not run Kubernetes or a production SRE rotation, and I will not pretend to.
- **Not Security or Tech BA unless you ask.** I am applying as an engineer who can explain technical choices to non-engineers (MCFN stakeholders), not as a BA or a security intern.

I can be in Columbus hybrid for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need visa sponsorship.

---

## "Tell us about a project you built" / additional information

**MDC (partner delivery).** Five-month contract, only engineer. Requests + Pandas ETL replacing ~800 hours of manual PAC pulls; production Flask REST API on AWS EC2 wired into MCFN's public research workflow. I scoped the work with the nonprofit from ingestion through endpoints.

**Vylet (automation + data).** vyletdata.com. Dockerized pipeline, Redis/Celery, 30x speedup, live $1,500 MRR. SQL timestamp validation that re-scrapes stale records.

**SignalWeaver (API + database + CI).** FastAPI REST at 9.1s p50 / 15.2s p99 across 90 tickers; Docker Compose (API + Postgres/pgvector + nginx); GitHub Actions (pytest + image build).

I have not built prior-authorization software. I have shipped partner-facing APIs and automation, and I would ramp onto CMM's domain on the team.

---

## "Preferred team / which intern track?"

If the form lets you pick: **Software Development** first, **Data Engineering** second. If they ask about Platform / Cloud and Database / SRE: talk Flask/EC2, Docker, Postgres, Redis, GitHub Actions — not Kubernetes. If they ask about Security: "I have not interned in security. I write injection-safe SQL and ship authenticated REST; I would ramp on the team's threat model." If they ask about Tech BA: "I have scoped delivery with non-engineer stakeholders (MCFN). I am applying as an engineer who can explain choices, not as a BA."

---

## "Tell us about a time you explained a technical choice to a non-engineer."

At MCFN I was the only engineer on the contract. Researchers were spending ~2 hours per committee on portal searches and irregular Excel exports. I walked them through why a Requests + Pandas ingest plus a Flask REST API on EC2 would replace that workflow, what they would query, and what I would own through the 5-month window — without a backend team to hide behind. The result was the public research API and ~800 hours of pulls removed across 400 tracked PACs. That is the communication bar this JD names.

---

## Availability

Summer 2027, 10 weeks, hybrid Columbus (CMM Main Campus). Available to start May/June 2027 per program dates. Returning to the University of Michigan after the internship (Expected May 2028). I will arrange housing; I do not need company relocation or visa help.

---

## Notes for the applicant (not for submission)

- **Do not claim Ruby, Elixir, MSSQL, Splunk, Sidekiq, Kubernetes, or a healthcare/prior-auth internship.** Prior-year CMM developer intern postings listed some of those; this JD does not require them. Honest Python + SQL + JS-family + Docker/Postgres/Redis beats a knockout lie.
- **Do not write a cover letter that sounds like an ML or audio intern.** Lead with MDC (partner API/ETL) and Vylet (automation + SQL). Granular is C++ discipline if they ask about multi-stack — not the opener. The shipped resume still has Granular at the bottom; if asked, it is lock-free/real-time constraints, not a music-hobby pitch and not healthcare.
- **Columbus is not a skip.** Say yes. No company housing — budget for 10 weeks in Columbus.
- **Pay is $16.50–$27.50/hr.** Accept the posted range on the form. Prestige is C-tier healthcare SaaS (`companies.md`); the resume screen is the gate (~15–25%).
- **Catch-all posting:** team match is after the screen. Apply before 17 Aug 2026.
- **Referral:** no McKesson/CoverMyMeds contact in `network.md`. A UMich alum at CMM still beats a cold Workday pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
