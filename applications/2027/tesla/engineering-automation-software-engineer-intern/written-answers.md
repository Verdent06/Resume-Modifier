# Tesla — Software Engineer Intern, Engineering Automation / Vehicle Engineering (Winter/Spring 2027, req 279763) · Written Application Answers

Draft answers for Tesla careers req `279763`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented Next.js, Go, Kubernetes, Jenkins, Redux, Drizzle, gRPC, Catia/3DX, or Autopilot/Dojo work. Trim to each form’s length limit before submitting.

This posting is **Design Technology inside Vehicle Engineering**: internal web apps that automate or streamline the design process for vehicle, battery, and manufacturing engineers — not Autopilot, not Tesla Energy UI, not an ML internship.

Apply: https://www.tesla.com/careers/search/job/279763
Simplify (same req): https://simplify.jobs/p/155f6df6-7cca-471e-8fb1-e8318faa6845/Software-Engineer-Intern
Resume: `applications/2027/tesla/engineering-automation-software-engineer-intern/Vedant Desai Resume.pdf`

**Do not submit from this file.** Artifacts only. Tesla.com Apply was not clicked.

---

## Cover letter

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

Tesla — University Recruiting / Design Technology, Vehicle Engineering
Palo Alto, CA

Re: Software Engineer Intern, Engineering Automation, Vehicle Engineering (req 279763)

Dear Tesla hiring team,

I am applying for the Winter/Spring 2027 Software Engineer Intern role on Vehicle Engineering’s Design Technology team. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a US citizen, authorized to work in the United States without visa sponsorship. I can work the full-time (40 hours/week) on-site term in Palo Alto or Fremont starting January 2027 (minimum 12 weeks, through ~May 2027). I remain enrolled after the internship.

This req is internal tools other engineers actually run — web apps, APIs, Postgres, maintain-and-improve — not Autopilot and not a research rotation. That is the work I already ship.

What I would bring:

- **Web tools for non-SWE users.** At Michigan Data Consulting I was the sole engineer on a five-month Michigan Campaign Finance Network contract. I replaced ~2-hour manual committee pulls with a Requests + Pandas ETL (eliminating ~800 hours of work across 400 tracked PACs) and shipped a production Flask REST API on AWS EC2 into their public research workflow.
- **Full-stack spine this team names.** SignalWeaver is a React/TypeScript dashboard on async FastAPI REST with scores persisted to PostgreSQL (9.1s p50 / 15.2s p99 across 90 tickers). github.com/Verdent06/SignalWeaver. I have not shipped Next.js; I would ramp on the team’s Next.js frontend rather than claim it.
- **Live-system debug.** At CaseStudyPrep.AI I closed a 27% audio-upload failure rate around expired S3 presigned URLs (RxJS retry + MIME negotiation in Angular) and moved processing off the UI thread (main-thread blocking under 5ms, 60 FPS). At Vylet I wrote an asyncpg SQL data layer with injection-safe freshness checks and fixed a name-collision defect that lifted lead-qualification from 79% to 89% (live product, vyletdata.com).

I have not shipped Next.js, Go, Kubernetes, Jenkins, Redux, Drizzle, or gRPC. My production languages are Python and TypeScript, plus C++ and SQL. Docker and AWS (EC2, S3) are in inventory; Kubernetes/Jenkins are not. SolidWorks is familiar CAD, not a Tesla design-tooling internship. If the stack sits on Next.js or Go I will ramp rather than invent it.

I return to Michigan after the term (Expected May 2028). I would welcome the chance to walk through the MCFN API delivery or the SignalWeaver React + FastAPI + Postgres path.

Sincerely,
Vedant Desai

---

## Exact form questions visible without Apply

Tesla.com careers (`https://www.tesla.com/careers/search/job/279763`) returned **Access Denied / Akamai** from this environment. Simplify’s Apply button redirects to the same blocked Tesla.com page. **No Tesla ATS fields were captured.** Do not invent unseen questions. Cover-letter required vs optional is **unknown**.

Knockouts stated on the JD (Simplify full posting, same req 279763) **before** Apply:

| Visible JD gate | Answer |
| --- | --- |
| Currently enrolled in an academic program (recent grads → full-time, not internships) | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Start January 2027 through Spring (~May 2027) or continuing into Summer 2027 if available | **Yes** — Winter/Spring 2027; available January 2027 |
| Minimum 12 weeks, full-time, on-site | **Yes** |
| 40 hours/week on-site (Palo Alto / Fremont / other SF Bay Area) | **Yes** — Palo Alto first; Fremont acceptable |
| International / CPT: confirm 40 hr/week with school before applying | **Not applicable** — US citizen; no CPT. If the form still asks: authorized to work 40 hrs/week on-site |

---

