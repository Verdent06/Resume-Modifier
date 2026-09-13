# Software Engineer Co-op (Spring 2027) at Klaviyo

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

Paid **Software Engineer Co-op (Spring 2027)** at Boston HQ (125 Summer St), **Jan 4–Jun 25 2027**, in office **5 days/week**, 40 hours, **$49.50–$60.50/hr**. Posted on the **Klaviyo Campus** Greenhouse board (`klaviyocampus` **7989365003** / **R-103005**) — not the Summer 2027 intern twin. Team-agnostic offer; placed ~30 days before start onto full-stack, back-end, or front-end inside any pillar (Data Infrastructure, MCMI, Core Infrastructure, Growth Marketing Platform, AI & Analytics, Autonomous Service). Base Camp onboarding. Interns own features for 180K+ paying customers: write / test / ship / improve; debug locally and in production; documentation and incident support; ship end-to-end. AI-first *workflow* (use AI tools at work) — do **not** invent Copilot or other AI products on the page.

JD surface is generic intern SWE: ≥1 prior SWE internship or co-op; CS/Engineering/Data Science/Math; graduating Dec 2027 or May/June 2028; experience with *some of* Python, Django, TypeScript, React, Go; MySQL, Cassandra, ClickHouse, Kafka, Redis; AWS (EC2, RDS, Aurora), Terraform. Across-the-stack; performance/scalability (slow UI, too many clicks, query timeout, queue that will not drain); ship early/often; in-person learning culture; experimented with AI in work or personal projects. Company identity (`company.md` / `companies.md`) is **e-commerce marketing automation / CDP / high-scale messaging+data platform** — not a generic consumer-app internship, not an ML-research seat, and not a DevOps/Terraform rotation.

## Track Decision

- **screen_track:** `full-stack`
- **differentiator:** e-commerce marketing automation / CDP / high-scale messaging+data platform
- **track_divergence:** true

Requirements literally test general SWE (`resume.md` Part III §12; `recruiting.md` Part III §11): languages, shipped features, debug, test, APIs, FE-to-BE. That routes to `full-stack` (default for a generic SWE co-op even at a specialized company). Do **not** route `ai-ml` because "AI-first" is how they work, not an ML-training/inference bar, and do **not** route `dev-ops` because Terraform/AWS are "some of" stack flavor, not an SRE test.

The company's dominant engineering identity is a **high-scale marketing-automation / CDP / messaging+data platform** (KDP, email/SMS/WhatsApp, 180K+ customers). That identity is distinct from generic product-SWE, so divergence is true: the resume leads with the `full-stack` spine **and** keeps data-pipeline / production-API / Redis-or-queue / AWS shipping prominent in the lead window. Do not lead as notebook ML, LoRA, or agent-eval because the JD mentioned AI. Do not lead as hard-real-time C++/audio-DSP because this co-op lands on product/infra web+data software.

## Team & Bar

Klaviyo is B-TIER (`companies.md`): Greenhouse ATS; human reads the PDF; eligibility knockouts (graduation window, no sponsorship, Boston 5 days/week, full term, ≥1 prior SWE intern/co-op) can fire before a fair read (`recruiting.md` Part I §1). Funnel: resume → recruiter → **CodeSignal OA** (practical/debug/extend; official CodeSignal customer) → HM project+behavioral → ~3h superday (weather-app / API+FE analog reported for FS intern) **[directional]**. Bottleneck: **OA**. Acceptance ~5–8% **[directional, peer Salesforce/Shopify]**. Recruiter voice: a campus/SaaS screener looking for an eligible undergrad who already shipped full-stack or backend software, can debug production, and is excited about a high-scale messaging+data product — not a marketing intern and not an ML researcher.

**Eligibility (computed):** Expected May 2028 is inside "December 2027 or May/June 2028." US citizen; no sponsorship needed vs JD not eligible for immigration sponsorship. Class standing at Spring 2027 co-op: **junior**. ≥1 prior SWE intern/co-op is a hard experience filter, not a class-year computation. GPA is not a hard JD floor (Greenhouse GPA bands exist). Resume must still pass the ~7-second scan; after that the OA is the binding intern filter (`recruiting.md` Part I §1 / Part II §8). Apply by 2026-10-07 if possible (rolling; first_published 2026-09-12).

Winning *kinds* of evidence: JD languages the candidate actually has (**Python**, **TypeScript**) demonstrated in bullets, not Skills alone; React / Redis / AWS EC2 through use; a shippable API+UI or production backend with a persistence decision and a deploy path; named production debug or incident-adjacent repair; tests/CI through use; data-pipeline or queue/Redis flavor as the CDP/messaging differentiator. Intern-stage weighting still favors engineered projects plus live GitHub (`resume.md` Part II intern). Django, Go, Kafka, Cassandra, ClickHouse, Terraform, Aurora are plus-and-train (or absent) — not fabrication targets.

## Screen Criteria

**Pass signals (abstract):**

- Polyglot proof for languages the candidate actually has that the JD names (**Python**, **TypeScript**). Keyword-through-use in bullets, not Skills-only (`resume.md` §2). React, Redis, AWS (EC2) through an architectural decision when present. **Do not invent Django, Go, Kafka, Cassandra, ClickHouse, Terraform, Aurora, MySQL (unless a legal swap is applied consistently), Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Redshift, or Kinesis.**
- Shipped full-stack software: REST/APIs, a real frontend surface, a persistence decision, and cloud/deploy (AWS/Docker/CI) tied to an outcome (`resume.md` §12). Breadth across the stack plus depth in at least one layer — matches team-agnostic FE/BE/FS placement.
- Production debug or incident-adjacent repair with a witness metric — matches "debug locally and in production" / incident support. Tests or CI through use matches write/test/ship.
- Performance or scalability through use (UI jank, latency, queue/worker drain, query time) — the JD's concrete failure modes.
- CDP / messaging-platform flavor on that spine: production APIs, customer-or-lead data pipelines, Redis/queue workers, AWS delivery — memorable here without replacing the SWE spine and without inventing Klaviyo products.
- Prior titled SWE internship or co-op visible on the page (hard JD filter).
- AI as *workflow or product experimentation* in existing work — never as Copilot, never as an ML-intern lead.
- Class-year on the page: `Expected May 2028` satisfies the graduation window.

**Anti-patterns:**

- Skills-line Django / Go / Kafka / Cassandra / ClickHouse / Terraform / Aurora / Copilot with zero bullet evidence (fabrication smell at a polyglot SaaS shop).
- Invented Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, Redshift, Kinesis, or Klaviyo-platform claims (email editor, Kinesis+Redshift, WhatsApp DOI) because former co-ops used those.
- Agentic-eval / LoRA / notebook-ML as the first-pass identity (AI-first is how they work, not an ML-training intern seat).
- Hard-real-time C++/audio-DSP as the first-pass identity when the role tests Python/TypeScript/React web+data SWE.
- Club-ops, community-growth, or coursework-only framing with no shipped application.
- Thin single-bullet entries that dilute a full-stack + data-platform spine.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact (`resume.md` §4).
- Skills-only Python/TypeScript/React with no architectural decision in bullets.

## ATS Keywords

Python, TypeScript, React, Redis, AWS, EC2, REST, production, debugging, testing, shipping, scalability, performance, full-stack, APIs, Git, Docker, PostgreSQL, CI, Flask
