# Intel — Software Engineering Intern, Bachelor’s (JR0286834) · Written Application Answers

Draft answers for Intel Workday req `JR0286834`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this.” **Form email: `verdent06@gmail.com` only.** Resume PDF header stays `vedantde@umich.edu` (do not edit the `.tex`). Do not invent Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, firmware internships, RTL, Verilog, SYCL, oneAPI, OpenVINO, CUDA, or Linux-as-a-skill. Trim to each form’s length limit before submitting.

This posting is the **Bachelor’s** catch-all SWE intern — **not** the graduate 🎓 sibling. Recruiting may route into applications, cloud, firmware, GPU software, middleware, research, system software, or validation. Prefer **Software Application / Cloud / Middleware**, then **System Software / Validation**. Do **not** volunteer firmware, GPU kernels, or oneAPI unless they ask, and then only as C++ real-time constraints from the synth — not device firmware or RTL.

Apply: https://intel.wd1.myworkdayjobs.com/en-us/external/job/US-Oregon-Hillsboro/Software-Engineering---Intern--Bachelor-s_JR0286834

Resume: `applications/2027/intel/software-engineering-intern-bachelors/Vedant Desai Resume.pdf`

**Do not submit from this file.** Artifacts only; no ATS apply.

---

## Cover letter

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Intel — University Recruiting
Hillsboro / Santa Clara / Folsom / Phoenix / Austin

Re: Software Engineering - Intern, Bachelor’s (JR0286834)

Dear Intel hiring team,

I am applying for the Bachelor’s Software Engineering Intern (JR0286834) for Summer 2027. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am authorized to work in the United States without visa sponsorship. I can work on-site at Hillsboro, Santa Clara, Folsom, Phoenix, or Austin. I remain enrolled after the internship (Fall 2027 and Winter 2028). This is the Bachelor’s req, not the graduate sibling.

This posting is software that enables Intel products and platforms — design, develop, test, debug, automate, validate — not a chip-design or ML-research seat. That is the work I already ship: a production REST API to a real stakeholder, C++ that cannot allocate on the hot path, and production debug when uploads fail.

What I would bring:

- **Shipped applications / data systems.** At Michigan Data Consulting I was the sole engineer on a five-month Michigan Campaign Finance Network contract. I replaced ~2-hour manual committee pulls with a Requests + Pandas ETL (eliminating ~800 hours of work across 400 tracked PACs) and shipped a production Flask REST API on AWS EC2 into their public research workflow.
- **C++ systems under a hard constraint.** I built a real-time C++/JUCE audio engine whose `processBlock()` path cannot allocate or take a lock: a `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering, shipped as VST3/AU binaries after a real-time safety audit. That is tools / system-software discipline, not a firmware or RTL internship. github.com/Verdent06/granular-synth
- **Debug, automation, validation.** At CaseStudyPrep.AI I closed a 27% audio-upload failure rate around expired S3 URLs (RxJS retry + MIME negotiation in Angular) and moved processing off the UI thread (<5ms main-thread blocking, 60 FPS). On Vylet I shipped a Dockerized pipeline with Redis/Celery workers and diagnosed a name-collision defect that lifted lead-qualification from 79% to 89% (live product, vyletdata.com).

I have not shipped SYCL, oneAPI, OpenVINO, CUDA, Verilog, or firmware. My production languages are Python and C++, plus TypeScript/JavaScript via Angular, SQL, HTML, PostgreSQL, Git, Docker, and AWS (EC2, S3). If the team sits on Linux system software or a firmware stack I will ramp rather than claim it. I develop on macOS and will ramp on Linux rather than list it as a skill I cannot defend.

I return to Michigan after the term (Expected May 2028). I would welcome the chance to walk through the MCFN API delivery or the `processBlock()` constraints.

Sincerely,
Vedant Desai

---

## Exact form questions visible on the posting

Pulled from the Workday JD without submitting. Further Workday fields were not captured. Do not invent unseen questions.

| Visible question / field | Answer |
| --- | --- |
| Email | **verdent06@gmail.com** (form only; override Workday autofill from the PDF if it pulls `vedantde@umich.edu`) |
| Req | JR0286834 — Bachelor’s SWE intern, not the graduate sibling |
| Locations: Hillsboro OR / Phoenix AZ / Folsom CA / Santa Clara CA / Austin TX | **Yes** — any of these; not Colorado (role is unavailable there) |
| On-site | **Yes** |
| This position is not eligible for employment-based visa sponsorship | **No conflict.** Authorized to work without sponsorship; answer **No** if a sponsorship question appears |
| Currently pursuing a Bachelor’s in CE / CS / Data Science / EE / Math / related STEM | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Available Spring / Summer 2027 (year-long intern/co-op also considered) | **Yes** — targeting **Summer 2027** on-site. Spring 2027 or year-long only if the calendar still returns me to Michigan after (Expected May 2028) |

---

## Knockout / structured fields (fill if Workday asks)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | **verdent06@gmail.com** |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/intel/software-engineering-intern-bachelors/Vedant Desai Resume.pdf` |
| Cover letter | Paste the letter above if an Additional Information / Cover Letter box exists |
| Location preference | **Any of:** Hillsboro OR, Santa Clara CA, Folsom CA, Phoenix AZ, Austin TX. Rank if forced: Santa Clara, Hillsboro, Austin, Folsom, Phoenix. Do not select Colorado. |
| Willing to relocate / work on-site | **Yes** |
| Currently enrolled Bachelor’s CS (or related STEM)? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Expected graduation | **May 2028** |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** |
| Work authorization | Authorized to work in the US without visa sponsorship. Answer Workday work-rights questions **truthfully**. Do not guess citizenship if the form asks it separately. |
| Will you now or in the future require visa sponsorship? | **No** |
| Term preference | **Summer 2027** full-time on-site. Spring 2027 or year-long intern/co-op only if asked and I still return to Michigan after. |
| Comp $95,698–$95,702 USD annualized (hourly intern role) | **Yes** — accept the posted intern range; actual rate depends on degree/location |
| How did you hear about this role? | **Company career site** (Intel Workday / jobs.intel.com, JR0286834). If a source list appears and none fit: **LinkedIn Jobs**. |
| Languages you can interview in | **C++, Python, SQL, TypeScript/JavaScript (Angular), HTML.** Do **not** check SYCL, oneAPI, OpenVINO, CUDA, Verilog, firmware, Snowflake, Databricks, Tableau, Copilot, Fusion, or Sentry. |

