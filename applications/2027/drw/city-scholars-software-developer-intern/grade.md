# Spring 2027 City Scholars Software Developer Intern at DRW

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** ineligible — form requires City Scholars at UIUC; candidate is UMich CS + Economics (Expected May 2028), not in that program
- **Track:** full-stack + market-data-infra / high-throughput trading systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC ingest (Requests + Pandas ETL, 400 PACs) plus a production Flask REST API on AWS EC2 is the closest analog to capture/catalog/serve. Granular lock-free C++ (SPSC FIFO, zero-allocation MemoryPool) is the systems/hot-path signal.
- Python and C++ are in bullets. SQL is in the Vylet asyncpg DAL. Expected May 2028 is on the page. No invented Java, FPGA, k8s, or UIUC enrollment.
- Binding dings on the PDF: Granular is unsized; CaseStudyPrep is a one-line Voice AI co-op. Binding ding on the *application* is the City Scholars form knockout — the resume does not fix that.

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — lock-free SPSC and MemoryPool never close with a latency, throughput, or xrun number a market-data team can size against 180B msgs/day
- **minor** · `CaseStudyPrep.AI` · single bullet — titled Voice AI co-op is one 5ms / 60 FPS line; the Experience stack still has a thin audio-ML co-op even after it moved below Vylet

### Misreads

- A rushed screen could bucket Granular as hobby audio DSP rather than trading-tech-adjacent real-time systems because the lead has no measured hot-path witness.
- CaseStudyPrep’s “Voice AI” title on a single bullet can misfile the bottom of Experience as a thin ML co-op if the reader skips the 5ms / 60 FPS hook.
- Vylet’s PE/search-fund founder tagline can look like GTM/agent product rather than a Docker/Redis/Celery + SQL pipeline.

### Interview angles

- **Lead with:** MDC ETL ingest + Flask/EC2 production API (capture → catalog → serve); Granular lock-free SPSC / zero-allocation `processBlock()`; Vylet Redis/Celery workers and injection-safe SQL; SignalWeaver pgvector 49ms p50 search; CaseStudyPrep sub-5ms / 60 FPS as the measured real-time number.
- **Defend:** Honest **No** on City Scholars / UIUC — do not invent membership *(out of rails: eligibility is a form knockout, not a resume bullet)*. Granular has no processBlock latency/CPU/xrun in the pool — narrate the real-time safety constraint and pivot measured latency to CaseStudyPrep / SignalWeaver *(out of rails: Granular hot-path timing — full 6-bullet pool is architecture/capacity/DSP/release-audit only)*. CaseStudyPrep stays one bullet — adding the RxJS 27% retry overflowed the page *(out of rails: second CaseStudyPrep bullet vs one-page budget; anti-deletion blocks cutting other iter-1 lines)*. No Java / FPGA / exchange-protocol decode. Interview in C++ or Python.
- **Depth prep:** Timed DS&A in C++ (preferred) or Python for the **in-person UIUC technical assessment** (Oct 14–16 2026) if they somehow bypass the membership knockout; remote is case-by-case. Walk MDC ingest/API and Granular threading/memory. Do not study as if this were a Codility OA unless DRW actually sends one — the live form names the campus assessment. Firm-wide SWE intern analog is Codility 3Q / ~150 min **[directional, not this req]**.

## Likelihood

- **Resume screen:** High — on-axis ingest + C++ systems; two minors dent polish. This assumes a City Scholars **Yes**. With **No**, Greenhouse never owes a human screen (`recruiting.md` Part I §1).
- **Overall hire odds:** Low — binary UIUC City Scholars knockout. Even a clean PDF does not open this seat for a Michigan junior.
- **Funnel filters:** Greenhouse **8220587** + transcript → **City Scholars / UIUC form knockout** → in-person UIUC tech assessment (Oct 14–16 2026; remote case-by-case) → unpublished remaining loop. Firm analog after resume: Codility + Zoom + Chicago onsite **[directional, not confirmed here]**. Chicago onsite semester · **$45/hr**.
- **Outside the resume:** Do not submit a **Yes** on City Scholars. Attach unofficial UMich transcript if you still apply. Form email **`verdent06@gmail.com`**. No DRW contact in `network.md`. Packet only — see `written-answers.md`. Never email this packet.
