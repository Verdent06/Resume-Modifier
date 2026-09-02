# Remarcable — Full Stack Developer (Student Co-op) · Written Application Answers

Drafts for the live Ashby apply page. Grounded in `persona.md`, `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Django, Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Java/Spring, a Canadian work permit, Vancouver residency, Fall 2026 availability, or AngularJS 1.x (inventory is Angular on CaseStudyPrep.AI).

Apply: https://jobs.ashbyhq.com/remarcable-inc/a4f3aaaa-9469-42e8-a610-450d25eb5da7/application
Resume: `applications/2027/remarcable/fullstack-coop-winter/Vedant Desai Resume.pdf`

**Pulled from the posting (2026-09-02):** Remarcable, Inc. · Full Stack Developer (Student Co-op) · Vancouver, BC · onsite 333 Seymour Street · 8:00am–5:00pm · Intern / Full Time Temporary · January 2027 start · 4–12 month terms · CA$23–CA$26/hr · deadline 15 October 2026.

This is **Winter 2027** (January start), not Fall 2026.

---

## Knockout / structured fields

Questions below are the exact labels on the Ashby application. `*` = required on the form.

| Field | Answer |
| --- | --- |
| Name * | Vedant Desai |
| Email * | verdent06@gmail.com |
| Phone * | (248) 704-4852 |
| Resume * | `applications/2027/remarcable/fullstack-coop-winter/Vedant Desai Resume.pdf` |
| Cover Letter | Optional. Paste the letter below if attaching. |
| Tell us about a project where you used Python. What part did you personally build or solve? * | Paste the Python answer below. |
| Describe a time you worked with a REST API (building or consuming). What did you do and what tools did you use? * | Paste the REST answer below. |
| Have you worked with any frontend frameworks (AngularJS, React, Vue, etc.)? If yes, what did you build? If no, how would you approach learning one? * | Paste the frontend answer below. |
| Location * — Where do you currently reside? | Ann Arbor, MI, United States. Do **not** invent Vancouver. |
| Are you legally authorized to work in the Canada? * | **GATE — see below. Do not click Yes unless you already hold a Canadian work permit.** US citizen; no CA permit is on file. Honest answer from `context.md` is **No**. |
| Are you willing and able to commute to our office in Downtown Vancouver? * | Only **Yes** if you will relocate to Vancouver for January 2027 onsite (333 Seymour). Current residence is Ann Arbor. Do not invent a Vancouver address. |
| Highest level of education * | **Pursuing Bachelors** — University of Michigan, B.S. Computer Science and Economics, Expected May 2028, GPA 3.66. Junior during Winter 2027. Not New Grad. |

---

## Canadian work-permit gate (read before submit)

Ashby required Yes/No: **"Are you legally authorized to work in the Canada?"**

`recruiting.md` Part I §1: work-authorization knockouts are auto-reject and absolute. US citizenship is **not** Canadian work authorization. `context.md` documents US citizen / no US sponsorship and does **not** document a Canadian work permit, IEC, or co-op work permit.

- Honest answer from files on disk: **No**.
- Clicking **Yes** without a permit is a fabrication. Do not do that.
- A **No** will likely knock this application out at the form (`companies.md` bottleneck: CA work-permit knockout + resume).
- If you later obtain a real permit (university-facilitated co-op work permit, IEC, etc.), update the answer then — do not invent one now.

Onsite commute question is a second location gate: Downtown Vancouver, 8:00am–5:00pm, 333 Seymour Street.

---

## Cover letter (optional)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Remarcable — Full Stack Developer (Student Co-op)
Vancouver, BC (onsite, January 2027)

Dear Remarcable recruiting team,

I am applying for the Winter 2027 Full Stack Developer Student Co-op in Vancouver. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am available January 2027 for a 4–12 month co-op. I am a U.S. citizen. I do not currently hold Canadian work authorization.

Your intern job is Python + REST + SQL + a real web surface on a procurement marketplace, with Django and AngularJS as the house stack and "not expected to know all of this on day one." I have not shipped Django or AngularJS 1.x. I have shipped Python REST APIs, Angular and React frontends, PostgreSQL, Docker, and AWS.

What I would bring:

- **Python backends that shipped to users.** As the only engineer on a five-month Michigan Campaign Finance Network contract I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees and delivered a production Flask REST API on AWS EC2. At Vylet (live product, $1,500 MRR) I Dockerized a LangGraph pipeline on Redis/Celery and built an asyncpg layer with injection-safe SQL freshness checks.
- **Frontend that had to work.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS that regenerates expired S3 presigned URLs mid-flight after Angular rejected WAV MIME types, and cut cloud inference cost 40% by running Silero VAD client-side via ONNX Runtime. SignalWeaver is the React/TypeScript + FastAPI pair: async REST at 9.1s p50 / 15.2s p99 with scores persisted to Postgres.
- **Honest stack gap.** I interview in Python, TypeScript, and SQL. I will ramp on Django and AngularJS rather than claim them.

Sincerely,
Vedant Desai

---

## "Tell us about a project where you used Python. What part did you personally build or solve?" *

At Michigan Data Consulting I was the only engineer on a five-month contract with the Michigan Campaign Finance Network. Researchers were doing portal searches capped by the Bureau of Elections, irregular Excel exports, and hand-normalization at about two hours per committee. I wrote a Python Requests + Pandas ETL that ingested filings directly, which eliminated about 800 hours of manual pulls across 400 tracked PACs, then shipped a production Flask REST API on AWS EC2 that wired the ingested data and PAC rankings into their public research workflow. I do not have Django. Flask is the Python web stack I actually shipped.

---

## "Describe a time you worked with a REST API (building or consuming). What did you do and what tools did you use?" *

I built the MCFN Flask REST API above (Python, Flask, AWS EC2) so the nonprofit could consume PAC rankings instead of rebuilding spreadsheets. Separately, SignalWeaver serves composite research scores through async FastAPI REST endpoints wrapping fundamentals, MPNet sentiment, and regression logic — instrumented at 9.1s p50 / 15.2s p99 across 90 successful runs on 90 tickers, with history persisted to Postgres. On the consume side, CaseStudyPrep.AI talks to S3 via presigned URLs: RxJS detects expiry mid-flight, regenerates the URL, and negotiates MIME types for WAV files Angular had been silently rejecting, which cut a 27% upload failure rate.

---

## "Have you worked with any frontend frameworks (AngularJS, React, Vue, etc.)? If yes, what did you build? If no, how would you approach learning one?" *

Yes. I have not shipped AngularJS 1.x. I have shipped Angular (CaseStudyPrep.AI) and React/TypeScript (SignalWeaver). At CaseStudyPrep I owned the client-side audio path: Silero VAD via ONNX Runtime to drop dead air before Whisper (40% inference-cost cut), a Web Worker so the visualizer stayed at 60 FPS with main-thread blocking under 5ms, and the RxJS/S3-presign repair after Angular rejected WAV MIME types. SignalWeaver is a React/TypeScript dashboard over FastAPI REST with scores stored in Postgres. I would learn Remarcable's AngularJS the same way I learned those frontends: clone a thin vertical slice, match existing patterns in code review, and ship a small user-facing fix first.

---

## Notes for the applicant (not for submission)

- **Email on this packet is verdent06@gmail.com.** Do not paste vedantde@umich.edu.
- **Do not claim Django.** JD bonus only; inventory is Flask/FastAPI.
- **Do not claim AngularJS.** Inventory is Angular + React.
- **Available Winter 2027 / January 2027**, not Fall 2026. Junior, Expected May 2028, GPA 3.66, US citizen, no US sponsorship.
- **CA work-auth is the binding form gate.** Honest No from current files. A Yes without a permit is a lie.
