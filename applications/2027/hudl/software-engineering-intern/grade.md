# Software Engineering Intern at Hudl

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028; Summer 2027 intern is rising junior / after sophomore year; JD requires currently enrolled CS/SWE/CE
- **Track:** full-stack
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: a production Flask REST API on AWS EC2 shipped into a nonprofit's public-facing workflow, then quantified ETL (~800 hours / 400 PACs) and sole-engineer stakeholder scoping — the JD's "ship real code to production" bar.
- Vylet is a live LangGraph/Docker product with a named 79%→89% defect and paying clients; SignalWeaver carries React/TypeScript, FastAPI REST, pgvector, and GitHub Actions CI. GPA 3.66 and a live GitHub clear a resume-first C-tier intern screen.
- Binding dings: nothing on the page is sports-video / coaching-product, and the React/CI exhibit is a 90-ticker research harness rather than production users.

### Demerits

- **minor** · `resume` · company-fit differentiator absent — Hudl's identity is sports-video / coaching-product SaaS for coaches, athletes, and fans. The page is campaign-finance ETL, PE/search-fund lead-gen, voice-AI uploads, and a financial-research dashboard. Closest analog is stakeholder-scoped Flask plus a React dashboard; no sports, coaching, video, or athlete-facing product signal.
- **minor** · `SignalWeaver` · research-harness framing, not production users — Leading with Docker Compose and GitHub Actions does not change the exhibit: the React/TypeScript dashboard still analyzes 90 self-run tickers with batch p50/p99. Hudl's intern bar is code that coaches/athletes/fans use; this still reads as a personal research harness.

### Misreads

- A Lincoln screener skimming titles (Data Engineer, Founder, Voice AI, financial-research dashboard) could bucket this as analytics / PE-tools / ML rather than a product SWE intern who ships web apps and sits in code review.
- SignalWeaver's "not investment advice" tagline plus ticker metrics can be bucketed as a class project rather than the only end-to-end React + API + DB + CI build.

### Interview angles

- **Lead with:** MDC Flask REST on AWS EC2 as the analog to shipping features used by non-engineers; then Vylet LangGraph/Docker ownership and the 79%→89% defect; then SignalWeaver React/TypeScript + GitHub Actions CI; then CaseStudyPrep 27% S3 upload-failure debug.
- **Defend:** No Hudl / Wyscout / sports-video / coaching-analytics work exists in the pool — say so, then map stakeholder-scoped Flask delivery onto a product team and GitHub Actions onto the JD's CI/CD practice. Do not invent C#, .NET, Java, Node.js, or microservices. SignalWeaver has no external users — point to MDC's nonprofit workflow and Vylet's three paying clients. *(out of rails: pool has no sports/coaching/video bullet; every SignalWeaver pool bullet is the 90-ticker research harness; iter-1 forbids dropping the React/CI exhibit)*
- **Depth prep:** Walk the Flask contract (ingest → rank → REST on EC2); LangGraph/Redis/Celery pipeline and the name-collision fix; GitHub Actions stages (frontend build, pytest, API image); React dashboard trade-offs. Easy–Med DS&A for the Oct 6–28 coding assessment (platform unpublished — do not assume HackerRank). STAR for code review, a named production defect, and shipping to a non-engineer stakeholder. Lincoln onsite May 17–early August is a work-model gate, not a resume line.

## Likelihood

- **Resume screen:** High — production Flask/AWS, React/TS through use, GitHub Actions CI, LangGraph product ownership, GPA 3.66, and live GitHub clear a resume-first C-tier intern screen; C# is nice-to-have only.
- **Overall hire odds:** Medium — C-tier ~15–25% with resume then unpublished Easy–Med coding assessment (`companies.md`; `recruiting.md` mid-size Greenhouse). The PDF should clear; Lincoln onsite from Michigan and the coding assessment still filter. Behavioral is a filter round, not a differentiator.
- **Funnel filters:** Greenhouse **8114314** resume (batch review Oct 1) → first-round interviews Oct 5–23 → coding assessment Oct 6–28 (platform unpublished) → finals Oct 12–Nov 6 → offers Nov 20. Easy–Med · no intern sys design · bottleneck: resume (then coding assessment) · ~15–25% **[directional]**. Current-student CS; housing + travel covered.
- **Outside the resume:** Apply before the Oct 1 close (opened Sep 10 — first wave). Say yes to Lincoln May 17–early August. No Hudl contact in `network.md`. Prep Easy–Med DS&A and STAR; form email **verdent06@gmail.com**.
