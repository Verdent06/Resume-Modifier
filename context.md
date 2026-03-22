# Candidate Context

---

## Personal Information

- **Name:** Ankur Desai
- **Phone:** (248) 657-3805
- **Email:** [ardusa05@gmail.com](mailto:ardusa05@gmail.com)
- **Website:** ardusa.github.io
- **LinkedIn:** linkedin.com/in/ardusa
- **Citizenship:** U.S. citizen — no current or future visa sponsorship required; unrestricted work authorization
- **University:** Michigan State University, East Lansing, MI
- **Degree:** B.S. in Computer Science
- **GPA:** 3.5 / 4.0
- **Current semester:** Spring 2026

---

## Graduation Date (ATS Targeting)

Use the year that maximizes fit for the specific role. Default rules:


| Target Class                                                      | Use On Resume                                                 |
| ----------------------------------------------------------------- | ------------------------------------------------------------- |
| Sophomore-targeted ("class of 2028", graduation window 2027–2028) | **Expected, May 2028**                                        |
| Junior-targeted ("class of 2027", graduation window 2026–2027)    | **Expected 2027** *(omit "December" — use bare year for ATS)* |


When the JD is ambiguous, use **May 2028**.

---

## Work Authorization & Relocation

- U.S. citizen; no sponsorship needed now or in the future
- Willing to relocate for any internship, anywhere in the U.S.
- Available for summer internships, co-ops (semester), and part-time (20+ hrs/week)

---

## Target Roles & Focus

- **Primary:** Software engineering — all tracks (full-stack, backend, systems, infra).
- Computer vision (CV) and DevOps.

---

## Experience

### Claude Builder Club @ MSU

**Title:** Vice President & Co-Founder
**Dates:** October 2025 – Present
**Location:** East Lansing, MI

**What it is:** A student-founded software engineering club at MSU that ships real tools using Anthropic's API. Ankur co-founded the club and leads all engineering. The club operates with production-grade practices: CI/CD, open source workflows, code review, branch protection, and 90%+ test coverage.

**What Ankur built and owns:**

- Automated all member onboarding: GitHub API + Slack SDK integration provisions repo access and Slack workspace membership in under 30 seconds. Before: manual, took days. Result: 97% reduction in setup time across 100+ members.
- QR-driven event check-in system: generates scoped tokens, caches them in AWS S3 via CloudFront CDN, handles real-time check-in. Replaced paper sign-in entirely. Processes 150+ scans/event; S3-backed token caching reduced redundant auth calls by 60%. Result: 80% reduction in processing time.
- CI/CD infrastructure: GitHub Actions pipeline with 90%+ coverage gates and branch protection on all production merges. 20–30+ tests. Bug escape rate reduced 65%.
- Enforces open source practices across the club: PR review process, branch naming conventions, contribution guidelines.

**Strongest angles by role type:**

- *Automation / Agentic AI:* workflow automation, member provisioning pipeline, 97% setup-time reduction
- *DevOps:* GitHub Actions CI/CD, coverage gates, branch protection, bug escape reduction
- *Full-stack:* GitHub API + Slack SDK integration, AWS S3, CloudFront, event-driven check-in
- *Leadership:* VP title, co-founder, 100+ member org

**Technologies:** GitHub API, Slack SDK, AWS S3, AWS CloudFront, GitHub Actions, CI/CD, Python, TypeScript, Docker

---

### MindMosaic

**Title:** Technical Lead (use "Software Engineer" for roles where leadership framing is a negative signal)
**Dates:** August 2025 – November 2025
**Location:** East Lansing, MI

**What it is:** A full-stack knowledge graph application where users map and visualize connections between ideas. Core value is multi-hop graph traversal over a relationship model — this is why Neo4j was introduced alongside PostgreSQL.

**What Ankur built and owns:**

- Led a 6-engineer team: owned sprint planning, PR review and merge authority, architecture decisions, CI/CD authorship.
- Dual-database persistence layer: PostgreSQL anchors relational/user data; Neo4j handles graph traversals. Chose Neo4j because recursive SQL self-joins on relationship queries were hitting 850ms p95. After migration: 440ms p95 (48% reduction). Cypher relationship-type indexing made traversals 3× faster than equivalent SQL self-joins.
- Dual-provider OAuth 2.0: Google + GitHub login with httpOnly JWT cookies, refresh token rotation, and user-scoped ABAC (each user traverses only their own subgraph).
- CI/CD: GitHub Actions CI/CD pipeline with build → test → containerized deploy stages. Branch protection on production. 85% coverage, 35+ tests (JUnit + Jasmine).
- Spring Boot backend + Angular frontend + Neo4j stack. Fully containerized with Docker Compose.

