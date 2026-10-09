# Mastercard — Data Engineering Intern, Summer 2027 – San Franscisco, CA, US (R-285993) · Written Application Answers

Draft answers for Mastercard Workday **Campus** req **R-285993**. Grounded in the **live posting + CXS JSON + `/apply` SPA opened 2026-10-09**, `persona.md` (Commerce Media / Offers data engineering — Python pipelines on AWS, **not** SWE R-287618, **not** PySpark/Databricks), and `context.md` identity/metrics. First-person, honest, defensible under "walk me through this."

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.** PDF header is already gmail. Override any autofill.

**Do not invent:** PySpark, Databricks, Azure, Snowflake, Spark, Kafka, Hadoop, Java, Copilot, Fusion, Tableau. **MatchStream must never appear.**

**GPA:** **3.7 / 4.0** (3.66 rounded to one decimal). Do not write 3.66.

**Class standing:** Junior. Expected graduation **May 2028** (never 2029).

Phone **(248) 704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen; permanent work authorization; **no CPT, OPT, or visa sponsorship now or later**.

**Employment on the form: CaseStudyPrep.AI + Vylet only.** MDC and SpaceXAI Campus Lead Ambassador are **extracurricular**. Lyndbrook: on the PDF as a consulting engagement; do not add it as a third W-2 job. Awards / honors: **None**.

**Do not submit from this agent.** Packets stay in the repo. App Man downloads via `gh`. Never email `verdent06@gmail.com` with this packet.

Apply (human only): https://mastercard.wd1.myworkdayjobs.com/Campus/job/San-Francisco-California/Data-Engineering-Intern--Summer-2027---San-Franscisco--CA--US_R-285993/apply

Listing: https://mastercard.wd1.myworkdayjobs.com/Campus/job/San-Francisco-California/Data-Engineering-Intern--Summer-2027---San-Franscisco--CA--US_R-285993

Resume: `applications/2027/mastercard/data-engineering-intern/Vedant Desai Resume.pdf`

Airtable: `recO4HbqtgFVbdZQO` (In Progress — kit landing; **do not submit until the human apply**). Source: GitHub/SimplifyJobs.

**THIS IS NOT** Software Engineer Intern, Summer 2027 – United States **R-287618** (already pipelined).

---

## Knockouts (read first)

Quoted from the live JD ("What we're looking for"):

1. "Currently enrolled in a Bachelors or accelerated Masters degree with an anticipated graduation date between December 2027 and June 2028" — **clears** (B.S. Computer Science and Economics, University of Michigan, **Expected May 2028**, Junior).
2. "Previous internship in software development, data engineering, or a related technical field." — **clears** (CaseStudyPrep.AI Software Engineer Co-op, Dec 2025–May 2026). MDC is extracurricular on the form; still a titled Data Engineer engagement on the PDF.
3. "Experience with Python through coursework, projects, internships, or personal initiatives." — **clears** (on the PDF through use).
4. "This role is not eligible for Mastercard's work authorization sponsorship. As such, candidates must be eligible to work in the United States, now as well as in the future, without employer sponsorship. For example, students or recent graduates in the United States on an F1 visa (including those with CPT or OPT authorization) are not eligible for this role." — **clears** (US citizen; no sponsorship).
5. San Francisco, CA, Summer 2027, full-time intern — **Yes**. Relocate from Northville, MI.
6. Unofficial transcript at submit — **will upload** the real UMich unofficial transcript (Vedant has the file; this agent does not).

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on sponsorship, graduation window, or PySpark.

---

## What was extracted from the live page (2026-10-09)

Pulled without creating an account, without uploading a resume, and without submitting.

### Job posting (public CXS JSON)

`GET https://mastercard.wd1.myworkdayjobs.com/wday/cxs/mastercard/Campus/job/San-Francisco-California/Data-Engineering-Intern--Summer-2027---San-Franscisco--CA--US_R-285993` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Data Engineering Intern, Summer 2027 – San Franscisco, CA, US** (Workday spelling) |
| Company | **Mastercard** (`hiringOrganization`: US: Mastercard International Incor) |
| Requisition | **R-285993** · jobPostingId `Data-Engineering-Intern--Summer-2027---San-Franscisco--CA--US_R-285993` · jobPostingInfo.id `f1d5d10fb61310015c75e5366a740000` |
| Location | **San Francisco, California** · United States of America |
| Time type | **Full time** |
| Posted | **Posted 2 Days Ago** · `startDate` **2026-10-07** |
| Pay | **$35–$46/hr** |
| Apply | `canApply: true`. `includeResumeParsing: true`. Site: **Campus** |
| `questionnaireId` | `802e7dac252910014cc8afe0d18d0000` |
| `secondaryQuestionnaireId` | `8131e020187d1000ba7c298c7afe0000` |

JD body (live): Commerce Media and Offers data-science-capabilities team; Python; data pipelines / workloads on AWS, Azure, or Databricks; PySpark plus; AI/ML workflows plus; unofficial transcript required.

### Start Your Application (live `/apply` SPA, Chrome dump 2026-10-09)

