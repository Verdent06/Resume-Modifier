# Fab2

Fab2 (formerly Atomic Semi) designs the hardware and software needed to make chips: complete fabrication facilities, tools, components, automation, and chip-design software, built largely in-house. The product identity is a software-defined “fab fab” — compact fabs whose operations are sequenced and controlled in software, with process-development data analyzed by the same stack — not a generic SaaS intern desk. Founded by Sam Zeloof (garage-fab chips) and Jim Keller (semiconductor architecture). `reference/companies.md` has no Fab2 / Atomic Semi row; nearest published peers for intern SWE signal are AMD (B-tier, semiconductor, B for SWE not chip engineering) and SpaceX (B-tier, C++/Python on hardware). Do not treat Keller/OpenAI-adjacent brand as S-tier.

## Quick Facts

- **Tier:** Unrated (`reference/companies.md` has no Fab2 row). Treat as B-tier hardware-startup intern signal, peer to AMD/SpaceX semiconductor/hardware — not an S-tier lottery ticket.
- **HQ / offices:** Austin, TX and San Francisco, CA (JD; this intern is in-office at those offices). Company also describes a Texas “fab fab” buildout and an SF garage-fab lineage; public square-footage claims are unverified — do not treat facility size as a hiring fact.
- **Valuation / signal:** Seed ~$15M led by OpenAI Startup Fund at ~$100M valuation (TechCrunch, Jan 2023, as Atomic Semi). Rebranded to Fab2 (Jul 2026) to underline the “factory that makes fabs” thesis. Early-stage; tiny cohort.
- **Product focus:** Software-defined semiconductor fabrication — frontend/backend apps, sequencing/control of fab operations, and data analysis for process development
- **Intern comp (2027 Fab Software Engineering Intern - Winter):** Software Interns paid hourly, annualized $114,000–$131,000 depending on experience and education, plus housing stipend (JD). Actual earnings vary with hours worked.
- **Work model:** Paid, in-office. Internship begins in January; preferred commitment 4 to 8 months. Philosophy: built and tested in days or weeks, not months. **Portfolio (GitHub OK) is required.**
- **Clearance / eligibility:** Export-control (US citizen / LPR / asylee-refugee). Work-auth and sponsorship questions on the form. Pursuing a BS in CS, CE, or demonstrated exceptional SWE skill. No class-year gate on the posting.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume + portfolio screen | Human + Ashby ATS | Startup funnel: a human reads the PDF early (`recruiting.md` Part I §1, §5). GitHub/portfolio is a hard apply requirement, not optional. Tiny intern class; resume + shipped-work proof is the front gate. |
| OA | None named | No standard intern OA platform in the JD or `companies.md`. Do not assume HackerRank/CodeSignal. Directional Atomic Semi-era reports emphasize project/architecture deep-dives over LeetCode puzzles. |
| Recruiter screen | Phone (directional) | Enrollment, January start / 4–8 month commitment, on-site Austin or SF, export-control / work auth, why-fab. |
| Tech | Project + systems (directional) | Walk-through of non-trivial software built from scratch; systems fundamentals (memory, performance, concurrency); TypeScript **or** Rust/Go path. Less LC-first than FAANG (`recruiting.md` startup practical loops). |
| Onsite / founders | Team + often founders (directional, Atomic Semi-era reports) | Hardware/process-engineer collaboration; mission fit; intern behavioral is a filter (`recruiting.md` §6). |

**Estimated funnel:** ~3–4 stages · practical/project-heavy rather than OA-gated · no named OA · no intern sys-design published · Bottleneck: Ashby resume + required GitHub/portfolio at a tiny early-stage cohort · acceptance unpublished (tighter than mid-size Greenhouse; do not invent an S-tier rate)

## Stack & Hiring Signal

- **Languages:** Rust and Go **or** TypeScript, plus a strong desire to learn (JD). This Fab intern seat is the TypeScript / full-stack path, not the separate Rust chip-design-tools intern req. Do not invent Rust or Go on the page.
- **Domains:** Frontend + backend data-driven apps to run the fab; sequencing and control of fab operations; databases, visualization, data processing pipelines; systems fundamentals (memory, performance, concurrency). Nice-to-haves (Figma, Blender, KiCad, Protobuf, CRDTs) are not floors — do not fabricate them.
- **What wins:** A full-stack intern spine (`resume.md` Part III §12 / `recruiting.md` Part III §11) with TypeScript shown through use, plus visible systems/concurrency/memory-performance and data-pipeline evidence so the page is memorable at a software-defined fab. Ashby + required GitHub means the PDF and the repo are the screen (`recruiting.md` §1, §5). Club-ops filler, Skills-only TypeScript, and a consumer-SaaS page with zero systems or control-adjacent depth fail here.

## Sources

- JD: Fab Software Engineering Intern - Winter — https://jobs.ashbyhq.com/fab2/0c4dc4f4-01c9-4138-a666-e7234cda7e95/application
- Built In posting (same req; intern comp and on-site offices) — https://builtin.com/job/fab-software-engineering-intern-winter/10905383
- `reference/companies.md` — no Fab2 row; AMD / SpaceX used only as nearest-peer B-tier semiconductor/hardware intern signal
- `reference/recruiting.md` Part I §1 (startup human-read funnels), Part I §5 (Greenhouse/Lever/Ashby-class startups), Part II §8 (intern eligibility/timing), Part III §11 (general SWE / full-stack)
- TechCrunch, 2023-01-10 (Atomic Semi seed ~$15M / ~$100M val, OpenAI Startup Fund) — https://techcrunch.com/2023/01/10/openai-in-talks-to-back-zeloof-and-chip-legend-kellers-startup-at-100-million-valuation/
- Tom's Hardware / WebProNews (Jul 2026 rebrand Atomic Semi → Fab2; Texas fab-fab thesis) — https://www.tomshardware.com/tech-industry/atomic-semi-rebrands-as-fab2-and-shifts-operations-to-texas
- Dataford Atomic Semi SWE guide (directional intern/full-time loop shape; project deep-dive over LC) — https://dataford.io/interview-guides/atomic-semi/software-engineer
