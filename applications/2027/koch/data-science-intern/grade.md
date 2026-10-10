# Georgia-Pacific Data Science Internship at Georgia-Pacific (Koch)

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — CS is a named related field; Expected May 2028 vs FT on/before Summer 2028; US citizen / no sponsorship; Summer 2027 is after junior year / rising senior; not grad-only
- **Track:** ai-ml + Georgia-Pacific manufacturing / industrial-ops data science (paper, packaging, mills — plant safety/efficiency models), Koch PBM
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- MDC leads with irregular Excel → Requests+Pandas ETL (~800 hours / 400 PACs), PAC funding rankings, and a Flask REST API on AWS EC2 — ingest → rank → deployed output, not notebook ML and not the KBX BA&I sibling.
- Lyndbrook water-utility / operational-scale merge plus Review Velocity (800 → 280, 35% precision) is the industrial-ops scoring analog in the lead window; SignalWeaver is held-out classification (LoRA 81% → 96%) plus out-of-sample regression and a FastAPI serve path.
- Binding ding: the only SQL-through-use proof is an unquantified asyncpg freshness DAL.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof this Python+SQL DS seat treats as a language floor, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact; the JD asked for SQL to retrieve data, not a metric-free DAL

### Misreads

- A keyword-first pass for SAS / mill SCADA / Power BI can bucket this as "no GP stack" even though Python, SQL, Pandas ETL, operational scoring, evaluated classification/regression, and a served API are on the page.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL data-science screen is looking for, because it never sizes the freshness win.
- Education says Computer Science and Economics, not Data Science — a title-match filter can miss that CS is a named related field on this JD.

### Interview angles

- **Lead with:** MDC (irregular filings → Pandas ETL → PAC ranking shipped to MCFN on EC2; ~800 hours / 400 PACs) as end-to-end analytics ownership; Lyndbrook Review Velocity (operational scale, 35% precision) as the manufacturing-ops scoring analog; SignalWeaver LoRA classification + held-out eval and out-of-sample regression if they ask for statistical / ML / deep-learning models; FastAPI p50/p99 if they ask how you deploy
- **Defend:** SQL on the page is Vylet asyncpg freshness / re-scrape, not a JOIN that retrieved mill data — say Pandas/Python did the analysis *(out of rails: pool has no JOIN/window/GROUP BY analytics bullet; only SQL pool bullet has no impact metric)*; SAS is preferred and not in inventory — walk Python stats/ML instead of inventing SAS *(out of rails: SAS is not in the pool or swap sets)*; this is Avature **195341** GP Atlanta DS intern, not KBX BA&I **194813**; degree is CS + Economics, not "Data Science" — do not rewrite the major
- **Depth prep:** walk a non-builder (business + engineer analog) through one finding (MDC ranking or Lyndbrook shortlist); SignalWeaver 81% → 96% held-out classification and 3.39% R² as "the score is not just fitting noise"; Vylet stale-timestamp re-scrape as data-validation analog. No confirmed LeetCode OA — expect Easy Python/SQL fluency, a project deep-dive, and PBM/STAR. Atlanta 12-week hybrid is a yes.

## Likelihood

- **Resume screen:** High — eligibility is clean (Expected May 2028, CS named, GPA 3.7) and the top half is Pandas ETL → operational scoring → evaluated classification/regression with a served API
- **Overall hire odds:** Medium — Koch/GP is C-tier with a resume bottleneck (~20–30%) and no published OA, so this page should clear the intern gate; remaining cut is Atlanta hybrid relocate, defending Python/SQL without SAS, and PBM/STAR with mill/ops partners
- **Funnel filters:** Avature **195341** resume screen → recruiter (Atlanta hybrid, FT-by-Summer-2028, no-sponsorship, CS-related degree) → unpublished intern loop (PBM/STAR; Easy Python/SQL + applied-DS walk analog). Intern OA unpublished — do not invent HackerRank/CodeSignal. No intern sys design. Bottleneck: resume (`companies.md`). Drug test + E-Verify if offer.
- **Outside the resume:** Apply in this wave. Honest US citizen / no sponsorship and Atlanta hybrid yes. Prep STAR (MDC/Lyndbrook) and an honest SQL-without-SAS answer — behavioral is a filter (`recruiting.md` §6). Form email `verdent06@gmail.com`.
