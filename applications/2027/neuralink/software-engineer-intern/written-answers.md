# Neuralink — Software Engineer Intern, Implant · Written Application Answers

Draft answers for the Greenhouse Implant intern form. Grounded in `context.md`, `grade.md` Interview angles, and `persona.md`. First-person, honest, defensible under "walk me through this" — no invented C/Rust/firmware/medical-device work, no invented Granular latency/xrun/CPU/user numbers.

JD: 3–4 concise exceptional-ability examples, quantitative impact, problem / solution / result, action-word open, technical detail. **"Answering this question fully is the most important part of our interview process."**

Apply: https://job-boards.greenhouse.io/embed/job_app?for=neuralink&jr_id=6a06fecf9f57175bd581d0e4&token=6569018003

If the form only has three boxes, paste **1–3**. Example 4 (MDC) is the spare.

---

## Knockout / structured fields

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| School | University of Michigan |
| End date | May 2028 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| Additional link | https://github.com/Verdent06/granular-synth (also vyletdata.com if they allow one extra) |
| Resume/CV | `applications/2027/neuralink/software-engineer-intern/Vedant Desai Resume.pdf` |
| Prior intern / co-op? | **Yes** — CaseStudyPrep.AI Software Engineer Co-op (Voice AI), Dec 2025–May 2026 |
| Graduation year | **2028** |
| Authorized to work in the US? | Answer **truthfully**. `context.md` has no citizenship / sponsorship fields. |
| Will you require sponsorship? | Same — do not guess. |
| I understand this position is on-site | **Yes** |
| Able to relocate without intern relocation assistance? | **Yes** if you will actually self-fund Austin or South San Francisco. Do not say yes and then stall. |
| Intern season | The season the form is currently interviewing for (JD: that option is the live req). If Summer is listed: **Summer**. |
| Ideal start date in office | Align with the selected season (Summer 2027 → late May / early June 2027). |
| How did you hear about us? | **LinkedIn** unless you have a real employee name. No Neuralink contact in `network.md` — do not invent a referral. |
| Onsite location | Pick **one**. Austin, TX or South San Francisco, CA. Do not split the difference. |

---

## Exceptional-ability examples (paste)

### First example — Granular Synthesizer Plugin (C++ real-time constraint)

Built a C++/JUCE real-time audio engine whose `processBlock()` callback cannot allocate or take a lock — a missed deadline is an audible glitch, not a retry. UI and audio shared state, so a mutex or heap allocation on the audio thread would break that constraint. I pre-allocated a `MemoryPool<Grain, 64>` slab per voice at startup so grain slots come off a free-list (`processBlock()` never calls `new`/`delete` after `prepareToPlay()`), and a 64-slot lock-free SPSC FIFO with atomic acquire/release so slider changes and WAV buffers (`shared_ptr` swap) never block the callback. I shipped VST3/AU from one CMake codebase (macOS universal, arm64 + x86_64) after auditing every `processBlock()` path for zero heap allocations and zero lock acquisitions.

### Second example — CaseStudyPrep.AI (production reliability)

Eliminated a 27% audio-upload failure rate in a production voice-AI product where expired S3 presigned URLs and Angular MIME rejection were dropping WAV files mid-session. I built fault-tolerant RxJS logic that detects expired URLs, regenerates them in-flight, and negotiates MIME types the client had silently rejected. Most Whisper frames were dead air, so I ran Silero VAD client-side via ONNX Runtime to filter silence before upload, cutting cloud inference cost 40%. I moved audio processing off the UI thread into a Web Worker with an async stream handoff, holding main-thread blocking under 5ms and the visualizer at 60 FPS during inference.

### Third example — Vylet (verification / hard-fail gate)

Engineered a pure-Python verification gate (no LLM) after ownership-matching was incorrectly rejecting valid acquisition targets that shared a name with an unrelated business elsewhere. The problem was a research-grade heuristic pretending to be a production check: same-name is not same-entity. I rebuilt Node 3 as a triangulated 0–100 consensus score — fuzzy-matching the pipeline query, state business registry, and live website crawl in a three-way weakest-link check — then hard-failing on legal status, industry, geography, or independence before the threshold applies. The name-collision fix lifted lead-qualification from 79% to 89% with zero change in sourcing volume.

### Fourth example — Michigan Data Consulting (shipped production, sole owner)

Replaced ~2 hours of manual committee research — portal searches, irregular Excel exports, hand normalization — with a Requests + Pandas ETL that ingests filings directly, eliminating ~800 hours of pulls across 400 tracked PACs. As the sole engineer on a 5-month Michigan Campaign Finance Network contract, I shipped a production Flask REST API on AWS EC2 that wired ingested data and PAC rankings into the nonprofit's public research workflow. I scoped delivery directly with the stakeholder, from ingestion through REST on EC2, with no backend team to share infrastructure, API design, or deployment.

---

## Notes for the applicant (not for submission)

- **Do not claim C, Rust, firmware, implants, or safety-critical medical-device work.** C++ under a real-time constraint is the adjacent signal (`grade.md` Defend). If they ask languages: Python + C++; you will ramp on C/Rust on the team.
- **Do not invent a Granular metric.** The pool has no CPU / xrun / callback-latency / user number. If they probe impact, narrate the safety checklist and what you would measure (callback time vs buffer size, xruns under load) — do not fabricate the measurement.
- **Do not invent Granular dates.** Header is GitHub. If they ask when: say when you actually built it; do not put a fake range on the form.
- **Do not analogize so hard it sounds like you interned on an implant.** Verification gate ≠ design-control software; audio callback ≠ implant firmware. The mapping is *kind of engineering* (hard constraint, production vs research, shipped to users).
- **Essay is the binding gate** (`persona.md` / JD). A 9.0 PDF does not substitute for thin stories.
- **Referral:** none in `network.md`. A real Neuralink employee name beats LinkedIn; a fake name is a knockout.
- **Work-auth:** binary knockout (`recruiting.md` §1). Answer the form fields honestly; they are not resume lines.
