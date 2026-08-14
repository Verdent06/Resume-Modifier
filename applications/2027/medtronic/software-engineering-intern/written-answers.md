# Medtronic — Software Engineering Intern (Summer 2027, Fridley) · Written Application Answers

Draft answers for Workday req `R73630`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented medical-device internships, no invented Java / C# / Swift / firmware. Trim to the form's length limit before submitting.

This posting is a **catch-all**. Recruiting may route you to software development, cloud, quality, DevOps, systems, test, AI/data science, or firmware. Prefer **software / cloud / test / data**. Firmware only if they ask, and then only as C++ real-time constraints from the synth — not embedded medical-device firmware.

Apply: https://medtronic.wd1.myworkdayjobs.com/medtroniccareers/job/Fridley-Minnesota-United-States-of-America/Software-Engineering-Intern---Summer-2027_R73630-1

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/medtronic/software-engineering-intern/Vedant Desai Resume.pdf` |
| Location preference | **Fridley, MN** (this req). Other listed hubs are acceptable if they ask; Fridley is the target. |
| Willing to work onsite / relocate | **Yes** — Fridley, minimum 4 days/week, Summer 2027. Housing/relocation assistance is listed for eligible interns. |
| Currently pursuing Bachelor's or Master's in CS / SWE / CompE / related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (Spring 2028 — inside Winter 2027 / Spring 2028 / Winter 2028 / Spring 2029) |
| Available full-time 40 hrs/week June 1–August 13 (semester)? | **Yes** |
| GPA | **3.66 / 4.0** |
| Work authorization | **U.S. citizen.** Authorized to work in the United States **without visa sponsorship** now or in the future. Not on F-1 / CPT / OPT / H-1 / TN / other listed visas. |
| Sponsorship | **No** — do not need and will not need sponsorship |
| How did you hear about this role? | **LinkedIn Jobs** / company careers (Workday). If a source list includes Other, use that. |
| Salary range $26.50–$45.25/hr | **Yes** — accept the posted intern range |
| Languages you can interview in | **C++, Python, SQL, TypeScript/JavaScript (Angular), HTML/CSS**. Do **not** check Java, C, C#/.NET, Swift, Jenkins, GitLab, or firmware. |

---

## "Why Medtronic / why this internship?"

I want to spend a summer writing software that has to be correct — design, test, debug, ship — not a generic intern rotation. Medtronic is the software around devices that reach patients. That is more interesting to me than another web-only intern seat.

The work I can defend:

- **Software / data / cloud.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2. On SignalWeaver I implemented pgvector semantic search at 49ms p50 / 99ms p99. That is design / develop / test / ship on real data.
- **Systems, honestly scoped.** I built a real-time C++/JUCE audio engine whose `processBlock()` path cannot allocate or take a lock: a `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering. That is engineering tools and correctness under constraint, not a medical-device or firmware internship. I have not interned on devices, Java, or embedded firmware, and I will not pretend to.

I can be onsite in Fridley for Summer 2027 (June 1–August 13). I return to Michigan afterward (Expected May 2028). I am a U.S. citizen and do not need sponsorship.

---

## "Tell us about a project you built" / additional information

Two that map onto this req without inflating the stack:

**Granular synthesizer (C++ systems).** github.com/Verdent06/granular-synth. Zero-allocation audio thread, lock-free UI-to-audio FIFO, VST3/AU release binaries after a real-time safety audit (no heap, no locks in `processBlock()`). Closest analog I have to "design, test, debug, and implement software components, tools, and utilities" — still DSP, not device firmware.

**MDC / Vylet (applications + data).** Production Flask API on EC2; Dockerized pipeline with Redis/Celery and an asyncpg data layer plus injection-safe SQL freshness checks. Live product at vyletdata.com.

---

## "Preferred team / which intern track?"

If the form lets you pick: **Software Engineer** (applications) first, **Software Test** / **Cloud** / **AI/Data Science** next. If they ask about Firmware: "I have not written embedded firmware or medical-device software. I have shipped C++ that cannot miss a real-time deadline. I would ramp on the team's hardware."

---

## Availability

Summer 2027, 10–11 weeks, onsite Fridley, June 1–August 13. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Do not claim medical-device internships, Java, C#, Swift, C, Jenkins, or firmware.** The JD lists them as possible languages or *possible* placement tracks. Your pool does not have them. Honest C++ + Python + SQL + JS-family beats a knockout lie.
- **Do not write a cover letter that sounds like a firmware intern.** Lead with MDC (shipped API/ETL) and Granular (C++ systems). Vylet's LangGraph story is fine as production ownership, not as "I want to do agents at Medtronic."
- **Location is not a skip.** Say yes to Fridley.
- **Catch-all posting:** team match is not guaranteed. Apply anyway; the resume is the gate (`companies.md`: bottleneck resume + Aon, ~10–15%).
- **Aon SJT** comes before the HM. Treat it as a real filter (`recruiting.md`: behavioral is elimination).
- **Referral:** no Medtronic contact in `network.md`. A UMich alum still beats a cold Workday pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
