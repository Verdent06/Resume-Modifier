# Middleware Intern [Winter 2027] at Figure

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 1 emergency, 1 major, 2 minor)
- **Eligibility:** ineligible — Junior at Winter 2027; Expected May 2028 vs JD final-year / graduate-student / degree-by-end-of-2026-or-2027 window
- **Track:** robotics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Timing-sensitive C++ is on the page: lock-free SPSC FIFO, zero-alloc `processBlock`, ring buffer, real-time safety audit — the middleware analog a Platform Software screener wants.
- Python debug is visible (Vylet 79%→89% name-collision fix) plus CSP real-time recovery (27% upload, sub-5ms / 60 FPS).
- Binding ding: Expected May 2028 on a final-year / graduate-student posting, and Linux is never named.

### Demerits

- **emergency** · `resume` · class-year gate miss — Education prints Expected May 2028. This posting is written for final-year undergraduates or master's students and recent grads finishing by end of 2026 or 2027, plus a requirements line that says graduate student or recent graduate. A junior graduating May 2028 is an auto-reject before the C++ is read.
- **major** · `resume` · Linux absent — Strong understanding of Linux is a listed requirement for C++ on embedded Linux. The page never names Linux, embedded Linux, or any Unix environment — C++ is a macOS audio plugin and Python is AWS/Docker.
- **minor** · `Granular Synthesizer Plugin` · metric-free runtime — Leading with the lock-free SPSC FIFO makes the middleware analog unmissable, but MemoryPool, the ring buffer, and the CMake audit still size no callback latency, xruns, or CPU — a skim can file it as hobby DSP. *(out of rails: full 6-bullet pool has no allowlisted runtime impact metric)*
- **minor** · `Michigan Data Consulting (MDC)` · API bullet unquantified — The Flask REST API on AWS EC2 is the only shipped service-plus-cloud line and lands with no traffic, latency, or consumer metric; sole-engineer / 5-month scopes the role, not the system. *(out of rails: pool has no API traffic/latency number)*

### Misreads

- Expected May 2028 files as “wrong class” immediately; some ATS/human screens never reach Granular.
- Granular without a latency number can read as weekend DSP rather than lock-free middleware.
- No Linux token can file a macOS JUCE + Docker page as “not embedded.”
- MDC’s unquantified Flask/EC2 line can be bucketed as a class project on a VM.

### Interview angles

- **Lead with:** Granular lock-free SPSC (atomic acquire/release, no mutex on the audio thread), zero-alloc `MemoryPool` / `processBlock`, ring-buffer addressing; CaseStudyPrep failure recovery and sub-5ms UI-thread offload; Vylet 79%→89% as Python investigate-and-fix
- **Defend:** Honest junior / Expected May 2028 — do not claim final-year or graduate student *(out of rails: Education is fixed)*; Linux is not on the page — the C++ is a real-time macOS plugin, Docker is not a Linux claim *(out of rails: inventory and pool have no Linux bullet)*; Granular has no callback-latency / xrun number *(out of rails: pool has none)*; no Bazel, ROS, shared-memory OS primitives, or embedded Linux
- **Depth prep:** If a recruiter still advances: C++ atomics / memory ordering / lock-free SPSC, processBlock real-time constraints, Python debugging (Vylet defect); coding challenge is C++ or Python **[directional, Extern]** — vendor unpublished, do not assume HackerRank. Behavioral is a filter (`recruiting.md` §6). San Jose 5 days/week, ≥10 weeks Winter 2027.

## Likelihood

- **Resume screen:** Low — class-year gate on the education line plus no Linux; lock-free C++ is otherwise on-axis for this middleware seat
- **Overall hire odds:** Low — A-tier ~2–5% even for eligible seniors (`companies.md` Figure); this JD’s graduate/final-year filter is the first cut, then a C++/systems challenge. A strong lock-free walk does not reopen a class-year knockout.
- **Funnel filters:** Greenhouse resume (AI Talent Matching disclaimer) → recruiter → C++/Python coding challenge **[directional, Extern]** → 1–2 tech → leadership/HM. Intern OA vendor unpublished. Bottleneck: resume then C++/lock-free tech. Visa unstated on this posting (US citizen / no sponsorship). Class-year: fails as printed.
- **Outside the resume:** Apply 2026-10-09 only if Vedant accepts the auto-reject risk (`recruiting.md` §8 first wave; posting first published 2025-09-30, updated 2026-10-08). Honest form: not a graduate student, Expected May 2028, San Jose 5-day yes, 10 weeks yes. No Figure contact in `network.md`. Form email `verdent06@gmail.com`. Airtable `recjKJUon4RDPzoV2` stays In Progress until a human submits
