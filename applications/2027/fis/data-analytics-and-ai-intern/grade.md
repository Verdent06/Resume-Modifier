# Intern, Data Analytics and AI, FIS University Program at FIS

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside the JD's December 2027–May 2028 window (Rising Senior is defined by that window)
- **Track:** ai-ml + payments-fintech
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular campaign-finance filings → Requests+Pandas ETL (~800 hours / 400 PACs) and a Flask REST API on EC2 shipped to MCFN — ingest → organize → stakeholder report, not ML research and not the SWE intern sibling.
- Lyndbrook (EPA/MassGIS entity merge → Review Velocity 800→280 at 35% precision) plus Vylet SQL freshness / 30x scored pipeline and a SignalWeaver dashboard + evaluated regression close the applied-analytics + payments/fintech flavor.
- Binding dings: the only SQL-through-use proof is an unquantified asyncpg freshness DAL, and Experience slot 4 is a Voice AI co-op.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; an Analytics & AI intern screen wants query/aggregate/insight SQL it can size
- **minor** · `CaseStudyPrep.AI` · voice-AI product framing — Fourth Experience slot is a Voice AI co-op whose bullets are expired-S3 upload recovery and Silero VAD/Whisper dead-air — real production numbers, but a DA/AI intern screener reads audio-product engineering before dashboards, validation, or payments/fintech analytics

### Misreads

- A keyword-first pass for Tableau / Snowflake / Databricks can bucket this as "no BI stack" even though a React dashboard and PAC/scoring reports are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen is looking for, because it never sizes the freshness win.
- A rushed screener may bucket CaseStudyPrep.AI as a voice-AI SWE intern applying to the wrong req (the JR0309512 sibling) and miss the 27% upload-failure quality analog.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC rankings shipped to MCFN; ~800 hours / 400 PACs) and Lyndbrook (entity database → Review Velocity shortlist at 35% precision) as the collect → validate → recommend loop this seat tests; SignalWeaver React dashboard + 3.39% R² regression if they ask for visualizations or model testing; Vylet Dockerized 30x pipeline if they ask for production scoring
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — walk the stale-timestamp check even though the line has no number *(out of rails: pool has one SQL bullet and it is metric-free; adding the 79→89 quality line overflowed to two pages)*; CaseStudyPrep is a Voice AI co-op kept for production-troubleshooting numbers, not a payments-analytics story *(out of rails: every CSP pool bullet is voice-AI; no fifth on-axis data Experience; Granular is worse C++ audio)*; no Snowflake, Databricks, Tableau, Copilot, or Fusion — walk Python/SQL/Pandas/React instead of inventing them; forms say Junior / Expected May 2028 — Education is fixed and eligible
- **Depth prep:** walk a non-builder through one finding (MDC ranking or Lyndbrook shortlist); Vylet stale-timestamp re-scrape as the validation/QA analog; SignalWeaver regression as "testing a model / documenting methodology," not investment advice. Recruiter OnDemand video + HM interview; behavioral/STAR is the documented intern filter. Do not invent HackerRank/CodeSignal for this DA/AI intern — SQL/Excel practical is directional only

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028 inside Dec 2027–May 2028; CS + Economics; GPA 3.66) and the top half is ingest → scored shortlist → SQL/pipeline → dashboard/regression, which is this req's applied-data screen
- **Overall hire odds:** Medium — FIS is C-tier with a resume bottleneck (~15–25% directional) and no published OA on this DA/AI intern; the page should clear the binding gate. Residual cut is Jacksonville/Atlanta/Milwaukee relocate for May 31–Aug 6, STAR on the recruiter video, and defending Python/SQL without inventing Tableau/Snowflake
- **Funnel filters:** Workday **JR0309690** + human resume screen (posted 2026-09-17) → Recruiter Video Screen / OnDemand → Hiring Manager Interview (video/on-site) → additional interviews → offer. Intern OA unpublished. No intern sys design. No sponsorship. Possible drug test. Bottleneck: resume · ~15–25% (`company.md` C-tier peer of Fifth Third / Ally / Citizens DA)
- **Outside the resume:** Apply in this first wave. Prep STAR for the OnDemand recruiter video. Do not invent a HackerRank/CodeSignal loop for this req
