# Analytics Intern at Electronic Arts

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is after the JD floor (graduate no earlier than December 2027); enrolled Summer 2027; US citizen, no sponsorship
- **Track:** ai-ml + EA SPORTS gameplay / player-behavior analytics (Madden NFL / College Football; retention and engagement)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN stakeholder delivery — designer/PM readout analog, not SWE and not ML-research.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision on operational scale) is the retention/engagement scoring analog in the lead window; SignalWeaver is out-of-sample regression + a React dashboard.
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL timestamp-validation bullet is the only on-page SQL-through-use proof the JD treats as a floor, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized freshness or query impact.

### Misreads

- A keyword-first pass for R / Tableau / Madden telemetry can bucket this as "no sports-analytics stack" even though PAC rankings, Review Velocity, a held-out regression, and a React dashboard are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- Vylet's PE/search-fund founder tagline can file as a generic agentic product if the reader never reaches the 79→89% quality line and the SQL DAL.

### Interview angles

- **Lead with:** MDC Excel-export ETL and PAC rankings as the stakeholder KPI/report analog for Analysts/PMs/Game Designers; Lyndbrook Review Velocity (800 → 280, 35% precision) as the "behaviors associated with retention/engagement" scoring analog; SignalWeaver out-of-sample 3.39% R² + React dashboard if they ask for modeling or viz; Vylet 79→89% + SQL freshness if they ask for data quality or SQL
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use)*. No R, Tableau, Snowflake, Databricks, Copilot, Fusion, or Madden/CFB internships — say you will ramp; do not invent them *(out of rails: those tools/domains are not in inventory or swap sets)*. No sports-sim work — analog is campaign-finance / search-fund behavioral scoring, not EA gameplay telemetry. This is the Orlando Analytics Intern (216252), not a SWE intern and not EA SPORTS Academy.
- **Depth prep:** Avature resume → Next-Gen Talent recruiter (Orlando hybrid, remaining-term, no sponsorship) → unpublished analytics walk (SQL/Python/stats + one project from problem → finding). Do **not** assume the SWE HackerRank (`company.md`). STAR for translating a scored finding to a designer. Confirm 12-week Summer 2027 hybrid Orlando. Behavioral is a filter (`recruiting.md` §6). Honest gaming-interest answer — do not invent a Madden rank.

## Likelihood

- **Resume screen:** High — Python/SQL through use, Pandas ETL, PAC rankings, Review Velocity precision, out-of-sample regression, and a React dashboard all register in one pass; GPA 3.66, stats/econ coursework, and Expected May 2028 clear the intern analytics bar
- **Overall hire odds:** Medium — B-tier ~8–12% with resume then recruiter/HM as the gate (`companies.md`); the page clears the applied-analytics screen, then Orlando relocate, unpublished SQL/Python walk, and missing on-page sports-sim work still eliminate
- **Funnel filters:** Avature Role ID **216252** + human resume screen; **do not assume SWE HackerRank**; recruiter then HM/culture-fit (`company.md` / Extern **[directional]**). Bottleneck: resume, then project defense · ~8–12%. Visa: sponsorship not available (cleared). Hybrid Orlando. Grad ≥ Dec 2027 (cleared).
- **Outside the resume:** Apply 2026-09-22 on this role posting (not a closed umbrella). No EA contact in `network.md` — do not pick employee referral. Optional cover letter only. See `written-answers.md`.
