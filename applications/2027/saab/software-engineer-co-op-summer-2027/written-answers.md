# Saab, Inc. — Software Engineering Co-Op (Summer 2027, East Syracuse / Collamer) · Cover letter & Workday answers

Req **R-03237** / posting **R-03237-1**. East Syracuse, NY (Collamer). Surveillance Software — air traffic management systems in use at airports. Drafted from `persona.md` + real inventory only. **Do not invent** Java, Linux homelab, Subversion, JUnit/GTest/JTest, clearance, ADS-B/multilateration/radar products, or Granular latency/xrun/CPU numbers.

Workday questionnaire endpoints returned HTTP 406 without an account (`questionnaireId` present). Labels below are JD knockouts + standard Workday fields. Trim to each form's length limit before submitting.

Apply: https://saabusa.wd1.myworkdayjobs.com/saab_careers/job/East-Syracuse-NY-Collamer/Software-Engineering-Co-Op--Summer-2027-_R-03237-1

Resume: `applications/2027/saab/software-engineer-co-op-summer-2027/Vedant Desai Resume.pdf`

**SHA-256:** `39865c92eb0289636a7c6f74cac8a612c9cd8365339a93f1908f69c8ed527f2a`

**Form kit (this apply only):** email **verdent06@gmail.com** — never `vedantde@umich.edu` on the Workday form. Resume PDF header still uses the umich address from `context.md`; that is expected. Phone **248-704-4852**. U.S. citizen, no sponsorship. GPA **3.66**. Expected **May 2028**. Class standing on forms: **Junior**. Address **49032 Freestone Dr, Northville, MI 48168**. LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06. SAT **1510** if asked. DOB **12/16/2006** if asked.

**Do not submit from this file.** Artifacts only.

School typeahead: see `company-notes.md` before filling Education.

---

## Knockout items (answer factually)

| JD / likely Workday label | Answer |
| --- | --- |
| Are you a U.S. citizen? / Citizenship | **Yes.** U.S. citizen. This req requires U.S. citizenship. |
| ITAR / U.S. person / export-control (if asked) | **Yes** — U.S. citizen. |
| Will you now or in the future require visa sponsorship? | **No** |
| Currently enrolled in CS / CE / SE? | **Yes** — B.S. Computer Science and Economics, University of Michigan. CS is the qualifying major. |
| Cumulative GPA 3.0 or better? | **Yes — 3.66 / 4.0** |
| Completed sophomore year or greater? | **Yes.** Expected May 2028. Summer 2027 after junior year. If the form asks class standing: **Junior**. |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain. Enrolled through the term. |
| Willing to work onsite East Syracuse, NY (Collamer) Summer 2027 (May–August)? | **Yes.** Relocate. Housing sign-on applies (Northville, MI is outside commuting distance). |
| Available Summer 2027 only (not Spring/Fall)? | **Yes — Summer 2027 only.** |
| Pre-employment drug screen (federal contractor) | Acknowledge. Condition of employment. |
| Existing security clearance? | **No.** Eligible as a U.S. citizen; do not claim a clearance you do not have. |
| Languages you can interview in | **C++, Python.** Also TypeScript/JavaScript (Angular), SQL, HTML/CSS. Do **not** check Java, Linux-as-skill, Subversion, JUnit, GTest. |

---

## Cover letter / additional information (≈160 words)

I am applying for the Software Engineering Co-Op at Saab, Inc. in East Syracuse (Collamer) for Summer 2027. I want to spend the summer writing object-oriented software for air traffic management systems that airports actually run — C++ and Python on a product team, with test and Git as the default, not a class project.

The work I can defend:

