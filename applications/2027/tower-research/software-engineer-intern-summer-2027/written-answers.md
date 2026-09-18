# Tower Research Capital — Software Engineer Intern (Summer 2027) · Screening Answers

Draft answers for Tower’s Greenhouse apply on `tower-research.com` (job **8212158**). Grounded in the **live posting opened in a browser 2026-09-18**, `persona.md` (full-stack intern + low-latency / HFT trading-systems / market-data differentiator — **not** Quant Trader, **not** Quant Developer, **not** Tower Research Ventures fullstack, **not Java/Go/Rust/FPGA**, **not** a trading desk), `grade.md` Interview angles, and `context.md` metrics only.

Apply (do **not** submit from this agent):

- https://www.tower-research.com/open-positions/?gh_jid=8212158

Direct `boards.greenhouse.io/towerresearch/jobs/8212158` is **dead** (“job board no longer active”). Use the branded careers URL.

**This agent did not submit.** Form fields captured from the live Apply embed (2026-09-18). No long-form essay on the form. Cover letter is optional.

**SHA-256:** `2afa1b226fd9744041b2772bf578a5e780c246287b79dcee01e3cc5c74ab3f40`

**Form-kit identity (use on Greenhouse — never `vedantde@umich.edu`):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · Address **49032 Freestone Dr, Northville, MI 48168** · US citizen, no sponsorship · GPA **3.66** · Expected **May 2028** · Junior · LinkedIn https://www.linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06 · SAT **1510** if asked · DOB **12/16/2006** if asked · valid US DL **Yes** if asked.

PDF header is **verdent06@gmail.com**. Still overwrite autofill if anything else appears.

**Employment on the form: CaseStudyPrep.AI SWE co-op + founder Vylet only.** MDC and SpaceXAI Campus Lead Ambassador are **extracurricular**, not employment. Awards / honors: **None**. Lyndbrook Capital: omit.

---

## Identity (live Greenhouse)

| Exact label | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | **verdent06@gmail.com** |
| Country * | **United States** |
| Phone * | **248-704-4852** |
| Location (City) * | **Northville, Michigan, United States** (Locate me if it resolves to Northville; not Ann Arbor) |
| Resume/CV * | attach `applications/2027/tower-research/software-engineer-intern-summer-2027/Vedant Desai Resume.pdf` (pdf) |
| Cover Letter | optional — paste the draft below, or attach as pdf/docx |
| LinkedIn Profile | https://www.linkedin.com/in/vedantde06 |
| Website | leave blank, or https://vyletdata.com if a box is required. GitHub is on the PDF. |

---

## Education widget (required)

Greenhouse typeahead (`Select...`). This agent did not create an account or exhaust the school catalog.

| Exact label | Answer |
| --- | --- |
| School * | Type **University of Michigan**. Also try **University of Michigan-Ann Arbor** / **University of Michigan - Ann Arbor**. If the catalog misses it, pick the closest official row — do not invent a school. |
| Degree * | **Bachelor's** / **Bachelor of Science** if listed |
| Discipline * | **Computer Science** (dual CS + Economics is on the PDF; do not invent a second row unless required) |
| Start date month * / year * | **August** **2025** |
| End date month * / year * | **May** **2028** (expected; not graduated) |

If a second education row is required: Northville High School, Northville MI, graduated **05/19/2025**.

---

## Additional required fields (live form)

| Exact label | Answer |
| --- | --- |
| Current University * | **University of Michigan** |
| Expected Graduation Date * | **May 2028** |
| Major(s) * | **Computer Science and Economics** |
| Preferred Programming Language(s) * | **C++, Python** — the languages you can interview in. Do **not** add Golang, Java, or Rust. TypeScript is honest secondary if they want a comma list; it is not the HFT screen. |

---

## Knockouts / compliance (required)

| Exact label | Answer | Why |
| --- | --- | --- |
| Do you currently have an offer? If so, what is your deadline to make a decision by? * | **No** | Tracker: 0 offers. If that changes, put company + date only — no invented exploding offer. |
| Where are you currently located? * | **Northville, Michigan** | Home address. Not Ann Arbor unless you are on campus the day you apply. |
| How did you hear about this job? * | **Company website** | No Tower contact in `network.md`. Not employee referral. Internet search is the fallback. |
| Are you or have you been entrusted with a position or function in any government, international organization (such as the UN or World Bank), or state-controlled or state-owned bank, brokerage firm, or other enterprise? * | **No** | Not a PEP. |
| Are you an immediate family member of someone holding such a position? An immediate family member is a parent, sibling, spouse or domestic partner, child, or in-law. * | **No** | |
| Are you currently authorized to work for all employers in the United States on a full-time basis? * | **Yes** | US citizen |
| Will you now or in the future require sponsorship for employment visa status (e.g., H-1B status)? * | **No** | US citizen; no sponsorship. If the box is a text area, write **No — U.S. citizen; I will not require sponsorship now or in the future.** |
| Have you been employed by Tower Research Capital before? * | **No** | |
| Were you referred to this role by a current Tower Research Capital employee? If so, please provide their name. * | **No** | Leave no fake name. |

