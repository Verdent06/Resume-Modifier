# Internal Data and Analytics Intern - Summer 2027 at American Family Insurance

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible — seeking baccalaureate, enrolled full-time, well past 24 semester hours by Summer 2027 (Expected May 2028 / Junior); US citizen so the no-sponsorship clause clears; no exclusive class-year window on this JD
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Vylet leads with a Dockerized scored-lead pipeline (30x), a SQL freshness DAL, and three paying clients — customer-driven analytical work, not generic SWE and not ML-research.
- SignalWeaver carries the present-results analog: React dashboard, out-of-sample regression, pgvector search over stored news.
- Binding ding: the only other Experience is a Voice AI co-op, and the second project is a C++ audio plugin.

### Demerits

- **major** · `CaseStudyPrep.AI` · voice-AI co-op occupying Experience slot 2 — The only other titled role is Software Engineer Co-op (Voice AI): Silero VAD/ONNX dead-air filtering and S3/Angular upload recovery. An Internal Data and Analytics intern screener reads audio-product engineering, not analytical work in a functional area or a stakeholder report.
- **minor** · `Granular Synthesizer Plugin` · audio-DSP project with no analytics analog — Second project is a C++/JUCE MemoryPool and VST3/AU release plugin. Real systems work, but zero ingest, score, KPI, or report signal for this department-analytics intern.
- **minor** · `Vylet` · SQL/DAL bullet metric-free — The only SQL through-use on the page is injection-safe timestamp validation and automatic re-scrapes. It closes on architecture with no sized freshness or accuracy win, so a data-and-analytics screen cannot size the SQL work.

### Misreads

- A rushed analytics screener may bucket this as a voice-AI / audio-DSP SWE intern because Experience slot 2 and Project slot 2 are both audio, and miss Vylet’s scored pipeline and SignalWeaver dashboard.
- A keyword-first pass for Tableau / Power BI / Excel may no-pile a page that actually has a React/Postgres dashboard and scored-lead reporting.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL analytics screen looks for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** Vylet (scored-lead pipeline, 30x, paying clients) as the customer-driven analytical project this intern tests; SignalWeaver dashboard + regression if they ask for presenting results to management
- **Defend:** CaseStudyPrep.AI is a Voice AI co-op kept because Experience is constrained to Vylet + this co-op — walk the 40% cost / 27% upload numbers as production troubleshooting, not as the analytics story *(out of rails: every CaseStudyPrep.AI pool bullet is voice-AI; MDC and Lyndbrook are forbidden for this packet)*; Granular is C++ systems depth, not an analytics analog *(out of rails: all six Granular bullets are DSP; omitting it drops below min_entries=4)*; SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Python did the scoring *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use)*; no Tableau, Power BI, Excel-as-tool, SAS, R, Snowflake, Databricks — walk React/Postgres instead of inventing them *(out of rails: those tools are not in inventory or swap sets)*
- **Depth prep:** STAR on presenting a scored output to a non-builder (Vylet clients); walk ingest → score → dashboard on SignalWeaver; honest SQL answer (timestamp freshness, not analysis SQL). No published intern OA — expect Easy Python/SQL fluency + STAR (`companies.md` peer of Nationwide / NM ID&A). Madison hybrid + in-person first-week NEO.

## Likelihood

- **Resume screen:** Medium — Vylet’s scored pipeline, paying clients, and SignalWeaver dashboard/regression/pgvector search are on-axis, but half of Experience is Voice AI and the second project is C++ DSP, so a rushed analytics screen can no-pile this as a SWE/audio resume
- **Overall hire odds:** Medium — American Family is C-tier with a resume bottleneck (~15–25%) and no published intern OA, so the PDF is the binding filter. Eligibility is clean (Expected May 2028, GPA 3.66, CS + Economics, US citizen). The remaining cut is Madison hybrid + in-person NEO, defending Python/SQL fluency without analysis-SQL, and why this is a data-and-analytics intern rather than a voice-AI SWE
- **Funnel filters:** Workday **R39401** (`includeResumeParsing` true; two login-walled questionnaires) → recruiter (auth, Madison hybrid + in-person NEO, enrollment, 24 credits, no sponsorship) → unpublished intern loop. Intern OA unpublished. No intern sys design. Bottleneck: resume · ~15–25% (`companies.md` C-tier, peer of Nationwide / State Farm / Great American / Northwestern Mutual). Posted 2026-09-18 — first wave.
- **Outside the resume:** Apply in this first wave. Prep STAR on presenting results to a non-builder and an honest SQL answer — behavioral is a filter (`recruiting.md` §6)
