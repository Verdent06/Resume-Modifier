# Software Engineer Intern (Summer 2027) at C3 AI

## Verdict

- **Score:** 10.0 / 10 (0 demerits — 0 emergency, 0 major, 0 minor)
- **Eligibility:** eligible — Pursuing BS CS (related: Economics double) at UMich; Expected May 2028 is a live Greenhouse option for this Summer 2027 intern req; still a student through the internship; US citizen / no sponsorship; OOP languages in inventory (TypeScript/C++/Python) satisfy "JavaScript, Java, or other OOP."
- **Track:** full-stack + enterprise AI application platform
- **Pipeline:** 1 cycle(s) · exit: zero_demerits

## Screen Review

### First read

- Vylet leads with a Dockerized LangGraph pipeline (30x), LangSmith eval (50%→90%), and a named production defect (79%→89%) — enterprise-AI *application* engineering registers in the first pass, not notebook ML.
- CaseStudyPrep.AI and MDC carry the product-SWE spine: client-side profiling/optimization (40% inference cost, 27% upload failures) and a production Flask REST API on AWS EC2 plus an ETL that replaces ~800 hours of PAC research.
- SignalWeaver (FastAPI + React/TypeScript) and Granular (C++ zero-alloc / lock-free SPSC) close JS-family OOP and "Java or similar" without inventing Java, Snowflake, Databricks, or C3 Suite. Binding ding: none at screen.

### Demerits

No demerits — clean screen.

### Misreads

- None material — the page reads as product/platform SWE who ships end-to-end apps, data tools, and optimization, not ML research and not FDE-only consulting.

### Interview angles

- **Lead with:** Vylet LangGraph + eval gates + name-collision debug; CaseStudyPrep ONNX VAD cost cut and RxJS/S3 upload repair; MDC sole-engineer Flask/EC2 plus PAC ETL; SignalWeaver FastAPI p50/p99 and React/TypeScript UI; Granular zero-alloc `processBlock` and lock-free SPSC as Platform OOP/profiling
- **Defend:** No Java — JD is "JavaScript, Java, or other OOP" / Platform "Java or similar"; TypeScript, C++, and Python are the honest interview languages. No Snowflake, Databricks, Copilot, Fusion, Tableau, or C3 Suite usage — do not claim them. Redwood City HQ 5 days/week is a yes. Granular is C++ systems discipline for Platform, not a music-hobby skip
- **Depth prep:** Timed HackerRank 2–3 Med–Hard LC (OA is the intern bottleneck); OOP + profiling walkthroughs (Vylet eval, CSP cost/reliability, Granular real-time constraints); light intern sys design possible after OA; behavioral is a filter (`recruiting.md` §6)

## Likelihood

- **Resume screen:** High — full-stack APIs/deploy, TypeScript and C++ through use, and production optimization numbers all register in one pass; Expected May 2028 matches the Greenhouse window
- **Overall hire odds:** Medium — B-tier ~3–8% with HackerRank OA as the intern bottleneck (`companies.md`; `recruiting.md` §1/§8). A clean PDF still dies on 2–3 Med–Hard LC if unprepared; light intern sys design and a screen follow
- **Funnel filters:** Greenhouse resume → HackerRank OA (2–3 Med–Hard LC) → screen → 2 coding + possible light sys design → HR · 4–6 rds · Bottleneck: OA · ~3–8% **[directional]** · HQ 5 days/week Redwood City · no sponsorship
- **Outside the resume:** Apply now (rolling Greenhouse 8739037002); drill HackerRank/LC mediums under a timer; a Redwood City alum referral still beats cold
