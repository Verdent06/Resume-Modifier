# GlobalFoundries

GlobalFoundries (Nasdaq: **GFS**) is a specialty foundry that manufactures essential semiconductors for AI, automotive, industrial, and communications customers — power-efficient process technology rather than a consumer GPU brand. HQ is Malta, NY (Fab 8); US manufacturing also includes Burlington, VT (Fab 9). FY2025 revenue was **$6.791B**. In 2025 GF acquired **MIPS** (RISC-V processor IP; continues as a standalone business inside GF); in June 2026 it closed Synopsys’ ARC Processor IP business and folded it into MIPS. This intern seat is **not** a fab process or RTL role: Workday hiring org is **MIPS Holding Inc**, and the work is a software performance-tuning application for MIPS RISC-V microprocessors (front-end workflows, back-end simulation concepts, data visualization). There is **no** `reference/companies.md` row — treat GF as **Unrated**; do not import AMD/Intel/Marvell as GF’s tier.

## Quick Facts

- **Tier:** Unrated (no `reference/companies.md` row). Semiconductor SWE intern peers in B-TIER (AMD, Intel, Marvell) are directional only — do not assign GF their tier
- **HQ / offices:** Malta, NY HQ (400 Stonebreak Road Extension, 12020). This intern: **Austin, TX** and **Santa Clara, CA**. Official US intern sites also include Burlington and Richardson
- **Valuation / signal:** Public (Nasdaq: **GFS**). FY2025 revenue **$6.791B**; Q2 FY2026 revenue **$1.786B**. MIPS RISC-V IP (2025) + Synopsys ARC Processor IP (closed Jun 2026). CHIPS Act ITC at Fab 8 / Fab 9
- **Product focus:** Specialty foundry silicon plus MIPS/ARC RISC-V processor IP and software tools — this req is the MIPS performance-tuning **application**, not a fab-tool or process-engineer intern
- **Intern comp (2027 Software Engineering Intern, JR-2604039):** **$20–$40/hr** (JD Expected Salary Range)
- **Work model:** Paid full-time intern (**≥40 hrs/week**); Summer 2027; Austin, TX or Santa Clara, CA. Official US intern program is typically **10–12 weeks**; housing stipend for eligible relocators (`gf.com` early-career FAQ). Mentorship, growth-scoped assignments, professional development, executive networking
- **Clearance / eligibility:** At least a **sophomore at time of application**; actively pursuing BS or MS in CS, CE, EE, Software Engineering, or related through an accredited program **during** the internship; overall GPA **≥ 3.0** and good standing; English written & verbal; **≥40 hours/week**. No clearance named on this JD. US citizen / LPR not printed as a knockout. Workday `canApply: true`; posted **2026-10-09** (`postedOn` Posted Today)

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Workday (`globalfoundries.wd1` / `External`); `includeResumeParsing: true` | Recruiter/HM screen. First-wave apply (`recruiting.md` Part II §8); GF targets US intern fills by **end of December**. Posted **2026-10-09** |
| OA | Unpublished for this **US** intern | Official FAQ: some roles add “an assessment test.” India campus loops start with an OA — **do not** copy that onto this US/MIPS req. Do **not** invent HackerRank/CodeSignal |
| Recruiter / HM | ~30-minute online or telephone interview (official FAQ) | Enrollment, sophomore+ / GPA 3.0, 40 hrs/week, Austin or Santa Clara relocate, why MIPS performance-tuning software (not fab process) |
| Follow-up | Some roles add team interviews | Project walk + programming fundamentals; preferred interest in developer tools, data viz, computer architecture, RISC-V, simulation, performance tuning, compilers, OS, or low-level systems |
| Behavioral | Filter round (`recruiting.md` §6) | Communication, planning, navigating ambiguity, AI-tools-for-productivity (not ML research). Feedback usually within **2–3 weeks** (official FAQ) |

**Estimated funnel:** Workday resume → recruiter/HM ~30-min interview · possible team follow-up or unpublished assessment · intern OA unpublished for this US req · No intern sys design published · Bottleneck: **resume** (Unrated; first-wave Workday; official US fill-by-December) · acceptance unpublished — do not invent a % from AMD/Intel/Marvell peers

## Stack & Hiring Signal

- **Languages:** JD names **no** programming languages. Do not invent Python, C++, Java, RISC-V assembly, or firmware as requirements. Honest inventory languages that may appear through use: Python, TypeScript, C++, SQL, HTML/CSS
- **Domains:** Application development, tests/automation/tooling, front-end workflows, data visualization, debugging, documentation, code review. Company/role identity is semiconductor + MIPS RISC-V performance-tuning / simulation / low-level / compilers/OS **interest** — not a fab process intern, not an RTL/firmware intern, not ML research
- **What wins:** Because the US intern FAQ has no named OA, the PDF is the gate (`recruiting.md` intern funnel; Workday human + parse). A one-pager that shows shipped general SWE (features, tests, tooling, front-end/viz) **and** systems / performance / real-time C++ discipline as the honest low-level analog — without claiming RISC-V, MIPS ISA, compiler, or firmware experience the page cannot defend. Preferred: prior internship, leadership, AI tools for productivity (not training/research). Do not invent RISC-V, MIPS, compilers, firmware, CUDA, or MatchStream

## Sources

- Live Workday posting (authoritative, captured 2026-10-10): https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---Texas---Austin/Software-Engineering-Intern--Summer-2027-_JR-2604039 — jobReqId **JR-2604039**; jobPostingInfo.id `6b0fd4abd03110020211d88afdc80000`; hiringOrganization **MIPS Holding Inc**
- GF early-career FAQ (US intern eligibility, 10–12 weeks, housing stipend, recruiter/HM ~30-min interview, fill-by-December): https://gf.com/careers/early-career/
- FY2025 results (revenue $6.791B; MIPS; proposed ARC deal): https://investors.gf.com/news-releases/news-release-details/globalfoundries-reports-fourth-quarter-2025-and-fiscal-year-2025
- Q2 FY2026 results (revenue $1.786B; ARC close Jun 2026): https://investors.gf.com/news-releases/news-release-details/globalfoundries-reports-second-quarter-2026-financial-results
- GF completes Synopsys ARC Processor IP acquisition (2026-06-02): https://gf.com/gf-news/globalfoundries-completes-acquisition-of-synopsys-processor-ip-solutions-business-delivering-a-holistic-technology-platform-for-physical-ai/
- Form 20-F YE2025 (Malta HQ address): https://www.sec.gov/Archives/edgar/data/1709048/000170904826000022/gfs-20251231.htm
- `reference/companies.md` — **no GlobalFoundries row** (Unrated). B-TIER AMD / Intel / Marvell rows are semiconductor SWE peers only, not GF’s tier
- `reference/recruiting.md` Part I §1 (knockouts / Workday), Part II §8 (intern first-wave), Part III §11 (general SWE)
