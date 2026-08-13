# Exa — Software Engineer, Intern · Written Application Answers

Draft answers to Exa's application prompts, grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented experience. Trim to each form's length limit before submitting.

---

## "Tell us about a technically difficult or interesting project you coded for fun."

I built a granular synthesizer audio plugin from scratch in C++/JUCE — a real-time DSP engine that shipped as VST3/AU binaries. The hard part is that the audio callback (`processBlock()`) runs on a real-time thread with a hard deadline and cannot allocate, lock, or block, or you get audible dropouts.

A few decisions I'm proud of:
- **Zero-allocation on the audio thread.** I pre-allocate a `MemoryPool<Grain, 64>` slab per voice at startup — a fixed free-list that acquires and releases grain slots without ever touching the heap — so after `prepareToPlay()` the audio path never calls `new`/`delete`.
- **Lock-free UI→audio handoff.** Slider changes reach the audio thread through a hand-rolled single-producer/single-consumer FIFO (fixed 64-slot array, atomic head/tail with acquire/release ordering) instead of a mutex, and I swap loaded WAV samples via an atomic `shared_ptr` swap so the UI thread never blocks the audio thread.

I built it because I wanted to actually understand real-time constraints and memory ordering rather than read about them, and I audited every `processBlock()` path against a real-time-safety checklist (zero allocations, zero locks) before cutting release builds. Code: github.com/Verdent06/granular-synth.

---

## "You care about the problem of finding high-quality information — why?"

Two of the things I've built are, at their core, retrieval and quality-of-information problems:

- **SignalWeaver** is a multi-signal financial research tool where I implemented semantic search over stored news with `pgvector` cosine similarity over 768-dimensional embeddings, benchmarked at 49ms p50 / 99ms p99. The interesting problem wasn't the model — it was making retrieval fast *and* trustworthy, so I paired it with held-out evaluation (e.g., a fine-tuned classifier lifted sentiment accuracy from 81% to 96%) rather than trusting raw output.
- **Vylet**, a lead-sourcing product I founded, is essentially a precision-of-information problem: I built a custom asyncpg data-access layer that stores embeddings alongside source records and triggers automatic re-scrapes when entries go stale, and I diagnosed a name-collision defect that was wrongly rejecting valid targets — the fix lifted qualification precision from 79% to 89%.

What draws me to Exa is that this is the whole product, at a scale I haven't touched: keyword search over ~10B pages, a crawler that adapts to any site, and sub-100ms retrieval over a billion vectors. I've built the primitives at student scale and want to work on them where correctness and latency are the entire job.

---

## "Are you willing to take a semester off to work full-time in San Francisco?"

Yes. I can be in San Francisco onsite full-time, and I'm open to taking a semester off to do it — I'd want to align the exact term with my University of Michigan academic plan, but the SF/onsite/full-time commitment itself is not a blocker. I do not require visa sponsorship.

---

## Notes for the applicant (not for submission)

- **Lead every conversation with the C++ real-time systems work and the pgvector latency** — those are the two things that map most directly to Exa's job, and on the resume they sit in Projects (below the fold), so make sure they surface early in any recruiter/founder conversation.
- **Be candid about scale.** pgvector was benchmarked at ~90 queries, not a billion vectors; if asked, reason about how the primitives extend (ANN indexes like HNSW/IVF, recall/latency trade-offs) rather than overclaiming.
- **Rust:** the JD lists C++/Rust; you have C++, not Rust. Don't claim Rust — position C++ lock-free/zero-allocation work as the transferable high-performance-language proof and note you're ready to ramp on Rust.
- **Referral > cold apply** at a small lab: there's 1 UMich alum on staff — a warm intro plus a live GitHub of the from-scratch systems work moves this far more than resume polish.
