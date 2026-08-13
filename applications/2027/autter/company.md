# Autter

Autter is an early-stage developer-tooling startup building a runtime-aware AI merge gate for engineering teams. Unlike review bots that only read the diff, Autter clones every pull request (human-written or AI-generated) into an isolated sandbox, executes the test suite against the base branch, verifies imports and dependencies against real registries, catches secrets/CVEs, maps the change's blast radius across the codebase, and blocks the merge button until findings clear. It installs as a native GitHub App, folds production errors into incidents via a lightweight open-source runtime SDK, and ships an Apache-2.0 CLI that tracks AI-generated code at the line level (which agent, which model, which prompt, whether a human edited it). The Backend Engineer Intern (Agentic AI) works on the services that power that PR analysis — backend orchestration of LLM APIs, GitHub webhook processing, and the detection engines behind the gate.

## Quick Facts

- **Tier:** Unrated (not in `reference/companies.md`; early-stage AI dev-tooling startup — comparable in shape to CTGT-style seed AI-infra seats: resume-first funnel, ship-with-ambiguity bar, not a big-tech OA gauntlet)
- **HQ / offices:** Pune, Maharashtra, India; presence in the United States and Australia
- **Valuation / signal:** Founded 2025; 1–10 employees; open-source CLI (Apache 2.0) + native GitHub App platform; positioned against read-only AI review tools with a "we actually run the code" wedge
- **Product focus:** Runtime-aware AI code review / merge gate — sandbox PR execution, dependency verification, blast-radius mapping, AI-vs-human line attribution, runtime observability
- **Intern comp (2027 Backend Engineer, Agentic AI):** Not stated in JD
- **Work model:** Internship, full-time or near full-time on **IST hours**; remote (US-eligible per Jobright); company operates Pune-first
- **Clearance / eligibility:** Current-student internship; no sponsorship/citizenship gate in the posting. IST-hours availability is the binding logistical expectation, not a class-year knockout.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human (founder-direct at 1–10 employees) | Startup resume-first funnel; agentic-backend + dev-tooling signal read directly off the page |
| Technical screen | Practical backend / project walkthrough | Expect Node/Python backend reasoning, LLM-API orchestration trade-offs, GitHub API/webhook mechanics; "can you read a codebase you didn't write" |
| Practical / take-home | Likely a small backend or agent task | Early-stage bar favors shipping with limited scaffolding over LC marathons |
| Behavioral / fit | Founder conversation | Timezone/availability (IST), autonomy, and genuine LLM curiosity are explicit JD themes |

**Estimated funnel:** 2–3 rounds · Easy–Med practical (not LC-hard) · no named OA platform · no intern system design expected · Bottleneck: founder resume + practical backend/agent screen · offer rate unknown (tiny team, niche seat)

## Stack & Hiring Signal

- **Languages:** Node.js or Python for backend services (Python squarely covered by the candidate; JD accepts either); GitHub API/webhooks throughout
- **Domains:** Backend service engineering, agentic orchestration over LLM APIs (OpenAI/Anthropic), GitHub App/webhook integration, sandboxed code execution, developer tooling, detection-engine accuracy/latency
- **What wins:** Demonstrated agentic pipelines built on LLM APIs (not API-wrapper demos), production backend services with REST + queues, Docker/containerized deployment, eval/consensus discipline that maps to "improve accuracy and speed of detection engines," and evidence of reading/extending unfamiliar codebases. Open-source / developer-tooling exposure is a plus.

## Sources

- Jobright JD: https://jobright.ai/jobs/info/6a7dc9f2e2030208f2765e87
- ATS: https://autter.dev/careers/backend-engineer-intern
- https://autter.dev/ , https://story.autter.dev/ , https://autter.dev/autter-cli , https://autter.dev/docs (product/runtime/CLI detail)
- LinkedIn "Announcing Autter CLI — Open Source" (team size, HQ, Apache-2.0 CLI, AI-line attribution)
- `reference/recruiting.md` startup resume-first funnel + intern-stage doctrine; `reference/companies.md` CTGT row as early-stage AI-infra shape analog