Visible widgets on **Start Your Application** (account not created):

| Exact label (live) | Action |
| --- | --- |
| Autofill with Resume | Upload the packet PDF, then review parsed fields |
| Apply Manually | Use if autofill is messy |
| Use My Last Application | Only if a prior Mastercard Campus app exists; still overwrite email to **verdent06@gmail.com** and do not reuse the SWE R-287618 resume |
| Sign In | If you already have a Mastercard Workday Campus account |

**No guest apply.** CXS `GET .../apply` and questionnaire URLs returned **HTTP 406** without an account. **No essay prompts, knockout radios, or My Information fields were visible on the public apply page.** Do not invent extra essays. If later pages differ, answer the actual question.

### Sign In (live `/Campus/login`, Chrome dump 2026-10-09)

| Exact label (live) | Answer |
| --- | --- |
| Email Address * | **verdent06@gmail.com** (never vedantde@umich.edu) |
| Password * | **Your real password.** Not stored in this repo |
| Sign In | After you have an account |
| Don't have an account yet? Create Account | Create if needed |
| Forgot your password? | Only if you already created one |
| Enter website. This input is for robots only, do not enter if you're human. | **Leave blank** |

Direct `/createaccount` URL returned a Workday error banner without extra fields. Create Account is behind that button. If the live create-account page matches the sibling Mastercard Campus wizard, it asks Email, Password, Verify Password, and Mastercard Global Applicant Privacy Notice consent — fill those; **do not invent extra essays**. Password is Vedant's own (not in this repo).

---

## Knockout / structured fields (fill exactly)

Later wizard pages are behind an account. Use these facts. If the logged-in wording differs, answer the actual question.

Mastercard Campus intern wizard captured on sibling req R-287618 (same `wd1` tenant; **this req's questionnaire IDs are listed above — confirm labels if they differ**): Autofill → My Information → My Experience → Application Questions 1 of 2 → Application Questions 2 of 2 → Voluntary Disclosures → Self Identify → Review. **No cover-letter box** on pages that loaded for that sibling. Unofficial transcript required on Q1.

### Identity / My Information

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email Address | **verdent06@gmail.com** |
| Phone Device Type | **Mobile** |
| Country Phone Code | **United States of America (+1)** |
| Phone Number | 2487044852 (or 248-704-4852 if the mask allows dashes) |
| Country | United States of America |
| Address Line 1 | 49032 Freestone Dr |
| City | Northville |
| State | Michigan |
| Postal Code | 48168 |
| Have you ever worked for Mastercard as an employee or provided services as a contingent worker (contractor, consultant)? | **No** |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Website | https://vyletdata.com |
| Resume/CV | `applications/2027/mastercard/data-engineering-intern/Vedant Desai Resume.pdf` |

### My Experience

| Field | Answer |
| --- | --- |
| Work Experience | **1. Vylet — Founder — May 2026–Present.** **2. CaseStudyPrep.AI — Software Engineer Co-op (Voice AI) — Dec 2025–May 2026.** Stop. Do not invent a Mastercard internship. |
| Education | **University of Michigan** · B.S. Computer Science and Economics · Expected **May 2028** · GPA **3.7 / 4.0** · currently enrolled. Start date if asked: **08/31/2025**. High school only if a second education row is required: Northville High School, Northville MI, graduated **05/19/2025**. |
| Skills | Only inventory on the PDF: **Python, SQL, Pandas, LangGraph, PostgreSQL, Redis, pgvector, AWS (EC2, S3), Docker, Celery, Git, FastAPI.** **Do not** add PySpark, Databricks, Azure, Snowflake, Spark, Kafka, Java, Copilot, Fusion, Tableau. |
| Extracurricular | **Michigan Data Consulting (MDC)** — Data Engineer for Michigan Campaign Finance Network, Jan 2026–May 2026. SpaceXAI Campus Lead Ambassador if a second row is required. |
| Awards / honors | **None** |

### Application Questions (expected Campus knockouts — confirm live)

These labels were live on Mastercard Campus intern R-287618. This req attaches questionnaires `802e7dac…` and `8131e020…`. Fill if shown; skip if absent.

| Exact label (sibling live) | Answer |
| --- | --- |
| Please select date that you will complete your current degree. … If you do not know the specific day, select the 1st of the month you graduated. * | **05/01/2028** |
| Please upload your college/university transcript. * | **Unofficial UMich transcript** — Vedant's file. Not in this repo. JD: "Please be sure to upload an unofficial copy of your school transcript when submitting your application." |
| Are you NOW legally authorized to work in the country where the position you are applying for is located? * | **Yes** — US citizen |
| Do you now, or will you in the future, require sponsorship for an employment visa in the country where the position you are applying for is located? * | **No** |
| Have you entered into any restrictive covenant, non-compete agreement, or non-disclosure agreement which could restrict you from performing any duties of any of the position(s) for which you intend to apply? * | **No** |
| Have you ever worked for Mastercard? * | **No** |

### Application Questions 2 of 2 (conflict-of-interest — sibling live)

Default **No** unless a fact below applies. `network.md` has **no Mastercard contact**.

| Topic | Answer |
| --- | --- |
| Engage with Mastercard employees to negotiate/sign commercial or government contracts? | **No** |
| Related to anyone with authority to influence/sign such contracts with Mastercard? | **No** |
| Employee of a government office/agency with oversight over Mastercard (last six months)? | **No** |
| Related to anyone in such an office/agency? | **No** |
| Close personal relationship with a current Mastercard employee? | **No** (`network.md`). If that changes before submit, switch to **Yes** and name them. |
| Currently engaged in any outside employment or activity you would like to continue if hired? | **Yes** — founder of Vylet (live product, $1,500 MRR). Disclose it. If you would **fully pause** Vylet for the intern term and not continue it while employed, you may answer **No**; do not hide a company you intend to keep running. **Vedant must choose pause vs continue.** |

### Voluntary / Self Identify

Voluntary. Kit defaults if you choose to answer: Hispanic or Latino **No**; Ethnicity **Asian (Not Hispanic or Latino)**; Gender **Male**; Veteran **I AM NOT A VETERAN**; Disability **No, I do not have a disability and have not had one in the past**. **I do not want to answer** is allowed on every voluntary field.

---

## Cover letter / "Why Mastercard / why this Data Engineering role?" (paste only if a later step has a box)

The live apply chrome had **no cover-letter box**. Skip unless a later page asks.

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

I am applying to Data Engineering Intern, Summer 2027 – San Francisco (R-285993) on the Commerce Media and Offers data team — pipelines and cloud workloads, not the generic SWE intern (R-287618) and not an ML-research seat. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.7, Junior). I am a U.S. citizen and will not need visa sponsorship. I can be in San Francisco for Summer 2027.

