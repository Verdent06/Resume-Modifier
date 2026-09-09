# CHAOS Industries — 2027 Summer- Software Engineer Intern · Written Application Answers

Draft answers for Greenhouse job **5226636007**. Field labels and option text captured from the live apply page plus `https://boards-api.greenhouse.io/v1/boards/chaosindustries/jobs/5226636007?questions=true` on 2026-09-09. Grounded in `persona.md` (full-stack spine + real-time / embedded-adjacent / defense sensor-sync / CDN differentiator), `grade.md` Interview angles, and `context.md` metrics only.

**Do not invent:** Java, JAX, C-as-distinct-from-C++, firmware, MCU, RTOS, ROS, oscilloscope / logic-analyzer work, Snowflake, Databricks, Copilot, Fusion, Tableau, Granular xrun / callback-latency / CPU / user counts, MDC API traffic or latency, an active clearance, a CHAOS referral.

**Do not submit from this run.** Resume + written answers only.

Apply: https://job-boards.greenhouse.io/chaosindustries/jobs/5226636007
Resume: `applications/2027/chaos-industries/software-engineer-intern-summer-2027/Vedant Desai Resume.pdf`
SHA-256: `dfb371b4c87af4afc1a5551536fff249b52aa69567e7f9c60e9f48e34dece31a`

`*` = required on the Greenhouse form.

There is **no screening-essay text box**. The JD asks for a sample of work or a short note tying experience to embedded + hardware + group collaboration — paste that as the optional Cover Letter (file or `cover_letter_text`).

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | **verdent06@gmail.com** only. Never `vedantde@umich.edu` on this form. The PDF header still shows umich (template; writer cannot change it). |
| Country (live page) | United States |
| Phone * | (248) 704-4852 |
| Location * | Ann Arbor, MI (school city). Use the Locate-me / city widget; hidden lat/long fill from the widget. Do not invent a California address. |
| Resume/CV * | `applications/2027/chaos-industries/software-engineer-intern-summer-2027/Vedant Desai Resume.pdf` |
| Cover Letter | Optional on Greenhouse. **Attach or paste** the cover letter below — it is the JD's "sample of work or short note." |
| Website | https://github.com/Verdent06/granular-synth (sample of work the JD asked for). Fallback: https://github.com/Verdent06 |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| I live within commutable distance of or am willing to relocate to the location where this position is based. * | **Yes** — El Segundo / LA onsite, 12 weeks, Summer 2027. Relocation package is on the JD. |
| Are you authorized to work for any employer in the United States? * | **Yes** — U.S. citizen. No sponsorship now or later. |
| Are you a U.S. Person (i.e. a U.S. Citizen, a lawful permanent resident of the U.S., or a protected individual as defined by 8 U.S.C. 1324b(a)(3)) who can obtain and maintain a Security Clearance? * | **Yes** — U.S. citizen; clearance-eligible. Do **not** select No. |
| Do you presently hold an active U.S. security clearance, or are you eligible to obtain and maintain a U.S. security clearance? * | **Yes, I am eligible for a U.S. security Clearance** (exact option spelling, including capital C in Clearance). Form note: this position does not necessarily require clearance eligibility. |
| Are you any of the following “protected individual(s)” as defined in the Immigration and Naturalization Act, 8 U.S.C. 1324b(a)(3)? * | **A United States citizen or national** |
| School / degree / GPA (not on this Greenhouse form; on the PDF) | University of Michigan · B.S. Computer Science and Economics · GPA **3.66 / 4.0** · Expected **May 2028** |
| Internship term | **Summer 2027 only.** Paid, in-person, 12 weeks. Return to Michigan afterward. |
| Gender / Hispanic/Latino / Race / Veteran / Disability (EEO) | Optional. Skip for volume (`recruiting.md` Part I §2). |

### Clearance multi-select — exact option text

Live options (`question_12802691007[]`):

- `Yes, I hold an active U.S. security clearance` — **do not select** (never held a clearance)
- `Yes, I am eligible for a U.S. security Clearance` — **select this**
- `No` — knockout if they later need eligibility; do not pick

### Protected-individual multi-select — exact option text

Live options (`question_12802692007[]`):

- `A United States citizen or national` — **select this**
- `A person lawfully admitted for permanent residence of the United States (i.e., "Green Card" holder)` — do not select
- `A person admitted as a refugee to the United States under 8 U.S.C. 1157` — do not select
- `A person admitted as an asylee to the United States under 8 U.S.C 1158` — do not select
- `None of the above` — knockout

