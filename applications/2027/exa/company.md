# Exa

Exa (formerly Metaphor) is an applied AI lab building a web-scale search engine designed for AI systems rather than humans — a neural/semantic search API over billions of pages, plus keyword search, a proprietary crawler, and an in-house vector database. The engineering problem is squarely infrastructure-and-performance: recreating Google-class keyword search over ~10 billion pages, building a crawler that adapts to any website, and serving a custom vector database over a billion vectors in under 100ms. It is a small, systems-heavy team where individual interns are handed load-bearing, hard problems, and where fluency in a high-performance language (C++/Rust) and a genuine obsession with finding high-quality information are the core hiring signals.

## Quick Facts

- **Tier:** Unrated (not in `reference/companies.md`) — reference-class: white-hot applied-AI-lab / search-infra startup, comparable in signal to the AI-lab and search-infra names in A-tier.
- **HQ / offices:** San Francisco, CA (onsite).
- **Valuation / signal:** Founded 2021; 51–200 employees; ~$357M raised; unicorn-scale. H1B sponsor. 1 University of Michigan alum on staff.
- **Product focus:** Web-scale search for AI — neural + keyword search API, proprietary web crawler, custom billion-vector database (<100ms retrieval).
- **Intern comp (2027 SWE):** $100K–150K/yr annualized (per JD).
- **Work model:** Paid, onsite in San Francisco, full-time. JD requires willingness to take a semester off to work full-time in SF — this is a semester-length commitment, not a standard summer term.
- **Clearance / eligibility:** Must be currently pursuing a degree in Computer Science, Engineering, Physics, or a related technical field. International candidates supported (STEM OPT, OPT, H1B, O1, E3) — sponsorship is not a knockout.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human-first (small startup / applied-AI lab) — a person reads the PDF early | Systems depth and "codes hard things for fun" register faster than keyword breadth |
| Technical screen | Practical coding, high-performance-language flavored | Expect C++/systems reasoning, performance thinking, and project deep-dives |
| Onsite / loop | Hard systems + domain rounds (search, crawling, vector retrieval, low-latency) | Ability to narrate real engineering trade-offs decision-by-decision is the bar |

**Estimated funnel:** ~3–4 rounds · Med–Hard, systems-flavored · No standard high-volume OA (startup/lab; human reads PDF early) · Systems design likely · Bottleneck: resume screen + technical depth · Acceptance: low (small team, hard bar) — no published rate.

## Stack & Hiring Signal

- **Languages:** High-performance systems languages are the requirement — C++, Rust (or similar). Python is common glue in AI-lab codebases; the JD names a high-performance language as the hard filter.
- **Domains:** Web-scale search infrastructure, crawling, information retrieval, vector databases / embeddings, low-latency serving, distributed systems.
- **What wins:** Demonstrated high-performance-language depth (real C++/systems work with memory/concurrency/latency reasoning), a track record of building technically difficult projects for their own sake, and evidence of caring about retrieval / high-quality information (semantic search, embeddings, crawling, ranking). Per `reference/recruiting.md` (startups + AI labs): a human reads the PDF early, founder-direct and referral outreach move the needle, and a practical eng bar plus defensible systems decisions beat brand padding.

## Sources

- JD (Jobright): https://jobright.ai/jobs/info/6a7d6d187c52154b59f5e898
- `reference/recruiting.md` (Part I §5 startup funnel; Part III §11 general-SWE / systems bar; Part II §8 intern eligibility gates)
- JD-provided facts: founded 2021, 51–200 employees, $357M raised, H1B sponsor, applied AI lab / web-scale search
