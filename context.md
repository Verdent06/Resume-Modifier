# Candidate Context

Canonical state for Ankur Desai's resume system. Headers, bullet pools, swap sets, and skills inventory. The writer agent reads this file; the grader does not.

**Profile (the 7-second impression):** A CS systems engineer who owns the layer between intelligence (LLMs, models, agents) and reliable real-world action: real-time delivery, async orchestration, the human-approval/safety boundary, and the deployment discipline to ship it. Not a frontend dev, not a notebook-ML person, not a controls/SLAM specialist.

Each entry carries a fixed **Lane**: the one distinct signal it contributes that no other entry can. Per-track scaling is volume control on lanes the target role rewards, not reassignment.

---

## Identity

- **Name:** Ankur Desai
- **Phone:** (248) 657-3805
- **Email:** [ardusa05@gmail.com](mailto:ardusa05@gmail.com)
- **Portfolio:** [https://ardusa.dev/](https://ardusa.dev/)
- **LinkedIn:** [https://linkedin.com/in/ardusa/](https://linkedin.com/in/ardusa/)
- **GitHub:** [https://github.com/ardusa](https://github.com/ardusa)

---

## Education

```
Michigan State University                          Expected May 2028
B.S. in Computer Science                           East Lansing, MI
GPA: 3.5 / 4.0
Coursework: Data Structures & Algorithms, Object Oriented Programming, Computer Architecture, Linear Algebra, Discrete Math
```

---

## Swap Sets

Flat dictionary. Unconditional within each set. Single-token swaps.

```yaml
relational-databases: [PostgreSQL, MySQL]
ci-cd-platforms: [GitHub Actions, GitLab CI/CD]
```

---

## Skills Inventory (Buckets)

Master pools. The writer picks 3-5 buckets per resume and trims each to ~80 characters after the label for the rendered line. Items below exceed that on purpose so there is room to select per role.

### Bucket: Languages

```
Python, Java, Go, JavaScript/TypeScript, C++, SQL, Cypher, Bash
```

### Bucket: Frameworks

```
FastAPI, Spring Boot, Node.js, React, Next.js, Angular, Vue, Electron
```

### Bucket: Databases

```
PostgreSQL, Neo4j, Redis, pgvector
```

### Bucket: AI / ML

```
PyTorch, Hugging Face, pyannote-audio, Whisper, Deepgram, Gemini, MediaPipe, OpenCV, RAG
```

### Bucket: Cloud & Infrastructure

```
AWS (EC2, S3, RDS), Docker, Terraform, GitHub Actions, CI/CD, Railway, Vercel, Supabase
```

### Bucket: Robotics

```
ROS2, Gazebo, WPILib, PathPlanner, AprilTag, RViz
```

### Bucket: Tools

```
Git, Linux, Postman, Figma, ROSBag
```

---

## Canonical Entries

Each entry has a fixed header, a Lane, and a bullet pool. Bullets are copied verbatim into the resume; swap-set substitutions are the only modification permitted. Experience entries carry dates; project entries carry a live link instead of a date so they can be ordered by relevance, not recency. Each project also carries a one-line descriptor that renders below the name (the rSectionEntry tagline slot, param #3), giving the at-a-glance "what it is." Because the descriptor carries identity, a project's lead bullet leads with its strongest engineering decision, never a re-description of the project. Experiences have no descriptor slot (the tagline holds the role), so an experience's first bullet still establishes what was built.

---

### Experience: Bopardikar Lab

**Lane:** Research ceiling and the LLM-to-action safety boundary. The only entry that says "works on novel, safety-critical AI-robotics problems," anchoring the autonomy track's intellectual ceiling. Now also carries the portfolio's only defensible C++ surface (the verifier node) and a real-robot, sim-to-hardware validation signal on a physical RoboMaster EP Core.

**Header:**

```
Secure and Efficient Autonomous Systems Lab       May 2026 -- Present
Undergraduate Research Assistant                  East Lansing, MI
```

**Bullet pool:**

```
1. Researching the security of an LLM-controlled robot, where the cheap per-step gate screening its motion plans is the exact seam an attacker slips a harmful plan through.
2. Reframed the contribution from building a defense to measuring one, arguing that a triage gate's cost savings and its attackability reduce to a single property: per-step versus whole-plan checking.
3. Ran the node graph byte-identical in Gazebo and on a physical RoboMaster EP Core, driving the real robot over a custom C++ WiFi driver at a 30 Hz control loop with sub-20ms command latency.
4. Built the verifier as a C++ ROS2 node running per-step geometric and semantic checks on each motion plan, the gate the decomposition attack is built to defeat.
5. Integrated nav2's production MPPI controller rather than hand-rolling a planner, keeping the C++ work on the security apparatus instead of motion control.
6. Reproduced a published adversarial-robotics attack loop (attacker, target, judge, syntax-checker) as the baseline, then drove the decomposition attack to an 80% success rate against the per-step triage gate.
7. Built the attacked defense as a steelman from published safety architectures, so the decomposition attack lands on the strongest reasonable system, not a strawman.
```

---

### Experience: Claude Builder Club @ MSU

**Lane:** Founder leadership plus operational infrastructure. Carries two signals no project does: founding-and-growth leadership (0 to 150+) and multi-service provisioning/CI-CD ops at community scale. Compresses hard on the autonomy track. Also owns a custom-graphics frontend lane: a hand-built react-three-fiber 3D lineage graph plus React Query client-data architecture.

**Header:**

```
Claude Builder Club @ MSU                         Oct 2025 -- Present
Co-Founder & Vice President                       East Lansing, MI
```

**Bullet pool:**

```
1. Co-founded and grew an MSU engineering community from zero to 150+ members, replacing a sprawl of spreadsheets, Slack threads, and manual invites with a single club-operations platform I built to run member lifecycle, events, and project provisioning.
2. Automated member onboarding end to end so an accepted applicant is provisioned into the right GitHub teams, Slack channels, Discord roles, and Google Drive access in a single flow, cutting onboarding from 15 minutes of manual invites to seconds.
3. Built event check-in as a single atomic database RPC that validates a QR token, records attendance, and awards points server-side, making door-time check-ins concurrency-safe and idempotent so simultaneous scans cannot double-award or be forged client-side, sustaining 150+ check-ins per event.
4. Built the club's mentorship lineage as an interactive 3D radial graph in react-three-fiber, hand-writing a proportional-arc layout that prevents edge crossings and a custom camera that autofits each family to the viewport.
5. Pushed authorization into the database with row-level security so every table enforces access in Postgres regardless of what the client sends, letting new features ship without re-implementing per-endpoint auth.
6. Built a hands-off attendance-enforcement pipeline that runs a daily in-database cron job, resolves absentees, and posts targeted Slack reminders, automating a three-strikes rule that previously required manual tracking.
7. Shipped the platform continuously from main on a GitHub Actions pipeline that applies database migrations and deploys edge functions on every push, with the frontend auto-deploying on the same commit, taking the team from manual changes to reviewed continuous deploys.
8. Scoped live dashboard updates to per-user realtime subscriptions filtered at the row level, so a member sees their own role or acceptance change instantly without waking every other client.
9. Tuned React Query cache tiers by data volatility across the dashboards, caching stable roles longer than fast-changing application queues to cut redundant refetches while keeping live data fresh.
```

---

### Experience: MindMosaic

**Lane:** Titled product delivery anchored on the Neo4j graph backend, the dual-database architecture, and the AWS deployment script plus Terraform/IaC. Carries shipped-to-real-users institutional weight. Not OAuth, not Postgres-as-the-star.

**Header:**

```
MindMosaic                                    Aug 2025 -- May 2026
Software Engineering Intern                   East Lansing, MI
```

**Bullet pool:**

```
1. Built and shipped an interactive knowledge-graph platform that keeps dense, interconnected content navigable as it grows, delivering a production MVP to real users on a polyglot Spring Boot, Neo4j, and PostgreSQL stack.
2. Migrated hot read paths off recursive SQL self-joins onto a Neo4j graph layer so relationships stay first-class, cutting query latency 48% (850ms to 440ms) and making multi-hop traversals 3x faster than the equivalent SQL.
3. Designed a dual-database layer that keeps transactional records in PostgreSQL while serving relationship-heavy reads from Neo4j, routing each query class to the store that answers it fastest instead of forcing one engine to do both jobs.
4. Owned the Spring Boot backend serving the platform's core CRUD and graph-traversal APIs, structuring endpoints around the dual-store model so the client never has to know which database backs a given read.
5. Authored an AWS deployment script and managed the environment as code with Terraform, replacing a manual multi-service bring-up that took 30 minutes with a single-command, version-controlled provision so the polyglot stack deploys identically every time.
```

---

### Experience: Robostangs

**Lane:** Competition-robotics pedigree and the hardware-software boundary, plus software-captain leadership and a world-stage result. Holds the autonomy Experience slot until Bopardikar produces narratable output, then compresses to one line. Drops on the full-stack track.

**Header:**

```
Robostangs (FRC Team 548)                   Jun 2023 -- May 2024
Software Captain                            Northville, MI
```

**Bullet pool:**

```
1. Led the software and electrical teams (5 and 6 engineers) for a competition robot that reached the FIRST World Championship and placed top 16 in its division in Houston, the program's strongest world-stage finish since 2014.
2. Delivered the team's first multi-piece autonomous routine, chaining vision-corrected driving paths with timed intake-and-shoot actions so the robot scored multiple game pieces with no driver input during the autonomous period.
3. Anchored auto-aim on real-time, vision-corrected localization that fused two AprilTag cameras with swerve odometry on a dedicated 250Hz thread with latency compensation, holding pose accurate during aggressive motion.
4. Hardened pose estimation against bad vision data by gating camera measurements on tag count, target area, and angular velocity before fusing them, rejecting the garbage estimates that would otherwise poison the localization filter during fast rotation.
5. Engineered graceful sensor-failure handling so the most match-critical mechanism falls back to an internal encoder and stays operable through a sensor loss instead of bricking mid-match, surfacing the degradation as an alert rather than a silent failure.
6. Built shoot-from-anywhere aiming that maps target distance to arm angle through a regression model, keeping several candidate models swappable behind one interface so the team could A/B them against measured shot data without code churn.
```

---

### Project: Dadei

**Lane:** Flagship systems depth. The deepest engineering signal in the portfolio: real-time cross-process delivery, async orchestration, hybrid retrieval, agentic tool-calling, and the single human-approval action boundary that is the profile thesis made concrete. The React client (real-time streaming UI and the cancel-to-abort countdown) gives the entry its full-stack and frontend signal.

**Header:**

```
Dadei  |  {tech derived from selected bullets}    dadei.app
Ambient voice assistant that turns overheard conversation into human-approved calendar, email, and task actions
```

**Bullet pool:**

```
1. Routed all model-proposed side effects through one approval chokepoint, so the assistant never fires an irreversible action without a cancelable countdown, giving every real-world effect one auditable seam between the LLM and the outside world.
2. Wired the React countdown banner to the action queue so cancelling the on-screen timer aborts the queued Redis job before it auto-fires and promotes the next pending action.
3. Decoupled background workers from the live API behind a Redis Streams event bus with consumer groups, dead-letter routing after 5 retries, and stale-claim recovery, giving at-least-once delivery that Redis pub/sub silently dropped on disconnect.
4. Engineered a no-merge-first speaker-ID model using an EMA voice centroid plus a bounded prototype bank with floor-and-margin gating, abstaining into a new identity on ambiguity, attributing 96% of utterances to the correct speaker.
5. Trained a custom wake-word model to 90% recall at under one false accept per hour, gating the command pipeline so the assistant only opens the mic on demand.
6. Solved the same-room, multi-mic problem with two arbitration layers, a live utterance-owner election and a 400ms windowed quality election on SNR, clarity, and cadence, routing to the best mic and cutting duplicate transcription by ~50%.
7. Built a React client that streams microphone audio over a WebSocket with client-side Web Audio processing, rendering live captions in under 300ms as the backend transcribes.
8. Split speech recognition into a Deepgram streaming path for live command latency and a batched Whisper path for ambient bulk transcription, matching each engine to its latency requirement so interactive commands stay responsive while bulk transcription stays cheap.
9. Replaced single-signal context lookup with hybrid retrieval over pgvector that fuses vector similarity, lexical overlap, recency decay, and participant overlap before the model proposes actions, grounding every proposal in ranked episodic evidence under a fixed token budget.
10. Shipped the backend as two services from one Docker image by role, with boot-time migrations and a three-layer restart strategy surviving the worker queue's silent exit-zero death on a Redis drop, behind a CI gate of lint, tests, and migrations.
```

---

### Project: fliks

**Lane:** Go concurrency and the self-hosted media pipeline, plus the ML validation layer. The only entry that owns Go deeply, and the only one carrying a crowd-to-model rating system.

**Header:**

```
fliks  |  {tech derived from selected bullets}    github.com/fliks-gg
Multi-game platform that crowd-validates gameplay skill and mints shareable certification cards
```

**Bullet pool:**

```
1. Chose a single Go monolith over a microservice split, keeping auth, rate-limiting, and rating aggregation in-process because premature decomposition is the harder call to defend at pre-scale, one deploy unit against one datastore.
2. Built a self-hosted video transcoding pipeline with a concurrent Go worker that pulls upload jobs, transcodes, and writes processed video back to object storage, owning the media path end to end instead of renting a managed service.
3. Coordinated transcode jobs through a Postgres-backed queue using SELECT FOR UPDATE SKIP LOCKED instead of bolting on Redis or SQS, keeping the whole system on one datastore and one self-provisioned EC2 box with no managed queue or transcoding service.
4. Architected an ML rating service that grades each clip independently and displays its verdict beside the crowd's, turning model-versus-community disagreement into product surface, with crowdsourced ratings serving as the labeled data the classifier trains on.
5. Made ratings immutable and gated commenting behind a submitted rating, so the certification signal cannot be retroactively gamed and social participation feeds skill data instead of diluting it.
```

---

### Project: WizViz

**Lane:** Real-time computer vision and on-device inference, built under hackathon constraint. The only perception-adjacent, real-time-CV entry; carries a hackathon track win for credibility.

**Header:**

```
WizViz  |  {tech derived from selected bullets}   devpost.com/software/wizviz
Webcam fighting game driven by real-time body-gesture recognition, winner of the Interactive Media track at SpartaHack X
```

**Bullet pool:**

```
1. Stabilized noisy per-frame pose output by accumulating every frame's gesture classification across the turn window and taking the dominant sustained gesture, instead of reading a single jittery frame at the turn boundary.
2. Classified five distinct combat gestures from body landmarks with a scale-invariant geometric model normalized by torso length, making detection work across players and camera distances without any labeled training data.
3. Ran pose inference asynchronously off the render loop with a monotonic timestamp guard that drops out-of-order results, sustaining 60 FPS with sub-20ms input lag instead of blocking on per-frame detection.
4. Separated two players on one webcam by landmark position, assigning each detected pose to a side of the frame so local two-player worked with zero additional cameras.
5. Built a single-player opponent with a difficulty knob, random play below a threshold and a finite-state policy above it that rests, defends, heals, or finishes based on game state.
```