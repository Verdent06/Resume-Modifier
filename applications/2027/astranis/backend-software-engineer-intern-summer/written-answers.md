# Astranis — Software Engineer Backend Intern (Summer 2027) · Written Application Answers

Draft answers for Greenhouse job **4705214006** / req **1062**. Grounded in `persona.md` (full-stack spine + aerospace / GEO-satellite / mission-critical / fleet-ops differentiator), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Kubernetes, RabbitMQ, Flink, ROS, satellite/flight internships, fleet-management titles, clearance-in-hand, Granular xrun/latency/CPU numbers, MDC API traffic/latency.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Apply: https://job-boards.greenhouse.io/astranis/jobs/4705214006
Resume: `applications/2027/astranis/backend-software-engineer-intern-summer/Vedant Desai Resume.pdf`
SHA-256: `3791449649f60e8b7d5832fc808925eae4f383c0a7f42f6a6ec1dfcfb220494e`

**Pulled from the live Greenhouse questions API** (`boards-api.greenhouse.io/v1/boards/astranis/jobs/4705214006?questions=true`) on 2026-09-23. Labels below are exact. `*` = required. Hidden `longitude` / `latitude` are filled by the Location picker — do not type them.

**Form / PDF email MUST be `verdent06@gmail.com`.** Never `vedantde@umich.edu`. Autofill may still pull umich from a prior Greenhouse profile; overwrite.

This is **Summer 2027** only. **Not** the Flight Software intern. **Not** Associate Engineer (that is for people who already graduated).

---

## Knockouts (read first)

1. Currently pursuing B.S./M.S. CS — **clears** (UMich CS + Economics, Expected May 2028).
2. Export control — **I am a U.S. Citizen.** (`context.md`). LPR/refugee/asylee also qualify; **None of the above** is auto-reject.
3. Season — **Summer 2027** (only option).
4. 12-week intern, onsite SF HQ **5 days/week**, **55 hours/week** — **Yes** if you actually mean it. This is a real knockout, not a vibe question. $29/hr.
5. Returning to school after the term — Expected May 2028; Fall 2027 / Winter 2028 remain.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on citizenship, hours, or onsite.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact labels on the live Greenhouse apply form for job **4705214006**.

