# 2027 Software Engineer Intern at Anduril Industries

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028; Summer 2027 is after junior year → rising senior per JD
- **Track:** full-stack + autonomy (track_divergence)
- **Pipeline:** 1 cycle · exit: writer_peak

## Screen Review

### First read

- C++ ROS2 verifier, Gazebo/sim-to-hardware, FRC world-stage vision stack, and Go/Python depth read on-axis for Anduril — autonomy signal sits in the top half where this screen expects it.
- Polyglot delivery and operational discipline (dead-letter routing, CI gates, Terraform/AWS) match a generic SWE req beyond pure robotics.
- The binding ding is full-stack breadth: nothing on the page names React, Angular, or Vue, so a rushed pass may bucket you backend/autonomy-only.

### Demerits

- **major** · `resume` · front-end frameworks absent — JD lists front-end frameworks as required familiarity; no React, Angular, or Vue appears in bullets or skills — reads backend/autonomy-only for a generic SWE req
- **minor** · `fliks` · metric-free — Go monolith and transcoding pipeline are the right signals but both lines read unquantified — thinner than the work likely was
- **minor** · `Dadei` · partial metric coverage — one-second scheduling bullet adds a number but the lead Redis Streams bullet remains unquantified — mixed density in the flagship project

### Misreads

- **Front-end gap:** A 30-second scan may bucket you as backend/autonomy-only; lead with C++/ROS if targeting Lattice/autonomy, not a web tooling team.
- **Research lab:** The reproduced attack baseline reads stronger than "researching," but still pre-publication — be ready to explain current outputs.
- **MindMosaic:** Neo4j latency swap may read as data-engineering, not defense — connect graph/query routing to "storage systems" JD language.

### Interview angles

- **Lead with:** C++ in production (verifier node, FRC stack); autonomy end-to-end (Gazebo → RoboMaster, AprilTag + odometry, security framing on motion plans); polyglot shipped systems (Go/fliks, Python/Dadei, Java/MindMosaic, Terraform/AWS).
- **Defend:** No front-end framework on the page — anchor on JavaScript/TypeScript in inventory and be honest about depth; do not claim React experience you cannot defend *(out of rails: no pool bullet names React, Angular, or Vue)*. fliks and Dadei's lead bullet lack metrics — prepare verbal scale (upload volume, latency targets, user count) *(out of rails: bullet pool has no impact-metric lines for fliks)*.
- **Depth prep:** Mission-oriented ownership language — triage, root cause, metrics — on Dadei/MindMosaic stories; C++ and practical systems problems for HackerRank and the ~4 hr onsite.

## Likelihood

- **Resume screen:** Medium–High — on-axis autonomy and systems depth; generic JD front-end gap is the main screen ding.
- **Overall hire odds:** Medium — ~3–5% funnel (`companies.md`); HackerRank OA then 4-hr practical onsite is the bottleneck. Profile is differentiated on autonomy vs typical web-intern pool, but Rust (JD-listed, not in inventory) and front-end proof are headwinds.
- **Funnel filters:** HackerRank OA (medium) → practical onsite (~4 hr) · U.S. Person required · Review begins August 2026
- **Outside the resume:** Apply early (JD encourages it); confirm U.S. Person and rising-senior standing in application; referral if any Anduril/defense contact exists; prep C++ and practical systems problems for HackerRank/onsite.