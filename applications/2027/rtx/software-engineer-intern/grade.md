# Software Engineer Intern at RTX (Raytheon)

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible on class year — Expected May 2028 makes him a rising senior during the May–Aug 2027 term (JD wants sophomore/junior/senior/post-grad by summer 2027); required-language floor is Java, which the candidate lacks (interview-defense gap, not a page eligibility miss). **Hard downstream gate:** the role requires U.S. citizenship for a security clearance — a binary knockout to confirm in the application, not visible on the resume.
- **Track:** full-stack
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads on a production Flask REST API on AWS EC2 with sole ownership plus an ~800-hour ETL win — the "software developer and integrator" spine the JD literally tests, on a Linux/cloud stack.
- CaseStudyPrep co-op (Angular fault-tolerant RxJS integration, 27% upload-failure fix) and SignalWeaver (FastAPI REST, Docker Compose + GitHub Actions CI/pytest) hit the JD-preferred Python + JS-framework + CI signals.
- Binding ding: the one required language, Java, is nowhere on the page, and Unix/Linux is only implied — a Java-forward defense screener has to infer the required floor rather than see it.

### Demerits

- **major** · `resume` · required Java absent, no compiled/systems-language depth — the JD requires Java in a Unix/Linux env and RTX is Java-forward, yet Java appears in no bullet and not in Skills; the typed-language story is TypeScript-only, so the page reads as a Python/TS web engineer and the required floor can't be confirmed
- **minor** · `SignalWeaver` · test/review discipline shown only once — unit tests / coverage / peer + design reviews / test plans are the JD's defining bar, but that discipline surfaces in a single CI/pytest line and is absent from all three professional experiences
- **minor** · `resume` · Unix/Linux never named — the required environment and a key ATS term never appear as words; Linux is only implied via EC2 and Docker, so a keyword scan can miss the required-environment signal

### Misreads

- With no Java and no compiled-language bullet, a rushed screener may bucket this as a generic web/data candidate and under-weight it against the required Java-in-Unix/Linux floor — even though the shipped integration, CI, and Linux/cloud delivery genuinely fit the role.
- Test/review rigor confined to one CI line can read as "tests one project" rather than a candidate who holds a professional coverage/review bar, which is the discipline this shop names as its identity.

### Interview angles

- **Lead with:** MDC production Flask REST API sole-ownership on AWS EC2 and the ~800-hour ETL integration; CaseStudyPrep 27% upload-failure fix and Angular/RxJS frontend integration; SignalWeaver FastAPI REST + Docker Compose + GitHub Actions CI/pytest as the developer-and-integrator + test-discipline story.
- **Defend:** Java gap *(out of rails: no Java bullet in pool — the usable pool is Python/TypeScript/C++)* — frame it as a single teachable language: "I ship typed/compiled code (TypeScript, and C++ real-time systems work with lock-free threading and a zero-allocation real-time-safety audit) and I ramp on a new language fast; give me the Unix/Linux Java stack and I'll integrate on it." Unix/Linux gap *(out of rails: no pool bullet or skills token names Linux/Unix)* — narrate the EC2 deployment, Docker containerization, and CMake systems build as the Linux/Unix development you've actually done. Test-discipline depth — narrate pytest + GitHub Actions CI on SignalWeaver and how you'd extend coverage/peer-review to the other systems.
- **Depth prep:** Java fundamentals + a Java-in-Linux warmup before the loop; REST/API design and integration debugging; unit testing / code coverage / CI (Jenkins/Maven/GitLab equivalents to your GitHub Actions); C++ real-time systems threads (lock-free SPSC, memory pools, real-time safety) as your compiled-language depth story; timed DS&A for the easy/light technical round.

## Likelihood

- **Resume screen:** Medium–High — on a resume-first, no-OA funnel the page fits the developer-and-integrator spine (EC2/Docker Linux delivery, integration across entries, Python, Angular, GitHub Actions + pytest), and the missing Java reads as trainable rather than disqualifying at a generous-offer-rate prime.
- **Overall hire odds:** Medium — the ~20-25% offer rate and easy behavioral/light-technical loop favor a clear full-stack fit who can narrate integration and testing credibly; the missing Java floor and the citizenship/clearance knockout are the two things most likely to surface downstream.
- **Funnel filters:** 2-3 rounds · Easy LC/practical · No OA · No system design · Bottleneck: resume · U.S. citizenship + ability to obtain a security clearance is a hard binary gate.
- **Outside the resume:** Apply in the first wave (Aug–Oct) — defense/resume-first reqs reward early applications; route a referral to the Huntsville site recruiter or hiring manager to convert a cold read to a warm one (HM > recruiter > engineer); confirm U.S.-citizenship/clearance eligibility honestly in the application knockouts; do a short Java-in-Unix/Linux ramp so the required language is defensible in the interview.
