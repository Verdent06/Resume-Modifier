# Software Engineering Intern (Summer 2027) at RTX / Applied Signal Technology

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — Expected May 2028, enrolled through Summer 2027 (~96 credits); U.S. citizen (citizenship is a Workday knockout, not a resume line)
- **Track:** full-stack + SIGINT / advanced-communications software
- **Pipeline:** 2 cycle(s) · exit: writer_peak · section-fix (Granular restored to Projects)

## Screen Review

### First read

- One-page UMich CS intern resume: titled roles first (Voice-AI co-op with Web Worker / Angular debug, then MDC Flask/EC2), then a deep C++ lock-free / zero-allocation / CMake DSP **project**, then SignalWeaver FastAPI + pytest CI — on-axis for AST comms/SIGINT software whose bottleneck is the resume, not an OA.
- C++ and Python are proven in bullets; Angular appears in a real UI failure; class year is in window; no Rust/Qt/Java invented. The plugin is labeled as a project, not a job.
- Binding dings: lead Experience title still reads Voice AI; Linux/Unix is never named; Granular's four systems bullets have no runtime metric.

### Demerits

- **minor** · `CaseStudyPrep.AI` · AI-product title on lead — lead is "Software Engineer Co-op (Voice AI)"; bullets are real-time/debug (Web Worker, <5ms, 60 FPS, Angular) but a SIGINT first-pass can misfile as AI intern.
- **minor** · `resume` · Linux/Unix absent — preferred C++-in-Linux environment appears nowhere; Docker and EC2 imply it, a 30-second Linux scan is empty.
- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC, zero-alloc `processBlock`, Gaussian LUT, and a CMake real-time safety audit are the C++/DSP signal, but none sizes callback latency, xruns, or CPU.

### Misreads

- A rushed SIGINT-software skim can file this as "Voice AI / web intern plus hobby audio, no Linux" before the lock-free C++ and shipped Python land.

### Interview angles

- **Lead with:** Granular zero-allocation `MemoryPool` and lock-free SPSC plus CMake VST3/AU real-time audit (hard real-time C++ / OOD); CaseStudyPrep Web Worker / 27% upload-failure debug on Angular; MDC sole-ownership production Flask API on EC2; SignalWeaver pytest + GitHub Actions.
- **Defend:** Lead title still says Voice AI — open with the Web Worker / Angular systems bullets, not the product category. Unix/Linux is implied by Docker/EC2 but unnamed. *(out of rails: Unix/Linux never appears in the pool or skills inventory.)* Granular has no xrun/latency/CPU metric on the page. *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one.)* No Rust, Qt, Java, embedded RTOS, TCP/IP, or ITU — say C++ and Python are the interview languages; do not claim them. *(out of rails: those stacks are absent from pool and inventory.)*
- **Depth prep:** C++ real-time (slab allocators, SPSC, `processBlock` constraints, CMake release gates); Python production (Flask/EC2, Docker, pytest CI); Angular/RxJS UI debug; light DS&A for a 2–3 round Easy loop; code-review / release-gate stories.

## Likelihood

- **Resume screen:** High — eligible class year, C++ in bullets with lock-free/CMake depth as the lead project, Python shipped; the three minors dent the scan, they do not flip it to a no.
- **Overall hire odds:** Medium — no OA, so most front-end elimination is this PDF, then 2–3 Easy rounds at a ~20–25% C-tier defense intern accept rate. Citizenship is a hard form knockout this page cannot show.
- **Funnel filters:** Workday apply → resume screen (binding) → 2–3 Easy technical/behavioral rounds · no OA · no system design · U.S. citizenship required (this intern posting does not name Secret/TS-SCI).
- **Outside the resume:** Answer citizenship yes; confirm onsite West Valley City / Salt Lake City (not a skip); referral into AST SLC (HM > recruiter > engineer); apply in the first wave; prep light DS&A plus process/test stories.
