# Qumulo

Qumulo is a Seattle software-defined unstructured-data platform: a distributed storage operating system in C and Rust that holds exabytes in the datacenter, at the edge, and natively in the cloud. The core is a userspace storage stack — a fault-tolerant erasure-coded block layer under a transactional file system whose aggregates roll up so queries across billions of files do not walk a tree — plus quotas, snapshots, multi-protocol access, replication, and backup. That is a distributed operating-system problem (scheduling, memory hierarchy, protection, concurrency), not a consumer web product. Founded 2012 by Isilon Systems alumni; JD scale is 1,100+ customers and exabytes under management.

## Quick Facts

- **Tier:** B-TIER (`reference/companies.md` — storage/systems peer to Western Digital; brand below NetApp/Pure)
- **HQ / offices:** Seattle, WA — 1501 4th Ave #1600, 98101. This intern is **hybrid downtown Seattle HQ**, targeting **3 days/week** in-office. 2026 Cork, Ireland R&D/customer-success hub (GeekWire).
- **Valuation / signal:** Private. **$351M** raised; last published round **$125M Series E (Jul 2020)** led by BlackRock at **$1.2–$1.25B** **[directional, last published round]**. GeekWire 2022: path-to-profitability layoffs. CEO Douglas Gourlay.
- **Product focus:** Unstructured file + object storage across core / edge / public cloud (AI/HPC, PACS imaging, media render, genomics, Splunk, surveillance)
- **Intern comp (2027 Software Development Engineer Intern):** **USD $100,000** annual base, prorated **$1,900/week**, plus relocation, travel, and local transit as applicable (Ashby JD)
- **Work model:** Paid full-time intern; **Winter, Spring, or Summer 2027**; hybrid Seattle HQ (~3 days/week). Core product work, not a siloed intern project
- **Clearance / eligibility:** Pursuing BS/BA CS or Computer Engineering (or equivalent). Must reside in Seattle for the term. **Authorized to work in the US; unable to provide visa sponsorship or transfer.** No class-year cap beyond current-student + 2027 intern term. Posted **2026-09-21**; no applicationDeadline on Ashby.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Knockouts | Ashby form | Sponsorship Boolean; Seattle residency for the term; US work auth. Binary gates fire before a fair PDF read (`recruiting.md` Part I §1) |
| Resume screen | Ashby (scale-up; human reads the PDF earlier than OA-gated big-tech) | C++ or Python through use; concurrent/OS/DB *concepts* in bullets; not Skills-only Rust/C |
| OA | None named on this intern req | Unpublished intern loop. Keep Medium C++/Python DS&A warm |
| Technical | Unpublished intern loop | FT SDE analog: 60-min live HackerRank coding then a same-day coding + systems + behavioral block **[directional, Zero G Talent / FT, not this intern]** |
| Behavioral | Filter round (`recruiting.md` §6) | Correctness, pair/code-review, debug; not the differentiator |

**Estimated funnel:** Ashby resume → unpublished intern loop · Medium C++/Python DS&A · no named intern OA · light intern sys design unpublished · Bottleneck: **resume** then tech · ~5–8% **[directional, peer WD / VMware-Broadcom storage]** (`reference/companies.md`)

## Stack & Hiring Signal

- **Languages:** Feature work in **C, Rust, and Python**. Floor: at least one class, internship, or personal project in **C, C++, Rust, Java, or Go**. Screen for languages the candidate actually has — **C++ and Python through use**. Do **not** invent Rust, C-as-distinct-from-C++, Java, Go, Linux, Snowflake, Databricks, Copilot, Fusion, or Tableau.
- **Domains:** Distributed storage OS (userspace): concurrent programming, memory hierarchy, protection, scheduling; file/object protocols; correctness under failure. Intern sits on core product, not a toy intern stack.
- **What wins:** C++ systems evidence (memory, lock-free/concurrency, real-time or hot-path discipline) **and** a shipped Python/full-stack spine (API, test/debug, production ownership). DS&A fluency for the unpublished coding loop. Anti-patterns: notebook ML as the lead; club-ops; invented Rust/C/Java/Go; a PE/GTM product story that buries concurrency and C++.

## Sources

- Live JD / apply: https://jobs.ashbyhq.com/qumulo/43855947-3a85-4d1c-8b8e-e0c0ddcaf183
- Ashby GraphQL `ApiJobPosting` (`jobs.ashbyhq.com/api/non-user-graphql`; posting `43855947-3a85-4d1c-8b8e-e0c0ddcaf183`; form id `5c1b6406-d0fc-42ec-a5e2-53ab76584f54`; source form `508c2c27-e546-4c15-9f2a-0f67b1737639`)
- `reference/companies.md` B-TIER Qumulo row
- GeekWire Cork hub (2026): https://www.geekwire.com/2026/seattle-data-storage-company-putting-rd-hub-in-ireland/
- Crunchbase / company Series E: BlackRock-led $125M, ~$1.2B val (2020)
- FT interview analog **[directional]**: https://zerogtalent.com/blog/inside-qumulo-s-hiring-boom-what-it-takes-to-pass-the-28-role-screening-process
