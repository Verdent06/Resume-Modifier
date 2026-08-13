# Software Development Intern (Summer 2027) at RTX / Raytheon — Tewksbury

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — Expected May 2028, enrolled through Summer 2027; U.S. citizen (clearance form knockout, not a resume line)
- **Track:** full-stack + high-performance / real-time C++ (radar product software)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume with shipped Python (MDC Flask/EC2, SignalWeaver FastAPI + pytest CI) plus a deep C++ lock-free / zero-allocation project — on-axis for Tewksbury Patriot/MDS product software whose bottleneck is the resume, not an OA.
- C++ and Python are proven in bullets; class year is in window; no Java/C#/Ada invented.
- Binding dings: lead Experience title still reads Voice AI; Unix/Linux is never named; MDC's third bullet restates ownership already in bullet 1.

### Demerits

- **minor** · `CaseStudyPrep.AI` · AI-product title — lead is "Software Engineer Co-op (Voice AI)"; bullets are real-time/debug (Web Worker, <5ms, 60 FPS, 27% upload failures) but a radar first-pass can misfile as AI intern.
- **minor** · `resume` · Unix/Linux absent — preferred JD environment appears nowhere; Docker and EC2 imply it, a 30-second Linux scan is empty.
- **minor** · `MDC` · metric-free restatement — third bullet repeats sole-engineer + EC2/REST ownership from bullet 1 with no new metric.

### Misreads

- A rushed Patriot-software skim can file this as "Voice AI / web intern, no Linux" before the lock-free C++ and shipped Python land.

### Interview angles

- **Lead with:** Granular zero-allocation `MemoryPool` and lock-free SPSC (hard real-time C++); CaseStudyPrep Web Worker / 27% upload-failure debug; MDC sole-ownership production Flask API on EC2; SignalWeaver pytest + GitHub Actions.
- **Defend:** No Java/C#/Ada — say C++ and Python are the interview languages; do not claim them. *(out of rails: Java/Ada absent from pool and inventory.)* Unix/Linux is implied by Docker/EC2 but unnamed. *(out of rails: Unix/Linux never appears in the pool or skills inventory.)* CaseStudyPrep title cannot be rewritten from the canonical header. *(out of rails: "Voice AI" is the pool title; MDC-first was already graded as a major lead-off-axis.)*
- **Depth prep:** C++ real-time (slab allocators, SPSC, `processBlock` constraints); Python production (Flask/EC2, Docker, pytest CI); light DS&A for a 2–3 round Easy loop; code-review / release-gate stories (real-time safety checklist, CI pytest).

## Likelihood

- **Resume screen:** High — eligible class year, C++ in bullets with lock-free depth, Python shipped; the three minors dent the scan, they do not flip it to a no.
- **Overall hire odds:** Medium — no OA, so most front-end elimination is this PDF, then 2–3 Easy rounds at a ~20–25% C-tier defense intern accept rate. Citizenship/interim Secret is a hard form knockout this page cannot show.
- **Funnel filters:** Workday apply → resume screen (binding) → 2–3 Easy technical/behavioral rounds · no OA · no system design · U.S. citizenship + interim Secret before start.
- **Outside the resume:** Answer citizenship/clearance knockouts honestly (yes); referral into Tewksbury Patriot/MDS (HM > recruiter > engineer); apply in the first wave; prep light DS&A plus process/test stories.
