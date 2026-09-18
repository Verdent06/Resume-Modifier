# Intern AI Center of Excellence Data Science at Smith+Nephew

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — currently enrolled B.S. Computer Science (listed majors include CS); Expected May 2028 so still a student after the May 2027 12-week term; US citizen vs no visa sponsorship
- **Track:** ai-ml (medical robotics / enabling technology is within-track flavor — no divergence)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- UMich CS + Economics, GPA 3.66, Expected May 2028, stats/calc coursework — class-year and academic-ML bar clear.
- Spine is applied ML, not SWE or notebook-only: LoRA held-out 81%→96%, out-of-sample regression (3.39% R²), Pandas ETL, LangSmith eval 50%→90%, React dashboard as the PoC interface.
- Binding dings: CaseStudyPrep.AI reads as voice-inference/UI; nothing on the page is surgical robotics / CORI.

### Demerits

- **minor** · `CaseStudyPrep.AI` · voice-AI co-op reads as inference-cost/UI, not training-data/stats modeling — ONNX Silero VAD and a 60 FPS visualizer are real inference work; a CoE screener hunting training-set prep and statistical validation will bucket this as a voice-product frontend co-op
- **minor** · `resume` · company-fit differentiator absent — differentiator is medical robotics / enabling technology; page identity is PE lead-gen, campaign-finance ETL, voice-AI, and financial-research modeling

### Misreads

- A Pittsburgh Robotics screener skims titles and buckets this as a PE/fintech founder resume, missing LoRA + R² + Pandas ETL.
- CaseStudyPrep.AI as the only "co-op" title gets extra weight and the page is misread as a voice-AI frontend intern.

### Interview angles

- **Lead with:** SignalWeaver LoRA (held-out 81%→96%) plus out-of-sample regression (3.39% R²) as the data→model→validate workflow; then Vylet LangSmith eval (50%→90%) and embeddings/freshness as PoC + data-quality; then MDC Pandas ETL as obtain/clean training-data analog.
- **Defend:** No CORI, ROS, or surgical-device internship — say so, then map LoRA/eval/ETL onto an AI CoE PoC. No scikit-learn, TensorFlow, Keras, NumPy, R, or MATLAB — Python + Pandas + PyTorch only. CaseStudyPrep is ONNX inference, not training-set work. *(out of rails: pool has no medtech/robotics bullet; CaseStudyPrep pool is voice-AI only.)*
- **Depth prep:** Walk LoRA setup, held-out split, and why 3.39% R² is a validation result not a vanity score; LangSmith adversarial cases vs a model-eval harness; how you would prep a robotics/OR dataset you have never seen without claiming you already have one.

## Likelihood

- **Resume screen:** High — Python/Pandas/PyTorch, held-out ML, statistical validation, data-prep ETL, prototype UI, live GitHub, 3.66 GPA on a resume-first B-tier intern screen; two minors are dings not knockouts
- **Overall hire odds:** Medium — B-tier resume-first (~10–15% peer Medtronic); PDF likely clears; HireVue + HM still filter on the data→model→validate walkthrough and Pittsburgh onsite / no-sponsorship knockouts
- **Funnel filters:** Workday (`smithnephew.wd5`) R92480; `endDate` **2026-09-25**; no published intern OA; HireVue / Modern Hire listed on careers; no visa sponsorship
- **Outside the resume:** Apply this window (posted 2026-09-17, closes 2026-09-25). No Smith+Nephew contact in `network.md`. Do not apply to R92482 / R92481 on this PDF.
