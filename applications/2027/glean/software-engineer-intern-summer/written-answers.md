# Glean — Software Engineer, Intern (Summer 2027) · Written Application Answers

Paste-ready answers for Greenhouse **4595665005** (`requisition_id` 643; `internal_job_id` 4388122005). Captured **2026-10-02** from `https://boards-api.greenhouse.io/v1/boards/gleanwork/jobs/4595665005?questions=true` plus the live job board page. Grounded in `persona.md` (full-stack SWE intern + work-AI / enterprise search — **not** ML-research, **not** Go/K8s) and `context.md` only.

**Do not invent:** Go, Java, Kubernetes, Elasticsearch, Glean connectors, Copilot, Snowflake, Databricks, a Glean internship, Spring 2027 graduation.

**Form-kit identity (use on Greenhouse — never `vedantde@umich.edu`):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · Address **49032 Freestone Dr, Northville, MI 48168** · US citizen, no sponsorship · GPA **3.66** · Expected **May 2028** · Junior · LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06

Resume PDF header uses **verdent06@gmail.com**.

Apply (do **not** submit from this agent):

- ATS: https://job-boards.greenhouse.io/gleanwork/jobs/4595665005
- Questions: https://job-boards.greenhouse.io/gleanwork/jobs/4595665005 (form on the same page; API: `?questions=true`)

**This agent did not submit.** Form fields captured from the live Greenhouse page + boards-api `?questions=true` (2026-10-02).

**SHA-256:** `21b9120e93cc08b0a90c90efe680262e6a7fa24654a392bda4371f580bc289c1`

Airtable: `recPhAx0nGNR5b4cG` (GrokBot Applications; Source **GitHub/SimplifyJobs**; Status stays **In Progress** until a human submits).

**Employment on the form: CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead Ambassador are extracurricular. Awards: **None**. Lyndbrook Capital: omit.

---

## Knockouts (read first)

1. **Printed JD graduation window.** About you: "Graduating in Fall 2026 or Spring 2027." Honest answer is **Expected May 2028**. There is **no graduation-date field** on the live form. The PDF still shows May 2028. Do **not** pick or type Spring 2027. Same Greenhouse id was previously titled Summer 2026; title now says Summer 2027 — treat the printed window as a possible auto-reject (`recruiting.md` Part I §1). `grade.md`: ineligible on the literal text.
2. **Hybrid policy \*.** Helper on the form: "We work out of the Palo Alto office on Monday, Wednesday, and Friday." JD body: hybrid **4 days a week** in Mountain View or San Francisco. Answer **Yes.** Relocate from Northville, MI for the term. Home city stays Northville.
3. **Work authorization / sponsorship.** Not on this public form. If a later step asks: US citizen · **Yes** authorized · **No** sponsorship.

Binary knockouts auto-reject. Do not lie on class year, hybrid, or sponsorship.

---

## Identity (live Greenhouse)

| Exact label | Required | Answer |
| --- | --- | --- |
| First Name | * | Vedant |
| Last Name | * | Desai |
| Email | * | **verdent06@gmail.com** |
| Phone | * | 248-704-4852 |
| Resume/CV | * | attach `applications/2027/glean/software-engineer-intern-summer/Vedant Desai Resume.pdf` |
| Cover Letter | | optional — skip for volume, or paste the draft below |
| LinkedIn Profile | * | https://linkedin.com/in/vedantde06 |
| Website | | https://github.com/Verdent06 (or https://vyletdata.com) |

If a Location / City widget appears (not in `questions[]`; `location_questions` was empty): **Northville, Michigan, United States**. Do not spoof Mountain View or Palo Alto.

---

## Education (Greenhouse `education_required`)

API sets `"education":"education_required"`. Fill the standard widget if it appears.

| Exact label | Answer |
| --- | --- |
| School | University of Michigan |
| Degree | Bachelor's |
| Discipline | Computer Science (dual CS + Economics is on the PDF; do not invent a second row unless required) |
| Start date | **August** **2025** |
| End date | **May** **2028** (expected; not graduated) |

If a second education row is required: Northville High School, Northville MI, graduated **05/19/2025**.

---

## Custom questions (exact live labels)

| Exact label | Required | Answer |
| --- | --- | --- |
| What is your GPA? | * | **3.66** |
| Are you willing and able to commit to the hybrid policy if hired? | * | **Yes** (helper: Palo Alto Mon/Wed/Fri; JD also says 4 days/week MV or SF) |
| How did you hear about Glean? | * | **Job Board** — Airtable source is GitHub/SimplifyJobs. Live options: Conference · Glean Career Site · Job Board · LinkedIn · On Campus Event · Podcast · Referred by Glean Employee · Social Media · Virtual Event · Word of Mouth · Other. **Do not pick Referred by Glean Employee** — no Glean contact in `network.md` |
| Please input the total years of experience you have that are relevant for this role. | * | **1** (SWE co-op Dec 2025–May 2026 plus founded Vylet May 2026–present; do not inflate) |
| What AI tools are you currently using today and how are you using them? | * | Paste **AI tools** below |

---

## AI tools * (paste)

