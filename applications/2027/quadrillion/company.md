# Quadrillion

Quadrillion (Quadrillion Labs) is a New York seed-stage startup founded in 2025 building **Qualia**, an agentic research platform — a coding agent for researchers that writes, runs, and manages Jupyter-compatible notebooks through natural-language conversation. Qualia treats experiments as first-class objects: it spawns parallel agents to test multiple hypotheses at once, organizes work into dependency-aware task graphs, tracks claims/conclusions with provenance back to evidence, and runs unattended for hours (posting updates to Slack). It integrates with notebooks, codebases, data warehouses, MCP servers, and collaboration tools. Primary buyers are quant firms, research-focused enterprises, and advanced data-science teams; deployment is cloud or local. The bet is distribution — embedding directly into researchers' existing workflows to become default research infrastructure — not raw model performance.

## Quick Facts

- **Tier:** Unrated (no `reference/companies.md` row) — early-stage, high-bar seed startup
- **HQ / offices:** New York, NY (228 Park Ave S) — onsite for this role
- **Valuation / signal:** Seed, $7M raised (Jan 2026); ~9 employees; founder Ethan Chi (ex-Hudson River Trading, ex-Google Research, 2,000+ citations); product in demo phase with strong quant/research validation
- **Product focus:** Qualia — agentic research platform (agent orchestration, parallel experiments, knowledge/provenance graph, notebook-native execution)
- **Intern comp (2027 SWE):** Not stated in JD
- **Work model:** Onsite, New York, NY; Summer 2027 internship; interns do the same work as full-time engineers (ship product changes, fix customer bugs, build features)
- **Clearance / eligibility:** Current undergrad (US/Canada); sophomores/juniors preferred; no citizenship/clearance gate stated

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human / founder-direct (9-person seed startup) | No large ATS gauntlet at this size; a person reads the PDF early |
| Technical screen | Coding / practical | DS&A + real-world engineering; comfort in unfamiliar codebases is explicitly tested |
| Practical / take-home or pairing | Build/extend a feature | Zero-to-one, ship-fast signal weighed heavily |
| Onsite (NYC) | Multi-round technical + founder culture | Interns treated like FTEs; ownership and speed expected |

**Estimated funnel:** ~3–4 rounds · Med–Hard practical + DS&A · No standard OA (too small) · Light sys-design at most · Bottleneck: tiny headcount = very few seats, extremely high practical bar · acceptance estimate: very low (seed startup, single-digit team). Unrated — no `reference/companies.md` row; funnel inferred from company size and JD.

## Stack & Hiring Signal

- **Languages:** Python primary (backend + agent systems); React (preferred) for product surfaces; TypeScript adjacent; systems/concurrency depth for compute scaling
- **Domains:** Agent orchestration (long-horizon reasoning, parallel experiments, knowledge management), sandboxed-compute scaling to tens of thousands of concurrent deployments (containers, concurrency, distributed infra), tools/integrations connecting Qualia to customer data sources and external systems (connectors, data warehouses, MCP), notebook-native execution
- **What wins:** Shipped, owned production systems narrated decision-by-decision (JD: "same work as full-time engineers"); Python full-stack/backend depth demonstrated in bullets; agentic-AI / LLM-orchestration pipelines with eval and real metrics (the company's core identity); container/queue/concurrency and data-pipeline signal for the compute-scaling and integrations mandates; evidence of moving fast in unfamiliar, zero-to-one codebases. Per `resume.md` §12 (full-stack spine) plus §14 / `recruiting.md` Part III §13 (AI/ML) for the agentic differentiator.

## Sources

- Quadrillion Software Engineering Intern (Summer 2027) JD — Jobright: https://jobright.ai/jobs/info/6a62dda199515267a6f00561
- aVenture company/product research (Quadrillion, Qualia): https://aventure.vc/companies/quadrillion-new-york-ny-us
- docs.quadrillion.io (product overview — task graphs, parallel agents, provenance, MCP integrations)
- angelsround.com company brief (founder background, funding, buyers)
- `reference/recruiting.md` Part II §8 (intern eligibility/funnel), Part III §11 (general SWE), §13 (AI/ML); `reference/resume.md` §12 / §14
