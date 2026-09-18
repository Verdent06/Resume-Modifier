# Geneva Trading — AI Engineer Internship – Summer 2027 (Chicago) · Written Application Answers

Draft answers for Greenhouse **5240107007** / req **2026-73** (AI Engineering). Grounded in `persona.md` and `context.md` metrics only. First-person, honest, defensible under "walk me through this."

**This is not** Junior SWE (Trading Systems & OS) **5085231007**, **not** a C++ matching-engine intern, and **not** an ML-research seat. Applied AI / agents / product / internal tooling only.

## EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.** Override Greenhouse / university autofill. PDF header is `verdent06@gmail.com`. Phone **(248) 704-4852**.

**Do not invent:** Claude Code, Codex, Grok Build, TensorFlow-as-used, Kubernetes, Snowflake, Databricks, Copilot, Fusion, Tableau, buy-side or Geneva-platform internships, HFT microstructure depth, awards.

**Do not submit from this agent.** Paste pack only.

Apply: https://job-boards.greenhouse.io/genevatrading/jobs/5240107007
Resume: `applications/2027/geneva-trading/ai-engineer-intern-summer-2027/Vedant Desai Resume.pdf`

**SHA-256:** `3c572db58d83db9a418229de041311c71f3dce6653d57190fb3b4e4df289c8b4`

**Live page (2026-09-18):** Geneva Trading · **AI Engineer Internship - Summer 2027** · Chicago Office · 10 weeks · start **June 2027** · **$55–65/hr** · posted **2026-09-17** · expected close **2026-10-23**. Dept: AI Engineering. Cover letter **not required**, encouraged (firm campus page).

This is **applied AI / product / agent engineering** (`persona.md` screen_track `ai-ml`). **Not** ML research.

---

## Knockouts (read first)

1. STEM / CS degree — **clears**. B.S. Computer Science and Economics, University of Michigan, Expected May 2028.
2. **Graduation window — conflict, answer honestly.** JD prose: **December 2026 – June 2027**. You are **May 2028**. Greenhouse dropdown **includes May/June 2028** — select that. Do **not** pick May/June 2027. Binary knockouts auto-reject (`recruiting.md` Part I §1). Grade.md treats the prose window as ineligible; the dropdown is why the packet is still submittable without lying.
3. GPA — unstated. **3.66 / 4.0**.
4. Chicago onsite, 10 weeks, June 2027 — **Yes** (relocate from Northville, MI; return to Michigan afterward).
5. Sponsorship — **No**. US citizen.
6. Agent orchestration / Python / LLM tooling — **clears** through use (Vylet LangGraph/LangSmith/Gemini; SignalWeaver 5-node LangGraph). Do **not** claim Claude Code, Codex, or Grok Build. Gemini is the honest in-pool tool.
7. Housing downtown Chicago — **No** (do not invent a lease).

---

## Form-kit reminders (experience / awards)

**Prior experience (jobs / internships / co-ops):** CaseStudyPrep.AI + **Founder of Vylet only**.

- **Michigan Data Consulting (MDC)** = **extracurricular only**. Not on this PDF. Do not list it as a job.
- **SpaceXAI Campus Lead Ambassador** = **extracurricular only**. Not on this PDF.
- **Lyndbrook Capital** is on the PDF as a consulting engagement. Do **not** add it as a third job/internship on the form kit. If Autofill pulls it from the PDF, leave it only if the widget already created it — do not add it yourself.
- **Awards / honors:** **None.** Do not invent Dean's List, hackathon wins, or fellowships.

If a projects box appears separately, SignalWeaver (github.com/Verdent06/SignalWeaver) is allowed — it is a project, not a job.

---

## Greenhouse form (fill exactly)

Live schema from `boards-api.greenhouse.io` on **2026-09-18** (`?questions=true`). Do not invent extra essays.

