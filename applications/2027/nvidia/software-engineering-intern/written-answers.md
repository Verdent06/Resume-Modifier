# NVIDIA — 2027 Internships: Software Engineering Intern (JR2023495) · Written Application Answers

Draft answers for Workday req `JR2023495`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented CUDA, Java, Go, Kubernetes, Jenkins, Ansible, Perforce, TensorRT, or cuDNN. Trim to the form's length limit before submitting.

This posting is a **catch-all**. Recruiting may route you to Development Tools, Cloud, Tools Infrastructure, or Machine Learning Operations. Prefer **Tools Infrastructure**, then **Cloud**, then **Development Tools**. Do **not** volunteer MLOps unless they ask, and then only as ONNX Runtime on-device inference + Dockerized Python pipelines — not CUDA training stacks.

Apply: https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Software-Engineering_JR2023495

Resume: `applications/2027/nvidia/software-engineering-intern/Vedant Desai Resume.pdf`

---

## Cover letter

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

NVIDIA — University Recruiting
Santa Clara, CA

Re: NVIDIA 2027 Internships: Software Engineering Intern (JR2023495)

Dear NVIDIA hiring team,

I am applying for the 2027 Software Engineering intern program (12-week, full-time). I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work the Santa Clara term, and I remain enrolled after the internship (Fall 2027 and Winter 2028). Other 2027 applications in this repo state I am authorized to work in the United States without visa sponsorship — I will answer Workday work-rights questions truthfully and will not invent citizenship.

NVIDIA builds the accelerated-computing stack other people build on. This posting is a catch-all into Development Tools, Cloud, Tools Infrastructure, or MLOps — design, debug, and ship software, not a research-paper seat. That is the work I already do: a production REST API to a real stakeholder, C++ that cannot allocate on the hot path, and on-device inference that cut cloud cost.

What I would bring:

- **Production backend + stakeholder delivery.** At Michigan Data Consulting I was the sole engineer on a five-month Michigan Campaign Finance Network contract. I replaced ~2-hour manual committee pulls with a Requests + Pandas ETL (eliminating ~800 hours of work across 400 tracked PACs) and shipped a production Flask REST API on AWS EC2 into their public research workflow.
- **C++ systems under a hard constraint.** I built a real-time C++/JUCE audio engine whose `processBlock()` path cannot allocate or take a lock: a `MemoryPool<Grain, 64>` slab per voice and a lock-free SPSC FIFO with atomic acquire/release ordering, shipped as VST3/AU binaries after a real-time safety audit. That is Tools Infrastructure / performance work, not a CUDA-kernel internship. github.com/Verdent06/granular-synth
- **Inference-adjacent and cloud/debug.** At CaseStudyPrep.AI I ran Silero VAD client-side via ONNX Runtime and cut cloud inference cost 40%, then closed a 27% audio-upload failure rate around expired S3 URLs. On Vylet I shipped a Dockerized pipeline with Redis/Celery workers and injection-safe SQL freshness checks (live product, vyletdata.com).

I have not shipped CUDA, Java, Go, Kubernetes, Jenkins, Ansible, or Perforce. My production languages are Python and C++, plus TypeScript/JavaScript via Angular and SQL. If the team sits on CUDA or a JVM service I will ramp rather than claim it. I am not applying as an MLOps-CUDA intern.

I return to Michigan after the term (Expected May 2028). I would welcome the chance to walk through the MCFN API delivery or the `processBlock()` constraints.

