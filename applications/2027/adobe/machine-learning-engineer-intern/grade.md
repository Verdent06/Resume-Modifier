# 2027 Intern - Machine Learning Engineer at Adobe

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** Eligible — JD class-year window is December 2027 – June 2028; page shows University of Michigan B.S. CS and Economics, Expected May 2028 (inside the window). Full-time May–September 2027 intern term is compatible with rising-senior standing.
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is a live LangGraph product plus a LangSmith eval harness (50%→90% faithfulness) — the JD's LLM-application and evaluation-framework signal, with Python-stack tools through use.
- SignalWeaver carries the modeling spine the intern req actually tests: LoRA fine-tune with held-out eval, pgvector search/retrieval, FastAPI serve. ONNX on-device inference and an AWS Flask deploy sit behind that. GPA 3.66, stats/calc coursework, live GitHub.
- Binding ding: Lyndbrook is a one-line PE scoring story in the bottom of Experience — a product-ML screener may read leftover deal-flow rather than a second applied-ML system.

### Demerits

- **minor** · `Lyndbrook Capital` · single bullet, PE scoring not product ML — One scoring-algorithm line on a titled consulting role; 35% precision is real, but the entry still reads as leftover deal-sourcing analytics rather than a second applied-ML system.

### Misreads

- A Firefly/Experience Cloud screener skimming titles could bucket this as a PE/search-fund founder resume and miss that the work is LLM orchestration, eval, LoRA, and retrieval.

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval (20 adversarial cases, Pydantic consensus gates, 50%→90% faithfulness) as the LLM-app / evaluation-framework analog; then SignalWeaver LoRA 81%→96% held-out + pgvector search + FastAPI serve as train → eval → retrieval → deploy.
- **Defend:** Lyndbrook is thin deal-sourcing analytics, not a second ML system — say so, then pivot to the scoring method and to SignalWeaver/Vylet for modeling and eval. No named PyTorch/TensorFlow/Hugging Face/LangChain/scikit-learn on the page; LoRA on Llama-3.1 is the honest DL-framework story — do not invent those tools. No creative-cloud or Firefly-domain work exists. *(out of rails: Lyndbrook second pool bullet overflowed the page; cannot name PyTorch in a verbatim pool bullet)*
- **Depth prep:** Walk the eval harness (archetype labels, faithfulness lift, when the consensus gate hard-fails); LoRA data split and held-out protocol; pgvector retrieval latency; ONNX VAD cost cut; HackerRank Mediums (arrays/strings/hash maps/DP) plus a project-based ML fundamentals set for the tech loop.

## Likelihood

- **Resume screen:** High — Eligible May 2028, 3.66 GPA, live GitHub, LangGraph+LangSmith eval lead, LoRA with held-out eval, pgvector search, FastAPI serve, ONNX inference and AWS deploy analogs. Remaining ding is a thin fourth experience, not track or eligibility.
- **Overall hire odds:** Medium — Adobe intern funnel is resume → HackerRank Medium → tech rounds (`companies.md` B-tier ~5–8%, bottleneck tech rounds; `recruiting.md` §8 OA-gated at scale). This PDF should clear the screen and team-match; OA plus live coding/ML-project depth still eliminate most eligible applicants.
- **Funnel filters:** Workday ATS; HackerRank OA (Medium; Extern directional: 60–90 min, 2–3 LC Medium). Recruiter screen, then CoderPad/tech deep dive; Light intern sys design. Graduation window December 2027 – June 2028 (met). Co-located hybrid at assigned office.
- **Outside the resume:** Submit on the rolling window immediately. No Adobe referral on file — a hiring-team intro beats cold Workday. Drill HackerRank Mediums and a 15-minute walkthrough of the eval harness plus LoRA held-out protocol before CoderPad/tech.
