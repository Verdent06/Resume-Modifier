# Software Engineer, Intern (2027) at Exa

## Verdict

- **Score:** 3.0 / 10 (7 weighted demerits — 0 emergency, 2 major, 1 minor)
- **Eligibility:** Eligible — `Expected May 2028` is a current student pursuing a degree in Computer Science, satisfying the "currently pursuing CS / Engineering / Physics or related technical field" gate. No visa sponsorship needed (Exa sponsors STEM OPT/OPT/H1B/O1/E3 regardless). The "willing to take a semester off to work full-time in SF" requirement is an apply-time personal commitment, not a paper knockout.
- **Track:** full-stack + search-infra / high-performance systems (track divergence)
- **Pipeline:** 2 graded cycle(s) · exit: writer_peak (final independent grade drew harsher than the 5.0 loop-exit — see First read)

## Screen Review

### First read

- The substance is a genuinely strong Exa fit: real from-scratch C++ high-performance systems (lock-free SPSC FIFO with acquire/release atomics, zero-allocation `MemoryPool<Grain,64>` in the audio hot path), measured sub-100ms vector retrieval (pgvector semantic search at 49ms p50 / 99ms p99), real embeddings + crawl/re-scrape (Vylet asyncpg + Gemini embeddings), and a shipped founder product with paying users — every hard requirement (a high-performance language, "codes hard projects for fun," "cares about finding high-quality information") is honestly evidenced.
- The binding structural ding: the two strongest Exa-specific proofs — the C++ lock-free systems work and the measured pgvector retrieval — live in **Projects at the bottom of the page**, because they are personal projects and `reference/resume.md` fixes Experience above Projects. The top half therefore leads with a Voice-AI co-op (CaseStudyPrep, real-time/on-device inference) and a founder lead-gen platform (Vylet), which a 7-second scan can bucket as generalist full-stack + AI-agent before reaching the systems/retrieval depth.
- This is an out-of-rails constraint, not a fixable defect: the candidate has **no C++/high-performance-language *experience*** to lead with (only the project), so the differentiator cannot be moved into the Experience-led top half without fabricating a role. The writer maximized the in-rails top-half systems read (led the resume with CaseStudyPrep's hard real-time sub-5ms / 60 FPS bullet; dropped the pure-generalist MDC entry; kept both differentiator projects deep and first-in-Projects).

### Demerits

- **major** · `Granular Synthesizer Plugin` · high-performance-systems depth buried below the fold — the only high-performance-language systems work (C++, zero-allocation memory pool, lock-free SPSC FIFO, real-time audio thread) sits in Projects at the bottom while the top half reads generalist, so a fast scan misses the systems signal Exa screens for. *(Out of rails: it is a project; section order fixes Projects below Experience; no C++ experience exists to lead with.)*
- **major** · `SignalWeaver` · on-domain retrieval-latency evidence below the fold — Exa's literal product is a sub-100ms billion-vector DB, but the only measured low-latency vector retrieval (49ms p50 / 99ms p99 pgvector) is a bottom-of-page project, so the strongest search-infra alignment never lands on the first pass. *(Out of rails: same section-order constraint; the retrieval proof is a project, and the top-half retrieval slice — Vylet embeddings — is unquantified plumbing by the pool's own wording.)*
- **minor** · `Granular Synthesizer Plugin` · metric-free — the most on-axis entry has deep architecture but no quantified performance number (latency, buffer throughput, allocation win), so a systems reader can't size the engineering. *(Out of rails: no Granular pool bullet carries a genuine impact metric — design/scale constants only; not fabricated.)*

### Misreads

- A scan-first triage can file this as a "voice-AI / AI-agent full-stack generalist" and pass before reaching the C++ lock-free and pgvector work below the fold — the exact systems + retrieval depth Exa hires for is the part most at risk of never being read.
- The top-half retrieval signal (Vylet Gemini embeddings + auto re-scrape) can read as "pipeline plumbing" rather than information-retrieval engineering, so a rushed reader may under-credit the on-domain crawl/embeddings fit.

### Interview angles

- **Lead with:** the C++ real-time systems story (hand-rolled lock-free SPSC FIFO with acquire/release ordering; zero-allocation `MemoryPool` so `processBlock()` never touches the heap) as the high-performance-language proof, then the pgvector semantic search at 49ms p50 / 99ms p99 as direct sub-100ms-retrieval alignment; frame Vylet's asyncpg + Gemini-embeddings + auto-re-scrape as real crawling/embeddings/IR work, and the shipped $1,500-MRR product + from-scratch synth as "codes hard things for fun."
- **Defend:** buried differentiator → open the conversation with the C++ lock-free/zero-allocation work and the pgvector latency, since the page ordering can't surface them first *(out of rails: differentiator lives in projects; section order fixes projects below experience; no C++ experience exists to lead with)*. Rust gap → C++ real-time/lock-free work is the transferable high-performance-language proof; ready to ramp on Rust *(out of rails: Rust absent from the pool, no swap bridge)*. Granular has no metric → narrate the real-time-safety guarantee (zero heap allocations, zero locks in the audio path) as the correctness/performance win *(out of rails: no Granular pool bullet carries an impact metric)*. Retrieval scale → be candid that pgvector was benchmarked at student scale (90 queries) and reason about how the primitives extend toward billion-vector, sub-100ms serving *(out of rails: no corpus/vector-count in the pool)*.
- **Depth prep:** lock-free data structures and memory ordering (acquire/release, SPSC), zero-allocation / real-time constraints; vector search internals (ANN indexes — HNSW/IVF, recall/latency trade-offs) to bridge from pgvector toward billion-vector serving; crawling/dedup/politeness and keyword-search/ranking fundamentals (inverted indexes, BM25) for Exa's core problems; be ready to walk through the C++ synth and SignalWeaver decision-by-decision.

## Likelihood

- **Resume screen:** Medium — the differentiator content genuinely exists and a human reading the full PDF at a small lab will find it, but it sits below the fold and a 7-second scan reads generalist, risking an early pass in fast triage.
- **Overall hire odds:** Medium — the binding filter is defensible technical depth, and the C++ concurrency plus measured IR-latency work would survive "walk me through it," alongside a shipped product with paying users and from-scratch hard projects that read as coding-for-fun. But this is a low-volume, high-bar, resume-first lab funnel where the differential is who gets read at all, so a buried differentiator plus no referral makes it easy to lose in triage rather than on merit.
- **Funnel filters:** Onsite San Francisco, full-time, semester-length commitment (willing to take a semester off); current-student / technical-degree gate (satisfied); sponsorship supported (not a knockout); resume-first, human-read, no high-volume OA gauntlet (`reference/companies.md` Exa brief) → practical/systems technical screen → hard systems + domain (search/crawling/vector-retrieval) loop.
- **Outside the resume:** Founder-direct or referral outreach into Exa converts far better than a cold PDF at a hot AI lab (`recruiting.md` §4–5); leverage the 1 UMich alum on staff; keep a live GitHub showcasing the from-scratch C++ systems work (Exa rewards "codes hard projects for fun"); apply within ~72h of the req opening (§8); and in outreach, articulate a genuine reason you care about high-quality-information retrieval.
