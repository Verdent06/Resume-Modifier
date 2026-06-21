# Candidate Context

Canonical state for Ankur Desai's resume system. Headers, bullet pools, swap sets, and skills inventory. The writer agent reads this file; the grader does not.

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

Character limit per bucket line: ~80 characters after the bucket label.

### Bucket: Languages

```
Python, Java, JavaScript/TypeScript, SQL, Cypher, C++, Go, Bash
```

### Bucket: Frameworks

```
FastAPI, Spring Boot, Node.js, React, Next.js, Angular, Electron, ROS2
```

### Bucket: Databases

```
PostgreSQL, Neo4j, MongoDB, Redis
```

### Bucket: Cloud & Infrastructure

```
AWS (EC2, RDS, S3), Docker, Kubernetes, GitHub Actions, CI/CD Pipelines, Gazebo
```

### Bucket: AI / ML

```
PyTorch, Hugging Face, faster-whisper, pyannote-audio, spaCy, sentence-transformers, RAG
```

### Bucket: Tools

```
Git, Linux, Postman, Figma, Microsoft Office, RViz, ROSBag
```

---

## Canonical Entries

Each entry has a fixed header and a bullet pool. Bullets are copied verbatim into the resume; swap-set substitutions are the only modification permitted.

---

### Experience: Bopardikar Lab

**Header:**

```
Secure and Efficient Autonomous Systems Lab       May 2026 -- Present
Undergraduate Research Assistant                  East Lansing, MI
```

**Bullet pool:**

```
1. [pending]
2. [pending]
3. [pending]
4. [pending]
5. [pending]
6. [pending]
```

---

### Experience: Claude Builder Club @ MSU

**Header:**

```
Claude Builder Club @ MSU                         Oct 2025 -- Present
Co-Founder & Vice President                       East Lansing, MI
```

**Bullet pool:**

```
1. Eliminated manual onboarding by automating member provisioning across GitHub and Slack, granting repository and workspace access in under 30 seconds for new contributors at scale. (vertical: onboarding automation)
2. Replaced paper attendance workflows with QR-based check-ins backed by token caching on AWS S3 and CloudFront, enabling real-time validation during events. (vertical: attendance infrastructure)
3. Built an event processing pipeline that cross-checks check-in records with enrollment data and publishes per-event Slack summaries for board visibility. (vertical: event reporting pipeline)
4. Hardened attendance batch reliability with soft-fail and idempotent processing so malformed records do not interrupt full event report generation. (vertical: fault-tolerant batch processing)
5. Enforced a four-tier role progression model using PostgreSQL row-level security so access policy is inherited by new routes without per-endpoint auth rewrites. (vertical: authorization architecture)
6. Standardized delivery quality with GitHub Actions coverage gates above 90 percent and production branch protections to block unreviewed, under-tested merges. (vertical: CI/CD guardrails)
7. Automated operational visibility for leadership with instant participation data instead of delayed manual reconciliation from paper sign-in sheets. (vertical: leadership analytics)
8. Scaled internal tooling to support a fast-growing engineering community, with onboarding and event systems used across 100-plus to 150-plus members. (vertical: organization scale operations)
```

---

### Experience: WFS Consulting Group

**Header:**

```
WFS Consulting Group                              May 2025 -- Aug 2025
Web Development Intern                            Plymouth, MI
```

**Bullet pool:**

```
1. Built the firm's primary customer-facing website in Vue, translating business goals into a production web experience for external clients. (vertical: website build ownership)
2. Iterated directly on Figma mocks with a non-technical stakeholder to convert design feedback into shipped frontend components. (vertical: cross-functional design collaboration)
3. Delivered a mobile-responsive interface so the site remained usable and visually consistent across phones, tablets, and desktop browsers. (vertical: responsive frontend implementation)
4. Implemented validated contact form flows to improve lead capture quality and prevent malformed submissions before backend handling. (vertical: form validation and reliability)
5. Converted static design artifacts into maintainable Vue views and reusable UI structures suitable for ongoing content and layout updates. (vertical: componentized frontend delivery)
6. Shortened design-to-release iteration cycles by pairing directly with stakeholders and incorporating feedback in the same build stream. (vertical: iterative delivery velocity)
7. Improved accessibility of firm information by consolidating service and contact experiences into a single coherent public web surface. (vertical: information architecture)
8. Executed end-to-end frontend implementation for an external-facing business site, from design interpretation through responsive launch readiness. (vertical: end-to-end web execution)
```

---

### Project: Dadei

**Header:**

```
Dadei                                             May 2025 -- Jun 2026
{tech stack derived from selected bullets}
```

**Bullet pool:**

