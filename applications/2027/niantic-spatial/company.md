# Niantic Spatial

Niantic Spatial builds physical-AI / geospatial foundation models and a Visual Positioning System (VPS) from a proprietary corpus of 30B+ posed images — reconstruct (meshes / Gaussian splats, including the open SPZ splat format), localize (centimeter-level positioning where GPS fails), and understand (spatial intelligence over 3D scenes). The company is the May 2025 geospatial-AI spinout of Niantic after Scopely bought the games business (Pokémon GO, etc.) for $3.5B; intern work sits on production mapping, product APIs, and high-throughput positioning services for robotics, public-sector, and industrial customers — not a Pokémon GO game intern and not a computer-vision research PhD seat.

## Quick Facts

- **Tier:** B (`reference/companies.md` B-TIER — Good / Solid Resume Addition; geospatial / physical-AI intern peer of Applied Intuition / Waymo brand-adjacency without A-tier intern prestige)
- **HQ / offices:** San Francisco, CA (One Ferry Building, Suite 200, 94111 on Form D). This intern is **San Francisco on-site, 4 days/week**, 12 weeks.
- **Valuation / signal:** Private. Day-one capitalization **$250M** ($200M Niantic + $50M Scopely) after the games sale (official Day One post, May 2025). SEC Form D (June 13, 2025): **$247,999,829** sold to 256 investors. No standalone post-money valuation published. Founder/CEO John Hanke. Public product claims: 30B+ posed images, 50M+ neural nets, 140+ patents.
- **Product focus:** Large Geospatial Model + VPS + reconstruction platform (Scaniverse / geospatial APIs) for robotics, defense/public sector, energy/industrial digital twins
- **Intern comp (2027 Software Engineering Intern):** **$48–$70/hr** (JD; skill/coursework assessed). Housing assistance for candidates outside the Bay Area (offer-stage). Lunch on-site.
- **Work model:** Paid Intern. **12 weeks**, Summer 2027. On-site SF **minimum 4 days/week**. Three apply-time tracks: **ML/AI Infrastructure**, **Product Engineering**, **Backend Systems** (match after apply; switching uncommon).
- **Clearance / eligibility:** Currently pursuing a **BS or MS** in CS, Robotics, EE, Systems Engineering, Computer Vision, or related. No printed GPA or class-year cap. No export-control / U.S.-person Boolean on the public Ashby form. Form knockouts: work authorization without restrictions; sponsorship now or later; SF 4x/week Boolean.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Knockouts | Ashby form | Work auth; sponsorship Boolean; SF 4x/week confirm; expected graduation (Month, Year); **primary track** select. Binary gates fire before a fair PDF read (`recruiting.md` Part I §1) |
| Resume screen | Ashby (scale-up; human reads the PDF earlier than OA-gated big-tech) | Generic SWE + track fit. Do not screen as a CV-research intern or a Pokémon-GO games intern |
| OA | **CoderByte ~60 min** **[directional, Summer 2026 intern reports]** | Timed; AI tools reportedly disallowed. Medium–hard DSA analog (strings / DP / arrays on older Niantic intern reports). Confirm platform if 2027 invite differs |
| Technical | **60-min live coding** after OA **[directional, 2026 intern]** | One of two post-OA interviews |
| Behavioral | **60-min** after OA **[directional, 2026 intern]** | Filter round (`recruiting.md` §6). Physical-world / spatial curiosity, independent debug, small-team communication (JD) |

**Estimated funnel:** Ashby resume + track pick → CoderByte OA → live coding + behavioral · Medium DSA · Bottleneck: **resume then OA** · ~3–8% **[directional, B-tier spatial/physical-AI intern peer]** (`reference/companies.md`)

## Stack & Hiring Signal

- **Languages:** JD or-list for Infrastructure and Backend tracks: **TypeScript, Python, C++ or Go**. Product Engineering copy is APIs / workflows / web+mobile, not a named language set. Do **not** invent Go, CUDA, Kubernetes, Terraform, Ray, Spark, COLMAP, OpenCV, NeRF, or Gaussian Splatting.
- **Domains:** Product APIs over spatial data; high-throughput VPS/reconstruction services (Go/C++); ML training infra (PyTorch, distributed GPU, petabyte ingest) — three intern tracks, one posting
- **What wins:** Shipped product/backend (REST APIs, upload/processing workflows, TypeScript or Python in bullets) **and** a systems or applied-ML signal in the top half so the page is memorable at a physical-AI company. Anti-patterns: notebook `model.fit()` as the lead for Product Engineering; invented CV/3D stack; Skills-only C++/Go; claiming the ML/AI Infra track without training-pipeline evidence.

## Sources

- Live JD / apply: https://jobs.ashbyhq.com/niantic-spatial/898b2da7-03cd-486e-96e3-3430a148c8fd
- Ashby GraphQL `ApiJobPosting` (`jobs.ashbyhq.com/api/non-user-graphql`; posting `898b2da7-03cd-486e-96e3-3430a148c8fd`; form id `f14c42ba-1836-44f3-a131-263517aec3b3`; published **2026-10-06**; `applicationDeadline` null; survey form present)
- Ashby job-board posting API: `api.ashbyhq.com/posting-api/job-board/niantic-spatial`
- `reference/companies.md` B-TIER Niantic Spatial row
- Company: https://www.nianticspatial.com/ · Day One: https://www.nianticspatial.com/en/blog/niantic-spatial-day-one
- Scopely games sale $3.5B (TechCrunch 2025-03-12): https://techcrunch.com/2025/03/12/pokemon-go-maker-niantic-is-selling-its-games-division-to-scopely-for-3-5b/
- Form D / HQ: https://altstreet.investments/edgar/2072158
- Summer 2026 intern OA reports **[directional]**: https://www.reddit.com/r/internships/comments/1rkmt9c/anyone_get_an_oa_or_interview_for_the_niantic/
- Older Niantic intern OA flavor **[directional]**: https://www.jointaro.com/interviews/companies/niantic/experiences/software-engineer-internship-united-states-april-1-2024-no-offer-positive-0505824e/
