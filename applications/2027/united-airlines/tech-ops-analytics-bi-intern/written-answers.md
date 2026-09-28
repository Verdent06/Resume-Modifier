# United Airlines — Intern - Tech Ops Analytics & Business Intelligence (Summer 2027) · Written Application Answers

Draft answers for Phenom careers → **Taleo** apply (req **WHQ00026447**). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Power BI, Tableau, Snowflake, Databricks, Copilot, Fusion, Sentry, or airline/MRO experience.** Trim to the form's length limit before submitting.

This posting is the **Tech Ops Analytics & BI Intern** seat — **not** Digital Technology SWE, **not** a maintenance-base wrench intern. Chicago WHQ (Willis Tower), onsite, Summer 2027, $20/hr, 2 seats.

Careers: https://careers.united.com/us/en/job/WHQ00026447
Taleo: https://ual-pro.taleo.net/careersection/10400/jobdetail.ftl?job=WHQ00026447

Window printed on the JD: **September 1, 2026 through September 15, 2026**. Recruiter: Anthony Sykes (`anthony.sykes@united.com`).

---

## Apply-path note (read first)

Phenom `directApply` is **false**. The careers page may show "no longer accepting new applications" even while `reqStatus` is Open and `postingEndDate` is 2026-09-15. Unauthenticated Taleo returned **"The job is no longer available"** on 2026-09-03. Two seats; window is two weeks. Try Taleo signed-in apply anyway; if it is truly closed, do not invent a workaround — the packet is still the resume to send if they reopen or if a recruiter asks.

**This agent did not submit.**

---

## Form-kit identity

The resume PDF header still uses the school email from `context.md`. That is the document. **The form uses gmail only.**

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | **verdent06@gmail.com** (never `vedantde@umich.edu` on the form) |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/united-airlines/tech-ops-analytics-bi-intern/Vedant Desai Resume.pdf` |
| School email (if a second field) | vedantde@umich.edu — only if they ask for a university address; primary login/contact is gmail |
| Location | **Chicago, IL — onsite Willis Tower WHQ.** Willing to relocate for Summer 2027. |
| Work model | Onsite, 40 hrs/week, Summer 2027 |
| Degree | B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| GPA | **3.66 / 4.0** (no floor on this JD) |
| Class standing | Junior applying for Summer 2027 (Expected May 2028) |
| Returning to school after internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| Authorized to work in the US for any employer without sponsorship? | **Yes** |
| Taleo: "Are you currently being sponsored for employment visa status (e.g., H-1B, TN, E-3, etc.), or do you now or will you in the future require sponsorship for such status?" | **No** |
| Pay | Accept posted intern rate: **$20.00/hr** |
| How did you hear about this role? | **Company website / United careers** (or the board you actually used). No United contact in `network.md` — do not invent a referral. |

---

## Cover letter / "Why United / why Tech Ops Analytics?" (paste if the form has a box)

I am applying to the Summer 2027 Intern - Tech Ops Analytics & Business Intelligence seat (req WHQ00026447) on the Technical Operations Analytics team in Chicago — not a Digital Technology SWE intern, and not a maintenance-base seat.

I want to spend the summer on the work this team actually does: query, transform, and model operational data, find gaps, and turn that into a decision a maintenance or supply-chain SME can use — right work, right aircraft, right location, right time. I have not interned on aircraft or MRO systems. I have shipped the data path — messy sources in, a ranking or score out, a number on what it saved.

What I can defend:

- **Messy ingest → ETL → ranked insight.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I scoped delivery with MCFN stakeholders as the only engineer on the contract.
- **Fleet-style scoring / right-work analog.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a PWSID entity database for a search fund targeting water-utility operators and delivered 800+ Day-1 targets. A Review Velocity score proxied fleet expansion and operational scale from public compliance data and cut that list to 280 leads at 35% precision against their revenue criteria.
- **SQL + a dashboard, not Power BI.** On Vylet I own a production asyncpg DAL with injection-safe SQL freshness checks that trigger re-scrapes. On SignalWeaver I built a React/TypeScript dashboard over scores persisted in Postgres and served them through FastAPI.

I have not used Power BI, Tableau, Snowflake, or Databricks. I would ramp on the team's approved stack rather than pretend I already have it.

I can be onsite in Chicago for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship. I accept the posted intern rate ($20.00/hr).

Vedant Desai
verdent06@gmail.com | (248) 704-4852

---

## "Tell us about a project" / data visualization / SQL / Python

**MDC (messy filings → Pandas ETL → ranked report).** Irregular Excel exports and portal caps; ~800 hours / 400 PACs. This is the grounded messy-dataset + SME story — do not invent an aircraft dataset.

**Lyndbrook (entity DB + fleet scoring).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision. Water-utility operators, not airline MRO. Say that out loud if they ask about domain.

**Vylet (SQL).** asyncpg DAL; stale-timestamp checks; automatic re-scrapes. The bullet has no sized freshness metric — walk the outcome in interview, do not invent a number.

**SignalWeaver (visualization analog).** React dashboard; FastAPI; scores persisted in Postgres. Research assistant, not investment advice. **Do not call this Power BI.**

---

## GenAI preferred (if asked)

Honest: LangSmith eval + Pydantic consensus gates on Vylet (extraction faithfulness 50% → 90%); LoRA fine-tune on SignalWeaver with a held-out test set. That is validation of model output, not "I use Copilot." Do not claim Copilot, Fusion, or Sentry. Do not oversell genAI — it is preferred United intern language, not the job.

---

## Availability

Summer 2027, **onsite Chicago WHQ**. Available to start May/June 2027 (typical United intern ~12 weeks). Returning to the University of Michigan after the internship (Expected May 2028). Can travel.

---

## Notes for the applicant (not for submission)

- **Form email is verdent06@gmail.com only.** Resume PDF still shows vedantde@umich.edu from `context.md`.
- **Sponsorship → No.** Work-authorized; no sponsorship now or later.
- **Do not claim Power BI, Tableau, Snowflake, Databricks, Copilot, Fusion, or Sentry.** JD says PowerBI *or other visualization tools*. React dashboard is the analog (`persona.md`).
- **Do not invent airline/MRO/aircraft experience.** Map ETL + fleet-style scoring; say the domain gap out loud.
- **SQL metric is out of rails.** The only SQL pool bullet has no impact number (`grade.md`). Walk freshness/re-scrape; do not fabricate a %.
- **Apply path is Taleo, not Phenom.** Careers overlay + unauthenticated Taleo both looked closed on 2026-09-03. If signed-in Taleo still rejects, stop — 2 seats may already be filled.
- **No United contact in `network.md`.** Do not invent a referral (`recruiting.md`: HM > recruiter > engineer > cold apply). Recruiter on the req: Anthony Sykes.
- **Pay $20/hr.** Accept it. Do not negotiate intern rate on the form.
