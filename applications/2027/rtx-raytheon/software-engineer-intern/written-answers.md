# RTX / Raytheon — Software Engineering Intern (Summer 2027, Marlborough) · Cover letter & Workday answers

Draft answers for a typical Workday intern application at a defense prime. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented projects, languages, or metrics. Trim to each form's length limit before submitting.

**Knockout honesty:** this role requires U.S. citizenship and eligibility for a Secret clearance (interim Secret before start). `context.md` does not record citizenship. Answer those Workday questions truthfully. If you are not a U.S. citizen, do not apply — it is an auto-reject, not a resume problem.

---

## Cover letter (paste into Workday "Cover Letter" / additional information)

I am applying for the Software Engineering Intern role on the Raytheon software team in Marlborough for Summer 2027. I want to spend the summer developing, integrating, and testing software that has to be stable — the same discipline I already practice in C++ real-time systems and in production Python services I have shipped to real users.

The work that maps most directly to this team is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a fixed `MemoryPool<Grain, 64>` slab per voice at startup and deliver UI parameters through a hand-rolled lock-free SPSC FIFO with atomic acquire/release ordering. That is the same class of constraint as radar and fire-control software: deterministic behavior, memory discipline, and integration between a control path and a hard-deadline compute path. I also configured the build so VST3/AU release binaries only ship after every `processBlock()` path is audited against a real-time safety checklist (zero heap allocations, zero lock acquisitions).

Alongside that systems work I ship production software. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network, I replaced ~800 hours of manual PAC research with a Python ETL and delivered a Flask REST API on AWS EC2 into their public research workflow. At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS logic in Angular and cut cloud inference cost 40% by running Silero VAD on-device. At Vylet, a product I founded that is live at $1,500 MRR across three clients, I built a Dockerized LangGraph pipeline with Redis/Celery workers and a LangSmith eval suite (20 adversarial cases, 13 archetypes) plus deterministic Pydantic consensus gates that lifted extraction faithfulness from 50% to 90%. SignalWeaver, a FastAPI + React research platform, ships with Docker Compose and a GitHub Actions pipeline that runs pytest on every main build.

I do not have Java in my portfolio; C++ and Python are the languages I can defend in an interview, and Angular is the JavaScript framework I have shipped. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), which puts me at sophomore-or-higher standing by Summer 2027. I can work on-site in Marlborough and will relocate for the internship.

I would like to contribute as a developer and integrator on a team that treats unit tests, code review, and test plans as the job — not extras.

---

## Workday screening / knockout answers

### U.S. citizenship / security clearance

Answer the form truthfully. This posting requires U.S. citizenship because only citizens are eligible for the required Secret clearance (interim Secret before start). Do not guess. If the answer is yes: "I am a U.S. citizen and able to obtain and maintain a U.S. government security clearance." If the answer is no: stop — the application will not proceed.

### Are you currently enrolled in a Bachelor's (or higher) in CS / CE / SE or related, and will you be at least a sophomore by Summer 2027?

Yes. I am enrolled in a B.S. in Computer Science and Economics at the University of Michigan, Expected May 2028. By Summer 2027 I will have completed my sophomore year (rising junior).

### Willing to relocate / work on-site in Marlborough, MA?

Yes. I can relocate to Marlborough, MA for Summer 2027 and work on-site for the internship.

### Preferred / required skills self-report (if the form asks you to check languages)

Check only what you can interview in: **C++, Python, Git, a JavaScript framework (Angular)**. Do **not** check Java. If there is a free-text "other" box, say: "C++ real-time systems (JUCE/DSP, lock-free threading, zero-allocation audio thread); Python production services (Flask, FastAPI, Docker, GitHub Actions/pytest); Angular/RxJS in a shipped co-op."

### "Why Raytheon / why this internship?" (short)

Because this team writes and integrates software for missiles, launchers, radars, and fire-control — real-time systems where stability and test rigor are the product. I already build that way in C++ (deterministic, zero-allocation hot path) and I already ship and test Python services (pytest CI, eval gates, production APIs). I want a summer inside a development team that treats integration, unit tests, code review, and test plans as the default, not a class project.

### "Tell us about a time you tested / integrated software."

**SignalWeaver + Vylet, honestly scoped:** I containerized SignalWeaver (FastAPI + Postgres/pgvector + nginx) and wired a GitHub Actions pipeline that builds the frontend, runs pytest, and builds the API image on every main push. On Vylet I treated the LLM path as an unreliable dependency: a LangSmith eval suite over 20 adversarial business cases across 13 archetypes, then deterministic Pydantic consensus gates, which lifted extraction faithfulness from 50% to 90%. That is the closest analog I have to "write unit tests, generate a test plan, hold quality before release." I have not worked in Java on Unix/Linux in a defense codebase; I would ramp on the team's language and process.

### Availability

Summer 2027, on-site Marlborough. Returning to Michigan after the internship (graduation Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Lead with C++ real-time, not ML.** The org mentions ML/autonomy; the JD tests general SWE + integration + test. Open with Granular (`processBlock`, MemoryPool, SPSC) and MDC/CaseStudyPrep shipping — not LoRA/SignalWeaver sentiment.
- **Never claim Java.** It is the one required language you do not have. Honest C++ + Python beats a Skills-line lie that collapses in the first technical conversation.
- **Clearance is the real gate.** The resume screen is High; overall odds are Medium because citizenship/Secret is binary and this PDF cannot show it.
- **Referral still helps.** Defense-prime intern reqs are resume-first (`companies.md`: bottleneck = resume, ~20–25%). A warm read beats a cold Workday pile.
- **Relocation is listed.** Say yes to Marlborough; location is not a reason to skip next summer.
