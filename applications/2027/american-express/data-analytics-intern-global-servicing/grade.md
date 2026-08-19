# Campus Undergraduate Summer Internship Program - 2027 Data Analytics, Global Servicing at American Express

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside December 2027–June 2028; B.S. Computer Science and Economics matches listed majors; US citizen, no sponsorship needed
- **Track:** ai-ml + finance-adjacent payments / Global Servicing / 1LOD financial-crime risk & controls
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → PAC funding rankings → Flask REST API on EC2. That is ingest → transform → insight → serve, the 1LOD monitoring/reporting analog without claiming AML tooling.
- Lyndbrook carries the risk/controls differentiator: EPA/MassGIS regulatory entity data plus Review Velocity scoring (800 → 280 at 35% precision). Vylet adds a false-reject control analog (79%→89%) and the only SQL-through-use line; SignalWeaver is the dashboard/visualization analog.
- Binding ding: preferred SQL is on the page only in an unquantified DAL/freshness bullet.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof the JD prefers, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact — a 1LOD analytics screener cannot tell how much the DAL moved data quality or reporting freshness.

### Misreads

- A PE/search-fund founder tagline on Vylet can file as startup GTM if the reader never reaches the name-collision / SQL freshness lines.
- SignalWeaver's financial-research descriptor can read as markets/quant or notebook ML; the on-page work is a dashboard + FastAPI scores + pgvector search.
- A keyword-first pass for Tableau / Power BI / AML platforms can bucket this as "no visualization / no financial-crime stack" even though a React dashboard and PAC/scoring reports are on the page.

### Interview angles

- **Lead with:** MDC Pandas ETL on irregular filings and PAC rankings (trends/spend monitoring analog); Lyndbrook PWSID entity DB + Review Velocity shortlist (compliance scoring / control-gap analog); Vylet name-collision false-reject (79%→89%) as evaluating a broken control; SignalWeaver React dashboard as the reporting analog
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use; adding the 30x Vylet launch overflowed to two pages)*. No Snowflake, Databricks, Copilot, Fusion, Tableau, Power BI, or AML production tools — say Python/SQL/Pandas/REST and ramp. No financial-crime internship — preferred interest, not a claimed domain; do not invent sanctions/AML work. This packet is not the ETS Sunrise SWE intern (26011015)
- **Depth prep:** Walk one ingest → normalize → aggregate → serve path (MDC) and one scoring/precision path (Lyndbrook). STAR for non-technical stakeholders (MCFN researchers) and HireVue why-Amex / commercial awareness (`company.md`). Easy HackerRank / Tech assessment if they route this Corporate Functions seat through the student Tech process; behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — applied data-analytics page on a resume-first B-tier req; Python/SQL through use; finance-adjacent scoring and a control-gap analog; no eligibility miss on the document
- **Overall hire odds:** Medium — B-tier ~10–15% with resume as the bottleneck; the page matches the work. Residual risk is HireVue commercial-awareness, NYC hybrid / Amex Flex, rolling class fill, and whether this GS seat uses the Tech HackerRank
- **Funnel filters:** Oracle Cloud HCM + resume screen (bottleneck); HireVue recorded behavioral (3 questions) then two ~30-minute live interviews (`company.md`); HackerRank Easy is the companies.md Tech analog, unpublished for this Corporate Functions req. No intern sys design. No visa sponsorship. Apply-before 10/02/2026; rolling
- **Outside the resume:** Apply in the first wave on Oracle Cloud HCM (posted 2026-08-18). A GS / 1LOD or Amex alum referral beats cold apply. Prep STAR on stakeholder-scoped delivery and an honest "why financial-crime controls" — do not recycle the ETS SWE story
