# Intern, Agent Development (Summer 2027) at Sierra

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 sits inside the intern window December 2027 – June 2028
- **Track:** full-stack + production AI agents for enterprise customer experience
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Vylet leads with a Dockerized LangGraph pipeline, LangSmith eval gates (50%→90% faithfulness), a diagnosed ship (79%→89% qualification), and live $1,500 MRR — production agents in the first pass.
- SignalWeaver puts TypeScript/React, pgvector semantic search, and a 5-node LangGraph pipeline in bullets; MDC is a sole-engineer Flask REST API on EC2 shipped to a real nonprofit.
- Binding dings: the Flask/EC2 line has no metric; nothing on the page is customer-experience / support, so a skim can bucket PE/fintech agents instead of CX.

### Demerits

- **minor** · `Michigan Data Consulting (MDC)` · metric-free API bullet — Flask REST API on EC2 is still unquantified; the ETL hook has ~800 hours but the production-API line itself has no number a screen can size
- **minor** · `resume` · no customer-experience domain — Sierra builds enterprise CX agents; the page is PE lead-sourcing, campaign-finance, voice-AI, and financial research — agent/eval/RAG engineering is present but no CX or customer-support adjacency

### Misreads

- MDC's unnumbered API line can read as spreadsheet/ETL consulting rather than the production REST spine that is the real full-stack proof.
- A rushed Ashby skim may file this as a PE/fintech agent intern and miss the eval/RAG/LangGraph craft Sierra actually screens for.

### Interview angles

- **Lead with:** Vylet LangGraph launch + LangSmith eval harness + name-collision ship; SignalWeaver React/TypeScript dashboard + pgvector search + LangGraph latency breakdown; MDC sole-engineer Flask/EC2; CaseStudyPrep on-device VAD cost cut
- **Defend:** MDC API metric *(out of rails: Flask/EC2 pool bullet has no impact number; remaining MDC pool lines are also metric-free or drop the REST spine)* — narrate what you would measure (p50 latency, request volume, researcher time saved via the API). CX domain *(out of rails: no CX/support bullets in the pool)* — frame eval gates, RAG retrieval, and agent tooling as the transferable CX-agent craft; use Customer Obsession stories from MCFN stakeholder delivery and paying Vylet clients
- **Depth prep:** LC medium–hard (take-home or online); light intern agent systems design (LangGraph topology, eval harness, RAG trade-offs); values (Trust, Customer Obsession, Craftsmanship, Intensity, Family) as a filter round not the screen differentiator

## Likelihood

- **Resume screen:** High — Vylet leads with LangGraph + LangSmith evals and paying clients; TypeScript/React and pgvector search are in bullets; one clean page
- **Overall hire odds:** Medium — A-tier Ashby funnel with resume + practical bottleneck; take-home/online is LC med–hard plus agent design, then onsite coding + agent sys design + values. Strong PDF still has to clear a small intern class (<3–5% directional)
- **Funnel filters:** Ashby resume screen (human reads PDF) · take-home or online tech (LC med–hard; agent design) · onsite coding + agent sys design + values · Bottleneck: resume + practical · <3–5% **[directional]** · graduation window Dec 2027 – Jun 2028
- **Outside the resume:** Apply immediately (rolling Ashby; resume is the first real filter). Prep LC medium–hard plus a walkthrough of the LangGraph/eval harness and the React/TypeScript + pgvector path. Values stories for Trust / Customer Obsession / Craftsmanship
