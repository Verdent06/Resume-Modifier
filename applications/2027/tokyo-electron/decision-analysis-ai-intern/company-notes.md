# Tokyo Electron — intern notes (Summer 2027 Decision Analysis & AI Intern, Chaska)

Intern-facing packet notes for Workday **R26-01574**. Not a rewrite of `company.md` (that file is the Austin BI intern brief — leave it). Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What TEL builds

Public semiconductor **capital-equipment** company (TSE: 8035; FY2026 net sales ¥2,443.5B): etch, deposition, coater/developer, cleaning tools fabs use — not the chips. US HQ is Austin **RiverSouth**. This intern is **TMEA Chaska design-engineering decision support** (prompts, agents, bots/widgets, guided review tools, knowledge capture, process-data analysis, dashboards/metrics for tool effectiveness) — **not** the Austin BI Analyst intern (R26-01504), **not** an ATG research intern, **not** a process-engineer intern, **not** ML research, and **not** the Snowflake/Power BI Data Engineer sibling.

Chaska site address on aggregator copies of this req: **3455 Lyman Boulevard, Chaska, MN**. Subsidiary on this JD: **TEL Manufacturing and Engineering of America, Inc.**

## This req

- **Title:** Decision Analysis & AI Summer 2027 Intern · Chaska, MN · onsite · full time
- **Term:** Monday, May 17 – August 20, 2027
- **ATS:** Workday **R26-01574** · https://tel.wd3.myworkdayjobs.com/tel-careers/job/Chaska/Decision-Analysis---AI-Summer-2027-Intern_R26-01574
- **Posted:** 2026-09-16 (`postedOn`: Posted Yesterday as of 2026-09-17 pull) · no public Workday `endDate` — first wave (`recruiting.md` Part II §8)
- **Work:** design/build/deploy AI-assisted tools for design reviews, knowledge capture, best-practice standardization; measure results; train users; refine from feedback. Typical: prompts, agents, bots/widgets, guided review tools; engineering process-data analysis; structure lessons learned / design guidance; infrastructure decisions for data/access/portability/nimbleness; dashboards/metrics/feedback for tool effectiveness.
- **Comp:** **$30.35–$40.60/hr** on this JD (higher than the Austin BI analog). Treat as hourly intern band.
- **Lean:** training and resources provided. Do **not** invent a Lean cert.

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| AI-assisted prompts / agents / bots / widgets / guided review tools | LangGraph agents, LangSmith eval, Pydantic consensus gates (Vylet). Do not invent Copilot |
| Prompt engineering / evaluation / data-driven methods | LangSmith eval (50% → 90% faithfulness); LoRA held-out eval (81% → 96%) |
| Engineering knowledge / lessons learned / design guidance | Analog: structured extraction + embeddings + retrieval (Vylet Gemini embeddings + SQL freshness; SignalWeaver pgvector). **Not** TEL design-review corpus |
| Dashboards / metrics / feedback for tool effectiveness | SignalWeaver React dashboard + FastAPI served scores (9.1s p50). Do not invent Tableau / Power BI |
| Analyze engineering process data | Analog: Pandas ETL (MDC); Review Velocity scoring (Lyndbrook). **Not** wafer/process tools |
| Python (unnamed on this JD; honest analog) | Python through use (Vylet, MDC, SignalWeaver). JD names **no** required programming language |
| Snowflake / Databricks / Tableau / Copilot / Fusion / Power BI / Sentry | **Not in inventory.** Do not invent |
| Lean | Training provided. **No Lean cert** — do not claim one |

## Funnel

B-TIER (`companies.md`): Workday resume → unpublished OA (**not** confirmed for this DA&AI intern) → recruiter → Easy practical + STAR · **bottleneck: resume** · ~8–12% peer of Applied Materials DA. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech). Loop flavor for *this* seat: applied agents/prompts/eval/knowledge tools — **not** LeetCode OA as the published bar.

## Knockouts

1. Listed majors — **clears** (CS; JD: Engineering, Data Science, Computer Science, Systems Engineering, or related).
2. Class year — **clears** (Expected May 2028; Junior; ~96 credits by Summer 2027; returns Fall 2027).
3. GPA — unstated — **clears** (3.66).
4. Chaska MN onsite May 17–August 20 2027 — **Yes** (relocate from Northville, MI).
5. Lean cert — **not a knockout**. Answer **No**; will take TEL training.
6. Work auth — unstated on this JD; sibling process intern: no sponsorship. **US citizen; no sponsorship.**
7. Ever worked for TEL — **No**.

## What to lead with

Vylet LangGraph + LangSmith eval (agents + measured tool quality). SignalWeaver pgvector + React dashboard (knowledge retrieval + metrics UI). MDC Pandas ETL + Flask on EC2 (process-data → served output for non-builder users). Then say you will ramp TEL design-engineering workflows rather than invent wafer/process tools or Copilot (`persona.md`).

**This is not** the Austin BI Analyst intern. Do not lead with Sales/Service reporting as the spine.

## Do not invent

Snowflake, Databricks, Copilot, Tableau, Power BI, Excel-as-BI, Power Pivot, Fusion, Sentry, Lean Six Sigma certs, TEL wafer/process tools, TEL CRM / Field Solutions platforms.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168 ZIP **48168**. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. High school: Northville High School, graduated **05/19/2025**. UMich start **08/31/2025**. Junior, Expected May 2028, GPA 3.66, **96 credits by Summer 2027**. No TEL contact in `network.md` — pick **Job board / LinkedIn**, not Employee Referral.

**Employment on form:** CaseStudyPrep.AI + Vylet **only**. MDC = extracurricular. SpaceXAI Campus Lead Ambassador = extracurricular. Awards = **None**.

Workday questionnaires were **HTTP 406** without an account (`questionnaireId` `6906243b16e410017821c3dacdb50000` — same TEL intern questionnaire as the BI sibling). Full paste table: `written-answers.md`.

**Do not submit from this agent.** Packet only.

## PDF

`applications/2027/tokyo-electron/decision-analysis-ai-intern/Vedant Desai Resume.pdf`

**SHA-256:** `10ce870553d8b4681da9674ac893675ad4580ab1a03ef111268122931e87dcc6`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** See `WORTH_IT.md` and `grade.md` after pipeline.