GPA is **not** on this form. If a later wizard asks: **3.66**.

---

## Cover letter (optional)

Public form has an optional Cover Letter attach/paste. Use only if you want a human extra; skip if you are volume-applying. ~170 words.

I am applying to Tower Research Capital’s Software Engineer Intern role for Summer 2027 in New York. I want a summer writing software that has to be fast and correct — latency-sensitive systems, market- and reference-data pipelines, trading-platform code — not a Quant Trader seat and not a generic product-SWE internship.

The closest analog I have to low-latency production work is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a `MemoryPool<Grain, 64>` slab per voice and deliver UI parameters through a lock-free SPSC FIFO so `processBlock()` never blocks on the heap or a mutex.

Alongside that I ship Python ingestion and APIs. I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and delivered a production Flask REST API on AWS EC2, and I built SignalWeaver as a financial-research assistant (not investment advice) with measured p50/p99 on FastAPI scoring and pgvector search. SQL shows up in production: an asyncpg data layer with injection-safe timestamp validation.

I do not have Golang, Java, Rust, or FPGA; C++ and Python are the languages I can defend. I do not have a trading-desk internship. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), a U.S. citizen, and I can work onsite in New York for Summer 2027.

---

## "Why Tower?" / "Why this internship?" (only if a later wizard has a box)

Tower is independent PM teams on a shared high-performance platform. This posting is the engineering side of that platform — systems programming to cut latency, data pipelines with fast access, algo-trading systems — which is the intern job I want, not QR. I already practice the two signals this screen rewards: lock-free C++ under a hard real-time constraint, and Python/SQL pipelines that have to be correct in production. I will not invent Java, Go, Rust, FPGA, or a desk.

---

## Preferred languages / skills tagger

Type only what is in inventory and on the PDF: **C++**, **Python**, **SQL**, **TypeScript**. Linux is named on the JD; there is no Linux line in the inventory — **do not claim it**. Never Java, Golang, Rust, FPGA, Snowflake, Databricks, Copilot, Fusion, or Tableau.

---

## Work history if Autofill creates rows

Greenhouse here is resume + education, not a full Workday job history. After Autofill from the PDF or LinkedIn:

| Entry | Form treatment |
| --- | --- |
| CaseStudyPrep.AI — Software Engineer Co-op (Voice AI), Dec 2025–May 2026 | **Employment.** Keep. |
| Vylet — Founder, May 2026–Present | **Employment.** Keep. |
| Michigan Data Consulting (MDC) | **Extracurricular only**, even though it is on the PDF. Move off Work Experience if Autofill files it as a job. |
| SpaceXAI Campus Lead Ambassador | **Extracurricular only.** Not on this PDF. Do not invent duties or metrics. |
| Lyndbrook Capital | Omit. Not a form-kit job. |
| Granular / SignalWeaver | Projects on the PDF. Do not log as jobs. |
| Awards / honors | **None** |

---

## Demographics (voluntary)

Skip, or complete only if you want. Not used in this packet.

---

## Notes for the applicant (not for submission)

- **Email = verdent06@gmail.com.** Fix autofill. Never umich.
- **No essay on the public form.** Do not invent one. Cover letter is optional.
- **Languages or-list, not a Java/Go/Rust gate.** Interview in C++ or Python. Honest gap if they press Golang/Java/Rust/FPGA.
- **Linux:** JD qualification; not in inventory. Do not claim it on the form.
- **Grad window:** Expected May 2028. Junior. Summer 2027 onsite NYC. Returns to Michigan after.
- **Citizenship YES, sponsorship NO.** No clearance gate on this posting.
- **No Tower contact in `network.md`.** How did you hear: Company website. Not employee referral.
- **OA is the real gate** after the resume (`recruiting.md` intern OA; quant/HFT is CP + math heavy, <1–2%). Timed C++/Python until a medium is a ~20-minute solve; add SQL and probability. Resume polish will not hire you here.
- **This agent did not apply.**
