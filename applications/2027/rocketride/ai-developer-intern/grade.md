# AI Developer Intern at RocketRide

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — current B.S. Computer Science & Economics student (Expected May 2028), enrolled at Summer 2027 and returning after; no sponsorship needed; JD imposes only current-student enrollment. Onsite ≥3 days/week in SF is workable given willingness to relocate for the term.
- **Track:** ai-ml (differentiator: open-source, developer-native agentic-AI tooling on a high-performance C++ engine; track_divergence = false)
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Leads with a genuinely shipped agentic system — Vylet: a Dockerized LangGraph pipeline with a LangSmith adversarial-eval harness and Pydantic consensus gates (50%→90% faithfulness), live at $1,500 MRR — which is almost exactly RocketRide's "agentic workflows + LLM integration + eval" surface in miniature.
- The ML spine is on-theme and verifiable: SignalWeaver LoRA fine-tune of Llama-3.1 (81%→96%, held-out), pgvector cosine similarity search (49ms p50 / 99ms p99) — a literal match to the platform's vector-DB core — plus a containerized GitHub Actions CI stack, with a live repo link.
- Rare company-fit bonus: the Granular Synthesizer plugin shows real C++ lock-free / zero-allocation systems depth that echoes RocketRide's multithreaded C++ engine — a differentiator most applied-AI intern candidates cannot offer.

### Demerits

- **minor** · `Vylet` · metric-free bullet, soft close — the asyncpg DAL / injection-safe re-scrape bullet ends on "fresh without manual intervention" with no number, so a reader can't size the freshness/reliability impact.
- **minor** · `resume` · no developer-community / open-source-contribution signal — the JD explicitly wants OSS contribution and DevRel/community presence (Discord, forums, technical content); the page shows strong personal repos and a live product but no upstream contribution or public community footprint.
- **minor** · `resume` · no multimodal / vision evidence — the JD names vision models and multimodal data pipelines as build areas, but the shipped work is text, audio, and tabular only, so that lane is unaddressed.

### Misreads

- A rushed screen weighting "public contribution" literally could read this as strong-but-private work and miss that the released VST3/AU plugin, live product, and public repos are genuine public artifacts.
- A skim hunting "vision" / "multimodal" keywords may bucket the candidate as LLM/text-only and under-credit the agentic + vector-search + C++ breadth actually on the page.

### Interview angles

- **Lead with:** the Vylet LangGraph pipeline + LangSmith adversarial-eval harness and Pydantic consensus gates (agentic orchestration + evaluation), then SignalWeaver's LoRA fine-tune + pgvector similarity search — the two systems map directly to RocketRide's agentic-workflow builder and vector-DB nodes.
- **Defend:**
  - Open-source/DevRel footprint → point to the released open-source VST3/AU plugin, the live Vylet product, and the public GitHub repos as real public contribution, and be ready to speak to engaging RocketRide's Discord/repo *(out of rails: no pool bullet describes an upstream OSS PR, technical content, or community/DevRel activity — a genuine profile gap to close before applying)*.
  - Vision / multimodal → frame SignalWeaver's multi-signal (fundamentals + macro + news) pipeline and the audio VAD/ONNX work as multi-source data-pipeline experience, and speak to how vision models would slot into the same orchestration *(out of rails: no pool entry ships a vision/CV model)*.
  - Vylet freshness bullet → have a concrete staleness-detection / re-scrape number ready to narrate live *(out of rails: no metric-bearing verbatim pool bullet for that specific claim)*.
- **Depth prep:** LangGraph multi-node orchestration + how the LangSmith eval harness and Pydantic consensus gates would generalize to RocketRide's node/agent framework; LoRA fine-tuning methodology and held-out eval; pgvector embedding-retrieval latency and how it maps to the platform's 8 vector DBs; the C++ lock-free SPSC FIFO / zero-allocation audio-thread design and how that discipline transfers to a multithreaded pipeline engine; MCP, CrewAI/OpenClaw, neo4j, and Cursor familiarity (name what you've touched honestly, and skim their docs before the call).

## Likelihood

- **Resume screen:** High — a shipped, evaluated agentic LangGraph system leads, similarity/vector search is demonstrated with real latency numbers, and there's genuine C++/lock-free performance depth — exactly this team's spine plus its rare bonus.
- **Overall hire odds:** Medium-High — at a resume-and-project-first startup the page clears the screen easily and sets up a strong project deep-dive the candidate can narrate decision-by-decision; the untested axes are the open-source/DevRel-community fit this team explicitly cares about and founder fit, which is where the offer is actually won.
- **Funnel filters:** ~2–3 rounds (resume screen → project deep-dive → founder/team fit) · practical/project-depth over LC-marathon · no published OA platform · no formal sys-design for interns · eligibility gate is current-enrollment only (met) · SF hybrid ≥3 days/week (relocation for the term required).
- **Outside the resume:** Build one visible public-contribution signal before applying — a PR to a RocketRide repo, engagement in their Discord/forums, or a short technical write-up — since it directly answers the one axis the resume leaves open. Network founder-direct rather than cold-applying (`recruiting.md` §5: HM > recruiter > engineer > cold apply), and apply early while the req is fresh.
