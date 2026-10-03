# Intern, Data Science at New York Mets

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — currently enrolled; Expected May 2028 returns after Summer 2027; B.S. Computer Science and Economics is related to statistics; US citizen vs unstated visa line; Queens / Citi Field onsite relocate
- **Track:** ai-ml + MLB baseball-ops statistical modeling
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.7, Expected May 2028, Python through use, and a lead spine of irregular filings → Pandas ETL → PAC ranking shipped to a research stakeholder. That is this Baseball Analytics intern (ingest → method → present), not Baseball Systems SWE R1433, not Applied AI R1468, not commercial Strategy & Analytics.
- Lyndbrook Review Velocity (800 → 280 at 35% precision) is the scoring analog in the lead window. SignalWeaver is the tested statistical model: out-of-sample regression (3.39% R²) plus held-out LoRA classification (81% → 96%) and a dashboard a non-builder can read.
- Binding dings are both on Vylet: the only SQL proof never sizes the win, and the lead line is a LangGraph 30x pipeline rather than a tested statistical model.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact a baseball-ops screen can scale.
- **minor** · `Vylet` · agentic pipeline lead vs statistical model — The lead Vylet line is a Dockerized LangGraph 30x scored-lead speedup — process automation, not a tested statistical model (assumptions, held-out eval, error analysis) this intern is hired to build.

### Misreads

- A keyword-first pass for R / Statcast / pybaseball / Tableau can no-pile a page that actually has Python, Pandas ETL, a scored shortlist, and a held-out regression.
- The Vylet LangGraph 30x line can bucket this as product-SWE / agentic automation and miss SignalWeaver as the model this intern would present to baseball ops.
- The SQL/DAL line can read as database plumbing rather than language proof, because it never sizes the freshness win.

### Interview angles

- **Lead with:** MDC (Excel-export ETL → PAC funding rankings for MCFN researchers; ~800 hours / 400 PACs) as the ingest → ranked insight analog; Lyndbrook Review Velocity (800 → 280, 35% precision) as the scoring analog; SignalWeaver out-of-sample regression + held-out LoRA if they ask you to walk a statistical model to a non-builder
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; swapping the DAL drops SQL-through-use)*. Vylet lead is a 30x LangGraph pipeline, not a tested model — walk SignalWeaver R² / LoRA held-out as the statistical analog; Node 3 0–100 scoring overflowed the page *(out of rails: scoring bullet fails page_fill)*. No R, Statcast, pybaseball, Tableau, Snowflake, Databricks, Copilot, Fusion — do not invent them *(out of rails: not in inventory or swap sets)*. This is Workday **R1508** Intern, Data Science — not Associate Hitting Analyst **R1518**, not Baseball Systems SWE **R1433**, not Applied AI **R1468**. Casual baseball interest is optional; do not fake a sabermetrics internship.
- **Depth prep:** No published OA (`company.md`). Club R&D intern analog: take-home + present a model **[directional]**. Walk one ingest → ranked insight path (MDC), one scored-shortlist path (Lyndbrook), and SignalWeaver as “the score is not just fitting noise” for a coach/front-office analog. STAR cooperative work is a filter (`recruiting.md` §6). Confirm Citi Field onsite Summer 2027 and **verdent06@gmail.com** (JD forbids `.edu`)

## Likelihood

- **Resume screen:** High — eligibility is clean and the top half plus SignalWeaver show ingest → score/rank → regression/classification with eval → dashboard
- **Overall hire odds:** Medium — Mets intern is resume-gated C-tier (~15–25%); remaining cut is Citi Field onsite, defending Python without R/Statcast, and presenting a model to a non-builder
- **Funnel filters:** Workday **R1508** (`sterlingmets.wd5` / `Mets`) resume (`includeResumeParsing` true) → recruiter/HM (Queens onsite, Summer 2027) → unpublished intern loop. Intern OA unpublished — do not invent HackerRank/CodeSignal. No intern sys design. Bottleneck: **resume**. ~15–25% (`companies.md`). Comp **$20.00–$25.00/hr**. Posted **2026-10-02**
- **Outside the resume:** Apply in this first-wave window (posted 2026-10-02). Use **verdent06@gmail.com** — the JD forbids `.edu`. No Mets contact in `network.md` — do not pick Employee Referral. Prep one model walk for a non-technical audience. Packet only — see `written-answers.md`
