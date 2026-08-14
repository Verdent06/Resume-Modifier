# 2027 Internship - Software Engineer at Virtu Financial

## Role Summary

Mentored SWE intern on a Virtu development team in New York or Austin. Interns take real development projects — design, develop, and optimize proprietary low-latency trading systems and algorithms, plus trading tools — and work with senior mentors to improve scalability, performance, and efficiency. The JD surface is generalist high-bar SWE: rising junior or FT-ready Dec 2027–June 2028, excellent CS/EE, Python **and** (Java or C++), quantitative problem-solving, comfort across frontend/backend and multiple languages. JavaScript and lower-level programming are pluses, not floors. The firm’s identity is electronic market-making on an in-house proprietary platform. This is the Software Engineer intern track only — not Quantitative Research/Strategist, Quantitative Trading, SRE, or Trading Operations.

## Track Decision

- **screen_track:** full-stack (general SWE — the JD requirements literally test Python + (Java or C++), CS/EE, DS&A for a HackerRank OA, and frontend/backend variety)
- **differentiator:** HFT / electronic market-making — proprietary low-latency trading systems (performance, scalability, massive data flow, lower-level programming)
- **track_divergence:** false — the differentiator is flavor on a general-SWE spine, not a second track. The screen still reads as general SWE (`reference/recruiting.md` III §11, `reference/resume.md` III §12); the systems/performance signal is what makes a candidate memorable here, not a re-target to ai-ml, robotics, or infra-only.

The spine is general SWE: ship real, defensible software; strong DS&A/CS fundamentals for a HackerRank Easy–Med OA; breadth across frontend/backend with depth in at least one layer. The differentiator is carried by whatever on-page work demonstrates real-time / low-latency / memory-discipline engineering — kept prominent and deep, but the resume does not become an ML-research or FPGA page.

## Team & Bar

Virtu is S-tier quant/HFT (`reference/companies.md`) — electronic market-making peer of IMC, Optiver, and HRT, with an OA-gated funnel (~1–2% intern acceptance). The screener is an engineer/recruiter at a firm where programming excellence and production discipline are floors. Funnel: resume screen → HackerRank OA (5Q / 75min, Easy–Med) → HR phone + brainteaser → 2–3 tech (project deep-dive, probability, low-latency systems). Comp is $5,000–$5,800 weekly plus housing/sign-on (JD exclusive of extras). What wins the human screen: Python and C++ proven in real systems work, not Skills-only; honest C++ + Python depth beats inventing Java; frontend/backend range; production shipping with metrics; genuine curiosity about how tech powers markets without fake desk experience. Class-year on page must show Expected May 2028 (rising junior; inside the rising-junior **or** FT-ready Dec 2027–June 2028 window). Prior finance is not required.

## Screen Criteria

- Python **and** C++ (or Java) proven in bullets — not Skills-only. The JD’s language floor is Python AND (Java or C++). Honest C++ + Python depth beats inventing Java.
- High-performance / low-latency **systems** depth surfaced on the page: real-time constraints, concurrency, lock-free or memory-discipline, latency/throughput, production correctness — the HFT-adjacent signal that separates this firm from a generic SWE screen.
- Frontend/backend range: the JD asks for comfort with a wide variety of projects (frontend/backend, multiple languages). Breadth should be real, not a skills-list dump.
- End-to-end ownership and production impact with metrics (latency, throughput, %, scale) — soft, metric-free claims read thin at this bar.
- Clean, well-architected systems the candidate can walk decision-by-decision; a live GitHub backing the claims.
- DS&A / CS fundamentals visible (coursework + engineered projects) for a HackerRank Easy–Med OA that still eliminates on time pressure.
- Quantitative problem-solving / mathematical aptitude visible enough to survive an HR brainteaser and later probability questions — stats/econ coursework or a rigorously evaluated data system, not finance-jargon padding.
- Class-year on page shows a current student who is a rising junior **or** FT-ready Dec 2027–June 2028 (Expected May 2028 is in window).

## Anti-Patterns

- Re-targeting to an ML-research / LoRA / agent-pipeline lead because a financial-research project exists — this is a general-SWE role at a trading firm.
- All-CRUD / all-web-app page with no systems-performance or production-reliability signal — reads generic and off-differentiator at a market maker.
- Java named in Skills with zero bullet evidence when the candidate cannot interview in it.
- Soft, metric-free shipping claims where latency/throughput/scale numbers are expected at a performance-obsessed firm.
- Finance-jargon padding with no engineering substance (prior finance is not required, and faking a trading-desk internship reads worse than honest strong CS).
- Thin single-bullet filler entries that dilute a strong systems + production spine.
- Treating this as a quantitative-trading, QR/Strategist, SRE, or Trading Ops internship instead of SWE.

## ATS Keywords

software engineer intern, Python, C++, Java, JavaScript, low-latency, trading systems, scalability, performance, efficiency, algorithms, quantitative, data structures, frontend, backend, proprietary technology, HackerRank, Austin, New York

---

## Application Form Answers (verbatim drafts)

Grounded only in context.md facts. No invented projects or metrics.

**Identity (Greenhouse profile)**

- **First name:** Vedant
- **Last name:** Desai
- **Email:** vedantde@umich.edu
- **Phone:** (248) 704-4852
- **LinkedIn:** https://linkedin.com/in/vedantde06
- **GitHub:** https://github.com/Verdent06
- **Resume/CV:** attach `Vedant Desai Resume.pdf` from this folder

### 1. Cover letter (optional)

I want to write software that has to be both fast and correct, and that actually ships. Virtu’s Software Engineer intern role is that job: proprietary low-latency trading systems and tools, scoped to real problems, with senior mentors who expect the work to improve scalability, performance, and efficiency. I am applying to this SWE track only — not Quantitative Research/Strategist, Quantitative Trading, SRE, or Trading Operations.

The work I already do sits on that axis. In C++, I built a granular synthesizer plugin in JUCE where `processBlock()` cannot allocate or take a lock — a per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO so the UI never blocks the audio thread — and I ship it as VST3/AU. In Python, I launched Vylet, a live lead-sourcing product ($1,500 MRR) on Docker/Redis/Celery, and I delivered a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract. I do not have a trading-desk internship. I do have CS + Economics at Michigan (Expected May 2028, GPA 3.66), I am a US citizen, and I built SignalWeaver as a financial-research assistant (not investment advice, not a trading desk) with measured p50/p99 on search and scoring.

I am available onsite in New York or Austin for the June 7–August 13 2027 program (free to travel). New York is my preference as HQ and a training-week hub; Austin is fully acceptable. I want to spend ten weeks next to engineers who treat microseconds and production correctness as the job.

*[Apply: https://boards.greenhouse.io/embed/job_app?token=8624410002]*

### 2. University

University of Michigan

### 3. GPA

3.66

### 4. Expected graduation year

2028

### 5. Will you be ready for full-time employment in 2028?

Yes. B.S. Computer Science and Economics, Expected May 2028.

### 6. Outstanding offers or deadlines?

No.

### 7. Office location preference (NYC or Austin only)

New York (also available for Austin).

### 8. How did you hear about this internship?

Jobright

### 9. Women's Winternship interest?

No

### 10. Sponsorship now or in the future?

No. US citizen.

### 11. Other tracks (QR/Strategist, Quant Trading, SRE, Trading Ops)

None — SWE only. Not genuinely aligned; do not select them.