**Strongest angles by role type:**

- *Fintech / backend:* Spring Boot, OAuth 2.0, JWT, ABAC, PostgreSQL, test coverage, code review
- *Full-stack:* end-to-end ownership, Angular + Spring Boot + Neo4j, Docker, CI/CD, team lead
- *DevOps:* GitHub Actions CI/CD, Docker Compose, environment parity, branch protection, coverage gates
- *Data / graph:* graph analysis, multi-hop traversals, polyglot persistence, p95 latency improvement

**Technologies:** Spring Boot (Java), Angular, Neo4j, Cypher, PostgreSQL, OAuth 2.0, JWT, Docker, GitHub Actions CI/CD, JUnit, Jasmine, Git

**Known gap:** Spring Boot appears in the stack but most resume versions don't surface a bullet proving Spring Boot ownership. For roles that require it (Fiserv, enterprise backend), use this hook: *"Built Spring Boot + Angular application where users map and visualize idea connections"* and surface the 850ms→440ms query latency story.

---

### WFS Consulting

**Title:** Web Development Intern
**Dates:** May 2025 – August 2025
**Location:** Plymouth, MI

**What it is:** Web Development Internship at a consulting firm, focused on developing web-based solutions for client needs.

**What Ankur built:**

- As an intern, contributed to a responsive company website using Vue.js, delivering a polished, production-ready experience for end customers.
- Implemented a user-facing contact form with robust client-side validation and smooth submission handling as part of the site's core feature set.
- Iterated on a Figma design, collaborating closely with the manager and incorporating feedback to ensure the final product precisely matched requirements.

**Pipeline guidance:**

- This is the weakest experience entry. Include it when the resume needs a third experience line or when the role values client-facing delivery.
- Do NOT lead with it or feature it prominently for engineering-heavy roles.
- Drop it entirely for any FAANG/A-tier application where the two-entry experience section is tighter.
- Never write more than 2 bullets for this entry.

**Technologies:** Vue.js, JavaScript

---

## Projects

### Mira — Agentic AI Voice Assistant

**Dates:** May 2025 – November 2025
**Tech stack:** Python, FastAPI, Next.js, TypeScript, Electron, MongoDB, Redis, Celery, AWS Lambda, Whisper, Sentence-BERT, spaCy, Docker

**What it is:** A multi-client, distributed voice assistant that resolves implicit speaker intent and dispatches real tasks (calendar events, reminders, API calls) to third-party services. Designed for concurrent voice streams from multiple speakers.

**Architecture:**

- FastAPI Python backend; Next.js + Electron frontend (Electron uses Next.js for the renderer process)
- Redis-backed Celery task queue decouples ML inference from the API layer → 73% API response time reduction
- RAG pipeline: Sentence-BERT embeddings + BM25 hybrid search over a MongoDB document store
- Speaker diarization: x-vector clustering for multi-speaker streams; threshold calibration reduced DER 18.4% → 9.1%
- AWS Lambda for inference: lazy-loaded Whisper (ASR), Sentence-BERT, spaCy. Cold-start: 6,643ms → 930ms (86% reduction) via lazy loading + model caching
- Bidirectional Electron + Next.js client with embedded HTTP server for OAuth callback interception; real-time IPC event bus; dedicated webhook server with sub-50ms event propagation
- End-to-end speaker transcription available in under 2 seconds

**ML training work (AI/ML track):**

- Fine-tuned Sentence-BERT intent classification head: SVM classifier, 12-class taxonomy, 200 synthetic utterances, 91% F1. Replaced a brittle regex router; eliminated an entire class of dispatch failures.
- Trained custom spaCy NER component: 180 annotated examples, extracts TASK / PERSON / TIME / APP. 34% recall improvement over `en_core_web_trf` baseline.
- x-vector diarization threshold calibration: DER 18.4% → 9.1%

**Strongest angles by role type:**

