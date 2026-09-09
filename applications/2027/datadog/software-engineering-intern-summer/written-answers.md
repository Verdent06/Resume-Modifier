# Datadog — Software Engineering Intern (Summer) · Written Application Answers

Draft answers for Greenhouse job `8052118` (`?questions=true`). Grounded in `persona.md` (full-stack screen + observability / high-scale telemetry differentiator — **not** an ML or Kubernetes-invented page) and `context.md` facts only. No cover letter on this form; do not invent one.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** Resume header email (`vedantde@umich.edu`) stays on the PDF. Phone **(248) 704-4852**. US citizen, no sponsorship. Expected May 2028, GPA **3.66**. LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06.

**Do not invent:** Kubernetes, Go, Java, Snowflake, Databricks, Copilot, Fusion, Tableau.

**Do not submit from this agent.** Paste pack only.

Apply: https://careers.datadoghq.com/detail/8052118/?gh_jid=8052118
Resume: `applications/2027/datadog/software-engineering-intern-summer/Vedant Desai Resume.pdf`

Skip optional EEOC / self-ID.

---

## Knockouts (read first)

1. **2028 FT start.** Expected **May 2028** matches "targeting a 2028 full-time start date." **Clears.**
2. **Class standing at Summer 2027.** Rising junior / after sophomore year; returns to Michigan for 2027–28. **Clears.**
3. **NYC or Boston, hybrid, full-time** on one of the posted windows. Relocate **Yes** to both offices. Prefer **New York**.
4. **Work authorization.** US citizen; legally authorized with no restriction; no sponsorship.

---

## Knockout / structured fields (fill exactly)

| Field (exact label) | Answer |
| --- | --- |
| First Name | Vedant |
| Last Name | Desai |
| Preferred First Name | Vedant |
| Email | **verdent06@gmail.com** |
| Phone | (248) 704-4852 |
| Resume/CV | `applications/2027/datadog/software-engineering-intern-summer/Vedant Desai Resume.pdf` |
| When is your graduation date (actual or expected)? | **Spring 2028** (Expected May 2028; this form treats May as Spring 2028) |
| Will participating in an internship during this period push your expected graduation date back? | **No** |
| Which dates do you prefer to work full-time in the Datadog office? | **May 24, 2027 – August 20, 2027** (shortest listed ~12-week window; typical UM summer) |
| What is your top location preference? | **New York, New York, USA** (HQ) |
| Are you available to relocate to New York for this position? | **Yes** |
| Are you available to relocate to Boston for this position? | **Yes** |
| Are you legally authorised to work full-time in the country where this job is based? | **Yes, no restriction** (U.S. citizen) |
| Which opportunity are you most interested in? | **Distributed Systems** — real-time / reliability / lock-free C++ plus instrumented services; matches Datadog's observability identity without claiming Kubernetes |
| Second choice | **Backend** — production Flask/FastAPI APIs, ETL, AWS EC2 deploy |
| Third choice | **Data Engineering** — Requests/Pandas ingestion, PAC aggregation, Docker/Redis/Celery workers |
| Which scripting / programming languages do you have experience with? | **C++**, **Python**, **SQL PL/SQL**, **Typescript** only. Do **not** check Javascript (inventory lists TypeScript, not Javascript). Do **not** check Go/Golang, Java, C#, Rust, or anything else not in `context.md`. |
| Are you currently in process with other companies that would require us to be time sensitive? | **Yes** — large 2027 apply book already in flight (`TRACKER.md`) |
| When considering an internship at Datadog, what are the most important factors to you? | **Challenging technical work**; **Impact of work**; **Mentorship and support** |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 |
| How did you hear about this opportunity? | **Datadog's Careers Page** |
| If Datadog employee | *(leave blank — no employee referral)* |
| Certify true | **Yes** |
| Privacy policy | **Yes** |

---

## Tell us why you are interested in building an engineering career at Datadog.

I want to spend a career on systems that have to be correct while they ingest and serve data at scale — not a generic CRUD rotation. Datadog is the company that made unified observability (metrics, logs, traces, security) the default way operators see production. The Summer intern req is a general SWE seat (backend, frontend, infra, data, developer tooling), but the work is still "process and analyze massive volumes of metrics, logs, and application data in real time." That is the job I already practice on a smaller surface, and it is the job I want to get better at under mentors who do it at global scale.

What I can defend in a project deep-dive:

- **Real-time and reliability.** At CaseStudyPrep.AI I moved audio processing off the UI thread (Web Worker, under 5ms main-thread block, 60 FPS visualizer) and closed a 27% S3 upload failure rate with fault-tolerant RxJS retries around expired presigned URLs. That is latency and failure recovery, not a Voice-AI product pitch.
- **Shipped data + API.** At Michigan Data Consulting I was the sole engineer on a five-month MCFN contract: a Requests + Pandas ETL that replaced ~2-hour manual committee pulls (~800 hours across 400 PACs) and a production Flask REST API on AWS EC2.
- **Instrumented services.** SignalWeaver serves async FastAPI scores at 9.1s p50 / 15.2s p99 and pgvector search at 49ms p50 / 99ms p99. I want to be in a place that treats p99 as a product question.
- **Hard constraints.** I shipped C++ whose audio thread cannot allocate or take a lock (`MemoryPool<Grain, 64>`, real-time safety audit, VST3/AU binaries). I have not shipped Kubernetes or Datadog's Go agent stack; I will ramp rather than invent it.

I am a U.S. citizen (no sponsorship), Expected May 2028, and I can work the May 24 – August 20, 2027 window full-time from the New York office (Boston is fine if that is the seat). I return to Michigan afterward. I would rather own a scoped production project on a telemetry path — backend or distributed systems — than optimize an intern resume for Bits AI.

---

## Notes for the applicant (not for submission)

- **No cover letter field** on job 8052118. Do not invent one.
- **Email is verdent06@gmail.com** on every form field. The PDF may still show vedantde@umich.edu.
- **Do not check Javascript** unless you decide TypeScript counts; inventory name is TypeScript. Do not check Go/Java/K8s.
- **Team pick:** Distributed Systems → Backend → Data Engineering. Do **not** pick Applied AI as #1 (`persona.md`: AI is a plus, not the lead).
- **Dates:** May 24 – August 20, 2027 unless Michigan's calendar forces the longer May 24 – August 27 window.
- **Referral:** no Datadog contact in `network.md`. Careers Page is the honest source.
- **Do not apply from this file automatically.**