```
1. Built an identity-aware voice assistant platform that turns noisy, multi-speaker audio into actionable conversations, memories, and follow-ups, balancing real-time responsiveness with durable history so users can act on spoken context later. (vertical: project overview)
2. Serialized interaction transcription behind a single processing lock to prevent memory spikes, then gated chunks by speech quality and per-window stream scoring before persistence and fan-out, reducing wasted inference on low-signal audio. (vertical: interaction ingest + audio quality gate)
3. Replaced single-signal context lookup with a hybrid retrieval pipeline that fuses 768-dimensional vector similarity, lexical overlap, recency, participant overlap, and threshold gating, then assembles ranked episodic and conversation context under a char budget. (vertical: hybrid RAG + context assembly)
4. Separated realtime delivery into an in-process WebSocket registry and a Redis Streams bridge, adding dedupe keys, retry/backoff handling, and dead-letter routing so cross-process events stay replayable without duplicating client-side mutations. (vertical: realtime broker + stream reliability)
5. Moved post-interaction memory work, conversation-close processing, and delayed action firing onto deduplicated queues with a dedicated scheduled-actions lane and 600-second claim windows, keeping request paths fast while preserving eventual consistency for side effects. (vertical: async orchestration + action scheduling)
6. Standardized identity around access-plus-refresh token lifecycles while preserving web and desktop Google OAuth return flows with strict state and origin validation, enabling safer auth hardening without breaking existing client sign-in paths. (vertical: auth + OAuth lifecycle)
7. Consolidated browser and desktop surfaces behind a shared UI/domain layer, then isolated native concerns in Electron main/preload boundaries and encrypted token storage with keychain fallback, cutting drift while keeping sensitive operations out of renderer scope. (vertical: dual-runtime frontend + desktop security boundary)
8. Combined reconnecting realtime control with local wake-word inference and 16 kHz command audio streaming, using 20-second heartbeats, a 60-second watchdog, and adaptive silence capture windows to keep hands-free interaction responsive during unstable network conditions. (vertical: client realtime + wake-word audio pipeline)
```

---

### Project: MindMosaic

**Header:**

```
MindMosaic --- Knowledge Graph Explorer           Aug 2025 -- Jun 2025
{tech stack derived from selected bullets}
```

**Bullet pool:**

```
1. Built an interactive Three.js knowledge graph explorer that lets users visually traverse, search, and filter interconnected ideas in 3D space. (vertical: 3D graph UX)
2. Designed dual-database persistence with PostgreSQL and Neo4j to model structured records and graph relationships in a unified application flow. (vertical: dual-database architecture)
3. Refactored Cypher queries with relationship-type indexing to cut p95 traversal latency from 850 ms to 440 ms on complex graph lookups. (vertical: graph query optimization)
4. Achieved multi-hop graph traversal performance roughly three times faster than comparable SQL self-join pathways for recursive relationship discovery. (vertical: traversal performance gains)
5. Integrated Google and GitHub OAuth 2.0 sign-in with httpOnly JWT cookies, refresh token rotation, and durable auth session handling. (vertical: authentication system)
6. Enforced user-scoped graph access so each authenticated user traverses only their own subgraph and related knowledge entities. (vertical: tenant data isolation)
7. Established Docker-based environment parity across local and staging workflows to support one-command setup and reduce config drift. (vertical: dev/staging parity)
8. Authored CI/CD pipelines and Dockerfiles for a polyglot stack, enforcing branch protection and automated test gates with 85-plus percent coverage across 35-plus tests. (vertical: release automation and quality gates)
```

---

### Project: WizViz

**Header:**

```
WizViz --- SpartaHack X                           Feb 2025
{tech stack derived from selected bullets}
```

**Bullet pool:**

```
1. Won first place in the Interactive Media track at SpartaHack X with a cooperative, gesture-controlled wizard duel built under hackathon constraints. (vertical: competition outcome)
2. Designed gameplay where full-body movement maps to spell casting, blocking, and ability activation to create a touchless, motion-first game loop. (vertical: gesture gameplay design)
3. Processed live player motion with a MediaPipe pose pipeline that extracts 33 skeletal landmarks per frame for action interpretation. (vertical: pose sensing pipeline)
4. Classified landmark streams into discrete game actions and tuned pose-to-action mappings for stable recognition during active play. (vertical: real-time action classification)
5. Tightened the inference loop to sustain 60 FPS with sub-20 ms input lag, preserving responsiveness in competitive duel interactions. (vertical: low-latency runtime optimization)
6. Projected live 3D pose output into a custom 2D physics model with collision response to keep character motion and combat interactions stable. (vertical: physics integration)
7. Implemented on-device gameplay intelligence so duel logic and opponent behavior run without cloud round-trips during matches. (vertical: edge-first game inference)
8. Delivered an end-to-end computer vision game stack using Python, MediaPipe, OpenCV, TensorFlow, and NumPy for real-time interactive media. (vertical: CV stack integration)
```

---

### Project: fliks.gg

**Header:**

```
fliks.gg                                          Jun 2026 -- Present
{tech stack derived from selected bullets}
```

**Bullet pool:**

```
1. [pending]
2. [pending]
3. [pending]
4. [pending]
5. [pending]
6. [pending]
```
