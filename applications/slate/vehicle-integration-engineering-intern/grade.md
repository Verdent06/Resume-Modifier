# Resume Grading Report — Intern, Vehicle Integration Engineering @ Slate

## Reviewer Persona

I'm on the Vehicle Integration side at Slate. We need someone who can install CAN instrumentation on prototype vehicles, work with cloud data to find root cause, and build dashboards and reporting tools that Chassis, Electrical, and Powertrain actually use. A strong intern has Python, data pipelines, metrics/dashboards, and cross-functional collaboration; bonus for anything instrumentation- or telemetry-adjacent. We're a startup—scrappy, hands-on, lab/plant capable. I read hooks first; if the first bullet doesn't signal data + systems + teamwork, I move on.

---

## Dimension Scores

| Dimension            | Grade | Notes |
|----------------------|-------|--------|
| Hook Quality         | B     | Hooks are clear and outcome-focused; MindMosaic and Mira lead with data/pipeline angle. |
| ATS Coverage         | C     | ~12/22 keywords in bullets (usage metrics, analytics, instrumentation, data collection, testing and validation, cross-functional, data analysis, requirements validation, cloud, Python, KPIs). Missing in bullets: vehicle integration, CAN, analytics dashboards, fleet performance, Grafana, telematics, Excel. |
| Metric Density       | A     | Strong before/after and scale (97%, 80%, 48%, 73%, 86%, 60 FPS). |
| Tech Justification   | B     | Redis/Celery, Neo4j, Lambda, MediaPipe have clear reasons; Tools line is keyword-heavy. |
| Role Relevance       | B     | Data pipeline, cross-functional, instrumentation, metrics, and validation are surfaced; no automotive domain. |
| Narrative Coherence  | B     | Data pipelines and automation thread; vehicle-integration angle implied, not explicit. |
| Skills Line Fit      | B     | Verify in PDF: "Tools & Data" line (Grafana, Excel, Microsoft Office, data analysis, telematics) may wrap; shorten if needed. |
| Page Fit             | A     | Fits one page; balanced density. |

**Overall grade: B**

---

## Entry Breakdown

**Claude Builder Club @ MSU**  
Hook: A — Clear problem (manual onboarding), solution, impact (97%, 30 sec, 100+).  
Keep: Yes.  
Strongest: QR-driven check-in with event instrumentation, data collection, usage metrics for analytics, 80% processing cut.  
Role fit: Automation, real-time metrics, instrumentation, and analytics align with role.

**MindMosaic**  
Hook: B — Cross-functional + data analysis + latency; good signal.  
Keep: Yes.  
Strongest: Led cross-functional team; Neo4j for multi-hop data analysis and analytics; 48% p95 cut.  
Role fit: Cross-functional, data analysis, requirements validation.

**Mira**  
Hook: B — Data pipeline + voice assistant; pipeline first.  
Keep: Yes.  
Strongest: RAG pipeline for semantic data analysis, Python FastAPI on AWS Lambda (cloud), cold-start 86% cut; key metrics and KPIs.  
Role fit: Data pipeline, Python, cloud, data analysis, KPIs.

**WizViz**  
Hook: B — Award + real-time pipeline.  
Keep: Yes but deprioritize.  
Strongest: Python MediaPipe pipeline, 33 landmarks, 60 FPS.  
Role fit: Python, real-time sensor-like input.

---

## What Would Make Me Pass Immediately

1. At least one bullet explicitly mentioning dashboards, reporting, or KPIs (partially addressed with KPIs and usage metrics).
2. More ATS keywords in bullets: analytics dashboards, instrumentation (addressed), Grafana/Excel in a bullet if defensible.
3. Stronger vehicle-integration framing without inventing domain experience (data collection, instrumentation, validation are present).

---

## Changes Made This Pass

- Injected ATS: usage metrics, analytics, instrumentation, data collection, testing and validation, cross-functional, data analysis, requirements validation, cloud, Python, KPIs.
- Reframed Mira as data pipeline first; added key metrics and KPIs.
- Skills: Grafana, Excel, Microsoft Office, data analysis, telematics.
- Preserved one page by tightening wording and removing one MindMosaic bullet (OAuth).

---

## Likelihood Estimate

**Resume screen pass:** Medium  
Rationale: Data pipeline, Python, cross-functional, instrumentation, and metrics are present. No automotive or CAN experience; role is willing to train (eagerness to learn Python/Grafana). CS degree and graduation window fit.

**Overall hire odds:** Medium  
Rationale: Startup bar and team fit matter. Candidate has no prior auto internship; project depth and leadership (VP, Technical Lead) help. Referral or Slate-specific interest would move the needle.

**Ceiling without changes:** Strong screen pass if ATS and hooks stay; interview depends on how well they speak to data pipelines and “instrumentation” in person.

**What would move the needle:** Referral, brief note in application tying data pipeline / metrics work to vehicle data and dashboards, or a small portfolio piece (e.g. Grafana or Python dashboard over real data).
