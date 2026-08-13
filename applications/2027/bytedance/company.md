# ByteDance

ByteDance is the technology company behind TikTok, Douyin, CapCut, and Toutiao, operating recommendation, ads, and content infrastructure at hyperscale. This role sits on the **Data-AML-Engine Orchestration** team (Applied Machine Learning — Engine), which builds the large-scale machine learning infrastructure that powers online model serving across ByteDance products, including TikTok. The team develops the orchestration, scheduling, and resource-management systems that connect heterogeneous compute (GPU/NPU) with production ML workloads — directly affecting GPU utilization, serving latency/availability, infrastructure reliability, and MLE productivity. Public artifacts of this org include the open-sourced Gödel unified scheduler (500+ clusters, ~20K servers, hundreds of millions of containerized tasks/day) and Katalyst; the stack centers on Kubernetes, Go, C++, and Python with model-serving frameworks like vLLM and Triton.

## Quick Facts

- **Tier:** A-Tier (via `reference/companies.md` TikTok/ByteDance-US row) — strong brand, excellent comp, respected eng culture; geopolitical/regulatory overhang on the brand
- **HQ / offices:** ByteDance global (Beijing / Singapore / LA); this role is **San Jose, CA** (US AML infra hub)
- **Valuation / signal:** ByteDance US; rec/infra/ads at massive scale; ML-infrastructure org (Gödel/Katalyst/Primus) that serves TikTok-scale online inference
- **Product focus:** ML platform orchestration — Kubernetes Operators, multi-tenant resource/quota scheduling, GPU FinOps, online model-serving lifecycle (deploy/rollback/autoscaling), and traffic management for disaggregated serving clusters (KV-cache affinity, request routing, QoS/SLA)
- **Intern comp (2027):** $45/hr (JD-stated hourly rate)
- **Work model:** Onsite, San Jose; Summer 2027 internship; state exact availability (start/end dates) in the resume; rolling review — apply early
- **Clearance / eligibility:** Currently pursuing a Bachelor's or Master's in CS/SE/AI or related technical field; max two applications across ByteDance and affiliates globally

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human + ATS | Bottleneck stage per `reference/companies.md` — resume clears the door before LC depth matters; infra org rewards systems evidence |
| OA | HackerRank / OA | Med–Hard difficulty per doctrine row; DS&A-driven |
| Technical rounds | 3–4 total rounds | DS&A + systems/infra depth (Linux, concurrency, distributed systems, "walk me through a system you built"); light intern system design |
| Behavioral / xFN fit | Folded into loop | Ownership + quantitative problem-solving (define measurements, test hypotheses, validate improvements) |

**Estimated funnel:** 3–4 rounds · Med–Hard difficulty · HackerRank/OA · light intern system design · Bottleneck: resume + LC · ~2–4% acceptance (per `reference/companies.md` TikTok/ByteDance-US row).

## Stack & Hiring Signal

- **Languages:** Go, C++, or Python (JD requires proficiency in at least one; DS&A/software-engineering fundamentals across all)
- **Domains:** ML platform/infrastructure — Kubernetes orchestration, container runtimes, multi-tenant resource scheduling/quota, GPU utilization/FinOps, online model-serving lifecycle, traffic management, autoscaling, highly available distributed systems; model-serving internals (vLLM/SGLang/Triton/KServe/Ray Serve, KV cache, continuous batching, prefill/decode disaggregation, model parallelism)
- **What wins:** demonstrated systems/infra depth backed by real bullets — containerized services with CI/CD, distributed workers/queues, concurrency and low-latency engineering, and quantified performance/latency/throughput work — in a JD-listed language (C++ and/or Python proven in bullets, not just a Skills line). Per `reference/recruiting.md` Part III §12 (DevOps/Platform: tie every tool to a problem; operational thinking is the differentiator) and Part I §1 (OA is the highest-elimination stage at big-tech scale), resume depth wins team-match after the OA clears. Kubernetes/scheduler/serving-framework exposure is a preferred nice-to-have, not a hard floor for interns; the hard floor is CS fundamentals + a JD language + a systematic, measurement-driven approach.

## Sources

- JD text provided by user (ByteDance, Data-AML-Engine Orchestration, Machine Learning Engineer Intern, 2027 Start, San Jose, $45/hr)
- Jobright: https://jobright.ai/jobs/info/6a79e3669ee17f276dbeff4f · External: https://joinbytedance.com/search/7671291260529821957
- `reference/companies.md` A-Tier TikTok/ByteDance-US row (San Jose, rec/infra/ads at massive scale, 3–4 rds, Med–Hard, HackerRank/OA, Bottleneck: resume + LC, ~2–4%)
- Web: ByteDance Gödel unified scheduler (KubeCon NA 2024), Katalyst, AML-Engine org overview (hyperscale K8s infra, vLLM/Triton serving)