- *Agentic AI / AI platform:* multi-agent task dispatch, implicit intent resolution, RAG, concurrent voice streams, real-world automation
- *AI/ML:* Sentence-BERT fine-tuning, spaCy NER training, speaker diarization, BM25 hybrid search, cold-start optimization
- *Backend / full-stack:* FastAPI, async task queues, OAuth, Electron client, IPC, webhook server
- *DevOps:* AWS Lambda, Docker, cold-start reduction, containerized inference
- *Distributed systems:* Redis/Celery decoupling, concurrent stream processing, async architecture

**Technologies:** Python, FastAPI, Next.js, TypeScript, Electron, MongoDB, Redis, Celery, AWS Lambda, Whisper, Sentence-BERT, spaCy, BM25, Docker, OAuth 2.0, IPC, Webhooks

**Track-specific framing guidance:**

- AI/ML track: lead with ML training work. Cold-start Lambda bullet is supporting evidence.
- Full-stack / Agentic AI track: lead with system-level hook (multi-client voice assistant dispatching real tasks). ML work goes later or drops.
- DevOps track: lead with Lambda + cold-start story. Async queue decoupling is bullet 2.
- The Redis/Celery decoupling angle is the single strongest technical decision — it shows you understand why you separate I/O-bound inference from the request path.

---

### WizViz — SpartaHack X

**Date:** February 2025
**Tech stack:** Python, MediaPipe, OpenCV, NumPy, TensorFlow
**Award:** 1st Place, Interactive Media Track — SpartaHack X

**What it is:** A real-time, gesture-controlled game built and demoed at SpartaHack X in 24 hours. Players cast spells and battle an AI opponent using full-body pose movements captured via webcam — no game engine.

**What Ankur built:**

- MediaPipe Pose pipeline: extracts 33 skeletal landmarks per frame, maps them to discrete game actions (spell cast, block, ability trigger). Real-time inference at 60 FPS, sub-20ms input lag.
- Custom 2D vector physics engine with AABB collision detection: translates live 3D skeletal coordinates into 2D game state. Maintains <5px positional drift at 60 FPS under sustained load.
- Fully on-device; no cloud dependency; no game engine.
- Presented and demoed live to judges.

**Strongest angles by role type:**

- *Computer vision / AI:* real-time pose estimation, 33-landmark skeletal mapping, inference at 60 FPS
- *Robotics / autonomous systems:* perception pipeline, real-world camera input, control signal generation from body pose
- *Game dev / simulation:* gameplay mechanics, 3D coordinate translation, physics engine, game state management
- *Any role:* hackathon win is a credibility shortcut — always include "Interactive Media Track Winner"

**Technologies:** Python, MediaPipe, OpenCV, NumPy, TensorFlow

**Notes:**

- Drop for DevOps or pure backend roles.
- For AI/ML: frame as perception pipeline. MediaPipe Pose is the model; inference optimization is the technical hook.
- Hackathon win must be in the hook. Do not bury it.

---

## Resume Track Reference


| Track        | Primary experience     | Lead project                 | Supporting project       | Drop         |
| ------------ | ---------------------- | ---------------------------- | ------------------------ | ------------ |
| `full-stack` | MindMosaic (Tech Lead) | Mira (client + auth + async) | WizViz (optional)        | WFS if space |
| `ai-ml`      | Claude Builder Club    | Mira (ML training first)     | WizViz (perception)      | MindMosaic   |
| `dev-ops`    | Claude Builder Club    | Mira (Lambda + cold-start)   | MindMosaic (CI/CD angle) | WizViz       |


---

## Known Gaps (Pipeline Must Flag These)

- **No prior corporate internship:** Compensate with project depth, metrics, and leadership titles (VP, Technical Lead, co-founder). Flag explicitly in likelihood estimate.
- **MSU is not a FAANG target school:** Compensate via referrals, polished GitHub, and project quality.
- **Spring Boot in bullets:** Stack lives in MindMosaic but most resume versions don't have a bullet proving Spring Boot ownership. Flag for any role requiring it.
- **Go / gRPC:** Go is in Skills on some templates but no project bullet demonstrates it. Flag for roles requiring Go.
- **Kubernetes:** In Skills on some resumes. No bullet demonstrates K8s. Acceptable in Skills only.
- **C++ in bullets:** In Skills but no project bullet with outcome. Only add where WizViz or MindMosaic honestly justify it.

