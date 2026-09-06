# Software Engineering Intern (Summer 2027) at Scale AI

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 = Spring 2028 vs JD Fall 2027 or Spring 2028; Summer 2027 intern returning to school
- **Track:** full-stack + AI data platform / applied pipelines / eval-and-quality infra
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on Vylet: a live product with a Dockerized LangGraph pipeline, a LangSmith eval harness (50%→90% faithfulness), and a named quality defect (79%→89%) — applied agentic / eval / quality, not a LoRA paper.
- CaseStudyPrep is a titled Software Engineer Co-op (the JD's prior-internship line) with production debug and on-device inference-cost work; MDC is sole-engineer Flask REST on EC2 plus ~800 hours / 400 PAC ETL with stakeholder scoping.
- Binding dings are framing: the React/TypeScript exhibit is a 90-ticker personal harness, and the titled frontend internship is Angular, not React.

### Demerits

- **minor** · `SignalWeaver` · research-harness framing, not production users — The only React/TypeScript + Postgres + CI exhibit is 90 self-run tickers and batch p50/p99, not features used by contributors or customers.
- **minor** · `CaseStudyPrep.AI` · Angular voice-pipeline, not a React product feature — The titled SWE internship is Angular/RxJS upload reliability and on-device VAD; React/TS through-use is only on the side project.

### Misreads

- SignalWeaver's 90-ticker / p50-p99 metrics can be bucketed as a class project rather than the only end-to-end React + API + DB + CI build.
- CaseStudyPrep can be skimmed as "audio ML intern" and miss that it is the employed SWE internship the JD requires.

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval + 79%→89% quality defect (eval/fraud analog); MDC Flask REST on EC2 and Requests+Pandas ETL for volume data + stakeholder delivery; SignalWeaver as the React/TypeScript + FastAPI + pgvector + CI sample you can walk layer-by-layer.
- **Defend:** SignalWeaver has no external users — point to Vylet's three paying clients and MDC's nonprofit workflow *(out of rails: SignalWeaver pool is 90-ticker / 90-run metrics)*. CaseStudyPrep is Angular/RxJS, not React — say that plainly and use SignalWeaver as the React/TS bridge *(out of rails: pool has no titled-role React product)*. Do not claim MongoDB, Snowflake, Databricks, Copilot, Tableau, Fusion, or Sentry. Do not lead with LoRA.
- **Depth prep:** HackerRank mediums (`companies.md` OA) then Med–Hard tech rounds (bottleneck). Eval harness vs quality gates; FastAPI vs Flask; asyncpg/pgvector vs inventing Mongo; Celery/Redis workers; what a name-collision false-reject looks like as a fraud/quality analog. Behavioral: Scale credos (ownership, quality, customer impact) mapped to MDC sole-contract and Vylet production defect.

## Likelihood

- **Resume screen:** Medium — eligibility is on the page, Python/TS/React through use, a titled SWE internship, and applied pipeline/eval in the top half; A-tier volume plus two framing dings keep this from High.
- **Overall hire odds:** Low — A-tier <3%; HackerRank then tech rounds are the binding filter after the PDF (`companies.md`). The page is on-axis enough to deserve the OA; it does not buy the loop.
- **Funnel filters:** Greenhouse resume → HackerRank · 3–4 rds Med–Hard · intern sys design Yes · Bottleneck: tech rounds · <3% · SF on-site May/June 2027 · Spring 2028 grad window
- **Outside the resume:** Apply in this first-wave window (first published 2026-09-04); timed HackerRank mediums; no Scale contact in `network.md` — do not mark referral.
