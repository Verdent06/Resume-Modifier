# Hermeus — Software Engineering Intern (Modeling & Simulation) · Written Application Answers

Lever posting `445db430-6f81-41cf-847a-56a947afb936`, scraped 2026-09-02 from the live apply form (not the Atlanta HIL sibling). Grounded in `persona.md` (robotics / 6DOF SITL, Los Angeles), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Julia, MATLAB, 6DOF, SITL, Monte Carlo, flight-test data, ROS/Gazebo, MatchStream/FRC, Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Granular xrun/CPU/callback-latency numbers, MDC API traffic, clearance, or an aerospace internship.

Apply: https://jobs.lever.co/hermeus/445db430-6f81-41cf-847a-56a947afb936
Resume: `applications/2027/hermeus/swe-intern-modeling-sim/Vedant Desai Resume.pdf`

**This packet is Modeling & Simulation, Los Angeles only.** Do not submit the Atlanta Software Engineering Intern (HIL) posting with this PDF.

Intern application cap: **not found** on the JD page, the apply form, or https://www.hermeus.com/internships (checked 2026-09-02). Still treat this as one role: LA M&S.

---

## Knockout / structured fields (fill exactly)

`*` = required on the Lever form.

| Field | Answer |
| --- | --- |
| Resume/CV * | `applications/2027/hermeus/swe-intern-modeling-sim/Vedant Desai Resume.pdf` |
| Full name * | Vedant Desai |
| Email * | **verdent06@gmail.com** (never `vedantde@umich.edu` on this packet) |
| Phone * | (248) 704-4852 |
| Current location | Ann Arbor, MI (school). Mailing used on other 2027 apps: Northville, MI. Do not invent a zip. |
| Current company | University of Michigan. Vylet is a founded product (`May 2026 -- Present`), not an employer to claim as a company internship. |
| LinkedIn URL | https://linkedin.com/in/vedantde06 |
| Other website | https://github.com/Verdent06 |
| Legal First Name * | Vedant |
| Legal Last Name * | Desai |
| Preferred First Name | Vedant |
| Nick Name | leave blank |
| Are you legally authorized to work for any employer in the United States? * | **Yes** (U.S. citizen) |
| Will you now or will you in the future require employment visa sponsorship? * | **No** |
| U.S. export compliance status * | **U.S. person. This status includes U.S. citizens, U.S. nationals, lawful permanent residents (green card holders), and asylums and refugees with such status granted, not pending.** |
| How did you hear about us? * | Pick the **true** source. Do not invent Referral / Recruiter Outreach / FSAE / Aerospace Summer Games. If Jobright/aggregator: **Other** and name it in the Other box. |
| Other (hear-about) | Only if the radio is Other / not listed. |
| Which semester(s) are you interested in? | Check **Spring 2027** and/or **Summer 2027** as actually available. This JD is Spring (~16 wk, Jan–Apr) and Summer (~12 wk, May–Aug). Do **not** check Fall 2026 or Fall 2027 unless that is true. |
| Have you completed your junior year of study (i.e., are you entering your senior year) or are you a graduate student? * | **No** as of the apply date (Sep 2026). Standing: Junior, Expected May 2028. Junior year is 2026–27, so Spring 2027 is still junior year. Summer 2027 (May–Aug) is entering senior year — that is **not** the present-tense question. Do not mark Yes to clear a rising-senior filter. |
| Gender / Race / Veteran / Disability / What is your location? | Voluntary. Skip for volume (`recruiting.md` Part I §2) unless you want to answer. |

GPA if a recruiter asks (not a labeled Lever field): **3.66 / 4.0**. JD floor is 3.0.

---

## Have you completed at least one previous internship? Please provide details. * (textarea)

Yes. Two overlapping 2026 engagements, both titled software/data work — not aerospace.

**1. CaseStudyPrep.AI — Software Engineer Co-op (Voice AI), Dec 2025 – May 2026.** Production voice product. Closed a 27% audio-upload failure rate (expired S3 presigned URLs + Angular MIME rejection) with fault-tolerant RxJS. Ran Silero VAD client-side via ONNX Runtime so dead air never hit Whisper (cloud inference cost −40%). Moved audio off the UI thread into a Web Worker (main-thread blocking under 5ms, visualizer at 60 FPS).

**2. Michigan Data Consulting — Data Engineer for Michigan Campaign Finance Network, Jan 2026 – May 2026.** Sole engineer on a five-month nonprofit contract. Replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees, then shipped a Flask REST API on AWS EC2.

I have not interned on 6DOF, SITL, Julia, or flight-test validation. Closest systems analog is a C++/JUCE granular synthesizer whose `processBlock()` path cannot allocate or take a lock (MemoryPool slab, lock-free SPSC, real-time safety audit). github.com/Verdent06/granular-synth

---

## What about our mission excites you? * (textarea)

Hermeus is trying to get high-Mach unmanned aircraft into the air by iterating hardware on a short cycle (Quarterhorse), not by running a decade-scale paper program. The Modeling & Simulation intern seat is the software side of that: 6DOF Software-in-the-Loop, physics-informed models, Monte Carlo scale, and checking the sim against real flight data with Flight Software / HMI / Flight Sciences.

I do not have Julia and I have not written a vehicle 6DOF. What I do have is software that has to stay correct under a hard runtime constraint, plus first-principles coursework (Physics — Mechanics) and scientific-computing Python.

The page I would walk through: a C++ granular engine whose audio callback cannot heap-allocate or take a lock — fractional-accumulator scheduler, per-voice `MemoryPool<Grain, 64>`, lock-free SPSC UI-to-audio, CMake VST3/AU after a real-time safety audit. Then Pandas ETL that replaced ~800 hours of manual pulls across 400 PACs (MDC). I want the Los Angeles M&S seat writing performant sim code, not the Atlanta HIL bench role, and I will ramp on Julia rather than claim it.

---

## Notes for the applicant (not for submission)

- **Do not claim Julia.** Not in inventory. Honest mapping: Python + C++ scientific/real-time (`persona.md`).
- **Do not apply this PDF to the Atlanta HIL intern.** Different location, different stack (bench vs 6DOF SITL).
- **Junior-year radio is a possible knockout for Spring 2027.** Honest answer is No today. Summer 2027 is the term where standing matches "entering senior year."
- **Granular has no runtime metric.** Walk MemoryPool, lock-free SPSC, and the `processBlock` audit. Do not invent xrun/CPU.
- **Funnel (`company.md` / internships FAQ):** Lever resume screen → recruiter 20–30 min → technical/role 30–60 min → final team 15–30 min. No named OA.
- **Lead with (`grade.md`):** Granular scheduler / zero-alloc / SPSC; MDC Pandas; CSP silence-vs-audio as model-vs-measured analog. Defend no 6DOF/SITL (not in the live pool).
- Voluntary EEO / veteran / disability / "What is your location?": skip unless you want to answer.
