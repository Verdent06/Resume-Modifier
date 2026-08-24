# AbbVie — 2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) · Written Application Answers

Draft answers for SmartRecruiters job `3743990014697918`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — **no invented Java, Spring Boot, Vue.js, NodeJS, R, APEX, or pharma internships.** Trim to the form's length limit before submitting.

This posting is **dual-track**. Recruiting aligns you to **Data Engineering** or **Software/Application Engineering**. Prefer **Data Engineering** first (Python/SQL/APIs/ETL is the pool). Software/Application second as Python + TypeScript full-stack (Flask/FastAPI + React). Do **not** volunteer Java/Vue/APEX. Generative AI only as tools on shipped pipelines (Vylet LangGraph, SignalWeaver embeddings) — not as an ML-research intern.

Apply: https://jobs.smartrecruiters.com/AbbVie/3743990014697918

Extern intern guide (directional): resume + cover letter + transcripts; apply in the first 4–6 weeks of the posting; rolling.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| Address | 49032 Freestone Dr, Northville, MI 48168 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/abbvie/bts-intern-data-software-engineering/Vedant Desai Resume.pdf` |
| Cover letter | Paste the letter below if the form has a box or upload. Extern says intern applications typically include one. |
| Transcript | Unofficial UMich transcript if asked. GPA **3.66 / 4.0** is on the resume. |
| Location preference | **Lake County / North Chicago, IL** (majority BTS intern placement). Other U.S. AbbVie or Allergan Aesthetics sites are acceptable if they place you there. |
| Willing to work onsite 11 weeks / relocate | **Yes** — North Chicago / Lake County, Summer 2027, 11 weeks onsite. Relocation support is listed for eligible students; I will use it if offered and arrange housing either way. |
| Currently pursuing Bachelor's in CS / CE / AI or related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** (inside December 2027 – June 2028) |
| Enrolled the semester after the internship? | **Yes** — Fall 2027 and Winter 2028 remain. Graduate May 2028 (within one year post-internship). |
| GPA | **3.66 / 4.0** (preferred cutoff 3.00) |
| Work authorization / sponsorship | **U.S. citizen.** Authorized to work in the United States **without visa sponsorship** now or in the future. |
| How did you hear about this role? | **SmartRecruiters / AbbVie careers** (this URL). If a source list includes Other, use that. Do not invent a referral — none in `network.md`. |
| Pay $21.00–$37.80/hr | **Yes** — accept the posted intern range |
| Languages you can interview in | **Python, SQL, TypeScript/JavaScript (React, Angular), HTML/CSS, C++.** Do **not** check Java, Spring Boot, Vue.js, NodeJS, R, APEX, or Salesforce. |
| Track preference (if asked) | **Data Engineering** first. **Software/Application Engineering** second (Python + TypeScript full-stack). |

---

## Cover letter / "Why AbbVie / why BTS?" (paste if the form has a box)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

AbbVie — 2027 Business Technology Solutions Intern, Data & Software Engineering (Undergraduate)
North Chicago / Lake County, IL (onsite)

I am applying for the Summer 2027 BTS intern role (SmartRecruiters 3743990014697918). I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen, I do not need sponsorship, and I can be onsite in Lake County for the 11-week program. I return to Michigan in Fall 2027.

I want this seat because BTS builds the applications and data infrastructure scientific and commercial teams actually run on — not a notebook rotation and not a help-desk intern. My work is already that shape: ingest messy sources, ship an API or pipeline, measure what it saved.

What I can defend on day one:

- **Data engineering.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and a production Flask REST API on AWS EC2, eliminating ~800 hours of manual pulls across 400 tracked PACs. At Lyndbrook I aggregated EPA ECHO and MassGIS into a PWSID entity database and delivered 800+ Day-1 acquisition targets. On Vylet I own a Dockerized LangGraph pipeline with Redis/Celery and an asyncpg layer whose injection-safe SQL timestamp checks trigger re-scrapes when records go stale.

- **Software / application engineering, honestly scoped.** I ship Python APIs (Flask, FastAPI) and TypeScript UIs (React on SignalWeaver; Angular on CaseStudyPrep.AI). I have a public GitHub. I have not used Java, Spring Boot, Vue.js, NodeJS, R, or APEX; I would ramp on the team's stack the same way I ramped onto Flask, FastAPI, and React — by shipping on it.

I prefer the Data Engineering track. I can do Software/Application as Python + TypeScript full-stack. I am not applying as an ML-research intern.

Sincerely,
Vedant Desai

---

## "Why AbbVie / why this internship?" (short form)

I want a summer on a team that ships enterprise software and data platforms for people who have to make decisions — scientific or commercial — not a generic web rotation. AbbVie BTS is that: pipelines, APIs, and internal apps next to immunology, oncology, and neuroscience operations.

The work I can defend:

- **Data Engineering.** MCFN: Requests + Pandas ETL and a Flask REST API on EC2 (~800 hours / 400 PACs). Lyndbrook: EPA ECHO + MassGIS → PWSID entity database, 800+ targets. Vylet: Dockerized pipeline, Redis/Celery, SQL freshness checks.
- **Software/Application.** FastAPI + React/TypeScript + Postgres/pgvector on SignalWeaver; Flask on EC2. Public GitHub. No Java, Vue, or APEX in my pool — I will not pretend.

I can be onsite in Lake County for 11 weeks, Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

---

## "Tell us about a project you built" / additional information

Three that map onto this req without inflating the stack:

**MDC (messy filings → Pandas ETL → Flask API).** Irregular Excel exports and portal caps; sole engineer, five-month MCFN contract; production Flask REST on AWS EC2; ~800 hours / 400 PACs. Closest analog to "integrate data sources and serve them."

**Vylet (pipeline + SQL).** vyletdata.com. Dockerized LangGraph, Redis/Celery, 30 scored leads in 30 minutes (30×). asyncpg DAL with injection-safe SQL freshness checks. Named defect: name-collision in ownership verification, qualification 79% → 89% with no change in sourcing volume.

**Lyndbrook (regulated public data → entity database).** EPA ECHO + MassGIS → unified PWSID database; 800+ Day-1 targets; Google Maps API cross-ref on 2,500+ legal entities. Water-utility operators, not pharma. Say that out loud if they ask about domain.

**SignalWeaver (full-stack + serve).** github.com/Verdent06/SignalWeaver. FastAPI REST, React/TypeScript, pgvector search (49ms p50 / 99ms p99). Research assistant, not investment advice. 9.1s p50 is batch research latency, not an interactive SLA.

---

## "Tell us about a time you showed initiative / solved a problem / worked with stakeholders"

**Initiative / defect.** On Vylet, ownership-verification was dropping valid targets that shared a name with an unrelated business in another geography. I traced it to a name-collision in the verification logic, fixed the match, and the qualification rate went from 79% to 89% with zero change in sourcing volume.

**Stakeholders.** At MCFN I was the only engineer on the contract. Researchers were spending ~2 hours per committee on portal searches and irregular Excel exports. I scoped ingest through REST endpoints with them — no backend team behind me — and shipped the Flask API on EC2 into their public research workflow.

**Regulated data, honest scope.** Lyndbrook: public EPA/MassGIS compliance data into a single entity key (PWSID), not an AbbVie or clinical dataset. I have not interned in pharma.

---

## Availability

Summer 2027, 11 weeks, onsite Lake County / North Chicago, IL (or another U.S. AbbVie / Allergan Aesthetics site if that is the placement). Available to start late May / early June 2027. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Do not claim Java, Spring Boot, Vue.js, NodeJS, R, APEX, Salesforce, or a pharma/clinical internship.** Preferred on the JD; not in the pool. Honest Python/SQL/TypeScript + shipped APIs/ETL beats a knockout lie (`persona.md` anti-pattern).
- **Do not write a cover letter that sounds like an ML-research intern.** Lead with MDC (ETL + Flask on EC2) and Vylet (pipeline + SQL). SignalWeaver embeddings and Vylet LangGraph are generative-AI-on-custom-software pluses sitting on shipped software — not the opener.
- **Track:** Data Engineering first. Software/Application only as Python + TypeScript full-stack. Placement follows business need (`company.md`).
- **Location is not a skip.** Say yes to Lake County. Relocation is listed for eligible students; still plan housing.
- **No AbbVie contact in `network.md`.** A UMich alum in BTS still beats a cold SmartRecruiters pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Funnel:** rolling resume screen is the intern bottleneck; no standard coding OA published; recruiter phone then 1–2 STAR behavioral; some BTS teams add a light coding or case (`company.md`). Apply in the first wave.
- **Transcript:** Extern says intern applications typically include one. Have an unofficial PDF ready.
- **This agent did not submit.**
