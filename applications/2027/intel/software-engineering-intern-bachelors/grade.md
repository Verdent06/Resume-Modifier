# Software Engineering - Intern, Bachelor's at Intel

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 B.S. CS; Summer/Spring 2027 intern term leaves Fall 2027–Winter 2028 still enrolled. Bachelor's STEM + 3+ months technical experience met. Role is not eligible for employment-based visa sponsorship; candidate needs none. On-site OK (not Colorado).
- **Track:** full-stack + semiconductor / silicon-adjacent systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a shipped Python ETL + Flask REST API on EC2 (~800 hours saved across 400 PACs) — applications / cloud / middleware routing is obvious.
- Granular sits second: C++ zero-alloc MemoryPool, lock-free SPSC FIFO, processBlock real-time audit — the chip-company systems differentiator, not a firmware or RTL internship.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc slab, lock-free SPSC, and a processBlock audit are the C++ signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than systems software next to silicon — a skim may underrate the C++ memory/concurrency evidence this catch-all uses to route tools / system software / validation.

### Interview angles

- **Lead with:** MDC sole-owned Flask REST + Requests/Pandas ETL (apps / data-system delivery); Granular C++ MemoryPool / lock-free SPSC / real-time checklist (silicon-adjacent systems — performance and debug, not firmware); CaseStudyPrep 27% upload-failure recovery plus <5ms / 60 FPS (debug + real-time); Vylet 79%→89% name-collision fix (validation)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. SYCL, oneAPI, OpenVINO, CUDA, Verilog, RTL, and firmware internships are not in the inventory — do not add them; say you would ramp on the team's platform stack. Linux is not a named skill — develop-on-macOS, ramp-on-Linux is the honest line. If they route firmware/GPU kernels, pivot to C++ real-time constraints honestly: plugin DSP, not device firmware.
- **Depth prep:** lock-free atomics, C++ memory/hot-path rules, Easy–Med HackerRank (`companies.md` bottleneck: resume, then OA); one STAR ship/debug story (CaseStudyPrep S3 URL recovery or Vylet 79%→89%); a one-minute why-Intel answer (software that enables products/platforms, not a generic web intern seat)

## Likelihood

- **Resume screen:** High — Python ETL/API ownership leads, C++ systems sits second, debug and automation show in bullets, Expected May 2028 and GPA 3.66 are visible, one page, and resume is the doctrine bottleneck
- **Overall hire odds:** Medium — B-tier catch-all, 2–3 Easy–Med rounds, HackerRank, ~5–8%, bottleneck: resume then OA; the page clears the generic SWE screen, but the live loop still has to hear DS&A plus a lock-free C++ defense, and firmware/oneAPI are honestly absent
- **Funnel filters:** Workday resume screen → HackerRank Easy–Med → 2–3 rds, no intern sys design (`companies.md`); on-site Hillsboro OR / Phoenix AZ / Folsom CA / Santa Clara CA / Austin TX (not Colorado); currently pursuing Bachelor's STEM; no employment-based visa sponsorship
- **Outside the resume:** Apply in the first Workday wave (posted 2026-09-02); an Intel/UMich alumni referral (HM > recruiter > engineer); rehearse Easy–Med HackerRank and the synth's memory/concurrency trade-offs; intern behavioral is a filter round (`recruiting.md`)
