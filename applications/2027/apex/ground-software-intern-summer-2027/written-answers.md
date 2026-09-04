# Apex — Ground Software Engineering Internship (Summer 2027) · Written Application Answers

Draft answers for Ashby posting `2d5ad921-241f-4e7a-b9ff-9d01763da88c`. Grounded in `persona.md` (full-stack spine + aerospace / satellite-bus / mission-critical spacecraft ops / ground-segment differentiator), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Rust, Vue, C-as-distinct-from-C++, ROS, Octopus OS, satellite/flight internships, firmware/microcontroller work, clearance, Granular xrun/latency/CPU/user numbers, MDC API traffic/latency.

Apply: https://jobs.ashbyhq.com/apex-technology-inc/2d5ad921-241f-4e7a-b9ff-9d01763da88c/application
Resume: `applications/2027/apex/ground-software-intern-summer-2027/Vedant Desai Resume.pdf`
SHA-256: `78e9875f096de3c95024a3c04d437ccaf41d89657d60fb16bf2bddac4f970555`

This is **Summer 2027 only**, not Spring 2027. **Not** the Embedded Systems twin.

Form fields captured from Ashby `applicationForm` GraphQL on 2026-09-04. `*` = required.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| Full Name * | Vedant Desai |
| Preferred First Name | Vedant (optional — leave blank if you prefer) |
| Resume * | `applications/2027/apex/ground-software-intern-summer-2027/Vedant Desai Resume.pdf` |
| Email * | **verdent06@gmail.com**. Resume PDF header still shows `vedantde@umich.edu` (template; writer cannot change it). If Ashby rejects personal mail: `vedantde@umich.edu`. |
| Phone * | (248) 704-4852 |
| Location * | Ann Arbor, MI (school city). Relocate to Los Angeles / Playa Vista for the term: **Yes**. |
| Current Employer | Optional. Leave blank (student). Do not invent a company. If they want a current title: Vylet (founder) is in `context.md`. |
| LinkedIn URL * | https://linkedin.com/in/vedantde06 |
| GitHub URL | https://github.com/Verdent06 |
| You must be a U.S. Person because this position requires access to information that is subject to U.S export controls. Are you a US Person? (Citizen, Green Card holder, etc.) * | **Yes** — US citizen. No sponsorship now or later. Do **not** select No. Do not claim a clearance. |
| Why are you interested in working at Apex? | Optional LongText. Paste the short answer below. |
| Additional Information: Paste your cover letter or anything else you would like to share. | Optional LongText. Paste the cover letter below. State **Summer 2027** here — there is no season dropdown. |
| School / degree / GPA (not on this Ashby form; on the PDF) | University of Michigan · B.S. Computer Science and Economics · GPA **3.66 / 4.0** · Expected **May 2028** · Junior (rising senior after Summer 2027) |
| Internship term (not a form field) | **Summer 2027 only.** Do not volunteer Spring 2027. |
| Willing to relocate to Los Angeles? (not a form field) | **Yes** — onsite Factory One / Playa Vista, 12 weeks. |
| Gender / Race / Veteran / Disability (Ashby EEO surveys) | Optional. Skip for volume (`recruiting.md` Part I §2). |

---

## Why are you interested in working at Apex? (paste)

I want the Ground Software intern seat writing the stack that operates Apex satellites — design, development, and deployment — not a generic CRUD rotation and not the Embedded Systems twin. Apex's productized buses (Aries / Nova / Comet) at Factory One are a manufacturing problem with software in the loop; I want to own tickets and a scoped project on that ground stack in **Summer 2027** (not Spring), onsite in Playa Vista.

Closest analog I have: production software other people depend on, plus C++ that cannot miss a deadline. At CaseStudyPrep I moved audio off the UI thread (main-thread blocking under 5ms at 60 FPS) and closed a 27% S3 upload failure with in-flight URL regeneration. At Michigan Data Consulting I shipped a Flask REST API on AWS EC2 as the only engineer on a five-month contract. SignalWeaver is the React/TypeScript + FastAPI pair. Granular is C++/JUCE `processBlock()` with a `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO — zero heap, zero locks on the audio thread.

I do not have Rust, Vue, or a satellite internship. I have C++ and React in real systems, I can relocate to Los Angeles for the 12-week term, I return to Michigan afterward (Expected May 2028, GPA 3.66), and I am a U.S. citizen who does not need sponsorship.

---

## Additional Information / cover letter (paste)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Apex — Ground Software Engineering Internship (Summer 2027)
Los Angeles / Playa Vista (onsite)

Dear Apex recruiting team,

I am applying for the Ground Software Engineering Internship for **Summer 2027 only** (not Spring). I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can relocate to Los Angeles for the full 12-week onsite term at Factory One, and I return to Michigan afterward. I am a U.S. citizen (U.S. Person) and do not need sponsorship.

This posting is the software that operates Apex satellites — architecture, backend, frontend, deploy — at a company whose product is a satellite bus manufactured at rate, not a consumer web internship and not the Embedded Systems twin. I have not shipped Rust or Vue. I have shipped C++ under a hard real-time constraint, React/TypeScript dashboards, and Python services I deployed myself.

What I would bring:

- **Real-time frontend and operational debug.** At CaseStudyPrep.AI I moved audio processing off the UI thread into a Web Worker (main-thread blocking under 5ms, visualizer at 60 FPS) and closed a 27% audio-upload failure rate with fault-tolerant RxJS that regenerates expired S3 presigned URLs mid-flight.
- **Backend + deploy.** As the only engineer on a five-month Michigan Campaign Finance Network contract I delivered a production Flask REST API on AWS EC2 after replacing ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 committees. At Vylet I Dockerized a LangGraph pipeline on Redis/Celery and fixed a name-collision defect that lifted lead-qualification from 79% to 89%.
- **C++ under a deadline.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit. github.com/Verdent06/granular-synth
- **React on a real API.** SignalWeaver is a React/TypeScript dashboard over async FastAPI REST endpoints (9.1s p50 / 15.2s p99 across 90 tickers). github.com/Verdent06/SignalWeaver

I interview in C++, Python, and TypeScript. I will ramp on Rust/Vue rather than claim them. I want the Playa Vista ground-software seat for Summer 2027.

Sincerely,
Vedant Desai

---

## Notes for the applicant (not for submission)

- **Email:** form uses `verdent06@gmail.com` per this packet. PDF still lists `vedantde@umich.edu`.
- **Do not claim Rust or Vue.** Preferred, not exclusive. Honest mapping: C++ backend-adjacent systems + React/TypeScript frontend + Python deploy.
- **Do not claim Octopus, satellite ops internships, or firmware.** Differentiator on the page is real-time C++ (Granular) and real-time frontend (CaseStudyPrep), not flight software.
- **Granular has no runtime metric.** If asked, walk MemoryPool, lock-free SPSC, and the processBlock audit. Do not invent xrun/CPU numbers (`grade.md` Defend).
- **Vylet reads PE/LangGraph on a skim.** Pivot to Docker/Redis/Celery and 79%→89% if asked (`grade.md`).
- **Behavioral:** CaseStudyPrep 27% upload recovery = own-the-failure. Granular = deadline you cannot miss. MDC = sole-engineer delivery.
- **Funnel:** Ashby human screen → recruiter → HM → unpublished practical/OA → LA onsite. Prep LC-mediums plus a C++ lock-free walkthrough and a React+API+EC2 story. Do not prep as firmware.
- **Do not apply twice** against the Embedded Systems intern posting with this PDF.
