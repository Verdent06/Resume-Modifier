# Software Engineering Intern at Quadrillion

## Role Summary

SWE Intern at a ~9-person seed-stage NYC startup building Qualia, an agentic research platform for ML researchers, quants, and data scientists. The intern does the same work as full-time engineers: ships product changes, fixes customer bugs, and builds features end-to-end. Three named mandates: (1) build systems for **agent orchestration** — the core engine driving Qualia's long-horizon reasoning, parallel experiments, and knowledge management; (2) **scale sandboxed compute** for agent experiments/training to tens of thousands of concurrent deployments; (3) build **tools and integrations** connecting Qualia to customers' data sources and external systems. JD surface is a generic full-stack/backend SWE requirement centered on Python (with React as a preferred plus); the company's engineering identity is agentic-AI research infrastructure — LLM agents, orchestration, and experiment/compute scaling that customers depend on.

## Track Decision

- **screen_track:** full-stack (JD requirements literally test "strong full-stack or backend engineering, especially Python"; preferred "Python or React chops" — a generic SWE req, which `resume.md` §12 routes to full-stack even at a specialized company)
- **differentiator:** agentic-AI / ml-infra (agent orchestration, LLM-driven experiment automation, sandboxed-compute scaling, data-source integrations — Qualia's core identity)
- **track_divergence:** true

The screen spine follows `resume.md` Part III §12 — a genuinely engineered, shippable product narrated decision-by-decision, with backend/API, a database, cloud deploy, and CI/CD demonstrated through use, and Python front-and-center. The differentiator follows `resume.md` §14 and `recruiting.md` Part III §13 — agentic/LLM-orchestration pipelines with real eval and production metrics, plus container/queue/concurrency and data-pipeline signal that maps to the compute-scaling and integrations mandates. When divergence is true, lead with the full-stack/Python spine **and** keep the agentic-orchestration + infra carriers prominent and deep in the top half — do not flip the whole page to research-only framing, and do not bury the agentic signal at the bottom.

## Team & Bar

Unrated in `companies.md` (no row); this is a single-digit-headcount seed startup, so the resume is read early by a human (likely founder/engineer-direct), not filtered by a big-tech ATS/OA gauntlet. That inverts the usual intern calculus: the PDF carries more front-end weight, and there is no OA to hide behind. Recruiter voice here is a founding engineer who wants someone who has **already shipped and owned** real systems, can drop into an unfamiliar codebase and move fast, and reads as genuinely excited about agentic research infrastructure — not a coursework-only or notebook-ML candidate. Seats are extremely scarce (very low acceptance), so the bar for demonstrated ownership and zero-to-one velocity is high. Eligibility is a soft-preferenced gate: current undergrad (US/Canada), sophomores/juniors preferred; the page must show current enrollment.

## Screen Criteria

- Shipped, owned production system(s) narrated decision-by-decision — sole/lead ownership and real users/customers register strongly for a "do the same work as full-time engineers" intern role.
- Python demonstrated in bullets (backend/full-stack), not Skills-only — Python is the JD's named floor.
- Agentic-AI / LLM-orchestration depth beyond API wrappers: multi-node/agent pipelines, eval harnesses, consensus/verification logic, orchestration with real latency/cost/quality metrics — the company differentiator must register in the first screen pass.
- Concurrency / containers / queues / distributed-compute signal that maps to the "scale sandboxed compute to tens of thousands of concurrent deployments" mandate (Docker, workers/queues, async, real-time systems).
- Data-pipeline / integrations / connectors evidence (ETL, external data sources, warehouses, third-party APIs) — maps to the "tools and integrations" mandate; throughput or time-saved metrics preferred.
- Full-stack breadth with depth in at least one layer (frontend framework such as React, backend/API, database, cloud, CI/CD) demonstrated through use.
- Zero-to-one / fast-in-unfamiliar-codebase signal: founder/self-started products, short-window contract delivery, breadth across a stack.
- Class-year on page must show current enrollment (`Expected May 2028` satisfies a Summer 2027 internship as a returning senior).

## Anti-Patterns

- Screening as an ML-research/PhD candidate when the req is a ship-features SWE intern — lead engineering delivery, not paper-abstract framing.
- Agentic/LLM buzzwords with no pipeline architecture, eval, or production metrics behind them.
- Frontend-only or club-ops/community framing with no backend/API/data/systems depth the role tests.
- Notebook-only `model.fit()` ML with no delivery, serving, or orchestration.
- Pipeline/scale claims (throughput, concurrency, cost) asserted with no number attached.
- Thin single-bullet filler entries that dilute a strong production + agentic-infra spine.
- Languages/frameworks (Python, React) listed in Skills with zero bullet evidence at a company where Python is a floor signal.

## ATS Keywords

software engineering, intern, full-stack, backend, Python, React, agent orchestration, agentic AI, LLM, autonomous agents, parallel experiments, orchestration, distributed systems, sandboxed compute, concurrency, scalability, Docker, queues, FastAPI, REST API, data pipelines, integrations, connectors, data sources, zero-to-one, production, shipped, ownership
