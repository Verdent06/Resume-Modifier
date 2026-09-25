# Co-op, Data Science at Biogen

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028, currently enrolled (started Aug 2025 → ≥1 term by Jan 2027), B.S. Computer Science (listed), 18+ by start, US citizen vs legal US work auth, remote USA from Michigan
- **Track:** ai-ml + biopharma R&D / SPARQ TADI regulatory-quality-safety analytics
- **Pipeline:** 1 cycle · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel-export → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and MCFN delivery — ingest → method → served output, not a 12-week summer intern sibling and not a lab bench co-op.
- Lyndbrook is multi-source EPA+MassGIS regulatory data plus Review Velocity (800 → 280, 35% precision); Vylet carries a Dockerized LangGraph pipeline and Gemini embeddings / SQL freshness; SignalWeaver is held-out LoRA 81%→96% plus a React dashboard.
- Binding dings: CaseStudyPrep.AI is a one-line voice-AI co-op, and the only SQL-through-use proof is an unquantified asyncpg DAL.

### Demerits

- **minor** · `CaseStudyPrep.AI` · off-axis voice-AI co-op — Last Experience slot is Silero VAD / ONNX / Whisper silence-filtering; real inference work, not regulatory/quality data ETL, statistical scoring, NLP-over-repos, or a stakeholder dashboard *(out of rails: pool is VAD / S3 / Web Workers; min_entries=5 blocks omit)*
- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL-through-use proof, but it closes on architecture with no sized impact *(out of rails: only SQL pool bullet has no metric)*

### Misreads

- A skim that stops on CaseStudyPrep.AI's Voice AI title can file this as a product/audio intern and miss the MDC Pandas ETL, Lyndbrook regulatory scoring, and SignalWeaver held-out LoRA this SPARQ TADI co-op wants.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python-or-R-or-SQL DS screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN; ~800 hours / 400 PACs) and Lyndbrook (EPA/MassGIS → Review Velocity 800 → 280 at 35% precision) as the ingest → score loop on messy/regulatory-shaped data; SignalWeaver LoRA 81%→96% held-out if they ask ML/NLP; Vylet 30x LangGraph + embeddings if they ask LLM chatbots / auditor-style agents; LangSmith eval 50%→90% is in the pool, not on this page — use it verbally for SOP/AI-oversight
- **Defend:** CaseStudyPrep.AI is ONNX VAD from a voice-AI co-op, not SPARQ TADI DS — it is the titled prior co-op, not the lead *(out of rails: pool is VAD / S3 / Web Workers; min_entries=5 blocks omit)*. SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that produced a ranking — say Pandas did the analysis *(out of rails: no SQL impact metric in pool)*. Do not claim R, SAS, Snowflake, Databricks, Tableau, Power BI, Copilot, Fusion, or GxP internships. This is the 6-month Jan–Jun Data Science co-op, not the 12-week summer intern.
- **Depth prep:** walk a quality/regulatory analog through one finding (MDC ranking or Lyndbrook shortlist); SignalWeaver held-out LoRA as NLP classification with evaluation; Vylet stale-timestamp re-scrape as reusable pipeline + documentation analog. No published OA — expect STAR + project walk (`company.md`). Confirm January–June 2027 remote USA, return-to-school Fall 2027, and US work auth on the form. Behavioral is a filter (`recruiting.md` §6).

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, GPA 3.66, CS + stats coursework) and the top half is ingest → ranking/shortlist → ML-with-eval / LangGraph
- **Overall hire odds:** Medium — Biogen is B-tier with a resume bottleneck (~8–12% for this remote DS co-op; overall intern ~4–8% **[directional, Extern]**) and no published OA (`companies.md`), so this page should clear the binding co-op gate; the loop still has to defend **Jan–Jun 2027 remote**, return-to-school, and walk a regulatory/quality story without claiming GxP systems
- **Funnel filters:** Workday **REQ24211** (`biibhr` / `external`) + recruiter (auth, dates, remote, enrolled) → 60–90m STAR + track-tech. No published intern OA. No intern sys design. Bottleneck: resume · ~8–12%. Visa: US citizen (cleared). Winter co-ops generally filled by end of November.
- **Outside the resume:** Apply in this first-wave window (posted 2026-09-24; resume review October 2026). No Biogen contact in `network.md` — do not pick Employee Referral. Form email **`verdent06@gmail.com`**. Packet only from this agent — see `written-answers.md`
