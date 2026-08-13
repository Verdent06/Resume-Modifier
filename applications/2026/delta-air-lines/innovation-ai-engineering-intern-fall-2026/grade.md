# Innovation & AI Engineering Intern (Fall 2026) at Delta Air Lines

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible — `Expected May 2028` undergraduate satisfies the JD's "actively enrolled in an undergraduate accredited college during the program" gate (this is the undergraduate posting, not the M.S./MBA/PhD graduate req)
- **Track:** ai-ml (Applied ML / GenAI) — differentiator: applied ML for airline customer/employee experience; no track divergence
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Genuinely strong applied-ML spine when read fully: SignalWeaver carries the end-to-end workflow the JD screens for (PyTorch LoRA fine-tuning 81%→96% on a held-out set, pgvector semantic search, out-of-sample regression, FastAPI serving with p50/p99 latencies), plus a live GitHub — exactly the "design and develop ML/AI-based products" bar.
- Python + PyTorch shown through use, not asserted; CaseStudyPrep adds model-serving/inference-cost signal (ONNX VAD, 40% cloud-inference cost cut), Vylet adds agentic eval (LangSmith 50%→90% faithfulness, 30x pipeline), and MDC now shows direct stakeholder scoping — mirroring "engage business stakeholders."
- Binding ding on a 30-second scan: Experience leads with voice-AI inference optimization, so the flagship PyTorch modeling work sits fourth (in Projects) and can be undervalued on a fast skim.

### Demerits

- **major** · `resume` · lead off-axis — top of Experience is voice-AI inference optimization (VAD/ONNX, Web Workers); the deepest PyTorch fine-tuning, held-out eval, and serving work sits fourth in Projects, so a 30-second scan undersells ML-model development. *(structural: the only true model-training entry is a personal project, which resume.md I.3 keeps below Experience — the writer front-loaded the most ML-flavored Experience entry as mitigation.)*
- **minor** · `Education` · thin ML coursework — coursework lists stats and core CS but no ML, linear algebra, or probability course, a weak math/ML foundation signal for an applied-ML screen. *(out of rails: Education block is immutable and the pool has no such course.)*
- **minor** · `resume` · narrow JD domain footprint — NLP/embeddings and GenAI eval are well evidenced, but computer vision, anomaly detection, gradient-boosted trees, and deep RL (named in the JD) have zero bullet support anywhere. *(out of rails: no verbatim CV/anomaly/GBT/deep-RL bullets in the pool; recommendation/personalization is covered adjacently by embedding-based semantic search.)*

### Misreads

- A rushed recruiter may bucket the candidate as a voice-AI / SWE-inference engineer or an agentic-GTM builder from the top half, missing that the flagship SignalWeaver work is real neural-net fine-tuning with held-out evaluation.
- Without an ML or linear-algebra course on the transcript line, a screener may under-credit the math foundation even though the modeling work on the page demonstrates it.

### Interview angles

- **Lead with:** SignalWeaver end-to-end (data → LoRA fine-tune → held-out eval 81%→96% → pgvector semantic search → out-of-sample regression → FastAPI serving); CaseStudyPrep ONNX on-device inference cutting cloud cost 40%; Vylet LangSmith adversarial eval (50%→90% faithfulness) + 30x Dockerized pipeline; MDC direct MCFN stakeholder scoping.
- **Defend:** Flagship ML sits below Experience — narrate SignalWeaver early and volunteer it as the headline *(out of rails: lead off-axis)*. No ML/linear-algebra course on the page — point to fine-tuning, held-out evaluation, and regression validation as applied proof of the math *(out of rails: thin ML coursework)*. No CV/anomaly/GBT/deep-RL — frame transferable modeling judgment and embedding-based recommendation adjacency; be honest about depth *(out of rails: narrow JD domain footprint)*.
- **Depth prep:** LoRA fine-tuning trade-offs and held-out evaluation methodology; embeddings / pgvector semantic search; ONNX client-side inference cost/latency; airline applied-ML domains (personalization/recommendation, anomaly detection) at a conceptual level; STAR behavioral stories for HireVue (Delta weights behavioral heavily).

## Likelihood

- **Resume screen:** Medium — eligibility and flagship ML depth are solid when read fully, but front-loaded inference/agentic work makes the first pass easy to misread at competitive enterprise intern volume.
- **Overall hire odds:** Medium — the substance is there for HM depth, but this funnel weights fit and communication heavily, and the field includes candidates whose lead entry reads PyTorch-training on day one.
- **Funnel filters:** Resume screen (Avature portal, human + ATS) → HireVue on-demand behavioral ("virtual job tryout," STAR method) → virtual hiring-manager interview (AI manager + department; resume projects mapped to JD, behavioral + light case). No big-tech coding OA gauntlet; behavioral/culture fit is the bottleneck. Onsite Atlanta; undergraduate current-student eligibility passes.
- **Outside the resume:** A warm referral or Delta/alumni intro moves the app from the cold pile to a careful read (`recruiting.md`: referrals multiply interview odds); prep STAR stories that connect stakeholder scoping (MDC nonprofit contract, Vylet paying clients) to ML delivery, and be ready to whiteboard SignalWeaver's full workflow in the HM round.
