# GE Vernova — Engineering Intern, PCS AI Tool Developer (Summer 2027) · Written Application Answers

Draft answers for Workday req `R5049957`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented solar/storage internships, CAD, power-electronics, or metrics. Trim to the form's length limit before submitting.

Cover letter is **not required** (Extern intern guide). Use `cover-letter.md` only if Workday shows an optional upload or "additional information" box.

Apply: https://gevernova.wd5.myworkdayjobs.com/vernova_externalsite/job/Niskayuna/Engineering-Intern---Power-Conversion---Storage-AI-Tool-Developer--2027_R5049957-2

Simplify: https://simplify.jobs/p/f34b1f76-8c04-44e3-af69-ab94a7694d4b

Deadline listed: **2026-08-21** (rolling; posting said "at least seven days" from 2026-08-12). Apply now.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/ge-vernova/engineering-intern-pcs-ai-tool-developer/Vedant Desai Resume.pdf` |
| Location | **Niskayuna, NY** (onsite). Willing to relocate for Summer 2027. Relocation assistance is listed on the posting. |
| Currently pursuing Bachelor's in CS / EE / similar? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Enrolled full time? | **Yes** |
| Graduation date | **May 2028** |
| GPA | **3.66 / 4.0** (preferred floor is 3.0 without rounding) |
| Work authorization / sponsorship | **Yes, authorized to work in the U.S. without employer sponsorship.** US citizen. This posting: legally authorized to work in the United States; no H1B / intern sponsorship. |
| Willing to work in the geographical area specified? | **Yes** — Niskayuna, NY, Summer 2027 |
| How did you hear about this role? | **Simplify** (https://simplify.jobs/p/f34b1f76-8c04-44e3-af69-ab94a7694d4b). If Simplify is not listed: **LinkedIn Jobs** / Other → Simplify. |
| Pay $1,000–$2,000/week (~$25–$50/hr) | **Yes** — accept the posted intern range |
| Drug screen | Acknowledge if asked — posting conditions any offer on a drug screen as applicable |

---

## "Why GE Vernova / why this internship?"

I want to spend Summer 2027 building AI tools that application and design engineers actually use — data in, agents and interfaces out, then test and train people on them. That is this PCS NPI intern seat, not a generic SWE rotation and not CAD.

What I can defend:

- **Agents and workflows.** I run Vylet, a live lead-sourcing product ($1,500 MRR, three paying clients). I shipped a Dockerized LangGraph pipeline (30 scored leads in 30 minutes, a 30x speedup) and a LangSmith eval harness over 20 adversarial cases that lifted extraction faithfulness from 50% to 90% with Pydantic consensus gates. That is prompt / agent / workflow creation with a test loop — the standout qualification on this req.
- **Data for an AI tool.** At Michigan Data Consulting I replaced ~2-hour manual committee pulls with a Requests + Pandas ETL and shipped a Flask REST API on AWS EC2 to MCFN researchers (eliminating ~800 hours across 400 PACs). At Lyndbrook I aggregated EPA ECHO and MassGIS into a PWSID entity database and delivered 800+ Day-1 targets. That is collect / format / serve data, not notebook ML.
- **Interface tools.** SignalWeaver serves composite scores through async FastAPI REST and pgvector search (49ms p50). I have not interned on solar inverters or energy-storage hardware. I would ramp on PCS product documents with the NPI team rather than pretend I already have that domain.

I can be onsite in Niskayuna for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

---

## "Tell us about a project" / experience with AI prompt, agent, and workflow creation

**Vylet** (vyletdata.com). LangGraph pipeline with Redis/Celery workers; LangSmith eval across 13 archetype labels; deterministic consensus gates. A name-collision bug in ownership verification was rejecting valid targets; the fix lifted lead-qualification from 79% to 89% with no change in sourcing volume. I can walk the eval cases, where the gate hard-fails, and what I would copy into an engineering-document AI tool (templates, held-out cases, a number for faithfulness).

**SignalWeaver** (github.com/Verdent06/SignalWeaver). FastAPI + pgvector semantic search over financial news; 90-run batch, 49ms p50 / 99ms p99 on top-k retrieval. Research assistant, not investment advice.

---

## "Describe your experience working with engineers / customers / training others"

MDC: I was the only engineer on a 5-month MCFN contract. I scoped ingestion through REST endpoints with the nonprofit's researchers — no backend team behind me. Closest analog to sitting with PCS application/design engineers and writing training materials: I had to make the API usable by people who were not going to read the ETL.

I have not written formal AI-tool training decks. I can walk a teammate through the LangSmith eval and the Flask API the same way I would a short internal how-to.

---

## Availability

Summer 2027, onsite Niskayuna, NY. Available to start May 2027 (~10–12 weeks). Returning to the University of Michigan after the internship (Fall 2027 and Winter 2028 remain).

---

## Notes for the applicant (not for submission)

- **Do not claim solar, storage hardware, CAD, SolidWorks-for-this-role, power electronics, or PLC.** The JD is CS/EE AI tooling. SolidWorks is in the inventory but unused here; do not volunteer it.
- **Do not write this as an ML-research intern.** Lead with Vylet (agents/eval) and MDC (data + API). SignalWeaver FastAPI/pgvector is the interface analog; LoRA fine-tuning is backup if they ask about tuning with AI Research — it is real, but this req is tooling, not publications.
- **Location is not a skip.** Say yes to Niskayuna.
- **Referral:** no GE Vernova contact in `network.md`. A UMich alum in Niskayuna/Schenectady still beats cold Workday.
- **Cover letter:** skip unless the form asks; paste from `cover-letter.md` if it does.