What I can defend:

- **Messy source data → ETL → served insight.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month contract.
- **SQL freshness + containers.** On Vylet I run a Dockerized LangGraph pipeline (30 scored leads in 30 minutes — a 30x speedup) with Redis/Celery workers. The production DAL uses injection-safe SQL timestamp checks that trigger re-scrapes when records go stale. I have not used PySpark, Databricks, or Spark; I would ramp rather than claim them.
- **Multi-source merge → entity key → score.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a unified PWSID entity database (800+ Day-1 targets) and built a Review Velocity score that cut the list to 280 leads at 35% precision.
- **Prior technical internship.** CaseStudyPrep.AI Software Engineer Co-op (Dec 2025–May 2026): recovered a 27% S3 upload-failure rate with presigned-URL regeneration.

Sincerely,
Vedant Desai

---

## Short paste blurb (if a small text box appears)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.7, Junior) applying to the San Francisco Data Engineering intern seat (R-285993) — Commerce Media / Offers pipelines, not generic SWE R-287618. I ship Python/SQL data work: a Pandas ETL that cut ~800 hours of pulls across 400 PACs, a Dockerized pipeline with injection-safe SQL freshness checks, and a multi-source entity score that shortlisted 800 targets to 280 at 35% precision. I have not used PySpark, Databricks, Spark, or Java. I am a U.S. citizen and do not need sponsorship. I can be in San Francisco Summer 2027.

---

## Availability

Summer 2027, full-time, **San Francisco, CA**. Returning to the University of Michigan after the internship (Expected May 2028). Junior at application; Summer 2027 = after sophomore year / rising junior on a May 2028 graduation. Relocate **Yes**.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field.** PDF header is already gmail. Do not type `vedantde@umich.edu`.
- **Unofficial transcript is required.** Q1 will not continue without it. Use the real UMich unofficial transcript. **This agent does not have that file.**
- **Do not invent PySpark, Databricks, Azure, Snowflake, Spark, Kafka, Java, Copilot, Fusion, or Tableau.** Walk Python/SQL/Pandas/AWS/Docker and say you will ramp.
- **Do not apply as SWE R-287618.** This is the Commerce Media / Offers Data Engineering intern.
- **Prior Experience = Vylet + CaseStudyPrep.AI only.** MDC is extracurricular. Awards: None.
- **Vylet disclosure.** Outside-activity question: default **Yes** if you would keep it; **No** only if you would pause it for the term. **Vedant chooses.**
- **No Mastercard contact in `network.md`.** Do not pick Employee Referral. How did you hear: the board you actually used (Airtable source: GitHub/SimplifyJobs).
- **Resume is the intern bottleneck** (`companies.md` B-tier ~8–12%). PDF first; Easy–Med HackerRank follows invitation.
- **Do not apply from this agent.**

## Form questions that need Vedant's own input (do not invent)

1. **Workday password** (and Create Account / Verify Password if you don't have an account yet).
2. **Unofficial UMich transcript file** (required upload).
3. **Vylet outside-activity:** continue during the intern term (**Yes**) vs fully pause (**No**).
4. **How did you hear about this role?** if a picker appears — pick the board you actually used (SimplifyJobs / company site). Do not invent a referral.
5. Any **free-text essay** that is not listed above. Stop and draft from `grade.md` Interview angles rather than inventing a new story. The live public apply page had **no essay box**.
