# Belvedere Trading — Software Engineer Intern (Summer 2027, Chicago) · Screening Answers

Drafted from `persona.md` + real experience only. No invented projects or metrics. Lever form: https://jobs.lever.co/belvederetrading/10746b3d-1760-4573-9b63-b93f5a5e4fc0/apply

---

## Knockout / form fields (answer factually)

- **Resume/CV:** `applications/2027/belvedere-trading/software-engineer-intern/Vedant Desai Resume.pdf`
- **Full name / email / phone:** Vedant Desai · vedantde@umich.edu · (248) 704-4852
- **LinkedIn:** https://linkedin.com/in/vedantde06
- **GitHub:** https://github.com/Verdent06
- **Current location:** Ann Arbor, MI
- **How did you learn about Belvedere Trading?** Other — Pitt CSC / Simplify GitHub internship list
- **Are you lawfully authorized to work in the United States?** [Answer honestly]
- **Will you need sponsorship at any point (including CPT and OPT)?** [Answer honestly]
- **If yes, what type?** [F-1 / CPT / OPT / H-1B — factual only]
- **What degree are you currently pursuing?** Bachelor Degree
- **Name of School:** University of Michigan
- **School Major:** Computer Science and Economics
- **Graduation date:** Spring 2028 (Expected May 2028 — this is the in-window option)
- **Start Date at Current School:** [Select the term that matches your actual UMich start]
- **What year did you graduate high school?** [Factual]
- **Are you able to perform the essential functions of the job, with or without a reasonable accommodation?** Yes
- **Do you currently have pending offers from other employers?** [Factual]
- **What date are you available to begin employment?** May 2027 (or June 2027 if the program start is later)
- **Your application will be reviewed for one position at a time…** Yes / I Understand
- **Willing to live in Chicago and attend fully in person Summer 2027?** Yes

---

## "Why do you want to work for Belvedere Trading?" (Lever required)

I want to build the software that makes a market-making firm competitive — low-latency, high-performance systems owned end to end, not a thin intern wrapper around someone else's stack. Belvedere's JD is that job: design, implement, and debug proprietary trading applications with full-time engineers, in a team that has been rewriting its own systems from the ground up.

That matches how I already work. I built a real-time C++ audio engine (JUCE) under a hard zero-allocation / lock-free constraint — a pre-allocated `MemoryPool` slab, a hand-rolled SPSC FIFO so the UI thread never blocks `processBlock()`, and a release audit that every hot-path stays heap- and lock-free before VST3/AU binaries ship. On a voice-AI co-op I moved audio off the UI thread to keep main-thread blocking under 5ms at 60 FPS. As the sole engineer on a five-month contract I shipped a production Flask REST API on AWS EC2 and an ETL that cut ~800 hours of manual PAC research. I also built SignalWeaver, a multi-signal financial research platform (FastAPI + pgvector) with measured p50/p99 latency — CS + Economics is the academic half of that interest; BTU can teach the trading half.

I want Chicago, onsite, Summer 2027, sitting with the people who run those systems.

---

## Short cover blurb (if a portal asks for one; Lever does not)

I'm a Computer Science & Economics junior at the University of Michigan who writes performance-sensitive software in C++ and Python. I shipped a real-time C++/JUCE engine under a zero-allocation, lock-free audio-thread constraint; a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract; and a financial-research service instrumented at 49ms p50 search and 9.1s p50 end-to-end scores. Belvedere's intern class builds low-latency proprietary trading systems with full-time engineers — that is the work I want to do in Chicago next summer.

---

## C# / Java gap — honest framing (if asked)

The JD names C++, C#, or Java. I have not shipped production C# or Java. I have shipped C++ under real-time constraints (lock-free SPSC, zero-allocation `processBlock()`, CMake release binaries) and Python in production (Flask/EC2, FastAPI). I would interview in C++ or Python and ramp C#/Java on the job if the desk uses them.
