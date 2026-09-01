# Software Engineer Intern, Cloud Services at HP IQ

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** ineligible — JD essential qualification is currently pursuing a Master's or PhD; page is B.S. Expected May 2028 (rising senior at Summer 2027; returns Fall 2027). Form "graduating before September 2027" is No, which does not clear the degree-level bar.
- **Track:** full-stack + device-cloud / AI-hardware ecosystem
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Top half is shipped cloud services: MDC Flask REST on AWS EC2, then CaseStudyPrep on-device VAD cutting cloud inference 40% plus S3 upload recovery — the device-cloud blend is visible, not an AML-training page.
- Vylet Docker/Redis/Celery (30x) and SignalWeaver FastAPI + Docker/GHA back the "services at scale" / automation preferred quals. Spring Boot is absent (preferred, not a floor).
- Binding ding is minor: Granular's lock-free C++ never sizes whether the plugin held load. The Master's/PhD knockout is the real filter, not this PDF.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — two lock-free C++ bullets prove real-time discipline but never size latency, CPU, xruns, or users

### Misreads

- A skim that stops on Granular's VST3/AU tech line can bucket this as a hobby DSP resume and miss the Flask/AWS + S3 + Docker/Celery cloud spine.
- Voice-AI / ONNX / LangGraph tokens can be misread as the AML Platform sibling (PyTorch / on-device inference req) rather than Cloud Services.

### Interview angles

- **Lead with:** MDC sole-engineer Flask REST on EC2; CaseStudyPrep Silero/ONNX on-device VAD (40% cloud-inference cost) and 27% S3 upload recovery; Vylet Docker/Redis/Celery 30x worker loop; SignalWeaver FastAPI + Docker Compose / GitHub Actions
- **Defend:** Granular has no latency/CPU/xrun/user number *(out of rails: full 6-bullet pool has no impact metric; entry is protected at 2 bullets)* — narrate the real-time safety constraint and what you would measure. Spring Boot is not on the page *(out of rails: not in the pool; MatchStream/Java is commented out — do not invent)* — talk FastAPI/Flask services instead. B.S. May 2028 is correct; do not claim a Master's. Do not claim Snowflake, Databricks, Copilot, Fusion, or Tableau.
- **Depth prep:** REST + cloud deploy (EC2, Docker, GHA); workers/queues (Celery/Redis); hardware-software / on-device vs cloud split (VAD before upload); intern-easy DS&A if a coding round appears (`companies.md`: no standard OA published, 2–3 rds Easy)

## Likelihood

- **Resume screen:** Medium — Flask/AWS, S3 recovery, Docker/Celery 30x, and on-device VAD are a credible cloud-services page; the remaining ding is an unsized C++ plugin. The Master's/PhD essential filter still fires before most humans finish the PDF.
- **Overall hire odds:** Low — B-tier Greenhouse, no OA, ~10–15% on paper, and the degree-level knockout is the binding gate. A clean intern PDF does not convert an undergrad into a Master's/PhD req.
- **Funnel filters:** Greenhouse 6111955004 · no standard OA · 2–3 rds Easy · bottleneck: resume + degree-level knockout · ~10–15% (`reference/companies.md` B-tier HP IQ). Form also asks whether the candidate graduates before September 2027.
- **Outside the resume:** Confirm whether they will waive Master's; a referral into Cloud Services is the only realistic bypass (`recruiting.md` §4). Do not apply as if this were HP/HPE campus SWE or the AML Platform sibling.
