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
AWS (EC2, S3), Docker, Celery, Git
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
1. Eliminated the silent-audio problem in a voice-AI product — most frames sent to the Whisper backend were dead air — by running Silero VAD client-side via ONNX Runtime, filtering silence before upload and cutting cloud inference costs by 40%.
2. Eliminated a 27% audio upload failure rate by building fault-tolerant RxJS logic that detects expired S3 presigned URLs and regenerates them mid-flight, and handles MIME-type negotiation for raw WAV files that Angular's HTTP client rejected silently.
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

### Project: Autonomous B2B Deal-Sourcing Agent

**Lane:** Agentic product depth and commercial validation. The only entry that owns LangGraph + LangSmith eval CI/CD, Redis/Celery workers, asyncpg DAL with embeddings, a closed paid pilot, and 4 live PE acquisition theses delivered to real search fund and mid-market PE clients — flagship agentic-systems signal.

**Header:**

```
Autonomous B2B Deal-Sourcing Agent  |  {tech derived from selected bullets}    github.com/Verdent06/Lead-Gen-Agentic-Pipeline
Dockerized LangGraph pipeline for private equity acquisition sourcing — deployed across 4 live theses for search funds and mid-market PE clients
```

**Bullet pool:**

```
1. Packaged a Dockerized LangGraph execution pipeline as a recurring B2B lead-gen product, cold-approached and closed a paid pilot with a consulting firm, and deployed Redis/Celery workers to autonomously aggregate and deliver qualified leads on a scheduled basis.
2. Architected a custom asyncpg Data Access Layer storing OpenAI embeddings alongside source records; engineered injection-safe SQL timestamp validation that detects stale entries and triggers automatic re-scrapes, keeping the lead database fresh without manual intervention.
3. Engineered a LangSmith eval pipeline with 20 adversarial business archetypes — manufacturers, SaaS tools, PE holding companies, and geographic mismatches the LLM otherwise passed — then layered deterministic Pydantic consensus gates to lift extraction faithfulness from 50% to 90%.
4. Operationalized the pipeline for 4 live private equity acquisition theses — healthcare operators in California, HVAC distributors in Michigan and Ohio, landscaping companies in New Jersey, and environmental testing labs across the central US — each retargeted by editing thesis_config.yaml with zero code changes, and delivered qualified lead sets to search fund and middle-market PE clients after cold-email pitches.
5. Engineered Node 3 as a pure-Python triangulated consensus gate — no LLM calls — that computes a 0–100 lead score by fuzzy-matching the pipeline query, state business registry, and live website crawl in a three-way weakest-link check, then hard-fails leads on legal status, industry, geography, or independence before the score threshold applies.
6. Built Node 5 as a fully deterministic succession-risk scoring engine — no LLM calls — that infers PE acquisition readiness from heuristic signals (founder operating status, PE backing, website stagnation, years in operation) into a configurable weighted 0–100 composite, then enriches each passing company with Hunter.io contact data before CSV export.
```

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
2. Wired UI-to-audio parameter delivery through a hand-rolled SPSC FIFO (64-slot fixed array, std::atomic<int> head/tail with acquire/release ordering) so slider changes reach the audio thread without a mutex — and routed WAV file handoff through a separate atomic shared_ptr swap, letting the UI thread publish a new sample without ever blocking processBlock().
3. Built the granular engine around a fractional-accumulator scheduler that fires grains at density × (1 - overlap × 0.5) effective rate — each grain reads a random WAV offset at 2^(semitones/12) playback speed, windowed by a pre-computed 8,192-entry Gaussian LUT to eliminate click artifacts at grain edges, with all grain memory drawn from a per-voice pre-allocated pool.
4. Implemented 16-voice polyphony with per-voice ADSR envelopes, pre-computing attack/decay/release rates as samples-per-step in prepareToPlay() to eliminate division inside the audio hot loop — and a voice-stealing algorithm that evicts the oldest active note by age counter when all 16 slots are busy, with each voice falling back to a sine oscillator until a WAV sample is loaded.
5. Implemented a global post-mix delay on a power-of-two ring buffer (2^17 = 131,072 samples, O(1) bitmask addressing) with per-sample delay time smoothing — the read head steps ±1 sample per block toward the target delay value — eliminating the zipper noise audible when a user adjusts the delay knob during live playback.
6. Configured CMake to compile VST3 and AU plugin bundles from a single JUCE codebase — targeting a macOS universal binary (arm64 + x86_64) so the plugin runs natively on Apple Silicon and Intel — and audited every processBlock() code path against a real-time safety checklist confirming zero heap allocations and zero lock acquisitions before cutting release builds.
```