Workday often has no screening essays on the JD page. Paste the cover letter into Additional Information / Cover Letter if a box exists. Skip optional self-ID unless required (`recruiting.md`: fill required fields, keep volume high).

---

## “Why Intel / why this internship?”

I want a summer writing software that has to be correct next to real compute — applications, tools, C++ systems — not a generic web rotation and not a fabricated chip-design internship. Intel is the company that still owns the full stack from silicon through the software that enables products and platforms. This req is B for SWE, not chip engineering: design, build, test, debug, automate, validate.

The work I can defend:

- **Applications / cloud / middleware.** Sole engineer on a five-month MCFN contract: Requests + Pandas ETL and a production Flask REST API on AWS EC2. Vylet is a Dockerized pipeline with Redis/Celery (live product, vyletdata.com).
- **System software / tools, honestly scoped.** Real-time C++ whose audio thread cannot allocate or lock (`MemoryPool<Grain, 64>`, lock-free SPSC, `processBlock()` safety audit). That is engineering-tools and performance work, not RTL, firmware, or a oneAPI internship.

I can be on-site at Hillsboro, Santa Clara, Folsom, Phoenix, or Austin for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

---

## “Tell us about a project you built” / additional information

Two that map onto this req without inflating the stack:

**MDC (applications).** Production Flask REST API on AWS EC2 plus a Requests + Pandas ETL that removed ~800 hours of PAC research. Closest analog to “design, develop, test, debug” software that other people actually used.

**Granular synthesizer (C++ systems).** github.com/Verdent06/granular-synth. Zero-allocation audio thread, lock-free UI-to-audio FIFO, VST3/AU release binaries after a real-time safety audit (no heap, no locks in `processBlock()`). Closest analog to system-software / validation discipline next to hardware — still DSP, not firmware.

---

## Availability

Summer 2027 full-time on-site at any listed US site (Hillsboro, Santa Clara, Folsom, Phoenix, Austin — not Colorado). Returning to the University of Michigan after the internship (Expected May 2028). Spring 2027 or year-long intern/co-op only if Intel asks and the calendar still returns me to school.

---

## Notes for the applicant (not for submission)

- **Form email is `verdent06@gmail.com` only.** If Workday autofills `vedantde@umich.edu` from the PDF, overwrite it before submit.
- **Lead with MDC (shipped API/ETL) and Granular (C++ systems).** CaseStudyPrep is the debug story. Vylet’s LangGraph story is production ownership, not “I want to do agents at Intel.”
- **Do not claim SYCL, oneAPI, OpenVINO, CUDA, Verilog, firmware, RTL, Linux-as-a-skill, Snowflake, Databricks, Tableau, Copilot, Fusion, or Sentry.** Honest C++ + Python + SQL + JS-family beats a knockout lie.
- **Granular has no latency/xrun/CPU number on the page.** If asked, describe the audio-thread constraints and what you would measure — do not invent a metric.
- **Location is not a skip.** Say yes to on-site at a listed site. Do not pick Colorado.
- **Sponsorship is a knockout on this req.** Answer **No**.
- **Catch-all posting:** recruiter routes into applications/cloud/system-software if the page fits. Apply anyway; after the PDF the remaining filter is Easy–Med HackerRank (`companies.md`: bottleneck resume, then OA, ~5–8%).
- **This is JR0286834 Bachelor’s.** Do not apply this packet to the graduate sibling.
- **Referral:** no Intel contact in `network.md`. A UMich alum at Intel still beats a cold Workday pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Do not apply from this file automatically.**
