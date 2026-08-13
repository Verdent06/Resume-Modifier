# Samsara — Software Engineering Internship (San Francisco, Summer 2027) · Written Application Answers

Draft answers for Greenhouse `gh_jid=8082091`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented projects, metrics, or stack. Trim to the form's length limit before submitting.

Cover letter is **optional** on this Greenhouse form. The required "Why Samsara" bullets below cover that ground — do not upload a separate cover letter unless the form feels empty without one.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Preferred first / last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/samsara/software-engineering-intern/Vedant Desai Resume.pdf` |
| Cover letter | Skip (optional) |
| Will you now or in the future require Samsara to sponsor an immigration case? | **No** |
| Currently legally authorized to work in the country in which this job is based? | **Yes** |
| Previously worked at Samsara? | **No** |
| How did you hear about this opportunity? | Jobright is not a listed option. Closest listed aggregator: **LinkedIn Jobs** (or Indeed / Glassdoor if that is how Jobright routed you). Do not pick University / Campus Recruiting. |
| Zip code of primary residence | **Fill from your actual address** — context only has Ann Arbor, MI / 248 area code. Do not guess a zip. |
| Able and willing to work out of the San Francisco office? | **Yes** (hybrid 3 days/week; relocation assistance is available; next-summer travel is OK) |
| When will you be graduating? | **2028** |
| Majoring in STEM (CS, EE, Data Science, …)? | **Yes** (B.S. Computer Science and Economics, University of Michigan) |
| Would this be your first internship in an Engineering role? | **No** — CaseStudyPrep.AI Software Engineer Co-op (Voice AI), Dec 2025 – May 2026 |
| Current Employer (if applicable) | Vylet |
| Applying to intern in Winter 2027 or Summer 2027? | **Summer 2027** |
| Do you accept the listed salary range for this position? | **Yes** ($61.90/hr) |
| Where have you learned about Samsara? | Select **Other**; in the follow-up write **Jobright** (listing https://jobright.ai/jobs/info/6a70bcdbe2b7476e7b20a819). Add LinkedIn if true. |
| AI Policy for Interviewers (no AI tools during the interview process) | **Yes** (read and agree) |
| Processing of Personal Data | Acknowledge/Confirm |

---

## "Tell us about a project you built or led on your own initiative - something outside of required schoolwork or an internship. This could be a startup, an open-source project, an app you shipped, or a research idea you pursued independently. What problem were you solving, and what was your role in building it?"

*(Optional on the form. Submit it — it is the strongest "curious / self-driven / own it end to end" signal they ask for.)*

I founded Vylet (vyletdata.com), a live lead-sourcing product for PE/search-fund acquisition prospecting. I am the sole engineer. The problem: a principal was spending ~30 minutes per business on manual research. I turned that into a Dockerized pipeline with Redis/Celery workers that generates 30 scored leads in 30 minutes — a 30x speedup — on a recurring cycle.

Two pieces of the systems work I would walk you through:

- **Data layer, not just the agent.** I wrote a custom asyncpg data-access layer that stores embeddings alongside source records, plus injection-safe SQL timestamp validation that detects stale rows and triggers automatic re-scrapes so the lead database stays fresh without a human in the loop.
- **A real production defect.** Ownership-verification was rejecting valid targets that shared a name with an unrelated business elsewhere. I diagnosed the name-collision, shipped the fix, and the pipeline's lead-qualification rate went from 79% to 89% with no change in sourcing volume.

It is a live product with three paying clients and $1,500 MRR. Separately, for a from-scratch systems project, I also built a real-time granular synthesizer in C++/JUCE (lock-free SPSC FIFO from the UI thread into the audio callback, VST3/AU binaries): github.com/Verdent06/granular-synth.

---

## "Why are you interested specifically in Software Engineering at Samsara? Give us a few bullets."

*(Required.)*

- **Build for scale, on real operations data.** I want to work on the ingestion/storage side of a platform that already runs on 15,000+ hardware asset types and tens of thousands of customers — not a toy pipeline. The closest work I have is sole-engineer delivery of a production Flask REST API on AWS EC2 plus a Requests/Pandas ETL that replaced ~800 hours of manual pulls across 400 tracked PACs (Michigan Data Consulting → Michigan Campaign Finance Network), and Vylet's Docker/Redis/Celery pipeline with an asyncpg data layer.
- **Full-stack that turns data into something a human can act on.** Samsara's web client is TypeScript/React (exact stack not required; similar tech encouraged). I have a React/TypeScript dashboard in SignalWeaver on top of Postgres/pgvector (49ms p50 / 99ms p99 semantic search) and production UI performance work in Angular/RxJS — including moving audio off the main thread to keep a visualizer at 60 FPS with <5ms blocking.
- **The hardware/edge side is a real draw, not a footnote.** Interns can land on embedded software (multimedia, power, real-time processing on device). I have already lived a hard real-time constraint: a C++/JUCE audio plugin whose `processBlock()` path cannot allocate or take a mutex, with UI→audio delivery through a hand-rolled SPSC FIFO.
- **Customers are not abstract.** Samsara engineers visit customers. The only titled work I have that looks like that is scoping ingestion → REST endpoints directly with MCFN as the sole engineer on a 5-month contract — no backend team to hide behind.
- **Fit on the gates you actually listed.** Junior, CS + Economics, Expected May 2028; I can be in the San Francisco office 3 days/week next summer; I do not need immigration sponsorship.

---

## "What's a Samsara product or feature you find interesting, and why? Separately, which of our operating principles resonates most with how you like to work?"

*(Optional. Submit it.)*

**Product.** Video-Based Safety, because it is the place the cloud platform and the hardware actually meet: cameras on vehicles, multimedia and (increasingly) edge inference, then a web/mobile client that has to turn that stream into an action a safety manager will take. I have not shipped telematics — I would not pretend to — but the shape of the problem matches work I *have* done: on-device Silero VAD via ONNX Runtime to drop silent audio before it hit cloud Whisper (40% inference-cost cut), and a C++ real-time multimedia engine that cannot miss its callback deadline. If I landed on backend ingestion or the React/TypeScript client instead, that is still the same product: get the bytes in, make them trustworthy, show the operator something they can act on.

**Operating principle.** Sample the customer experience. I do not want to build a pipeline that is "correct" on a laptop and unused in the field. At MCFN I sat with the researchers who were still doing portal searches and hand-normalizing Excel, and I scoped the ETL + REST API around that workflow because there was no one else to own it. Same instinct as Samsara engineers visiting a yard instead of guessing from dashboards.

---

## Notes for the applicant (not for submission)

- **Do not claim Go, GraphQL, or React Native.** They are not in the inventory. The JD says similar tech is enough — defend Python/Flask + TypeScript/React + C++ real-time as the similar-tech proof.
- **Do not inflate Vylet into IoT scale.** 30 leads / 30 minutes and 90 pgvector queries are student-scale. If asked about Samsara's 15,000 hardware assets, be explicit that you have not operated at that volume and talk about how you would reason about backpressure, partitioning, and failure.
- **Behavioral:** MDC/MCFN stakeholder scoping is the customer-obsession story. CaseStudyPrep's 27% upload-failure recovery is the "own the hard problem end to end" story. Granular's zero-allocation audio thread is the systems/embedded story.
- **OA:** CoderPad/Codility, 4–5 timed easy–medium DSA, arrays/grids/matrices; everyone gets it; a high score alone does not advance you.
