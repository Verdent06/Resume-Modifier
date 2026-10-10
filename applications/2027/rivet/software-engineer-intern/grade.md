# Intern, Software Engineering (Summer 2027) at Rivet Industries

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — enrolled UMich CS undergrad, Junior, Expected May 2028 (Summer 2027 = rising senior); U.S. citizen → U.S. Person; no class-year or clearance-in-hand knockout
- **Track:** robotics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ lock-free SPSC, zero-alloc `processBlock`, and a real-time safety audit sit on page 1 — the edge/hardware analog a Rivet screener can probe.
- On-device Silero VAD via ONNX (40% inference-cost cut), sub-5ms / 60 FPS, and a 27% upload-failure recovery back the edge-ML *interest* bar and debug-on-real-systems without inventing OpenCV.
- Binding ding: Experience still reads Voice-AI / campaign-finance / PE-sourcing; no cameras, IMUs, fusion, or evaluate-on-hardware story.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Lock-free SPSC, zero-alloc `processBlock`, and a real-time safety audit are the C++ analog, but none of the three bullets sizes callback latency, xruns, or CPU. *(out of rails: full 6-bullet pool has no allowlisted runtime impact metric; swap sets cannot invent one)*
- **minor** · `Vylet` · off-axis product — Header is a PE/search-fund lead-sourcing product at $1,500 MRR. Eval gates and a 79%→89% defect fix are real; a rushed ITS/AR skim still buckets GTM. *(out of rails: cannot rewrite the pool header; omit drops below min_entries)*
- **minor** · `SignalWeaver` · off-axis stack — FastAPI p50/p99 is shipped-systems proof, but the entry is a financial-research scorer wrapping MPNet sentiment. *(out of rails: entire pool is financial-research; FastAPI is the keep)*

### Misreads

- Granular without a latency number can read as hobby DSP rather than constraint-bound edge software.
- Vylet's founder/PE tagline can bucket the resume as agentic GTM rather than defense hardware.
- SignalWeaver's MPNet/financial-research line can bucket the page as leftover fintech/ML rather than ITS/edge.

### Interview angles

- **Lead with:** Granular — lock-free SPSC (atomic acquire/release, no mutex on the audio thread), zero-alloc `MemoryPool` / `processBlock`, CMake/real-time safety audit; CaseStudyPrep on-device ONNX VAD, 27% upload recovery, Web Worker / sub-5ms / 60 FPS; MDC Flask REST on EC2 as delivery proof
- **Defend:** No cameras / IMUs / OpenCV / ROS / C# / CUDA / HoloLens / IVAS / clearance-in-hand *(out of rails: pool has none; MatchStream is banned)* — say so, then map to on-device inference and audio-thread constraints. Granular has no xrun/latency/CPU metric *(out of rails: pool has none)*. Vylet header is PE/GTM *(out of rails: cannot rewrite)* — pivot to eval gates and the 79%→89% defect fix. SignalWeaver is financial-research *(out of rails: entire pool)* — pivot to FastAPI instrumentation as shipped systems.
- **Depth prep:** C++ atomics / memory ordering / lock-free SPSC and why `processBlock` cannot allocate or lock; ONNX Runtime on-device vs cloud Whisper; honest "evaluate on hardware" gap. Intern OA unpublished — do not assume HackerRank/CodeSignal. Peer loop is a C++/systems project walk **[directional]**. Behavioral is a filter (`recruiting.md` §6). Confirm San Jose 40h/wk Summer 2027 and U.S. Person on Ashby.

## Likelihood

- **Resume screen:** Medium — C++ through use plus on-device ONNX clear the language and edge-ML-interest floor; Experience still leads Voice-AI / PAC ETL / PE with no sensor-fusion nouns
- **Overall hire odds:** Medium — B-tier Ashby resume-then-unpublished C++/systems walk (~5–8% directional, `companies.md` Rivet). Eligible U.S. citizen, Expected May 2028, San Jose onsite. No perception/CV stack to defend if the loop asks how you evaluated on hardware; live C++ still has to land
- **Funnel filters:** Ashby resume + U.S. Person / San Jose-relocate Booleans → unpublished intern loop · no HackerRank/CodeSignal · light intern sys design unpublished · Bottleneck: **resume** · U.S. Person (citizen / LPR / 8 U.S.C. 1324b(a)(3))
- **Outside the resume:** Apply in the first wave (posted 2026-10-06, deadline null); answer U.S. Person and San Jose relocate honestly; form email `verdent06@gmail.com`; prep the Granular audio-thread walk plus an honest hardware-gap map
