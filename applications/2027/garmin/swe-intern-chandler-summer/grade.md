# SOFTWARE ENGINEER INTERN at Garmin

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Summer 2027 internship + Expected May 2028 leaves Fall 2027 and Winter 2028, so junior / rising senior; JD has no class-year gate (pursuing CS/EE/CE or relevant); GPA 3.66 ≥ 3.0 required and ≥ 3.5 desired; US citizen, JD prints no sponsorship knockout
- **Track:** full-stack + embedded / consumer-hardware / C++ systems / aviation
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads as a titled SWE co-op: Web Worker real-time under 5ms / 60 FPS plus a 27% fault-tolerant S3/RxJS recovery — production latency and debug, not a Voice-AI product pitch.
- Granular sits #2 with C++ zero-alloc `MemoryPool`, lock-free SPSC FIFO, and a `processBlock` release audit — the aviation/comms-hardware differentiator is in the top half; MDC Flask/ETL and Vylet Docker/defect-fix back the generic SWE + QA screen.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-alloc MemoryPool, lock-free SPSC FIFO, and a processBlock release audit are the C++ systems signal this aviation intern screen wants, but none of the three bullets sizes an outcome (callback latency, xruns, CPU) so a skim can still read hobby DSP.

### Misreads

- Granular without a number can read as hobby DSP rather than systems discipline next to comms/nav products — a skim may underrate the C++ memory/concurrency/release evidence Garmin Embedded routing rewards.

### Interview angles

- **Lead with:** CaseStudyPrep Web Worker / <5ms / 60 FPS and 27% upload-failure recovery (test/debug + real-time); Granular C++ MemoryPool / lock-free SPSC / processBlock safety checklist (hardware-adjacent systems, not firmware); MDC sole-owned Flask REST + Requests/Pandas ETL (shipped delivery / stakeholder)
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure. Do not claim C, C#, Java, Assembly, firmware, ROS, or an aviation internship. If they route Embedded, pivot honestly: plugin DSP real-time constraints, not device firmware. If they route Web/Mobile/DevOps, pivot to Flask/EC2, Angular/RxJS, Docker/Celery.
- **Depth prep:** lock-free atomics, C++ hot-path / zero-alloc rules, OOP + data structures on the SPSC/slab design; one debug STAR (CaseStudyPrep expired S3 URLs or Vylet 79%→89% name-collision). No standard intern OA — expect recruiter phone then ~1 hr HM tech (C/C++/C# or Java, DS, OOP).

## Likelihood

- **Resume screen:** High — titled SWE co-op leads with sized real-time and debug, C++ lock-free sits in slot 2, Python/Flask is shipped, GPA 3.66 clears the desired 3.5, one page; this funnel's front door is the PDF
- **Overall hire odds:** Medium — B-tier catch-all, 2–3 Easy–Med rounds, no standard OA, bottleneck resume, ~8–15%. The page should clear the screen, but the HM still has to hear a live C++/DS/OOP walkthrough and Chandler on-site is a real constraint; Embedded vs Web placement is a team-match after the screen
- **Funnel filters:** iCIMS resume (rolling) → recruiter phone → ~1 hr HM tech (listed language, DS, OOP; intern reports no standard OA) **[directional]** · no intern sys design · Bottleneck: resume · ~8–15%; on-site Chandler AZ; GPA ≥3.0 (desired ≥3.5); no class-year gate; JD does not list a sponsorship knockout
- **Outside the resume:** Apply in the first iCIMS wave; a Garmin Aviation / UMich alumni referral (HM > recruiter > engineer); prep STAR plus a lock-free `processBlock` walkthrough and one debug story. Intern behavioral is a filter round (`recruiting.md`)
