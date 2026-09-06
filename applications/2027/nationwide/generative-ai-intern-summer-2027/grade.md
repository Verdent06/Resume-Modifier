# Summer 2027 Generative AI Internship at Nationwide

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** Eligible — no class-year exclusive on req 100231; "graduate candidates will be considered" is additive. B.S. Computer Science and Economics, University of Michigan, Expected May 2028, GPA 3.66. US citizen / no STEM OPT / no entry-level sponsorship. Columbus onsite May–August 2027 is acceptable.
- **Track:** ai-ml (applied GenAI / agentic-AI; insurance / EAO applied analytics is within-track emphasis — no divergence)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is a live LangGraph + LangSmith eval system (30x speedup, 50%→90% faithfulness) plus Gemini embeddings/SQL freshness — the JD's LLM/agent/eval bar, with Python in the bullets.
- SignalWeaver LoRA (81%→96% held-out) and pgvector retrieval (49ms p50) cover generative modeling and the vector/RAG analog; MDC Pandas ETL + Flask on EC2 is business-partner delivery. GPA 3.66 and a live GitHub clear the resume-first C-tier intern screen.
- Binding dings: the page's identity is PE/search-fund, campaign finance, and financial research — an EAO screener looking for insurance value-chain GenAI has nowhere to land except "we shipped to non-ML users." PyTorch is Skills-only.

### Demerits

- **minor** · `resume` · company-fit differentiator absent — The differentiator is insurance / EAO applied analytics; the page's identity is PE/search-fund lead-gen, campaign-finance ETL, and financial-research RAG. Closest analog is stakeholder-scoped MDC delivery, with no insurance, claims, underwriting, or policy-operations signal.
- **minor** · `Skills` · PyTorch only in Skills — JD lists PyTorch in the Python/ML-library e.g. set. Skills names PyTorch; no bullet says PyTorch. The LoRA Llama-3.1-8B line is the generative-modeling proof, but a keyword scan for PyTorch-through-use finds only the Skills row.

### Misreads

- A Columbus EAO screener skimming titles could bucket this as a PE/fintech founder resume and miss that the work is agent orchestration, eval, embeddings, and RAG-style retrieval for non-ML users.
- A keyword pass for PyTorch/TensorFlow/sklearn could file the Skills line as stuffing if they do not read the LoRA bullet.

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval (20 adversarial cases, Pydantic consensus gates, 50%→90% faithfulness) as the analog to "LLMs, AI agents, and agentic workflows"; then SignalWeaver LoRA + pgvector as generative modeling and vector/RAG; then MDC ETL + Flask API as end-to-end delivery to business partners.
- **Defend:** No insurance/claims/underwriting work exists in the pool — say so, then map MDC's researcher-facing API and irregular-document ETL onto "work with business partners to develop integrated, end-to-end solutions." PyTorch is in inventory and on Skills; the named work is LoRA on Llama-3.1-8B and LangGraph agents — do not invent TensorFlow, scikit-learn, Kubernetes, or a P&C model. *(out of rails: pool has no insurance/claims/underwriting bullet; no pool bullet names PyTorch)*
- **Depth prep:** Walk the eval harness (archetype labels, faithfulness lift, when the consensus gate hard-fails); pgvector cosine retrieval vs a claims/document RAG; embedding freshness/re-scrape; how you would validate an insurance LLM workflow without claiming you have already done one.

## Likelihood

- **Resume screen:** High — LangGraph/LangSmith eval, LoRA held-out NLP, pgvector retrieval, Pandas ETL, stakeholder APIs, Python-through-use, sized metrics, live GitHub, and 3.66 GPA clear every abstract pass signal on a resume-first C-tier screen.
- **Overall hire odds:** Medium — Nationwide intern loops are Easy and resume-weighted (`companies.md` C-tier ~15–25%; `recruiting.md` mid-size/non-tech-tech). Clearing the PDF is most of the front end; two live rounds (STAR + project walkthrough) still eliminate if the transfer story to EAO insurance partners is weak, or if they quietly prefer graduate students.
- **Funnel filters:** Workday ATS req **100231**; no standard intern OA published. Recruiter auth/location/enrollment, then 2–3 Easy live rounds. US work-auth / no STEM OPT knockout (met). Posted 2026-09-04; Workday `endDate` 2026-11-15.
- **Outside the resume:** Apply in this window. No Nationwide contact in `network.md` — a Columbus EAO/alum referral beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply). Mock the eval-harness walkthrough mapped onto insurance-document RAG; keep STAR stories for the behavioral filter. See `written-answers.md`.
