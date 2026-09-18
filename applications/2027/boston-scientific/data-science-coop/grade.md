# Data Science Co-op — Spring or Summer 2027 at Boston Scientific

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is Spring 2028 (JD: December 2027–Spring 2028); B.S. Computer Science (listed); US citizen vs no-sponsor; Python through use; ML via held-out LoRA + ONNX VAD (3 months–1 year floor)
- **Track:** ai-ml + medical-device manufacturing / process-development analytics
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel-export → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN delivery — ingest → method → served output, not SWE and not a 12-week intern sibling.
- Lyndbrook is multi-source EPA+MassGIS plus Review Velocity (800 → 280, 35% precision); SignalWeaver is LoRA 81%→96% held-out plus out-of-sample regression; Vylet carries a Dockerized LangGraph pipeline and SQL freshness.
- Binding dings: CaseStudyPrep.AI is a one-line voice-AI co-op, and the only SQL-through-use proof is an unquantified asyncpg DAL.

### Demerits

- **minor** · `CaseStudyPrep.AI` · off-axis voice-AI co-op — Last Experience slot is Silero VAD / ONNX / Whisper silence-filtering; real inference work, not process-data ETL, statistical scoring, or a predictive dashboard
- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL-through-use proof, but it closes on architecture with no sized impact *(out of rails: only SQL pool bullet has no metric; eval swap made SQL Skills-only)*

### Misreads

- A skim that stops on CaseStudyPrep.AI's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL, Lyndbrook scoring, and SignalWeaver held-out LoRA this DS co-op wants.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL process-DS screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS → Review Velocity 800 → 280 at 35% precision) as the ingest → score loop; SignalWeaver LoRA 81%→96% held-out if they ask for the ML floor; Vylet 30x LangGraph pipeline if they ask for genAI/docs automation analog
- **Defend:** CaseStudyPrep.AI is ONNX VAD from a voice-AI co-op, not process DS — it is the preferred prior co-op, not the lead *(out of rails: pool is VAD / S3 / Web Workers; min_entries=5 blocks omit)*. SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas did the analysis *(out of rails: no SQL impact metric in pool)*. Do not claim Snowflake, Databricks, Tableau, Copilot, Fusion, TensorFlow, scikit-learn, NumPy, SciPy, matplotlib, seaborn, or Plotly. This is the 8-month Data Science Co-op, not the 12-week SWE intern.
- **Depth prep:** walk a process engineer analog through one finding (MDC ranking or Lyndbrook shortlist); SignalWeaver held-out LoRA / 3.39% R² as "the score is not just fitting noise"; Vylet stale-timestamp re-scrape as pipeline automation. No published OA — expect STAR + project walk (`company.md`). Confirm Maple Grove May 17/24–Dec 17 2027, hybrid ≥4 days/week, transportation, and no sponsorship on the form. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + stats coursework) and the top half is ingest → ranking/shortlist → ML-with-eval
- **Overall hire odds:** Medium — Boston Scientific is B-tier with a resume bottleneck (~10–15%) and no published OA (`companies.md`), so this page should clear the binding co-op gate; the loop still has to defend the **8-month** Maple Grove hybrid, commute/housing, and walk a process-data story without claiming med-device manufacturing systems
- **Funnel filters:** Eightfold pid **563602813600487** / req **634924** + recruiter (auth, 8-month dates, Maple Grove, Python/ML) → 1–2 STAR/project rounds. No published intern OA. No intern sys design. Bottleneck: resume · ~10–15%. Visa: no sponsor (cleared). Safety-sensitive prohibited-substance test.
- **Outside the resume:** Apply 2026-09-18 (listed ~2026-09-17; first wave). No Boston Scientific contact in `network.md` — do not pick Employee Referral. Form email `verdent06@gmail.com`. See `written-answers.md`. Behavioral is a filter (`recruiting.md` §6).