I use Cursor as my daily coding environment. In shipped work I use Gemini (and other LLM APIs) inside LangGraph agent pipelines on Vylet, LangSmith for an eval harness that lifted extraction faithfulness from 50% to 90%, ONNX Runtime with Silero VAD for client-side inference at CaseStudyPrep.AI (40% cloud-inference cost cut), and pgvector semantic search plus a LoRA-tuned Llama 3.1 8B on SignalWeaver. I have not used Glean. I do not claim Copilot, Kubernetes, or a Glean connector.

---

## Form employment — only these two

Do **not** add MDC, Lyndbrook, or SpaceXAI Campus Lead as jobs.

### 1. Vylet (current)

| Field | Answer |
| --- | --- |
| Job Title | Founder |
| Company | Vylet |
| Location | Northville, MI |
| Current | Yes |
| From | May 2026 |
| To | Present |
| Description | Founded Vylet (vyletdata.com), a live PE/search-fund lead-sourcing product ($1,500 MRR, three clients). Dockerized LangGraph pipeline with Redis/Celery (30 scored leads in 30 minutes, 30x). RCA on a name-collision defect that lifted qualification 79%→89%. Python/TypeScript. No Go or Kubernetes. |

### 2. CaseStudyPrep.AI

| Field | Answer |
| --- | --- |
| Job Title | Software Engineer Co-op (Voice AI) |
| Company | CaseStudyPrep.AI |
| Location | Remote |
| Current | No |
| From | Dec 2025 |
| To | May 2026 |
| Description | Titled SWE co-op. Cut cloud inference cost 40% with client-side Silero VAD (ONNX Runtime). Recovered a 27% audio upload failure rate with RxJS + expired S3 presigned URLs. Angular/TypeScript. No Go. |

### Extracurriculars (if a section exists)

| Item | How to log |
| --- | --- |
| Michigan Data Consulting (MDC) | Extracurricular / organization. Data Engineer for MCFN via MDC · Jan 2026 – May 2026 · Ann Arbor. On the PDF Experience block as a delivery analog — **do not add a second job row**. |
| SpaceXAI Campus Lead Ambassador | Extracurricular only. Not on this PDF. Do not invent duties or metrics. |

### Awards / honors

**None.** Leave blank.

---

## Cover letter (optional — skip unless you want it)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Glean Engineering — Software Engineer, Intern (Summer 2027)
Greenhouse 4595665005 · Mountain View / Palo Alto hybrid

I want to spend summer 2027 in the Bay Area building production software next to Glean's search and agent stack — backend, product, or ML/AI/search — not a research-paper rotation. I have not used Go, Kubernetes, or Glean, and I will not pretend I have.

The work I can defend: CaseStudyPrep.AI (Software Engineer Co-op) — Silero VAD via ONNX Runtime, 40% cloud-inference-cost cut; RxJS + expired S3 URLs, 27% upload-failure recovery. Vylet (vyletdata.com) — Dockerized LangGraph + Redis/Celery (30 scored leads in 30 minutes); name-collision fix 79%→89% qualification; $1,500 MRR. SignalWeaver — pgvector semantic search (49ms p50) + FastAPI + React/TypeScript + GitHub Actions CI. Michigan Data Consulting — Flask REST API on AWS EC2, sole engineer on a five-month nonprofit contract.

U.S. citizen; no immigration sponsorship. B.S. Computer Science and Economics, University of Michigan (Expected May 2028, GPA 3.66, Junior). I can work the hybrid policy (Palo Alto Mon/Wed/Fri and/or 4 days/week in Mountain View or San Francisco).

Vedant Desai

---

## EEO / demographic (voluntary)

Live compliance questions: Veteran Status, Race, Gender. Not used in hiring (`recruiting.md` Part I §2). **I don't wish to answer** / **Decline To Self Identify** unless you choose to self-ID.

| Field | If you skip | If you self-ID |
| --- | --- | --- |
| Veteran Status | **I don't wish to answer** | I am not a protected veteran |
| Race | **Decline To Self Identify** | Asian |
| Gender | **Decline To Self Identify** | Male |

Disability CC-305 was **not** in the API payload. If a later page appears, skip unless required.

Privacy / arbitration: the JD conclusion asks you to confirm you have read Glean's Privacy Policy and Applicant Arbitration Agreement when you click Submit. That is a human submit-time click — this agent does not click it.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Greenhouse field.** Do not type `vedantde@umich.edu`.
- **Grad year is May 2028.** The JD's Fall 2026 / Spring 2027 line is a possible knockout. Do not lie.
- **Hybrid = Yes.** Home city stays Northville.
- **How heard = Job Board** (Simplify/GitHub). No employee referral.
- **Years relevant = 1.**
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead are extracurricular. Awards: **None**. Lyndbrook: omit.
- **Do not invent Go, Java, Kubernetes, Elasticsearch, Glean usage, or Spring 2027 graduation.**
- **Resume is the first gate; 1hr coding + 2hr project next** (`companies.md` / `recruiting.md` startup human-read). No named intern OA.
- Comp: $57–$69/hr (JD). Hybrid MV/SF 4 days or Palo Alto M/W/F.
- Cover letter: skip unless you want it.
- **This pack was not submitted.**