| Field | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Preferred First Name | Vedant |
| Email * | **verdent06@gmail.com** (never `vedantde@umich.edu`). PDF header matches. Overwrite Autofill if it inserts umich. |
| Phone * | (248) 704-4852 |
| Resume/CV | `applications/2027/astranis/backend-software-engineer-intern-summer/Vedant Desai Resume.pdf` — attach the PDF. Form marks resume optional; still attach. |
| Cover Letter | Optional. Leave blank **or** paste the short letter below. PDF is the screen (`companies.md`: bottleneck resume then tech). |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 |
| Location * | Ann Arbor, MI (school city on the resume). Relocate to San Francisco for the term: **Yes**. Mailing address if asked: 49032 Freestone Dr, Northville, MI 48168. |
| Astranis complies with U.S. Government space technology export regulations, therefore will you state which of the following applies to you: * | **I am a U.S. Citizen.** Do **not** pick LPR / refugee / asylee unless that is actually true. Do **not** pick **None of the above**. Do not claim a clearance. |
| What is the most impressive thing you have ever accomplished? * | Paste the textarea below. |
| Please confirm the season you are applying for. * | **Summer 2027** (only listed value). |
| When are you able to join Astranis as an intern? (12 week minimum) * | **May 17, 2027** (Monday; can shift ±1 week to match the intern cohort). UMich winter term is over by then. |
| When do you plan on ending your internship? * | **August 6, 2027** (Friday — 12 weeks from May 17). If the cohort runs a week later: August 13, 2027. Returning to Michigan for Fall 2027 (Expected May 2028). |
| At Astranis, we value in-person collaboration and a strong work ethic. Are you comfortable with working onsite at our San Francisco HQ 5 days a week and commit to 55 hours per week? * | **Yes** |
| How did you hear about Astranis? * | Greenhouse job board (https://job-boards.greenhouse.io/astranis/jobs/4705214006). Do **not** invent a referral — none in `network.md`. If a real Astranis name appears later, use that instead. |
| By selecting YES, I consent to receive recruiting SMS messages from Astranis at the phone number provided on my job application. * | **Yes** (required field; recruiting SMS only). |
| School / degree / GPA (not on this form; on the PDF) | University of Michigan · B.S. Computer Science and Economics · GPA **3.66 / 4.0** · Expected **May 2028** · Junior |
| Languages you can interview in | **Python, C++, TypeScript/JavaScript (Angular), SQL**. Do **not** check Go, Rust, Java, Kubernetes, RabbitMQ, or Flink. |
| Voluntary Self-Identification (Gender, Race, Veteran) | Optional. Skip / **Decline To Self Identify** / **I don't wish to answer** for volume (`recruiting.md` Part I §2). |

Greenhouse AI Talent Matching disclaimer is on the posting. Opt-out URL exists (`/ai_opt_out_request/job_post/4705214006/ai_opt_out`). Do not treat opt-out as required.

---

## "What is the most impressive thing you have ever accomplished?" * (textarea)

One accomplishment. Metrics below are from `context.md` — no Granular latency/xrun/CPU number exists, so none is claimed.

The hardest engineering constraint I have actually enforced is a C++ audio callback that is not allowed to allocate or take a lock. I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot call `new`/`delete` or acquire a mutex after `prepareToPlay()` — a missed deadline is a glitch, not a retry. I pre-allocated a `MemoryPool<Grain, 64>` slab per voice at startup so grain slots come off a free-list, and a 64-slot lock-free SPSC FIFO with atomic acquire/release so UI slider changes never block the audio thread; WAV handoff uses an atomic `shared_ptr` swap. I shipped VST3 and AU from one CMake codebase (macOS universal, arm64 + x86_64) after auditing every `processBlock()` path for zero heap allocations and zero lock acquisitions. github.com/Verdent06/granular-synth

That is DSP, not satellites. I do not have a space internship. The transferable piece is software that has to hit a deadline on a shared-memory path, which is why I am applying to Platform backend (command/telemetry services), not inventing Flight Software experience. Closest production backend I have shipped: a Flask REST API on AWS EC2 as the only engineer on a five-month Michigan Campaign Finance Network contract, plus Redis/Celery workers on a live product (Vylet) and FastAPI + PostgreSQL/pgvector (SignalWeaver, 49ms p50 semantic search). I interview in Python and C++.

---

## Cover letter (optional — paste only if attaching)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Astranis — Software Engineer Backend Intern (Summer 2027)
San Francisco, CA (onsite)

Dear Astranis recruiting team,

I am applying for the Summer 2027 Software Engineer Backend Intern role on the Platform team. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work onsite at the San Francisco HQ five days a week for 12 weeks starting May 17, 2027 (through August 6), including the 55-hour week the form asks about. I return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

This intern job is backend and infrastructure that commands satellites, watches telemetry, and has to work — not a generic CRUD rotation and not the Flight Software intern. I have not shipped Kubernetes, RabbitMQ, or Flink. I have shipped Python services, Postgres, and queue workers, plus C++ that cannot miss a real-time deadline.

What I would bring:

- **Python backends other people use.** As the only engineer on a five-month Michigan Campaign Finance Network contract I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees and delivered a production Flask REST API on AWS EC2. SignalWeaver serves async FastAPI endpoints (9.1s p50 / 15.2s p99 across 90 tickers) and PostgreSQL/pgvector semantic search at 49ms p50 / 99ms p99.
- **Queues / workers, not invented pub/sub brands.** At Vylet (live product, $1,500 MRR) I Dockerized a LangGraph pipeline on Redis/Celery workers and wrote a pure-Python consensus gate (no LLM calls) that hard-fails bad leads before the score threshold. Redis/Celery is the honest analog; I will not write RabbitMQ or Flink on the form.
- **Systems under a hard constraint.** Granular synthesizer in C++/JUCE: `processBlock()` cannot allocate or take a lock. Per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO. VST3/AU after a real-time safety audit. github.com/Verdent06/granular-synth. At CaseStudyPrep.AI I closed a 27% audio-upload failure rate (expired S3 URLs + MIME mismatch) and held main-thread blocking under 5ms at 60 FPS.

I interview in Python and C++. I want the SF Platform intern seat writing services operators and satellites depend on.

Sincerely,
Vedant Desai

---

## Availability

Summer 2027, paid, **onsite San Francisco HQ**, 12 weeks, **5 days/week, 55 hours/week**. Start **May 17, 2027**. End **August 6, 2027**. Returning to the University of Michigan (Expected May 2028). GPA 3.66. US citizen; no sponsorship. Comp: accept posted **$29.00/hr**.

---

## Notes for the applicant (not for submission)

- **Do not claim Kubernetes, RabbitMQ, Flink, ROS, a satellite internship, fleet-ops title, or clearance.** JD names RabbitMQ/Flink as pub/sub examples and K8s as bonus; inventory does not have them (`grade.md` Defend). Honest mapping: Redis/Celery workers + FastAPI/Flask + PostgreSQL/pgvector.
- **Do not invent a Granular runtime metric.** Pool has no xrun / callback-latency / CPU / user count. Walk MemoryPool, lock-free SPSC, and the `processBlock` audit.
- **Vylet still reads as PE/LangGraph on the PDF.** If asked, pivot to Redis/Celery and the pure-Python gate — not the GTM story (`grade.md` Defend).
- **55 hours / 5-day SF is a form knockout.** $29/hr is below SpaceX/Apex intern bands in `companies.md`. Only submit if you will actually do that week.
- **Cover letter is optional.** Attach it if you want; the PDF is the screen. Binding filters after that: unpublished Coderbyte/live coding **[directional, FSW 2024 sibling]** then tech/loop (`companies.md`: bottleneck resume then tech, ~5–8%).
- **Referral:** none in `network.md`. A real Astranis name beats Greenhouse; a fake name is a knockout.
- **Email is `verdent06@gmail.com` on the PDF and every Greenhouse field.** Never `vedantde@umich.edu`.
