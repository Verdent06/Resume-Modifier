# Software Engineering Summer Intern 2027 at GE HealthCare

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — CS major vs CS/SWE/BME; sophomore-year minimum vs after-sophomore / rising-junior Summer 2027 (Expected May 2028); GPA 3.66 vs 3.0; US citizen vs no-sponsorship US work-auth
- **Track:** full-stack + medical-device / surgery-imaging / regulated software quality
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python ETL + Flask REST API on EC2 (~800 hours saved across 400 PACs) — general-SWE / software-implementation routing is obvious.
- CaseStudyPrep sits second: 27% upload-failure recovery and <5ms / 60 FPS — test/debug in the top half. Vylet adds a named defect (79% → 89%); SignalWeaver carries pytest/GitHub Actions CI plus 49ms search.
- Binding ding: Granular never sizes the C++ systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc slab, lock-free SPSC, and a processBlock audit are the C++ signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than system-software discipline next to regulated imaging products — a skim may underrate the C++ memory/concurrency/V&V-adjacent evidence.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (software / data / cloud); CaseStudyPrep debug/perf (27% upload-failure recovery, <5ms / 60 FPS); Vylet name-collision root-cause (79% → 89%); Granular C++ MemoryPool / lock-free SPSC / processBlock real-time checklist (tools and correctness, not a C-arm); SignalWeaver pytest/CI + 49ms pgvector
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Do not claim surgery-imaging, Java, C-arm, Snowflake, Databricks, Tableau, Copilot, Fusion, or embedded-firmware internships. SQL is in Skills; Postgres shows on SignalWeaver — do not invent a SQL-heavy imaging internship.
- **Depth prep:** lock-free atomics, C++ memory/hot-path rules, test-framework vs defect-triage vs V&V vocabulary; two STAR debug stories (CaseStudyPrep S3 URL recovery; Vylet name-collision); recruiter screen is auth + SLC relocate; no standard intern OA on this packet — light technical on the video loop. Behavioral is a filter round (`recruiting.md`).

## Likelihood

- **Resume screen:** High — shipped Flask/AWS API, a named 27% failure debug, a 79→89% defect fix, pytest/CI plus 49ms search, and three C++ real-time bullets on one page; this intern funnel's front door is the PDF
- **Overall hire odds:** Medium — B-tier Surgery Imaging intern, 2–3 Easy–Med practical rounds, ~10–15%, bottleneck is the resume then a recruiter/HM walk-through. The page should clear the screen; the loop still filters on live debug/V&V stories and Salt Lake City relocate
- **Funnel filters:** Workday (`gehc` / GEHC_ExternalSite) resume → recruiter phone (auth, SLC relocate) → one video behavioral + light technical 30–60m; no standard intern OA; no intern system design; GPA 3.0; sophomore year minimum; US work-auth / no visa sponsorship now or later; relocation assistance Yes; posted 2026-09-21 (no `endDate`)
- **Outside the resume:** Apply in this first rolling wave. Form email **verdent06@gmail.com**. Rehearse two STAR debug stories and a one-minute why-Surgery-Imaging answer (software that has to be correct in an OR, not generic web). This packet is **not** EEDP Software intern (Waukesha; Java/C++/Python required)
