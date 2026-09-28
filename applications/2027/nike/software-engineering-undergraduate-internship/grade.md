# NIKE, Inc. Software Engineering Undergraduate Internship at Nike

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 = Spring 2028; JD window is December 2027 through Spring 2028
- **Track:** full-stack
- **Pipeline:** 4 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with a production Flask REST API on AWS EC2 wired into a public-facing research workflow; the ETL line sizes the work (~800 hours / 400 PACs). Binding ding: the title still reads Data Engineer, so a skim can slot the lead as civic analytics rather than product/backend SWE.
- CaseStudyPrep carries consumer-facing frontend performance (Web Worker, sub-5ms main-thread, 60 FPS) and Angular/RxJS S3 reliability (27% upload-failure cut).
- SignalWeaver closes the full-stack archetype: React/TypeScript dashboard, FastAPI REST (9.1s p50 / 15.2s p99), Docker Compose + GitHub Actions CI with pytest.

### Demerits

- **minor** · `Michigan Data Consulting (MDC)` · Data Engineer title as first-pass identity — Experience opens as Data Engineer at Michigan Campaign Finance Network; this req is SWE for consumer digital. Bullet 1 is a production Flask REST API on AWS, but a title-skimming pass can mis-slot the lead as analytics rather than product/backend SWE. *(out of rails: canonical header cannot be rewritten)*
- **minor** · `Michigan Data Consulting (MDC)` · metric-free aggregation bullet — The third bullet architects a deterministic aggregation/ranking engine with only a qualitative outcome (researchers stop rebuilding spreadsheets) and no number, so a recruiter cannot size that layer next to the ETL's ~800 hours / 400 PACs. *(out of rails: pool has no aggregation metric; inventing QPS/latency is forbidden)*

### Misreads

- Title-skimming pass buckets MDC as a data-analyst / civic-ETL intern instead of the public Flask/EC2 API the first bullet actually describes.
- A Nike mobile team looking for Java/Swift/Node may treat TypeScript + Python as a miss even though the JD is "at least one" language.

### Interview angles

- **Lead with:** MDC sole-engineer Flask REST on AWS EC2 + public research workflow; CaseStudyPrep Web Worker / 60 FPS and RxJS S3 recovery; SignalWeaver React/TypeScript dashboard + FastAPI + Docker/CI; Vylet named debug fix (79%→89%)
- **Defend:** Title is Data Engineer because that was the contract role — the shipped artifact is a Flask API on EC2, not a notebook. No Java, C#, Swift, Node.js, Xcode, or Android Studio on the page — inventory is Python/TypeScript; narrate ramp willingness if the intern seat lands on those stacks. TypeScript is JS-family proof, not a relabel of JavaScript in Skills. Flask API line has no QPS/latency — walk the 5-month sole-engineer contract and what you would measure. Aggregation engine has no count — walk normalize/rank logic, not a fake number. LoRA/agentic work is not the lead story.
- **Depth prep:** Easy HackerRank/Codility DS&A (`companies.md` bottleneck is resume + HireVue); Flask/REST + EC2 deploy; React/TypeScript dashboard; Angular/RxJS fault-tolerance; GitHub Actions/pytest. HireVue games + on-demand video and Nike-values behavioral (`recruiting.md` §6 is a filter round) plus manager resume deep-dive.

## Likelihood

- **Resume screen:** High — Eligible May 2028, Python/React/AWS/REST/Postgres/Docker/CI through use, quantified product work, no fabricated JD languages; Workday should not bounce this PDF.
- **Overall hire odds:** Medium — Nike is B-tier (~5–10% directional) with bottleneck resume + HireVue, then an Easy–Med HackerRank/Codility if issued; a strong intern page clears the first gate but HireVue games/video and the coding screen are still real elimination stages, and behavioral is a filter mapped to Nike values.
- **Funnel filters:** Workday resume → HireVue games + on-demand video **[directional]** → HackerRank/Codility LC-easy for tech **[directional]** → manager interviews (resume + Nike values) · Easy–Med · Bottleneck: resume + HireVue · ~5–10% **[directional]** · grad window Dec 2027–Spring 2028 · in-person Beaverton
- **Outside the resume:** Apply in this first-week window (posted ~2026-08-31); timed easy OA; short STAR set for HireVue (MDC stakeholder scoping, Vylet name-collision fix, CaseStudyPrep upload-failure); a WHQ/Global Technology referral beats cold Workday. No Nike contact in `network.md`.
