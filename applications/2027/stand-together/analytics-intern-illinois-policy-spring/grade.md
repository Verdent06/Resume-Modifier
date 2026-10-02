# KIP Spring 2027 - Analytics Intern - Illinois Policy Institute at Stand Together

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — B.S. Computer Science and Economics, Expected May 2028 (enrolled junior for Spring 2027); US citizen; geographically in the US; 18+
- **Track:** ai-ml + policy/nonprofit analytics (Illinois Policy Institute / KIP)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and a Flask REST API on AWS EC2 for Michigan Campaign Finance Network — nonprofit researcher analog, not generic SWE and not ML-research.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision) is the public-data scoring analog; Vylet leads with a 79→89% data-quality catch, then SQL freshness/validation.
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL timestamp-validation bullet is the only on-page SQL-through-use proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact.

### Misreads

- A keyword-first pass for matplotlib / seaborn / plotly / ggplot2 / R can bucket this as "no viz stack" even though a React dashboard, PAC rankings, and operational scoring are on the page.
- The SQL/DAL line can read as database plumbing rather than analytics-language proof, because it never sizes the freshness win.
- Vylet's PE/search-fund founder tagline can file as a generic agentic product if the reader never reaches the 79→89% quality line.
- Flask on EC2 can be mistaken for a SWE intern spine if the reader skips the ETL / ranking / nonprofit-research workflow.

### Interview angles

- **Lead with:** MDC Excel-export ETL and PAC rankings as the stakeholder KPI/report analog; Lyndbrook Review Velocity as public-data scoring; Vylet 79→89% quality catch plus SQL freshness; SignalWeaver React dashboard as the matplotlib/plotly analog
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it for the Docker 30x line underfilled the page)*. No R, ggplot2, matplotlib, seaborn, or plotly — say you will ramp; do not invent them. No Illinois policy internship — analog is campaign-finance research for MCFN, not IPI statutes. This is the Analytics Intern, not the IPI Policy Intern. Spring 2027 while enrolled at Michigan: **Part Time** (24h/wk), not Chicago 5-day onsite.
- **Depth prep:** Lever human screen → STF short-answer email → matching call → IPI interview (Python/messy-data walk + report) → partner offer → STF admissions interview (`company.md`). No standard LC OA. Walk one ingest → ranking path (MDC) and one quality path (Vylet). Behavioral/mission is a filter (`recruiting.md` §6). Confirm Thursday 1–4pm ET and Arlington summit Feb 3–6, 2027.

## Likelihood

- **Resume screen:** High — Python through use, Pandas ETL, PAC rankings as a KPI analog, Review Velocity precision, a React dashboard, AWS EC2, and a named data-quality fix all register in one pass; GPA 3.66 and econ coursework clear the intern analytics bar
- **Overall hire odds:** Medium — C-tier ~15–25% with resume + mission/behavioral fit as the bottleneck (`companies.md`); the page clears the analytics screen, then KIP programming + Chicago hybrid vs Ann Arbor enrollment + STF values interview still eliminate
- **Funnel filters:** Lever **`2d8f9d0f-9218-4936-8f39-dfb729db830b`** + human resume screen; official STF process then short-answer email, matching call, IPI interview, partner offer, STF admissions interview. HireVue reported on some KIP loops **[directional]**. Bottleneck: resume + mission fit. Visa: US citizen (cleared). Hybrid Chicago. Rolling through December 2026.
- **Outside the resume:** Apply 2026-10-02. No Stand Together / IPI contact in `network.md`. Do not write a liberty-keyword essay the page cannot support. Optional later short-answers only (not on the live Lever form).
