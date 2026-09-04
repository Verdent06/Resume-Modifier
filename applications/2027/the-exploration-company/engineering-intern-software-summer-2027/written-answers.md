# The Exploration Company — Summer 2027 Internship (Software) · Written Application Answers

Draft answers for Ashby posting **`86270058-8eec-4692-b49d-97ce59fd54ac`**. Grounded in `persona.md` (full-stack spine + aerospace / crewed-vehicle / mission-critical differentiator) and the live Ashby form. First-person, honest, defensible under "walk me through this."

**NOT the Spring 2027 Internship (Software) twin.** This is LA, onsite, Summer 2027 only (May–Aug).

Apply (do not submit from this agent): https://jobs.ashbyhq.com/the-exploration-company/86270058-8eec-4692-b49d-97ce59fd54ac/application

Resume: `applications/2027/the-exploration-company/engineering-intern-software-summer-2027/Vedant Desai Resume.pdf`

**SHA-256 (PDF):** `983368dd0c0f3206ec23164d930cad342f70e6c782164fe0a1876c1bef8225af`

**This agent did not submit.**

**Form-kit identity (use on Ashby — never `vedantde@umich.edu` on the form):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · US citizen, no sponsorship · GPA **3.66** · Expected **May 2028** (junior at internship) · Address **49032 Freestone Dr, Northville, MI 48168** · LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06 · SAT **1510** if asked · DOB **12/16/2006** if asked.

The resume PDF header still uses the school email from `context.md`. That is the document. The **form** uses verdent06@gmail.com.

**Do not invent:** MATLAB, Simulink, ROS, C (as distinct from C++), Java, Spring, GNC, DO-178, Nyx/Storm internships, flight software, CubeSat / Formula SAE / robotics competition teams, clearance, CUDA, Go, Kubernetes, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, or a Granular latency / xrun / CPU number. MatchStream is commented out of the pool — do not claim it.

---

## Knockout / structured fields (fill exactly)

Ashby section: **Tell us about yourself..** Every field below is required unless noted.

| Exact label | Required | Answer |
| --- | --- | --- |
| Full Name | * | Vedant Desai |
| Email | * | **verdent06@gmail.com** |
| Phone Number | * | **(248) 704-4852** — best number to reach you |
| Location | * | **Northville, Michigan, United States** (current). Internship site is Los Angeles — do not put LA as current city. |
| LinkedIn Profile | * | https://www.linkedin.com/in/vedantde06 |
| Education History | * | University of Michigan · B.S. Computer Science and Economics · **Expected May 2028** · currently enrolled · did **not** graduate. GPA 3.66 if the education widget asks. |
| Current GPA (Undergraduate) | * | **3.5 - 3.79** (3.66 / 4.0). Do **not** pick 3.8–4.0. |
| SAT Score | * | **1500 - 1600** (1510) |
| ACT Score | * | **Did Not Take / Not Applicable** |
| Resume | * | `applications/2027/the-exploration-company/engineering-intern-software-summer-2027/Vedant Desai Resume.pdf` |
| Do you have prior internship experience? | * | **Yes** (MDC 5-month contract; CaseStudyPrep.AI co-op; Lyndbrook consulting; Vylet founder) |
| Engineering Highlight Reel | * | Paste the two-accomplishment answer below |
| Engineering Portfolio | * | Upload the **same PDF** again if a second file is required. Do **not** invent a portfolio deck. GitHub is https://github.com/Verdent06 (granular-synth, SignalWeaver). |
| Please indicate any engineering, technical, or project-based student organizations, clubs, or competition teams you have been involved with | * | **None of the Above**. Do **not** check Robotics Team, Rocketry, CubeSat, Formula SAE, or Autonomous Systems. |
| Software/Computer Engineering Focus: Do you have 3+ months of hands-on software development experience through prior internships, research, project teams, or personal projects? | * | **Yes** |
| If selected for the internship, are you able to work full-time (40 hours per week) for a minimum of 12 consecutive weeks? | * | **Yes** |
| If selected for the internship, what would be your preferred start date? | * | **May 3, 2027** (JD: beginning May 2027; Summer 2027 only). Backup: May 17, 2027. Do **not** pick June 1 unless May is impossible. |
| If selected, will you be able to provide your own housing, relocation, and transportation to the internship site? | * | **Yes** — will relocate to Los Angeles. Housing and relocation are **not** provided. |
| Due to federal regulations (e.g., ITAR/EAR), applicants must be U.S. citizens or lawful permanent residents (e.g., current Green Card holders). Are you eligible? | * | **Yes** — U.S. citizen. No sponsorship now or later. |
| Interview Recording Consent | * | **Yes, I consent to be recorded** |
| Subject to receiving an offer from The Exploration Company, please confirm you are happy to complete the mandatory ZINC background check | * | **Yes** |

### Optional surveys (skip unless you want them)

