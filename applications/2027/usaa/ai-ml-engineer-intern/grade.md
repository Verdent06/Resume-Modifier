# AI/ML Engineer Intern at USAA

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside Sep 2027–May 2028; B.S. CS listed; internship ends Aug 13, 2027 and May 2028 is after that; US citizen needs no sponsorship
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on Vylet: Dockerized LangGraph (30x), LangSmith eval (50%→90% faithfulness), and an injection-safe SQL embeddings DAL — production genAI pipeline with paying clients, not a notebook.
- CaseStudyPrep ONNX VAD (40% inference-cost cut) plus MDC Pandas ETL and Flask REST on EC2 show production model serving and shipped APIs; SignalWeaver carries the only LoRA + held-out accuracy (81%→96%) plus FastAPI/pgvector latency.
- Binding ding: SignalWeaver's numbers sit on a 90-ticker/90-query self-run batch, so the ML-training proof is a research harness rather than an operated model.

### Demerits

- **minor** · `SignalWeaver` · self-run harness, not production model ops — LoRA 81%→96%, FastAPI 9.1s p50, and pgvector 49ms p50 still close on 90 self-run tickers/queries. Latency instrumentation is real, but there is no live-user or operated-model witness. JD wants deploy-to-production and model performance monitoring of something in an environment others use.

### Misreads

- SignalWeaver's 90-ticker / p50-p99 metrics can be bucketed as a class project rather than FastAPI + pgvector + held-out LLM fine-tune.
- CaseStudyPrep can be skimmed as "audio intern" and miss that it is on-device production inference (ONNX Runtime, cloud-cost cut).

### Interview angles

- **Lead with:** Vylet LangGraph + LangSmith eval + SQL/embeddings DAL (pipeline → eval → freshness); CaseStudyPrep Silero VAD via ONNX as production inference/cost; SignalWeaver LoRA 81%→96% held-out as the ML-framework proof; MDC Flask REST on EC2 as deploy-to-stakeholder.
- **Defend:** SignalWeaver has no external users — point to Vylet's three paying clients, MDC's nonprofit workflow, and CaseStudyPrep's live voice product as the production-ops proof *(out of rails: SignalWeaver pool is 90-ticker / 90-run / 90-query metrics; swap sets cannot add live users)*. Do not claim TensorFlow, scikit-learn, Keras, SageMaker, Kubeflow, Kubernetes, Snowflake, Databricks, Tableau, Power BI, Java, Palantir, or military service. Prompt engineering is analog (LangGraph/LangSmith eval), not a named prompt-design bullet.
- **Depth prep:** Walk the eval harness (20 adversarial cases, Pydantic consensus, 50%→90% faithfulness); LoRA held-out protocol vs claiming PyTorch-from-Skills; ONNX-in-production cost vs inventing SageMaker; SQL timestamp freshness; FastAPI vs Flask serving. Intern OA unpublished for this AI/ML req — do not assume HackerRank (`companies.md` No OA; Extern OA is a technology-intern web delta). Expect Easy STAR + project walk. Plano onsite June 2–August 13, 2027. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — eligibility is on the page, Python/SQL through use, production genAI + ONNX inference + LoRA-with-eval in the top half; one framing ding on SignalWeaver keeps this from a clean 10.
- **Overall hire odds:** Medium — C-tier ~15–20%; resume is the intern bottleneck; Easy 2–3 round loop after the PDF; Plano onsite still filters.
- **Funnel filters:** Workday USAAJOBSWD resume (`includeResumeParsing` true) → unpublished intern loop · Easy STAR + project walk · **No OA** on `companies.md` (do not assume HackerRank for R0121196) · no intern sys design · Bottleneck: resume · ~15–20% · no visa sponsorship · grad window Sep 2027–May 2028 · term June 2–August 13, 2027 Plano TX
- **Outside the resume:** Apply the same day (posted 2026-09-22; Workday `endDate` 2026-10-02; `recruiting.md` Part II §8 first wave). US citizen — sponsorship knockout is No. Mock eval-harness and ONNX-in-production stories. No USAA contact assumed — do not invent a referral.
