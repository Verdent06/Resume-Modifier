# Software Engineering Intern (Summer 2027) at RTX / Raytheon ASDS — Aurora

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028, enrolled through Summer 2027; U.S. citizen (clearance form knockout, not a resume line)
- **Track:** full-stack + satellite-ground / space C2 / DevSecOps-AWS
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume that leads with a shipped Flask REST API on AWS EC2, then a real-time co-op, then a deep C++ lock-free / slab-allocator plugin and a Docker + GitHub Actions FastAPI service — on-axis for Aurora ground-software once past the literal screen.
- C++ is proven in bullets (MemoryPool, SPSC, 16-voice `processBlock` discipline); Python/AWS/Docker/CI are through use; class year is in window; Java/Kafka/Kubernetes/SAFe/Linux homelab/clearance were not invented.
- Binding ding: this req lists prior Raytheon intern experience as a must-have and the page has none — a first-time applicant can die at that filter before the C++ is weighed.

### Demerits

- **major** · `resume` · returning-intern must-have absent — JD lists Experience as an intern at Raytheon as a qualification you must have; this page has no Raytheon/RTX internship.
- **minor** · `resume` · Unix/Linux absent — LINUX/UNIX is preferred; Docker and EC2 imply it, a 30-second environment scan is empty.
- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC and slab allocation are the OOP proof, but no latency or deadline number sizes the constraint.

### Misreads

- A rushed ASDS skim can file this as "first-time intern, Voice AI / plugin hobby, no Linux" before the AWS lead and C++ real-time work land — and the returning-intern line can stop the skim entirely.

### Interview angles

- **Lead with:** MDC sole-engineer Flask API on EC2; Granular zero-allocation `MemoryPool` and lock-free SPSC; CaseStudyPrep Web Worker / 27% S3 upload-failure debug; SignalWeaver Docker Compose + pytest GitHub Actions.
- **Defend:** No prior Raytheon internship — first-time applicant, do not invent a returner line. *(out of rails: pool has no Raytheon/RTX intern entry.)* No Java — C++ is the interview OOP language. *(out of rails: Java absent from pool and inventory.)* Unix/Linux is implied by Docker/EC2 but unnamed. *(out of rails: Linux/UNIX never appears in the pool or skills inventory.)* Granular has no latency number to quote. *(out of rails: no pool bullet names ms/CPU%/deadline.)*
- **Depth prep:** C++ real-time (slab allocators, SPSC, `processBlock` constraints); Python production (Flask/EC2, Docker, pytest CI); satellite-ground vocabulary as learning goals only (command & telemetry, flight dynamics, planning/scheduling — do not claim them); light DS&A for a 2–3 round Easy loop.

## Likelihood

- **Resume screen:** Low — returning-intern must-have is a listed filter this PDF cannot satisfy; the rest of the page would otherwise be a Medium C-tier pass.
- **Overall hire odds:** Low — no OA, so most elimination is this screen plus a 2–3 round Easy loop at ~20–25% C-tier intern accept. A first-time applicant who survives the returning-intern filter still has to clear citizenship/TS-SCI knockouts the page cannot show.
- **Funnel filters:** Workday apply → resume screen (binding; no OA) → 2–3 Easy technical/behavioral rounds · no system design · U.S. citizenship + TS/SCI without polygraph (posting also states active/existing clearance after day 1).
- **Outside the resume:** Answer citizenship/clearance knockouts honestly (yes / able to obtain); do not claim a prior Raytheon intern term or an existing clearance; referral into Aurora ground-software (HM > recruiter > engineer); apply in the first wave (req posted 2026-08-31).
