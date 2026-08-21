# 2027 Undergrad Data Analyst Intern/co-op at Advanced Micro Devices, Inc

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 vs Summer 2027 (May 24 – August 13); UMich CS undergrad; US citizen vs no-sponsorship knockout
- **Track:** ai-ml + semiconductor / high-performance computing
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- 30-second screen: CS + Economics, GPA 3.66, Expected May 2028, and a lead spine of messy ingest → PAC ranking → scored shortlist → dashboard. That is this Undergrad Data Analyst intern/co-op, not the Masters DA seat and not an ML intern.
- Binding dings: SQL is listed as a language but never used as analysis SQL, and slot 2 is a Voice AI co-op.
- Eligibility and San Jose / Santa Clara hybrid-or-onsite / no-sponsorship knockouts are clean on the page.

### Demerits

- **minor** · `resume` · SQL never used as an analysis language — Skills lists SQL as a first-class language, but the only through-use is injection-safe timestamp validation on a DAL (Vylet) plus Postgres persistence (SignalWeaver); a Data Analyst screen looks for query/aggregate/insight SQL and does not find it
- **minor** · `CaseStudyPrep.AI` · voice-AI product framing in the second slot — Slot 2 is a Voice AI co-op whose bullets are ONNX VAD, Whisper dead-air, a 40% inference-cost cut, and a 27% audio-upload failure fix in RxJS/Angular — real reliability numbers, but a DA intern screener reads audio-product engineering before analysis of performance or quality datasets

### Misreads

- A rushed DA recruiter may bucket SQL as a real analysis skill from the Languages line, then bounce in the tech screen when the only SQL story is timestamp plumbing — or the reverse: skip a strong Python analytics page because the SQL claim looks inflated.
- A rushed screener may bucket the second slot as a voice-AI SWE intern applying to the wrong req and miss the 40% cost / 27% failure performance-QA analog.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS entity database → Review Velocity shortlist at 35% precision) as the ingest → insight loop this seat tests; SignalWeaver dashboard + out-of-sample score if they ask for viz or predictive-modeling analog
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet)*; CaseStudyPrep is a Voice AI co-op kept in the lead window for cost/latency/reliability numbers, not a product-data analysis story *(out of rails: every pool bullet is voice-AI; entry is protected in the top-2 window)*; this is the Undergrad DA intern/co-op, not Masters DA and not an ML intern; no Snowflake, Databricks, Copilot, Fusion, Tableau, Power BI, Kubernetes, Azure, R, or Java
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); CaseStudyPrep 40% inference-cost / 27% upload-failure as performance and QA analog if they ask why a chip company; SignalWeaver 3.39% R² as "the score is not just fitting noise," not investment advice. No standard OA — expect Python/SQL fluency and a project deep-dive, then STAR (Achievement, Innovation, Collaboration, Integrity)

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics) and the top half is ingest → ranking/shortlist → stakeholder-adjacent delivery, which is this req's screen
- **Overall hire odds:** Medium — AMD is B-tier with a resume then tech-rounds bottleneck (~5–8%) and no standard OA on this DA posting, so this page should clear the binding intern gate; the Teams deep-dive still has to defend Python/SQL fluency and why this is a data seat at a chip company rather than a voice-AI SWE intern
- **Funnel filters:** iCIMS resume screen (rolling; posted 2026-08-20) → recruiter phone (~30 min) → hiring-manager / tech-behavioral (Extern analog 45–60 min Teams). No standard LeetCode OA. No visa sponsorship. Full-time 40 hrs/week hybrid or onsite San Jose or Santa Clara. Bottleneck: tech rounds (`companies.md` AMD B-tier)
- **Outside the resume:** Apply in this first rolling wave. No AMD contact in `network.md`. Prep STAR on MDC/Lyndbrook and an honest SQL answer — behavioral is a filter (`recruiting.md` §6)
