# AMD — 2027 Undergrad Software Engineer Intern/Co-op (req 90891) · Written Application Answers

Draft answers for AMD careers req `90891`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented Azure, Java, Perl, PowerShell, Django, Rails, Spring Boot, MongoDB, MySQL, Perforce, UML, firmware, RTL, or CPU-microarchitecture internships. **Do not invent Snowflake, Databricks, Copilot, Fusion, or Tableau.** Trim to each form’s length limit before submitting.

This posting is a **catch-all undergrad SWE intern/co-op**, not the Masters-tagged SWE and not an ML intern. Recruiting may route you onto applications, tools, or platform software. Prefer **applications / SDLC software** first, then **tools / platform (C++ performance)** as the semiconductor differentiator. Do **not** volunteer embedded/microcontroller or CPU-architecture work unless they ask, and then only as C++ real-time constraints from the synth — not firmware or RTL.

Apply: https://careers.amd.com/jobs/90891
Resume: `applications/2027/amd/software-engineer-intern/Vedant Desai Resume.pdf`

**Do not submit from this file.** Artifacts only; no ATS apply.

---

## Cover letter

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

AMD — University Recruiting
Santa Clara / San Jose, CA

Re: 2027 Undergrad Software Engineer Intern/Co-op (req 90891)

Dear AMD hiring team,

I am applying for the 2027 Undergrad Software Engineer Intern/Co-op in San Jose or Santa Clara. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a US citizen, authorized to work in the United States without visa sponsorship. I can work the full-time (40 hours/week) hybrid or onsite term, and I remain enrolled after the internship (Fall 2027 and Winter 2028). As a semester student I am targeting the Summer Internship window of May 24, 2027 – August 13, 2027.

This posting is software next to silicon — build and maintain applications, full SDLC, automation scripts, and debugging — not a chip-design or ML-research seat. That is the work I already ship: a production REST API to a real stakeholder, C++ that cannot allocate on the hot path, and production debug when uploads fail.

What I would bring:

- **Shipped applications / data systems.** At Michigan Data Consulting I was the sole engineer on a five-month Michigan Campaign Finance Network contract. I replaced ~2-hour manual committee pulls with a Requests + Pandas ETL (eliminating ~800 hours of work across 400 tracked PACs) and shipped a production Flask REST API on AWS EC2 into their public research workflow.
- **C++ systems under a hard constraint.** I built a real-time C++/JUCE audio engine whose `processBlock()` path cannot allocate or take a lock: a `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering, shipped as VST3/AU binaries after a real-time safety audit. That is tools / platform-software discipline, not an RTL or firmware internship. github.com/Verdent06/granular-synth
- **Debug and automation.** At CaseStudyPrep.AI I closed a 27% audio-upload failure rate around expired S3 URLs (RxJS retry + MIME negotiation in Angular) and moved processing off the UI thread (<5ms main-thread blocking, 60 FPS). On Vylet I shipped a Dockerized pipeline with Redis/Celery workers and diagnosed a name-collision defect that lifted lead-qualification from 79% to 89% (live product, vyletdata.com).

I have not shipped Azure, Java, Perl, PowerShell, Django, Rails, Spring Boot, MongoDB, MySQL, Perforce, or UML. My production languages are Python and C++, plus TypeScript/JavaScript via Angular, SQL, HTML, PostgreSQL, Git, Docker, and AWS (EC2, S3). If the team sits on Azure or a JVM service I will ramp rather than claim it. I develop on macOS and will ramp on UNIX/Linux rather than list Linux as a skill I cannot defend.

I return to Michigan after the term (Expected May 2028). I would welcome the chance to walk through the MCFN API delivery or the `processBlock()` constraints.

Sincerely,
Vedant Desai

---

## Exact form questions visible on the posting

Pulled from https://careers.amd.com/jobs/90891 without submitting. The Apply step stops at an email/privacy gate; further Workday fields were not captured. Do not invent unseen questions.

| Visible question / field | Answer |
| --- | --- |
| Email (required to begin application) | vedantde@umich.edu |
| “I have read and understand the AMD Global Notice for Applicants and the AMD Privacy Policy” | Check **yes** after reading the notice |
| “I accept” | Check **yes** |
| “This role is not eligible for visa sponsorship.” (JD) | **No conflict.** US citizen; no sponsorship needed; answer **No** if a sponsorship question appears |
| Locations: San Jose, CA or Santa Clara, CA | **Yes** — either; Santa Clara HQ or San Jose |
| Full time (40 hours a week), hybrid or onsite for the term | **Yes** |
| Currently enrolled in a US-based university, Undergrad, CE / EE / CS or related | **Yes** — B.S. Computer Science and Economics, University of Michigan |

---

## Knockout / structured fields (fill if Workday asks; not all were on the public page)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/amd/software-engineer-intern/Vedant Desai Resume.pdf` |
| Cover letter | Paste the letter above if an Additional Information / Cover Letter box exists |
| Location preference | **Santa Clara, CA or San Jose, CA** |
| Willing to work onsite / hybrid, 40 hrs/week | **Yes** |
| Currently enrolled undergrad CS / CE / EE (US university)? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Expected graduation | **May 2028** |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** |
| Work authorization | **US citizen**; authorized to work in the US without visa sponsorship |
| Will you now or in the future require visa sponsorship? | **No** |
| Term preference (semester student) | **Summer Internship: May 24, 2027 – August 13, 2027.** Spring/Summer or Summer/Fall co-op only if they ask and the calendar still returns you to Michigan after. |
| Comp USD $64,064–$96,096/Yr. | **Yes** — accept the posted intern range |
| How did you hear about this role? | **Company career site** (careers.amd.com / req 90891). If a source list appears and none fit: **LinkedIn Jobs**. |
| Languages you can interview in | **C++, Python, SQL, TypeScript/JavaScript (Angular), HTML.** Do **not** check Java, Perl, PowerShell, Azure, Django, Rails, Spring Boot, MongoDB, MySQL, Perforce, UML, Snowflake, Databricks, Copilot, Fusion, or Tableau. |

