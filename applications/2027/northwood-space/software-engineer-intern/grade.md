# Software Engineering Intern (2027 Summer Internship) at Northwood Space

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 maps to enrolled undergrad at Summer 2027; JD has no class-year gate (ITAR U.S. Person is an apply-form knockout, not a resume line)
- **Track:** full-stack + space-infra / phased-array ground-station network / data-plane / distributed systems / networking
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on fault-tolerant S3 upload recovery (27%) plus Web Worker / sub-5ms / 60 FPS — production data-movement reliability and low-latency, not a Voice-AI product pitch.
- Granular sits #2 with C++ lock-free SPSC, zero-alloc `processBlock`, and a real-time safety audit — the systems/data-plane differentiator is in the top half; MDC Flask/ETL on AWS and FastAPI p50/p99 back the generic SWE + pipeline screen.
- Binding ding: Granular never sizes the systems win (no latency / xrun / CPU number).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — Lock-free SPSC, zero-alloc processBlock, and a real-time safety audit are the systems signal this ground-station shop wants, but none of the three bullets sizes the outcome (callback latency, xruns, CPU)

### Misreads

- Granular without a number can read as hobby DSP rather than mission-critical real-time discipline — a skim may underrate the C++/systems evidence Northwood's data plane rewards.

### Interview angles

- **Lead with:** Granular Synthesizer — zero-alloc `processBlock`, lock-free SPSC FIFO, atomics, real-time safety checklist; CaseStudyPrep 27% S3 upload-failure recovery and sub-5ms / 60 FPS as production data movement under latency constraints; MDC sole-owned Flask REST + Requests/Pandas ETL on AWS EC2 as the cloud/pipeline delivery
- **Defend:** Granular has no xrun/latency/CPU metric on the page *(out of rails: full 6-bullet pool has no verbatim impact metric; swap sets cannot invent one)* — script the audio-thread constraints and what you would measure next. Do not claim Rust, Golang, Terraform, or FPGA. If asked about Vylet, pivot to the Docker/Redis/Celery workers and 79%→89% defect fix, not the PE/agentic product story. No TCP/IP on the page — talk S3/presigned-URL recovery and lock-free handoff as the networking-adjacent stories.
- **Depth prep:** lock-free concurrency, C++ memory/audio-thread rules; Flask/ETL and FastAPI latency instrumentation; Docker/Celery workers; unpublished intern coding/systems screen (do not assume HackerRank). STAR on collaboration with software/network partners.

## Likelihood

- **Resume screen:** High — C++ in the top two, fault-tolerant data movement, AWS/Docker pipeline evidence, one clean page, resume is the gate
- **Overall hire odds:** Medium — B-tier space-infra funnel is resume-gated then an Easy–Med unpublished intern loop (~8–12% directional); the page clears the screen, but ITAR / five-day Torrance are binary form knockouts and tech still has to hear systems and data-movement live
- **Funnel filters:** Ashby resume → recruiter → unpublished intern tech; no named intern OA; Light sys design; bottleneck: resume · ~8–12%; onsite Torrance 5 days/week; ITAR U.S. Person
- **Outside the resume:** Apply in the first wave; answer ITAR and five-day Torrance honestly on Ashby; a Northwood engineer referral (HM > recruiter > engineer); prep lock-free/`processBlock` plus one pipeline/failure-recovery story
