# RTX / Raytheon ASDS — Software Engineering Intern (Summer 2027, Aurora CO) · Cover letter & Workday answers

Req **01870410**. US-CO-AURORA-S75, 16800 E Centretech Pkwy, Bldg S75. Drafted from `persona.md` + real experience only. No invented Java, Kafka, Kubernetes, SAFe, Linux homelab, Raytheon intern term, existing clearance, projects, or metrics. This is Aurora satellite-ground / space C2 software — not Marlborough radar, Tewksbury Patriot, West Valley City SIGINT, or Cedar Rapids avionics.

Workday questionnaires were pulled from the public CXS endpoints on this posting (`questionnaireId` / `secondaryQuestionnaireId`). Answers below match those questions. Trim to each field's length limit before submitting.

---

## Application Questions 1 of 2 (exact wording)

- **Are you a CURRENT or FORMER employee of RTX’s Independent Auditor, PriceWaterhouseCoopers (PwC)?** No.
- **If yes, please indicate: (a) the dates of your PwC employment; (b) whether you are/were a partner of the firm; and (c) if you were a member of the PwC RTX engagement team within the last three years, details regarding your current/former role on the engagement.** Skip unless Yes. Do not invent PwC employment.
- **Are you a FORMER U.S. federal government civilian or military (active duty or reserves) employee?** No.
- **Did you previously work for RTX (including its predecessors or any of its businesses) in any capacity?** No. Do not invent a Raytheon internship. The JD lists prior Raytheon intern experience as a must-have; answer this knockout honestly.
- **Are you a CURRENT U.S. federal government civilian or military (active duty or reserves) employee?** No.
- **Are you participating in, supervising, or otherwise responsible for any pending government procurement or contract administration matter that does or might involve RTX and/or a matter that has a direct and predictable effect on the financial interests of RTX?** Only appears if Current federal = Yes or Unsure. Not applicable when Current federal = No.
- **Are you a citizen of the United States?** Yes. U.S. citizenship is required; only U.S. citizens are eligible for a security clearance. No sponsorship.

---

## Application Questions 2 of 2 (exact wording)

- **If you answered "Yes" to question 1, please provide your permanent address. If you did not answer "Yes", please enter "N/A".** Use the real permanent address. It is not stored in `context.md` — do not invent one.
- **If you answered "Yes" to question 1, please provide your major. If you did not answer "Yes", please enter "N/A".** Computer Science.
- **What is your cumulative GPA?** 3.5 or higher (3.66 / 4.0).
- **How many credit hours towards your degree do you anticipate having completed by the time you would start this position?** Fill from Wolverine Access for Summer 2027 start. `context.md` does not record a credit-hour count — do not invent one.
- **Are you currently enrolled in a degree seeking program?** Yes.
- **What is your Current Degree Program?** Bachelors.
- **Please Specify:** If this is the OTHER-major follow-up after selecting Computer Science, enter N/A. If the form still requires text, enter Computer Science. Do not pick a second major that is not on the resume.

---

## Cover letter / additional information (≈160 words)

I am applying for the Software Engineering Intern role on Raytheon's Air & Space Defense Systems satellite-ground team in Aurora for Summer 2027. I want to spend the summer designing, developing, testing, delivering, and maintaining software for ground systems — the same discipline I already practice in C++ and in production Python services.

The work that maps most directly is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a fixed `MemoryPool<Grain, 64>` slab per voice at startup and deliver UI parameters through a hand-rolled lock-free SPSC FIFO with atomic acquire/release ordering. Sixteen-voice polyphony pre-computes ADSR rates in `prepareToPlay()` so `processBlock()` never divides or heap-allocates after startup.

Alongside that I ship production software. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network, I delivered a Flask REST API on AWS EC2 and a Requests + Pandas ETL that removed ~800 hours of manual PAC research. SignalWeaver is containerized with Docker Compose and a GitHub Actions pipeline that runs pytest on every main build. At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS and held main-thread blocking under 5ms with a Web Worker.

I have not interned at Raytheon and I have not shipped Java. C++ is the object-oriented language I can defend in an interview. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), a U.S. citizen able to obtain a TS/SCI clearance, and I will work onsite in Aurora.

---

## "Why RTX / this internship / Aurora ASDS?" (≈90 words)

Aurora's ASDS software teams write satellite ground-system software — command and telemetry, flight dynamics, planning and scheduling, spacecraft operations — on Agile product teams with AWS, microservices, and DevSecOps. That matches how I already build: deterministic C++ on a hard-deadline thread (zero-allocation `processBlock()`, lock-free UI-to-audio), and Python services held to a test bar (pytest CI, production Flask on EC2, Docker Compose). I want a summer inside a development team that treats design, test, delivery, and maintain as the job, specifically on ground-software in Aurora, not a radar, SIGINT, or avionics site.

---

## Availability / onsite

Summer 2027, exclusive onsite Aurora, CO. Willing to relocate (posting lists relocation eligible). Returning to Michigan after the internship (graduation Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Lead with C++ OOP and Python/AWS delivery, not ML and not campaign-finance.** Open with Granular (`processBlock`, MemoryPool, SPSC), then MDC Flask/EC2 and SignalWeaver Docker + GitHub Actions.
- **Never claim Java, Kafka, Kubernetes, SAFe, a Linux homelab, a prior Raytheon intern term, or an already-held clearance.** Honest C++ + Python beats a Skills-line lie. Unix/Linux is implied by Docker/EC2; do not name a homelab that does not exist.
- **Returning-intern must-have.** This req lists "Experience as an intern at Raytheon" as a qualification you must have. Answer prior-RTX = No. Do not skip the apply for citizenship; the returning-intern line is the real screen risk.
- **Citizenship / TS/SCI.** Answer citizen = Yes; clearance = able to obtain, not already held. The posting also says active/existing clearance required after day 1 — that is processed after start, not a current TS/SCI claim.
- **Referral still helps.** C-tier RTX intern reqs are resume-first (`companies.md`: bottleneck = resume, ~20–25%).
