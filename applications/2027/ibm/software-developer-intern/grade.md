# Software Developer Intern 2027 at IBM

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028; Summer 2027 leaves Fall 2027 + Winter 2028 after the internship. JD education floor is high school diploma / bachelor's preferred; no class-year knockout on jobId 128497.
- **Track:** full-stack
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- On-axis general SWE intern page: Python/TypeScript in use, Flask REST on AWS EC2, React + FastAPI REST (9.1s p50), Docker, Git, debug metrics (27% upload-failure, 79%→89% qualification).
- Vylet (live product, Docker/Redis) then MDC (ETL + Flask/AWS) then a titled Angular co-op — not a notebook-ML or CAD resume.
- Binding dings are both minor: the Flask API closer has no service-size number, and Granular is one C++ DSP line that does not sell IBM Software.

### Demerits

- **minor** · `MDC` · metric-free API hook — Flask REST on AWS EC2 closes on unquantified "wiring into workflow"; ~800 hours / 400 PACs sit on the Pandas ETL
- **minor** · `Granular Synthesizer Plugin` · single-bullet DSP, no product impact — ring-buffer delay (2^17 samples) with no users/latency; reads as extra audio systems, not intern-product evidence

### Misreads

- A skim that stops on Granular's DSP tagline can bucket this as a hobby-audio resume and miss the Flask/React/Docker spine that actually matches the req.
- MDC's API line without a number can read as "data intern who also stood up Flask" rather than backend/cloud delivery.

### Interview angles

- **Lead with:** MDC sole-engineer Flask REST API on AWS EC2 + Requests/Pandas ETL; SignalWeaver FastAPI REST (9.1s p50 / 15.2s p99) + React dashboard; Vylet Dockerized pipeline with a diagnosed 79%→89% defect; CaseStudyPrep Angular/RxJS debug (27% upload-failure recovery)
- **Defend:** Flask API has no QPS/latency on the page *(out of rails: MDC pool 1–4 has no service-size metric; swap sets cannot invent one)* — narrate the 5-month sole-engineer contract and what you would measure. Granular is C++ proof, not the job *(out of rails: pool has no users/latency/shipping metric)* — one sentence on real-time constraints, then pivot to web/API/cloud. Do not claim Java, Kubernetes, IBM Cloud, Node.js production, or ML research.
- **Depth prep:** easy HackerRank DS&A (IBM bottleneck is resume, then OA); REST + Docker + Git stories; one IBMer-values STAR (MDC stakeholder scoping or Vylet name-collision fix). Behavioral is a filter round (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — one page, class year in window, shipped Python/TS, Flask REST on AWS, React, Docker, Git; Avature + human pass should not bounce this at a resume-bottleneck intern screen
- **Overall hire odds:** Medium — B-tier high-volume intern class, ~10–15%, bottleneck resume; page likely clears it, then easy HackerRank + 2–3 easy loops. Survivable, not a lock
- **Funnel filters:** Avature resume screen → HackerRank (easy) → 2–3 rounds; no intern systems-design; hybrid with location flexibility (Lowell MA, Durham NC, Bellevue WA, San Jose CA, Austin TX); ~15-day posting window
- **Outside the resume:** Apply in the first wave; IBM Software / Red Hat referral (`recruiting.md` §4 — none in `network.md`); timed easy HackerRank; short IBMer-values story set
