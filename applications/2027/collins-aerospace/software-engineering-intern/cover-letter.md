# Collins Aerospace (RTX) — Software Engineering Intern (Summer 2027, Cedar Rapids IA) · Screening & Cover Answers

Req 01865875. Drafted from `persona.md` + real experience only. No invented projects or metrics. This is **not** the closed Huntsville req 01865160.

Answer the citizenship item **factually** — it is a hard binary knockout.

---

## Knockout items (answer factually in the application)

- **Are you a U.S. citizen?** [Answer honestly — only U.S. citizens are authorized to access information under this program/contract. If not a U.S. citizen, this req is not eligible regardless of fit.]
- **Currently enrolled, returning to school after the internship?** Yes — B.S. Computer Science & Economics, University of Michigan, Expected May 2028 (rising senior in Summer 2027).
- **Cumulative GPA / projected graduation (put on resume too):** 3.66 / 4.0; Expected May 2028.
- **Willing to work onsite in Cedar Rapids, IA for Summer 2027?** Yes.
- **Coding in Python, C/C++, or Java?** Yes — Python (production Flask/FastAPI) and C++ (real-time audio plugin with lock-free threading). Java is not a language I have shipped; I ramp on typed/compiled languages quickly.

---

## Short cover blurb (≈130 words)

I'm a Computer Science & Economics student at the University of Michigan who builds object-oriented, concurrent software — the pairing this CDU simulation internship names as preferred. I wrote a C++/JUCE granular synthesizer with a lock-free SPSC FIFO, per-voice pre-allocated memory pools, and a real-time safety audit so the audio thread never allocates or takes a lock after startup. On a voice-AI co-op I moved processing off the UI thread into a Web Worker, holding main-thread blocking under 5ms at 60 FPS. I also ship Python services: a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract, and FastAPI endpoints with measured p50/p99 latency. I want to apply that OOP and threading discipline to modeling CDU 7000 control pages for Collins' military helicopter programs in Cedar Rapids.

---

## "Why Collins / this role?" (≈90 words)

This team models and simulates CDU control pages for the CDU 7000 suite that flies on 160th SOAR, Marines, and Coast Guard helicopters. That is software with a real-time, object-oriented bar, not a generic CRUD internship. I already work that way: lock-free UI-to-audio delivery in C++, zero-allocation `processBlock()`, and production Python services under a mentor-style ownership model (sole engineer on a fixed-window contract). I want to learn Collins engineering processes and the avionics display stack by shipping a SEPP-demoable simulation, not by watching from the sidelines.

---

## "Describe relevant technical experience." (≈120 words)

- **Threaded / real-time C++:** Granular synthesizer in C++/JUCE — `MemoryPool<Grain, 64>` so `processBlock()` never heap-allocates after `prepareToPlay()`; lock-free SPSC FIFO (atomic acquire/release) for UI-to-audio; CMake VST3/AU builds audited for zero allocations and zero locks.
- **Concurrent production code:** Voice-AI co-op — Web Worker off the UI thread, <5ms main-thread blocking, 60 FPS visualizer; fault-tolerant RxJS that cut a 27% upload-failure rate.
- **Python OOP / delivery (JD's first-listed language):** Sole engineer on a 5-month contract — Flask REST API on AWS EC2 plus a Requests + Pandas ETL that removed ~800 hours of manual pulls across 400 PACs. SignalWeaver: async FastAPI at 9.1s p50 / 15.2s p99 across 90 runs.
- **Defect discipline:** Vylet — diagnosed a name-collision in ownership-verification logic; qualification rate 79% → 89% with no change in sourcing volume.

---

## Threading / OOP / Java gaps — honest framing (if asked)

**Granular has no xrun/latency/CPU number on the page.** I would measure callback latency, xruns, and CPU next; the constraint I actually enforced is zero heap allocations and zero locks on the audio thread after startup.

**Java:** I have not shipped production Java. I ship typed/compiled code in C++ (lock-free threading, custom memory pools, OOP class modeling) and TypeScript, plus Python services. Java is one language to ramp on; the OOP and threading habits transfer.

**Simulation/modeling:** I have not written avionics CDU pages. Closest analog is building a deterministic real-time engine (grain scheduler, voice stealing, delay ring buffer) and demonstrating it as a finished binary — the same "model it, then demo it" shape as SEPP.
