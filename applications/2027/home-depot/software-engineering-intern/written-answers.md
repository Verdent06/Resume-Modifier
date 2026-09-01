# The Home Depot — 2027 Summer Internship, Software Engineering (Atlanta / remote, Req191937) · Written Application Answers

Draft packet for Workday CareerDepot req **Req191937**. Grounded in `persona.md` (full-stack intern SWE lens: web FE through use, production product-team ship, Git, pairing — not BI/warehouse, not ML research). First-person, honest, defensible under "walk me through this."

**Do not invent:** Snowflake, Databricks, Copilot, Fusion, Tableau, BigQuery, GCP, Java, jQuery, Sentry, Kubernetes, or Go. Vedant has no Sentry experience.

Apply (do not submit from this agent): https://homedepot.wd5.myworkdayjobs.com/CareerDepot/job/STORE-SUPPORT-CENTER-ATLANTA---9090/XMLNAME-2027-Summer-Internship---Software-Engineering_Req191937

Careers mirror: https://careers.homedepot.com/job/23777891/2027-summer-internship-software-engineering-remote/

Resume: `applications/2027/home-depot/software-engineering-intern/Vedant Desai Resume.pdf`

**Pulled from the posting:** The Home Depot · 2027 Summer Internship - Software Engineering · Req191937 · STORE SUPPORT CENTER, ATLANTA - 9090 · Remote/Virtual · 11 weeks May 17–July 30, 2027 · up to 3 weeks in Atlanta (travel covered for eligible interns) · $24.00–$27.00/hr · full time.

---

## Exact form questions found (public Workday page + Apply click, no account)

Clicked **Apply**. There is **no Apply as Guest**. Custom screening questions live in wizard step **Application Questions** and were not readable without creating an account or signing in. **Do not invent those questions.**

### Create Account (visible, required)

1. Email Address
2. Password
3. Verify New Password

### Sign In (visible, required)

4. Email Address
5. Password

### Application wizard step names (progress bar only — not question text)

6. Create Account/Sign In
7. Autofill with Resume (only when using the autofill option)
8. My Information
9. My Experience
10. Application Questions
11. Voluntary Disclosures
12. Review

Workday also exposes `questionnaireId` `d495f841c38310106cc36c11b8d90000` on the public job JSON; the questionnaire body is not public.

---

## Cover letter (paste only if Workday has a Cover Letter / additional-information box)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

The Home Depot — 2027 Summer Internship, Software Engineering (Req191937)
Remote / Atlanta Store Support Center

Dear Home Depot recruiting team,

I am applying for the Summer 2027 Software Engineering internship (Req191937). I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work the full 11 weeks from May 17 to July 30, 2027, including up to three weeks at the Atlanta Store Support Center. I return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

This seat is product-team software: join an existing team, pair with UX, engineering, and PM, and ship production code under a senior engineer. That is the work I already do — web front end plus a service I can deploy — not a store rotation and not a BI internship.

What I would bring:

- **Web front end on a real product.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with fault-tolerant RxJS that regenerates expired S3 presigned URLs mid-flight for files Angular silently rejected, and moved audio off the UI thread into a Web Worker (main-thread blocking under 5ms at 60 FPS). On SignalWeaver I built a React/TypeScript dashboard over FastAPI REST, instrumented at 9.1s p50 / 15.2s p99. I interview in TypeScript, Angular, and React. I have not used jQuery.
- **Production delivery, owned.** As the only engineer on a five-month Michigan Campaign Finance Network contract I shipped a Flask REST API on AWS EC2 and replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees. I scoped ingestion through REST endpoints directly with MCFN — no backend team behind me.
- **Automation with a deploy.** I founded Vylet (vyletdata.com), a live product at $1,500 MRR. I turned a ~30-minute manual process into a Dockerized pipeline with Redis/Celery workers (30 scored leads in 30 minutes) and fixed a name-collision defect that lifted lead-qualification from 79% to 89%. Git is how I ship (GitHub + GitHub Actions on SignalWeaver).

I want this intern seat writing production code on a product team that associates and customers actually use. I do not claim Java, Sentry, Snowflake, Databricks, Tableau, GCP, Copilot, Fusion, or Kubernetes.

Sincerely,
Vedant Desai

---

## Notes for the applicant (not for submission)

- **Do not fill or invent Application Questions.** They were behind the Workday login wall. Answer the live wording. If a later step asks why Home Depot / why this intern role, paste a trimmed version of the cover letter (Angular + MDC production API + remote/Atlanta availability).
- **Do not claim jQuery, Java, Sentry, Snowflake, Databricks, Tableau, BigQuery, GCP, Copilot, Fusion, Kubernetes, or Go.** HTML/CSS is on the Skills line; the on-page FE story is Angular and React/TypeScript. If asked about markup, point at those UIs — do not invent a CSS bullet.
- **Lyndbrook is deal-sourcing, not product SWE.** If they walk the resume, pivot to CaseStudyPrep Angular and MDC Flask/EC2. Do not inflate Lyndbrook into a web internship.
- **Availability:** Yes to May 17–July 30, 2027, remote-first, Atlanta up to 3 weeks. Returning to UMich (Expected May 2028). GPA 3.66.
- **Work authorization:** Other 2027 packets in this repo state U.S. citizen, no sponsorship. Answer Workday work-rights questions truthfully if they appear. This req does not print a visa knockout.
- **How did you hear about this role?** The board you actually used. `network.md` has no Home Depot contact — do not claim a referral.
- **Optional self-ID / Voluntary Disclosures:** Skip unless required (`recruiting.md` Part I §2).
- **Funnel:** Workday resume screen is the binding gate (`companies.md` ~15–25%). Extern **[directional]** reports a 60–90 min CoderPad Easy–Medium (arrays/strings/hash maps/basic SQL) on the SWE intern track — not printed on this req. Prep LC Easy–Medium + STAR on pairing, ambiguity, and customer-facing delivery (intern values in `persona.md`).
- **No Home Depot contact in `network.md`.** A UMich alum on SSC tech still beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply).
