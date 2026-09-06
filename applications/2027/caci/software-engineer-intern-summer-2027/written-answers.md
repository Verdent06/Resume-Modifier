# CACI — Software Engineer Intern Summer 2027 (Ypsilanti RST) · Eightfold answers

Draft answers for the live Eightfold apply on `searchcareers.caci.com`. Grounded in `persona.md` (generic SWE screen + SAR/RST differentiator: C++ DSP + Python delivery — **not** Java/CUDA invention, **not** ML-research). First-person, honest, defensible under "walk me through this."

**Form-kit email is `verdent06@gmail.com`. Never use `vedantde@umich.edu` on Eightfold.** Resume PDF header still shows the UMich address (template-fixed). That is the document. The **form** uses Gmail.

**Do not invent Java, Rust, CUDA, Linux homelab, Jira/Scrum, Snowflake, Databricks, Copilot, Tableau, Fusion, Sentry, or a radar/EO internship.** Honest stack: C++, Python, AWS, Docker, Git, pytest/CMake. Trim to each field's limit before submitting.

**Employer / title / location from the live page:** CACI · **Software Engineer Intern - Summer 2027** · Ypsilanti, MI · Radar and Sensor Technologies Portfolio · displayJobId **331648** · Eightfold pid **1443153389145** · onsite · listed **$41,900–$83,800** (Simplify **$20.14–$40.29/hr**) · Minimum clearance to start: **None** · must be **willing and able to obtain Top Secret**.

**Prefer this ATS URL (not Simplify):**
https://searchcareers.caci.com/careers/job/1443153389145-software-engineer-intern-summer-2027-ypsilanti-mi-us

Simplify (source listing): https://simplify.jobs/p/abf84bbc-9f9b-4db5-8637-7b7772fb25e4

**This agent did not submit.** Knockouts below are from the JD plus CACI intern-form conventions; verify labels on the live wizard.

**SHA-256 (PDF):** `d8869e22d505f5b286f4f7ebd6abe451c4be657266b9d41dde540ecf9146fbda`

---

## Form-kit identity (Eightfold — never school email)

| Field | Answer |
| --- | --- |
| Legal First Name | Vedant |
| Legal Last Name | Desai |
| Legal Middle Name | (blank) |
| Email | **verdent06@gmail.com** |
| Phone | **248-704-4852** (Mobile) |
| Address | **49032 Freestone Dr**, Northville, MI **48168** |
| Date of birth | **12/16/2006** (if asked) |
| US citizen | **Yes** |
| Sponsorship now or later | **No** |
| Valid US driver's license | **Yes** (if asked) |
| SAT | **1510** (if asked) |
| GPA | **3.66 / 4.0** |
| Class | Junior · Expected **May 2028** · Summer 2027 = completed junior year / returning senior |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |

---

## Knockouts (answer factually)

| Question | Answer | Why |
| --- | --- | --- |
| U.S. citizen / U.S. person | **Yes** | Required for TS eligibility |
| Require visa sponsorship (incl. H-1B, F-1 OPT/CPT) | **No** | Citizen; posting is No H-1B |
| Authorized to work in the U.S. | **Yes** | Citizen |
| Currently hold a U.S. government clearance | **No** | Do not claim Secret/TS in-hand |
| Willing and able to obtain Top Secret | **Yes** | Citizen, clearance-eligible; JD required |
| Currently enrolled in CS / EE / Math / Physics / related | **Yes** | B.S. CS + Economics, UMich |
| Graduation date | **May 2028** | Still enrolled after Summer 2027 |
| Willing to work onsite Ypsilanti, MI Summer 2027 | **Yes** | Northville commute; valid US DL |
| GPA | **3.66** | No floor on this JD |
| Languages you can interview in | **C++, Python** | Or-list on the JD. Do **not** check Java, Rust, CUDA |

If a skills tagger appears, type only: C++, Python, AWS, Docker, Git, CMake. **Never** Java, Rust, CUDA, Jira, Linux (unnamed in inventory).

---

## Cover letter / additional information (≈160 words)

I am applying for the Software Engineer Intern role on CACI’s Radar and Sensor Technologies team in Ypsilanti for Summer 2027. I want to spend the summer turning algorithm definitions into software that has to be tested and reviewed — the work this posting describes, and the work I already do in C++ and in production Python.

The closest analog I have is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a `MemoryPool<Grain, 64>` slab per voice, deliver UI parameters through a lock-free SPSC FIFO, and only ship VST3/AU binaries after every `processBlock()` path is audited for zero heap allocations and zero lock acquisitions. I also implemented the granular scheduler (fractional accumulator, Gaussian-windowed grains) — prototype math into a running engine.

Alongside that I ship production software. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network I delivered a Flask REST API on AWS EC2 and replaced ~800 hours of manual PAC research with a Requests + Pandas ETL. SignalWeaver ships with Docker Compose and a GitHub Actions pipeline that runs pytest on every main build.

I do not have Java, Rust, or CUDA; C++ and Python are the languages I can defend. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), a U.S. citizen, and I do not currently hold a clearance. I can work on-site in Ypsilanti from Northville.

---

## "Why CACI / why RST / why Ypsilanti?" (≈90 words)

This site writes SAR, low-observables, and electro-optical software — taking algorithm prototypes into applications, then testing and reviewing them. That is already how I build: deterministic C++ on a hard-deadline thread, and Python services held to a test bar (pytest CI, production Flask on EC2). I live in Northville and can commute to Ypsilanti. I have not interned on radar; I will not invent SAR or CUDA. I want a summer on this RST team, not a generic IT intern seat in Reston.

---

## "Tell us about relevant technical experience." (≈120 words)

- **C++ / algorithms / real-time:** Granular synthesizer — `MemoryPool<Grain, 64>` so `processBlock()` never heap-allocates; lock-free SPSC; fractional-accumulator grain scheduler with a pre-computed Gaussian LUT; CMake VST3/AU builds audited for zero allocations and zero locks.
- **Python delivery (JD-listed language) + AWS (preferred):** Sole engineer, 5-month MCFN contract — Flask REST API on AWS EC2; Requests + Pandas ETL that removed ~800 hours of manual pulls across 400 PACs.
- **Test / CI:** SignalWeaver GitHub Actions (frontend build, pytest, API image on main). CaseStudyPrep: cut a 27% upload-failure rate with fault-tolerant RxJS.
- **Not in inventory:** Java, Rust, CUDA, Jira, a named Linux homelab, radar/EO coursework beyond Physics (Mechanics) + Calculus III.

---

## Availability

Summer **2027**, onsite Ypsilanti, MI (commute from Northville; valid US driver's license). Returning to Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Eightfold email = verdent06@gmail.com.** PDF header is still umich. Fix autofill.
- **Citizenship YES, clearance in-hand NO, TS willingness YES.**
- **Never claim Java, Rust, CUDA, Linux, Jira, or a radar internship.**
- **This is Ypsilanti RST (331648), not Sarasota SWE intern (331359) and not Reston IT.**
- **No CACI contact in `network.md`.** How did you hear: Company website / Internet search. Not employee referral.
- **Funnel:** resume is the bottleneck (`persona.md`). No published OA on this req. Do not assume the Sarasota OA.
- **Federal drug test** if selected (marijuana disqualifying even if legal in MI).
- **WORTH_IT.md is YES** — do not overwrite.
