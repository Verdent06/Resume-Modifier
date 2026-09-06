# Schonfeld — 2027 Software Engineering Intern · Screening Answers

Draft answers for Schonfeld’s Greenhouse application (job **8180089**). Grounded in `persona.md` (full-stack intern: C++ / Python through use, Git and databases, shipped ownership, markets curiosity — **not Java**, **not** a trading-desk internship, **not** LoRA/LangGraph lead) and the form kit. First-person, honest, defensible under “walk me through this.” Trim to each field’s length limit before submitting.

Apply (do **not** submit from this agent):

- ATS: https://job-boards.greenhouse.io/schonfeld/jobs/8180089
- Embed: https://boards.greenhouse.io/embed/job_app?token=8180089

Simplify listing (redirected): https://simplify.jobs/p/1679d1fa-953d-4b83-b4f5-e2e3a9f4cdd0

**This agent did not submit.** Form fields captured from the live Greenhouse embed + jobs API (2026-09-06).

**SHA-256:** `315720a9ae2d2f2c20b471ce5d9135c2606b164dcc182916f5e5ffaf528a5ab0`

**Form-kit identity (use on Greenhouse — never `vedantde@umich.edu`):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · Address **49032 Freestone Dr, Northville, MI 48168** · US citizen, no sponsorship · GPA **3.66** · Expected **May 2028** · Junior · LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06 · SAT **1510** if asked · DOB **12/16/2006** if asked · valid US DL **Yes** if asked.

The resume PDF header still uses `vedantde@umich.edu` from `template.tex`. The **form** uses verdent06@gmail.com.

---

## Identity (live Greenhouse)

| Exact label | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | **verdent06@gmail.com** |
| Country | **United States** |
| Phone * | **248-704-4852** |
| Location (City) * | **Northville, Michigan, United States** (Locate me if it resolves to Northville; not Ann Arbor) |
| Resume/CV * | attach `applications/2027/schonfeld/software-engineering-intern/Vedant Desai Resume.pdf` (pdf) |
| Cover Letter | optional — paste the draft below, or attach as pdf/docx |
| LinkedIn Profile | https://www.linkedin.com/in/vedantde06 |
| Website | leave blank (no portfolio URL in `context.md`). GitHub is on the PDF. |

---

## Education widget (required)

Greenhouse typeahead (`Select...`). This agent did not create an account or exhaust the school catalog.

| Exact label | Answer |
| --- | --- |
| School | Type **University of Michigan**. Also try **University of Michigan-Ann Arbor** / **University of Michigan - Ann Arbor**. If the catalog misses it, pick the closest official row — do not invent a school. |
| Degree | **Bachelor's** / **Bachelor of Science** if listed |
| Discipline | **Computer Science** (dual CS + Economics is on the PDF; do not invent a second row unless required) |
| Start date month / year | **August** **2025** |
| End date month / year | **May** **2028** (expected; not graduated) |

If a second education row is required: Northville High School, Northville MI, graduated **05/19/2025**.

---

## Knockouts (required Yes/No)

| Exact label | Answer | Why |
| --- | --- | --- |
| What is your current cumulative GPA? * | **3.66** | `context.md` |
| What degree are you currently pursuing? * | **Bachelor's** | Options: Bachelor's / Master's / PhD / Other |
| Are you authorized to work in the United States? * | **Yes** | US citizen |
| Do you now, or will you in the future, require sponsorship for employment visa status to work legally in the United States? * | **No** | US citizen; no sponsorship |
| Are you graduating in the summer or fall of 2027? * | **No** | Expected **May 2028**. **Do not answer Yes** to pass a filter. If they auto-reject No, this req wanted a 2027 grad — walk away. |

---

## Cover letter (optional)

I want to write software that has to ship, stay up, and stay fast. Schonfeld’s 2027 Software Engineering Intern role is that job: ten weeks in New York on the Technology division, assigned to Treasury or Compliance, writing software that improves the research and trading platform — functionality, performance, stability, efficiency, scalability — next to a manager and a mentor, with a summer-long project I present at the end. I am applying as an engineer. I do not have a trading-desk internship, and I will not pretend I have built an OMS.

The work I already do sits on that axis. In Python I delivered a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract, replacing manual campaign-finance pulls with a Requests + Pandas ETL. I also run Vylet, a live PE/search-fund lead product ($1,500 MRR): an asyncpg data layer with injection-safe SQL timestamp validation, and a name-collision bug I diagnosed and fixed that lifted qualification from 79% to 89%. In C++ I built a granular synthesizer in JUCE where `processBlock()` cannot allocate or take a lock — a per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO — and I ship it as VST3/AU. I am a US citizen. I have CS + Economics at Michigan (Expected May 2028, GPA 3.66), and I built SignalWeaver as a financial-research assistant (not investment advice) with measured p50/p99 on FastAPI scoring and pgvector search, plus GitHub Actions CI.

I can work onsite in New York for the 10-week Summer 2027 program and I return to Michigan after (Expected May 2028 — I am **not** graduating summer or fall 2027). I want a summer next to engineers who treat production correctness as the job.

---

## Demographics (voluntary)

Skip, or complete only if you want. Not used in this packet. Options: gender (Male / Female / Prefer not to say); Hispanic/Latino Yes/No; race (EEOC list). Whatever you choose, it is not a knockout.

---

## Notes for the applicant (not for submission)

- **Do not invent Java or a trading-desk / Treasury / OMS internship.** Interview in C++ or Python. Java is named on the JD as one of several languages, not an exclusive gate.
- **Do not name Snowflake, Databricks, Copilot, Tableau, Fusion, or Sentry.** Not in inventory.
- **Do not lead with LoRA / LangGraph / agent pipelines.** This is Treasury/Compliance platform SWE.
- **SignalWeaver GitHub is real:** https://github.com/Verdent06/SignalWeaver — also https://github.com/Verdent06/granular-synth
- **Graduating summer/fall 2027 = No.** Expected May 2028. Honest answer.
- **OA is the real gate after the resume.** Platform unpublished. Timed C++/Python until a medium is a ~20-minute solve (`recruiting.md`: intern OA).
- No Schonfeld contact in `network.md` — do not claim an employee referral.
- Comp: $125,000–$145,000 annualized, prorated to 10 weeks (JD). Simplify: $60.10–$69.71/hr.
