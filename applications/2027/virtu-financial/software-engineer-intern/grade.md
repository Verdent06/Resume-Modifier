# 2027 Internship - Software Engineer at Virtu Financial

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028; internship June 7–August 13 2027; JD wants rising juniors OR FT-ready Dec 2027–June 2028
- **Track:** full-stack (HFT / electronic market-making — proprietary low-latency trading systems flavor; no track divergence)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ real-time systems (Granular — lock-free SPSC, zero-allocation MemoryPool, processBlock() safety audit) plus Python production (MDC Flask/EC2, CaseStudyPrep sub-5ms / 60 FPS) clear a selective Virtu SWE screen.
- CS + Economics, SignalWeaver (49ms p50 financial-news search, 9.1s p50 research scores), and May 2028 class year surface genuine markets curiosity without fabricating a trading intern.
- Binding ding: Granular never lands a processBlock() callback latency, xrun, or CPU number — the C++ differentiator is design-dense but unsized.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · hot-path latency unmeasured — lock-free SPSC and MemoryPool never land a time; the CMake closer is a real-time safety audit (zero heap, zero locks), not callback latency, xrun, or CPU.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than trading-tech-adjacent real-time systems because the closer is a release/safety checklist, not a latency number.
- CaseStudyPrep’s “Voice AI” title plus ONNX/Whisper third bullet can still misfile the top of Experience as ML if the reader skips the sub-5ms / 60 FPS hook.

### Interview angles

- **Lead with:** Granular lock-free SPSC / zero-allocation MemoryPool / processBlock constraints; CaseStudyPrep sub-5ms main-thread and 60 FPS (frame as real-time systems, not Whisper); MDC sole-ownership production Flask/EC2 + 800-hour ETL; SignalWeaver 49ms p50 semantic search and 9.1s p50 research scores.
- **Defend:** Granular has no processBlock latency/CPU/xrun in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) as the ship gate, pivot measured latency to CaseStudyPrep *(out of rails: Granular hot-path timing — full 6-bullet pool is architecture/capacity/DSP/release-audit only)*. No Java in the live pool — interview in C++ or Python. No trading-desk internship — CS + Economics plus SignalWeaver is the honest markets story. Do not lead with LoRA/agent pipelines; this is the SWE intern track only.
- **Depth prep:** Timed DS&A in C++ (preferred) or Python until a medium is a ~20-minute solve; HackerRank OA is 5 questions / 75 min Easy–Med (arrays, loops, edge cases). HR phone: why Virtu / why SWE plus one quantitative brainteaser. Tech: project deep-dive (Granular threading/memory, CaseStudyPrep real-time path), probability, low-latency / systems questions.

## Likelihood

- **Resume screen:** High — C++ and Python are in bullets, production shipping has metrics, class year is in window; one minor dents polish, it does not flip the screen.
- **Overall hire odds:** Low — S-tier quant intern funnel (~1–2%); the resume buys the HackerRank invite, not the offer. Binding filters are the OA then HR brainteaser and 2–3 tech.
- **Funnel filters:** Greenhouse resume screen → HackerRank OA (5Q / 75min, Easy–Med) → HR phone + brainteaser → 2–3 tech (project deep-dive, probability, low-latency systems) · NYC or Austin onsite · rising junior or FT-ready Dec 2027–June 2028 · SWE track only (not QR/Strategist, Quant Trading, SRE, Trading Ops).
- **Outside the resume:** Timed C++/Python OA plus probability/brainteaser reps; apply in the first wave; no Java — interview in C++ or Python; do not check other intern tracks on the form.
