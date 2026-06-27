# Software Engineering Intern at CTGT

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** Eligible — Expected May 2028 maps to a current CS undergrad returning to school after Summer 2027
- **Track:** full-stack + AI workflow governance
- **Pipeline:** 4 graded cycle(s) — exit: writer_peak

## Screen Review

### First read

- Strong CTGT screen: Dadei leads with human approval chokepoint, auditable LLM side-effect boundary, React/FastAPI, and Redis Streams reliability — directly on the governance differentiator.
- Full-stack spine is credible: MindMosaic shipped Java/Spring/Neo4j with 48% latency win and AWS/Terraform; club platform shows GitHub Actions CI/CD and concurrency-safe backend RPCs.
- Lab adds adversarial AI safety depth (80% bypass against per-step triage gate) without burying the product story.

### Demerits

- **minor** · `fliks` · single bullet, no metric — Go media-pipeline ownership is relevant, but the entry is only one unquantified line, so the recruiter cannot size throughput, scale, or reliability impact.
- **minor** · `Dadei` · metric-free governance bullet — The approval chokepoint is the strongest CTGT signal, but it has no failure-rate, usage, or latency metric to size how often it prevented bad actions.

### Misreads

- A rushed reviewer may read `fliks` as thin Go keyword coverage rather than a real media pipeline because it is a single unquantified bullet.
- A reviewer may like Dadei's governance boundary but still ask whether the approval chokepoint protected real usage or is mostly architecture framing.

### Interview angles

- **Lead with:** Dadei's approval chokepoint and Redis Streams recovery path; MindMosaic's Neo4j migration and Terraform AWS bring-up; lab verifier design and 80% decomposition attack result.
- **Defend:** Dadei governance impact is not quantified because the pool has no failure-rate/user/incident metric for the approval chokepoint *(out of rails: no legal metric-bearing bullet for that claim)*; fliks scale is not quantified because the pool has no throughput/job-volume/latency metric *(out of rails: full fliks pool exhausted)*.
- **Depth prep:** Why one approval seam vs per-action checks; FastAPI + Redis Streams consumer groups and dead-letter routing; Neo4j vs recursive SQL tradeoffs; per-step triage gate attack model; practical Python/JS system design and timed DS&A medium practice.

## Likelihood

- **Resume screen:** High — on-axis for CTGT's full-stack intern screen with AI governance at the top, Python/JS/cloud evidence in shipped work, and metrics on the load-bearing entries.
- **Overall hire odds:** Medium — early-stage startup funnel favors a human PDF read and referral signal; the resume should earn a careful look, but practical technical depth and small intern cohort size still decide conversion.
- **Funnel filters:** Resume-first startup screen; practical full-stack/backend discussion likely; DS&A may appear if an OA is used; onsite SF Summer 2027; visa sponsorship noted on posting but not guaranteed per role.
- **Outside the resume:** Apply early, pursue warm intro or founder-adjacent referral, and prep narratable ownership stories on Dadei's approval boundary and MindMosaic's production delivery.
