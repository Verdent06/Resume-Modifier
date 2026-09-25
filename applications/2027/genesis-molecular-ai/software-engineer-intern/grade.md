# Software Engineer Intern - 2027 at Genesis Molecular AI

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — JD prints no class-year or grad-window gate; Expected May 2028 is a current bachelor's student for a 2027 intern term; US citizen
- **Track:** full-stack + molecular-AI/ml-infra
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Vylet leads with a Dockerized LangGraph product, Redis/Celery workers, a LangSmith eval harness (50%→90% faithfulness), and a named production defect (79%→89%) — shipped software plus model-analysis/eval, not a notebook.
- CaseStudyPrep puts inference-in-production and visualization on the page: Silero VAD via ONNX (40% cloud-cost cut) and a 60 FPS real-time visualizer off the UI thread.
- SignalWeaver plus MDC close the loop: LoRA 81%→96% held-out, FastAPI serving, pgvector at 49ms p50, Docker/GitHub Actions CI, and a Flask REST API on EC2 with a Requests + Pandas ETL. Binding ding: none at screen.

### Demerits

No demerits — clean screen.

### Misreads

- None material on the page — it reads as Python SWE with production pipelines, eval/serving, and a viz analog, not the sibling ML Research Intern and not a computational chemist. A screener who treats biochemistry coursework or RDKit as a must-have (JD does not) could still wait for the unpublished tech loop.

### Interview angles

- **Lead with:** Vylet Docker/Redis/Celery + LangSmith eval + name-collision fix (code quality); CaseStudyPrep ONNX inference cost and 60 FPS visualizer (JD viz + productionize); SignalWeaver LoRA held-out + FastAPI/pgvector + CI (analyze models, serve, infra)
- **Defend:** No RDKit, CUDA, PyTorch-as-named, OpenMM, or biochemistry coursework — do not claim them. Interested in *learning* drug development, not a fake chem degree. SignalWeaver is finance research, not molecules. Vylet's PE/search-fund domain is the product, not GTM filler. Voice-AI co-op is inference + viz, not an audio-DSP identity. San Mateo is a term relocate, not a spoofed home address
- **Depth prep:** Walk the eval harness (20 adversarial cases, Pydantic consensus, 50%→90%); LoRA held-out protocol; ONNX-in-client cost; Redis/Celery as a job-fan-out analog (do not invent MD engines); Flask vs FastAPI serving. Keep Medium Python DS&A warm for the unpublished loop. STAR on a named production defect and on shipping to a real stakeholder (MDC)

## Likelihood

- **Resume screen:** High — eligible May 2028 CS/Econ 3.66; Python through use; production Flask REST on EC2; Docker/Redis/Celery product with eval and a named bug fix; LoRA + FastAPI + pgvector + CI
- **Overall hire odds:** Medium — B-tier scale-up, bottleneck is the resume then unpublished tech (~3–8% directional, Cohere/Mistral intern peer). Cold Ashby; no named OA; biochemistry is curiosity, not a knockout
- **Funnel filters:** Ashby resume → unpublished intern loop · Medium Python DS&A · no named intern OA · light intern sys design unpublished · US work auth / no sponsorship · location pick (San Mateo primary)
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-24). Form email **verdent06@gmail.com**. Location **San Mateo, CA**. Start **2027-06-01**. No Genesis contact in `network.md` — do not invent a referral. Do **not** attach this PDF to ML Research Intern – BS/MS or PhD. Packet only from this agent — see `written-answers.md`
