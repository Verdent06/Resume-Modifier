# Data Analytics Intern (Summer 2027) at Zipline

## Verdict

- **Score:** 9.0 / 10 (1 demerit — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — B.S. Computer Science and Economics, Expected May 2028 (rising junior for Summer 2027); full-time onsite SSF May/June–Aug/Sept 2027 is feasible; US citizen, JD cannot sponsor
- **Track:** ai-ml + IQME factory-floor manufacturing analytics / autonomous logistics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN stakeholder delivery — production-lead analog, not consumer-apps SWE and not ML-research.
- Lyndbrook multi-source EPA+MassGIS merge plus Review Velocity (800 → 280, 35% precision on operational scale) is the factory-floor scoring analog; Vylet leads with SQL freshness/validation, then a 79→89% data-quality fix and a Dockerized scored pipeline (30x).
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL timestamp-validation bullet is the only on-page SQL-through-use proof the JD requires, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact.

### Misreads

- A keyword-first pass for Mode / Sigma / Streamlit / Tableau / ERP / MES can bucket this as "no reporting stack" even though a React dashboard, PAC rankings, and operational-scale scoring are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- Vylet's PE/search-fund founder tagline can file as a generic agentic product if the reader never reaches the SQL DAL and 79→89% quality lines.
- This PDF can be mistaken for the already-applied consumer-apps SWE intern if the reader only sees Flask/React and skips the ETL / scoring / data-quality spine.

### Interview angles

- **Lead with:** MDC Excel-export ETL and PAC rankings as the stakeholder KPI/report analog; Lyndbrook Review Velocity (fleet expansion / operational scale, 35% precision) as the IQME floor-metrics analog; Vylet SQL freshness + 79→89% name-collision catch as data-quality; SignalWeaver React dashboard as the Mode/Streamlit/Sigma analog
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use)*. No Mode, Sigma, Streamlit, Tableau, Looker, Snowflake, Databricks, Copilot, or Fusion — say you will ramp; do not invent them. No factory-floor internship — analog is campaign-finance / search-fund operational scoring, not Zipline ERP/MES. This is IQME analytics, not the SWE intern already applied.
- **Depth prep:** Greenhouse resume deep-dive then likely practical SQL/Python/reporting take-home + project defense (`company.md` sibling funnel; no standard LC OA). Walk one ingest → KPI path (MDC) and one quality/anomaly path (Vylet). STAR for translating a business question into a query (IQME "what you'll do"). Confirm onsite SSF dates and no sponsorship on the form. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — Python/SQL through use, Pandas ETL, PAC rankings as a KPI analog, Review Velocity precision, a React dashboard, and a named data-quality fix all register in one pass; GPA 3.66 and stats/econ coursework clear the intern analytics bar
- **Overall hire odds:** Medium — B-tier ~3–8% with take-home + project defense as the bottleneck (`companies.md`); the page clears the analytics screen, then onsite SSF relocate, unpublished practical take-home, and missing named BI tools still eliminate
- **Funnel filters:** Greenhouse **7990632003** + human resume screen; no standard LC OA; sibling SWE loop is resume → recruiter → tech deep-dive → take-home → project presentation. Bottleneck: take-home + project defense · ~3–8%. Visa: cannot sponsor (cleared). Full-time in-person South San Francisco. Application cap: three per 30 days (SWE summer + spring already logged).
- **Outside the resume:** Apply 2026-09-11. Confirm Summer 2027 onsite availability (form may say "spring"). No Zipline IQME contact in `network.md`. Do not write a "why Zipline" essay — this analytics form has none. Optional cover letter only.