## Knockout / structured fields (fill if Tesla ATS asks; not captured live)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub / website | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/tesla/engineering-automation-software-engineer-intern/Vedant Desai Resume.pdf` |
| Cover letter | Paste the letter above if an upload or Additional Information box exists |
| Location | **Palo Alto, CA** (also Fremont / SF Bay if a second site is required) |
| Willing to relocate / work on-site 40 hrs/week | **Yes** — January 2027, minimum 12 weeks |
| Currently enrolled undergrad CS or related | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Expected graduation | **May 2028** |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| GPA | **3.66 / 4.0** |
| Work authorization | **US citizen**; authorized to work in the US without visa sponsorship |
| Will you now or in the future require visa sponsorship? | **No** |
| CPT / 40 hours during the academic year | **N/A (citizen).** If asked whether you can work 40 hrs/week on-site in Winter/Spring 2027: **Yes** |
| How did you hear about this role? | **Simplify** (https://simplify.jobs/p/155f6df6-7cca-471e-8fb1-e8318faa6845/Software-Engineer-Intern). If Simplify is not listed: **LinkedIn Jobs** / Other → Simplify. **Do not invent a Tesla employee referral** (`network.md` has none). |
| Previous Tesla intern / employee | **No** |
| Languages you can interview in | **Python, TypeScript, C++, SQL.** Do **not** check Go, Java, C#, Next.js, Kubernetes, Jenkins, Redux, Drizzle, or gRPC. |
| Mailing address (if asked) | 49032 Freestone Dr, Northville, MI (used on other 2027 apps). School city on the resume is Ann Arbor, MI. |
| Voluntary EEO | Decline / skip unless required. Do not invent. |

Tesla’s public portal is an internal ATS (not Workday/Greenhouse). Fill required fields only (`recruiting.md`: keep volume high). Skip optional self-ID unless required.

---

## “Why Tesla / why Design Technology?”

I want a Winter/Spring term writing software that vehicle, battery, and manufacturing engineers actually use — internal web apps, APIs, Postgres, then debug when it breaks. That is this Design Technology intern seat, not Autopilot and not a generic CRUD rotation.

What I can defend:

- **Tools for non-SWE users.** Sole engineer on a five-month MCFN contract: Requests + Pandas ETL and a production Flask REST API on AWS EC2. Closest analog to “deliver web applications useful to design engineers and program managers.”
- **Full-stack the JD names.** SignalWeaver: React/TypeScript UI, FastAPI REST, PostgreSQL persistence. I have not shipped Next.js; I will ramp on it.
- **Debug.** CaseStudyPrep 27% S3-upload recovery; Vylet 79%→89% qualification fix on a live product.

I can be on-site in Palo Alto (or Fremont) January 2027, 40 hours/week, 12+ weeks. I return to Michigan afterward (Expected May 2028). I am a US citizen and do not need sponsorship.

---

## “Tell us about a project you built”

**MDC (internal tools / production API).** Production Flask REST on AWS EC2 plus a Requests + Pandas ETL that removed ~800 hours of PAC research. Closest analog to shipping and maintaining apps for a non-SWE stakeholder.

**SignalWeaver (full-stack).** github.com/Verdent06/SignalWeaver. React/TypeScript dashboard, FastAPI REST at 9.1s p50 / 15.2s p99, scores persisted to Postgres. Honest React + Python + PostgreSQL — not Next.js.

**CaseStudyPrep (live debug).** 27% upload-failure recovery (expired S3 URLs + Angular MIME) and Web Worker offload (sub-5ms main thread, 60 FPS).

Do not lead with Granular or Vylet’s LangGraph story. Granular is C++ constraint engineering with no latency number on the page. Vylet is SQL + a production defect fix if they ask about databases or ownership — not “I want to do agents at Tesla.”

---

## Availability

Winter/Spring 2027: **January 2027 through ~May 2027**, full-time **40 hours/week, on-site Palo Alto** (Fremont acceptable), minimum 12 weeks. Willing to continue into Summer 2027 if the team offers it. Returning to the University of Michigan after the internship (Expected May 2028).

---

## Notes for the applicant (not for submission)

- **Lead with MDC (tools for researchers) and SignalWeaver (React/TS + FastAPI + Postgres).** CaseStudyPrep is the debug story. Vylet is SQL + 79%→89% if they ask about production ownership. Do not lead with LoRA, LangGraph, or Granular (`persona.md` anti-patterns).
- **Do not claim Next.js, Go, Kubernetes, Jenkins, Redux, Drizzle, gRPC, Catia, or Autopilot.** Honest Python + TypeScript + PostgreSQL + Flask/FastAPI/React beats a knockout lie. Docker is Skills-only on this PDF — do not overclaim Compose/K8s in the form.
- **Granular has no latency/xrun/CPU number.** If asked, describe the audio-thread constraints and what you would measure — do not invent a metric (`grade.md` Defend).
- **Location and hours are not a skip.** Yes to Palo Alto/Fremont, 40 hrs/week, on-site, January 2027.
- **CPT language on the JD is a knockout for internationals.** You are answering as a US citizen; still confirm you can do a full-time winter term on-site.
- **Referral:** none in `network.md`. A UMich alum on Vehicle Engineering / Design Technology still beats a cold Tesla.com pile (`recruiting.md`: HM > recruiter > engineer > cold apply). Do not name a fake referrer.
- **After the PDF:** HackerRank Medium is the volume gate; tech rounds are the bottleneck (`companies.md` Tesla row, ~5–8%). Drill arrays/hash maps/trees/graphs. Behavioral/ownership is a filter.
- **Do not apply from this file automatically.** Tesla.com was not submitted.
