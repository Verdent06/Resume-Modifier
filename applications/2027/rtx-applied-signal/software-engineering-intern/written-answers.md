# RTX / Applied Signal Technology — Software Engineering Intern (Summer 2027, West Valley City / Salt Lake City UT) · Cover letter & Workday answers

Req **01865952**. US-UT-WEST-VALLEY-CITY-338, 1127 & 1128 W 2400 S, Bldg 338; staffed in Salt Lake City. Drafted from `persona.md` + real experience only. No invented Java, Rust, Qt, embedded HW, ITU, TCP/IP, Linux homelab, projects, or metrics. This is Applied Signal Technology SIGINT / advanced-communications software — not Marlborough radar, Tewksbury Patriot, Huntsville, or Cedar Rapids avionics.

Workday questionnaire endpoints were not publicly readable; these are the knockout + short-answer set RTX intern apps typically ask. Trim to each form's length limit before submitting.

---

## Knockout items (answer factually)

- **Are you a U.S. citizen?** Yes. U.S. citizenship is required; only U.S. citizens are authorized under this program/contract. No H-1B.
- **Currently enrolled, returning to school after the internship?** Yes — B.S. Computer Science & Economics, University of Michigan, Expected May 2028 (rising senior in Summer 2027; ~96 credits by the term). Enrolled through completion of the internship.
- **Cumulative GPA / graduation:** 3.66 / 4.0; Expected May 2028.
- **Willing to work onsite in West Valley City / Salt Lake City, UT for Summer 2027?** Yes. Location is not a skip — I will relocate and work onsite for the term. Relocation is listed as eligible on RTX intern postings.
- **Languages you can interview in (check only these):** **C++, Python**. Angular is in Frameworks (Voice-AI co-op UI work). Do **not** check Java, Rust, Qt, Ada, or embedded RTOS. If there is an "other" box: "C++ real-time systems (JUCE/DSP, lock-free SPSC, zero-allocation audio thread, CMake VST3/AU); Python production services (Flask, FastAPI, Docker, GitHub Actions/pytest); Angular UI."

---

## Cover letter / additional information (≈160 words)

I am applying for the Software Engineering Intern role at RTX Applied Signal Technology in West Valley City / Salt Lake City for Summer 2027. I want to spend the summer on architecture, design, integration, testing, and field support for software that processes advanced communications — the same discipline I already practice in C++ systems work and in production Python services.

The work that maps most directly is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a fixed `MemoryPool<Grain, 64>` slab per voice at startup and deliver UI parameters through a hand-rolled lock-free SPSC FIFO with atomic acquire/release ordering. CMake builds VST3/AU binaries only after every `processBlock()` path is audited for zero heap allocations and zero lock acquisitions.

Alongside that I ship production software. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network, I replaced ~800 hours of manual PAC research with a Python ETL and delivered a Flask REST API on AWS EC2. At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS on an Angular client and held main-thread blocking under 5ms with a Web Worker. SignalWeaver ships with Docker Compose and a GitHub Actions pipeline that runs pytest on every main build.

I do not have Java, Rust, Qt, embedded RTOS, or ITU/telecom coursework; C++ and Python are the languages I can defend in an interview. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028) and will work on-site in West Valley City / Salt Lake City.

---

## "Why RTX / this internship / Applied Signal Technology?" (≈90 words)

AST's Salt Lake City software teams write SIGINT and advanced-communications applications — full lifecycle work on collaborative product teams where code review, integration, and test are the job. That matches how I already build: deterministic C++ on a hard-deadline thread (zero-allocation `processBlock()`, lock-free UI-to-audio, CMake release gates), and Python services held to a test bar (pytest CI, production Flask on EC2). I want a summer inside a development team that treats performance, integration, and SDLC as the default, not a class project — specifically on comms/SIGINT software in Utah, not a radar or avionics site.

---

## "Tell us about relevant technical experience." (≈120 words)

- **C++ / OOD / multithreading / CMake:** Granular synthesizer in C++/JUCE — `MemoryPool<Grain, 64>` so `processBlock()` never heap-allocates after `prepareToPlay()`; lock-free SPSC FIFO (atomic acquire/release) for UI-to-audio; CMake VST3/AU builds audited for zero allocations and zero locks.
- **UI / Angular:** Voice-AI co-op — Angular client, Web Worker off the UI thread, <5ms main-thread blocking, 60 FPS; fault-tolerant RxJS that cut a 27% upload-failure rate (including MIME types Angular rejected).
- **Python delivery (JD-listed language):** Sole engineer on a 5-month contract — Flask REST API on AWS EC2 plus a Requests + Pandas ETL that removed ~800 hours of manual pulls across 400 PACs. SignalWeaver: async FastAPI at 9.1s p50 / 15.2s p99 across 90 runs, Docker Compose + GitHub Actions pytest.
- **Team / SDLC:** Code-review-adjacent release gates (real-time safety checklist before binaries; pytest on every main push). I have not shipped Rust, Qt, Java, or ITU/telecom stacks; I ramp on typed/compiled languages from C++.

---

## "Tell us about a time you tested / integrated / reviewed software."

**SignalWeaver + Granular, honestly scoped:** I containerized SignalWeaver (FastAPI + Postgres/pgvector + nginx) and wired a GitHub Actions pipeline that builds the frontend, runs pytest, and builds the API image on every main push. On the C++ plugin I treated the audio callback as a safety-critical path: every `processBlock()` route is audited against a zero-allocation / zero-lock checklist before VST3/AU release builds. That is the closest analog I have to "code review + test plan before the artifact ships." I have not worked embedded HW/SW integration or ITU standards on a SIGINT codebase; I would ramp on the team's language and process.

---

## Availability

Summer 2027, exclusive onsite West Valley City / Salt Lake City, UT. Willing to relocate. Returning to Michigan after the internship (graduation Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Lead with C++ real-time and Python delivery, not ML and not campaign-finance.** Open interviews with Granular (`processBlock`, MemoryPool, SPSC, CMake), then CaseStudyPrep concurrency/Angular and MDC shipping.
- **Never claim Java, Rust, Qt, Ada, embedded RTOS, TCP/IP projects, ITU, or a Linux homelab.** Honest C++ + Python beats a Skills-line lie.
- **Unix/Linux:** not on the resume and not in the inventory. If asked: I develop and deploy on Linux-class environments (AWS EC2, Docker) and macOS CMake builds; I have not done VxWorks/embedded RTOS. Do not invent a Linux homelab.
- **Location is not a skip.** Answer yes to West Valley City / Salt Lake City onsite; relocation intent is real.
- **Citizenship is a form knockout.** Answer yes; this intern posting does not name Secret/TS-SCI (FT AST roles at the site often do).
- **Referral still helps.** C-tier RTX intern reqs are resume-first (`companies.md`: bottleneck = resume, ~20–25%).
