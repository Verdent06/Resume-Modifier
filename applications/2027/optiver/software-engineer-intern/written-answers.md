# Optiver — Software Engineer Intern (Summer 2027, Chicago) · Screening Answers

Draft answers for Optiver’s careers-portal application. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented projects, metrics, Java, or trading-desk internship. Trim to each form’s length limit. The live posting does not require a cover letter; paste the optional letter only if the form has a free-text box.

Apply: https://www.optiver.com/join-us/jobs/technology/chicago/software-engineer-intern-summer-2027-chicago/

---

## Knockouts / facts

**Are you legally authorized to work in the United States?**
Yes.

**Will you now or in the future require sponsorship for employment visa status?**
No. US citizen.

**What is your anticipated graduation date?**
May 2028.

**Degree / major**
B.S. in Computer Science and Economics, University of Michigan.

**Undergraduate GPA**
3.66 / 4.0

**Class standing at internship**
Junior standing or higher (Summer 2027 intern; Expected May 2028).

**Preferred location**
Chicago, IL (onsite). Available to relocate for the summer. Austin is a separate req — apply to one Optiver technology intern listing.

**Have you completed an online assessment or interviewed for a technology intern/grad role at any Optiver location in the past 8 months?**
No. (If this is ever yes, do not apply — 8-month cool-off.)

---

## Optional cover letter (only if the form has a box)

I want to write software that has to be both fast and correct, and that actually ships. Optiver’s SWE intern role is that job: production systems that improve performance, reliability, and scalability for a market maker, scoped to real desk needs, with a mentor who expects the code to last.

The work I already do sits on that axis. In C++, I built a granular synthesizer where `processBlock()` cannot allocate or take a lock — a per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO so the UI never blocks the audio thread. In Python, I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract, and I moved real-time audio off the UI thread so a visualizer stays at 60 FPS with under 5ms of main-thread blocking. I do not have a trading-desk internship. I do have CS + Economics, stats coursework, and a financial-research platform (SignalWeaver — research assistant, not investment advice) with measured p50/p99 on search and scoring. I want to spend a summer next to engineers and traders who treat microseconds and production correctness as the job.

---

## Why Optiver? / Why this internship?

I want to ship production software in an environment where performance and correctness are the product. Optiver is a technology-driven market maker: intern projects are real desk needs, code hits production, and the bar is C++/Python/Java plus CS fundamentals — not a sandbox. That matches how I already work: lock-free C++ under a real-time budget, and Python services that other people actually use. I am applying as a software engineer intern, not a trader or researcher. CS + Economics is why I am curious about how tech powers markets; the engineering is why I think I can contribute in ten weeks.

---

## Why software engineering, not quantitative trading or research?

I like constraints I can enforce in code: no heap on the audio thread, no mutex on `processBlock()`, a REST API that a nonprofit actually runs. That is SWE. I use math and markets as context (stats coursework, SignalWeaver’s out-of-sample regression and 49ms p50 search), not as the job I am applying for. Optiver posting a distinct SWE intern track is the point — I want to build the systems under the desk.

---

## What programming languages are you strongest in?

C++ and Python. C++ is where I have gone deepest on constraints (lock-free SPSC, custom slab allocation, no heap on the audio thread). Python is what I ship in production (Flask on EC2, FastAPI research endpoints, Pandas ETL). I can interview in either. I am not listing Java — I have not shipped it.

---

## Tell me about a challenging technical problem you solved.

When I started the granular synthesizer, I thought the hard part would be the DSP. It was the audio thread: once `processBlock()` is running you cannot allocate, you cannot take a lock, and you cannot wait on the UI. I pre-allocated a `MemoryPool<Grain, 64>` slab per voice so grain slots come off a free-list, and I built a 64-slot SPSC FIFO with atomic acquire/release so slider changes reach the audio thread without a mutex. None of that was a user-facing feature. All of it was the difference between a plugin that clicks and one I could ship as VST3/AU.

---

## GitHub / projects we should look at

**Granular Synthesizer Plugin** (C++/JUCE) — https://github.com/Verdent06/granular-synth

Zero-allocation audio thread via a per-voice `MemoryPool<Grain, 64>` slab; hand-rolled SPSC FIFO so the UI never blocks `processBlock()`. That is the systems sample I can walk line by line.

**SignalWeaver** has no public GitHub in my pool. I can walk FastAPI scores (9.1s p50 / 15.2s p99) and pgvector search (49ms p50) from the resume; I will not paste a fake repo.

---

## Location / availability

Available onsite in Chicago for Summer 2027. I return to Michigan after the internship (Expected May 2028). US citizen; no sponsorship.

---

## Notes for the applicant (not for submission)

- **Do not invent Java or a trading-desk internship.** Interview in C++ or Python.
- **Do not invent a SignalWeaver GitHub.** Link granular-synth.
- **OA is the real gate.** HackerRank: coding + CS MCQ (OS/networks/DS&A) + Zap-N. Timed C++/Python mediums until a medium is a ~20-minute solve. Resume polish will not hire you here (`recruiting.md`: intern OA; quant/HFT is CP + math heavy).
- **8-month cool-off:** do not start the OA unless this is the Optiver technology attempt you want to spend.
- **Apply now.** Req posted ~14 hours ago; rolling; first wave is smaller.
- Official base: $80,000 USD (JD). Housing/flights/commute covered.
