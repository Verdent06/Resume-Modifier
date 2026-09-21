# 2027 AI Engineer Summer Internship at Lazard

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 + Summer 2027 term = still enrolled Junior; JD requires June 7–August 13 2027 in NYC and a CS / ML / AI bachelor — no exclusive class-year gate
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on Vylet: Dockerized LangGraph + Redis/Celery, LangSmith eval (50%→90% faithfulness), and an asyncpg embeddings DAL — applied agentic LLM, not a LoRA paper as the lead.
- MDC is sole-engineer Flask REST on AWS EC2 plus Requests+Pandas ETL (~800 hours / 400 PACs) with stakeholder scoping — deploy + data-product analog.
- Binding dings are framing: SignalWeaver is a 90-ticker self-run harness, and the titled SWE co-op is voice-AI rather than AI-driven applications for bankers and PMs.

### Demerits

- **minor** · `CaseStudyPrep.AI` · voice-AI pipeline, not an AI-driven data product — The titled SWE co-op is on-device VAD cost-cut and S3 audio-upload recovery; it does not show LLM frameworks, NLP/RAG, or AI applications for bankers or PMs.
- **minor** · `SignalWeaver` · research-harness framing, not production users — FastAPI serving and pgvector search still close on 90 self-run tickers and batch p50/p99; leading with serving does not make this an AI product used by bankers, PMs, or other operators.

### Misreads

- CaseStudyPrep can be skimmed as "audio ML intern" and miss that it is production SWE (S3 failure recovery, on-device inference cost).
- SignalWeaver's 90-ticker / p50-p99 metrics can be bucketed as a class project rather than FastAPI + pgvector + held-out NLP.

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval + embeddings DAL (agents → eval → retrieval); SignalWeaver sentiment classification (81%→96% held-out) and pgvector search as the NLP/RAG analog; MDC Flask REST on EC2 as deploy-to-stakeholder.
- **Defend:** SignalWeaver has no external users — point to Vylet's three paying clients and MDC's nonprofit workflow *(out of rails: SignalWeaver pool is 90-ticker / 90-run metrics)*. CaseStudyPrep is voice-AI, not an FA/AM AI product — say that plainly and use Vylet/MDC as the product proof *(out of rails: CaseStudyPrep pool is voice-only; anti-deletion blocked omit)*. Do not claim MCP-as-used, Kubernetes, LangChain, LlamaIndex, MongoDB, Snowflake, or Databricks. LoRA is supporting NLP evidence, not the job.
- **Depth prep:** Timed Python/OOP even though intern OA platform is unpublished (`companies.md`). Eval harness vs quality gates; RAG-style pgvector vs inventing a named VectorDB; FastAPI vs Flask; what a name-collision false-reject looks like as a data-quality analog; sentiment classification vs claiming NER. Behavioral: why AI Engineer vs the 6603 SWE sibling vs IBD; NYC June 7 start.

## Likelihood

- **Resume screen:** Medium — eligibility is on the page, Python stack through use, applied agent/eval/NLP in the top half; two framing dings keep this from High.
- **Overall hire odds:** Medium — B-tier ~5–8%; Easy–Med coding after the PDF; intern OA unpublished so the page carries unusual weight, but the loop is still a real filter (`recruiting.md` intern funnel; `companies.md` bottleneck: resume).
- **Funnel filters:** Oracle HCM resume → recruiter/video screen → coding assessment (intern OA unpublished; do not treat HackerRank as confirmed) · Easy–Med · light intern sys design · Bottleneck: resume · ~5–8% · NYC June 7–August 13 2027
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-21). Confirm NYC for the full term. Timed Python/OOP. Do not invent MCP/K8s/LangChain. No Lazard contact in `network.md` — do not pick Employee Referral. Form-kit: CaseStudyPrep.AI + Vylet only (MDC/SpaceXAI extracurricular; Awards None). Sibling of already-Applied **6603** SWE — this is **6606**. See `written-answers.md`.
