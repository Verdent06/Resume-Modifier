# BAE Systems — Software Engineering Intern III, Summer 2027 (Onsite, San Diego) · Brassring answers

Draft answers for the Brassring / BAE careers form. Grounded in `context.md` and `persona.md`. First-person, honest, defensible under "walk me through this" — no invented Java, clearance, hardware, or metrics. Trim to each field's length limit before submitting.

**Knockouts (this req):** U.S. citizen YES. Existing clearance: NO. Eligible to obtain: YES (citizenship). Do not claim Secret/TS in hand.

---

## U.S. citizenship / work authorization

Yes. I am a U.S. citizen and authorized to work in the United States without sponsorship. I do not require H-1B or other visa sponsorship now or in the future.

## Do you currently hold a U.S. government security clearance?

No. I do not currently hold a clearance. I am a U.S. citizen and eligible to obtain and maintain a U.S. government security clearance if this role requires it.

## Are you willing to work onsite in San Diego, CA for Summer 2027?

Yes. I can relocate to San Diego for the internship and work onsite for the LEAP program term.

## Class standing / enrollment

Yes. I am enrolled in a B.S. in Computer Science and Economics at the University of Michigan, Expected May 2028. For Summer 2027 I will be transitioning into my senior year (JD: junior or senior, or graduate student).

## Languages / skills self-report (check only what you can interview in)

**Check:** C++, Python, JavaScript/TypeScript, Angular, React, HTML/CSS, Docker, AWS, Git, PostgreSQL, Redis.

**Do not check:** Java, C#, Spring, Kubernetes, GIS, hardware, or an existing clearance.

If there is a free-text "other" box: "C++ real-time systems (JUCE, zero-allocation audio thread, lock-free SPSC); Python production services (Flask, FastAPI, Docker); Angular/RxJS fault-tolerant client work."

---

## Cover letter / additional information (paste if the form has a box)

I am applying for the Software Engineering Intern III role in San Diego for Summer 2027. I want to spend the summer writing new code, debugging failures, and improving system stability — the work the posting describes, and the work I already do.

The closest analog I have to "resolve critical problems / improve resilience" is a voice-AI co-op at CaseStudyPrep.AI. Audio uploads were failing 27% of the time because S3 presigned URLs expired mid-flight and Angular silently rejected WAV MIME types. I built fault-tolerant RxJS logic that regenerates URLs and negotiates MIME types, and I moved audio processing off the UI thread into a Web Worker so the visualizer stayed at 60 FPS with main-thread blocking under 5ms. I also cut cloud inference cost 40% by running Silero VAD on-device via ONNX Runtime so dead air never hit Whisper.

On the systems side I built a granular synthesizer plugin from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a `MemoryPool<Grain, 64>` slab per voice at startup and (off the resume, if asked) deliver UI parameters through a lock-free SPSC FIFO. That is the same class of constraint as mission software: deterministic behavior on a hard deadline.

I also ship production Python. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network I delivered a Flask REST API on AWS EC2 and replaced ~800 hours of manual PAC research with a Requests + Pandas ETL. At Vylet, a product I founded that is live at $1,500 MRR, I Dockerized a LangGraph pipeline with Redis/Celery workers and fixed a name-collision defect that lifted lead-qualification from 79% to 89%.

I do not have Java in my portfolio. C++, Python, and TypeScript are the languages I can defend. I am a U.S. citizen, I do not currently hold a clearance, and I can work onsite in San Diego for Summer 2027.

---

## "Why BAE / why this internship?" (short)

Because Electronic Systems writes software that has to stay up — new code, critical-problem debugging, stability and resilience — and that is already how I work: fault-tolerant Angular/RxJS in production, zero-allocation C++ on a real-time thread, and Python services I shipped to real users. I want a LEAP summer on a San Diego team doing that, not a generic feature factory.

## "Tell us about a time you resolved a critical problem / improved stability."

**CaseStudyPrep.AI:** a 27% audio-upload failure rate. Root cause was expired S3 presigned URLs plus Angular rejecting WAV MIME types. I added RxJS retry that regenerates URLs mid-flight and negotiates MIME types, which eliminated that failure mode. Same product: Silero VAD on-device cut wasted Whisper calls 40%. If they want a systems version: the C++ audio callback cannot heap-allocate, so I used a fixed `MemoryPool` free-list instead of `new`/`delete` after `prepareToPlay()`.

## Availability

Summer 2027, onsite San Diego. Returning to Michigan after the internship (graduation Expected May 2028). GPA 3.66.

---

## Notes for the applicant (not for submission)

- **Citizenship YES, clearance in-hand NO.** Do not write "Secret" anywhere. Eligible-to-obtain is the honest line.
- **Never claim Java.** The JD wants one of Java/C++/C#/Python/JavaScript. You have three of five.
- **Lead conversations with the 27% failure fix and the MemoryPool audio thread**, not Vylet's PE framing or SignalWeaver LoRA.
- **Referral still helps.** Bottleneck is the resume (`companies.md` B-tier defense primes). A warm San Diego / Electronic Systems read beats a cold Brassring pile.
- Apply: https://sjobs.brassring.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=25771&siteid=5464&PageType=JobDetails&jobid=302588
