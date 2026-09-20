# Tools Programmer Intern at Epic Games

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — enrolled CS (Expected May 2028); 2027 intern = Junior, still enrolled; U.S. citizen / authorized to work in Cary; no class-year gate on the JD
- **Track:** full-stack + Unreal Engine content-architecture tooling (packaging / distribution / streaming; editor toolchain; C++ tool systems)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Granular leads: C++/JUCE MemoryPool, lock-free SPSC, CMake VST3/AU bundles — Greenhouse C++-on-resume is obvious, and this is not a frontend intern page.
- Vylet and CaseStudyPrep carry tools/pipeline ownership and production-defect debugging (79%→89% qualification; VAD/S3 recovery), then MDC as a shipped Flask API.
- Binding ding: Granular never sizes the systems win (no callback latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc MemoryPool, lock-free SPSC, and a CMake/processBlock audit are the C++ tools signal, but none of the three bullets sizes an outcome (callback latency, dropped buffers, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than Content Architecture toolchain work — a skim may underrate the C++ memory/concurrency evidence this intern uses to pass the C++ knockout.

### Interview angles

- **Lead with:** Granular C++ — zero-alloc `processBlock`, lock-free SPSC FIFO, CMake VST3/AU packaging; Vylet Dockerized pipeline plus the 79%→89% name-collision defect; CaseStudyPrep Silero VAD (40% inference-cost cut) and 27% S3 upload-failure recovery
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Unreal Engine, C#, Perforce, Slate, Blueprints, and Windows-native tooling are not on the page — do not invent them; Unreal is a plus, not a filter. If they hear Angular in CaseStudyPrep, pivot to the S3/VAD debug, not the visualizer.
- **Depth prep:** lock-free atomics, C++ memory/hot-path rules, OOP class modeling (MemoryPool, SPSC); Medium DS&A (`companies.md` bottleneck: tech rounds; no standard OA); one STAR debug story (Vylet name-collision or CaseStudyPrep expired S3 URLs)

## Likelihood

- **Resume screen:** High — C++ leads on a Content Architecture tools page (plugin + CMake bundles), pipeline/debug sit behind it, Expected May 2028 and GPA 3.66 are visible, one page
- **Overall hire odds:** Medium — B-tier Epic, ~8–12%, no standard OA, bottleneck is Medium C++/OOP tech rounds. The PDF clears the Greenhouse C++ knockout and is not a frontend intern, but the loop still has to hear DS&A plus C++ memory/concurrency live, and Unreal is honestly absent
- **Funnel filters:** Greenhouse ATS + human (C++-on-resume knockout) · No standard OA (`companies.md`) · 3 rds Medium · No intern sys design · Bottleneck: tech rounds · ~8–12% · legally authorized to work in Cary; onsite; education_required
- **Outside the resume:** Apply in the first rolling wave (req first_published 2026-09-18); a Cary/Unreal or UMich-alumni referral (HM > recruiter > engineer); prep lock-free/OOP walkthroughs of the synth and Medium C++ DS&A — behavioral is a filter, not the differentiator
