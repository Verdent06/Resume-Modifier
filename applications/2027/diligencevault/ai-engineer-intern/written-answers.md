# DiligenceVault — AI Engineer Intern (JazzHR Yo3RhxiDyM) · Written Application Answers

Draft answers for JazzHR **Yo3RhxiDyM**. Grounded in `persona.md` and `context.md` metrics only. First-person, honest, defensible under "walk me through this."

## EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.** Override any JazzHR / browser / university autofill. PDF header email is `verdent06@gmail.com`. Phone **(248) 704-4852**.

**Do not invent:** Snowflake, Databricks, Copilot, Fusion, Tableau, TensorFlow-as-used, Kubernetes, buy-side internships, DiligenceVault-platform experience, allocator/ODD desk work.

**Do not submit from this agent.** Paste pack only.

Apply: https://diligencevault.applytojob.com/apply/Yo3RhxiDyM/AI-Engineer-Intern
Resume: `applications/2027/diligencevault/ai-engineer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `0257f10a6328a02714e603a872038113abb6f691a39093aca1422cccfe89169e`

**Live page (2026-09-12):** DiligenceVault · **AI Engineer Intern** · New York, NY · Internship / Student (College) · **Hybrid, 8 hours/week in office** · **3 months** · JazzHR slug **Yo3RhxiDyM**. Posted/close dates not shown. Comp: "Competitive internship compensation" (unlisted). No visa line. Prior investment-industry experience is **not** required.

This is **applied AI / product / agent engineering** (`persona.md` screen_track `ai-ml`). **Not** an ML-research intern.

---

## Knockouts (read first)

1. Pursuing Bachelor's or Master's in CS, AI, Data Science, Engineering, or related — **clears**. B.S. Computer Science and Economics, University of Michigan, Expected May 2028.
2. Class year — **clears**. No exclusive gate. Summer 2027 = rising junior / after sophomore year (`context.md`).
3. GPA — unstated. **3.66 / 4.0**.
4. NYC hybrid, 8 hours/week in office, 3-month term — **Yes** (relocate from Northville, MI for the term; return to Michigan afterward).
5. Strong Python + LLM/embeddings/RAG/NLP familiarity — **clears** through use (Vylet LangGraph/LangSmith/Gemini embeddings; SignalWeaver pgvector semantic search). Do **not** claim RAG as a bullet word — it is Skills-only on the PDF (`grade.md` minor). Walk retrieve-then-generate instead.

Binary knockouts auto-reject (`recruiting.md` Part I §1). No visa/sponsorship line on this req; still answer honestly: US citizen, no sponsorship.

---

## JazzHR form (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | **verdent06@gmail.com** (override autofill) |
| Phone | 248-704-4852 |
| Address | 49032 Freestone Dr, Northville, MI 48168 |
| Resume | `applications/2027/diligencevault/ai-engineer-intern/Vedant Desai Resume.pdf` |
| LinkedIn Profile URL | https://linkedin.com/in/vedantde06 |
| Website, blog or portfolio | https://vyletdata.com (backup: https://github.com/Verdent06) |
| GitHub | https://github.com/Verdent06 |
| School | University of Michigan |
| Degree | B.S. Computer Science and Economics (pick CS if one) |
| Graduation date | **May 2028** (if a day is required: **05/01/2028**) |
| Class standing | Junior (Expected May 2028; Summer 2027 is after sophomore year / rising junior) |
| GPA | **3.66 / 4.0** |
| Currently enrolled | **Yes** |
| Location | **New York, NY** — hybrid, 8 hours/week in office. Willing to relocate for the 3-month term. |
| Work authorization | **Yes** — US citizen; authorized to work for any US employer |
| Sponsorship now or later | **No** |
| Age 18+ | **Yes** |
| How did you hear about this role? | Job board / LinkedIn Jobs. **No DiligenceVault contact in `network.md`.** Do not pick Employee Referral. |
| How soon you will be available to join? | **May 2027 / Summer 2027** (3-month intern term). Not immediately — enrolled at UMich through the academic year. If the dropdown is date-only, pick the earliest May 2027 option. |
| What is your expectation on stipend per hour basis? | **$30/hour** (single box). Range if they want one: **$28–$32/hr**. Grounded in C-tier intern band $22–38 (`companies.md`); JD pay is unlisted. Do not convert to a salaried FTE number. |
| Skills / tools checkboxes | Only what is on the PDF / inventory: **Python, SQL, LangGraph, LangSmith, Pandas, RAG, Redis, pgvector, AWS (EC2), Docker, Celery, FastAPI, Flask.** Do **not** check Snowflake, Databricks, Copilot, Fusion, Tableau, Kubernetes, TensorFlow. |

Voluntary EEO / disability / veteran (if shown): **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

---

## Form-kit reminders (experience / awards)

**Prior experience (jobs / internships / co-ops):** CaseStudyPrep.AI Software Engineer Co-op (Voice AI, Dec 2025–May 2026) and **Founder of Vylet only**.

- **Michigan Data Consulting (MDC)** = **extracurricular only**. Do not list it as a job/internship even though it is on the PDF as a delivery analog.
- **SpaceXAI Campus Lead Ambassador** = **extracurricular only**.
- **Awards / honors:** **None.** Do not invent Dean's List, hackathon wins, or fellowships.

If a "projects" box appears separately, SignalWeaver (github.com/Verdent06/SignalWeaver) is allowed — it is a project, not a job.

---

## Question 1 — Something you've built with AI (paste)

**Vylet** (vyletdata.com; github.com/Verdent06). I founded an automated lead-sourcing product for PE/search-fund work. It is live: **$1,500 MRR across three paying clients**.

I shipped a **Dockerized LangGraph** pipeline with Redis/Celery workers that turns a ~30-minute manual process per business into **30 scored leads in 30 minutes (30x)**. A **LangSmith eval** over 20 adversarial cases and 13 archetype labels, plus deterministic Pydantic consensus gates, lifted extraction faithfulness from **50% to 90%**. A custom asyncpg layer stores **Gemini embeddings** with injection-safe SQL freshness checks that re-scrape stale records.

That is applied AI-agent/product work — orchestration, eval, embeddings, messy public-web/registry text — not a notebook and not an ML-research paper. Closest analog to DiligenceVault's "idea → PoC → test against a real workflow → move what works toward production."

**Backup if they ask for a second artifact:** **SignalWeaver** (github.com/Verdent06/SignalWeaver) — pgvector cosine search over financial news (**49ms p50 / 99ms p99**, 768-d MPNet embeddings) and FastAPI serving (**9.1s p50 / 15.2s p99** across 90 tickers), containerized with Docker Compose. Research assistant, **not** investment advice, **not** a DiligenceVault clone.

I will not claim the word **RAG** as a bullet on the resume; the retrieve-then-generate analog is semantic search + embeddings. I have not used Snowflake, Databricks, Copilot, Fusion, or Tableau.

---

## Question 2 — Three points on why this internship interests you (paste)

1. **Applied AI on messy documents, not a research rotation.** I want a summer building and testing practical AI — semantic search, embeddings, agents, evaluation — against real diligence workflows, then pushing a PoC toward production. That matches how I already ship: LangGraph + LangSmith eval on Vylet (50% → 90% faithfulness) and pgvector retrieval on SignalWeaver (49ms p50).

2. **Unstructured / fragmented data is the job I already do.** DiligenceVault's problem is irregular docs and broken workflows. I have replaced ~2-hour manual campaign-finance pulls with a Requests + Pandas ETL (MDC, extracurricular) and aggregated EPA/MassGIS regulatory data into 800+ validated acquisition targets (Lyndbrook). I want that plumbing on allocator/manager diligence data.

3. **Enterprise product, short loop, NYC.** A 3-month hybrid seat (8 hours/week in office) on a Goldman-backed diligence SaaS is the right size to own a prototype and defend it with users. I am a UMich CS + Economics junior (Expected May 2028, GPA 3.66), a US citizen, and I can be in New York for the term. I have not interned on a buy-side desk; curiosity about markets is why I built Vylet and SignalWeaver — I will not pretend I already know DDQ/ODD process.

---

## Cover letter / additional information (only if JazzHR has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

DiligenceVault — AI Engineer Intern (Yo3RhxiDyM)
New York, NY (hybrid)

I am applying for the 3-month AI Engineer Intern seat. I want applied AI product work — unstructured documents, semantic search, agents, eval — not an ML-research rotation. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen and will not need visa sponsorship. I can be in New York for the hybrid term (8 hours/week in office).

What I can defend:

- **Agents and eval.** Vylet: Dockerized LangGraph + LangSmith eval (50% → 90% faithfulness; 30x lead scoring) and Gemini embeddings with SQL freshness. Live product, $1,500 MRR, three clients. vyletdata.com
- **Retrieval / messy text.** SignalWeaver: pgvector cosine search over financial news (49ms p50 / 99ms p99). github.com/Verdent06/SignalWeaver
- **Document plumbing.** MDC (extracurricular): Requests + Pandas ETL on irregular Excel filings + Flask REST on AWS EC2 (~800 hours / 400 PACs). Lyndbrook: EPA/MassGIS regulatory aggregation → 800+ Day-1 targets.

I have not interned in fund diligence or on DiligenceVault. I have not used Snowflake, Databricks, Copilot, Fusion, Tableau, or Kubernetes. I will ramp on DDQ/document workflows with the team rather than invent that domain.

Vedant Desai

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every JazzHR field and on the PDF.** Do not type `vedantde@umich.edu`. Override autofill.
- **Prior experience fields:** CaseStudyPrep.AI co-op + Vylet founder only. MDC and SpaceXAI Campus Lead = extracurricular. Awards = none.
- **Do not claim RAG as a spoken bullet word unless you say it is Skills-only.** Walk semantic search + embeddings (`grade.md` Defend).
- **Do not invent** Snowflake, Databricks, Copilot, Fusion, Tableau, buy-side internships, or DiligenceVault-platform work.
- **This is not an ML-research intern.** Lead with Vylet (agents/eval) and SignalWeaver (retrieval). LoRA on SignalWeaver is applied held-out adaptation — backup only if they ask about modeling; it is not on this PDF.
- **NYC hybrid is not a skip.** 8 hours/week in office, 3 months.
- **Referral:** none in `network.md`. A UMich / NYC diligence-tech intro still beats cold JazzHR (`recruiting.md`).
- **Stipend:** $30/hr is a C-tier ask, not a posted rate. Accept a reasonable offer in the $22–38 band.
- **Resume is the intern bottleneck** (`persona.md` / `companies.md` C-tier ~15–25%). PDF + the two essays first. No published OA.
- **Funnel:** JazzHR Yo3RhxiDyM → unpublished intern loop. Apply now; posted/close dates were not on the live page.
