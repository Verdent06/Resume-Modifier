# Hermeus

Hermeus is a venture-backed defense aviation company that builds high-Mach unmanned aircraft through rapid hardware iteration rather than decade-scale prime programs. Flagship work is the Quarterhorse family (Mk 2.1 F-16-scale demonstrator; path toward Mach 3+ and hypersonic Mach-5-class platforms) for the Department of War. Software sits next to airframe: embedded flight software, 6DOF SITL simulation, HMI/C2, and hardware-in-the-loop test — this packet is the Los Angeles Modeling & Simulation intern (Julia 6DOF SITL), not the Atlanta HIL-bench sibling. `reference/companies.md` has no Hermeus row; nearest published peers are SpaceX / Shield AI / Anduril (defense aviation / autonomy, C++/Python systems) for brand pressure only — do not copy those firms' OA or round counts.

## Quick Facts

- **Tier:** Unrated (`reference/companies.md` has no Hermeus row)
- **HQ / offices:** El Segundo / Los Angeles area HQ (Series C, Apr 2026); internships page lists 3401 Jack Northrop Ave, Hawthorne, CA 90250. Atlanta remains a production hub. Intern terms also run in Atlanta, Washington, D.C., Jacksonville, and Los Angeles. This req: Los Angeles, on-site.
- **Valuation / signal:** $1B post-money after $350M Series C (Apr 2026; $200M equity led by Khosla Ventures + $150M debt); >$500M total capital; ~300 employees. Backers include Canaan, Founders Fund, RTX Ventures, In-Q-Tel. DIU high-Mach work and White Sands flight test are public mission signals, not intern-funnel data.
- **Product focus:** Unmanned high-speed / hypersonic aircraft (Quarterhorse); software team owns FSW, SITL simulation, HMI, and HIL used to control, test, and validate the airframe
- **Intern comp (2027 Software Engineering Intern, Modeling & Simulation):** $25–$33/hr (JD guideline; final by degree level). Firm also states hourly rates by academic level, overtime eligibility, monthly living stipend; no housing; relocation is a covered flight or gas reimbursement cap.
- **Work model:** Paid, on-site Los Angeles. Spring ~16 weeks (January–April); Summer ~12 weeks (May–August). Three intern terms per year.
- **Clearance / eligibility:** U.S. export control — must be a U.S. person (citizen, national, LPR, asylee/refugee granted) or eligible for deemed export licensing. JD: pursuing CS, AE, EE, Applied Math, or related; GPA 3.0+. No class-year gate on this JD (apply form asks junior-year completion; that is a form field, not a posting requirement).

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human + Lever ATS | Lever: parsed card first (`resume.md` ATS notes). Startup/defense-aviation: a human reads the PDF early (`recruiting.md` §1, §5). |
| Recruiter conversation | 20–30 min | Official internships FAQ. Work authorization / U.S. person, term (Spring vs Summer), mission fit. |
| Technical or role-based interview(s) | 30–60 min each | Official internships FAQ. Count unpublished. Do not assume a named OA platform — none is stated on the internships page or this JD. |
| Final team interview | 15–30 min | Official internships FAQ. Team match / hiring-team close. |
| Behavioral | Embedded in screens | Culture: first principles, cross-functional delivery, aviation mission. STAR is a field default (`recruiting.md` §6), not a Hermeus-published LP set. |

**Estimated funnel:** unpublished intern round count (official FAQ: recruiter + technical/role-based + final team) · LC/OA platform unpublished · no intern system-design published · Bottleneck: resume + technical/role interviews (Lever human-read; OA not documented) · acceptance unpublished (tiny defense-aviation cohort vs FAANG volume; do not borrow Anduril ~3–5% or SpaceX ~5–8% as if measured here)

## Stack & Hiring Signal

- **Languages:** This M&S intern JD: Julia, or scientific computing in Python, MATLAB, or C++. Company software surface (internships page / sibling reqs, not this JD): C++ on FSW/HMI; TypeScript/JS on some C2/HMI reqs. Do not treat Atlanta HIL-bench or Unreal as this LA SITL role's screen.
- **Domains:** 6DOF SITL, Monte Carlo scalability, physics-informed hardware models, flight-data validation, real-time sim performance, Flight Software / HMI / Flight Sciences interfaces
- **What wins:** A robotics/sim intern spine (`resume.md` Part III §15 / `recruiting.md` Part III §14) with Python and/or C++ shown in bullets (Julia only if actually used), plus visible real-time, numerical, or model-vs-measured-data discipline so the page is memorable for 6DOF SITL. Lever means the PDF carries front-end weight (`recruiting.md` §1). Skills-only Julia, HIL-rack framing copied from the Atlanta sibling, and consumer-SaaS pages with no systems/sim adjacency fail this screen.

## Sources

- JD: Software Engineering Intern (Modeling & Simulation) - Spring/Summer 2027 — https://jobs.lever.co/hermeus/445db430-6f81-41cf-847a-56a947afb936
- Official intern FAQ (eligibility, pay/stipend, housing, interview stages): https://www.hermeus.com/internships
- `reference/companies.md` — no Hermeus row; Unrated. SpaceX / Shield AI / Anduril cited only as nearest-peer brand context, not copied funnels
- `reference/recruiting.md` Part I §1 (Lever/Greenhouse human-read), Part II §8 (intern cycle), Part III §14 (robotics/autonomy/sim)
- Series C / HQ: https://www.hermeus.com/newsroom-content/series-c · https://techcrunch.com/2026/04/07/hermeus-raises-350m-to-build-unmanned-hypersonic-fighters/
