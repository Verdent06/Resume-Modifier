# ID.me — intern notes (SDE Intern, Summer 2027, Mountain View)

Intern-facing packet notes for Greenhouse **7980429003** / **1796**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What ID.me builds

ID.me is a digital identity wallet: verify once, reuse login and proofing across partners. JD: ~152M users, 20 federal / 45 state agencies, 70+ healthcare orgs, 600+ consumer brands. NIST 800-63-3 IAL2/AAL2 CSP. This intern is **generic SDE** on API-first product/platform teams in Mountain View — not a security-research seat, not McLean unless they move you later (`company.md`).

## This req

- **Title:** Summer Intern 2027 — Software Development Engineer Intern · Mountain View, CA · **$60–$70/hr** + housing stipend (eligible) · onsite 5 days / 40h · 12 weeks
- **Term:** May or June 2027 start
- **Work:** design/build/test; API-first services; reviews/agile; prod debug; security/testing/observability. Example intern projects: shop.id.me AI concierge widget; LLM Slack agent for Shop Ops
- **Posted:** first_published 2026-09-03 — first wave (`recruiting.md` Part II §8)
- **ATS:** https://job-boards.greenhouse.io/idmeuniversityrecruiting/jobs/7980429003 (prefer this over Simplify)

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Java, JavaScript, Go, Python, or Ruby (at least one) | Python, TypeScript, C++, SQL — **no Java, no Go, no Ruby**. "At least one" is the honest frame |
| REST + client-server | Flask REST (MDC), FastAPI REST (SignalWeaver) |
| Git | Git; GitHub Actions + pytest (SignalWeaver) |
| AWS, GCP, or Azure | AWS EC2 (MDC Flask), S3 (CaseStudyPrep) — **no GCP, no Azure** |
| Applied AI/LLM (RAG, prompt, tool-calling) — preferred | LangGraph + Redis/Celery (Vylet); pgvector embeddings (SignalWeaver). **Not** LoRA-as-lead; **not** ID.me RAG product |

## Funnel

B-TIER (`companies.md`): Greenhouse resume → recruiter → unpublished intern tech · no intern sys design · **bottleneck: resume** · ~8–12%. Mid-size Greenhouse is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Graduating 2028 or later — **clears** (May 2028). Greenhouse = **Yes**.
2. GPA band 3.5–3.99 — **clears** (3.66).
3. CS bachelor's enrolled — **clears**.
4. Mountain View 5-day onsite — **Yes, willing to relocate** (not the commuting-distance option).
5. Work auth / no future sponsorship — **Yes / No** (US citizen).

## What to lead with

MDC production Flask REST on AWS EC2 + ETL. Vylet LangGraph + named production defect. SignalWeaver FastAPI + React/TypeScript + pgvector + CI. CaseStudyPrep 27% S3 recovery as production-debug analog. Then say you will ramp Java/Go/Ruby rather than invent them (`persona.md`).

## Do not invent

Java, Go, Ruby, Azure, GCP, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, NIST 800-63 implementation, ID.me wallet, partner APIs, shop.id.me ownership, Slack-agent production.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Greenhouse). Phone 248-704-4852. US citizen. No ID.me contact in `network.md` — pick **LinkedIn**, not Referral.

## SHA-256

`f4570eb245a3a16027bb4563e76b8b933b49fcb63d94716bc9ccd4071e7c0a49`  `Vedant Desai Resume.pdf`

Worth-it: **YES** — see `WORTH_IT.md`. Score after pipeline: **9.0 / 10** (`grade.md`).
