# 2027 Software Engineer Intern at Anduril Industries

## Verdict

- **Score:** 8.0 / 10 (2 demerits - 0 emergency, 0 major, 2 minor)
- **Eligibility:** Eligible - Expected May 2028 maps to rising senior for Summer 2027 and returning to school afterward
- **Track:** full-stack + autonomy / mission-critical defense software
- **Pipeline:** 5 graded cycle(s) + fit pass - exit: writer_peak

## Screen Review

### First read

- Strong Anduril screen: C++/ROS2 autonomy work leads, with hardware, Gazebo, and mission-adjacent security evidence visible immediately.
- Broad SWE spine is credible: Java/Spring/Neo4j/PostgreSQL, Python/React reliability work, Go media pipeline, AWS/Terraform/GitHub Actions.
- Binding dings are small: fliks is now a one-bullet fit sacrifice with no scale metric, and Dadei's approval-boundary bullet is conceptually strong but not quantified.

### Demerits

- **minor** · `fliks` · single bullet, no metric - Go and media-pipeline ownership are relevant, but the entry is only one unquantified line, so the recruiter cannot size throughput, scale, or reliability impact.
- **minor** · `Dadei` · one bullet reads abstract - The approval chokepoint is relevant to safety boundaries, but "one auditable seam" does not show the concrete mechanism, failure mode, or measured impact as clearly as the surrounding technical bullets.

### Misreads

- A rushed reviewer may read `fliks` as thin Go keyword coverage rather than a real media pipeline because the fit pass left it at one unquantified bullet.
- A reviewer may like Dadei's safety boundary but still ask whether the approval chokepoint protected real usage or is mostly architecture framing.

### Interview angles

- **Lead with:** the ROS2 verifier and real-robot deployment in the lab entry; MindMosaic's Java/Neo4j latency win; Dadei's worker-queue root-cause and restart path.
- **Defend:** Dadei safety boundary is not quantified because the pool has no failure-rate/user/incident metric for the approval chokepoint *(out of rails: no legal metric-bearing bullet for that claim)*; fliks scale is not quantified because the pool has no throughput/job-volume/latency/cost metric *(out of rails: full fliks pool exhausted)*.
- **Depth prep:** C++ ROS2 node design, Gazebo-to-hardware validation, why nav2 MPPI was integrated, Neo4j vs recursive SQL tradeoffs, Redis/Docker failure recovery, and timed HackerRank/LeetCode medium practice.

## Likelihood

- **Resume screen:** High - on-axis for Anduril's SWE intern screen, with autonomy at the top and broad SWE evidence across C++, Java, Python, Go, cloud, databases, deployment, and debugging.
- **Overall hire odds:** Medium - the resume should earn a serious look, but Anduril remains an A-tier defense-tech funnel where timing, referral, OA performance, and practical debugging depth decide conversion.
- **Funnel filters:** Greenhouse screen; likely HackerRank medium; practical technical/system discussion; bottleneck is the 4-hour onsite; U.S. Person and rising-senior/return-to-school gates.
- **Outside the resume:** apply early, use a warm referral or recruiter touchpoint, and prep DS&A plus concise system walk-throughs for the ROS2 verifier, MindMosaic deployment, and Dadei recovery path.
