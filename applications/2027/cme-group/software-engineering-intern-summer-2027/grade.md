# Software Engineering Internship - Summer 2027 at CME Group

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — pursuing B.S. Computer Science (Expected May 2028); JD requires current CS or related student with no class-year window; WayUp Summer 2027 form: graduating Summer 2027 is ineligible — May 2028 still enrolled after the term; US citizen clears no-sponsorship
- **Track:** full-stack + ultra-low-latency electronic trading / derivatives-marketplace infrastructure
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Granular leads with lock-free SPSC FIFO and a zero-allocation `processBlock()` MemoryPool — the ultra-low-latency / systems differentiator in the 30-second window. SignalWeaver follows with FastAPI REST, Docker Compose, and pytest CI on financial-research scores.
- Spine is Python shipping: MDC Flask REST on EC2 (~800 hours / 400 PACs), Vylet Dockerized pipeline + injection-safe SQL freshness, CaseStudyPrep sub-5ms / 60 FPS. GPA 3.66, Expected May 2028, live GitHub. No invented Java, GCP, Kubernetes, or Globex.
- Binding dings: Granular never lands a sized latency/xrun number, and CaseStudyPrep is a one-line Voice AI co-op.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC FIFO and zero-allocation MemoryPool never close with a latency, throughput, or xrun number an exchange screen can size.
- **minor** · `CaseStudyPrep.AI` · single bullet — titled Voice AI co-op is one 5ms / 60 FPS line; the role looks thinner than the title at a shop that wants prior technical experience.

### Misreads

- A rushed CME screener could bucket Granular as hobby audio DSP rather than exchange-adjacent real-time systems because the lead has no measured hot-path witness.
- CaseStudyPrep’s “Voice AI” title on a single bullet can misfile Experience as a thin ML co-op if the reader skips the 5ms / 60 FPS hook and the Flask/SQL spine.

### Interview angles

- **Lead with:** Granular lock-free SPSC / zero-allocation MemoryPool / `processBlock()` constraints; SignalWeaver FastAPI REST + Docker Compose + pytest CI; MDC Pandas ETL + production Flask/EC2; Vylet injection-safe SQL + Dockerized pipeline; CaseStudyPrep sub-5ms / 60 FPS as the measured real-time number.
- **Defend:** Granular has no processBlock latency/CPU/xrun in the pool — narrate the real-time safety constraint (no heap, no mutex on the audio thread) and pivot measured latency to CaseStudyPrep / SignalWeaver 9.1s p50 scoring *(out of rails: Granular hot-path timing — full 6-bullet pool is architecture/capacity/DSP/release-audit only)*. CaseStudyPrep stays one bullet — adding the 27% S3 retry overflowed the page *(out of rails: second CaseStudyPrep bullet vs one-page budget; anti-deletion blocks cutting other iter-1 lines)*. No Java — JD is Java **and/or** Python; interview in Python. Do not claim GCP, Kubernetes, Maven, IntelliJ, or a Globex internship. Linux is bonus; it is not on the page as a skill line.
- **Depth prep:** Timed Python DS&A until an Easy–Med is a ~20-minute solve (OA vendor unpublished; LC-easy analog **[directional]**). Walk Flask REST (MDC), FastAPI + pytest CI (SignalWeaver), asyncpg SQL freshness (Vylet), and Granular threading/memory. Virtual loop adds coding, design, and behavioral (JD). STAR for ownership, a named production defect, and continuous learning.

## Likelihood

- **Resume screen:** High — Python, REST, SQL, Docker, and pytest are through use; C++ real-time systems lead; class year and GPA clear the intern window; two minors dent polish, they do not flip the screen.
- **Overall hire odds:** Medium — B-tier exchange intern (~5–8% **[directional, peer Interactive Brokers / Deutsche Bank TDI]**). The resume should buy the coding pre-assessment; the OA then virtual coding/design/behavioral are the binding filters. Intern pay is C-band ($21.68–$36.10/hr).
- **Funnel filters:** Workday `cme_careers` req **34821** resume → coding pre-assessment (vendor unpublished) → virtual coding, design, and behavioral (JD) · Chicago hybrid 10–12 weeks · no sponsorship (CPT/H1B/F1/L) · posted 2026-09-18.
- **Outside the resume:** Apply in this first-wave window (tech reqs historically live ~4–5 weeks **[directional]**). Drill timed Python the week of apply. No CME contact in `network.md` — do not claim a referral. This is **not** Year-Long **34831** and **not** Fellowship **34824**.
