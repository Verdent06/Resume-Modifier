# Nationwide — intern notes (Summer 2027 Generative AI Internship, EAO)

Intern-facing packet notes for Workday **100231**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Nationwide builds

Fortune 100 mutual insurer and financial-services company (Columbus HQ): auto, home, life, farm, retirement, annuities. EAO Data Scientists sit in Finance and ship end-to-end analytics with business partners under a statistical-inference / model-validation bar. This intern is **applied GenAI on the insurance value chain**, not the catch-all Technology intern and not Feature Engineer **100233**.

## This req

- **Title:** Summer 2027 Generative AI Internship · Columbus Metro / One Nationwide Plaza · onsite · **$23–$50/hr**
- **Term:** May–August 2027
- **ATS:** Workday **100231** · https://nationwide.wd1.myworkdayjobs.com/Nationwide_Career/job/Ohio---Columbus-Metro/Summer-2027-Generative-AI-Internship_100231
- **Simplify:** https://simplify.jobs/p/99fd2453-9c39-447d-bb66-a0aebc0473e5
- **Posted:** 2026-09-04 · Workday `endDate` **2026-11-15** — first wave (`recruiting.md` Part II §8)
- **Work:** LLMs, AI agents, agentic workflows, RAG/vector DBs, Python/ML libraries, cloud/MLOps; Docker/K8s/CI plus

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python | Python through use (MDC, Vylet, SignalWeaver) |
| PyTorch, TensorFlow, Transformers, scikit-learn (*e.g.*) | PyTorch in inventory / Skills. **No** TensorFlow, sklearn, HF Transformers-as-a-library. Do not invent them |
| LLMs / agents / agentic systems | LangGraph, LangSmith eval, LoRA on Llama-3.1-8B |
| Vector DBs / RAG | pgvector cosine search; Gemini embeddings. Skills lists RAG as the JD term |
| Cloud / MLOps / Docker / K8s / CI | AWS EC2, Docker, Celery. GitHub Actions exists in the SignalWeaver pool (not on this PDF). **No Kubernetes** |
| Insurance domain | Analog only: campaign-finance ETL + Flask API; PE/search-fund scoring. **Not** P&C, claims, or Nationwide platforms |

## Funnel

C-TIER (`companies.md`): Workday resume → recruiter phone → 2–3 Easy STAR + project walkthrough · intern OA unpublished · no intern sys design · **bottleneck: resume** · ~15–25%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Work auth / no STEM OPT / no entry-level sponsorship — **clears** (US citizen).
2. Class year — **clears** (no exclusive gate; May 2028). Graduate-candidates line is additive.
3. GPA 3.2 sibling convention — **clears** (3.66).
4. Columbus onsite May–August 2027 — **Yes** (relocate).
5. TensorFlow / sklearn / K8s — **not knockouts**.

## What to lead with

Vylet LangGraph + LangSmith eval. SignalWeaver LoRA + pgvector. MDC Pandas ETL + Flask on EC2 as business-partner analog. Then say you will ramp insurance workflows rather than invent them (`persona.md`).

## Do not invent

TensorFlow, scikit-learn, Hugging Face Transformers, Kubernetes, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, P&C models, claims/underwriting internships, Nationwide platforms.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. No Nationwide contact in `network.md` — pick **Simplify / Job board**, not Employee Referral.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/nationwide/generative-ai-intern-summer-2027/Vedant Desai Resume.pdf`

**SHA-256:** `3b6fdee2ab21905311ebf8deb9aa8f1295d0182bf0571a45c6300c48f62892c6`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **8.0 / 10** (2 minor: insurance differentiator absent; PyTorch only in Skills). See `WORTH_IT.md` and `grade.md`.
