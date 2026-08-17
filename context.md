# Candidate Context

Canonical state for Vedant Desai's resume system. Headers, bullet pools, swap sets, and skills inventory. The writer agent reads this file; the grader does not.

**Profile (the 7-second impression):** A full-stack data and AI engineer with real-time C++ systems depth who ships production pipelines, voice-AI cost/latency wins, agentic B2B products, and hard real-time audio DSP — not notebook ML or pure frontend.

Each entry carries a fixed **Lane**: the one distinct signal it contributes that no other entry can. Per-track scaling is volume control on lanes the target role rewards, not reassignment.

---

## Identity

- **Name:** Vedant Desai
- **Phone:** (248) 704-4852
- **Email:** [vedantde@umich.edu](mailto:vedantde@umich.edu)
- **Portfolio:** — (omit from resume header)
- **LinkedIn:** [https://linkedin.com/in/vedantde06](https://linkedin.com/in/vedantde06)
- **GitHub:** [https://github.com/Verdent06](https://github.com/Verdent06)

---

## Education

```
University of Michigan                              Expected May 2028
B.S. in Computer Science and Economics              Ann Arbor, MI
GPA: 3.66 / 4.0
Coursework: Data Structures & Algorithms, Intro to Statistics and Data Analysis, Microeconomics, Macroeconomics, Discrete Mathematics, Calculus III, Physics (Mechanics)
```

---

## Swap Sets

Flat dictionary. Unconditional within each set. Single-token swaps.

```yaml
llm-apis: [Gemini, Claude, OpenAI]
```

---

## Skills Inventory (Buckets)

Master pools. The writer picks 3-5 buckets per resume and trims each to ~80 characters after the label for the rendered line. Items below exceed that on purpose so there is room to select per role.

### Bucket: Languages

```
Python, TypeScript, C++, SQL, HTML/CSS
```

### Bucket: Frameworks

```
React, Angular, FastAPI, Flask, RxJS, JUCE
```

### Bucket: Databases

```
PostgreSQL, Redis, pgvector
```

### Bucket: AI / ML

```
LangGraph, LangSmith, PyTorch, Pandas, RAG, Agentic Workflows, LLM-as-a-Judge, Silero VAD, ONNX Runtime
```

### Bucket: Cloud & Infrastructure

```
AWS (EC2, S3), Docker, Celery, Git, GitHub Actions
```

### Bucket: Robotics

```
SolidWorks
```

### Bucket: Tools

```
Playwright, Selenium, Web Workers, Asynchronous Queues, Google Maps API, VST3, AudioUnit, SIMD
```

---

## Canonical Entries

Each entry has a fixed header, a Lane, and a bullet pool. Bullets are copied verbatim into the resume; swap-set substitutions are the only modification permitted. Experience entries carry dates; project entries carry a live link instead of a date so they can be ordered by relevance, not recency. Each project also carries a one-line descriptor that renders below the name (the rSectionEntry tagline slot, param #3), giving the at-a-glance "what it is." Because the descriptor carries identity, a project's lead bullet leads with its strongest engineering decision, never a re-description of the project. Experiences have no descriptor slot (the tagline holds the role), so an experience's first bullet still establishes what was built.

**Bullet length ceiling (going forward, this pool only — not retroactive).** `resume.md` §4 targets "two tight lines" qualitatively; quantified against `template.cls`'s actual rendering (10pt CMU Serif, 0.4in margins), that template wraps bullet body text at **~115–120 characters/line**, measured directly off compiled output. Two tight lines ≈ **230–240 characters total**. When writing or editing a bullet for this pool going forward, target that ceiling — three-line bullets should be the exception (a bullet earning its extra depth), not the default. Existing bullets were not audited/trimmed against this number retroactively; several run 250–380 characters (3 lines). Re-tighten opportunistically when an entry is touched for other reasons, not as a standalone pass.

---

### Experience: Michigan Data Consulting (MDC)

**Lane:** Client-facing data engineering and production delivery. The only entry that shows sole-contractor ownership of a Flask REST API on AWS EC2 shipped to a real nonprofit stakeholder (MCFN) inside a fixed engagement window — anchors the full-stack + data-pipeline track's "shipped to real users" signal.

**Header:**

```
Michigan Data Consulting (MDC)                    Jan 2026 -- May 2026
Data Engineer — Michigan Campaign Finance Network   Ann Arbor, MI
```

**Bullet pool:**

```
1. Replaced manual Michigan campaign-finance research — portal searches capped by the Bureau of Elections, irregular Excel exports, hand normalization at ~2 hours per committee — with a Requests + Pandas ETL that ingests filings directly, eliminating ~800 hours of manual pulls across 400 tracked PACs.
2. Architected a deterministic aggregation engine that parses those exports, normalizes irregular contribution amounts, and ranks PACs by total funding volume so researchers stop rebuilding spreadsheets to surface top spenders.
3. Delivered a production Flask REST API on AWS EC2 as the sole engineer on a 5-month MCFN contract, wiring ingested data and PAC rankings into the nonprofit's public-facing research workflow.
4. Scoped technical delivery directly with MCFN stakeholders as the only engineer on contract — from ingestion pipelines through REST endpoints on EC2 — with no backend team to share infrastructure, API design, or deployment ownership.
```

---

### Experience: CaseStudyPrep.AI

**Lane:** Voice-AI systems and client-side performance engineering. Carries the only on-device inference signal (Silero VAD via ONNX), Web Workers / RxJS decoupling, and fault-tolerant S3 upload pipeline — the portfolio's real-time frontend + audio stack depth.

**Header:**

```
CaseStudyPrep.AI                                  Dec 2025 -- May 2026
Software Engineer Co-op (Voice AI)                  Remote
```

**Bullet pool:**

```
1. Eliminated the silent-audio problem in a voice-AI product — most frames sent to Whisper were dead air — by running Silero VAD client-side via ONNX Runtime, filtering silence before upload and cutting cloud inference costs by 40%.
2. Eliminated a 27% audio upload failure rate with fault-tolerant RxJS logic that detects expired S3 presigned URLs, regenerates them mid-flight, and negotiates MIME types for WAV files Angular silently rejected.
3. Moved audio processing off the UI thread into a Web Worker with an async stream handoff, reducing main-thread blocking time to under 5ms and keeping the real-time audio visualizer at a smooth 60 FPS during active inference.
```

---

### Experience: Lyndbrook Capital

**Lane:** Deal-sourcing and GTM data engineering for a boutique search fund. The only entry with pre-acquisition target generation (EPA ECHO, MassGIS, Google Maps cross-ref) and proprietary scoring algorithms — quant/GTM lane without fintech-exchange framing.

**Header:**

```
Lyndbrook Capital                                   Feb 2026 -- Apr 2026
Data Engineering Consultant                         Remote
```

**Bullet pool:**

```
1. Contracted pre-LOI to build acquisition intelligence for a boutique search fund targeting water utility operators; aggregated EPA ECHO and MassGIS regulatory data into a unified PWSID entity database and delivered 800+ validated Day-1 acquisition targets within the engagement window.
2. Automated off-market deal sourcing by aggregating 2,500+ legal entities from EPA compliance databases and cross-referencing Google Maps API data to surface unlisted acquisition targets, eliminating 15 hours of manual prospecting per week for the fund's Principal.
3. Built a Review Velocity scoring algorithm that proxied fleet expansion and operational scale from public compliance data, filtering 800 acquisition targets down to a 280-lead qualified shortlist — a 35% precision rate against the fund's revenue criteria.
```

---

### Experience: Vylet

**Lane:** Founded venture with paying clients and closed-loop pipeline
metrics — the only titled experience carrying founder/owner signal:
external revenue, product ownership end-to-end, and a diagnosed/fixed
defect with a before/after number, not just architecture.

**Header:**

Vylet | May 2026 -- Present | {tech derived from selected bullets} vyletdata.com
Founder --- Automated lead-sourcing platform for PE/search-fund; live
product generating $1,500 MRR across three paying clients

**Bullet pool:**

1.  Launched Vylet, automating a ~30-minute manual process per business into a Dockerized LangGraph pipeline generating 30 scored leads in 30 minutes --- a 30x speedup --- with Redis/Celery workers on a recurring cycle.

2.  Diagnosed a name-collision defect in ownership-verification logic that
    was incorrectly rejecting valid acquisition targets sharing a name with
    an unrelated business elsewhere; the fix lifted the pipeline's lead-
    qualification rate from 79% to 89% with zero change to sourcing volume.

3.  Grew Vylet from 1 to 3 paying subscription clients within six weeks of
    launch — spanning workforce-software, landscaping, and geography-first
    sourcing engagements — generating $1,500 in monthly recurring revenue.

4.  Shipped a geography-first discovery mode decoupled from a pre-set
    vertical, surfacing ~30 leads/month in niche verticals — custard shops,
    bowling alleys — structurally invisible to vertical-first discovery.

5.  Engineered a LangSmith eval pipeline spanning 20 adversarial business
    test cases across 13 archetype labels — manufacturers, SaaS tools, PE
    holding companies, geographic mismatches — then layered deterministic
    Pydantic consensus gates to lift extraction faithfulness from 50% to 90%.

6.  Engineered Node 3 as a pure-Python triangulated consensus gate — no LLM
    calls — that computes a 0–100 lead score by fuzzy-matching the pipeline
    query, state business registry, and live website crawl in a three-way
    weakest-link check, then hard-fails leads on legal status, industry,
    geography, or independence before the score threshold applies.

7.  Architected a custom asyncpg Data Access Layer storing Gemini embeddings
    alongside source records; engineered injection-safe SQL timestamp
    validation that detects stale entries and triggers automatic
    re-scrapes, keeping the lead database fresh without manual
    intervention.

---

### Project: Granular Synthesizer Plugin

**Lane:** Hard real-time C++ systems and audio DSP. The only entry with JUCE, VST3/AU release binaries, lock-free SPSC UI-to-audio threading, custom slab memory pools, and granular synthesis at sample-rate precision — anchors low-latency/embedded-style systems depth the Python and web stack cannot carry.

**Header:**

```
Granular Synthesizer Plugin  |  {tech derived from selected bullets}    github.com/Verdent06/granular-synth
Real-time audio DSP plugin built from scratch in C++/JUCE — sine oscillator through full granular engine with lock-free threading and release-ready VST3/AU binaries
```

**Bullet pool:**

```
1. Enforced the audio thread's zero-allocation constraint by pre-allocating a MemoryPool<Grain, 64> slab per voice at plugin startup — a fixed free-list that acquires and releases grain slots without touching the heap — so processBlock() never calls new or delete after prepareToPlay() completes.
2. Wired UI-to-audio delivery through a hand-rolled SPSC FIFO (64-slot fixed array, atomic head/tail with acquire/release ordering) so slider changes reach the audio thread without a mutex — and routed WAV handoff via atomic shared_ptr swap so the UI thread never blocks processBlock().
3. Built the granular engine around a fractional-accumulator scheduler that fires grains at density × (1 - overlap × 0.5) effective rate — each grain reads a random WAV offset at 2^(semitones/12) playback speed, windowed by a pre-computed 8,192-entry Gaussian LUT to eliminate click artifacts at grain edges, with all grain memory drawn from a per-voice pre-allocated pool.
4. Implemented 16-voice polyphony with per-voice ADSR envelopes, pre-computing attack/decay/release rates as samples-per-step in prepareToPlay() to eliminate division inside the audio hot loop — and a voice-stealing algorithm that evicts the oldest active note by age counter when all 16 slots are busy, with each voice falling back to a sine oscillator until a WAV sample is loaded.
5. Implemented a global post-mix delay on a power-of-two ring buffer (2^17 = 131,072 samples, O(1) bitmask addressing) with per-sample delay time smoothing — the read head steps ±1 sample per block toward the target delay value — eliminating the zipper noise audible when a user adjusts the delay knob during live playback.
6. Configured CMake to compile VST3 and AU bundles from a single JUCE codebase — targeting a macOS universal binary (arm64 + x86_64) for native Apple Silicon and Intel — and audited every processBlock() path against a real-time safety checklist confirming zero heap allocations and zero lock acquisitions before release builds.
```

### Project: SignalWeaver

**Lane:** The only entry demonstrating actual model fine-tuning (not just
API/agentic orchestration like Vylet) — a real LoRA adaptation of an open-
weight LLM plus a statistically rigorous regression model, both validated
with proper held-out evaluation. Also the only entry that closes the
`pgvector` orphan in the Databases skills bucket, and the only single
project spanning all four stack layers end-to-end: FastAPI backend,
pgvector-based semantic search, a 5-node LangGraph agentic pipeline, and a
React/TypeScript frontend.

**Header:**

```
SignalWeaver  |  {tech derived from selected bullets}    github.com/Verdent06/SignalWeaver
SignalWeaver --- Multi-signal financial research platform combining
fundamentals, macro indicators, and news sentiment (research assistant;
not investment advice)
```

**GitHub:** [https://github.com/Verdent06/SignalWeaver](https://github.com/Verdent06/SignalWeaver)

**Bullet pool:**

<!--
  Metrics source: logs/metrics/metrics_2026-08-04.jsonl
  Clean batch = afternoon runs (ts >= 2026-08-04T17:26Z).
-->

1. Lifted financial-sentiment classification accuracy from 81% to 96% by
   LoRA fine-tuning a quantized meta-llama/Meta-Llama-3.1-8B-Instruct
   model on 3,454 Financial PhraseBank entries, evaluated on a held-out
   test set.

2. Built a linear regression combining fundamental, embedding-based
   sentiment, and LLM-derived sentiment signals into a composite return-
   prediction score; validated out-of-sample (3.39% R^2, consistent with
   the low single-digit R^2 typical of real return-prediction literature)
   to confirm the model wasn't just fitting noise.

3. Served composite financial-research scores through async REST endpoints
   (FastAPI) wrapping fundamentals, MPNet sentiment, and regression logic,
   instrumented end-to-end at 9.1s p50 / 15.2s p99 across 90 successful
   runs on 90 tickers.

4. Implemented semantic search over stored financial news with pgvector
   cosine similarity (768-d MPNet embeddings), hitting 49ms p50 / 99ms
   p99 over 90 queries returning top-5 or top-10 matches.

5. Orchestrated a 5-node LangGraph pipeline (fetch → classify → embed →
   score → explain) with per-node timing from the same 90-run batch:
   fetch 7.3s p50, classify 1.1s p50 (~29ms/article over 40-article
   batches), embed 1.1s p50, score under 1ms p50, explain 3ms p50 —
   fetch dominated wall time (~80% of p50 latency).

6. Built a React/TypeScript dashboard for composite scores and
   fundamental/sentiment/macro breakdowns; used it to analyze 90
   distinct tickers with scores persisted to Postgres for history views.

7. Containerized the stack with Docker Compose (API + Postgres/pgvector +
   nginx frontend) and a GitHub Actions CI pipeline (frontend build,
   pytest, API image build on main).

<!-- ### Project: MatchStream — Real-Time Robot Telemetry & Analytics Platform

**Lane:** Only entry demonstrating Java/Spring Boot backend engineering and a
relational database (PostgreSQL) — closes the Java/Spring/SQL gap nothing
else in the pool carries. High school (senior season), FRC Team 1234, core
member of a multi-person software subteam — not solo work; framing must
reflect team context, not sole ownership.

**Header:**

MatchStream --- Real-Time Robot Telemetry & Analytics Platform | FRC Team 548
Java, Spring Boot, WebSocket, PostgreSQL, React, WPILib

**Bullet pool:**

1. As a core member of FRC Team 548's software subteam, replaced post-match
   robot debugging with a Java/Spring Boot telemetry pipeline streaming live
   subsystem state to a React dashboard at 50Hz, under 45ms latency.

2. Built a NetworkTables4-based ingestion service sustaining 2,500 messages/sec
   under load testing with p99 processing latency under 8ms and zero data
   loss across 2 radio dropout events over 3 hours.

3. Ran a closed-loop tuning workflow on dashboard-captured telemetry, reducing
   autonomous path position error 64% (14cm to 5cm) and mechanism settling
   time 38% (1.7s to 1.05s) through iterative PID/feedforward tuning.

4. Wrote 52 JUnit tests across robot (WPILib simulation) and backend logic,
   integrated into a GitHub Actions CI pipeline running on every push.

5. Designed threshold-based anomaly detection that flagged 5 hardware issues
   across 10 practice sessions, including one motor pre-failure caught before
   it caused a match-critical stall. -->
