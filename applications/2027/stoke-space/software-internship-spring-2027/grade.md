# Spring 2027 Internship - Software at Stoke Space

## Verdict

- **Score:** 2.0 / 10 (8 demerits — 0 emergency, 2 major, 2 minor)
- **Eligibility:** Eligible — Expected May 2028 maps to junior class standing for Spring 2027 (Jan–April) with return-to-school afterward
- **Track:** full-stack + aerospace / real-time mission-critical systems
- **Pipeline:** 4 graded cycle(s) · exit: writer_peak

## Screen Review

### First read

- Strong Stoke screen for a rocket company: C++ real-hardware control loop (30 Hz, sub-20ms) and 80% adversarial attack metric sit in the top half alongside shipped production systems (MindMosaic MVP, Neo4j latency win, Terraform/AWS).
- Full-stack spine is credible across Java/Spring, Python/FastAPI, React, PostgreSQL, Go, and deployment — but the page reads Spring/Python/Go backend more than Boltline's named JS/TS SaaS stack.
- Binding dings: no explicit testing/validation/CI signal on the page (major), and JS/TS full-stack proof is thinner than the skills line claims (major); MindMosaic "real users" and fliks architecture choices lack scale metrics (minors).

### Demerits

- **major** · `Technical Skills / resume` · JavaScript/TypeScript full-stack signal is under-evidenced — Boltline is JS/TS-heavy, but bullets show React without TypeScript, Node, Next.js, GraphQL, or JS/TS API depth; backends read Java/Python/Go.
- **major** · `resume` · testing and validation discipline is absent — deployment, latency, and failure recovery are present, but no automated testing, CI/CD, validation harness, or test-stand verification signal for a mission-critical aerospace bar.
- **minor** · `MindMosaic` · production MVP impact is undersized — "shipped to real users" has no user count, adoption, or reliability witness beyond the later 48% latency win.
- **minor** · `fliks` · architecture decisions lack outcome metrics — Go monolith and Postgres queue trade-offs are defensible but unquantified (no throughput, latency, or user scale).

### Misreads

- A rushed reviewer may bucket this as a robotics specialist because the SEAS lab leads the differentiator signal, missing the full-stack production spine underneath.
- A Boltline-routed reviewer may see React + a JS/TS skills line and assume Node/GraphQL depth that the bullets do not actually demonstrate.
- The absence of a testing/CI bullet may read as "never tested anything" rather than "testing happened but isn't narrated on this one-page cut."

### Interview angles

- **Lead with:** the 30 Hz C++ WiFi driver on a physical RoboMaster in Gazebo + hardware; MindMosaic's Neo4j migration (48%/3x) and Terraform single-command deploy; Dadei's Redis exit-zero root-cause and three-layer restart.
- **Defend:** Boltline JS/TS backend gap — backends in the pool are Python/Java/Go, not Node/Express/GraphQL *(out of rails: no JS/TS backend bullet in pool)*; testing/CI not on page — CBC GitHub Actions bullet was cut for one-page fit, can narrate deploy discipline verbally; MindMosaic user scale and fliks throughput — pool has no adoption/load metrics *(out of rails)*; Dadei approval chokepoint has no failure-rate metric *(out of rails: no metric variant for bullet #1)*.
- **Depth prep:** C++ control-loop design and Gazebo-to-hardware validation; why nav2 MPPI was integrated; Neo4j vs recursive SQL tradeoffs; Postgres RLS + atomic RPC concurrency model; Redis/Docker failure recovery; timed practical coding for startup technical screen.

## Likelihood

- **Resume screen:** High — shipped systems, real-hardware control-loop evidence, and full-stack breadth are unusually on-axis for a reusable-rocket company despite the Boltline stack and testing gaps.
- **Overall hire odds:** Medium — small competitive aerospace cohort with human Greenhouse review; resume should earn a serious read if ITAR/onsite/Spring availability clear, but conversion hinges on practical coding, project deep-dives, and team routing (Boltline vs Vehicle Software vs Data).
- **Funnel filters:** Greenhouse knockouts (work auth, sponsorship, grad date, Spring Jan–April 2027 availability, GPA); ITAR U.S. person requirement; ~750-word essay and team-preference question; no published OA platform — likely practical coding + project depth.
- **Outside the resume:** apply during the May–July Spring window; warm referral or recruiter touchpoint; prep DS&A plus crisp walk-throughs of the control-loop, MindMosaic deploy, and Dadei recovery stories; confirm ITAR eligibility before investing essay time.
