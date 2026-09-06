# 2027 Business Analytics Intern at Schonfeld

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside January 2028–Summer 2028; B.S. Computer Science and Economics is a quantitative degree; US citizen, no sponsorship
- **Track:** ai-ml + multi-manager hedge fund / Business Analytics serving risk, trading, accounting, operations, BD
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) → PAC funding rankings → Flask REST API on EC2. That is ingest → transform → report → serve, the BA analog to streamlining manual processes and supporting reporting infrastructure.
- Lyndbrook carries the hedge-fund differentiator: search-fund acquisition intelligence, 15 hours/week of prospecting removed, Review Velocity scoring (800 → 280 at 35% precision). Vylet adds a 30x scored-lead pipeline with Redis workers plus the only SQL-through-use line; SignalWeaver is the dashboard / query analog (React history views + pgvector search at 49ms p50).
- Binding ding: required SQL is on the page only in an unquantified DAL/freshness bullet.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof the JD requires, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact — a BA screener cannot tell how much the DAL moved data quality or reporting freshness.

### Misreads

- SignalWeaver's "research assistant; not investment advice" descriptor can file as ML-research or a notebook; the on-page work is a dashboard plus pgvector search.
- A keyword-first pass for Power BI / Tableau / Snowflake can bucket this as "no reporting stack" even though PAC rankings and a React dashboard with persisted history are on the page.
- Vylet's PE/search-fund founder tagline can file as startup GTM if the reader never reaches the 30x pipeline / SQL freshness lines.

### Interview angles

- **Lead with:** MDC Pandas ETL on irregular filings and PAC rankings (manual-process / report analog); Lyndbrook PWSID entity DB + Review Velocity shortlist (proposed analytics / scored decision); Vylet 30x Redis pipeline as streamlining; SignalWeaver React dashboard as the Power BI reporting analog
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use; adding the 79%→89% qualification line overflowed to two pages)*. No Power BI, Snowflake, Databricks, Copilot, Tableau, Fusion, Sentry, or KDB — say Python/SQL/Pandas/Postgres/Redis and ramp Power BI on the team. No trading-desk internship — interest via CS+Econ and finance-adjacent data products; do not invent OMS/P&L work. This packet is **not** Greenhouse 8180089 SWE.
- **Depth prep:** Walk one ingest → normalize → aggregate → serve path (MDC) and one scoring/precision path (Lyndbrook). STAR for non-technical stakeholders (MCFN researchers, search-fund principal). SQL/Python practical plus campus values (structured problem-solving, intellectual humility — Jennifer Kaplan). Do not prep the SWE sibling's C++ OA as this req's identity.

## Likelihood

- **Resume screen:** High — applied data-analytics page on a resume-weighted B-tier HF BA req; Python/SQL through use; Redis plus Postgres; finance-adjacent scoring and a dashboard analog; no eligibility miss on the document
- **Overall hire odds:** Medium — B-tier ~3–8% with resume + technical as the bottleneck; the page matches Data Analyst work. Residual risk is an unpublished SQL/Python technical, NYC onsite, and Power BI ramp in the seat
- **Funnel filters:** Greenhouse 8171703 + resume screen; technical unpublished on this BA posting (directional SQL/Python + reporting; SWE sibling OA is not this req); tech/behavioral; campus values. No intern sys design. Split visa questions — both No. Grad window January 2028–Summer 2028 = **Yes** (May 2028). Posted 2026-09-04 (first wave)
- **Outside the resume:** Apply in this opening wave; optional cover letter from `written-answers.md`; honest **Yes** on Jan–Summer 2028 (do not copy the SWE sibling's 2027-grad **No**). No Schonfeld contact in `network.md`
