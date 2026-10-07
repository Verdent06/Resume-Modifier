# Everpure (Pure Storage)

Everpure is the former Pure Storage — an all-flash enterprise storage company that rebranded in February 2026 as it pushed from arrays into a broader data platform (FlashArray, FlashBlade, the Purity operating environment, Portworx, Pure Fusion / Enterprise Data Cloud). FY2026 closed at $3.7B revenue with a first billion-dollar quarter; the JD names hyperscalers, AI labs, and the AI hardware supply chain as the next-era customers. Interns sit in Santa Clara on a scoped project that is supposed to reach the core platform, not a throwaway intern sandbox. The hard language floor is C++.

## Quick Facts

- **Tier:** B-TIER (`reference/companies.md` — storage/systems peer to Western Digital / Qumulo; brand with NetApp)
- **HQ / offices:** Santa Clara, CA (HQ / this intern; Greenhouse office **Office - Santa Clara**)
- **Valuation / signal:** Public NYSE:**P** (ticker changed from PSTG April 17, 2026). FY2026 revenue **$3.7B** (+16% YoY); Q4 **$1.1B** (official Q4 FY26, ended Feb 1 2026). Rebrand announced Feb 23 2026; 1touch data-intelligence acquisition announced the same day
- **Product focus:** All-flash block/file/object storage + data-platform control plane (Purity, FlashArray, FlashBlade//EXA for AI/HPC)
- **Intern comp (2027 Software Engineer Intern):** **$8,500–$10,000/month** (~$49–$58/hr) on the Greenhouse pay band; housing assistance and/or travel bonus possible (Simplify **[directional]**). Levels.fyi Summer 2026 Santa Clara analog **$50/hr** + $9k housing + $500 relocation **[directional]**
- **Work model:** Paid full-time intern; **12 consecutive weeks** Summer 2027; **onsite Santa Clara** (in-office unless PTO / travel / approved leave)
- **Clearance / eligibility:** Current BS/MS/PhD in CS or related; graduation **on or after December 2027**. **C++ proficiency required.** Deemed-export form: sanctioned-nationality restriction (Syria, Cuba, Iran, North Korea, full BIS list) unless second nationality / PR in a non-sanctioned nation. US work-authorization and sponsorship Yes/No on the form. Posted **2026-10-06**; no application deadline (rolling until filled)

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Knockouts | Greenhouse form | Return-to-school (undergrad/grad/other/not returning); Santa Clara in-person Yes/No; work auth; sponsorship; deemed export; prior Everpure employment. Binary gates fire before a fair PDF read (`recruiting.md` Part I §1) |
| Resume screen | Greenhouse (human + ATS; LLM summaries **[directional, resume.md §2]**) | **C++ through use** is the floor; generic SWE shipping is the spine |
| OA | HackerRank **[directional]** | Intern analog: ~2 LC easy–med + MCQ / OS fill-ins (JoinTaro intern 2025; Glassdoor SWE). New-grad reports: 5 MCQ + 2 LC + a code-check **[directional, r/csMajors]** |
| Technical | DS&A + concurrency | FT / early-career analog: whiteboard algorithms (often custom/multi-part, not stock LC) plus locks / semaphores / races / deadlocks **[directional, r/purestorage / r/FAANGinterviewprep]**. Recruiter-facing early-career note: they do a lot of concurrency |
| Behavioral | Filter round (`recruiting.md` §6) | Ownership, mentor reporting, code-review hygiene — not the screen differentiator |

**Estimated funnel:** Greenhouse resume → HackerRank OA · Medium · light intern sys design unpublished · Bottleneck: **OA** after C++ resume screen · ~3–8% **[directional, B-tier peer WD / Qumulo]** (`reference/companies.md`)

## Stack & Hiring Signal

- **Languages:** **C++ is required**, not an or-list. Do **not** invent Java, Go, Rust, Linux, Purity, FlashArray internships, Kubernetes, Snowflake, Databricks, Copilot, or Fusion.
- **Domains:** Storage / data-platform software: performance, stability, tests, infrastructure tools on a core product used by global customers. Interns own a project through requirements, design, implementation, and unit/integration tests.
- **What wins:** C++ demonstrated in bullets (memory, lock-free / concurrency, hot-path discipline) **and** a shipped SWE spine (API, debug, tests, ownership). DS&A + concurrency fluency for the OA and later rounds. Anti-patterns: Skills-only C++; notebook ML as the lead; GTM/deal-flow filler; claiming a storage-engine or Purity internship the page cannot defend.

## Sources

- Live JD / apply: https://job-boards.greenhouse.io/purestorage/jobs/8249749
- Greenhouse questions API: https://boards-api.greenhouse.io/v1/boards/purestorage/jobs/8249749?questions=true (job id 8249749; req 18937; internal 3569242; first published 2026-10-06)
- `reference/companies.md` B-TIER Everpure (Pure Storage) row
- Rebrand + ticker: https://www.everpuredata.com/company/newsroom/press-releases/pure-storage-becomes-everpure.html ; https://www.everpuredata.com/company/newsroom/press-releases/everpure-to-change-ticker-symbol.html
- FY2026 results: https://www.sec.gov/Archives/edgar/data/1474432/000147443226000015/pstg-ex991q4fy2026.htm
- Comp analog: https://simplify.jobs/p/9a11053a-2a3f-4079-bfd4-8eea0e4acf53/Software-Engineer-Intern ; https://www.levels.fyi/internships/Pure-Storage/Software-Engineer-Intern/
- OA / loop **[directional]:** JoinTaro SWE intern 2025; Glassdoor Everpure SWE; r/csMajors Everpure OA; r/purestorage early-career tips
