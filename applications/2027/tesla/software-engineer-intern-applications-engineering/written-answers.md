# Tesla — Software Engineer Intern, Applications Engineering (Winter/Spring 2027, Fremont, req 280820) · Written Application Answers

Draft answers for Tesla careers req **280820**. Grounded in `persona.md` (full-stack spine + EV / vehicle-engineering internal tools & infrastructure), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Go, Java, Oracle, MS SQL, Snowflake, Databricks, Copilot, Fusion, Tableau, Autopilot/FSD models, vehicle firmware, ROS, or a C++ project on this PDF (Granular is in the pool but **not on this resume** — page overflow). Do not claim you wrote Autopilot or firmware.

Apply (do not submit from this agent): https://www.tesla.com/careers/search/job/280820
Simplify mirror used when tesla.com 403'd this environment: https://simplify.jobs/p/7e502eb4-3d9c-4f91-8e83-a471504d8a4b/Software-Engineer-Intern
Resume: `applications/2027/tesla/software-engineer-intern-applications-engineering/Vedant Desai Resume.pdf`

This posting is **Applications Engineering + Business Ops & Infrastructure** (internal apps and infra for Connected Systems, Firmware, and Autopilot *teams*). **Not** Autopilot-ML, vehicle firmware, AI Hardware/EDA, Energy Commercial UI, or Factory Software / IT Apps.

**Location / term are not a skip:** Fremont, CA, on-site, 40 hours/week, minimum 12 weeks, start around January or February 2027 through Spring term (ending ~May 2027 or later if available). Tesla requires you stay an enrolled student. Confirm you can be in Fremont full-time for that window (co-op / leave that still counts as enrolled). Winter-term CPT is often part-time — Tesla's JD says consult your school before applying if you need CPT for 40 hours/week.

---

## Exact form questions visible on the posting (no Apply click)

**None.** tesla.com/careers/search/job/280820 was Access Denied from this environment. Simplify's copy of req 280820 had `questions: []`. Former Tesla intern reports (Borderless) describe the intern portal as **resume upload, no cover letter required**. This packet does **not** click Apply and does **not** submit. Use the identity / knockout table if the post-Apply wizard asks them. Do not invent extra Tesla fields.

---

