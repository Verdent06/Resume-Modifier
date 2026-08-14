# Software Engineer Intern (Summer 2027 – Chicago) at Optiver

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside the JD window (December 2027–June 2028); CS major; junior standing or higher at a Summer 2027 intern term
- **Track:** full-stack (HFT / market-making performance-reliability-scalability flavor; no track divergence)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- C++ real-time systems (Granular — zero-allocation audio thread, lock-free SPSC, O(1) ring buffer) plus Python production (MDC Flask/EC2, CaseStudyPrep sub-5ms / 60 FPS) clear a selective Chicago market-maker SWE screen.
- CS + Economics, SignalWeaver (49ms p50 financial-news search, 9.1s p50 research scores), and May 2028 class year surface genuine markets curiosity without fabricating a trading intern.
- Binding ding: Granular never lands a processBlock() callback latency, xrun, or CPU number — the C++ differentiator is design-dense but unsized.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · hot-path latency unmeasured — MemoryPool and lock-free SPSC never land a time; the ring-buffer closer sizes 131,072 samples / O(1) addressing plus zipper-noise, not callback latency, xrun, or CPU.

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than trading-tech-adjacent real-time systems because the closer is buffer capacity, not a latency number.
- CaseStudyPrep’s “Voice AI” title plus ONNX/Whisper middle bullet can still misfile the top of Experience as ML if the reader skips the sub-5ms / 60 FPS hook.

### Interview angles

- **Lead with:** Granular lock-free SPSC / zero-allocation MemoryPool / processBlock constraints; CaseStudyPrep sub-5ms main-thread and 60 FPS (frame as real-time systems, not Whisper); MDC sole-ownership production Flask/EC2 + 800-hour ETL; SignalWeaver 49ms p50 semantic search and 9.1s p50 research scores.
- **Defend:** Granular has no processBlock latency/CPU/xrun in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) as the ship gate, pivot measured latency to CaseStudyPrep *(out of rails: Granular hot-path timing — full 6-bullet pool is architecture/capacity/DSP/release-audit only)*. No Java in the live pool — interview in C++ or Python. No trading-desk internship — CS + Economics plus SignalWeaver is the honest markets story. Do not lead with LoRA/agent pipelines; “AI-enabled tools” on this JD is trading/developer tooling.
- **Depth prep:** Timed DS&A in C++ (preferred) or Python until a medium is a ~20-minute solve; OA also has CS-fundamentals MCQ (OS, networks, DS&A) and Zap-N / cognitive games; Super Day: implement a data structure, concurrency/memory, low-level systems, and a collaborative debugging story.

## Likelihood

- **Resume screen:** High — C++ and Python are in bullets, production shipping has metrics, class year is in window; one minor dents polish, it does not flip the screen.
- **Overall hire odds:** Low — S-tier quant intern funnel (~1–2%); the resume buys the HackerRank invite, not the offer. Binding filters are the multi-part OA then language-matched tech and Super Day.
- **Funnel filters:** Rolling apply → HackerRank OA (coding + CS MCQ + Zap-N) → recruiter behavioral → technical screen → Super Day (algorithms + low-level/systems + behavioral) · Chicago onsite · grad window Dec 2027–June 2028 · 8-month re-apply cool-off if an OA or interview was already completed at any Optiver location.
- **Outside the resume:** Timed C++/Python OA plus OS/networks drill; apply in the first wave (posted ~14 hours ago); warm referral if available; do not start an OA unless this is the Optiver technology attempt you want to spend the cool-off on.
