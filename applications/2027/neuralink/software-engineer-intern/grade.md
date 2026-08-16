# Software Engineer Intern, Implant at Neuralink

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028; Summer 2027 internship is rising junior / after sophomore year. JD states no class-year requirement. Work-auth / sponsorship are form fields; context.md has no citizenship fields (uncomputed for those gates).
- **Track:** full-stack + BCI / medical-device / safety-critical / firmware-adjacent
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Top half is dated CaseStudyPrep reliability (5ms / 27% upload recovery / 40% inference-cost) plus Granular’s C++ real-time stack (zero-alloc MemoryPool, lock-free SPSC, CMake safety audit) — the Implant-memorable systems signal is visible, not buried.
- Python shows up in production (Vylet consensus/verification, MDC Flask/ETL); C++ is used under a hard real-time constraint, not Skills-only.
- Binding ding is minor: Granular never sizes whether the engine held load (no CPU, xrun, callback latency, or users).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — three lock-free / zero-alloc C++ bullets plus a real-time safety checklist, but no sized outcome (CPU, xruns, callback latency, users)

### Misreads

- A skim that stops on Granular’s audio-plugin tagline can bucket this as a hobby DSP resume and miss the production Python + failure-recovery spine.
- An undated GitHub in Granular’s date slot can read as an old personal project even though the systems work is the company-fit hook.

### Interview angles

- **Lead with:** Granular zero-alloc audio thread + lock-free SPSC + CMake real-time safety checklist; CaseStudyPrep 27% upload-failure recovery and sub-5ms UI-thread budget; Vylet verification gate (hard-fail on legal/industry/geography) and 79%→89% name-collision fix; MDC sole-engineer Flask REST on EC2
- **Defend:** Granular has no latency/xrun/CPU/user number *(out of rails: full 6-bullet pool has no impact metric; 16-voice closer overflowed the page)* — narrate the real-time safety checklist and what you would measure. Granular has no dates *(out of rails: project header is GitHub, not a timeline)* — say when you built it; do not invent a medical-device or implant-firmware internship. No literal C or Rust on the page — C++ is the adjacent systems language; do not claim C/Rust fluency.
- **Depth prep:** lock-free / memory-pool / real-time constraints; Python verification vs research-grade prototypes; exceptional-ability essay as 3–4 quantitative problem/solution/result stories (persona: the most important part of the process); intern-medium DS&A for an unpublished coding screen (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — Python in production, C++ under a real-time constraint, CMake/deploy, and reliability metrics in the top half clear a human Implant PDF read
- **Overall hire odds:** Low — tiny Musk-adjacent intern class; exceptional-ability essay and the technical loop are the binding gates after the PDF. A clean screen does not move residual seats.
- **Funnel filters:** Greenhouse + exceptional-ability essays → recruiter → unpublished OA (do not assume HackerRank) → coding/systems loop. On-site Austin or South San Francisco; no intern relocation; work-auth / sponsorship on the form
- **Outside the resume:** Write the essay as 3–4 quantitative stories; get a warm intro (`recruiting.md` §4); apply in the first wave; keep DS&A at intern-medium fluency
