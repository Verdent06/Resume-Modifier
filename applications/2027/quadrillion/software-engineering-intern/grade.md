# Software Engineering Intern at Quadrillion

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028; current undergrad (US) completing junior year by Summer 2027 and returning for senior year — within the JD's "sophomores/juniors preferred" band
- **Track:** full-stack + agentic-AI/ml-infra (track_divergence: true)
- **Pipeline:** 4 graded cycle(s) · exit: writer_peak

## Screen Review

### First read

- Vylet leads hard on the company identity: a shipped, founder-owned live product ($1,500 MRR, paying clients) built as a Dockerized **LangGraph** pipeline with Redis/Celery workers, plus a **LangSmith eval harness** that lifted extraction faithfulness 50%→90% — agent-orchestration + eval depth registers in the first pass, in Python.
- Full-stack spine is credible and defensible: MDC ships a production Flask REST API on EC2 as the sole engineer (+ a Requests/Pandas ETL eliminating ~800 hours across 400 PACs), and SignalWeaver adds a second 5-node LangGraph pipeline with real p50 latencies, a React/TypeScript dashboard, and Docker Compose + GitHub Actions CI.
- Binding dings are both structural, not quality: the "scale sandboxed compute to tens of thousands of concurrent deployments" mandate has no at-scale concurrency number on the page, and React surfaces only once, low, in Projects.

### Demerits

- **minor** · `Vylet` · weak compute-scaling signal — Redis/Celery workers and Docker show queues and containers, but nothing maps to sandboxed agent runtimes, parallel experiment isolation, or concurrent deployment at the scale Qualia's compute mandate describes.
- **minor** · `SignalWeaver` · thin frontend evidence — React/TypeScript proof is one dashboard bullet in a single bottom-of-page Projects entry while Experience is backend/pipeline-heavy — thin for a JD that names React as a preferred plus.

### Misreads

- A founder skimming fast could read "finance-automation builder" from the experience domains (PE prospecting, campaign finance, deal sourcing) and miss that the *engineering* — agent orchestration, eval, data pipelines — is exactly Qualia's stack; the LangGraph/eval framing in the top half is what corrects this.
- Docker/Celery at recurring-job scale can be under-read as "generic containers/queues" rather than a foundation for the concurrent-sandbox work the role actually ships.

### Interview angles

- **Lead with:** Vylet as a zero-to-one founder story — LangGraph agent pipeline, LangSmith eval harness (50%→90% faithfulness), Redis/Celery worker orchestration, live paying users; then SignalWeaver's 5-node LangGraph pipeline with per-node p50 timing; then MDC's sole-engineer production Flask API on EC2 (ownership + shipping-under-constraint).
- **Defend:** compute-scaling — *(out of rails: no pool bullet quantifies sandboxed/concurrent-deployment scale)* — narrate how you'd design isolated, massively-parallel agent sandboxes (container isolation, worker-pool sizing, queue fan-out, orchestration trade-offs) building on the Redis/Celery worker experience. React depth — *(out of rails: React lives only in the SignalWeaver project, and Experience always renders before Projects per resume doctrine)* — walk through the React/TypeScript dashboard's component/state/API-wiring decisions verbally.
- **Depth prep:** LangGraph/agent-orchestration design and eval-harness methodology (consensus gates, faithfulness); concurrency/queue architecture and how to scale to many concurrent isolated runs; embeddings + pgvector retrieval trade-offs; API latency (p50/p99) reasoning; timed DS&A / LeetCode mediums for the coding screen.

## Likelihood

- **Resume screen:** High — shipped founder product with paying customers, dual LangGraph pipelines with eval + latency metrics, Python throughout Experience, and integration/ETL signal all land in a human first read at a startup where the PDF is the front door.
- **Overall hire odds:** Medium — the screen bar is clearly met, but a single-digit-headcount seed startup has one scarce intern seat and no OA buffer; the technical loop still binds on DS&A depth, agent-system design fluency, and founder-fit against many strong shippers.
- **Funnel filters:** ~3–4 rounds · Med–Hard practical + DS&A · no standard OA (too small) · light agent-system design possible · onsite NYC · bottleneck: tiny headcount = extremely few seats · current-undergrad eligibility (sophomores/juniors preferred).
- **Outside the resume:** Warm intro or founder/engineer referral is the highest-leverage move at a seed startup (`recruiting.md` §4 — moves a cold apply to a motivated human read); apply within the first wave of the req (`recruiting.md` §2, §8); run timed DS&A + agent-system-tradeoff mocks before the technical screen (`recruiting.md` §6).
