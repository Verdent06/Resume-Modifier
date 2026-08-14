# Software Engineering Intern – Summer 2027 at Medtronic

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is Spring 2028, inside the JD window (Winter 2027, Spring 2028, Winter 2028, Spring 2029). U.S. citizen; no sponsorship required.
- **Track:** full-stack + medical-device / healthcare technology / regulated software quality
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python ETL + Flask REST API on EC2 (~800 hours saved across 400 PACs) — software / cloud / data routing is obvious.
- Granular sits second: C++ zero-alloc MemoryPool, lock-free SPSC FIFO, processBlock real-time audit — the healthcare-device systems differentiator, not a fabricated medical-device or firmware internship.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc slab, lock-free SPSC, and a processBlock audit are the C++ signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than system-software discipline next to regulated products — a skim may underrate the C++ memory/concurrency evidence.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (software / data / cloud); Granular C++ MemoryPool / lock-free SPSC / real-time checklist (tools and correctness, not OS or firmware); CaseStudyPrep debug/perf (27% upload-failure recovery, <5ms / 60 FPS)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Do not claim medical-device, Java, C#, Swift, or embedded-firmware internships. If they route Firmware, pivot to C++ real-time constraints honestly: plugin DSP, not device firmware.
- **Depth prep:** lock-free atomics, C++ memory/hot-path rules; Aon SJT plus two STAR ship/debug stories (CaseStudyPrep S3 URL recovery; Vylet SQL freshness / 30x pipeline); a one-minute why-Medtronic answer (software that has to be correct next to patients, not generic web)

## Likelihood

- **Resume screen:** High — Python/C++/SQL/JS-family show in bullets, a shipped API and data pipeline lead, C++ real-time systems sit in the top half, one page; this intern funnel’s front door is the PDF, not a coding OA
- **Overall hire odds:** Medium — B-tier catch-all, 2–3 Easy rounds, ~10–15%, bottleneck: resume + Aon; the page should clear the screen, but Aon SJT is a real second filter, the catch-all does not guarantee a team, and the HM still has to hear a live project walkthrough
- **Funnel filters:** Workday resume screen → Aon situational judgment → recruiter phone → HM Zoom (STAR + light technical); no coding OA on the intern path; no intern system design; anticipated close ~16 Oct 2026; Fridley onsite (min 4 days/week); no intern sponsorship
- **Outside the resume:** Apply in the first rolling wave; a Medtronic/UMich alumni referral (HM > recruiter > engineer); rehearse the synth’s memory/concurrency trade-offs and Aon SJT; intern behavioral is a filter round (`recruiting.md`)
