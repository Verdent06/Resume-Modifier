# Western Digital — Summer 2027 Intern, Software Engineering (San Jose) · Written Application Answers

Draft answers for SmartRecruiters req `744000143171017`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented OS, compiler, or firmware internships, no invented Linux, Java, or Go. Trim to the form's length limit before submitting.

This posting is a **catch-all**. Recruiting may route you to Applications, System Tools, Data Analytics, Firmware, or Systems Integration. Prefer **Applications** and **Data Analytics**; System Tools only as C++ engineering-tools / performance work. Do **not** volunteer Firmware unless they ask, and then only as C++ real-time constraints from the synth — not embedded firmware.

Apply: https://jobs.smartrecruiters.com/WesternDigital/744000143171017-summer-2027-intern-software-engineering

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/western-digital/software-engineering-intern/Vedant Desai Resume.pdf` |
| Location preference | **San Jose, CA** (Great Oaks HQ). Other listed sites (Irvine, Fremont, Colorado Springs, Longmont, Rochester MN) are acceptable if they ask, but San Jose is the target. |
| Willing to work onsite / relocate | **Yes** — San Jose for Summer 2027. Relocation is at hiring-manager discretion (WD FAQ). |
| Currently pursuing Bachelor's or Master's in CS / SWE / related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Will you have at least one term remaining after the internship? | **Yes** — Fall 2027 and Winter 2028 remain after Summer 2027 |
| Graduation date | **May 2028** |
| GPA | **3.66 / 4.0** (only if the form asks; ≥3.5 so it belongs) |
| Work authorization / sponsorship | Other 2027 applications in this repo state you are authorized to work in the US **without visa sponsorship**. Answer the SmartRecruiters work-rights question **truthfully**. This 2027 catch-all posting does **not** list a no-sponsorship knockout (some 2026 WD firmware reqs did). Do not guess citizenship if the form asks it separately. |
| How did you hear about this role? | **Jobright** (https://jobright.ai/jobs/info/6a7cd1d6d77e8156a8e34665). If Jobright is not listed: **LinkedIn Jobs** / Other → Jobright. |
| Salary range $34.52–46.00/hr | **Yes** — accept the posted CA intern range |
| Languages you can interview in | **C++, Python, SQL, TypeScript/JavaScript (Angular)**. Do **not** check Java, Go, C, Linux, firmware, compilers, or OS internals. |

---

## "Why Western Digital / why this internship?"

I want to spend a summer writing software that has to be correct next to real systems — storage, tools, and applications — not a generic intern rotation. WD is building the storage layer the AI data economy actually sits on. That is more interesting to me than another web-only intern seat.

The work I can defend:

- **Applications / data systems.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2. On SignalWeaver I implemented pgvector semantic search at 49ms p50 / 99ms p99. That is design / develop / test / ship on real data — the Applications and Data Analytics tracks on this posting.
- **System software, honestly scoped.** I built a real-time C++/JUCE audio engine whose `processBlock()` path cannot allocate or take a lock: a `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering. That is engineering tools and performance work, not an operating-systems or compiler internship. I have not interned on OS kernels, compilers, or drive firmware, and I will not pretend to.

I can be onsite in San Jose for Summer 2027. I return to Michigan afterward (Expected May 2028).

---

## "Tell us about a project you built" / additional information

Two that map onto this req without inflating the stack:

**Granular synthesizer (C++ systems).** github.com/Verdent06/granular-synth. Zero-allocation audio thread, lock-free UI-to-audio FIFO, VST3/AU release binaries after a real-time safety audit (no heap, no locks in `processBlock()`). Closest analog I have to "troubleshoot, debug, and optimize software performance" and to collaborating with a hard constraint the way firmware/tools teams do — still DSP, not HDD firmware.

**MDC / Vylet (applications + data).** Production Flask API on EC2; Dockerized pipeline with Redis/Celery and an asyncpg data layer plus injection-safe SQL freshness checks. Live product at vyletdata.com.

---

## "Preferred team / which intern track?"

If the form lets you pick: **Applications Software** first, **Data Analytics** second. If they ask about System Tools, talk C++ performance and engineering tools (the synth), not OS/compilers. If they ask about Firmware: "I have not written embedded firmware or assembly. I have shipped C++ that cannot miss a real-time deadline. I would ramp on the team's hardware."

---

## Availability

Summer 2027, ~12 weeks, onsite San Jose. Available to start May 2027. Returning to the University of Michigan after the internship.

---

## Notes for the applicant (not for submission)

- **Do not claim OS, compilers, firmware, Linux, Java, or Go.** The JD lists them as possible languages or *possible* System Tools work. Your pool does not have them. Honest C++ + Python + SQL + JS-family beats a knockout lie.
- **Do not write a cover letter that sounds like a firmware intern.** Lead with MDC (shipped API/ETL) and Granular (C++ systems). Vylet's LangGraph story is fine as production ownership, not as "I want to do agents at WD."
- **Location is not a skip.** Say yes to San Jose.
- **Catch-all posting:** "an immediate opening or interview is not guaranteed." Apply anyway; the resume is the gate (`companies.md`: bottleneck resume, ~8–12%).
- **Referral:** no WD contact in `network.md`. A UMich alum at WD still beats a cold SmartRecruiters pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
