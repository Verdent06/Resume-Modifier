# Trillium — Software Engineer Intern (Summer 2027) · Screening / Cover-Letter Answers

Draft answers for Trillium's Greenhouse application (job id 5207089007, https://www.trlm.com/apply/5207089007). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented experience, metrics, or C#. Trim to each form's length limit before submitting.

---

## Cover letter / "Why Trillium?"

I'm applying for the Software Engineer Intern role on Trillium Labs because the job is writing high-performance software next to a trading desk — in-house systems for equities and options, not a generic fintech CRUD internship.

The work I can defend in an interview maps onto that: I built a real-time C++/JUCE audio engine with a pre-allocated `MemoryPool<Grain, 64>` so `processBlock()` never allocates after startup, a lock-free SPSC FIFO for UI-to-audio delivery, and a release audit that confirmed zero heap allocations and zero locks on the audio thread. That's the same constraint class as low-latency trading software — hot path, no jitter from the allocator or a mutex. Separately, SignalWeaver is a financial-research platform I built end-to-end: pgvector semantic search over news at 49ms p50 / 99ms p99, a regression combining fundamentals and sentiment, FastAPI/Postgres, Docker Compose, and GitHub Actions CI. I also shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract, and I founded Vylet, a live lead-sourcing product at $1,500 MRR.

I'm a CS + Economics student at Michigan (Expected May 2028, GPA 3.66), available for the NYC in-person Summer 2027 internship, and I return to school after. I do not have professional C# — my load-bearing languages are Python and C++.

---

## "Tell us about something you've built" / technical sample

**Granular Synthesizer Plugin** (C++/JUCE) — the systems sample:

- Zero-allocation audio thread via a per-voice slab allocator; `processBlock()` never calls `new`/`delete` after `prepareToPlay()`.
- Hand-rolled SPSC FIFO (64-slot, atomic acquire/release) so the UI never blocks the audio thread; WAV handoff via atomic `shared_ptr` swap.
- CMake ships VST3 and AU from one codebase (macOS universal); every `processBlock()` path audited for heap and lock use before release.

Code: github.com/Verdent06/granular-synth.

**SignalWeaver** — the financial data-analysis sample: pgvector search at 49ms p50 over 90 queries, composite scores on 90 tickers, Docker Compose + pytest CI. Not investment advice; it is a research assistant I can walk through layer by layer.

---

## "Why this internship / what do you want to learn?"

I want a summer inside a production trading-tech codebase: design, debug, integrate across systems, and take code review seriously. My C++ work has been real-time constraints in a plugin I own; my Python work has been shipped APIs and data pipelines. I want both under a Lead Software Architect next to people who care about correctness when the firm's capital is on the line.

---

## Availability / location / authorization

Yes — available May 2027 for the 12–13 week in-person internship in New York. University of Michigan, B.S. Computer Science and Economics, Expected May 2028; returning to school after the internship. Authorized to work in the US without visa sponsorship.

---

## Notes for the applicant (not for submission)

- **Do not claim C#.** JD lists Python, C++, and C# as "such as." Interview in Python and C++.
- **Lead conversations with Granular (C++ constraints) and SignalWeaver (financial data),** then MDC (shipped API) and Vylet (debug + production). Do not open with campaign-finance narrative — the screen already risks that misread.
- **Honest gap:** no market-data, execution, or matching-engine work. Analogize from real-time constraints and financial-data pipelines; do not invent a trading stack.
- **OA is the binding filter** at this peer set. Timed C++/Python mediums before the loop.
- Apply URL: https://www.trlm.com/apply/5207089007
