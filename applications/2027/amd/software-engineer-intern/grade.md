# 2027 Undergrad Software Engineer Intern/Co-op at AMD

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 B.S. CS at a US university; Summer 2027 intern term (May 24–Aug 13) is rising junior; still enrolled after. Role is not eligible for visa sponsorship; candidate needs none.
- **Track:** full-stack + semiconductor / CPU-adjacent systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python ETL + Flask REST API on EC2 (~800 hours saved across 400 PACs) — applications / SDLC routing is obvious.
- Granular sits second: C++ zero-alloc MemoryPool, lock-free SPSC FIFO, processBlock real-time audit — the chip-company systems differentiator, not an RTL or firmware internship.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc slab, lock-free SPSC, and a processBlock audit are the C++ signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than systems software next to CPUs — a skim may underrate the C++ memory/concurrency evidence this catch-all uses to route tools / platform software.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (apps / data-system delivery); Granular C++ MemoryPool / lock-free SPSC / real-time checklist (CPU-adjacent systems — performance and debug, not RTL); CaseStudyPrep 27% upload-failure recovery plus <5ms / 60 FPS (debug + real-time)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Azure, Java, Perl, PowerShell, Django/Rails/Spring Boot, MongoDB, MySQL, Perforce, and UML are not in the inventory — do not add them; say you would ramp on the team's stack. If they route embedded/microcontroller, pivot to C++ real-time constraints honestly: plugin DSP, not firmware or CPU-pipeline internships. Linux is a JD plus and is not a named skill — develop-on-macOS, ramp-on-Linux is the honest line.
- **Depth prep:** lock-free atomics, C++ memory/hot-path rules, DS&A mediums (`companies.md` bottleneck: tech rounds; no standard US intern OA); one STAR ship/debug story (CaseStudyPrep S3 URL recovery or Vylet 79%→89% name-collision); a one-minute why-AMD answer (CPU/GPU software next to silicon, not a generic web intern seat)

## Likelihood

- **Resume screen:** High — Python ETL/API ownership leads, C++ systems sits second, SQL and JS-family show in bullets, one page, and this US funnel has no standard OA so the PDF is the gate
- **Overall hire odds:** Medium — B-tier catch-all, 3–4 Medium rounds, ~5–8%, bottleneck: tech rounds; the page clears the generic SWE screen, but the live loop still has to hear DS&A plus a lock-free C++ defense, and Azure/Java/embedded-firmware are honestly absent
- **Funnel filters:** AMD careers resume screen → recruiter phone → hiring-team tech (Teams); no standard OA (`companies.md` / student FAQ); no intern sys design; San Jose or Santa Clara hybrid/onsite; US-university undergrad CE/EE/CS; no visa sponsorship
- **Outside the resume:** Apply in the first wave; an AMD/UMich alumni referral (HM > recruiter > engineer); rehearse the synth's memory/concurrency trade-offs and LC mediums; intern behavioral is a filter round (`recruiting.md`)
