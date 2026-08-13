# RTX / Raytheon — Software Development Intern (Summer 2027, Tewksbury MA) · Cover letter & Workday answers

Req **01865635**. Concord Bldg, 50 Apple Hill Dr, Tewksbury TB3. Drafted from `persona.md` + real experience only. No invented Java, C#, Ada, projects, or metrics.

Workday questionnaire endpoints were not publicly readable; these are the knockout + short-answer set RTX intern apps typically ask. Trim to each form's length limit before submitting.

---

## Knockout items (answer factually)

- **Are you a U.S. citizen?** Yes. U.S. citizenship is required because only U.S. citizens are eligible for the DoD Secret clearance (interim required before start).
- **Can you obtain and maintain a U.S. government security clearance?** Yes — I am a U.S. citizen and able to obtain INTERIM Secret before the start date.
- **Currently enrolled, returning to school after the internship?** Yes — B.S. Computer Science & Economics, University of Michigan, Expected May 2028 (rising junior in Summer 2027).
- **Cumulative GPA / graduation:** 3.66 / 4.0; Expected May 2028.
- **Willing to work exclusive-onsite in Tewksbury, MA for Summer 2027?** Yes. Relocation eligible on the posting; I can relocate for the term.
- **Languages you can interview in (check only these):** **C++, Python**. Do **not** check Java, C#, or Ada. If there is an "other" box: "C++ real-time systems (JUCE/DSP, lock-free SPSC, zero-allocation audio thread); Python production services (Flask, FastAPI, Docker, GitHub Actions/pytest)."

---

## Cover letter / additional information (≈160 words)

I am applying for the Software Development Intern role on the Raytheon software team in Tewksbury for Summer 2027. I want to spend the summer designing, debugging, and reviewing software for complex, high-performance systems — the same discipline I already practice in C++ and in production Python services.

The work that maps most directly is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a fixed `MemoryPool<Grain, 64>` slab per voice at startup and deliver UI parameters through a hand-rolled lock-free SPSC FIFO with atomic acquire/release ordering. Release VST3/AU binaries only ship after every `processBlock()` path is audited for zero heap allocations and zero lock acquisitions.

Alongside that I ship production software. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network, I replaced ~800 hours of manual PAC research with a Python ETL and delivered a Flask REST API on AWS EC2. At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS logic and held main-thread blocking under 5ms with a Web Worker. SignalWeaver ships with Docker Compose and a GitHub Actions pipeline that runs pytest on every main build.

I do not have Java, C#, or Ada in my portfolio; C++ and Python are the languages I can defend in an interview. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028) and can work on-site in Tewksbury.

---

## "Why RTX / this internship / Tewksbury?" (≈90 words)

Tewksbury's Concord campus writes Patriot and Missile Defense Sensors product software — complex, high-performance, object-oriented systems where debug, integration, and code review are the job. That matches how I already build: deterministic C++ on a hard-deadline thread (zero-allocation `processBlock()`, lock-free UI-to-audio), and Python services held to a test bar (pytest CI, production Flask on EC2). I want a summer inside a development team that treats performance, code review, and SDLC as the default, not a class project.

---

## "Tell us about relevant technical experience." (≈120 words)

- **C++ / high-performance systems:** Granular synthesizer in C++/JUCE — `MemoryPool<Grain, 64>` so `processBlock()` never heap-allocates after `prepareToPlay()`; lock-free SPSC FIFO (atomic acquire/release) for UI-to-audio; CMake VST3/AU builds audited for zero allocations and zero locks.
- **Debug / optimize existing code:** Voice-AI co-op — Web Worker off the UI thread, <5ms main-thread blocking, 60 FPS; fault-tolerant RxJS that cut a 27% upload-failure rate.
- **Python delivery (JD-listed language):** Sole engineer on a 5-month contract — Flask REST API on AWS EC2 plus a Requests + Pandas ETL that removed ~800 hours of manual pulls across 400 PACs. SignalWeaver: async FastAPI at 9.1s p50 / 15.2s p99 across 90 runs, Docker Compose + GitHub Actions pytest.
- **Team / SDLC:** Code-review-adjacent release gates (real-time safety checklist before binaries; pytest on every main push). I have not shipped Java/Ada; I ramp on typed/compiled languages from C++.

---

## "Tell us about a time you tested / integrated / reviewed software."

**SignalWeaver + Granular, honestly scoped:** I containerized SignalWeaver (FastAPI + Postgres/pgvector + nginx) and wired a GitHub Actions pipeline that builds the frontend, runs pytest, and builds the API image on every main push. On the C++ plugin I treated the audio callback as a safety-critical path: every `processBlock()` route is audited against a zero-allocation / zero-lock checklist before VST3/AU release builds. That is the closest analog I have to "code review + test plan before the artifact ships." I have not worked in Java or Ada on a defense codebase; I would ramp on the team's language and process.

---

## Availability

Summer 2027, exclusive onsite Tewksbury, MA. Returning to Michigan after the internship (graduation Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Lead with C++ real-time, not ML and not campaign-finance.** Open interviews with Granular (`processBlock`, MemoryPool, SPSC), then CaseStudyPrep concurrency and MDC shipping.
- **Never claim Java, C#, or Ada.** Honest C++ + Python beats a Skills-line lie.
- **Unix/Linux:** not on the resume and not in the inventory. If asked: I develop and deploy on Linux-class environments (AWS EC2, Docker) and macOS CMake builds; I have not done VxWorks/embedded RTOS. Do not invent a Linux homelab.
- **Clearance is a form knockout.** Answer citizenship yes; interim Secret is processed after offer.
- **Referral still helps.** C-tier RTX intern reqs are resume-first (`companies.md`: bottleneck = resume, ~20–25%).
