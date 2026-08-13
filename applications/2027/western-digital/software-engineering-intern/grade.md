# Summer 2027 Intern — Software Engineering at Western Digital (WD)

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is currently pursuing a Bachelor's in CS; Summer 2027 leaves Fall 2027 + Winter 2028 after the internship (WD FAQ: at least one term remaining). No class-year cap on this posting.
- **Track:** full-stack + storage / system software (hardware–software integration)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python ETL + Flask REST API on EC2 (~800 hours saved across 400 PACs) — Applications / Data Analytics routing is obvious.
- Granular sits second: C++ zero-alloc MemoryPool, lock-free SPSC FIFO, processBlock real-time audit — the storage-company systems differentiator, not an OS/compiler internship.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc slab, lock-free SPSC, and a processBlock audit are the C++ signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than system-software discipline next to storage hardware — a skim may underrate the C++ memory/concurrency evidence.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (Applications / Data Analytics); Granular C++ MemoryPool / lock-free SPSC / real-time checklist (System Tools adjacency — utilities and performance, not OS or compilers); CaseStudyPrep debug/perf (27% upload-failure recovery, <5ms / 60 FPS)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Linux is a JD plus and is not in the inventory *(out of rails: no Linux skill or bullet in the pool)* — do not add it; say you develop on macOS and would ramp on Linux. Do not claim OS, compiler, firmware, Java, or Go internships. If they route Firmware, pivot to C++ real-time constraints honestly: plugin DSP, not embedded firmware.
- **Depth prep:** lock-free atomics, C++ memory/hot-path rules, DS&A mediums for a possible HM coding round; one STAR ship/debug story (CaseStudyPrep S3 URL recovery or Vylet 79%→89% name-collision); a one-minute why-storage answer (data at AI scale, software that has to be correct next to hardware)

## Likelihood

- **Resume screen:** High — Python ETL/API ownership leads, C++ systems sits second, SQL and JS-family show in bullets, one page, and this US funnel has no standard OA so the PDF is the gate
- **Overall hire odds:** Medium — B-tier catch-all, 2–3 Easy–Med rounds, ~8–12%, bottleneck: resume; the page clears the screen, but the HM still has to hear DS&A plus a live lock-free C++ defense, and the posting does not guarantee a seat
- **Funnel filters:** SmartRecruiters resume screen → recruiter → hiring manager (official FAQ); no standard OA; no intern system design; anticipated close ~10/20/26; San Jose onsite; must remain enrolled after the internship
- **Outside the resume:** Apply in the first wave; a WD/storage or UMich alumni referral (HM > recruiter > engineer); rehearse the synth’s memory/concurrency trade-offs; intern behavioral is a filter round (`recruiting.md`)
