# Software Engineer Intern (Summer 2027) at Together AI

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is on or before JD degree-by-Summer-2028
- **Track:** full-stack + ml-infra / AI-native-cloud / inference-infra
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on CaseStudyPrep.AI: titled Software Engineer Co-op with client-side ONNX VAD that cut cloud inference cost 40%, plus a 27% S3 upload-failure recovery and a Web Worker path under 5ms / 60 FPS.
- Vylet is a live product ($1,500 MRR, three clients) with a Dockerized LangGraph pipeline, Redis/Celery workers, and a named quality defect (79%→89%); MDC is sole-engineer Flask REST on AWS EC2 plus ~800 hours / 400 PAC ETL.
- Binding ding: SignalWeaver is the right FastAPI + React + Docker Compose + GitHub Actions shape, but every metric is 90 self-run tickers.

### Demerits

- **minor** · `SignalWeaver` · research-harness framing, not production users — FastAPI + React + Docker Compose + GitHub Actions is the right serving/CI shape, but every metric is 90 self-run tickers and batch p50/p99 — no external user or customer of the service.

### Misreads

- SignalWeaver's 90-ticker / p50-p99 metrics can be bucketed as a class research project rather than the only end-to-end FastAPI + React + Postgres + CI build.
- CaseStudyPrep can be skimmed as "audio ML intern" and miss that it is the titled SWE co-op and the inference-cost analog.

### Interview angles

- **Lead with:** CaseStudyPrep ONNX VAD → 40% cloud-inference-cost cut and the 27% S3 recovery; Vylet Docker/Redis/Celery pipeline + 79%→89% qualification defect; MDC Flask REST on EC2 and Requests+Pandas ETL; SignalWeaver as the FastAPI + React + pgvector + GitHub Actions sample you can walk layer-by-layer.
- **Defend:** SignalWeaver has no external users — point to Vylet's three paying clients and MDC's nonprofit workflow *(out of rails: SignalWeaver pool is 90-ticker / 90-run metrics)*. CaseStudyPrep is on-device Angular/ONNX, not GPU-cloud serving — say that plainly. Do not claim CUDA, Go, Kubernetes, TensorFlow, HackerRank, or CodeSignal.
- **Depth prep:** 45–60m live coding, new-grad analog LC medium (`companies.md`; no named intern OA). ONNX Runtime vs cloud inference cost; FastAPI vs Flask; Redis/Celery workers; GitHub Actions CI (frontend build, pytest, image); what a name-collision false-reject looks like as a quality gate. Behavioral is a filter (`recruiting.md` Part I §6) — ownership stories from MDC sole-contract and Vylet production defect.

## Likelihood

- **Resume screen:** Medium — eligibility is on the page, titled SWE co-op, live-product pipeline, inference-cost work, and GitHub Actions CI; the serving exhibit is still a 90-ticker self-run harness.
- **Overall hire odds:** Low — A-tier <3%; resume then 45–60m live coding is the remaining filter (`companies.md`; no named intern OA). The PDF deserves a human read; it does not buy the loop.
- **Funnel filters:** Greenhouse resume (`recruiting.md` startup / human-read) → recruiter → 1–2 live coding (45–60m; LC medium) **[directional]** → team/HM · No named intern OA · Light intern sys design · Bottleneck: resume then tech · <3% · SF HQ four days/week · degree by Summer 2028
- **Outside the resume:** Apply in this first-wave window (JD live 2026-09-19); timed LC mediums; no Together contact in `network.md` — do not mark a referral.
