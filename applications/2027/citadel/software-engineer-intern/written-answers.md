# Citadel — Software Engineer Intern (US) · Screening / Essay Answers

Draft answers for Citadel’s (hedge fund, citadel.com — **not** Citadel Securities) application, grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented experience or metrics, no trading-desk internship. Paste the essay into the required 150–300 word box; trim other answers to each form’s length limit.

---

## Required essay (150–300 words)

**Prompt:** In 150–300 words, share a story or experience that reflects who you are as a candidate. Possible topics: A challenge you've faced; A passion of yours; An achievement you're proud of.

When I started building a granular synthesizer from scratch in C++/JUCE, I thought the hard part would be the DSP. It wasn’t. The hard part was the audio thread: once `processBlock()` is running, you cannot allocate, you cannot take a lock, and you cannot wait on the UI. Break any of those and the plugin glitches in a way a unit test will not fully catch.

I spent weeks making that constraint hold. I pre-allocated a `MemoryPool<Grain, 64>` slab per voice at startup so grain slots come off a free-list instead of the heap — `processBlock()` never calls `new` or `delete` after `prepareToPlay()`. I built a 64-slot SPSC FIFO with atomic acquire/release so slider changes reach the audio thread without a mutex, and I handed WAV buffers across threads with an atomic `shared_ptr` swap so the UI never blocks playback. None of that was a user-facing feature. All of it was the difference between a plugin that clicks and one I could ship as VST3/AU.

That is the work I like: a hard constraint, a first design that fails it, and the engineering that makes the constraint hold. I use the same instinct on a financial research platform — serving composite scores through FastAPI at 9.1s p50 / 15.2s p99, and refusing to trust a return-prediction model until it was checked out-of-sample (3.39% R², consistent with the low single-digit R² of real return-prediction literature). I want to spend a summer around people who treat performance and statistical honesty as the job, not extra credit.

---

## "Why Citadel?" / "Why this internship?"

I want to write software that has to be both fast and correct. Citadel’s intern engineers build the tools that bring trading strategies to life and the high-performance, large-data research platforms those strategies run on — small teams, short cycles into production. The work I already do sits on that same axis: lock-free C++ under a real-time budget, and a research platform where I refused to trust an in-sample fit. I do not have a trading-desk internship; I do have CS + Economics, stats coursework, and a habit of sizing systems with numbers. That is the intern I would rather be than someone polishing a generic SWE page. This application is for Citadel the hedge fund, not Citadel Securities.

---

## "What programming languages are you strongest in?"

C++ and Python. C++ is where I have gone deepest on constraints (lock-free SPSC, custom slab allocation, no heap on the audio thread). Python is what I ship in production (Flask on EC2, FastAPI research endpoints, Pandas ETL). I can interview in either.

---

## Location / availability

Available for the 11-week summer program. I can work onsite in New York (preferred). Also open to Miami, Greenwich, or Houston if that’s where the team is. University of Michigan, B.S. Computer Science and Economics, Expected May 2028 — I return to school after the internship.

---

## Notes for the applicant (not for submission)

- **Essay word count:** check before paste; keep 150–300. Do not add metrics that are not on the resume or in `context.md`.
- **Do not invent a SignalWeaver GitHub** — it is not in the pool. If they ask for a link, send the granular-synth repo and walk SignalWeaver from the page.
- **Do not describe Citadel Securities market making.** This req is the hedge fund. You already applied to Citadel Securities separately.
- **OA is the real gate.** Timed HackerRank mediums until a medium is a ~20-minute solve; add probability/stats reps for the loop. Resume polish will not hire you here (`recruiting.md`: intern OA; quant/HFT is CP + math heavy, <1%).
- **Referral > cold apply**, and apply in the opening wave — quant opens earliest.
