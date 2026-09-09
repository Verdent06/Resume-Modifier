# Two Sigma — Software Engineering Internship (Summer 2027) · Avature answers

Draft answers for the live Avature apply on `twosigma.avature.net` (JobDetail **14016**). Grounded in `persona.md` (full-stack SWE screen + high-performance trading / data-ingestion differentiator — **not** QR, **not** a trading desk, **not** Java/C/Ruby/Perl invention). First-person, honest, defensible under "walk me through this."

**Form-kit email is `verdent06@gmail.com`. Never use `vedantde@umich.edu` on Avature.** Resume PDF header still shows the UMich address (template-fixed). That is the document. The **form** uses Gmail.

**Do not invent Java, C, Ruby, Perl, a trading-desk internship, Snowflake, Databricks, Copilot, Fusion, or Tableau.** Honest stack: C++, Python, AWS, Docker, Git. Trim to each field's limit before submitting.

**Employer / title / location from the live page (2026-09-09):** Two Sigma (Two Sigma Investments, LP) · **Software Engineering Internship (Summer 2027)** · NY New York, United States · Soho-based New York City office · Investment Management / Engineering · Internship · **10 weeks** · **$3,800/Week (Bachelor's)** · Hybrid Work Policy (internship takes place at the Soho office) · general SWE role, team match 2–3 months before start.

**Prefer this ATS URL:**
https://twosigma.avature.net/careers/JobDetail/14016

**This agent did not submit.** Avature apply flow visible without an account: Login / Create Account → Upload Resume → About You → Role Specific Questions → Confirm Application. **Exact Role Specific Questions were not readable** — account creation is required before that step. Prompts below marked *inferred* are typical Avature / Two Sigma intern screening boxes, not copied from the live wizard. If the live labels differ, answer the live wording; do not invent extra essays.

**SHA-256 (PDF):** `3b489519ccc3ab20fced61cb7a2d31878d50376930dc8cfb20f0d3c61994fb3b`

---

## Form-kit identity (Avature — never school email)

| Field | Answer |
| --- | --- |
| Legal First Name | Vedant |
| Legal Last Name | Desai |
| Legal Middle Name | (blank) |
| Email | **verdent06@gmail.com** |
| Phone | **248-704-4852** (Mobile) |
| Address | **49032 Freestone Dr**, Northville, MI **48168** |
| US citizen | **Yes** |
| Sponsorship now or later | **No** |
| Authorized to work in the U.S. | **Yes** |
| GPA | **3.66 / 4.0** |
| Class | Junior · Expected **May 2028** · Summer 2027 = after sophomore year / rising junior (`context.md`) |
| Degree / major | B.S. Computer Science and Economics, University of Michigan |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |

---

## Knockouts (answer factually)

| Question | Answer | Why |
| --- | --- | --- |
| U.S. citizen / authorized to work | **Yes** | Citizen; no visa |
| Require visa sponsorship (now or later) | **No** | Citizen |
| Currently enrolled in a technical or quantitative degree | **Yes** | B.S. CS + Economics, UMich — JD bar |
| Graduation date | **May 2028** | Still enrolled after Summer 2027 |
| Willing to work the 10-week program onsite Soho NYC, Summer 2027 | **Yes** | Can relocate for the summer |
| GPA | **3.66** | No published floor on this JD |
| Languages you can interview in | **C++, Python** | JD is an OR list. Do **not** check Java, C, Ruby, or Perl |
| Prior Two Sigma application / employee | **No** | Unless that changes |
| Financial / trading-desk experience | **No** | JD: financial experience is not required. Do not invent a desk |

If a skills tagger appears, type only: C++, Python, AWS, Docker, Git. **Never** Java, Ruby, Perl, Snowflake, Databricks, Copilot, Fusion, Tableau.

---

## Optional cover letter / additional information (*inferred* — cover letters are not typical on this Avature intern req)

Use only if Avature shows a cover-letter upload, "Additional information," or a free-text box. Community + official JDs do not treat a cover letter as required. ~160 words.

I am applying for Two Sigma’s Software Engineering Internship in Soho for Summer 2027. I want a 10-week project on the infrastructure this posting describes — reliability of mission-critical systems, low-latency execution, and pipelines that ingest data at scale — not a quant-research seat and not a generic product-SWE summer.

The closest analog I have is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a `MemoryPool<Grain, 64>` slab per voice and deliver UI parameters through a lock-free SPSC FIFO so `processBlock()` never blocks on the heap or a mutex. That is the high-performance systems work I can walk line by line.

Alongside that I ship Python ingestion and APIs. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and delivered a production Flask REST API on AWS EC2. SignalWeaver serves financial-research scores through FastAPI at 9.1s p50 / 15.2s p99 and news search at 49ms p50 over pgvector.

I do not have Java, C, Ruby, or Perl; C++ and Python are the languages I can defend. I do not have a trading-desk internship — the JD does not require one. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), a U.S. citizen, and I can work the 10-week program in New York.

