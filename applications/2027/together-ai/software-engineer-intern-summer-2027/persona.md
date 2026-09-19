# Software Engineer Intern (Summer 2027) at Together AI

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

Paid Summer 2027 SWE intern, 12 weeks on-site at Together AI HQ in San Francisco (Greenhouse **5232036007**, requisition **313**). Interns are placed onto Platform Engineering, Infrastructure, Inference, or a sibling engineering team. Comp is **$58/hr plus a housing stipend**. Term windows: **May 17–August 6 2027** or **June 14–September 3 2027**. Form knockout: willing to work **four days/week in the SF office**.

JD surface is generic intern SWE: excellent programming, Git and collaborative workflows, creative problem-solving and trade-off communication, degree in CS / Software Engineering / related **earned or expected by Summer 2028**. Bonus, not filters: web development, databases, distributed systems, cloud platforms, OSS. Responsibilities span designing/maintaining software from **low-level systems to customer-facing UIs**, code review, debugging, and **performance optimization**. Company identity (`company.md` / `companies.md` A-tier) is the **AI Native Cloud** — high-performance inference, fine-tuning/RL, pre-training, open-model marketplace (JD: 400T+ tokens/month). This seat is a **generic SWE rotation**, not a research-paper intern and not a CUDA/kernel posting.

**Eligibility (computed):** Expected May 2028 vs JD "degree earned or expected by Summer 2028" → **eligible**. Summer 2027 is after junior year / rising senior (currently Junior). US citizen; no sponsorship needed. SF four-day on-site is a form knockout, not a resume-page fact.

## Track Decision

- **screen_track:** `full-stack`
- **differentiator:** ml-infra / AI-native-cloud / inference-infra
- **track_divergence:** true

Requirements literally test general SWE (`resume.md` Part III §12; `recruiting.md` Part III §11): programming skill, Git/collab, problem-solving, plus bonus web / databases / distributed systems / cloud. That routes to `full-stack` (default for a generic SWE req). Do **not** route `ai-ml` — the JD names no ML frameworks, no training loop, no PyTorch/CUDA filter. Do **not** route `dev-ops` — cloud/distributed appear as *bonus*, not the exclusive test.

Together's dominant engineering identity is **GPU-cloud inference and serving infrastructure for open-weight models**. That identity is distinct from generic product-SWE, so divergence is true: the resume leads with the `full-stack` spine **and** keeps inference-cost/serving, open-model adaptation, and performance-critical systems prominent in the lead window. Do not lead as notebook ML, a LoRA-paper intern, or a closed-lab researcher. Do not invent CUDA, Go, Kubernetes, or TensorFlow.

## Team & Bar

A-tier, <3% **[directional, Scale AI / Replit peer]** (`companies.md`). Funnel: Greenhouse resume (`recruiting.md` startup / human-read) → recruiter → 1–2 live coding (45–60m; new-grad analog LC medium) **[directional]** → team/HM. **No named intern OA.** Do not invent HackerRank or CodeSignal. Bottleneck: **resume then tech**. Recruiter voice: a human reading a startup PDF in ~7 seconds (`resume.md` Part I), looking for an eligible undergrad who already ships software, can talk Git/collab and trade-offs, shows web/data/cloud/distributed bonus evidence, and looks like they belong next to inference/platform engineers — not someone listing GPU kernels they have never written.

Graduation by Summer 2028 is the hard program gate; Expected May 2028 is in window. No GPA floor on the JD; 3.66 is a plus if they look. Resume carries more front-end weight here than at OA-gated big tech (`recruiting.md` Part I §1 startups). After the PDF, live coding is the remaining filter. Apply in the first wave (`recruiting.md` Part II §8).

Winning *kinds* of evidence: programming languages demonstrated in bullets, not Skills alone; a shippable product or production API with a persistence decision and a deploy path; cloud/distributed/queue analogs; inference or serving work with a witness metric (cost, latency, throughput); performance-critical systems the candidate can defend; Git/CI as collaborative-workflow proof. Intern-stage weighting still favors engineered projects plus live GitHub (`resume.md` Part II intern).

## Screen Criteria

**Pass signals (abstract):**

- Programming skill shown through use — languages the candidate actually has, in bullets, not Skills-only (`resume.md` §2). This JD names **no** required languages; do not invent Go, CUDA, or a Winter-sibling stack as a floor.
- Git and collaborative development: version control plus a real workflow (review, CI, shared deploy) rather than a Skills-line token.
- Shipped full-stack or backend software: REST/APIs, a real client surface, a persistence decision, and cloud/deploy tied to an outcome (`resume.md` §12). Breadth across the stack + depth in at least one layer.
- Bonus JD flavors on that spine: web development, databases, distributed systems (workers/queues/lock-free handoff), cloud platforms — each tied to a problem, not a glossary.
- Inference-infra / open-model serving flavor in the top half when present: on-device or cloud inference cost/latency, serving an adapted open-weight model, eval/quality gates — memorable at an AI-native-cloud company without replacing the SWE spine (`recruiting.md` Part III §13 applied vs research).
- Performance optimization with a witness metric (the JD's performance-critical / debugging bar).
- Class-year on the page: `Expected May 2028` satisfies degree-by-Summer-2028.

**Anti-patterns:**

- Inventing CUDA, Go, Kubernetes, TensorFlow, HackerRank, CodeSignal, or a research-intern title.
- Leading as a LoRA-paper / `model.fit()` researcher because the company sells fine-tuning.
- Skills-list-only Git, cloud, or web with no bullet evidence for the bonus terms claimed.
- Club-ops, GTM/quant sourcing, or deal-flow work with no engineering the role tests.
- Notebook ML with no serving, API, eval, or deploy story.
- Thin single-bullet filler that dilutes a production + inference-infra spine.
- Claims the candidate cannot defend in a 45–60m live coding follow-up or a project deep-dive.

## ATS Keywords

Git, version control, web development, databases, distributed systems, cloud, AWS, Docker, REST API, Python, TypeScript, inference, performance optimization, scalable systems, Platform Engineering, Infrastructure, full-stack, debugging, PostgreSQL, CI/CD
