# Software Engineer, Intern (Summer 2027) at Pylon

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — `Expected May 2028` sits inside the JD's December 2026–Summer 2028 window; CS+Econ undergrad; willing to relocate to San Francisco for Summer 2027
- **Track:** full-stack (screen) + AI-native / agentic B2B product engineering (differentiator; no track divergence)
- **Pipeline:** 6 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Leads with the employed `CaseStudyPrep.AI` Software Engineer Co-op — production voice-AI wins (40% inference-cost cut, 27% upload-failure fix in RxJS/TypeScript) — an employed-team product-engineering first impression, not a solo-founder GTM scoreboard.
- AI-native ownership is on-axis: `Vylet` is a live Dockerized LangGraph product with Redis/Celery workers, LangSmith eval (50%→90% faithfulness), and a diagnosed 79%→89% qualification-rate fix, plus a public `vyletdata.com` link.
- Full-stack exhibit is complete in `SignalWeaver` (React/TypeScript dashboard, FastAPI REST, Postgres/pgvector, Docker Compose, GitHub Actions CI) plus a production Flask REST API on AWS EC2 at MDC. Binding dings are framing, not missing gates: the co-op lead is pipeline reliability, and the React app is a personal research harness.

### Demerits

- **minor** · `CaseStudyPrep.AI` · lead is pipeline reliability, not a user-facing feature — both bullets are client-side VAD and S3-upload failure handling; a product-engineering screen never sees a UI or workflow feature in the lead.
- **minor** · `SignalWeaver` · research-harness framing, not a shipped user product — React/FastAPI/Postgres/CI is the page's only full-stack UI story, but the evidence is 90 self-run tickers and batch p50/p99, not users.

### Misreads

- A rushed skim can bucket CaseStudyPrep as "audio ML intern" and miss that it is the employed TypeScript/RxJS shipping story for a React/TS shop.
- SignalWeaver's "not investment advice" tagline can be misread as a class project rather than the only end-to-end React + API + DB + CI build on the page.

### Interview angles

- **Lead with:** `CaseStudyPrep.AI` as the employed-team ship (ONNX/Silero cost cut, RxJS/S3 fault-tolerance); `Vylet` as the AI-native product you own end-to-end (LangGraph + eval gates + paying clients); `SignalWeaver` as the spec-to-ship full-stack sample (React/TS + FastAPI + Postgres + Docker + GHA) — narrate it the way Pylon's "prototype, iterate, ship fast" JD frames the intern project.
- **Defend:** React depth is project-scale, not titled-role — the co-op frontend is Angular/RxJS; say that plainly and use SignalWeaver plus framework-pickup as the bridge *(out of rails: pool has no titled-role React product and cannot promote SignalWeaver into Experience)*. SignalWeaver has no external users in the pool — don't invent them; point to Vylet's three paying clients and MDC's nonprofit stakeholder as the real-user shipping evidence *(out of rails: SignalWeaver pool is personal 90-ticker / 90-run metrics)*. Go and GraphQL are JD bonuses, not inventory — do not claim them.
- **Depth prep:** practical build-a-feature rounds (not LeetCode volume) — defend FastAPI vs Flask, why Postgres/pgvector, what each CI stage guards; LangGraph + LangSmith eval design (treat the LLM as an unreliable dependency); autonomy/ambiguity stories from sole-engineer MDC and founder Vylet.

## Likelihood

- **Resume screen:** High — eligibility is on the page, titled AI-product shipping plus founder ownership with eval metrics is the intern packet this funnel wants, and a human reads the PDF early (Ashby).
- **Overall hire odds:** Medium — the resume clears the front door, but this is a small intern class at a hot ~120-person AI startup; the remaining filter is practical build-and-ship plus autonomy/collab fit, not an OA gauntlet.
- **Funnel filters:** ~3–4 rounds · practical (build-a-feature) difficulty · likely no heavy OA · light/no sys design for interns · Bottleneck: resume screen + practical technical rounds · Dec 2026–Summer 2028 graduation window · onsite SF / willing to relocate.
- **Outside the resume:** Referral up the HM > recruiter > engineer ladder. Apply within ~72 hours of the req opening. Timed mocks of a practical feature-build, not LeetCode volume. Do not overclaim Go/GraphQL or titled-role React.
