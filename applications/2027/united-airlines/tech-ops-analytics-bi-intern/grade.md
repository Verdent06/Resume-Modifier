# Intern - Tech Ops Analytics & Business Intelligence (Summer 2027) at United Airlines

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027 is junior-year intern; JD has no class-year or GPA floor; work authorization / no sponsorship matches
- **Track:** ai-ml + airline Tech Ops / fleet-maintenance operational analytics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular Excel/filings → Pandas ETL (~800 hours / 400 PACs) → PAC funding rankings → Flask REST on EC2 for MCFN researchers. That is ingest → transform → insight/serve, the Tech Ops Analytics analog without claiming aircraft systems.
- Lyndbrook carries the differentiator: entity database plus Review Velocity fleet-expansion / operational-scale scoring (800 → 280 at 35% precision).
- SignalWeaver is the visualization analog (React dashboard); Vylet is the SQL-through-use proof. No invented Power BI, Tableau, Snowflake, Databricks, Copilot, Fusion, or Sentry. Binding ding: the only SQL bullet is unsized architecture.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof the JD names as a quantitative-analysis language, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact — a Tech Ops BI screener cannot tell how much the DAL moved freshness or reporting.

### Misreads

- A keyword-first pass for Power BI can bucket this as "no visualization stack" even though a React dashboard and PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- Vylet's PE/search-fund founder tagline can file as startup SaaS if the reader never reaches the SQL DAL / scored-pipeline lines.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and PAC rankings as the SME/KPI analog; Lyndbrook PWSID entity DB + Review Velocity fleet scoring (right-work / right-location analog); SignalWeaver React dashboard as the "PowerBI or other visualization tools" analog; Vylet SQL freshness/re-scrape DAL
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use)*. No Power BI, Tableau, Snowflake, Databricks — say Python/SQL/Pandas plus a shipped dashboard and ramp on their stack. No airline/MRO internship — do not invent domain; map fleet-scoring and messy operational ETL instead
- **Depth prep:** Walk one ingest → normalize → rank → serve path (MDC) and one scoring/KPI path (Lyndbrook). Easy SQL/Python if United uses an unpublished analytical assessment (`talogyAssessmentCode` empty on this req). STAR for SME-facing delivery (MDC sole-engineer / MCFN researchers) and comfort with ambiguity. Behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — applied-data page on a resume-first C-tier req; Pandas ETL, PAC rankings shipped via REST, fleet-expansion scoring, React dashboard, and SQL through use all register in one pass; no eligibility miss on the document
- **Overall hire odds:** Medium — C-tier ~15–25% with resume as the bottleneck and two seats in a two-week window; the packet matches the work, but residual cut is Chicago onsite fit, STAR behavioral, and a possible unpublished analytical assessment
- **Funnel filters:** Phenom careers → Taleo apply; no published intern OA on this req; 1–2 STAR behavioral; possible analytical assessment on some United tracks (not printed here). No sponsorship. Window Sep 1–15 2026. Recruiter Anthony Sykes. Bottleneck: resume · ~15–25% directional (`companies.md`)
- **Outside the resume:** Apply in the Sep 1–15 2026 window immediately (`recruiting.md` §8). Taleo prescreen "require sponsorship" → No. Do not put citizenship on the resume. Prep STAR on SME-scoped delivery and fleet/entity scoring; be ready to ramp on Power BI rather than claim it
