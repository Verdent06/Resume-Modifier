# Xcel Energy — intern notes (Summer 2027 AI Solutions Development Intern, CO/MN)

Intern-facing packet notes for Workday **JR116329**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Xcel Energy builds

Fortune 500 regulated electric and natural gas utility (Nasdaq:XEL, Minneapolis HQ): ~3.9M electric / ~2.2M gas customers across eight states. Enterprise AI Enablement ships AI-powered productivity and process-automation solutions (Copilot exposure, agents, analytics) — not generation-engineering and not ML-research.

## This req

- **Title:** AI Solutions Development Intern CO, MN · Denver HQ T3 **or** Minneapolis 55401 · hybrid commute · **$20.90–$22.10/hr**
- **Start:** May 24, 2027 (summer up to 40h/week; possible school-year 20h)
- **ATS:** Workday **JR116329** · https://xcelenergy.wd1.myworkdayjobs.com/External/job/Denver-CO-80205/AI-Solutions-Development-Intern-CO--MN_JR116329-1
- **Posted:** 2026-09-07 · Workday `endDate` **2026-10-16** · JD deadline **10/15/26** — first wave (`recruiting.md` Part II §8)
- **Work:** AI solutions and agents, automation/workflow, analytics, documentation, stakeholder demos, AI-tool maintenance
- **Not this packet:** AI Enablement Intern CO, MN · AI & Automation Intern-CO **JR115739** · Power Generation Analytics Intern-CO **JR115734** (Henderson; separate folder)

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Python, SQL | Python + SQL through use (MDC, Vylet DAL) |
| JavaScript, Power Platform, *or similar* | TypeScript + React (SignalWeaver). **No** JavaScript-as-claimed, **no** Power Platform |
| Microsoft Copilot, ChatGPT, Claude, GitHub Copilot | Claude via llm-api swap on Vylet embeddings. **No** Copilot, GitHub Copilot, ChatGPT-as-product |
| Automation, APIs, low-code | LangGraph/Celery, Flask/FastAPI REST. **No** low-code |
| Applications / websites | React/TypeScript dashboard; Flask API to MCFN |
| Microsoft 365 | **Not** in the pool. Do not invent |
| Utility domain | Analog: water-utility EPA/MassGIS (Lyndbrook). **Not** Xcel/electric-grid platforms |

## Funnel

C-TIER (`companies.md`): Workday resume → recruiter/HM → 2–3 Easy STAR panel · intern OA unpublished · no intern sys design · **bottleneck: resume** · ~20–30%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Junior or higher — **clears** (Junior, Expected May 2028; 96 credits by Summer 2027).
2. CS / listed majors — **clears**.
3. Summer 40h hybrid Denver or Minneapolis from May 24, 2027 — **Yes** (relocate).
4. School-year 20h in-person from Ann Arbor — **do not promise**; summer yes.
5. Work auth — **clears** (US citizen). GPA unstated; 3.66 is a plus if they apply a 3.0–3.5 intern convention.

## What to lead with

Vylet LangGraph + LangSmith eval. MDC Pandas ETL + Flask on EC2. Lyndbrook water-utility EPA analog. SignalWeaver dashboard/API as apps+APIs. Then say you will ramp Copilot/Power Platform rather than invent them (`persona.md`).

## Do not invent

Microsoft Copilot, GitHub Copilot, Power Platform, Microsoft 365, JavaScript (vs TypeScript), Snowflake, Databricks, Tableau, Fusion, Sentry, Xcel/PSCo/NSP internships, ML-research/LoRA-as-identity.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. UMich start **08/31/2025**. HS Northville High School **05/19/2025**. No Xcel contact in `network.md` — pick **Simplify / Job board**, not Employee Referral.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/xcel-energy/ai-solutions-development-intern/Vedant Desai Resume.pdf`

**SHA-256:** `b262c3e88ce92553a46c3936144cb7c9f21a01cc3ece0345a175d5acbfc4499a`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **8.0 / 10** (2 minor: utility Copilot differentiator absent; preferred Microsoft stack absent). See `WORTH_IT.md` and `grade.md`.
