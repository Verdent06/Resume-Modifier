# Software Engineer Intern (Winter 2027) at Together AI

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs JD degree earned or expected by Summer 2028; Winter 2027 intern (Jan 4–Apr 9) during junior year
- **Track:** full-stack + ml-infra / inference-cloud
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on Vylet: Dockerized LangGraph pipeline (30x) and a LangSmith eval harness (50%→90% faithfulness) — full-stack shipping plus ml-infra in the top half.
- CaseStudyPrep is a titled SWE co-op with on-device ONNX inference (40% cloud-cost cut) and Angular/RxJS S3 reliability; MDC is sole-engineer Flask REST on EC2 plus PAC ETL at 400 committees / ~800 hours.
- Binding dings: Granular's lock-free C++ has no sized latency closer, and TypeScript is proven on SignalWeaver rather than the titled co-op.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · real-time C++ with no sized latency/throughput closer — Lock-free SPSC and slab allocation read as genuine low-level systems depth the JD asks for, but neither bullet lands a microsecond, fps, or throughput number, so a Together screen cannot size the performance claim against inference/serving work.
- **minor** · `CaseStudyPrep.AI` · titled SWE co-op is Angular, not TypeScript — On-device ONNX inference and S3 reliability are the right intern signals; the JD's TypeScript language is proven only on the SignalWeaver side project, so a rushed screen can bucket the only titled SWE role as an Angular voice-AI co-op.

### Misreads

- Granular can skim as an audio hobby instead of the JD's low-level / performance-critical systems line.
- CaseStudyPrep can skim as "audio ML intern" and miss that it is the employed SWE co-op; TypeScript then looks Skills-only until SignalWeaver.

### Interview angles

- **Lead with:** Vylet LangGraph + LangSmith eval (50%→90%); CaseStudyPrep ONNX on-device inference cost; SignalWeaver LoRA 81%→96% and FastAPI 9.1s p50 / 15.2s p99; MDC Flask REST on EC2.
- **Defend:** Granular has no µs/ms/fps closer *(out of rails: pool bullets 1–6 have no impact-metric latency unit; swap sets cannot invent one)* — narrate lock-free SPSC + zero-heap audio thread vs GPU serving as "same class of real-time constraint." CaseStudyPrep is Angular/RxJS, not TypeScript *(out of rails: CSP pool never names TypeScript)* — say that plainly and walk SignalWeaver's React/TypeScript dashboard as the TS exhibit. Do not invent Go, CUDA, Kubernetes, vLLM, TensorRT-LLM, or SGLang.
- **Depth prep:** Timed LC mediums plus applied ML-systems coding (batching, serving, eval) for the ~60m tech screen; LoRA held-out eval; FastAPI p50/p99 vs fetch-dominated pipelines; ONNX on-device vs cloud inference cost; Flask/AWS deploy path. Light intern sys design possible on multi-tenant inference.

## Likelihood

- **Resume screen:** High — eligibility on the page, Python through use, a live product with eval, on-device inference, LoRA plus FastAPI p50/p99, C++ systems in the field; two framing dings, not a no-pile.
- **Overall hire odds:** Medium — A-tier ~2–4% with bottleneck at resume + tech (`companies.md`). The PDF deserves the recruiter/tech screen; the loop still eliminates on coding and inference-systems depth.
- **Funnel filters:** Greenhouse resume → recruiter ~30m → tech screen ~60m LC medium or applied ML-systems → 2–4 team rounds · Med–Hard · Light intern sys design · OA for some roles **[directional]** · Bottleneck: resume + tech · degree by Summer 2028 · SF on-site Jan 4–Apr 9 2027
- **Outside the resume:** Apply in this first-wave Greenhouse window; timed LC mediums + ML-systems serving/eval drills; no Together contact in `network.md` — do not mark referral.