EXPORT CONTROLS preface on the form: answers are for eligibility to receive export-controlled information, not a resume line (`persona.md`).

---

## JD short note / Cover Letter (paste)

The posting: "In your application, we'd love to see either a sample of work you're proud of or a short note about your prior experience and how it relates to the three points above" — embedded exposure, willingness to work on hardware, and having done those in a group.

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06/granular-synth

CHAOS Industries — 2027 Summer- Software Engineer Intern
El Segundo, California (onsite)

Dear CHAOS recruiting team,

I am applying for the Summer 2027 Software Engineer Intern seat in El Segundo. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can relocate for the full 12-week in-person term and return to Michigan afterward. I am a U.S. citizen. I do not need sponsorship. I have never held a clearance; I am eligible to obtain one.

This posting is firmware on sensor nodes plus the software that keeps them synchronized — real-time under timing, power, thermal, and radio constraints — at a company whose product is CDN™, not a consumer web internship. I have not shipped MCU firmware, RTOS, Java, or JAX. I have shipped C++ under a hard real-time constraint, Python services I deployed myself, and frontend that other people used.

How that maps to the three points on the posting:

- **Embedded / real-time software.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO (64-slot, atomic acquire/release) keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit. That is the sample of work I am proud of: https://github.com/Verdent06/granular-synth. I do not have a callback-latency or xrun number to quote.
- **Willingness to work on hardware.** I want the bench-adjacent intern work, not a remote CRUD rotation. Closest analog I have is production audio that had to stay correct next to real devices and files: at CaseStudyPrep I ran Silero VAD on-device via ONNX Runtime, moved processing off the UI thread (main-thread blocking under 5ms, visualizer at 60 FPS), and closed a 27% S3 upload failure with in-flight URL regeneration. I have not used a logic analyzer or written node firmware. I will ramp on the hardware next to people who have.
- **Group delivery.** CaseStudyPrep was a co-op on a live voice-AI product, not a solo demo. At Michigan Data Consulting I was the only engineer on a five-month MCFN contract and still scoped delivery with the stakeholder — Flask REST on AWS EC2 after a Requests + Pandas ETL across 400 PACs. I do not have a competition-team or club firmware project to name.

I interview in C++ and Python. I will not claim Java, JAX, or C as a separate language. I want the El Segundo SWE intern seat for Summer 2027.

Sincerely,
Vedant Desai

---

## If the cover-letter box is tight (short note only)

Sample of work: https://github.com/Verdent06/granular-synth — C++/JUCE `processBlock()` with a `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO so the audio thread never allocates or takes a lock after `prepareToPlay()`. That is my embedded-adjacent signal (not MCU firmware). Hardware willingness: I will work onsite next to sensor hardware; closest shipped analog is CaseStudyPrep on-device VAD + a 27% upload-failure fix on a team voice-AI product. Group work is that co-op, not a fabricated robotics club. U.S. citizen; relocate to El Segundo for Summer 2027; Expected May 2028.

---

## Notes for the applicant (not for submission)

- **Email:** form uses `verdent06@gmail.com` only. Never umich on Greenhouse. PDF still lists `vedantde@umich.edu`.
- **Do not claim firmware, MCU, RTOS, ROS, Java, JAX, or C-as-C.** Honest mapping: C++ real-time (Granular) + Python deploy (MDC/Vylet) + frontend (CaseStudyPrep/SignalWeaver).
- **Do not invent a Granular metric.** Walk MemoryPool, lock-free SPSC, and the `processBlock` audit (`grade.md` Defend).
- **Vylet reads PE/LangGraph on a skim.** Pivot to Docker/Redis/Celery and 79%→89% if asked (`grade.md`).
- **SignalWeaver is financial research storage + React**, not CDN sync (`grade.md`).
- **No CHAOS contact** in `network.md`. Cold Greenhouse apply. Do not invent a referral.
- **Behavioral:** CaseStudyPrep 27% upload recovery = own-the-failure. Granular = deadline you cannot miss. MDC = sole-engineer delivery with a stakeholder.
- **Funnel:** Greenhouse human PDF read (binding; OA unpublished) → recruiter → live tech → panel. Do not assume HackerRank/CodeSignal (`company.md`). Prep C++ constraint walkthrough + Python/storage/frontend stories for the generic SWE screen (`persona.md`).
- **Apply in this first wave** (posted 2026-09-08). Do not submit from this agent.
