# 2027 Summer Internship - Machine Learning Engineer at Q2 Software, Inc.

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 Junior, US citizen vs currently pursuing CS/DS/ML or related; JD has no class-year/GPA gate; authorized to work for any US employer / no visa sponsorship
- **Track:** ai-ml (fintech-fraud-ml / Risk & Fraud / Iso Framework emphasis; screen track and company identity agree — no divergence)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Vylet leads with a Dockerized LangGraph scoring pipeline and a LangSmith eval harness (50%→90% faithfulness) — applied train/eval analog, not notebook `model.fit()` and not generic SWE.
- SignalWeaver is the modeling proof: PyTorch + LoRA classification 81%→96% on a held-out set, plus an out-of-sample regression score. Lyndbrook Review Velocity (800→280, 35% precision) is the risk/scoring analog.
- Binding ding: CaseStudyPrep still reads as a voice-AI co-op, and the page never prints fraud/risk/identity-behavior-transaction — a Risk & Fraud keyword scan can miss the domain fit.

### Demerits

- **minor** · `CaseStudyPrep.AI` · voice-AI co-op on an applied-fraud-ML intern — Title and the single bullet are silent-audio / Whisper / ONNX in a voice product. Production-inference analog is there, but a 30-second screen buckets this as a voice-frontend co-op rather than fraud/risk model work.
- **minor** · `resume` · fraud/risk-modeling terms never appear — Nice-to-have on the JD is fraud detection or risk modeling. Scoring/precision analogs exist (lead scoring, 35% precision shortlist) but the page never says fraud, abuse, risk, identity, behavior, or transaction — a keyword scan can miss the domain fit.

### Misreads

- A Risk & Fraud screener keyword-scanning for fraud / abuse / identity / transaction can file this as generic applied-ML / lead-scoring, not Iso Framework-adjacent detection work.
- CaseStudyPrep.AI at the bottom of Experience can read as "this candidate also does voice products," momentarily thinning the MLE signal from Vylet + SignalWeaver.
- TensorFlow / scikit-learn / R / Java named on the JD and absent from the page can look like a stack miss even though Python + PyTorch through use is the honest inventory match.

### Interview angles

- **Lead with:** SignalWeaver LoRA held-out classification (81%→96%) and the out-of-sample regression as the model-development / evaluation walk; Vylet LangSmith eval + scored-leads pipeline as training/eval/inference-adjacent product ML; Lyndbrook Review Velocity (35% precision) as the risk-model / scoring analog for identity-adjacent entity shortlists.
- **Defend:** CaseStudyPrep is on-device ONNX inference and cost/monitoring analog, not the fraud-ML spine — say it backs "monitor production ML / inference," then return to SignalWeaver/Vylet *(out of rails: all CSP pool bullets are voice-AI; loop cannot omit the iter-1 entry; Granular DSP is more off-axis)*. The page never says fraud/risk — narrate scoring, precision, held-out classification, and hard-fail/consensus gates as detection-shaped work without inventing Iso Framework or bank-fraud internships *(out of rails: no pool bullet contains fraud/abuse/risk/identity/behavior/transaction; swap sets cannot bridge)*. Do not invent TensorFlow, scikit-learn, R, Java, Copilot, Snowflake, Databricks, Tableau, or Fusion.
- **Depth prep:** LoRA data curation + held-out eval vs overfitting; Lyndbrook precision against a business criterion as experimental method; Vylet eval harness failure modes; MDC Pandas ETL + Flask API as training/eval/inference pipeline analog. No published OA — expect Easy–Med applied-ML project walk + STAR (`recruiting.md` §13 / §6). Behavioral is a filter.

## Likelihood

- **Resume screen:** Medium-High — SignalWeaver shows PyTorch next to a held-out LoRA classification, Vylet carries an eval harness, and Lyndbrook is a scored shortlist with a precision number; remaining dings are a voice-AI co-op slot and missing fraud vocabulary, not a missing modeling loop.
- **Overall hire odds:** Medium — unpublished OA; 1–2 hiring-team interviews plus STAR. The modeling walk is defensible; C-tier resume bottleneck (~15–25%) means the voice-AI entry and absent fraud terms still skim a few screens, not the loop.
- **Funnel filters:** Workday `q2ebanking.wd5` / Q2 **REQ-12800** resume (`includeResumeParsing: true`) → TA screen (qualifications + interest) → **1–2 hiring-team interviews** → offer (typical **2 weeks**). Intern OA unpublished — do not invent HackerRank/CodeSignal. No intern sys design. English + US work-auth without visa are knockouts (cleared). Bottleneck: **resume** (`companies.md`).
- **Outside the resume:** Apply in this first wave (posted 2026-09-29). Honest US citizen / no sponsorship. Prep the LoRA held-out walk and a scoring-as-risk-model story; STAR on MCFN/Lyndbrook stakeholder delivery.
