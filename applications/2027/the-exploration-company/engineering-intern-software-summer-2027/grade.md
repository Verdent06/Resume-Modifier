# Summer 2027 Internship (Software) at The Exploration Company

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 + Summer 2027 (May–Aug) = junior; CS is a related technical field; GPA 3.66 ≥ 3.5 preferred; 3+ months experience; US citizen / ITAR; 12 weeks from May 2027; will self-relocate to LA. Citizenship is an apply-form knockout, not a resume line.
- **Track:** full-stack + aerospace / crewed-vehicle / mission-critical systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on Web Worker / sub-5ms / 60 FPS plus a 27% fault-tolerant S3 upload recovery — real-time constraints and operational debug, not a Voice-AI product pitch.
- Granular sits #2 with C++ lock-free SPSC, zero-alloc `processBlock`, and a real-time safety audit — the Nyx/crewed-vehicle differentiator is in the top half; MDC Flask/ETL and a 49ms pgvector search back the generic SWE screen.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Lock-free SPSC, zero-alloc processBlock, and a real-time safety audit are the crewed-vehicle differentiator, but none of the three bullets sizes the outcome (callback latency, xruns, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than mission-critical real-time discipline — a skim may underrate the C++ evidence crewed-vehicle work rewards.

### Interview angles

- **Lead with:** CaseStudyPrep Web Worker / <5ms / 60 FPS and 27% upload-failure recovery as production real-time plus test/debug; Granular zero-alloc `processBlock`, lock-free SPSC FIFO, CMake/real-time safety audit; Vylet 79%→89% name-collision defect as operational debug; MDC sole-owned Flask REST + Requests/Pandas ETL as shipped systems and data analysis
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one; 16-voice swap overflowed the page)* — script the audio-thread constraints and what you would measure next. Do not claim citizenship, Nyx/Storm internships, MATLAB, ROS, GNC, or flight software. If asked about Vylet, pivot to the 79%→89% defect fix and Docker/Celery workers, not the PE/search-fund product story.
- **Depth prep:** lock-free concurrency, C++ memory/audio-thread rules, deterministic constraints; Flask/ETL ownership and the Web Worker real-time story; internships FAQ interview is a walkthrough of the most recent technical project plus mission fluency (Nyx / democratizing space). No published intern OA.

## Likelihood

- **Resume screen:** High — real-time lead, C++ lock-free in the top two, Python APIs/ETL plus a 49ms search line, test/debug in bullets, one clean page; resume is the gate
- **Overall hire odds:** Medium — C-tier intern funnel is resume-gated then a project-walkthrough interview (~15–25%); the page clears the screen, but ITAR US-person and self-relocate are binary apply-form knockouts and the loop still wants mission fluency (Nyx) plus a live walkthrough of the last technical project
- **Funnel filters:** Ashby resume screen (bottleneck) → interview (most recent technical project + mission fluency) · no published intern OA · no intern sys design · ITAR US citizen/LPR · self-relocate to LA · Zinc background check on offer · ~15–25%
- **Outside the resume:** Apply in this first wave (posted 2026-09-03); answer ITAR honestly on Ashby; prep a walkthrough of the most recent technical project plus Nyx / democratizing-space fluency per the internships FAQ
