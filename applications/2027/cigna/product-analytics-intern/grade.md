# Product Analytics Summer Intern at The Cigna Group

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — official intern program hires juniors or rising seniors; Expected May 2028 is the conversion window (returns after the May 24 2027 10-week term). Dual CS + Economics is related to preferred Analytics/Business majors. US citizen, sponsorship knockout clears
- **Track:** ai-ml + healthcare-product-analytics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of irregular Excel filings → Pandas ETL → PAC ranking → Flask reporting API for a named nonprofit stakeholder. That is this Product Analytics intern (data prep, reporting, dashboards, medical-spend analog), not AEDP actuarial, not TECDP, not ALDP, and not a SWE intern.
- Lyndbrook Review Velocity (800 → 280, 35% precision) is the statistical-driver / scored-shortlist analog in the top half; Vylet carries injection-safe SQL freshness plus a 30x scored pipeline; SignalWeaver opens on a React/Postgres dashboard, then held-out regression eval.
- Binding dings: Excel / Microsoft Office is named on the JD and absent as an interview skill; SQL is freshness/validation, not analysis SQL.

### Demerits

- **minor** · `resume` · named Excel / Microsoft Office stack absent — JD Qualifications require proficiency with SQL and Microsoft Office Suite (i.e. Excel); the page shows Pandas ETL on irregular Excel exports and a React/Postgres dashboard analog, but never names Excel or Office as a skill the candidate interviews in
- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a Product Analytics screen looks for query/aggregate/insight SQL and does not find it

### Misreads

- A keyword-first pass for Excel / Power BI / Tableau can bucket this as "wrong stack" even though Pandas-on-Excel-exports, PAC rankings, and a React dashboard are on the page.
- SQL on the Languages line can file as analysis SQL, then bounce in the panel when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- Flask REST / founder MRR on Vylet can file as product-SWE if the reader never reaches the ETL, ranking, scoring, SQL freshness, and dashboard lines.

### Interview angles

- **Lead with:** MDC (irregular Excel filings → Pandas ETL → PAC ranking shipped to MCFN; ~800 hours / 400 PACs) as the ingest → KPI → report loop this seat tests; Lyndbrook Review Velocity (800 → 280, 35% precision) as the medical-spend / scoring analog; SignalWeaver React/Postgres dashboard if they ask for viz; Vylet SQL freshness + 30x scored pipeline if they ask for data quality
- **Defend:** Excel / Office are not interview skills in inventory — walk Pandas-on-Excel-exports and the React dashboard instead of inventing them *(out of rails: no Excel/Office in pool or swap sets)*; SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; this is Workday **26010180** Product Analytics Intern (Morris Plains or St. Louis hybrid), not AEDP, not TECDP, not ALDP, not SWE
- **Depth prep:** No published OA (`company.md`; InterviewSense Accredo Product analog: verbal SQL/data + STAR). Walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist). Confirm hybrid Morris Plains **or** St. Louis, 40h from May 24 2027, and no-sponsorship knockouts. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — eligible Expected May 2028, GPA 3.66, and an ingest → ranking/shortlist → stakeholder delivery spine on a resume-first C-tier intern req
- **Overall hire odds:** Medium — C-tier ~20–30% with resume as the bottleneck and no published OA; residual cut is hybrid NJ/MO relocate, a verbal SQL/Excel walk, and 1–2 STAR rounds
- **Funnel filters:** Workday **26010180** (`cigna.wd5` / `cignacareers`) resume (`includeResumeParsing` true) → recruiter/HM (auth, hybrid NJ or MO, May 24 start, class year) → 1–2 behavioral / SQL-analytics walks **[directional]** · intern OA unpublished · no intern sys design · Bottleneck: resume · ~20–30% (`companies.md` Cigna / Centene / Wellmark peers). **No sponsorship** (H-1B, CPT/OPT/STEM). Comp **$26.00–$28.00/hr**. Hybrid 3 days/week, 40h, 10 weeks from **May 24, 2027**
- **Outside the resume:** Apply on Workday this first-wave window (posted 2026-10-01). Phenom careers mirror can show closed while Workday `canApply` is true — use the Workday apply URL. Confirm US work auth without sponsorship. Prep STAR (MDC/Lyndbrook) and an honest SQL/Excel answer. See `written-answers.md`
