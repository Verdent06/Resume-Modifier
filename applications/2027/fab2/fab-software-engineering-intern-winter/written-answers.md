# Fab2 — Fab Software Engineering Intern - Winter (2027) · Written Application Answers

Draft answers for Ashby `0c4dc4f4-01c9-4138-a666-e7234cda7e95`. Grounded in `persona.md` (full-stack spine + software-defined-fab / hardware-adjacent process-control differentiator) and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Rust, Go, Protobuf, CRDTs, KiCad, Blender, Figma-as-skill, firmware, RTL, Snowflake, Databricks, Copilot, Fusion, Tableau, React Native, ROS/ROS2, Java, or any fab-equipment internship. TypeScript is the JD language path (`Rust and Go or Typescript`).

Apply: https://jobs.ashbyhq.com/fab2/0c4dc4f4-01c9-4138-a666-e7234cda7e95/application
Resume: `applications/2027/fab2/fab-software-engineering-intern-winter/Vedant Desai Resume.pdf`

**Pulled from the live Ashby form (2026-08-31):** fab2 · Fab Software Engineering Intern - Winter · Austin or San Francisco · in-office · January start · preferred 4–8 months · $114K–$131K annualized hourly + housing stipend. Portfolio is required.

Email on this packet is **verdent06@gmail.com** only. Never vedantde@umich.edu.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact labels on the Ashby application. `*` = required on the form.

| Field | Answer |
| --- | --- |
| Name * | Vedant Desai |
| Email * | verdent06@gmail.com |
| Resume * | `applications/2027/fab2/fab-software-engineering-intern-winter/Vedant Desai Resume.pdf` |
| Autofill from resume | Optional. Upload this PDF if you use it. |
| Portfolio - File upload | Not required if the website link is filled. Skip the file unless you want a PDF of GitHub. |
| Portfolio - website link * | https://github.com/Verdent06 |
| Have you included a portfolio with your application? * | **Yes** |
| Location * | **San Francisco, CA** or **Austin, TX** — both are in-office on the JD. Pick the office you will actually relocate to. Do not skip. |
| Tell us a bit about yourself and why you'd like to join fab2 | Paste the short answer below. |
| Ideal start date in office * | **2027-01-04** (first Monday in January). This is an in-office position. |
| Ideal end date * | **2027-08-28** (8 months — matches the JD preferred 4–8 month window). Winter-only fallback: **2027-05-01** (4 months). Either way you return to Michigan Fall 2027 (Expected May 2028). The form note says San Francisco for end date; still pick the same office as Location. |
| Are you currently authorized to work in the United States? * | **Yes** |
| Will you, at any point, require employer sponsorship to work in the United States? * | **No** — US citizen. JD lists visa sponsorship as a benefit; you still answer No because you do not need it. |
| How did you hear about us? * | Do **not** invent Referral or Sam's Youtube. If you found the Ashby/Built In posting online: **LinkedIn** or **Google Search** or **Indeed or other search engine**. If none of those is true: **Other**. |
| I am one of the following: (a) a citizen of the United States; (b) a lawful permanent resident of the United States; or (c) a person admitted into the United States as an asylee or refugee * | **Yes** — US citizen. |
| If no, is your home country listed below? * | Skip / **No** — you answered Yes above. Do not pick a listed country. |

Voluntary EEO: skip unless required (`recruiting.md` Part I §2).

School / degree if a recruiter asks (not on this form): University of Michigan · B.S. Computer Science and Economics · GPA 3.66 / 4.0 · Expected May 2028.

Phone / LinkedIn if a later step asks: (248) 704-4852 · https://linkedin.com/in/vedantde06

---

## Portfolio (required)

Ashby requires a file **and/or** a website link. Use the website link:

**https://github.com/Verdent06**

Repos that match this resume (do not invent others):

- https://github.com/Verdent06/granular-synth — C++/JUCE real-time engine (memory / concurrency / zero-alloc hot path)
- https://github.com/Verdent06/SignalWeaver — React/TypeScript dashboard + Postgres

"Have you included a portfolio with your application?" → **Yes**.

---

## "Tell us a bit about yourself and why you'd like to join fab2"

I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I want the winter Fab intern seat writing full-stack tools other engineers use to run a software-defined fab — frontend + backend data apps, sequencing/control software, process-development data — and shipping in days or weeks, not a consumer CRUD rotation. I can be in-office in San Francisco or Austin starting 4 January 2027 for 4–8 months (I am targeting the 8-month window through late August and I return to Michigan afterward). I am a U.S. citizen and do not need sponsorship.

I interview in TypeScript, Python, and C++. I do not have Rust or Go; the posting's language path is Rust and Go or TypeScript, and TypeScript is the one I can defend.

What I would bring:

- **Data-driven apps that other people actually run.** At Michigan Data Consulting I was the sole engineer on a five-month Michigan Campaign Finance Network contract. I replaced ~2-hour manual committee pulls with a Requests + Pandas ETL (eliminating ~800 hours of work across 400 tracked PACs) and shipped a production Flask REST API on AWS EC2 into their public research workflow.
- **Systems fundamentals — memory, performance, concurrency — without pretending it is fab firmware.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock: a per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO with atomic acquire/release ordering, plus 16-voice polyphony with hot-loop division pulled out of `prepareToPlay()`. That is control-adjacent discipline, not an RTL or equipment internship. github.com/Verdent06/granular-synth
- **Frontend that has to stay up.** At CaseStudyPrep.AI I moved audio off the UI thread into a Web Worker (main-thread blocking under 5ms at 60 FPS) and closed a 27% upload-failure rate around expired S3 URLs with fault-tolerant RxJS. SignalWeaver is the React/TypeScript + Postgres dashboard: composite scores persisted for history views across 90 tickers. github.com/Verdent06/SignalWeaver

GitHub is the portfolio: github.com/Verdent06. I want to write the software that sequences and runs the fab, and I will ramp on Rust/Go rather than claim them.

---

## Notes for the applicant (not for submission)

- **Lead with MDC (shipped Flask/ETL) and Granular (C++ memory/concurrency).** CaseStudyPrep is the visualization + fault-tolerant frontend story. SignalWeaver is the TypeScript proof — one bullet on the page; walk the repo if they push.
- **Do not claim Rust or Go.** Honest TypeScript + Python + C++ beats a knockout lie. `persona.md`: TypeScript is the stated alternate path.
- **Granular has no latency/xrun/CPU number on the page.** If asked, walk MemoryPool, lock-free SPSC, and the `processBlock()` constraint. Do not invent a metric (`grade.md` out of rails).
- **Portfolio is a hard gate.** Submit GitHub. A resume without the repo fails the apply form.
- **Location is not a skip.** In-office Austin or SF. January start.
- **Sponsorship is a knockout.** US citizen; answer **No**. Export-control: **Yes** (US citizen).
- **Do not apply from this file automatically.**
