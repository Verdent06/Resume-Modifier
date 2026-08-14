# Castleton Commodities International — Full-Stack Software Engineer Internship (Summer 2027) · Written Application Answers

Draft answers for Workday req **R1350** (Stamford, CT, onsite). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Streamlit, Snowflake, Kubernetes, Kafka, Helm, energy-desk internships, or metrics not in the pool.**

The Workday apply questionnaire could not be scraped from the public posting. Fill knockouts exactly. Paste the cover letter / "why CCI" text only if the form has a matching field or an upload slot. Trim to the form's character limit before submitting.

Apply: https://osv-cci.wd1.myworkdayjobs.com/ccicareers/job/Stamford-CT/Full-Stack-Software-Engineer-Internship--Summer-2027-_R1350

Deadline: **September 1 at 11:59 pm EST**

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/castleton-commodities/full-stack-software-engineer-intern/Vedant Desai Resume.pdf` |
| Location | **Stamford, CT** — onsite for Summer 2027 |
| Willing to relocate / work onsite | **Yes** |
| Currently pursuing Bachelor's or Master's in CS / Engineering / MIS / related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Expected graduation | **May 2028** (Spring 2028 — inside Winter 2027 or Spring/Summer 2028) |
| Will you return to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** (only if asked) |
| Work authorized in the US? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** — US citizen, no sponsorship needed |
| How did you hear about this role? | **Jobright** (https://jobright.ai/jobs/info/6a5ff769f68dd368023e9e2d). If Jobright is not listed: **Other** → Jobright |
| Cover letter | Optional on many Workday flows — upload the letter below if there is a slot; do not skip a required essay |

---

## Cover letter (upload if the form allows)

I am applying for the Full-Stack Software Engineer Internship (Summer 2027) on Castleton Commodities International's Global Data Science & Technology team in Stamford.

I want to spend the summer writing Python tools that traders and analysts actually run — APIs, data pipelines, and dashboards — not a generic intern rotation. CCI's DS&T intern track is that job: front-office software for real-time trading, market-data analytics, and visualization, sitting next to commercial users.

What I can defend on a screen:

- **Python services and data pipelines.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2. On SignalWeaver I served composite financial-research scores through async FastAPI endpoints (9.1s p50 / 15.2s p99 across 90 tickers) and a React dashboard, containerized with Docker Compose and GitHub Actions CI.
- **Tools commercial users pay for or depend on.** Vylet is a live lead-sourcing product at $1,500 MRR across three clients. I engineered a pure-Python consensus gate (no LLM calls) that scores leads 0–100 from registry, crawl, and query agreement, then hard-fails on legal status, industry, geography, or independence. That is scoring and workflow software, not a notebook.
- **Markets curiosity I will not fake as desk experience.** I am a CS and Economics major. I have built financial-research scoring (SignalWeaver) and acquisition-intelligence pipelines (Lyndbrook). I have not interned on an energy trading floor. I want to learn how CCI's physical and financial commodity markets show up in the tools DS&T ships.

I can be onsite in Stamford for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Why CCI / why this internship?" (if a short essay)

I want to build the software layer that sits next to a trading desk. CCI is an energy merchant whose DS&T team ships Python services, APIs, and analytics into commercial workflows — that is the intern seat I am aiming at, not the ML or GenAI sibling tracks.

The work I already do looks like that job: Pandas ETL and a Flask API on EC2 for a real research client; FastAPI + a React dashboard + Docker/CI for financial-research scores; a live Python product with paying users and a deterministic scoring gate. I am a CS and Economics student. I have not worked in power, gas, or oil markets. I want the summer to put those engineering habits next to CCI's commercial team.

---

## "Tell us about a project" / additional information

**MDC (production API + ETL).** Requests + Pandas ingestion of Michigan campaign-finance filings; Flask REST API on AWS EC2; sole engineer on a 5-month MCFN contract; ~800 hours of manual pulls removed across 400 PACs.

**SignalWeaver (dashboard + API + CI).** FastAPI scores, React/TypeScript dashboard, Postgres history, Docker Compose, GitHub Actions (frontend build, pytest, API image). I have not used Streamlit; this is the visualization and microservice evidence I can walk through.

**Vylet (live product).** Pure-Python consensus scoring; qualification rate 79% → 89% after a name-collision fix; $1,500 MRR, three clients.

---

## Availability

Summer 2027, onsite Stamford, CT. Available to start May 2027. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Do not claim Streamlit, Snowflake, Kubernetes, Kafka, or Helm.** Preferred on the JD; not in your pool. Honest React dashboard + Docker Compose + AWS EC2 beats a keyword lie.
- **Do not apply as the ML or GenAI DS&T intern.** This req is Software Engineering — Python front-office tools. SignalWeaver's LoRA work stays off this resume for that reason.
- **No CCI contact in `network.md`.** A UMich alum on DS&T still beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply). Campus recruiting email if the form breaks: CampusRecruiting@cci.com.
- **Deadline is September 1, 11:59 pm EST.** Apply inside the campus window.