- **C++ under a hard constraint.** I built a real-time audio DSP plugin in C++/JUCE whose audio thread cannot allocate or take a lock: a `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering. CMake ships VST3/AU binaries only after every `processBlock()` path is audited for zero heap allocations and zero lock acquisitions. github.com/Verdent06/granular-synth
- **Python delivery.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2. SignalWeaver is async FastAPI with Docker Compose and GitHub Actions pytest on every main build.
- **UI / debug.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS on an Angular client and held main-thread blocking under 5ms with a Web Worker.

I have not shipped Java, JUnit/GTest, or Subversion, and I do not have a Linux homelab or an existing clearance. C++ and Python are the languages I can interview in. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), a U.S. citizen, and I will relocate onsite to East Syracuse for May–August 2027.

---

## "Why Saab / this co-op / Surveillance Software?" (≈90 words)

Saab's East Syracuse Surveillance Software team writes ATM systems used at airports — software that has to be correct next to live operations, not a generic web rotation. That matches how I already build: deterministic C++ on a hard-deadline thread (zero-allocation `processBlock()`, lock-free UI-to-audio, CMake release gates) and Python services held to a test bar (pytest CI, production Flask on EC2). I want a summer on that product, onsite in Collamer, and I return to Michigan afterward (Expected May 2028).

---

## "Tell us about relevant technical experience." (≈120 words)

- **C++ / OOD / concurrency / CMake:** Granular synthesizer — `MemoryPool<Grain, 64>` so `processBlock()` never heap-allocates after `prepareToPlay()`; lock-free SPSC FIFO for UI-to-audio; CMake VST3/AU builds audited for zero allocations and zero locks.
- **Python / scripting / SQL-adjacent delivery:** Sole engineer, 5-month MCFN contract — Flask REST on AWS EC2 plus Requests + Pandas ETL (~800 hours / 400 PACs). SignalWeaver: FastAPI at 9.1s p50 / 15.2s p99 across 90 runs; Postgres; GitHub Actions pytest.
- **JavaScript / HTML / CSS:** Angular client, Web Worker, <5ms main-thread blocking, 60 FPS; RxJS recovery of a 27% S3 upload-failure rate.
- **Git / unit test:** Git through use; pytest on every main push. I have not used Subversion, JUnit, GTest, or Java; I ramp on typed/compiled languages from C++.

---

## "Tell us about a time you tested / reviewed software."

SignalWeaver + Granular, honestly scoped: I containerized SignalWeaver (FastAPI + Postgres/pgvector + nginx) and wired GitHub Actions to build the frontend, run pytest, and build the API image on every main push. On the C++ plugin I treated the audio callback as a safety-critical path: every `processBlock()` route is audited against a zero-allocation / zero-lock checklist before VST3/AU release builds. That is the closest analog I have to "code review + test plan before the artifact ships." I have not shipped JUnit/GTest on an ATM codebase.

---

## Availability / location

Summer 2027 only, exclusive onsite East Syracuse, NY (Collamer), May–August. Willing to relocate from Northville, MI. Returning to Michigan after the internship (Expected May 2028). Ask for the housing sign-on if the form has a commuting-distance question.

---

## Notes for the applicant (not for submission)

- **Lead with C++ real-time and Python shipping, not ML and not campaign-finance.** Open with Granular (`processBlock`, MemoryPool, SPSC, CMake), then MDC Flask/EC2 and CaseStudyPrep Angular/debug (`grade.md` Interview angles).
- **Never claim Java, Linux-as-homelab, Subversion, JUnit/GTest, ADS-B, or a clearance.** Honest C++ + Python beats a Skills-line lie (`persona.md`).
- **Unix/Linux:** not on the resume and not in inventory. If asked: I develop and deploy on Linux-class environments (AWS EC2, Docker) and macOS CMake builds. Do not invent a homelab *(out of rails)*.
- **Citizenship / ITAR is a form knockout.** Answer **Yes** (U.S. citizen). Do not put citizenship on the PDF.
- **Location is not a skip.** East Syracuse onsite; relocate Yes.
- **Form email is verdent06@gmail.com.** Autofill will try `vedantde@umich.edu` — change it.
- **No Saab contact in `network.md`.** Do not invent a referral.
- **Resume is the intern bottleneck** (C-tier, Workday, ~20–25%). Apply in the first wave (posted 2026-09-03; open through 2027-01-01).