---

## "Why Two Sigma?" / "Why this internship?" (*inferred* Role Specific — ≈90 words)

Two Sigma treats technology as the business: distributed storage and cloud other teams consume, a mission-critical trading system, model test/deploy environments, low-latency execution, and ingest from 10,000+ sources a day. That is the engineering identity I want to sit next to for ten weeks — one project, a mentor, a final presentation — not a QR internship and not a CRUD shop. I already practice the two signals this screen rewards: lock-free C++ under a hard real-time constraint, and Python pipelines/APIs that have to be correct at a measured latency. I will not invent a desk or Java.

---

## "Why software engineering, not quantitative research?" (*inferred* — ≈80 words)

I am applying as an engineer. The work I can defend is systems and delivery: zero-alloc / lock-free C++ on a deadline thread, and production Python ingest + REST. I have CS + Economics and stats coursework; that is enough analytical signal for a general SWE intern (`persona.md`: prior finance is not required). I do not have a research-publication or Putnam/IMO record, and I will not re-target this page as LoRA / agent-pipeline QR. Match me to an infra, reliability, execution, or ingest team.

---

## "Tell us about relevant technical experience." (*inferred* — ≈120 words)

- **C++ / high-performance (differentiator):** Granular synthesizer — `MemoryPool<Grain, 64>` so `processBlock()` never heap-allocates; lock-free SPSC FIFO with acquire/release so the UI never blocks the audio thread. No latency/xrun number in the pool — the constraint is the story; measured latency lives on CaseStudyPrep (sub-5ms / 60 FPS) and SignalWeaver.
- **Python ingest + APIs (JD language + 10k-source analog):** Sole engineer, 5-month MCFN contract — Requests + Pandas ETL that removed ~800 hours of manual pulls across 400 PACs; Flask REST API on AWS EC2.
- **Measured Python systems:** SignalWeaver — pgvector news search 49ms p50 / 99ms p99; FastAPI scoring 9.1s p50 / 15.2s p99 across 90 tickers.
- **Reliability:** CaseStudyPrep — cut a 27% S3 upload-failure rate with mid-flight presigned-URL regeneration.
- **Not in inventory:** Java, C, Ruby, Perl, Snowflake, Databricks, Copilot, Fusion, Tableau, a trading-desk internship.

---

## "What programming languages are you strongest in?"

C++ and Python. C++ is where I have gone deepest on constraints (lock-free SPSC, custom slab allocation, no heap on the audio thread). Python is what I ship in production (Flask on EC2, FastAPI research endpoints, Pandas ETL). I can interview in either. I will not list Java.

---

## Availability / location

Summer **2027**, 10-week program, Soho NYC office. Available to relocate for the internship. Returning to Michigan after (Expected May 2028). Hired as general SWE; open to team match on infra, reliability, execution, ingest, or internal tools — not QR.

---

## Notes for the applicant (not for submission)

- **Avature email = verdent06@gmail.com.** PDF header is still umich. Fix autofill.
- **Exact Role Specific Questions were behind login.** Re-read the live wizard before paste; drop any *inferred* prompt that is not on the page.
- **Cover letter is not typical** on this intern req (community + JD). Use the letter only if a box appears.
- **Citizenship YES, sponsorship NO.** No clearance gate on this posting.
- **Never claim Java, C, Ruby, Perl, or a trading desk.** JD language list is OR; C++ and Python are the honest pair (`persona.md` anti-patterns).
- **No Two Sigma contact in `network.md`.** How did you hear: Company website / Internet search. Not employee referral. If you get an engineer referral, submit the referral **before** Avature — community reports say the ATS cannot attach a referral after the fact.
- **Funnel (`persona.md` / `companies.md`):** resume is the published bottleneck (<1%). Then Hard CodeSignal (official interview page does not name the platform — invitation controls) → technical loop (DS&A / OOP in C/C++/Java/Python; systems-design possible). Resume polish will not hire you (`recruiting.md`: quant / HFT is earliest-cycle, CP + math heavy; OA is a high-elimination gate).
- **Binding ding to own in interview:** Granular has no latency number; Lyndbrook is search-fund acquisition intelligence — do not dress it as a trading system (`grade.md`).
- **This agent did not apply.**
