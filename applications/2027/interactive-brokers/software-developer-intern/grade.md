# Software Developer Summer Internship – 2027 at Interactive Brokers

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside the preferred window (Dec 2027–May 2028); GPA 3.66 meets the 3.5 floor; CS degree in progress; C++ and Python in inventory
- **Track:** full-stack (high-performance brokerage / electronic-trading platform flavor; no track divergence)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- GPA 3.66, Expected May 2028, Python production (MDC Flask/EC2 + 800-hour ETL) and C++ real-time systems (Granular — zero-allocation `processBlock()`, lock-free SPSC) clear the named intern gates.
- SignalWeaver (49ms p50 financial-news search, Docker/CI) plus CS + Economics registers markets-adjacent flavor without claiming a trading intern.
- Binding dings: Flask REST / aggregation unquantified beyond the ETL metric; MDC "sole engineer" overlaps the Voice AI co-op dates with no part-time note.

### Demerits

- **minor** · `MDC` · metric-free shipping — production Flask REST on EC2 and the aggregation engine have no latency, load, or user metric; "delivered"/"architected" reads soft at a shop that pitches high-performance large-data platforms.
- **minor** · `resume` · overlapping sole-engineer window — MDC Jan–May 2026 ("sole engineer" on a 5-month contract) overlaps CaseStudyPrep.AI Dec 2025–May 2026 with no part-time note.

### Misreads

- A rushed screen could treat the Flask/EC2 line as an unscaled class deploy because the size number lives on the ETL bullet, not the API.
- A careful reader could discount sole-ownership on MDC because the Voice AI co-op sits on the same months.

### Interview angles

- **Lead with:** Granular C++ zero-allocation / lock-free SPSC / `processBlock()` safety audit; MDC 800-hour ETL → production Flask REST on EC2; CaseStudyPrep sub-5ms / 60 FPS as real-time systems (not Whisper); SignalWeaver 49ms p50 pgvector search.
- **Defend:** Flask/EC2 has no request-volume or latency in the pool — keep the ETL 800-hour / 400 PAC number as the scale cue and narrate sole-engineer API ownership honestly *(out of rails: MDC API-scale metric — pool bullets 2–4 have no latency/load/user numbers; swap sets cannot invent them)*. MDC and CaseStudyPrep overlapped in calendar 2026 — say both were concurrent, not sequential full-time jobs *(out of rails: overlapping sole-engineer window — headers/dates are fixed; no part-time wording in the pool)*. Java is on the intern JD; do not claim it — interview in C++ or Python and ramp Java if the team uses it.
- **Depth prep:** Timed DS&A mediums plus probability/logic for the OA; C++ memory/threading/lock-free grill on Granular; Python production (Flask/EC2, ETL); SQL/relational basics; STAR on owning a project with daily check-ins.

## Likelihood

- **Resume screen:** High — GPA 3.66, Expected May 2028, Python and C++ proven in bullets, production API plus lock-free real-time C++, one page; clears every named intern screen gate.
- **Overall hire odds:** Medium — IBKR is B-tier with an OA/tech bottleneck (~5–8%); recruiting.md puts the binding intern filter after the PDF (coding+math OA, then C++/Java-depth screens). This page should get the OA; hire odds then track timed DS&A/math and whether the C++ plugin story survives a memory/threading grill.
- **Funnel filters:** Dayforce apply → OA (coding + math/probability) → technical screens (C++/Java depth; Python accepted on intern JD) → super day · 9-week onsite Greenwich · GPA ≥ 3.5 · preferred grad Dec 2027–May 2028.
- **Outside the resume:** Timed OA reps (DS&A mediums plus probability/logic) and a C++ threading/memory mock; a referral into the Greenwich loop beats another resume pass. No IBKR contact in `network.md`.
