# Software Engineering Intern at Fable (Fable Security)

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028; Summer 2027 intern is Junior / rising junior; JD requires CS/SE/CE in progress with no class-year gate
- **Track:** full-stack
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: a production Flask REST API on AWS EC2, a Requests + Pandas ETL (~800 hours / 400 PACs), and a deterministic aggregation engine that ranks PACs — the JD's Python-backend + production-shipping floor.
- Vylet is a live Dockerized LangGraph product with Redis/Celery, a LangSmith eval (50%→90% faithfulness), and a named production defect (79%→89%) plus paying clients — gen-AI as a shipped surface, not notebook ML.
- SignalWeaver closes schema + API + tests (pgvector cosine search 49ms p50, FastAPI REST p50/p99, GitHub Actions pytest). Binding ding: CaseStudyPrep is a titled SWE co-op but client-side TypeScript, not a second Python-backend internship.

### Demerits

- **minor** · `CaseStudyPrep.AI` · SWE co-op is client-side TS, not Python backend — both bullets are Silero VAD via ONNX Runtime and RxJS/Angular/S3; no Python, API, or schema. At a shop whose floor is 2+ Python-backend internships, this titled co-op does not add a second Python-backend internship signal.

### Misreads

- A screener who treats "2+ internships in a Python backend" as two *titled SWE intern* lines could wait for the project walk (MDC is Data Engineer; Vylet is Founder; CSP is voice-frontend). The page still shows two Python-backend production systems (MDC Flask/ETL + Vylet LangGraph).

### Interview angles

- **Lead with:** MDC Flask REST on AWS EC2 and the Pandas ETL / aggregation engine as the Python-backend analog; then Vylet LangGraph/Redis/Celery, LangSmith eval, and the 79%→89% name-collision fix; then CaseStudyPrep Silero VAD / ONNX and RxJS S3 recovery as the titled SWE co-op (JS/Angular web analog); then SignalWeaver pgvector + FastAPI p50/p99 + GitHub Actions pytest.
- **Defend:** No GraphQL, notebooks-as-jobs, Java, Go, Snowflake, Databricks, Tableau, Copilot, Fusion, or React-through-use on the page — inventory is Python/TypeScript/Angular/Flask/FastAPI. CaseStudyPrep is the one titled SWE co-op (client-side voice, not Python backend); MDC is a contract Data Engineer role; Vylet is founder-owned Python pipeline — do not claim two "SWE Intern, Python backend" titles. *(out of rails: CSP pool has no Python/API/schema bullet; swap sets cannot bridge.)* SignalWeaver is a 90-ticker research harness — point to MDC's nonprofit workflow and Vylet's three paying clients for production users. No Fable / human-risk / gen-AI-video training work exists — map LangGraph + VAD as product-AI on a shipped system, not security-domain ownership. SF hybrid: currently Northville, MI; willing to relocate for the term.
- **Depth prep:** Walk the Flask contract (ingest → rank → REST on EC2); LangGraph/Redis/Celery drain and the name-collision fix; FastAPI + pgvector query path + GitHub Actions pytest. Easy–Med DS&A or a practical Python/API walk if a screen is issued (platform unpublished — do not invent HackerRank/CodeSignal). STAR for ownership, well-factored code, and iterating on a named production defect. Light intern sys design unpublished. Recruiter/founder: weekly ship cadence and SF hybrid (`recruiting.md` §6 filter).

## Likelihood

- **Resume screen:** High — one-page Python-backend + production API/pipeline story with a live gen-AI product, eval/defect metrics, and honest Angular through-use; Ashby human-read should not bounce this for a C-tier intern screen
- **Overall hire odds:** Medium — C-tier intern funnel ~15–25% **[directional, peer of Ibotta / early-stage SF product SWE]** with resume as the binding gate. The PDF likely clears; unpublished practical Python/API or Easy–Med DS&A if issued, SF hybrid from Michigan, and behavioral as a filter still sit downstream
- **Funnel filters:** Ashby **`3fd04c23-a63d-4b40-bfae-feafaa478caf`** resume (human-read early-stage) → unpublished intern loop (startup peer: recruiter + project walk / practical Python backend + STAR) · intern OA unpublished · No intern sys design published · Bottleneck: **resume** · ~15–25% · SF hybrid · full-time intern · CS/SE/CE in progress
- **Outside the resume:** Apply in this first-wave Ashby window (posted 2026-09-19). Confirm SF hybrid for the term. Form email **verdent06@gmail.com**. No Fable contact in `network.md` — a founder-adjacent referral still helps (`recruiting.md` §4). Prep a Python API/project walk and STAR; do not invent GraphQL or a named OA platform. See `written-answers.md`.
