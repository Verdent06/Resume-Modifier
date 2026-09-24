# Software Engineering Co-op (Signal Processing) at Sonos, Inc.

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — enrolled CS (Expected May 2028); Jan–June 2027 co-op = Junior, still enrolled; U.S. citizen / authorized for any US employer; no class-year gate on the JD
- **Track:** full-stack + consumer-audio / DSP / embedded-adjacent
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Granular leads: C++/JUCE MemoryPool plus a fractional-accumulator granular engine — musical DSP and real-time allocation, not a SaaS page.
- CaseStudyPrep is a titled Voice AI co-op (on-device Silero VAD, 40% inference-cost cut, S3 recovery, Web Worker 5ms / 60 FPS), then MDC Flask and Vylet Docker as the shipped-tools spine; SignalWeaver FastAPI is sized (9.1s p50 / 15.2s p99).
- Binding ding: Granular never sizes the DSP win (no callback latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc MemoryPool and the grain scheduler are the musical-DSP signal, but neither bullet sizes an outcome (callback latency, xruns, CPU)

### Misreads

- Granular without a number can read as hobby plugin rather than product DSP — a skim may underrate the real-time / musical-application evidence this co-op prefers.

### Interview angles

- **Lead with:** Granular — zero-alloc `processBlock`, fractional-accumulator grain engine, Gaussian LUT / musical DSP; CaseStudyPrep Silero VAD (40% inference-cost cut) and 27% S3 upload-failure recovery; MDC Flask-on-EC2 as the internal-tooling analog
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Linux, dev boards, Java/Spring, MATLAB, and ROS are not on the page — do not invent them; the JD treats boards as exposure and CI as learn-on-the-job. Boston 4-day onsite with no housing is a life question, not a resume line.
- **Depth prep:** real-time audio-thread rules (alloc, locks, SPSC), granular synthesis / filtering-aliasing vocabulary, ONNX VAD vs cloud ASR; Easy–Med DS&A if a live coding screen appears (`company.md`: OA unpublished; bottleneck resume)

## Likelihood

- **Resume screen:** High — musical DSP leads on a Signal Processing co-op page, titled voice-AI co-op and sized APIs sit behind it, Expected May 2028 and GPA 3.66 are visible, one page
- **Overall hire odds:** Medium — C-tier mid-size Workday funnel, resume is the published bottleneck, OA unpublished. Boston 4-day onsite with no housing is a life filter the PDF cannot clear, and the loop still has to hear DSP plus Easy–Med coding live
- **Funnel filters:** Workday ATS + human (`includeResumeParsing`) · OA unpublished · recruiter + Easy–Med tech **[directional]** · Behavioral filter · Bottleneck: resume · C-tier ~15–20% **[directional, Harman audio peer]** · work-auth / no-sponsorship; Boston min 4 days/week; Jan–June 2027
- **Outside the resume:** Apply in the first wave (posted 2026-09-23); a Boston-office or UMich-alumni referral (HM > recruiter > engineer); prep commute/housing honesty and walkthroughs of the granular engine plus VAD — behavioral is a filter, not the differentiator