Workday often has no screening essays on the JD page. Paste the cover letter into Additional Information / Cover Letter if a box exists. Skip optional self-ID unless required (`recruiting.md`: fill required fields, keep volume high).

---

## “Why AMD / why this internship?”

I want a summer writing software that has to be correct next to real compute — applications, tools, C++ systems — not a generic web rotation and not a fabricated chip-design internship. AMD is the CPU/GPU company competing in that stack. This req is B for SWE, not chip engineering: design, build, test, deploy, automate, debug.

The work I can defend:

- **Applications / SDLC.** Sole engineer on a five-month MCFN contract: Requests + Pandas ETL and a production Flask REST API on AWS EC2. Vylet is a Dockerized pipeline with Redis/Celery (live product, vyletdata.com).
- **Tools / platform, honestly scoped.** Real-time C++ whose audio thread cannot allocate or lock (`MemoryPool<Grain, 64>`, lock-free SPSC, `processBlock()` safety audit). That is engineering-tools and performance work, not RTL, firmware, or a CPU-pipeline internship.

I can be onsite/hybrid in Santa Clara or San Jose for the Summer 2027 term (May 24 – August 13). I return to Michigan afterward (Expected May 2028). I am a US citizen and do not need sponsorship.

---

## “Tell us about a project you built” / additional information

Two that map onto this req without inflating the stack:

**MDC (applications).** Production Flask REST API on AWS EC2 plus a Requests + Pandas ETL that removed ~800 hours of PAC research. Closest analog to “build and maintain software applications” and full SDLC with a real stakeholder.

**Granular synthesizer (C++ systems).** github.com/Verdent06/granular-synth. Zero-allocation audio thread, lock-free UI-to-audio FIFO, VST3/AU release binaries after a real-time safety audit (no heap, no locks in `processBlock()`). Closest analog to debugging and performance next to CPUs — still DSP, not firmware.

---

## Availability

Summer 2027 semester internship: **May 24, 2027 – August 13, 2027**, full-time 40 hours/week, hybrid or onsite Santa Clara or San Jose. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Lead with MDC (shipped API/ETL) and Granular (C++ systems).** CaseStudyPrep is the debug story. Vylet’s LangGraph story is production ownership, not “I want to do agents at AMD.”
- **Do not claim Azure, Java, Perl, PowerShell, Django, Rails, Spring Boot, MongoDB, MySQL, Perforce, UML, firmware, RTL, Linux-as-a-skill, Snowflake, Databricks, Copilot, Fusion, or Tableau.** Honest C++ + Python + SQL + JS-family beats a knockout lie.
- **Granular has no latency/xrun/CPU number on the page.** If asked, describe the audio-thread constraints and what you would measure — do not invent a metric.
- **Location is not a skip.** Say yes to Santa Clara or San Jose, 40 hrs/week, hybrid/onsite.
- **Sponsorship is a knockout on this req.** US citizen; answer **No** to sponsorship.
- **Catch-all posting:** “indicating your interest in AMD intern positions”; recruiter routes if experience aligns. Apply anyway; after the PDF the bottleneck is tech rounds (`companies.md`: no standard OA, ~5–8%).
- **Referral:** no AMD contact in `network.md`. A UMich alum at AMD still beats a cold careers.amd.com pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Do not apply from this file automatically.**
