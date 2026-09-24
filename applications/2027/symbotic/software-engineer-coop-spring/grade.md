# Co-op - Software Engineer (Spring 2027) at Symbotic

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible — JD requires currently pursuing CS or related; UMich CS+Econ Expected May 2028, enrolled at Spring 2027. No class-year or GPA knockout on this posting.
- **Track:** full-stack + warehouse-robotics / fleet-orchestration / real-time systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads on a titled SWE co-op with a real-time path (Web Worker / sub-5ms / 60 FPS) and a 27% upload-failure recovery — generic SWE plus test/debug in the first glance.
- Granular sits in slot two with zero-allocation C++ `MemoryPool` and lock-free SPSC — the warehouse-robotics differentiator is visible in the top half; MDC Flask/EC2 plus Vylet Redis/Celery cover Python services and the JD-named Redis/Docker analog.
- Binding ding: **C# is never on the page** at a .NET Core fleet-orchestration shop whose need list leads with C#, Python and C++.

### Demerits

- **major** · `resume` · C# absent — JD needs strong OOP in C#, Python and C++; Python and C++ are through use, C# is zero. A Wilmington screener can bucket this as a Python/DSP intern rather than a Software co-op who will compile on the actual codebase
- **minor** · `Granular Synthesizer Plugin` · metric-free — Lock-free SPSC and zero-alloc `processBlock` are the multi-thread signal, but neither bullet sizes latency, xruns, CPU, or voices
- **minor** · `Vylet` · off-axis product framing — Redis/Celery and a 79%→89% defect are real; the Founder tagline still leads PE/search-fund lead-gen

### Misreads

- Missing C# plus a DSP plugin in slot two can read as the wrong intern seat (audio/Python) rather than warehouse fleet software.
- Granular without a number can read as hobby DSP rather than the lock-free systems proof this shop wants.
- Vylet's PE/search-fund tagline can file the founder role as GTM instead of Docker/Redis production.

### Interview angles

- **Lead with:** CaseStudyPrep 27% upload-failure recovery and sub-5ms / 60 FPS; Granular zero-alloc `processBlock` / `MemoryPool<Grain, 64>` and lock-free SPSC; MDC sole-owned Flask REST on EC2; Vylet Redis/Celery workers + 79%→89% defect
- **Defend:** C# is not in inventory *(out of rails: no C#/.NET pool bullet; swap sets cannot bridge; Skills-line C# would be fabrication)* — interview languages are Python, TypeScript, C++, SQL; say you will ramp C#/.NET rather than claim it. Granular has no xrun/latency/CPU number *(out of rails: pool bullets 1–6 are architecture-only)*. Vylet's title is PE lead-sourcing — pivot to Redis/Celery and the defect fix *(out of rails: tagline is verbatim from context.md; rewrite is original prose)*. Do not claim Kubernetes, RabbitMQ, Jenkins, Vitis/Vivado, ROS, or a warehouse internship.
- **Depth prep:** C++ audio-thread rules (no alloc, no lock, slab allocator, SPSC); Redis/Celery as the honest microservices analog; Flask/EC2 + Docker/GitHub Actions; OOP in Python/C++ (not C#). STAR for recruiter + HM — intern OA unpublished (`recruiting.md` intern funnel; B-tier resume bottleneck)

## Likelihood

- **Resume screen:** Medium — Python + C++ + Redis/Docker + real-time in the top half; missing C# at a .NET fleet shop is a material ding
- **Overall hire odds:** Medium — B-tier Workday funnel is resume-first (~8–12% directional). Unpublished intern OA, Wilmington onsite / Spring dates / driver's license still have to clear, and C# ramp plus PE/DSP frames can steal seconds
- **Funnel filters:** Workday `symbotic.wd504` **R8111** → recruiter (Wilmington HQ, Jan–May 2027, DL/travel) → unpublished intern OA (do not invent HackerRank) → project walk + STAR · Easy–Med · No intern sys design · Bottleneck: resume
- **Outside the resume:** Apply in this first wave (posted 2026-09-23). Form email **`verdent06@gmail.com`**. No Symbotic contact in `network.md` — do not pick Employee Referral. Honest no-C# / yes-Python-C++ if they ask languages. See `written-answers.md`
