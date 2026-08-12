# Machine Learning Engineer Intern (AML-Engine-Orchestration) at ByteDance

## Role Summary

A Summer 2027 onsite internship ($45/hr, San Jose) on ByteDance's **Data-AML-Engine Orchestration** team — the group that builds the large-scale ML infrastructure powering online model serving across ByteDance products, including TikTok. Despite the "Machine Learning Engineer" title, the JD's requirements do not test model building. They test **platform/infrastructure engineering**: Kubernetes Operators and container runtimes, multi-tenant resource/quota systems (priorities, preemption, fair sharing, elasticity, cross-cluster scheduling), GPU utilization and FinOps, online model-serving lifecycle (distribution, deploy, rollback, autoscaling, multi-cluster, DR), and serving/traffic orchestration for disaggregated clusters (topology-aware scheduling, KV-cache affinity, request routing, QoS/SLA). The ML is the domain the infrastructure serves, not the work the intern does.

## Track Decision

- **screen_track:** dev-ops (platform / infrastructure) — the JD's required qualifications literally test CI/CD-style delivery, containers, cloud/cluster infra, resource scheduling, distributed systems, Linux, and concurrent programming (`reference/resume.md` §13; `reference/recruiting.md` §12).
- **differentiator:** ml-infra — ByteDance's dominant engineering identity here is model-serving orchestration and GPU resource platforms at hyperscale (Gödel/Katalyst; vLLM/Triton serving).
- **track_divergence:** false — screen_track (dev-ops/platform) and differentiator (ml-infra) sit on the same infrastructure axis and reinforce each other; the single platform/infra spine grounds the resume, with model-serving/inference-infra flavor.

The literal minimum bar is a systems/platform SWE screen: proficiency in at least one of Go/C++/Python with strong DS&A and software-engineering fundamentals; Linux plus a foundational understanding of operating systems, computer networks, concurrent programming, and distributed systems; a systematic, measurement-driven approach (define metrics, test hypotheses, validate improvements); and demonstrated ownership. Kubernetes/scheduler/serving-framework experience and open-source infra contributions are **preferred nice-to-haves**, not hard floors for an intern. The resume must therefore read as a strong systems engineer who ships and measures real infrastructure — not as a notebook-ML candidate and not as a pure-frontend/CRUD candidate.

## Team & Bar

The reviewer is a ByteDance/TikTok-US campus recruiter (and, at team-match, an AML-infra engineer) screening a high-volume, OA-gated intern pipeline (per `reference/companies.md`: 3–4 rounds, Med–Hard, HackerRank/OA, bottleneck is resume + LC, ~2–4% acceptance). Per `reference/recruiting.md` Part I §1, the OA is the highest-elimination stage and the resume's depth mostly wins **team-match after** the OA clears — so the resume must survive the ~7-second screen cleanly and then read as a strong systems/infra match for this specific team. This bar rewards evidence of: a JD-listed language (C++ and/or Python) demonstrated through real engineering decisions in bullets, not a bare Skills-line claim; operational/systems thinking (what breaks, how you detect and recover, how you make it faster or cheaper) tied to a concrete problem; containerization / CI/CD / distributed-worker / queue / concurrency work with quantified latency, throughput, or cost outcomes; and a quantitative, hypothesis-driven engineering style (measure → change → validate) that mirrors the JD's stated way of working.

## Screen Criteria

- At least one JD-listed language (Go, C++, or Python) demonstrated through real engineering decisions in bullets — C++ systems depth (concurrency, memory, low-latency) and/or Python service/infra work — not only in the Skills line.
- Systems/infra substance visible near the top of the page: containerized services, CI/CD, distributed workers/queues, async or lock-free concurrency, and measured performance (latency p50/p99, throughput, cost/utilization) — the closer this reads to "built and operated a real system," the stronger the fit.
- Quantitative, measurement-driven framing: bullets that define a metric, make a change, and validate the improvement (aligned to the JD's "define measurements, test hypotheses, validate system improvements").
- Anti-patterns: notebook-only ML with no delivery/serving path; an LLM feature described as a thin API call with no orchestration, concurrency, or infra behind it; front-end/CRUD-only framing with no systems signal; "familiar with Docker/Kubernetes" claims with no demonstrated, problem-tied use; club-ops or membership padding without engineering depth.
- Ownership + collaboration signal: shipped something real end-to-end (sole or lead ownership, or delivery to a real stakeholder/user), consistent with the JD's ownership expectation.

## ATS Keywords

Kubernetes, container runtime, Docker, orchestration, resource scheduling, quota, multi-tenant, autoscaling, GPU utilization, FinOps, model serving, inference, distributed systems, concurrency, low-latency, Linux, CI/CD, traffic management, request routing, QoS/SLA, C++, Python, Go, performance optimization, throughput, latency (p50/p99)
