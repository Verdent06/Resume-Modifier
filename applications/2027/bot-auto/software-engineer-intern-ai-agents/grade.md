# Intern, Software Engineer AI Agents (Winter 2027) at Bot Auto

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** Eligible — JD requires currently pursuing BS/MS CS/Engineering/related; no class-year or GPA knockout. B.S. Computer Science and Economics, University of Michigan, Expected May 2028 (Junior at a Jan–Apr 2027 intern). US citizen; Greenhouse work-auth / no-sponsorship knockouts pass.
- **Track:** ai-ml + autonomous-trucking / fleet-ops TaaS
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is a live LangGraph agent pipeline (Docker/Redis/Celery, 30x speedup) plus LangSmith eval (50%→90% faithfulness) and OpenAI embeddings — the JD's agent/eval/LLM bar on a C-tier Greenhouse human screen.
- SignalWeaver carries the preferred stack through use: 5-node LangGraph, pgvector retrieval (49ms p50), FastAPI serving, TypeScript dashboard. MDC Flask/AWS is backend APIs; CaseStudyPrep.AI is ONNX inference on a titled SWE co-op. GPA 3.66 and a live GitHub clear intern format.
- Binding ding: every domain is PE/search-fund or financial research. A Houston TaaS screener looking for agents on fleet/ops workflows has no operational-trucking landing zone.

### Demerits

- **minor** · `resume` · fleet-ops / TaaS operational domain absent — The shipped page leads with PE/search-fund LangGraph agents and financial-research RAG. MDC is campaign-finance ETL/API. A Houston autonomous-trucking TaaS screen still sees no fleet/ops workflow domain.

### Misreads

- A Houston AV recruiter skimming titles (Vylet, SignalWeaver, campaign finance) could bucket this as a PE/fintech founder resume and miss that the work is agent orchestration, eval, tool/consensus gates, and RAG/API delivery.

### Interview angles

- **Lead with:** Vylet LangGraph + Redis/Celery workers (30 scored leads / 30 minutes, 30x) and the LangSmith eval harness (20 adversarial cases, Pydantic consensus, 50%→90% faithfulness) as the analog to "planning, tool usage, memory, multi-step reasoning" plus evaluation. Then SignalWeaver LangGraph → pgvector → FastAPI as RAG + backend deploy. Then MDC Flask on EC2 as internal-systems integration.
- **Defend:** No autonomous-trucking, ROS, or fleet-ops engineering exists to put on the page — say so, then map Vylet's operational-workflow automation (manual process → agent pipeline with eval/fail-closed gates) onto fleet/business-process agents without claiming you have shipped on a truck. Do not invent LangChain, AutoGen, Go, Java, Kubernetes, or perception/world-model work. *(out of rails: no live pool entry carries AV/fleet-ops engineering; Lyndbrook's "fleet expansion" line is GTM deal-sourcing and overflows a 95% page)*
- **Depth prep:** Walk Node-style consensus vs LLM-as-judge; LangSmith adversarial archetypes; embedding freshness/re-scrape; pgvector cosine vs a fleet-document RAG; FastAPI + Docker deploy of an agent service. Easy–Med Python/agent project walk; intern OA unpublished — do not assume HackerRank/CodeSignal. STAR for the behavioral filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — LangGraph orchestration, LangSmith eval (50%→90% faithfulness), OpenAI embeddings, FastAPI, pgvector RAG analog, Docker/Redis/Celery, titled SWE co-op with ONNX inference, TypeScript and Python in Skills, live GitHub, GPA 3.66. C-tier resume-first intern bar.
- **Overall hire odds:** Medium — Bottleneck is the Greenhouse resume (~15–25% directional). PDF should pass a human agent-intern screen; unpublished project-walk + STAR still filters people who cannot transfer PE-agent work onto ops automation, or who miss a medium Python/agent exercise.
- **Funnel filters:** Greenhouse **5429357008** / req **3012**; onsite Houston Office; Winter 2027 only (skip Fall 2026). Work-auth + sponsorship knockouts (met). Intern OA unpublished. No intern sys design published. Bottleneck: resume.
- **Outside the resume:** Apply in the first-wave window (first_published 2026-09-18). Cold Greenhouse — a Houston/AV or TuSimple-alumni intro beats the pile. Drill the eval/consensus-gate walkthrough framed as an ops-automation agent without claiming trucking or ROS experience.