| Field | Required | Answer |
| --- | --- | --- |
| First Name | Yes | Vedant |
| Last Name | Yes | Desai |
| Email | Yes | **verdent06@gmail.com** (override autofill) |
| Phone | Yes | 248-704-4852 |
| Resume/CV | Yes | `applications/2027/geneva-trading/ai-engineer-intern-summer-2027/Vedant Desai Resume.pdf` |
| Cover Letter | No | Optional. Firm campus page encourages it. Paste the letter below into **cover_letter_text**, or skip. |
| Location | Yes | Current: **Northville, Michigan, United States**. Internship is Chicago onsite — willing to relocate for June 2027. Do not list Chicago as current home. |
| LinkedIn Profile | No | https://linkedin.com/in/vedantde06 |
| What is your expected graduation date? | Yes | **May/June 2028** (dropdown value `35212429007`). Not May/June 2027. Not Other. |
| Do you have housing arrangements for a summer internship in downtown Chicago? | Yes | **No** |
| Are you interested in full-time opportunities with our firm after the internship, if a position is available? | Yes | **Yes** |
| Will you require sponsorship for employment authorization (e.g., H-1B visa) now or in the future? | Yes | **No** |
| School / degree (if parse asks) | — | University of Michigan · B.S. Computer Science and Economics (pick CS if one) · **Expected May 2028** · GPA **3.66** · Junior · currently enrolled **Yes** |
| Work authorization (if asked) | — | **Yes** — US citizen; authorized for any US employer; no sponsorship now or later |
| Website (if asked) | — | https://vyletdata.com (backup: https://github.com/Verdent06) |
| GitHub (if asked) | — | https://github.com/Verdent06 |
| How did you hear about this role? (if asked) | — | Job board / Greenhouse. **No Geneva contact in `network.md`.** Do not pick Employee Referral. |

Voluntary EEO / disability / veteran (if shown): **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

---

## Question 1 — custom tool / library from scratch, not LangChain (paste)

**Field:** `question_12912924007` (required textarea)

**Prompt:** Geneva Trading looks for 'engineers first.' Describe a custom tool or library you built from scratch—outside of standard frameworks like LangChain—to optimize your own engineering workflow. What was the performance gain, and why was existing tooling insufficient?

I built **Node 3** of Vylet (vyletdata.com) as a **pure-Python triangulated consensus gate with zero LLM calls**. It is a library in my own pipeline, not a LangChain chain and not an LLM-as-judge wrapper.

I needed a hard check that a lead actually matches the query, exists in the state business registry, and matches the live website — then fail closed on legal status, industry, geography, or independence **before** a score threshold. LangChain-style LLM scoring was the wrong tool: another model call on every lead, and it could not guarantee those constraints. Extraction faithfulness on messy public-web/registry text started at **50%**.

Node 3 fuzzy-matches the pipeline query, the registry record, and the crawl in a three-way weakest-link check and returns a 0–100 score only after the hard-fails. Around it I added a **LangSmith eval** over **20 adversarial cases / 13 archetype labels** plus deterministic **Pydantic consensus gates**, which lifted extraction faithfulness from **50% to 90%**. A name-collision bug in ownership verification was also a custom-logic fix (qualification **79% → 89%**), not a prompt tweak.

On-resume sibling (same product): a **custom asyncpg DAL** storing **Gemini embeddings** with injection-safe SQL freshness checks that re-scrape stale rows — I did not have a stock ORM that kept embeddings and source records honest.

That is engineer-first applied AI: a from-scratch gate and data layer because the standard agent framework was insufficient, then measure it. I have not used Claude Code, Codex, or Grok Build. Gemini is the LLM I can defend.

---

## Question 2 — prior internship (paste)

**Field:** `question_12912920007` (required textarea)

**Prompt:** Have you interned previously? If so, please provide details including the company name, duration, and key responsibilities.

**Yes — one co-op.** I have not interned at a prop-trading firm.

