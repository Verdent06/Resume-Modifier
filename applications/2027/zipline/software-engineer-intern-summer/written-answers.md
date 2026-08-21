# Zipline — Software Engineer Intern (Summer 2027) · Written Application Answers

Draft answers for Greenhouse embed token `7929236003`. Grounded in `persona.md` (full-stack spine + autonomy / autonomous logistics differentiator), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Snowflake, Databricks, Copilot, Fusion, Tableau, Go, React Native, ROS/ROS2, Java, internships at Zipline, drone/perception work, or Granular callback-latency / xrun / CPU numbers.

Apply: https://boards.greenhouse.io/embed/job_app?token=7929236003
Resume: `applications/2027/zipline/software-engineer-intern-summer/Vedant Desai Resume.pdf`

**Pulled from the posting:** Zipline · Software Engineer Intern (Summer 2027) · South San Francisco, California, USA · full-time onsite May/June–August/September · $50/hr.

This is **Summer 2027**, not Spring 2027.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact labels on the Greenhouse embed (token 7929236003). `*` = required on the form.

| Field | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | vedantde@umich.edu |
| Country * | United States |
| Phone * | (248) 704-4852 |
| Location (City) * | Ann Arbor, MI |
| Resume/CV * | `applications/2027/zipline/software-engineer-intern-summer/Vedant Desai Resume.pdf` |
| Cover Letter | Optional. Paste the letter below if attaching / entering manually. |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| GitHub (not a form field — use in cover letter / if asked) | https://github.com/Verdent06 |
| School / degree (if a recruiter asks; not on this embed) | University of Michigan · B.S. Computer Science and Economics · GPA 3.66 / 4.0 · Expected May 2028 |
| Tell us how you heard about Zipline and this job! * | **Other Job Board** (Jobright is not a listed option). If that is how you found it: **Other** → Jobright. Do not pick University Careers Fair Event unless that is true. Listed options: Google Search · Word of Mouth or Referrals · LinkedIn · SkillBridge · Glassdoor · Indeed · Handshake · BuiltIn · Social Media · YouTube or News · Partner Organization · Zipline Investors · University Careers Fair Event · Event at Zipline · Other Job Board · Other |
| Are you available for a full-time onsite internship this summer (May/June - August/September)? * | **Yes** |
| Why are you interested in becoming a Software Engineer Intern at Zipline? * | Paste the short answer below (not the full cover letter). |
| Please provide details on your current work authorization status in the United States * | **I am legally authorized to work for any employer in the United States.** (US citizen; **no** sponsorship now or later.) Do **not** select "I require, or in the future will require sponsorship…" or "I am not currently authorized to work in the United States." |
| Voluntary Self-Identification - Disability | Skip unless you want to answer. Options: Yes, I have a disability, or have had one in the past · No, I do not have a disability, and have not had one in the past · I do not want to answer |
| Voluntary Self-Identification - Veteran | Skip unless you want to answer. Options: I am not a protected veteran · I identify as one or more of the classifications of a protected veteran · I don't wish to answer |
| U.S. Standard Demographic Questions (gender, race/ethnicity, sexual orientation, transgender, disability, veteran) | All optional. Skip for volume (`recruiting.md` Part I §2). |

---

## Cover letter (paste)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

Zipline — Software Engineer Intern (Summer 2027)
South San Francisco, CA (onsite)

Dear Zipline recruiting team,

I am applying for the Summer 2027 Software Engineer Intern role in South San Francisco. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work full-time onsite May/June–August/September, I return to Michigan afterward, and I am a U.S. citizen who does not need sponsorship.

Zipline's intern job is consumer mobile and web features owned from design through deployment — React Native or Python/Go backends — at a company whose product is autonomous logistics, not a generic CRUD internship. I have not shipped React Native or Go. I have shipped user-facing product software, Python services, and C++ that cannot miss a real-time deadline.

What I would bring:

- **User-facing product, owned end to end.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS that regenerates expired S3 presigned URLs mid-flight, moved audio off the UI thread into a Web Worker (main-thread blocking under 5ms at 60 FPS), and cut cloud inference cost 40% by running Silero VAD client-side via ONNX Runtime so dead air never hit Whisper.
- **Python backends you can deploy.** As the only engineer on a five-month Michigan Campaign Finance Network contract I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees and delivered a production Flask REST API on AWS EC2. At Vylet (live product, $1,500 MRR) I Dockerized a LangGraph pipeline on Redis/Celery and fixed a name-collision defect that lifted lead-qualification from 79% to 89%. SignalWeaver is the React/TypeScript + FastAPI pair: a dashboard over async REST endpoints instrumented at 9.1s p50 / 15.2s p99.
- **Systems under a hard constraint.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit. github.com/Verdent06/granular-synth

I interview in Python, TypeScript, and C++. I want the South San Francisco intern seat writing features users touch on a logistics system that already flies, and I will ramp on React Native / Go rather than claim them.

Sincerely,
Vedant Desai

---

## "Why are you interested in becoming a Software Engineer Intern at Zipline?" * (textarea)

I want to own user-facing features on a product people actually use — Zipline's consumer mobile/web apps, from design through deploy — at a company whose system is already flying autonomous deliveries, not a toy logistics demo. Closest analog I have: CaseStudyPrep (27% upload-failure recovery, on-device VAD, sub-5ms UI-thread offload) plus Python services I shipped myself (MDC Flask/EC2 to a nonprofit; Vylet Docker/Redis/Celery with a 79%→89% qualification fix). I do not have React Native or Go. I have React/TypeScript (SignalWeaver) and Python backends, and C++ that cannot allocate on the audio thread (granular-synth). I can be in South San Francisco full-time May/June–August/September; UMich CS + Economics, Expected May 2028, GPA 3.66; U.S. citizen, no sponsorship.

---

## Notes for the applicant (not for submission)

- **Do not claim Go or React Native.** The JD names both; they are not in inventory. Honest mapping: Python backends + React/TypeScript web. `persona.md`: Go is not a binary knockout if the product-engineering spine is strong.
- **Do not claim drone, ROS, perception, or fleet-ops internships.** Differentiator on the page is real-time / safety-boundary C++ (Granular), not robotics research.
- **Granular has no runtime metric on the page.** If asked, say so — walk MemoryPool, lock-free SPSC, and the processBlock audit. Do not invent xrun/CPU numbers.
- **MDC Flask/EC2 has no traffic/latency number.** Point to 400 PACs / ~800 hours on the ETL bullet and sole-engineer delivery.
- **Behavioral:** CaseStudyPrep 27% upload recovery = own-the-failure. Vylet 79%→89% = diagnose/fix in production. MDC = stakeholder scoping with no backend team.
- **Funnel:** Greenhouse human screen → recruiter → resume deep-dive → take-home → project presentation. No standard LC OA. Prep the take-home and a Granular + MDC/CSP walkthrough; DS&A still shows in the tech screen.
- **Do not apply twice** against the Spring 2027 Zipline SWE intern. This packet is Summer 2027 only.
