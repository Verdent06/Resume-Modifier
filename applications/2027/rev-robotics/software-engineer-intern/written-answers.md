# REV Robotics — Software Engineering INTERN 2027 (Carrollton, TX) · Written Application Answers

Draft answers for the live Rippling intern card (`INTERN or CO-OP 2027`). Grounded in `persona.md`, `grade.md` Interview angles, and `context.md` only. First-person, honest, defensible under "walk me through this."

**Form-kit email is `verdent06@gmail.com`. Never use `vedantde@umich.edu`.**

**Do not invent:** FIRST / FRC / FTC team years, C, Java, LabVIEW, WPILib, robot firmware, ROS, Snowflake, Databricks, Tableau, Copilot, Fusion, Granular xrun/latency/CPU/user numbers, Michigan Data Consulting or SpaceXAI as employers, or awards/honors.

Apply: https://ats.rippling.com/rev-robotics/jobs/9f4e5d99-0bba-4e03-8018-e312810a3dba/apply

JD: https://ats.rippling.com/rev-robotics/jobs/9f4e5d99-0bba-4e03-8018-e312810a3dba

Resume: `applications/2027/rev-robotics/software-engineer-intern/Vedant Desai Resume.pdf`

**This agent did not submit.** Paste into Rippling yourself.

---

## Knockout / structured fields (Rippling basic + intern card)

| Field | Answer |
| --- | --- |
| First name | Vedant |
| Last name | Desai |
| Email | **verdent06@gmail.com** |
| Phone number | (248) 704-4852 |
| Location (city only) | Northville, MI |
| LinkedIn link | https://linkedin.com/in/vedantde06 |
| Website link | https://github.com/Verdent06 |
| Resume | `applications/2027/rev-robotics/software-engineer-intern/Vedant Desai Resume.pdf` |
| Cover letter | Optional. Paste the letter below if you attach one. |
| Where did you first hear about REV's internship opportunities? | **Somewhere else (please share the location in the comments)** → `Rippling ATS job posting (ats.rippling.com/rev-robotics)` |
| What year of schooling are you currently in and what is your major? | Sophomore year; B.S. Computer Science and Economics (Expected May 2028). Summer 2027 = after sophomore year / rising junior. |
| Which college are you attending? | University of Michigan, Ann Arbor |
| Preferred timing for an internship? | **June - September 2027** |
| Are you authorized to work in the United States? | **Yes** |
| Will you now or in the future require any form of sponsorship to continue your employment? | **No, I will not need sponsorship of any kind** |
| REV Robotics is an in-office employer based in Carrollton, Texas. If offered this position, will you be able to reliably make the commute each day? | Yes. I will relocate to the Dallas / Carrollton area for the internship and can be in-office each workday. (Northville, MI is current home; I am not commuting from Michigan.) |
| What is your desired hourly pay range? | $20–$22 per hour (within the posted $18–$22 range) |

---

## Required long answers (paste)

### Describe your experience and role(s) with the FIRST® Organization or other robotics team.

I have not been a member of a FIRST Robotics (FRC/FTC) team or another competitive robotics team, and I will not invent one.

