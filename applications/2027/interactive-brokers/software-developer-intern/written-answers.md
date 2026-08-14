# Interactive Brokers — Software Developer Summer Internship 2027 (Greenwich) · Written Application Answers

Drafted from `persona.md` + real experience in `context.md` only. No invented projects, metrics, Java, or trading internships. Trim to the form's length limit before submitting.

Apply: https://jobs.dayforcehcm.com/en-US/ibgllc/candidateportal/jobs/2088
Jobright: https://jobright.ai/jobs/info/6a7e2554b56bea5779c03fe6
Resume: `applications/2027/interactive-brokers/software-developer-intern/Vedant Desai Resume.pdf`

The live Dayforce form was not fully scrapeable from this environment. Fill knockouts factually; paste the cover letter if the portal asks for one. Do **not** check Java.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/interactive-brokers/software-developer-intern/Vedant Desai Resume.pdf` |
| Location | **Greenwich, CT — onsite.** Willing to relocate for Summer 2027. |
| Currently pursuing BS/MS/Ph.D. in CS or Software Engineering? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (inside preferred window Dec 2027–May 2028) |
| GPA | **3.66 / 4.0** (JD floor is 3.5) |
| 9-week onsite commitment | **Yes** |
| Programming languages you can interview in | **C++, Python, SQL, TypeScript/JavaScript (Angular).** Do **not** check Java. |
| Work authorization / sponsorship | US citizen; authorized to work in the US **without sponsorship**. |
| How did you hear about this role? | **Jobright** (https://jobright.ai/jobs/info/6a7e2554b56bea5779c03fe6). If Jobright is not listed: Other → Jobright. |
| Available to start | June 2027 (program start; can be onsite Greenwich for the full 9 weeks) |

---

## Cover letter (if Dayforce asks; paste as-is)

I am a Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66) applying to Interactive Brokers' Software Developer Summer Internship in Greenwich.

I want to spend nine weeks writing software that has to be correct next to real markets infrastructure — execution, custody, back/middle/front office — not a generic intern rotation. IBKR's intern posting is that job: design, develop, and maintain software, own a project with mentorship, and sit in code reviews. I can be onsite in Greenwich for the full 9 weeks.

What I can defend:

- **C++ systems.** I built a real-time audio engine in C++/JUCE whose `processBlock()` path cannot allocate or take a lock: a pre-allocated `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering, then a release audit (zero heap, zero locks) before VST3/AU binaries. That is the closest analog I have to performance-sensitive production code. github.com/Verdent06/granular-synth
- **Python shipping.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2.
- **Financial-data work, honestly scoped.** SignalWeaver is a multi-signal financial research assistant (not investment advice): pgvector semantic search at 49ms p50 / 99ms p99, containerized with Docker Compose and GitHub Actions CI. CS + Economics is the academic half of that interest; I have not interned on an exchange matching engine, and I will not pretend to.

I interview in C++ and Python. The intern JD also names Java; I have not shipped production Java and will not check it. I would ramp Java on the team's codebase if that is what the desk uses.

I return to Michigan after the internship (Expected May 2028).

Vedant Desai
vedantde@umich.edu · (248) 704-4852
https://github.com/Verdent06 · https://linkedin.com/in/vedantde06

---

## "Why Interactive Brokers / why this internship?"

I want to write software for a brokerage that actually runs on technology — automated execution and custody — not a bank IT rotation. The intern role is design/develop/maintain plus owning a project with daily check-ins and code review. That matches how I already work: C++ under a hard real-time constraint (Granular), and Python shipped to a real stakeholder (MDC Flask/EC2). SignalWeaver is the financial-data project I can walk through; I have not worked on live order routing, and I will say so.

Greenwich, onsite, nine weeks, Summer 2027. I am a US citizen and do not need sponsorship.

---

## "Tell us about a project you built"

**Granular synthesizer (C++).** github.com/Verdent06/granular-synth. Zero-allocation audio thread, lock-free UI-to-audio FIFO, VST3/AU release binaries after a real-time safety audit. Closest analog to "high-performance" on this posting.

**MDC (Python production).** Production Flask REST API on AWS EC2 as sole engineer on a 5-month contract; ETL that cut ~800 hours of manual PAC pulls across 400 committees.

**SignalWeaver (financial research, not trading).** pgvector search 49ms p50 / 99ms p99; Docker Compose + GitHub Actions CI. Research assistant, not investment advice.

---

## Java gap — honest framing (if asked)

The JD names C++, Java, or Python. I have not shipped production Java. I have shipped C++ under real-time constraints (lock-free SPSC, zero-allocation `processBlock()`, CMake release binaries) and Python in production (Flask/EC2). I interview in C++ or Python and will ramp Java if the team uses it.

---

## Date overlap — honest framing (if asked)

MDC (Jan–May 2026) and CaseStudyPrep.AI (Dec 2025–May 2026) overlapped. Both were real; neither was a sequential full-time job. MDC was a contracted data-engineering engagement (sole engineer on that contract). CaseStudyPrep was a remote Voice AI co-op. If a screen asks "sole engineer," say sole on the MCFN contract, concurrent with the co-op — not 80-hour exclusive employment.

---

## Notes for the applicant (not for submission)

- **Do not claim Java, exchange matching, or a prior trading intern.** The production floor is C++/Java; your inventory is C++ and Python. Honest beats a knockout lie.
- **Do not lead with LoRA / LangGraph / agentic product.** Persona anti-pattern for this req.
- **GPA belongs on the form.** 3.66 vs 3.5 floor.
- **Referral:** no IBKR contact in `network.md`. A UMich alum in Greenwich still beats cold Dayforce (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **OA is the binding filter** after this PDF (`companies.md` / `grade.md`): DS&A mediums + math/probability, then C++ threading/memory.