Sincerely,
Vedant Desai

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/nvidia/software-engineering-intern/Vedant Desai Resume.pdf` |
| Location preference | **US-CA-Santa Clara**. If Canada is offered on the same intern program, it is acceptable — Santa Clara is the target. |
| Willing to work onsite / relocate | **Yes** — Santa Clara for the 2027 12-week term. |
| Currently enrolled in BS/MS/PhD in EE/CE or related for the full internship? | **Yes** — B.S. Computer Science and Economics, University of Michigan. CS is the related field. Enrolled through the internship. |
| Will you return to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain after a Summer 2027 term. |
| Graduation date | **May 2028** (month and year; required on the resume — already on the PDF) |
| GPA | **3.66 / 4.0** (only if the form asks) |
| Work authorization / sponsorship | Other 2027 applications in this repo state you are authorized to work in the US **without visa sponsorship**. Answer the Workday work-rights question **truthfully**. Do not guess citizenship if the form asks it separately. |
| How did you hear about this role? | **Company career site / Workday** (NVIDIA External Career Site). If a referral source list appears and none fit: **LinkedIn Jobs**. |
| Comp $20–71/hr + intern benefits | **Yes** — accept the posted intern range |
| Languages you can interview in | **C++, Python, SQL, TypeScript/JavaScript (Angular)**. Do **not** check CUDA, Java, Go, C (as distinct from C++), Kubernetes, Jenkins, Ansible, Perforce, TensorRT, or cuDNN. |

Workday often has no screening essays on the JD page. Paste the cover letter into Additional Information / Cover Letter if a box exists. Skip optional self-ID unless required (`recruiting.md`: fill required fields, keep volume high).

---

## "Why NVIDIA / why this internship?"

I want a summer writing software that has to be correct next to real compute — developer tools, cloud/data platforms, C++ systems — not a generic web rotation. NVIDIA is the company that made accelerated computing the default substrate for AI and graphics. That is more interesting to me than another intern seat on a CRUD app.

The work I can defend:

- **Tools Infrastructure / Development Tools.** I shipped C++ whose audio thread cannot allocate or lock (`MemoryPool<Grain, 64>`, lock-free SPSC, `processBlock()` safety audit) and I debug production failures (27% S3 upload failures closed with RxJS retry). That is engineering tools and performance work. I have not interned on CUDA kernels, Jenkins farms, or chip-design methodologies, and I will not pretend to.
- **Cloud / data platforms.** Sole engineer on a five-month MCFN contract: Requests + Pandas ETL and a production Flask REST API on AWS EC2. Vylet is a Dockerized pipeline with Redis/Celery and an asyncpg data layer. SignalWeaver semantic search at 49ms p50 / 99ms p99.

I can be onsite in Santa Clara for the 2027 12-week term. I return to Michigan afterward (Expected May 2028).

---

## "Tell us about a project" paste

Two that map onto this req without inflating the stack:

**Granular synthesizer (C++ systems).** github.com/Verdent06/granular-synth. Zero-allocation audio thread, lock-free UI-to-audio FIFO, VST3/AU release binaries after a real-time safety audit (no heap, no locks in `processBlock()`). Closest analog I have to Tools Infrastructure — performance, memory, debugging — still DSP, not CUDA.

**MDC / CaseStudyPrep (cloud + inference-adjacent).** Production Flask API on EC2; ONNX Runtime client-side VAD that cut cloud inference cost 40%. Live product work at vyletdata.com if they want Docker/SQL ownership.

---

## Preferred intern track (the four JD buckets)

If the form lets you pick or a recruiter asks:

1. **Tools Infrastructure** — C++, Python, JavaScript-family (Angular), Git, Docker. Matches the JD's Unix/Linux/C++/Python/Git/containers list without claiming Kubernetes, Java, Go, CUDA, or Perforce.
2. **Cloud** — AWS EC2/S3, Docker, data/API delivery, debugging storage-adjacent upload failures.
3. **Development Tools** — only as debugging / performance / engineering-tools (the synth + CaseStudyPrep defect work), not Jenkins or OS-internals coursework I do not have.
4. **Machine Learning Operations** — **do not volunteer.** If asked: "I have not written CUDA, cuDNN, NCCL, or TensorRT. I have shipped ONNX Runtime on-device inference and Dockerized Python pipelines. I would ramp on the team's GPU stack."

---

## Availability

2027 internships program, ~12 weeks full-time, onsite Santa Clara. Available to start May 2027 (or NVIDIA's intern calendar). Returning to the University of Michigan after the internship.

---

## Notes for the applicant (not for submission)

- **Do not claim CUDA, Java, Go, C, Kubernetes, Jenkins, Ansible, Perforce, TensorRT, cuDNN, NCCL, SLURM, LSF, Snowflake, Databricks, Copilot, Fusion, or Tableau.** The JD lists them as role-dependent. Your pool does not have them. Honest C++ + Python + SQL + JS-family beats a knockout lie.
- **Do not write a cover letter that sounds like an MLOps intern.** Lead with MDC (shipped API/ETL) and Granular (C++ systems). CaseStudyPrep ONNX is the honest inference-adjacent story. Vylet's LangGraph story is production ownership, not "I want to train models at NVIDIA."
- **Graduation date is a stated filter.** The PDF already has Expected May 2028. Re-enter month+year on Workday; do not leave year-only.
- **Location is not a skip.** Say yes to Santa Clara.
- **Catch-all posting:** recruiter outreach if experience fits; an immediate team match is not guaranteed. Apply anyway; after the PDF the bottleneck is tech rounds (`companies.md`: ~2–4%).
- **Referral:** no NVIDIA contact in `network.md`. A UMich alum at NVIDIA still beats a cold Workday pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Do not apply from this file automatically.** Resume + letter only unless you choose to submit.