## Identity / standard Tesla screening (fill if the wizard asks)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub / website | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/tesla/software-engineer-intern-applications-engineering/Vedant Desai Resume.pdf` |
| School | University of Michigan |
| Degree | B.S. Computer Science and Economics (pick **Computer Science** if only one discipline) |
| Graduation date | **May 2028** (inside JD window 2027–2028) |
| GPA | **3.66 / 4.0** |
| Currently enrolled / returning to school after the internship? | **Yes** — Winter/Spring 2027 intern; Fall 2027 and Winter 2028 remain (Expected May 2028) |
| Location | **Fremont, CA** — this req only. On-site, 40 hours/week, ≥12 weeks |
| Available January or February 2027 through Spring 2027? | **Yes** if you can actually relocate to Fremont for the term. If you cannot, do not apply this packet. |
| Are you authorized to work in the United States? | Answer **truthfully**. Other 2027 applications in this repo treat you as a **US citizen**. `context.md` has no citizenship field. Tesla intern postings accept CPT if you can work **40 hours/week on-site**; many schools cap academic-year CPT at part-time — check before applying. |
| Will you require visa sponsorship now or in the future? | **No** if you are a US citizen / do not need a visa. Do not guess. |
| How did you hear about this role? | **Tesla careers** (https://www.tesla.com/careers/search/job/280820). If an aggregator is listed and that is actually how you found it, pick that. `network.md` has **no Tesla contact** — do not invent a referral. |
| Cover letter | Optional; Tesla intern apps are typically resume-only. Paste the letter below only if a box exists. |
| Languages you can interview in | **Python, TypeScript/JavaScript (React, Angular), SQL, C++**. Do **not** check Go, Java, Oracle, or MS SQL. C++ is Skills-only on this PDF — you can interview in it; do not point at a C++ bullet that is not on the page. |

Mailing address used on other 2027 apps (if asked): 49032 Freestone Dr, Northville, MI. School city on the resume is Ann Arbor, MI.

---

## Cover letter / "Why Tesla / why Applications Engineering?" (optional)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

I am applying to the Winter/Spring 2027 Software Engineer Intern role on Applications Engineering in Fremont (req 280820) — internal infrastructure and applications for Tesla Engineering (Connected Systems, Firmware, Autopilot support software), not Autopilot model training and not vehicle firmware.

I want to ship and operate tools other engineering teams depend on. That is already the shape of my work: production services, containers, and reliability fixes, in Python and TypeScript.

What I can defend:

- **Internal tools and operated services.** As the sole engineer on a five-month Michigan Campaign Finance Network contract, I replaced portal searches and irregular Excel exports with a Requests + Pandas ETL (~800 hours of manual pulls across 400 PACs) and delivered a production Flask REST API on AWS EC2.
- **Infrastructure you can restart.** I founded Vylet (vyletdata.com): a Dockerized pipeline with Redis/Celery workers that turns a ~30-minute manual research pass into 30 scored leads in 30 minutes. I diagnosed a name-collision defect that was rejecting valid targets; qualification went from 79% to 89% with no change in sourcing volume.
- **Full-stack plus client reliability.** SignalWeaver is FastAPI + React/TypeScript + Postgres, containerized with Docker Compose and GitHub Actions CI (9.1s p50 / 15.2s p99 across 90 tickers). At CaseStudyPrep.AI I cut a 27% audio-upload failure rate by regenerating expired S3 presigned URLs mid-flight in RxJS/Angular, and moved audio off the UI thread (main-thread blocking under 5ms, 60 FPS).

I have not used Go, Java, Oracle, or MS SQL. If a rotation is heavier in one of those, I will ramp; I will not pretend I already have it. I interview in Python and TypeScript. I can be on-site in Fremont 40 hours/week for the Winter/Spring 2027 term (start January or February 2027, ≥12 weeks) and I return to Michigan afterward (Expected May 2028, GPA 3.66).

---

## If they ask "Tell us about a project / a time you operated a service"

**MDC (lead).** Sole engineer, Flask REST on EC2, Pandas ETL, stakeholder-scoped contract. Maps to Applications Engineering "architect, build, manage, operate infrastructure and applications" without inventing Tesla vehicle work.

**Vylet (infra + defect).** Docker + Redis/Celery; name-collision fix 79%→89%. Do not turn LangGraph into an Autopilot-ML pitch (`persona.md` anti-pattern).

**SignalWeaver (full-stack).** FastAPI, React/TypeScript dashboard, Docker Compose, GitHub Actions. Research assistant, not a trading product.

**CaseStudyPrep (reliability).** Expired S3 URLs + Angular MIME rejection → 27% failure recovered. Web Worker offload for a live UI. The ONNX/VAD bullet is on the PDF — if they ask, it is client-side cost/latency, not an ML-research intern story.

**C++ if they ask why it is on Skills.** Honest: Granular Synthesizer (C++/JUCE, lock-free audio thread) is real work in the pool and **not on this one-page PDF**. Do not point at a resume bullet that is not there. Python is the production language on the page (`grade.md` Defend).

---

## Availability

Winter/Spring 2027, paid, **onsite Fremont**, 40 hours/week, minimum 12 weeks. Available to start January or February 2027 through ~May 2027. Returning to the University of Michigan afterward (Expected May 2028). Class standing at the internship: **junior**. GPA 3.66.

---

## Notes for the applicant (not for submission)

- **Do not apply from this agent.** Tesla Apply was not clicked; no form questions were visible. This packet is drafted answers + PDF.
- **Req 280820 only.** Do not upload this PDF to Autopilot-ML, firmware, AI Hardware, Energy UI, or Factory Software intern reqs.
- **Do not invent Go, Java, Oracle, MSSQL, Autopilot, or firmware.** JD "one or more" languages is already met by Python in bullets (`persona.md`).
- **C++ is Skills-only on this PDF** (`grade.md` minor). Interview in it if asked; do not claim a C++ intern project on the resume.
- **Fremont 40 hrs/week in Winter/Spring is the real knockout after the PDF.** Confirm housing + enrollment/CPT before you click Apply.
- **Cover letter is optional.** Tesla intern reports: resume only. The PDF is the screen. Binding filters after that: HackerRank Medium (Codility on some intern cycles) then tech rounds (`companies.md`: bottleneck tech rounds, ~5–8%).
- **Referral:** none in `network.md`. A real Tesla name beats a cold apply; a fake name is a knockout.
- **Comp:** not on 280820. Prior-cycle same-team Fullstack AE intern listed $36.06–$50.48/hr — directional only.
