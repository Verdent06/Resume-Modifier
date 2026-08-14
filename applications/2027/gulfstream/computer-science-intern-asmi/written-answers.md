# Gulfstream — Summer 2027 IEF ASMI College Associate Intern (Savannah) · Written Application Answers

Draft answers for SuccessFactors req `234996`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented CATIA/CAD automation, no VBA, no airframe or structures internships. Trim to the form's length limit before submitting.

This seat is a **CS tooling intern on ASMI**, not an airframe CAD designer. Lead with engineering applications, data pipelines, and database integration. CAD/CATIA is desired, not a filter. Do **not** screen yourself as ML-research, agentic-AI, or robotics.

Apply: https://careers.gulfstream.com/job/Savannah-Summer-2027-IEF-Advanced-Structures-and-Materials-(ASMI)-College-Associate-Intern-GA-31401/1417869000/?ats=successfactors

The posting does not list screening essays. SuccessFactors still usually asks knockouts plus an optional cover letter. Use the letter below if the form has an upload or "additional information" box.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/gulfstream/computer-science-intern-asmi/Vedant Desai Resume.pdf` |
| Cover letter | Paste the letter below if the form allows an upload or free-text |
| Location | **Savannah, GA** (onsite). Permanent residence: Michigan — more than 50 miles from Gulfstream (housing stipend applies). |
| Willing to work onsite / relocate | **Yes** — Savannah, Summer 2027, 12–14 weeks. Reliable transportation. |
| Currently enrolled full-time, pursuing bachelor’s or higher? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Will you have completed freshman year by the internship start? | **Yes** — rising junior by Summer 2027 |
| Graduation date | **May 2028** |
| GPA (unrounded; posting requires it on the resume) | **3.66 / 4.0** |
| Work authorization / sponsorship | **U.S. citizen.** Authorized to work in the United States **without visa sponsorship**. Not a current Gulfstream employee. |
| Reliable transportation | **Yes** |
| How did you hear about this role? | **Simplify** (https://simplify.jobs/p/c54661fa-4ea4-4783-b996-0470acb38ef8). If Simplify is not listed: **LinkedIn Jobs** / Other → Simplify. |
| Languages you can interview in | **Python, C++, SQL, TypeScript/JavaScript**. Do **not** check VBA, CATIA, or MATLAB. |

---

## Cover letter (paste if the form asks)

I am applying for the Summer 2027 Advanced Structures and Materials (ASMI) College Associate Intern role in Savannah. I want to spend the summer writing software that encodes a real engineering process — applications, data pipelines, and database integration that cut repetitive work — not a generic intern rotation. ASMI’s mandate (tools that capture design requirements and established process so structures engineers spend less time on the same pull) is the work I already do in Python, and I can be onsite for 12–14 weeks.

What I can defend:

- **Engineering applications and data pipelines.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced portal searches and hand-normalized Excel exports (~2 hours per committee) with a Requests + Pandas ETL, eliminating ~800 hours of manual pulls across 400 tracked PACs, then shipped a production Flask REST API on AWS EC2 into the nonprofit’s research workflow. I also built a deterministic aggregation engine so researchers stopped rebuilding spreadsheets to rank spenders.
- **Automation plus engineering-database integration.** I launched Vylet, turning a ~30-minute manual process per business into a Dockerized pipeline that produces 30 scored leads in 30 minutes (Redis/Celery), and wrote an asyncpg data layer with injection-safe SQL freshness checks so stale records re-scrape without a person in the loop. At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a unified PWSID entity database, automated sourcing that had been 15 hours/week of manual prospecting, and delivered 800+ validated Day-1 targets.
- **C++, honestly scoped.** I have not interned on CATIA or aircraft structures. I have shipped C++ that cannot miss a deadline: a real-time JUCE engine whose `processBlock()` path does not allocate or take a lock (per-voice `MemoryPool<Grain, 64>`, CMake VST3/AU release builds). That is deterministic engineering software under constraint, not a CAD internship. I would ramp on the team’s CATIA APIs; I will not pretend I have already written them.

I am a U.S. citizen and do not need sponsorship. GPA 3.66. Expected May 2028 — I return to Michigan after the internship. Permanent residence is more than 50 miles from Savannah.

Vedant Desai
vedantde@umich.edu | (248) 704-4852

---

## "Why Gulfstream / why ASMI?"

I want to apply computer science to aircraft-engineering productivity: software that captures a process, keeps data consistent, and removes repetitive work for the people who actually design the airplane. That is ASMI, not a web-only intern seat and not an ML-research rotation.

The closest analog I have is MDC (Pandas ETL + Flask API that replaced hundreds of hours of manual research) and Vylet/Lyndbrook (automation + entity databases). I have not shipped CATIA automation. I have shipped Python tools and C++ that has to be correct under a hard constraint. I can be onsite in Savannah for Summer 2027.

---

## "Tell us about a project you built" / additional information

**MDC (engineering application + pipeline).** Requests + Pandas ETL ingesting filings directly; Flask REST API on EC2 as sole engineer on a 5-month contract; ~800 hours of manual pulls removed across 400 PACs.

**Vylet (automation + database).** vyletdata.com. Dockerized pipeline, Redis/Celery, asyncpg DAL with SQL freshness gates. Live product.

**Granular synthesizer (C++).** github.com/Verdent06/granular-synth. Zero-allocation `processBlock()`, CMake VST3/AU binaries. Closest analog to "design, develop, test, and deploy" under a non-negotiable constraint — still audio DSP, not CATIA.

---

## Availability

Summer 2027, 12–14 weeks, onsite Savannah, GA. Available to start May 2027. Returning to the University of Michigan after the internship (Expected May 2028). Reliable transportation. Housing stipend: yes — permanent residence is Michigan, >50 miles from the site.

---

## Notes for the applicant (not for submission)

- **Do not claim CATIA, VBA, airframe design, or structures internships.** The JD lists CAD/CATIA as desired / "projects may include." Your pool has no CAD bullet. Honest Python pipelines + C++ systems beats a knockout lie.
- **Do not write a cover letter that sounds like an ML or robotics intern.** Hobbies on the JD include those; the requirements do not. Lead with MDC / Vylet / Lyndbrook.
- **GPA 3.66 is already on the resume** — the posting requires unrounded GPA on the page; do not omit it from the form either.
- **Location is not a skip.** Say yes to Savannah. Ask for the housing stipend; Michigan is >50 miles.
- **One opening, posted 2026-08-10.** Resume is the gate (`companies.md`: bottleneck resume, ~15–25%). Apply in this window.
- **Referral:** no Gulfstream contact in `network.md`. A UMich alum in GAC Engineering still beats a cold SuccessFactors pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
