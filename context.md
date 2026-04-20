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
| Junior-targeted ("class of 2027", graduation window 2026–2027)  | **Expected 2027** *(omit "December" — use bare year for ATS)* |

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
- CI/CD infrastructure: GitHub Actions pipeline with 90%+ coverage gates and branch protection on all production merges. 60+ tests. Bug escape rate reduced 65%.
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

### Dadei — product identity (how to describe it)

**Dates on resume:** May 2025 – February 2026 *(timeline is candidate-owned; stack facts below are repo-audit current.)*

**One-sentence pitch:** Dadei is an **ambient, distributed personal assistant** that passively listens across a **network of devices**, **attributes speech to people**, builds **episodic memory** over time, and proposes **actions** (calendar, reminders, messages) from natural conversation **without** a wake-word-first interaction model.

**Problem it solves:** Traditional assistants are reactive and command-driven: the user must invoke them, repeat context, and manually turn speech into structured artifacts. Dadei inverts that: it maintains conversational state, attributes utterances to individuals, and surfaces proposed actions from ambient speech.

**Product copy anchor (landing page):** *"A distributed personal assistant: you interact through voice and rich panels, and your experience can span multiple devices on the same network."*

**Distribution / properties:**

- **Live product (public):** [https://dadei.app](https://dadei.app) — primary landing / web entry point for the assistant.
- **Website:** React (Vite) SPA; deployment conventions align with **Vercel** (env via Vite `loadEnv`, `.env.production`).
- **Desktop:** **Electron** installers published via GitHub Releases — `https://github.com/dadei-app/frontend/releases` (macOS, Windows, Linux targets per product copy).
- **Backend:** Independent **FastAPI** service on **Railway** (Docker build from `docker/Dockerfile.prod`).

---

### Dadei — lead story for resumes (prioritize; do not bury)

Use these themes **before** laundry lists of repos, “monorepo,” or generic CI. They are what makes the product technically interesting:

1. **Episodic memory + RAG in Postgres (`pgvector`)** — Embeddings on **interactions**, **conversation summaries**, and **episodic memories**; **hybrid** retrieval (semantic + lexical token overlap + **30-day recency** half-life; optional **RRF**); **budgeted** context with similarity gates. Retrieved text is fed into **Gemini** when a conversation closes so summaries and extractions are **grounded** in prior dialogue and stored facts, not free‑regenerated each session.
2. **Authenticated WebSockets + multi-client fan-out** — `WS /api/v1/service/realtime/ws` pushes **`interaction`** and **`action`** JSON to **many registered clients** on the same network so every device stays current without polling; broker is in-process today (single-instance realtime).
3. **Multi-device audio + quality-aware processing** — Several clients can **upload overlapping streams** from the same room. The pipeline runs **audio quality scoring** before heavy ASR so weak or redundant clips are deprioritized; **Redis idempotency**, **per-network locks**, and **webhook dedupe** keep overlapping devices from corrupting one timeline or spamming duplicate events. *(Roadmap / design direction: a stricter “single winning stream” selector by `AudioQualityMetrics` in a short window—confirm wording in interviews if not fully shipped.)*
4. **Gemini tool calling + assembled prompt context** — On conversation close, **Gemini 2.5 Pro** uses declared tools such as **`propose_episodic_memory`** and **`propose_action`** (with evidence quotes and participant indices). **Internal / structured context** is assembled for the model: **RAG hits from the database** (memories, summaries, interactions), plus **grounding helpers** such as **current date/time** and **weather** where integrated, so extraction and summarization run with **explicit, inspectable context** rather than a naked transcript alone.

**Not a headline for Dadei resumes:** “We used a monorepo” or “we have GitHub Actions” — those are table stakes and belong in Skills or one clause, not as the main Dadei story.

---

### Dadei — canonical technical reference (point of proof)

Use this subsection as **ground truth** for bullets, interviews, and system-design questions. It supersedes older resume language that referenced **Next.js, MongoDB, Celery, AWS Lambda, Sentence-BERT fine-tuning, x-vector diarization, BM25-over-Mongo**, etc.

#### End-to-end data flow (verified)

1. Registered client (**browser** or **Electron**) captures audio, gates with **`@ricky0123/vad-react`**, `POST`s WAV to **`/api/v1/interactions/register`** (multipart + `client_id`).
2. Handler returns **`204 No Content`** immediately; work is **`enqueue_or_run`** — **Redis + RQ** when `use_redis_queue`, else **FastAPI `BackgroundTasks`** / inline.
3. Worker **`process_interaction`:** audio quality scoring → **`faster-whisper`** transcription → **`pyannote-audio`** diarization + **speaker matching** (cosine vs per-person centroid + capped prototype bank) → persist **`Interaction`** with **Gemini text embedding** (768-d, see below).
4. **`assign_to_conversation`:** append vs new conversation using **~90s gap** (`CONVERSATION_GAP_THRESHOLD`) **plus topic coherence**.
5. **WebSocket** `WS /api/v1/service/realtime/ws` pushes `{"event":"interaction",...}` to registered clients (**in-process broker** + Redis-backed dedupe claims for fan-out).
6. On **conversation close**, **`context_service.process_conversation`:** **RAG** retrieval → **Gemini 2.5 Pro** structured summary → second Gemini call with **`propose_episodic_memory`** / **`propose_action`** tool declarations → persist proposed **`episodic_memories`** and **`actions`**.
7. **`Action`** rows fan out as `{"event":"action",...}` on the same WebSocket.

#### Backend stack (Python 3.12)

| Area | Technology | Notes |
| --- | --- | --- |
| API | **FastAPI** ~0.116, **Starlette**, **Uvicorn** ~0.35 | `uvloop`, `httptools` |
| ORM / migrations | **SQLAlchemy** 2.0, **Alembic** 1.16 |  |
| Database | **PostgreSQL 15** + **`pgvector`** | Dev image `pgvector/pgvector:pg15`; prod Railway Postgres + extension via migration |
| Config / validation | **Pydantic** 2.9, **pydantic-settings** |  |
| Auth | **authlib**, **python-jose**, **passlib[bcrypt]**, **itsdangerous** | JWT access + refresh; session middleware for OAuth state threading |
| HTTP client | **httpx** |  |
| Legacy ASGI on AWS | **`mangum`** imported in `main.py` | **Vestigial** for Lambda era; **inert** on Railway |
| Optional queue | **`redis`**, **`rq`**, **`core/async_tasks.py`** | Graceful degradation when Redis absent |

#### ML / audio stack

| Component | Model / library | Role |
| --- | --- | --- |
| ASR | **`faster-whisper`**, `large-v3-turbo`, **CPU**, **`int8`** | Word-level timestamps |
| Diarization | **`pyannote-audio`**, `pyannote/speaker-diarization-3.1` | Local inference; **torch** / **torchaudio** / **speechbrain** ecosystem |
| VAD | **Silero** (master TODO) + **`@ricky0123/vad-react`** | Client-side gating before upload |
| Audio DSP | **`noisereduce`**, **SciPy** Butterworth high-pass (`butter_highpass_filter` in transcription path) |  |
| NLP helpers | **`sentence-transformers`**, **`spacy`** + `en_core_web_sm` | Auxiliary (not the core LLM fine-tuning story) |
| LLM | **`google-genai`**, **Gemini 2.5 Pro** | Summaries + tool calling for memory/action extraction |
| Embeddings | **Gemini `gemini-embedding-001`** | All semantic embeddings for RAG rows |

**Central constants (conceptual; names mirror `app/core/constants.py`):**

- `WHISPER_MODEL_NAME = "large-v3-turbo"`
- `WHISPER_MODEL_DEVICE = "cpu"`
- `WHISPER_MODEL_COMPUTE_TYPE = "int8"`
- `PYANNOTE_DIARIZATION_MODEL_NAME = "pyannote/speaker-diarization-3.1"`
- `GEMINI_TEXT_MODEL_NAME = "gemini-2.5-pro"`
- `GEMINI_EMBEDDING_MODEL_NAME = "gemini-embedding-001"`

**Custom ML-flavored logic (not fine-tuned foundation models):** per-**`Person`** **online** voice identity: **centroid** `voice_embedding` + **prototype bank** `voice_embedding_bank` (max **8** prototypes). Updates via **EMA** (`SPEAKER_EMBEDDING_EMA_ALPHA=0.22`), bank eviction favors **furthest-from-centroid**. Matching: **cosine** with **`SPEAKER_MATCH_FLOOR=0.32`**, **`SPEAKER_MATCH_MARGIN=0.038`**, small **`SPEAKER_PRIOR_BOOST=0.04`**. This is a **hand-tuned classifier**, not a separately trained diarization model.

**Important correction vs older resume drafts:** There are **no fine-tuned LLMs** in Dadei. Do not claim Sentence-BERT fine-tuning, SVM intent heads, or custom spaCy NER training **for Dadei** unless independently verified outside this audit.

#### Gemini integration (three modes)

1. **Structured summarization** — built context → Gemini 2.5 Pro → **`ConversationSummary`** via JSON schema / `response_mime_type="application/json"` + `response_schema`.
2. **Tool calling on conversation close** — `propose_episodic_memory` and `propose_action` with JSON-schema parameters; `tool_config` function calling **AUTO** at **temperature 0.1**; iterate calls via `_iter_function_calls_from_response` pattern; validate into **`ExtractedEpisodicMemory`** (Pydantic).
3. **Embeddings** — `embed_content` on **`gemini-embedding-001`**, **truncate to 768 dims**, pad if short, **L2-normalize** before persistence.

**Prompt assembly (highlight for resumes):** Before those calls, **`retrieve_relevant_context`** (and related assembly) pulls **vector + hybrid-ranked** rows from Postgres so the model sees **prior conversations, episodic memories, and scored interactions** as first-class context. **Additional structured signals** (e.g. **current date/time**, **weather**, other **internal tool or API results**) are folded into the same prompt surface where the product wires them, so extraction runs against **grounded facts + transcript**, not the transcript alone. *(Exact set of live “weather” / clock integrations—confirm against current `context_service` / tool wiring before claiming specifics in high-stakes interviews.)*

**Fallback path:** `call_gemini_memory_extraction` when tool path yields zero calls — flat `proposed_memories[]` JSON schema. Controlled by **`CLOSE_CONVERSATION_USE_GEMINI_TOOLS = True`** (prefer tools when healthy).

#### RAG / retrieval (`context_service.retrieve_relevant_context`)

- **Vector store:** **pgvector** co-located in Postgres (not Pinecone / Weaviate / Qdrant).
- **Embedding:** Gemini → **768-d** L2-normalized vectors.
- **Stages (conceptual):** (1) conversation summaries by **cosine distance** (top ~40), (2) episodic memories (`status in ('proposed','confirmed')`, not expired), (3) interaction-level scoring via **`_top_interactions_by_embedding`**, (4) **hybrid** `hybrid_score(semantic_sim, lexical_score, semantic_weight=0.7, lexical_weight=0.3)` where lexical is **token-set overlap** (not BM25 IDF), **recency** weight `exp(-ln2 * age_days / half_life_days)` with **30-day** half-life, (5) **RRF** `reciprocal_rank_fusion` **k=60** available for merging lists, then **budgeting** (e.g. episodic **28%** of char budget) with gates **`MEM_GATE = 0.22`**, **`CONTEXT_SIMILARITY_THRESHOLD = 0.45`**.

#### Vector columns and indexes (768-d text embeddings)

| Table.column | Indexed | Method |
| --- | --- | --- |
| `episodic_memories.text_embedding` | **Yes** — `ix_episodic_memories_text_embedding_ivfflat` | **IVFFlat** `vector_cosine_ops`, **lists=100** |
| `conversations.summary_embedding` | **Yes** — `ix_conversations_summary_embedding_ivfflat` | **IVFFlat** `vector_cosine_ops`, **lists=100** |
| `interactions.text_embedding` | **No IVFFlat** | Queried within filtered recent sets by design |

**Voice embeddings (different space):** `persons.voice_embedding` + `persons.voice_embedding_bank` store **pyannote-space** vectors as JSON/lists; **NumPy cosine** in application code — **not** pgvector columns.

#### API surface (all under `/api/v1`)

**Auth**

- `POST /auth/login`, `POST /auth/register`, `POST /auth/refresh`
- Google OAuth: desktop loopback (**port 4280**) and **web** flow with SPA origin handshake + CORS / Referer validation

**Interactions**

- `POST /interactions/register` — **204**, multipart audio, background job
- `GET /interactions`, `GET /interactions/{id}`, `DELETE /interactions/{id}`

**Service + realtime**

- Client registry: `POST /service/clients`, `GET /service/clients`, `DELETE /service/clients/{client_id}`, `PATCH /service/clients/{client_id}/rename`
- Network enable/disable: `PATCH /service/network/enable`, `PATCH /service/network/disable`
- **`WS /service/realtime/ws?token=…&client_id=…`** — JWT in query; events: **`interaction`**, **`action`**, **`service_status`**

**Conversations & persons**

- Conversations: `GET /conversations`, `GET /conversations/{id}`, `PATCH /conversations/{id}`
- Persons: `GET /persons`, `GET /persons/{id}`, `PATCH /persons/{id}` (multipart: name, enrollment audio, expected text), `DELETE /persons/{id}`

**Versioning:** `GET /` returns `{"stable":"v1","beta":"v2"}`; **`/api/v2`** scaffold exists but **v1** is the wired surface today.

#### State, scaling, and reliability notes

- **Auth token subject:** `Authorization: Bearer {UserNetwork.id}` as JWT `sub`; resolved via **`get_network_id`** dependency pattern.
- **Persistence:** Postgres for all durable state; **WebSocket registry is in-process** → **single-instance** realtime today; horizontal scale would need **pub/sub**.
- **Conversation close serialization:** per-`network_id` lock in Redis (`lock:conversation:{network_id}`, **15s** hold, **3s** block wait) with **no-op fallback** if Redis disabled.
- **Idempotency:** `interaction_job:{network_id}:{client_id}:{sha256_digest}` with **`SET NX EX 300`** when Redis available (`app/docs/interaction_pipeline_contract.md`).
- **Webhook / fan-out dedupe:** `claim_webhook_delivery` — hourly Redis slot **`webhook:{event_type}:{entity_id}:{client_id}:{YYYYMMDDHH}`** with **1h TTL**.

#### Frontend (implementation layout — not the product headline)

- **Tooling:** **npm workspaces** — `apps/website`, `apps/desktop`, `packages/ui` (**published as `@dadei/ui`**). Treat as **how the UI is organized**, not as the core technical story on a resume.
- **UI stack:** **React 19.2**, **Vite 7**, **TypeScript 5**, **Tailwind CSS 4**, **framer-motion**, **lucide-react**, **Radix** dialog + **react-alert-dialog**.
- **Desktop:** **Electron** ~39.8, **electron-builder** ~26, **electron-updater** ~6.8, **keytar** ~7.9 (OS keychain).
- **HTTP:** **axios** (~1.13) via shared client; enumerated endpoints in `shared/api/constants.ts`; timeouts (e.g. default **10s**, interactions **30s**); **`retryWithBackoff`** (~2 attempts, **1000ms** baseline).
- **Realtime:** `realtimeClient.ts` — **`wss://…/api/v1/service/realtime/ws`**, exponential backoff reconnect (cap **30s**), **20s** heartbeat, listener fan-out to hooks.
- **Electron security posture (intentional):** **`contextIsolation: true`**, **`nodeIntegration: false`**, OAuth window **`sandbox: true`**; preload exposes a **narrow** `contextBridge` API (~**11** IPC methods) for tokens, Google login, client name, deregistration, and event subscriptions; tokens in **keytar**, not renderer **localStorage**.

#### Infra, CI/CD, deployment (supporting detail — rarely the Dadei headline)

- **Docker:** `docker/Dockerfile.dev` vs `docker/Dockerfile.prod`; **`docker-compose.yml`** pins **`pgvector/pgvector:pg15`** for local DB.
- **Railway:** `railway.toml` → `dockerfilePath = "docker/Dockerfile.prod"`; start: **`alembic upgrade head`** then **`uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}`**; healthcheck **`GET /`**, **300s** timeout, **`ON_FAILURE`** restart.
- **Backend CI (GitHub Actions):** matrix — **`lint`** (Ruff on `app` + `tests`), **`test`** (Alembic + **pytest** against **pgvector** service container), **`database`** (Alembic + extension sanity for `vector`).
- **Frontend CI:** separate workflow(s) for cross-platform **electron-builder** builds / signing concerns (per README patterns).
- **Environments:** effectively **local dev → production on Railway**; no separate staging branch called out in deployment config.

These items support reliability and hiring signal but **do not replace** RAG, realtime, multi-device audio, and Gemini/tooling as the primary Dadei narrative on resumes.

#### Architectural decisions (how to talk about tradeoffs)

1. **Passive-first memory** — heavy analysis on **conversation close** (gap + topic shift) vs per-utterance extraction (token cost + noise) vs wake-word-only (product identity). Tool calls require **evidence quotes** + **participant indices** into a numbered transcript manifest → **hallucination control**.
2. **pgvector co-located with OLTP** — single migration/backup story, transactional joins between rows and embeddings; trade IVFFlat tuning / scale limits vs dedicated vector DB.
3. **Distributed realtime + dedupe** — multi-device networks imply duplicate audio paths; **Redis** dedupe + **per-network locks** with **graceful degradation** when Redis absent (accept duplicate delivery risk). Future direction (per master TODO): backend **`PendingCommandBuffer`** winner by **`AudioQualityMetrics.score`** in ~**400ms** window — **not** the only story in current prod.

---

### Dadei — resume-ready technology list (aggregated)

**Backend:** Python 3.12, FastAPI, Starlette, Uvicorn, SQLAlchemy 2.0, Alembic, PostgreSQL 15, pgvector, Pydantic, Redis (optional), RQ (optional), httpx, authlib, JWT, pytest, Ruff, Docker, Railway, GitHub Actions.

**ML / AI:** faster-whisper, pyannote-audio, torch/torchaudio, Silero VAD (client), noisereduce, SciPy, sentence-transformers, spaCy, Google Gemini API (2.5 Pro + embeddings), structured output + function calling, hybrid RAG over pgvector.

**Frontend:** React 19, Vite 7, TypeScript 5, Tailwind CSS 4, Electron 39, electron-builder, electron-updater, keytar, axios, WebSockets, Framer Motion, Radix UI, npm workspaces, `@dadei/ui`.

---

### Dadei — strongest angles by role type (audit-aligned)

- *Agentic AI / AI platform:* passive listening, multi-device network, **RAG-grounded** Gemini passes, **tool calling** to **episodic memory** + **actions**, evidence-grounded proposals, **WebSocket** fan-out.
- *AI/ML engineering:* **RAG** with **hybrid semantic + lexical + recency**, **pgvector** ANN (**IVFFlat**), **Gemini** structured outputs + tools, **ASR + diarization + online speaker embedding** updates, **audio quality** gating before ASR.
- *Backend / distributed:* **WebSockets** to many clients, optional **Redis/RQ**, **idempotency** + **delivery dedupe**, **per-network locking**, Postgres + **pgvector** in one transactional store.
- *Full-stack:* **Realtime** UX (WS-driven panels), **RAG-backed** assistant flows, multi-device capture; OAuth / Electron / shared UI package are **supporting** implementation details, not the lead hook.
- *DevOps / platform:* Docker + **Alembic-on-start**, Railway healthchecks, CI with real **pgvector** — use as **one line** of credibility, not the main Dadei story unless the JD is infra-first.

---

### WizViz — SpartaHack X

**Date:** February 2025  
**Portfolio / submission (public):** [https://devpost.com/software/wizviz](https://devpost.com/software/wizviz) — hackathon write-up, screenshots, team credits, and **Best Game / Interactive Media** placement for SpartaHack X (see Devpost “Submitted to” and updates).

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

- For pure DevOps/backend targeting, keep WizViz to **at most one short bullet** (or title + Devpost URL only); full CV/ML detail belongs on AI/ML and full-stack tracks.
- For AI/ML: frame as perception pipeline. MediaPipe Pose is the model; inference optimization is the technical hook.
- Hackathon win must be in the hook. Do not bury it.

---

## Resume Track Reference

| Track        | Primary experience     | Lead project | Supporting project | Drop         |
| ------------ | ---------------------- | ------------ | ------------------- | ------------ |
| `full-stack` | MindMosaic (Tech Lead) | **Dadei** — **RAG + pgvector** (episodic + summaries + interactions), **Gemini** tool calling, **WebSocket** multi-client fan-out, quality-aware multi-mic ingest | WizViz (optional) | WFS if space |
| `ai-ml`      | Claude Builder Club    | **Dadei** — RAG over **pgvector**, Gemini summaries + tool extraction, faster-whisper + pyannote + online speaker embeddings | WizViz (perception) | MindMosaic   |
| `dev-ops`    | Claude Builder Club    | **Dadei** — Docker + Railway + Alembic-on-start, GitHub Actions CI (Ruff, pytest+pgvector, extension checks), Redis/RQ optional path | MindMosaic (CI/CD angle) | WizViz       |

---

## Known Gaps (Pipeline Must Flag These)

- **No prior corporate internship:** Compensate with project depth, metrics, and leadership titles (VP, Technical Lead, co-founder). Flag explicitly in likelihood estimate.
- **MSU is not a FAANG target school:** Compensate via referrals, polished GitHub, and project quality.
- **Spring Boot in bullets:** Stack lives in MindMosaic but most resume versions don't have a bullet proving Spring Boot ownership. Flag for any role requiring it.
- **Go / gRPC:** Go is in Skills on some templates but no project bullet demonstrates it. Flag for roles requiring Go.
- **Kubernetes:** In Skills on some resumes. No bullet demonstrates K8s. Acceptable in Skills only.
- **C++ in bullets:** In Skills but no project bullet with outcome. Only add where WizViz or MindMosaic honestly justify it.
- **Historical resume drift for Dadei:** Older PDFs may still list **Mira** naming or **Next.js / MongoDB / Celery / Lambda / fine-tuned BERT** claims. Pipeline should **normalize** against **this file** before grading or shipping new resumes.