The closest analog I can defend is shipping C++ that has to meet a hard real-time constraint, then packaging it as a library-style binary other people can load. I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` callback cannot heap-allocate or take a lock. I pre-allocate a `MemoryPool<Grain, 64>` slab per voice, move UI-to-audio messages through a lock-free SPSC FIFO, and ship VST3/AU from one CMake codebase after a real-time safety audit (zero heap, zero locks). github.com/Verdent06/granular-synth

That is not FRC. It is independent C++ systems work, GitHub-visible, with test/release discipline — the same shape as contributing to firmware or student libraries under a REV engineer, then ramping on REV's stack (including Java/C if that is what the team ships) rather than claiming it.

### Please describe any other information, experience, or coursework that you feel would make you an ideal candidate for this position.

I am a University of Michigan B.S. Computer Science and Economics student (Expected May 2028, GPA 3.66) applying for June–September 2027, onsite Carrollton. I interview in TypeScript and C++ (the JD's JS/TS must and C++ plus). I do not interview in C, Java, or LabVIEW.

What I would bring to firmware-or-library work, plus test/debug/docs:

- **TypeScript in production, with debug ownership.** At CaseStudyPrep.AI (Software Engineer Co-op, Voice AI) I cut a 27% audio-upload failure rate with fault-tolerant RxJS that regenerates expired S3 URLs mid-flight and negotiates MIME types Angular was silently rejecting. I moved audio off the UI thread into a Web Worker (main-thread blocking under 5ms at 60 FPS) and cut cloud inference cost 40% by running Silero VAD client-side via ONNX Runtime. That is student-library adjacent in spirit: find the failure, fix it, document the contract.
- **C++ under a deadline the hardware will not wait for.** Granular (above): zero-alloc audio thread, lock-free UI-to-audio FIFO, CMake VST3/AU release. I have no callback-latency / xrun / CPU number; I would measure those next. I will not invent firmware-on-a-SPARK-MAX.
- **Independent delivery and eval.** I founded Vylet (live product, $1,500 MRR): Dockerized pipeline, a name-collision defect that lifted lead-qualification 79%→89%, and a LangSmith eval suite plus deterministic gates (faithfulness 50%→90%). I can follow a spec and also ship when the spec is "make the library usable and tested."

Coursework I can actually talk about: Data Structures & Algorithms, Discrete Mathematics, Calculus III, Physics (Mechanics). Git/GitHub is how I collaborate (public repos above). IDEs: VS Code for TypeScript; CMake/JUCE tooling for C++.

I will relocate to Carrollton for the term. No awards. Prior employment to list: CaseStudyPrep.AI SWE co-op and founder of Vylet only.

---

## Cover letter (optional — paste if you attach one)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

REV Robotics — Software Engineering INTERN 2027
Carrollton, TX (onsite)

Dear REV recruiting team,

I am applying for the Summer 2027 software engineering internship in Carrollton. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work in-office for June–September 2027 after relocating to the Dallas area. I am a U.S. citizen and do not need sponsorship.

REV's intern job is firmware or student libraries, plus test, debug, and documentation for parts FRC/FTC teams actually use. I have not been on a FIRST team. I have shipped TypeScript in production, C++ that cannot miss a real-time deadline, and independent test/eval work.

- **Debug on a live product.** CaseStudyPrep.AI: 27% upload-failure recovery (RxJS / S3 / Angular MIME), Web Worker offload under 5ms at 60 FPS, 40% inference-cost cut via on-device Silero VAD.
- **C++ library-style release.** Granular synthesizer plugin: `MemoryPool<Grain, 64>`, lock-free SPSC, CMake VST3/AU after a zero-heap / zero-lock audit. github.com/Verdent06/granular-synth
- **Independent eval.** Vylet: qualification 79%→89% on a name-collision defect; LangSmith eval gates 50%→90% faithfulness.

I want the Carrollton seat writing example code and firmware-adjacent C++/TS that students can trust, not a generic feature rotation. I will ramp on Java/C if that is the team's library language rather than claim them.

Sincerely,
Vedant Desai

---

## Notes for the applicant (not for submission)

- **FIRST essay is load-bearing** (`persona.md` / Rippling card). An 8.0 PDF does not substitute for inventing FRC. Honest "no FIRST + C++ analog" is the only defensible path (`grade.md` Defend).
- **Do not list Michigan Data Consulting or SpaceXAI Campus Lead as employers.** CaseStudyPrep.AI + Vylet only. No honors/awards.
- **Do not claim C, Java, LabVIEW, WPILib, SPARK MAX firmware, ROS, Snowflake, Databricks, Tableau, Copilot, or Fusion.**
- **Do not invent a Granular runtime metric.**
- **Commute field is 250 characters.** Relocate-to-Carrollton, not Michigan-to-Texas daily commute.
- **Pay:** stay inside $18–$22. $20–$22 is the top of the posted band, not a negotiation opener.
- **Work-auth:** U.S. citizen in `context.md`. Yes / no sponsorship.
- **Referral:** none in `network.md`. Do not invent a REV employee name.
- **Cover letter is optional.** The PDF plus the FIRST essay are the screen. Binding filter after that: unpublished small-office project walk (`companies.md`: bottleneck resume + FIRST essay, ~20–30%).
