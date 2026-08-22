# SpaceX — Spring 2027 Software Engineering Internship/Co-op · Written Application Answers

Greenhouse `8621756002`. Grounded in `persona.md` (full-stack spine + aerospace / real-time / mission-critical / embedded-adjacent differentiator), `grade.md` Interview angles, and real `context.md` inventory only. First-person, honest, defensible under "walk me through this."

**Do not invent:** C (as distinct from C++), C#, Java, ROS, flight/avionics internships, clearance, Starshield/gov work, Granular latency/xrun/CPU/user numbers, student-group memberships, SAT/ACT, citizenship.

Apply: https://job-boards.greenhouse.io/spacex/jobs/8621756002
Resume: `applications/2027/spacex/software-engineering-intern-spring/Vedant Desai Resume.pdf`

**Do not submit from this file.** Artifacts only; no website apply.

---

## Identity / attachments (fill if the form asks)

| Field | Answer |
| --- | --- |
| First Name | Vedant |
| Last Name | Desai |
| Preferred First Name | Vedant |
| Email | vedantde@umich.edu |
| Country | United States |
| Phone | (248) 704-4852 |
| Location (City) | Ann Arbor, MI (school city on the resume). Other 2027 apps use Northville, MI for mailing — do not invent a zip here. |
| Resume/CV | `applications/2027/spacex/software-engineering-intern-spring/Vedant Desai Resume.pdf` |
| Cover Letter | Optional — **leave blank.** The PDF is the screen (`persona.md` / `companies.md`: resume then HackerRank). |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Portfolio | https://github.com/Verdent06/granular-synth (highest-signal for this req). Extra if allowed: https://github.com/Verdent06/SignalWeaver and https://vyletdata.com. Combine extras into one zip; do not invent a portfolio PDF. |
| Education — School | University of Michigan |
| Education — Degree | Bachelor's |
| Education — Discipline | Computer Science (also Economics — pick CS if only one) |
| Education — End date | May 2028 |
| Education — Start date | **SKIP** — not in `context.md`. Do not invent Fall 2024. |
| GPA (Undergraduate) | **3.66** on a 4.0 scale (preferred bar is 3.5). |
| GPA (Graduate) | **Not Applicable** |
| GPA (Doctorate) | **Not Applicable** |
| SAT Score | **SKIP** / Did not take — not in `context.md`. Do not invent. |
| ACT Score | **SKIP** / Did not take — not in `context.md`. Do not invent. |
| Can you perform all of the essential functions of this role with or without reasonable accommodations? | **Yes** if that is true for you. Do not guess a disability status. |
| Are you legally authorized to work in the United States? | **SKIP — answer truthfully on the form.** `context.md` has no citizenship / sponsorship field. Other 2027 defense packets treat you as a U.S. citizen *if that is actually true*. If it is not, stop — ITAR is an auto-reject (`persona.md`). |
| Citizenship Status | Same honesty rule as above. ITAR options: U.S. citizen/national, LPR, refugee, asylee. Do not pick "Other" and invent a story. |
| Site / transportation | JD is Flexible — any SpaceX site; ≥12 weeks onsite. Prefer Hawthorne, Irvine, Palo Alto, or Redmond unless you actually have a car. Own transportation is required only for Brownsville, Cape Canaveral, and McGregor — **SKIP** that checkbox unless you can honestly say yes. |

Voluntary EEO / disability / veteran: decline or skip. Do not invent.

---

## Please provide a summary highlighting your top two exceptional academic and/or professional accomplishments. Ideally, the examples you share will be a reflection of your most highly technical accomplishments and demonstrate why you are a top candidate for SpaceX.

Two accomplishments only. Metrics below are from `context.md` — no Granular latency/xrun/CPU number exists, so none is claimed.

**1. Granular Synthesizer Plugin (C++ real-time systems).** I built a C++/JUCE audio engine whose `processBlock()` callback cannot allocate or take a lock — a missed deadline is a glitch, not a retry. UI and audio share state, so a mutex or heap allocation on the audio thread would break that constraint. I pre-allocated a `MemoryPool<Grain, 64>` slab per voice at startup so grain slots come off a free-list (`processBlock()` never calls `new`/`delete` after `prepareToPlay()`), and a 64-slot lock-free SPSC FIFO with atomic acquire/release so slider changes never block the callback; WAV handoff uses an atomic `shared_ptr` swap. I shipped VST3 and AU from one CMake codebase (macOS universal, arm64 + x86_64) after auditing every `processBlock()` path for zero heap allocations and zero lock acquisitions. github.com/Verdent06/granular-synth

**2. CaseStudyPrep.AI — Software Engineer Co-op, Voice AI (Dec 2025 – May 2026).** On a production voice product I closed a 27% audio-upload failure rate: expired S3 presigned URLs and Angular MIME rejection were dropping WAV files mid-session. I wrote fault-tolerant RxJS that detects expired URLs, regenerates them in-flight, and negotiates MIME types the client had silently rejected. Most Whisper frames were dead air, so I ran Silero VAD client-side via ONNX Runtime to filter silence before upload, cutting cloud inference cost 40%. I moved audio processing off the UI thread into a Web Worker with an async stream handoff, holding main-thread blocking under 5ms and the visualizer at 60 FPS during inference.

Those two are the SpaceX-shaped signal: software that has to hit a deadline, and production debug when a live system fails. I do not have an aerospace internship. I interview in C++ and Python.

---

## Please select the month you will be able to start your internship.