| Field | Answer |
| --- | --- |
| Diversity Survey — Which of the following communities do you belong to? | Skip / **I prefer not to answer** (`recruiting.md`: fill required fields, keep volume high) |
| Future Contact Consent — Do you agree to allow TEC Federal to contact you about job opportunities for up to 2 years? | **I agree** |

No cover-letter field on this Ashby form. Do not invent one.

---

## Engineering Highlight Reel (paste)

**Prompt:** What are the two accomplishments that best showcase your technical expertise, impact, and potential? Outline your role, responsibilities, and individual ownership.

I would walk two pieces of work — production test/debug under a latency constraint, then C++ that cannot miss a real-time deadline.

**1. CaseStudyPrep.AI — Software Engineer Co-op (Voice AI), Dec 2025–May 2026.** I owned the client-side audio path. Uploads failed 27% of the time: expired S3 presigned URLs plus Angular silently rejecting WAV MIME types. I wrote fault-tolerant RxJS that regenerates URLs mid-flight and negotiates MIME types. I also moved audio processing off the UI thread into a Web Worker with an async stream handoff so main-thread blocking stayed under 5ms and the visualizer held 60 FPS during inference. Individual ownership: the audio pipeline and the defect, not a shared backend team.

**2. Granular synthesizer plugin — C++/JUCE (github.com/Verdent06/granular-synth).** I built a real-time audio engine whose `processBlock()` path cannot heap-allocate or take a lock after `prepareToPlay()`. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO (atomic acquire/release) keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit (zero heap, zero locks). Individual ownership: engine, threading, and release builds. I do not have a callback-latency / xrun / CPU number; I would measure those next.

I have not interned on Nyx, Storm, GNC, or flight software. I have shipped systems other people used, closed named defects, and written C++ under a hard real-time constraint — the intern job's design/test/debug/document loop. I can be onsite in Los Angeles for 12 weeks starting May 3, 2027, and I return to Michigan afterward (Expected May 2028).

---

## If they ask "Why TEC / why this internship?" (≈90 words)

I want a summer writing and debugging software next to hardware that has to work — crewed-vehicle development, not a generic CRUD rotation. TEC is building Nyx (reusable cargo, crew path) and Storm; the intern posting is design, test, debug, and document under a mentor on that program. Closest analog I have: CaseStudyPrep (27% upload-failure recovery, sub-5ms UI-thread offload) and C++ that cannot allocate on the audio thread. I have not shipped flight software, MATLAB, or ROS. I will ramp on the team's stack rather than claim it. Los Angeles, 12 weeks, May 2027; I return to school after.

---

## If they ask "Tell us about a project" (internships FAQ)

This is the interview. Lead with the most recent technical achievement, then Granular if they want systems depth (`persona.md` / `grade.md`).

**Most recent — Vylet (May 2026–present).** Live product. Dockerized LangGraph pipeline on Redis/Celery. Name-collision in ownership verification was rejecting valid targets; the fix lifted qualification **79% → 89%** with no change in sourcing volume. Pivot to the defect and workers, not the PE/search-fund story (`grade.md` Defend).

**CaseStudyPrep (operational debug / real-time).** 27% upload-failure recovery; Web Worker / <5ms / 60 FPS.

**Granular (systems constraint).** Zero-alloc `processBlock`, lock-free SPSC, real-time safety audit. No latency/xrun/CPU number on the page — say that and what you would measure.

Mission fluency they want: Nyx is a reusable orbital cargo capsule with a crewed path; Storm is the engine; TEC's pitch is democratizing space transportation. Do not pretend you worked on it.

---

## Availability

Summer 2027 only. Full-time 40 hours/week, **minimum 12 consecutive weeks beginning May 2027**, **onsite Los Angeles**. Preferred start **May 3, 2027**. Returning to the University of Michigan after the internship (Expected May 2028). GPA 3.66. Will provide own housing, relocation, and transportation.

---

## Notes for the applicant (not for submission)

- **This is the Summer software intern, not Spring.** Confirm the URL id is `86270058-8eec-4692-b49d-97ce59fd54ac` before submit.
- **PDF email is school; form email is gmail.** Fix if Ashby parses `vedantde@umich.edu` from the PDF.
- **ITAR is a binary knockout.** You are a US citizen — answer Yes. If that were ever not true, stop.
- **Housing is on you.** JD Additional Requirements override the generic "relocation assistance" footer.
- **Do not check a competition team.** None of the Above is the honest option.
- **Do not claim MATLAB, ROS, GNC, Java, C, flight software, or a Granular runtime metric.**
- **Cover letter:** none on this form. The PDF is the screen (`companies.md`: bottleneck resume, ~15–25%). After that: walk the last technical project + Nyx fluency. No published OA.
- **Referral:** no TEC contact in `network.md`. Cold Ashby apply.
- **Do not apply from this file automatically.**
