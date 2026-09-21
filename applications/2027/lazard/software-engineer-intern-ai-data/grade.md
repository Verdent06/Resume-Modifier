# 2027 Software Engineer Summer Internship at Lazard

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 + Summer 2027 term = still enrolled Junior; JD requires June 7–August 13 2027 in NYC and a CS/Engineering bachelor — no exclusive class-year gate
- **Track:** full-stack + applied-AI/data-pipelines
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on Vylet: Dockerized LangGraph + Redis/Celery, LangSmith eval (50%→90% faithfulness), a named quality defect (79%→89%), and an asyncpg embeddings DAL — applied AI / data pipelines, not a LoRA paper.
- MDC is sole-engineer Flask REST on AWS EC2 plus Requests+Pandas ETL (~800 hours / 400 PACs) with stakeholder scoping — the data-product intern analog.
- Binding dings are framing: SignalWeaver is a 90-ticker self-run harness, and the titled SWE co-op is voice-AI rather than data-intensive applications.

### Demerits

- **minor** · `SignalWeaver` · research-harness framing, not production users — Docker/CI lead does not change the exhibit: FastAPI serving and pgvector search are 90 self-run tickers and batch p50/p99, not a data product used by bankers, PMs, or other operators.
- **minor** · `CaseStudyPrep.AI` · voice-AI pipeline, not a data-intensive application — The titled SWE co-op is Angular/RxJS audio upload reliability and on-device VAD cost-cut; it does not show ETL, serving, or embeddings the AI & Data intern builds.

### Misreads

- SignalWeaver's 90-ticker / p50-p99 metrics can be bucketed as a class project rather than the only FastAPI + Postgres/pgvector + CI build.
- CaseStudyPrep can be skimmed as "audio ML intern" and miss that it is production SWE (S3 failure recovery, on-device inference cost).

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval + 79%→89% quality defect + embeddings DAL; MDC Flask REST on EC2 and Requests+Pandas ETL for volume data + stakeholder delivery (banker/PM analog).
- **Defend:** SignalWeaver has no external users — point to Vylet's three paying clients and MDC's nonprofit workflow *(out of rails: SignalWeaver pool is 90-ticker / 90-run metrics)*. CaseStudyPrep is voice-AI, not a data product — say that plainly and use Vylet/MDC as the pipeline proof *(out of rails: CaseStudyPrep pool is voice-only; anti-deletion blocked omit)*. Do not claim MCP-as-used, Kubernetes, Airflow, Prefect, MongoDB, Java, Snowflake, or Databricks. Do not lead with LoRA.
- **Depth prep:** Timed Python/OOP coding even though intern OA platform is unpublished (`companies.md`). Eval harness vs quality gates; FastAPI vs Flask; asyncpg/pgvector vs inventing Mongo; Celery/Redis workers; Docker Compose + GitHub Actions; what a name-collision false-reject looks like as a data-quality analog. Behavioral: why AI & Data vs IBD; NYC June 7 start.

## Likelihood

- **Resume screen:** Medium — eligibility is on the page, Python stack through use, applied pipeline/eval/ETL in the top half; two framing dings keep this from High.
- **Overall hire odds:** Medium — B-tier ~5–8%; Easy–Med coding after the PDF; intern OA unpublished so the page carries unusual weight, but the loop is still a real filter (`recruiting.md` intern funnel; `companies.md` bottleneck: resume).
- **Funnel filters:** Oracle HCM resume → recruiter/video screen → coding assessment (intern OA unpublished; do not treat HackerRank as confirmed) · Easy–Med · light intern sys design · Bottleneck: resume · ~5–8% · NYC hybrid June 7–August 13 2027
- **Outside the resume:** Apply in this first-wave window (posted 09/18/2026). Confirm NYC for the full term. Timed Python/OOP. Do not invent MCP/K8s/Airflow. No Lazard contact in `network.md` — do not pick Employee Referral. Form-kit: CaseStudyPrep.AI + Vylet only (MDC/SpaceXAI extracurricular; Awards None). See `written-answers.md`.