**January 2027.** JD: full-time onsite, minimum 12 consecutive weeks beginning January or March 2027. January is the pick (`persona.md` does not override). I remain enrolled after the term (Expected May 2028 — Fall 2027 and Winter 2028 remain).

---

## How much experience in C programming language do you have?

**None.** Inventory is C++, not C. Do not treat Granular as C.

If the dropdown is duration not level: **None** / 0 months.

---

## How much experience in C++ programming language do you have?

**Intermediate.** Evidence: Granular Synthesizer Plugin — lock-free SPSC FIFO, `MemoryPool<Grain, 64>`, atomics, JUCE `processBlock()` real-time constraint, CMake VST3/AU. Not a professional C++ job; not Advanced.

If the dropdown is duration: **SKIP months** — Granular has no dated range in `context.md`. Do not invent 6–12 months. Pick Intermediate (level) if that option exists; if only months exist and Intermediate is absent, pick the lowest bucket that is not None (do not invent a year count).

---

## How much experience in C# programming language do you have?

**None.** Not in `context.md`.

---

## How much experience in Java programming language do you have?

**None.** MatchStream / FRC Java is commented out of the canonical pool — do not claim it.

---

## How much experience in JavaScript (JS) programming language do you have?

**Intermediate.** Evidence: CaseStudyPrep.AI co-op (Angular, RxJS, Web Workers; Dec 2025 – May 2026) and SignalWeaver React/TypeScript frontend. Inventory language is TypeScript; do not list a separate JavaScript skill you cannot interview in beyond that Angular/TS work. Not Advanced.

If duration: CaseStudyPrep is a dated six-month co-op — **6–12 months** is honest for JS/TS product work; do not add extra years.

---

## How much experience in Python programming language do you have?

**Intermediate.** Evidence: production Flask REST API + Pandas ETL at MDC (Jan 2026 – May 2026, sole engineer, 5-month contract); Vylet Dockerized pipeline (May 2026 – Present); SignalWeaver FastAPI. Strongest language by volume. Not Advanced (no multi-year professional Python title).

If duration: MDC + Vylet is dated production use through present — **6–12 months** is the honest band. Do not claim 2+ years.

---

## SpaceX Program Preference

**1st preference: Starship (Vehicle).**

Resume fit is product/full-stack plus real-time C++ / systems (`persona.md`: do not collapse into a SpaceXAI ML narrative). Vehicle software — flight/ground systems next to hardware under operational constraints — is the honest analog to Granular + CaseStudyPrep. Aerospace experience is not required.

**Do not pick Starshield** as first preference — no clearance, no gov/intel internship, persona does not support it.

**Do not pick SpaceXAI** as first preference — Vylet/LangGraph is not the screen this req tests.

If the dropdown is family-level only (Vehicle / Starlink / Starshield / SpaceXAI): pick **Vehicle**. If Starship is not listed but Falcon or Dragon is, pick **Falcon** as the operational-vehicle fallback, then Starship in any free-text. **Starlink** is an acceptable 2nd if the form requires two; it is software-heavy constellation work, not the primary differentiator on this PDF.

---

## Please select your enrollment status.

**Currently enrolled undergraduate.** University of Michigan, B.S. Computer Science and Economics, **Expected May 2028**. Spring 2027 is junior-year spring. Returning to school after the internship (Fall 2027 and Winter 2028 remain).

If the form wants class year: **Junior**.

---

## How did you hear about this job?

**Other.** Specify: **Jobright.**

No SpaceX contact in `network.md` — do not invent a referral or employee name. If Jobright is a listed option, pick it directly.

---

## If other, please specify below.

**Jobright**

---

## SpaceX & SpaceXAI Employment History

If this field means **prior SpaceX / SpaceXAI internships or full-time**: **None / No.** Never employed by SpaceX or SpaceXAI.

If this field is a general work-history dump (internships and full-time, not SpaceX-only), list only real inventory:

1. **CaseStudyPrep.AI** — Software Engineer Co-op (Voice AI) — Dec 2025 – May 2026 — Remote
2. **Michigan Data Consulting (MDC)** — Data Engineer, Michigan Campaign Finance Network (contract) — Jan 2026 – May 2026 — Ann Arbor, MI
3. **Vylet** — Founder — May 2026 – Present — live product, vyletdata.com

Do not add Lyndbrook unless the form requires a complete employment history; it is real (`context.md`: Data Engineering Consultant, Feb 2026 – Apr 2026) but was not requested for this packet. Never list Granular or SignalWeaver as jobs.

---

## Are you a member of any of the following student groups?

**None / leave blank.**

Listed options (Amateur Radio Club, Autonomous Vehicles, Aero Club, Engineering Affinity Group, Hackathons, Hyperloop, Motorsport Competitions, Robotics Club, Rocket Club, Satellite Club, Other) are **not documented** as current memberships in `persona.md` or the active `context.md` pool. Do not check Robotics Club from commented-out FRC/MatchStream. Do not check Other and invent a group.

---

## Notes for the applicant (not for submission)

- Essay is Granular + CaseStudyPrep only (`grade.md` Lead with). Do not swap in Vylet LangGraph or SignalWeaver LoRA — those read as SpaceXAI-only ML (`persona.md` anti-pattern).
- Do not invent a Granular runtime metric. If they probe impact, narrate the safety checklist and what you would measure next.
- Language levels are Intermediate / None only. Do not upgrade C++ or Python to Advanced on the form.
- Cover letter optional — skip. PDF path above.
- Binding filters after apply: HackerRank Med–Hard, then 3–4 tech rounds (`companies.md` / `grade.md`). ITAR is the binary knockout on the form, not on the resume.
