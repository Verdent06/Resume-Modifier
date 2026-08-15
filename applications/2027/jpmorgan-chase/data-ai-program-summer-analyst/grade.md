# 2027 Data & AI Program – Summer Internship – Analyst at JPMorgan Chase

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — Expected May 2028 falls in the JD window (December 2027–August 2028); B.S. Computer Science is a listed quantitative/technical discipline; returns to school after Summer 2027; posting requires permanent U.S. work authorization and offers no OPT/CPT/sponsorship
- **Track:** ai-ml + fintech-backend / enterprise financial-services platforms
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Vylet leads with a Dockerized LangGraph pipeline, LangSmith eval (50%→90% faithfulness), and SQL in a production DAL — applied data/AI with PE/search-fund identity, not notebook ML.
- MDC Pandas ETL (~800 hours / 400 PACs) plus Flask/AWS and Lyndbrook's scoring shortlist (35% precision) read as data platforms, messy datasets, and measured experiments; SignalWeaver closes with LoRA 81%→96% held-out and an out-of-sample regression.
- Binding ding: the SQL proof and the production API closer are unquantified, and the JD's "agent-based" phrasing never appears as a word.

### Demerits

- **minor** · `Vylet` · SQL/DAL bullet metric-free — The asyncpg/SQL freshness bullet is the only on-page SQL proof, but it closes on architecture (re-scrapes, injection-safe timestamps) with no sized impact — a Data & AI screener cannot tell how much the DAL moved the pipeline.
- **minor** · `Michigan Data Consulting (MDC)` · API bullet metric-free — The Flask/EC2 delivery line is the production-platform closer after a strong ETL hook, but it has no throughput, latency, or adoption number — the 5-month sole-engineer frame sizes tenure, not impact.
- **minor** · `resume` · agent-based never named — The JD screens for generative AI and agent-based solutions; LangGraph + LangSmith eval is that work in substance, but neither 'agent' nor 'agent-based' appears in bullets or Skills, so a keyword-first pass can under-register the construct.

### Misreads

- A keyword-first pass for "agent" / "agent-based" can bucket this as generic data-engineering + a chatbot-adjacent LangGraph pipeline rather than the JD's agent-based AI path.
- The SQL/DAL line can read as database plumbing rather than the language-floor proof a Python+SQL Analyst screen is looking for, because it never sizes the freshness win.

### Interview angles

- **Lead with:** Vylet LangGraph pipeline + LangSmith eval (20 adversarial cases, Pydantic consensus gates, 50%→90% faithfulness) as the agent-based analog; MDC Requests+Pandas ETL on irregular filings; SignalWeaver LoRA + held-out accuracy and out-of-sample regression; Lyndbrook Review Velocity shortlist
- **Defend:** SQL is on the page only in the unquantified DAL bullet — walk re-scrape/freshness as the outcome even though the line has no number *(out of rails: only SQL pool bullet has no impact metric; swapping it drops SQL-through-use)*. Flask/EC2 is tenure-and-stack — pair it verbally with the 800-hour ETL *(out of rails: MDC pool has no metric-bearing API bullet)*. Say "agentic/LangGraph" out loud; the page never uses the word *(out of rails: no pool bullet names agent/agentic; Agentic Workflows in Skills failed the orphan gate)*. No Snowflake, Databricks, Copilot, Fusion, or Tableau — do not invent them
- **Depth prep:** LangSmith eval failure modes and consensus gates; LoRA data split / overfit story; SQL+Python Easy–Med coding (HackerRank analog unpublished for this 2027 Analyst req); HireVue STAR on stakeholder-scoped delivery (MDC/Lyndbrook); data governance/privacy talking points the resume implies but does not name

## Likelihood

- **Resume screen:** High — Python/SQL through use, Pandas ETL, LangGraph+eval, LoRA with held-out accuracy, scoring/precision, AWS, and PE/financial-research identity all register in one pass; GPA 3.66 and stats coursework clear the intern ML bar
- **Overall hire odds:** Medium — B-tier intern funnel with rolling fill; the resume is on-axis for the Analyst program, but HireVue plus a likely unpublished HackerRank still eliminate after a clean screen, and the SWE-row ~8–12% is a ceiling analog not this program's published rate
- **Funnel filters:** Complete application + resume review against required qualifications (rolling classes). 2027 Data & AI posting names no OA; predecessor Data Science Analyst loops reported HackerRank + HireVue before further review. No sponsorship / no OPT/CPT. Section 19 FDIA conviction review. Bottleneck analog: tech rounds (`companies.md` JPMorgan Chase B-tier) after the screen
- **Outside the resume:** Apply in the first rolling wave; no Data & AI Analyst OA is published so prep HireVue STAR plus Easy–Med SQL/Python coding; a referral into the program beats cold Workday
