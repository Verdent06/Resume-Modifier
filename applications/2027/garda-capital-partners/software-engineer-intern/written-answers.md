# Garda Capital Partners — Software Engineer Intern · Screening Answers

Draft answers for Garda’s Greenhouse application (job 6146213004, https://job-boards.greenhouse.io/gardacp/jobs/6146213004). Grounded in `context.md` identity and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented trading-desk internship, metrics, GitHubs, or forbidden tools (Snowflake, Databricks, Copilot, Fusion, Tableau). Trim to each form’s length limit before submitting.

Apply: https://job-boards.greenhouse.io/gardacp/jobs/6146213004

---

## Identity

- **First Name:** Vedant
- **Last Name:** Desai
- **Email:** vedantde@umich.edu
- **Country:** United States
- **Phone:** (248) 704-4852
- **Location (City):** Ann Arbor, MI
- **LinkedIn Profile:** https://linkedin.com/in/vedantde06
- **Website:** — (none in `context.md`; leave blank)
- **GitHub:** https://github.com/Verdent06
- **Resume/CV:** attach `Vedant Desai Resume.pdf` from this folder

---

## Knockouts / facts

**Are you authorized to work in the United States?**
Yes. US citizen.

**Do you now, or will you in the future, require sponsorship for employment visa status (e.g., H-1B, etc.) to work legally for Garda Capital Partners in the United States?**
No.

Facts if a recruiter asks (not extra form fields):
- University of Michigan — B.S. Computer Science and Economics
- GPA 3.66 / 4.0
- Expected May 2028
- US citizen; no sponsorship

---

## Cover letter (optional)

I want to write software that has to be correct, supportable, and shipped — Python and SQL in production, with enough C++ that I can defend a hot path. Garda’s Software Engineer Intern role on the New York Research and Technology team is that job: new lines of business in Python and SQL, complete front-office/risk solutions with senior staff, and support for in-house and third-party applications. I am applying as an engineer, not as a trader.

The work I already do sits on that axis. In Python I delivered a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract, replacing manual campaign-finance pulls with a Requests + Pandas ETL. I also run Vylet, a live lead-sourcing product ($1,500 MRR): an asyncpg data layer with injection-safe SQL timestamp validation, and a name-collision bug I diagnosed and fixed that lifted qualification from 79% to 89%. In C++ I built a granular synthesizer in JUCE where `processBlock()` cannot allocate or take a lock — a per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO — and I ship it as VST3/AU. I do not have a trading-desk internship and I have not worked a fixed-income relative-value book. I do have CS + Economics at Michigan (Expected May 2028, GPA 3.66), I am a US citizen, and I built SignalWeaver as a financial-research assistant (not investment advice) with measured p50/p99 on FastAPI scoring and pgvector search.

I am available onsite in New York for Summer 2027 and return to Michigan after the internship. I want a summer next to R&T engineers who treat complete, supportable solutions as the job — including writing and debugging without an assistant when that is what the system needs.

---

## Notes for the applicant (not for submission)

- **Do not invent a trading-desk or FI internship.** Fit is project match: MDC/Vylet (Python+SQL production) + Granular (C++) + SignalWeaver (financial-research systems). Garda’s plus is interest in fixed income, not prior desk time.
- **Do not name Snowflake, Databricks, Copilot, Fusion, or Tableau.** Not in inventory and not on this JD.
- **Do not lead with LoRA / LangGraph / agent pipelines** on the call. This is enterprise R&T SWE; AI-assisted workflows are a plus only if you can still write and debug unaided — use the Vylet name-collision fix and the Granular real-time checklist.
- **SignalWeaver GitHub is real:** https://github.com/Verdent06/SignalWeaver — also link granular-synth: https://github.com/Verdent06/granular-synth
- **Website:** leave blank. No portfolio URL in `context.md`.
- **OA is the real gate after the resume.** Platform unpublished; candidate reports mix timed math/verbal with SQL/LeetCode-medium coding. Timed Python + SQL + DS&A until a medium is a ~20-minute solve (`recruiting.md`: intern OA; mid-size/quant-adjacent is resume + OA).
- Comp on the posting is a Greenhouse $50–$50 placeholder — do not invent a base number if a form asks.
- Apply URL: https://job-boards.greenhouse.io/gardacp/jobs/6146213004
