# Fab Software Engineering Intern - Winter at Fab2

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Pursuing B.S. CS (Expected May 2028); January 2027 start is junior year; JD has no class-year gate; US citizen / export-control ok; returns to Michigan after (grad May 2028); no sponsorship needed
- **Track:** full-stack + software-defined semiconductor fab / hardware-adjacent process-control + fab data systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python ETL + Flask REST API on EC2 (~800 hours saved across 400 PACs) — fab-ops tooling / data-app routing is obvious.
- Granular sits second: C++ zero-alloc MemoryPool, lock-free SPSC FIFO, 16-voice hot-path discipline — the systems-fundamentals differentiator (memory, concurrency, real-time), not an invented firmware internship.
- Binding dings: Granular never sizes the systems win; TypeScript (the honest JD language path) is a single SignalWeaver closer.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc slab, lock-free SPSC, and 16-voice polyphony are the systems signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)
- **minor** · `SignalWeaver` · single bullet, TypeScript proof thin — The JD TypeScript path and React frontend live in one last-project line; 90 tickers does not size an engineering outcome

### Misreads

- Granular without a number can read as hobby DSP rather than control-adjacent systems software next to a fab.
- A skim that stops at MDC + C++ may bucket this as a Python/C++ intern and miss the TypeScript floor until the last project.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (frontend-adjacent data apps / backend to run a workflow); Granular C++ MemoryPool / lock-free SPSC / hot-path polyphony (memory, performance, concurrency); CaseStudyPrep Web Worker <5ms / 60 FPS visualizer plus 27% upload-failure recovery (visualization + fault-tolerant frontend); SignalWeaver React/TypeScript + Postgres (JD language path)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. TypeScript proof is one SignalWeaver line *(out of rails: adding FastAPI overflowed the page at 93% fill)* — walk the dashboard and GitHub; Angular/RxJS on CaseStudyPrep is the other TS-family story. Rust and Go are not in inventory — say TypeScript is the JD alternate and you would ramp. Do not claim firmware, RTL, KiCad, Protobuf, or CRDTs.
- **Depth prep:** lock-free atomics and C++ memory/hot-path rules; TypeScript/React + Flask/REST + Postgres; one STAR ship/debug story (CaseStudyPrep S3 URL recovery or Vylet 79%→89%); a one-minute why-Fab2 (software-defined fab, ship in days/weeks, GitHub is the portfolio)

## Likelihood

- **Resume screen:** High — MDC ships a Python ETL + Flask API, Granular puts memory/concurrency in slot two, TypeScript appears through use, GitHub is on the header, one page
- **Overall hire odds:** Medium — Ashby human-read at a tiny early-stage cohort with no named OA; the PDF clears full-stack + systems, but the live loop is a project/systems deep-dive and Rust/Go are absent (TypeScript is the stated alternate, still a thinner language story if the team is Rust-first)
- **Funnel filters:** Ashby resume + required GitHub/portfolio → recruiter screen → project/systems deep-dive (no named OA) → possible onsite/founders; export-control US-person; in-office Austin or SF; January start / 4–8 months; intern behavioral is a filter (`recruiting.md` §6; `company.md`)
- **Outside the resume:** Apply in the first wave with GitHub matching the page; rehearse lock-free/memory and the TypeScript dashboard trade-offs; intern behavioral is a filter — one STAR ship/debug story
