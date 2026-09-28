# Hermeus — Software Engineering Intern (HIL) Spring/Summer 2027 · Written Application Answers

Draft answers for Lever `d87ed913-affc-475e-b721-c5b5f11c3c7b`. Grounded in `persona.md` (robotics / Atlanta HIL — not LA Modeling & Simulation), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Raspberry Pi, Arduino, STM32, Julia, MATLAB, ROS/ROS2, MatchStream/FRC, flight-software internships, HIL benches, or Granular callback-latency / xrun / CPU numbers.

Apply: https://jobs.lever.co/hermeus/d87ed913-affc-475e-b721-c5b5f11c3c7b/apply
Resume: `applications/2027/hermeus/swe-intern-hil/Vedant Desai Resume.pdf`

**Pulled from the posting:** Hermeus · Software Engineering Intern (HIL) — Spring/Summer 2027 · Atlanta, GA, onsite · $25–$33/hour · Spring ~16 weeks (January–April) · Summer ~12 weeks (May–August).

This packet is **Atlanta HIL only**. Do not apply it to the Los Angeles Modeling & Simulation intern.

---

## Knockout / structured fields (fill exactly)

Questions below are the labels on the live Lever apply form. `*` = required.

| Field | Answer |
| --- | --- |
| Full name | Vedant Desai |
| Legal First Name * | Vedant |
| Legal Last Name * | Desai |
| Preferred First Name | Vedant |
| Nick Name | (leave blank unless you actually use one) |
| Email * | verdent06@gmail.com |
| Phone * | (248) 704-4852 |
| Resume/CV * | `applications/2027/hermeus/swe-intern-hil/Vedant Desai Resume.pdf` |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| School / degree (if asked) | University of Michigan · B.S. Computer Science and Economics · GPA 3.66 / 4.0 · Expected May 2028 · Junior |
| Are you legally authorized to work for any employer in the United States? * | **Yes** (US citizen) |
| Will you now or will you in the future require employment visa sponsorship? * | **No** |
| U.S. export compliance * | **U.S. person.** US citizen. Do **not** select Foreign person. |
| How did you hear about us? * | **Pick the true source.** Do not guess. Options: Company Website · LinkedIn · YouTube · X (formerly Twitter) · University – Career Services · Facebook · Glassdoor · Indeed · Built In · Event – Recruiting · Event – Industry · Referral · Recruiter Outreach · FSAE EV Competition 2026 · Aerospace Summer Games 2026 · Other |
| Spring 2027 availability (Jan–Apr, ~16 weeks) | **Check if you will actually be in Atlanta onsite for that term.** Honest if you can do Spring 2027. |
| Summer 2027 availability (May–Aug, ~12 weeks) | **Check if you will actually be in Atlanta onsite for that term.** Honest if you can do Summer 2027. Checking both is fine if both are true. |
| Have you completed your junior year of study (i.e., are you entering your senior year) or are you a graduate student? * | **No** — Junior; Expected May 2028. As of Sep 2026 junior year is in progress, not completed. Spring 2027 internship is during junior year; Summer 2027 sits between junior and senior. |
| Have you completed at least one previous internship? Please provide details. * | Paste the short answer below. |
| What about our mission excites you? * | Paste the short answer below. |
| Voluntary EEO / veteran / disability / demographic survey | Skip unless you want to answer (`recruiting.md` Part I §2). |

---

## "Have you completed at least one previous internship? Please provide details." * (textarea)

Yes. Software Engineer Co-op (Voice AI) at CaseStudyPrep.AI, Dec 2025–May 2026: I owned real-time audio on the client — cut a 27% upload-failure rate by regenerating expired S3 URLs mid-flight, moved processing off the UI thread (main-thread blocking under 5ms at 60 FPS), and ran Silero VAD on-device via ONNX Runtime so dead air never hit Whisper (40% inference-cost cut). I also shipped as the sole engineer on a Jan–May 2026 Michigan Data Consulting contract for the Michigan Campaign Finance Network (Requests/Pandas ETL across 400 PACs; production Flask REST API on AWS EC2). I have not interned in flight software or HIL; I have not used Raspberry Pi, Arduino, or STM32.

---

## "What about our mission excites you?" * (textarea)

Hermeus is trying to get high-Mach aircraft into the air by iterating hardware fast, not by waiting on a paper airplane. The Atlanta HIL intern job is the part of that I actually want: keep the benches that connect hardware to software models reliable, write the automated tests that catch flight-software regressions, and debug across signal / hardware / software when something does not match. Closest work I have is C++ that cannot allocate or take a lock on the audio thread (granular-synth: MemoryPool, lock-free SPSC, processBlock audit) and production debug when a pipeline fails (CaseStudyPrep 27% upload recovery; Vylet eval gates plus a 79%→89% qualification fix). I do not have Pi/Arduino/STM32 or a prior flight-software internship. I can be onsite in Atlanta for Spring 2027 and/or Summer 2027; UMich CS + Economics, Expected May 2028, GPA 3.66; U.S. citizen, no sponsorship.

---

## Notes for the applicant (not for submission)

- **Email on the PDF is `verdent06@gmail.com`.** Do not type `vedantde@umich.edu` into Lever.
- **Do not claim Raspberry Pi, Arduino, STM32, Julia, MATLAB, ROS, or HIL benches.** Honest map: C++ real-time constraints + Python scripts/tests + signal/failure debug.
- **This is Atlanta HIL, not LA Modeling & Simulation.** Do not mention trajectory codes, M&S, or Los Angeles in the mission answer.
- **Junior-year checkbox is No today** even if Summer 2027 is after junior year. Answer the question as of apply date.
- **Granular has no runtime metric on the page.** If asked, walk MemoryPool, lock-free SPSC, and the processBlock audit. Do not invent xrun/CPU numbers.
- **Funnel:** Lever human screen → recruiter 20–30 min → technical/role-based 30–60 min → final team 15–30 min. No documented OA. Prep the Granular first-principles walkthrough and an honest hardware-gap answer.
- **How did you hear:** pick what is actually true. Do not invent a referral or a campus event.
