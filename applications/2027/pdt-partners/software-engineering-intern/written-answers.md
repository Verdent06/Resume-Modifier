# PDT Partners — Summer 2027 Software Engineering Intern · Screening Answers

Draft answers for PDT’s Greenhouse application (token 8077685, https://boards.greenhouse.io/embed/job_app?token=8077685). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented trading-desk internship, metrics, or GitHubs. Trim to each form’s length limit before submitting.

---

## Knockouts / facts

**Are you legally authorized to work in the United States?**
Yes.

**Do you require sponsorship for employment visa status?**
No.

**What is your anticipated graduation date?**
May 2028.

**Have you tutored or TA'd for any classes?**
No.

**If yes, please list what courses or subject areas you tutored/TA'd for**
— (leave blank)

**What is your undergraduate GPA?**
3.66

---

## What about quantitative finance appeals to you?

I like problems where the software has to be both correct and fast, and where being wrong is expensive. That is what I already practice: a C++ audio engine where `processBlock()` cannot allocate or take a lock, and Python pipelines that turn messy public filings into something a researcher can actually use. CS + Economics at Michigan (stats, micro, macro) is the academic half of that; the engineering half is lock-free C++ and production ETL/APIs. I do not have a trading-desk internship. I want a summer building the systems under the desk — financial data, real-time events, batch processing — next to senior developers, and to learn markets on the job the way PDT describes the intern program. PDT not running a QR intern track is a feature for me: I am applying as an engineer.

---

## Are you especially proud of any GitHub repositories or personal projects? We’d welcome links.

**Granular Synthesizer Plugin** (C++/JUCE) — https://github.com/Verdent06/granular-synth

Zero-allocation audio thread via a per-voice `MemoryPool<Grain, 64>` slab; hand-rolled SPSC FIFO so the UI never blocks `processBlock()`; CMake ships VST3/AU; every hot-path audited for heap and lock use before release. That is the systems sample I can walk line by line.

**Vylet** — vyletdata.com — live Python product ($1,500 MRR): a no-LLM consensus gate plus a name-collision bug that lifted qualification from 79% to 89%.

**SignalWeaver** (no public GitHub in my pool) — a financial-research assistant (not investment advice): FastAPI scores, pgvector news search, out-of-sample regression. I can walk the stack; I will not paste a fake repo.

---

## If you have any time constraints or competing offer deadlines you'd like to make us aware of, please list them here.

None right now. Available early June–mid August 2027 for the 10-week NYC onsite program. I return to Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Do not invent a trading-desk internship.** Fit is project match: Granular (C++ real-time) + MDC/Vylet (Python data/batch).
- **Do not invent a SignalWeaver GitHub.** Link granular-synth; walk SignalWeaver from memory if asked.
- **OA/coding is the real gate** after screen. Timed C++ and Python mediums. Resume polish will not hire you here (`recruiting.md`: quant funnel, CP + math heavy).
- **Listing window** reported ~July 30–August 30 2026; rolling, ~3-week feedback. Apply now.
- Apply URL: https://boards.greenhouse.io/embed/job_app?token=8077685