**CaseStudyPrep.AI — Software Engineer Co-op (Voice AI), Dec 2025 – May 2026, remote.** I shipped production voice-AI plumbing: client-side **Silero VAD via ONNX Runtime** so dead-air frames never hit Whisper (**40%** cloud inference cost cut), and moved audio off the UI thread into a **Web Worker** (**under 5ms** main-thread blocking, visualizer at **60 FPS**). I also built fault-tolerant RxJS upload logic that regenerated expired S3 presigned URLs and fixed a **27%** WAV upload failure rate.

**Not an internship:** I founded **Vylet** (May 2026 – present), a live PE/search-fund lead-sourcing product (**$1,500 MRR**, three clients) — Dockerized **LangGraph**, **LangSmith** eval, **Gemini** embeddings. That is founder/product work.

I will not list Michigan Data Consulting or SpaceXAI Campus Lead Ambassador as internships (extracurricular). Awards: none.

---

## Optional cover letter (paste into cover_letter_text only)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Geneva Trading — AI Engineer Internship – Summer 2027 (Greenhouse 5240107007)
Chicago, IL · 10 weeks · June 2027

I am applying for the AI Engineering intern seat — applied AI tools, agents, and prototypes for internal workflows — not the C++ trading-systems intern and not an ML-research rotation. I am a B.S. Computer Science and Economics student at the University of Michigan (**Expected May 2028**, GPA 3.66), currently a junior. I am a U.S. citizen and will not need visa sponsorship. I can be in Chicago for the 10-week term.

What I can defend:

- **Agents and eval.** Vylet: Dockerized LangGraph + LangSmith eval (50% → 90% faithfulness; 30x lead scoring) and a from-scratch Python consensus gate with no LLM calls. Custom asyncpg layer stores Gemini embeddings with SQL freshness. Live product, $1,500 MRR, three clients. vyletdata.com
- **Multi-step workflows.** SignalWeaver: 5-node LangGraph (fetch → classify → embed → score → explain) and pgvector search (49ms p50 / 99ms p99). github.com/Verdent06/SignalWeaver — research assistant, not investment advice.
- **Performance-sensitive product work.** CaseStudyPrep.AI co-op: on-device VAD (40% inference-cost cut) and a <5ms UI-thread budget at 60 FPS.

I have not used Claude Code, Codex, or Grok Build. I have not interned on a Geneva or prop desk. CS + Economics, search-fund scoring, and financial-research tooling are why I am curious about markets; the engineering is what I would spend ten weeks on.

Vedant Desai

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Greenhouse field and on the PDF.** Override autofill if parse yields `vedantde@umich.edu`.
- **Grad date = May/June 2028.** The JD prose window is Dec 2026–June 2027. Lying to May/June 2027 is a fabrication smell (`resume.md` defensibility). If they auto-reject on the prose window, that is the honest outcome (`grade.md` Likelihood: Low).
- **Housing = No.** Do not claim a downtown Chicago lease.
- **FT after intern = Yes.** You graduate May 2028; conversion would be after that term.
- **Prior jobs on the form = CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI = extracurricular. Awards = none.
- **Question 1 is the paste that matters.** They asked for a from-scratch tool *outside LangChain*. Lead with Node 3 (not on the PDF; in `context.md`). LangGraph/LangSmith stay on the resume as the agent spine — do not use them as the "I wrapped LangChain" answer.
- **Do not claim Claude Code / Codex / Grok Build.** Gemini only.
- **Do not claim RAG as a spoken bullet** unless you walk retrieve-then-generate (SignalWeaver pgvector). RAG is not on this PDF.
- **Referral:** none in `network.md`. A Chicago / UMich trading-tech intro still beats cold Greenhouse (`recruiting.md`).
- **Funnel:** Greenhouse → HackerRank if applicable → 15-min campus phone → mid/senior ± live tech → HM final (`company.md`). Timed Python mediums if OA is sent. Recruiter phone is motivation + markets curiosity without microstructure bluffing.
- **This is not the C++ Junior SWE req.** Do not attach a trading-systems PDF.
- **Apply before 2026-10-23.** Posted 2026-09-17 (`recruiting.md` §8 first wave).
