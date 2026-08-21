# Databricks — Software Engineering Intern (2027 Start) – Winter · Written Application Answers

Draft answers for Databricks university-recruiting Greenhouse (`P-1588`, embed `8732364002`). Grounded in `persona.md` (recruiter lens) and `context.md` identity. First-person, honest, defensible under “walk me through this” — no invented tools, metrics, Java, or Databricks product experience (Lakehouse, Unity Catalog, Spark-as-employer, Genie, Lakebase, Agent Bricks, Lakeflow). No Snowflake, Copilot, Fusion, or Tableau. Trim to each form’s length limit before submitting.

**Do not submit from this run.** Artifacts only.

ATS: https://www.databricks.com/company/careers/university-recruiting/software-engineering-intern-2027-start---winter-8732364002
Jobright: https://jobright.ai/jobs/info/6a8791cd25fc4e7ae3dadd36
Resume: `applications/2027/databricks/software-engineer-intern-winter/Vedant Desai Resume.pdf`

This req is **Winter 2027 (January–April) only**. One application per 30 days. This apply location: **Bellevue, WA**. Greenhouse has **no cover-letter upload** — the letter below is for email/recruiter, not a form field.

---

## Knockout / structured fields (fill exactly)

Questions and dropdowns captured from the live Greenhouse form on the ATS page (not submitted).

| Field (exact form wording) | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Preferred First Name | Vedant |
| Email * | vedantde@umich.edu |
| Country * | **United States +1** |
| Phone * | (248) 704-4852 |
| Location (City) * | Ann Arbor, MI (school city on the resume). Other 2027 apps use Northville, MI for mailing; do not invent a zip. |
| Resume/CV * | `applications/2027/databricks/software-engineer-intern-winter/Vedant Desai Resume.pdf` (pdf) |
| School * | **University of Michigan - Ann Arbor** (typeahead) |
| Degree * | **Bachelor's Degree** — B.S. Computer Science and Economics |
| End date month * | **May** |
| End date year * | **2028** |
| Please provide a recent transcript * | Upload your real UMich transcript. **No transcript file is in this repo — do not invent one.** |
| Please provide a recent transcript of your graduate studies (If applicable) * | **Skip.** Undergraduate only. If Greenhouse blocks submit, upload a one-line PDF that says not applicable / no graduate studies — never a fake transcript. |
| What is your graduation date? * | **Spring 2028** (options: Earlier than Fall 2027 / Fall 2027 / Spring 2028 / Later than Summer 2028) |
| What is your GPA? * | **3.6 or above (out of 4.0)** — actual GPA **3.66 / 4.0** (convert-to-4.0 note is on the form) |
| Please choose the single location that you're the most interested in… * | **Bellevue, WA** (not Mountain View, San Francisco, or Vancouver). Form note: Vancouver is **not** available for Winter. |
| LinkedIn Profile * | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 (optional field; GitHub is the honest site) |
| How did you hear about this job? * | Jobright is **not** a listed option. Listed: LinkedIn Job Posting / Recruiter Reach Out / BrickFest / School Career Fair and/or Event / Referral from Employee / Referral from Intern / I am a previous Databricks intern. **Do not pick referral or previous intern.** Least-wrong public-board pick: **LinkedIn Job Posting**. |
| Are you legally authorized to work in the country in which you are applying? * | **Yes** — US citizen |
| Do you now or will you in the future need sponsorship for employment visa status in the country in which you are applying? * | **No** |
| Do you currently or have you previously worked for Databricks in the past? * | **No** |
| Please confirm whether any of the below applies to you… (sanctions / export controls) * | **None of the above** |
| If you selected a response to the prior question other than “none of the above”… | **Not applicable (i.e., I selected "none of the above" for the prior question)** |
| Gender / Hispanic/Latino / Race / Veteran / Disability (CC-305) | Voluntary EEO. Decline if you do not want to answer. Do not invent. |

Cover letter upload: **not on this form.**

---

## Cover letter (not a Greenhouse field — recruiter / email)

I am applying for the Software Engineering Intern (2027 Start) – Winter role in **Bellevue** (P-1588). I want a Winter 2027 intern project I own end-to-end — design, code, review — on a data-and-AI infrastructure platform, not a notebook-ML rotation and not a product-usage internship. I have not used Databricks products (Lakehouse, Unity Catalog, Spark, Genie, Lakebase, Agent Bricks, Lakeflow) and I will not pretend I have. What I can defend is shipping data systems and systems software in Python and C++.

The closest work I have to “move data, serve it, keep it correct”:

- **Michigan Data Consulting → Michigan Campaign Finance Network.** Sole engineer on a five-month contract. I replaced portal-search / hand-normalized Excel pulls (~2 hours per committee) with a Requests + Pandas ETL, eliminating ~800 hours of manual pulls across 400 tracked PACs, and shipped a production Flask REST API on AWS EC2 into the nonprofit’s research workflow.
- **SignalWeaver.** Async FastAPI scoring instrumented at 9.1s p50 / 15.2s p99 across 90 tickers; pgvector cosine search at 49ms p50 / 99ms p99; Docker Compose + GitHub Actions (frontend build, pytest, API image). Storage/query-adjacent platform work, not a Databricks stack claim.
- **Vylet.** Live lead-sourcing product ($1,500 MRR, three clients). I wrote a custom asyncpg data-access layer with injection-safe SQL freshness checks, and I diagnosed a name-collision defect in ownership-verification that lifted qualification from 79% to 89% with no change in sourcing volume.
- **Granular synthesizer (C++/JUCE).** The audio thread cannot heap-allocate or take a mutex: per-voice `MemoryPool<Grain, 64>` and a lock-free SPSC FIFO with acquire/release atomics. That is the concurrency discipline I would walk into a single-machine concurrency round with — I do not have a callback-latency number on the resume, and I will say so.

I graduate **May 2028** (Spring 2028) with a B.S. in **Computer Science and Economics** from the University of Michigan, GPA **3.66 / 4.0**. I am a **US citizen**, legally authorized to work in the US, and I **do not need sponsorship**. I can be in Bellevue for Winter 2027 (January–April) and I return to school after. Java is not in my inventory; Python and C++ are.

---

## Notes for the applicant (not for submission)

- **Do not claim Databricks products or Snowflake / Tableau / Copilot / Fusion.** The JD is a generic SWE intern req; product names are an anti-pattern in `persona.md`.
- **Do not invent Java.** JD lists Python, Java, or C++ as examples. Python and C++ are the honest languages.
- **Location:** Bellevue this apply. Do not also fire Mountain View / SF — one application per 30 days.
- **Transcript** is required; graduate transcript is “if applicable.”
- **OA after the PDF:** CodeSignal (intern reports: ~70 min / 4Q), then a concurrency round that `companies.md` names as the bottleneck. Drill single-machine concurrency (mutexes, atomics, lock-free SPSC) using Granular as the story, not Spark.
- **Behavioral:** MDC sole-engineer stakeholder delivery is the end-to-end ownership story. Vylet 79%→89% is the defect/quality story. Granular `processBlock()` is the concurrency story.
