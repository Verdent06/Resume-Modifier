# Software Engineering Intern — Summer 2027 at RTX / Raytheon

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — Expected May 2028 is sophomore-or-higher by summer 2027 (JD floor)
- **Track:** full-stack (real-time/DSP systems flavor; no track divergence)
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume with shipped SWE (MDC Flask/EC2, CaseStudyPrep Angular/RxJS reliability, Vylet live product) plus a deep C++ real-time/DSP project — on-axis for a radar/fire-control software org whose bottleneck is the resume, not an OA.
- Python, C++, Angular, Git, Docker, and pytest/CI are proven in bullets; class year is in window.
- Binding dings: Java (JD required language) is absent, Unix/Linux is never named, and the C++ differentiator has no test/verification line.

### Demerits

- **minor** · `resume` · Java wholly absent — JD required language for a C/C++/Java shop; C++ is on-domain and deep, so this is a keyword miss, not a capability no.
- **minor** · `resume` · Unix/Linux never named — JD environment string appears nowhere; Docker and EC2 imply it, but a 30-second Linux scan is empty.
- **minor** · `Granular Synthesizer Plugin` · no test or verification — lock-free / zero-allocation `processBlock` is the right depth; the intern JD still names test plans and coverage, and this project shows none.

### Misreads

- A Java-keyword ATS pass or a rushed defense skim can file this as “no Java / not Linux / audio hobby” before the systems discipline lands.

### Interview angles

- **Lead with:** Granular zero-allocation `MemoryPool` and lock-free SPSC (hard real-time C++/DSP); CaseStudyPrep 27% upload-failure fix in Angular/RxJS; MDC sole-ownership production Flask API on EC2; Vylet LangSmith eval / Pydantic consensus gates (50% → 90%) plus Docker/Celery shipping.
- **Defend:** No Java on the page — say C++ and Python are the languages you interview in; do not claim Java. *(out of rails: Java absent — live pool and inventory have no Java; MatchStream is commented out.)* Unix/Linux is implied by Docker/EC2 but unnamed. *(out of rails: Unix/Linux never appears in the pool.)* Granular verification: narrate the CMake real-time safety checklist (zero heap, zero locks before release) even though that bullet is not on the page; SignalWeaver pytest + GitHub Actions is the on-page test story. *(out of rails: Granular has no callback/CPU/jitter metric and no unit-test/CI bullet in the live pool.)*
- **Depth prep:** C++ real-time (slab allocators, SPSC, `processBlock` constraints); Python production (Flask/EC2, Docker, CI); light DS&A for a 2–3 round easy loop; process/test-discipline stories (eval gates, pytest CI, real-time safety audit).

## Likelihood

- **Resume screen:** High — eligible class year, shipped SWE + deep C++ real-time/DSP; Java/Linux/test dings dent the scan, they do not flip it to a no.
- **Overall hire odds:** Medium — no OA, so most front-end elimination is this PDF, then 2–3 easy rounds at a ~20–25% B-tier defense intern accept rate. Citizenship/clearance is a hard knockout this page cannot show.
- **Funnel filters:** Workday apply → resume screen (binding) → 2–3 easy technical/behavioral rounds · no OA · no system design · U.S. citizenship + interim Secret before start.
- **Outside the resume:** Answer citizenship/clearance knockouts honestly; referral (HM > recruiter > engineer); apply in the first wave; prep light DS&A plus process/test stories.
