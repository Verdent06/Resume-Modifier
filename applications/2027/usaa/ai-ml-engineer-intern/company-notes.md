# USAA — intern notes (Summer 2027 AI/ML Engineer Intern, Plano)

Intern-facing packet notes for Workday **R0121196**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What USAA builds

Fortune 500 insurance and banking group (legal hiring org on this posting: **2002 United Services Automobile Asn**) serving the U.S. military community and their families. Employment does not require military service. This intern is **production AI/ML engineering** at **Plano Legacy** — deploy models, genAI pipelines, and APIs — not a generic Technology Intern and not Data Scientist Intern.

## This req

- **Title:** AI/ML Engineer Intern · **Plano Legacy, Plano, TX** · onsite · **$26.50–$36/hr** + intern stipend
- **Term:** **June 2, 2027 – August 13, 2027**
- **ATS:** Workday **R0121196** · https://usaa.wd1.myworkdayjobs.com/en-US/USAAJOBSWD/job/Plano-Legacy/AI-ML-Engineer-Intern_R0121196
- **Apply:** https://usaa.wd1.myworkdayjobs.com/en-US/USAAJOBSWD/job/Plano-Legacy/AI-ML-Engineer-Intern_R0121196/apply
- **Posted:** 2026-09-22 · Workday `endDate` **2026-10-02** — first wave (`recruiting.md` Part II §8)
- **Work:** design/develop/deploy production AI/ML; genAI models; AI pipelines/APIs; model monitoring
- **Not this packet:** Technology Intern **R0120133** · Data Scientist Intern **R0121200**

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python | Python through use (Vylet, MDC, SignalWeaver, CaseStudyPrep) |
| SQL and database concepts | SQL timestamp freshness / asyncpg DAL (Vylet). pgvector (SignalWeaver) |
| ML frameworks | LoRA on Llama 3.1 8B (SignalWeaver). **No** TensorFlow / scikit-learn / Keras as claimed skills |
| LLMs / prompt engineering | LangGraph + LangSmith eval + Pydantic gates (Vylet). Prompt-design class **not** in the pool |
| Production AI / APIs | ONNX VAD in a live product; Flask REST on EC2; FastAPI scores; Dockerized LangGraph |
| MLOps / cloud-native (preferred) | Docker, Celery, AWS EC2/S3, Git. **No** SageMaker, Kubeflow, Kubernetes |
| Snowflake / Databricks / Java | **Not** in inventory. Do not invent |

## Funnel

C-TIER (`companies.md`): Workday resume → unpublished Easy STAR + project walk · **No OA** on the USAA row · no intern sys design · **bottleneck: resume** · ~15–20%. Extern OA reports are **[directional]** for generic Technology Intern siblings — do not treat HackerRank as published for R0121196.

## Knockouts

1. Grad window Sep 2027–May 2028 — **clears** (Expected May 2028).
2. Graduate after Aug 13, 2027 — **clears**.
3. CS / listed majors — **clears**.
4. No visa sponsorship — **clears** (US citizen).
5. Plano onsite June 2–August 13, 2027 — **Yes** (relocate).
6. Rising-senior wording is typical, not the printed gate. Answer **Junior** / rising junior honestly.

## What to lead with

Vylet LangGraph + LangSmith eval + SQL DAL. CaseStudyPrep ONNX production inference. SignalWeaver LoRA held-out as the ML-framework proof (defend the 90-run harness). MDC Flask on EC2 as deploy-to-stakeholder. Then say you will ramp USAA serving/monitoring rather than invent SageMaker (`persona.md` / `grade.md`).

## Do not invent

TensorFlow, scikit-learn, Keras, SageMaker, Kubeflow, Kubernetes, Snowflake, Databricks, Copilot, Fusion, Tableau, Power BI, Java, Palantir, military service, USAA policy platforms.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` — Workday **blocks `.edu`**). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510**. UMich start **08/31/2025**. HS Northville High School **05/19/2025**. **96 credits by Summer 2027.** No USAA contact in `network.md` — pick **company website / LinkedIn / job board**, not Employee Referral.

Live capture 2026-09-23: Start Your Application (Autofill / Apply Manually / Use My Last Application) + Create Account fields. Application Questions were **HTTP 406** without an account. Full paste table: `written-answers.md`.

## PDF

`applications/2027/usaa/ai-ml-engineer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `5f00f59b5033e701f9f3b3cc1e413059d00463ff0fd5933a1dd8e4ddeb6a3651`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **9.0 / 10** (1 minor: SignalWeaver self-run harness vs operated-model monitoring). See `WORTH_IT.md` and `grade.md`.
