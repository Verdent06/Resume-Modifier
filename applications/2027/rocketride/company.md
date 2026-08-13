# RocketRide

RocketRide is a San Francisco-based, open-source AI infrastructure startup building the "AIDE" (AI Development Environment) — a developer-native platform that turns a normal IDE into a place to visually compose, debug, observe, and deploy agentic AI pipelines. Under the hood it is a data-pipeline builder and runtime for AI/ML workloads: 50+ pipeline nodes spanning 13 LLM providers, 8 vector databases, OCR, and NER, with pipelines defined as portable JSON and executed by a battle-tested, multithreaded **C++ engine**. It ships a VS Code extension, Python and TypeScript SDKs, and an MCP server, and auto-detects coding agents (Cursor, Claude, Copilot, Windsurf) so pipelines can be built and modified in natural language. Positioning is open-source-first (MIT), any-model / any-agent / no-lock-in, deployable locally, via Docker, or on the managed RocketRide Cloud.

## Quick Facts

- **Tier:** Unrated (early-stage open-source AI-infra startup; not in `reference/companies.md`)
- **HQ / offices:** San Francisco, CA (downtown); "Made with love in SF & EU" — small distributed team with an SF hub
- **Valuation / signal:** Early-stage; open-source traction (public GitHub org `rocketride-ai` / `rocketride-org`, VS Code Marketplace extension, Discord community, public launch event in SF)
- **Product focus:** Open-source AI pipeline infrastructure (AIDE) — visual agentic-workflow builder + high-performance C++ runtime; similarity search over 8 vector DBs; MCP + IDE-native tooling
- **Intern comp (2027 AI):** Not stated in JD
- **Work model:** Paid internship, part-time or full-time, 3–6 months with potential to convert; **hybrid, SF office ≥3 days/week**
- **Clearance / eligibility:** Current student in CS/related pursuing BS or MS; strong GenAI/ML interest; ability to work from the SF office ≥3 days/week

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human + founder/engineer read (small team via TrinetHire ATS) | Resume-and-project-first; open-source footprint and a live GitHub weigh heavily |
| Technical / project deep-dive | Walk-through of shipped agentic/LLM work + practical build reasoning | Expect to narrate agentic pipeline design, LLM integration, vector search, and (bonus) C++ performance trade-offs |
| Team / founder fit | Conversational | DevRel / open-source / developer-community mindset matters |

**Estimated funnel:** ~2–3 rounds · practical/project-depth over LC-marathon · no published OA platform · no formal sys-design for interns · Bottleneck: resume + project deep-dive at a small team · acceptance estimate: unrated (small-team startup, reads PDFs directly).

## Stack & Hiring Signal

- **Languages:** Python (primary for nodes/SDKs), TypeScript (SDK/extension), **C++** (the high-performance pipeline engine core)
- **Domains:** Agentic workflows / agent orchestration, LLM integrations (13 providers), multimodal data pipelines, similarity / vector search (8 vector DBs), graph databases (neo4j), MCP, IDE-native AI tooling, open-source developer tooling
- **What wins:** A genuinely shipped agentic AI system the candidate can narrate end-to-end (orchestration, LLM integration, eval), demonstrated vector/similarity-search work, and public/open-source contributions (GitHub, live product, technical content). C++ / performance-systems depth is an explicit "plus" and a rare differentiator that directly echoes RocketRide's C++ engine. Toy projects are explicitly discounted — "the real stack, not toy projects."

## Sources

- JD: https://jobright.ai/jobs/info/6a7db52819ce4e6e9d92f53d · https://app.trinethire.com/companies/1071922-rocketride-inc/jobs/122441-ai-developer-intern
- Web: rocketride.org, rocketride.ai, GitHub `rocketride-ai/rocketride-server`, VS Code Marketplace (RocketRide) — product, stack (C++ engine, 13 LLM providers, 8 vector DBs, MCP, SDKs), open-source positioning
- No `reference/companies.md` row exists (Unrated)
