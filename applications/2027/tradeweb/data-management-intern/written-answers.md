# EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY — never `vedantde@umich.edu`.**
Override any Oracle HCM parse / Autofill / last-application email. PDF header is already `verdent06@gmail.com`. If a field shows `vedantde@umich.edu`, delete it and type `verdent06@gmail.com` before submit.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

---

# Tradeweb — Summer 2027 Data Management Internship (Oracle CX 301946) · Written Application Answers

Draft answers for Oracle Cloud HCM Candidate Experience on `ecnf.fa.us2.oraclecloud.com`, site **CX**, job **301946**. Grounded in the **live posting opened 2026-10-06**, `recruitingCEJobRequisitionDetails` finder `ById;Id=301946,siteNumber=CX`, guest `/apply` SPA, `persona.md`, `grade.md` Interview angles, and `context.md` identity/metrics only. First-person, honest, defensible under "walk me through this."

**This is Summer 2027 Data Management Internship 301946 (NYC, 245 Park Ave, $22–$25/hr).** It is **not** Data Product Manager intern **301932**, **not** Data Platform intern **301904**, **not** Quantitative intern, and **not** a Java/C++/Node developer intern.

**Do not invent:** Excel-as-claimed-skill, Bloomberg, vendor security-master platforms, Snowflake, Databricks, Tableau, Copilot, Fusion, Fixed Income desk experience, a Tradeweb internship.

**Form kit email MUST be `verdent06@gmail.com`.** Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship. GPA **3.7** (unrounded 3.66 — do **not** type 3.66).

Airtable: `rec1Th1kdKwTz4rox` (In Progress — kit landing; **do not submit until the human apply**). Source logged: **GitHub/SimplifyJobs**.

Listing: https://ecnf.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/301946

Apply: https://ecnf.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/301946/apply

Resume: `applications/2027/tradeweb/data-management-intern/Vedant Desai Resume.pdf`

**SHA-256:** `109723c10dc26781545e5410bab0dc466a8ea1c14d0f4f287937cf545c1644ef`

Posted **2026-10-06T13:29:54Z**. `ExternalPostedEndDate` **null**. `ApplyWhenNotPostedFlag` true. RequisitionId **300000134983199**. Work location **US, NY, 245 Park Ave** (40.75469, -73.97564). Primary location **New York, NY, United States**. Pay **$22–$25 hourly** if performed in New York City. **This agent did not create an Oracle draft, did not create an account, and did not submit.**

---

## Knockouts (read first)

1. Currently pursuing a bachelor's in **Finance, Data Analytics, Computer Science, Information Systems, Economics, Mathematics, or a related field** — **clears.** B.S. Computer Science and Economics, University of Michigan. Both majors are named on the JD.
2. Summer 2027, New York, NY (245 Park Ave) — **Yes** if you actually take the seat. Relocate from Northville, MI for the term; return to Michigan afterward. Term dates **not printed** on this JD — do not import sibling SWE intern "9 weeks 28 Jun–27 Aug 2026" dates.
3. Work authorization — **clears** (US citizen; no sponsorship now or later). This JD prints **no** visa or clearance line.
4. Pay **$22–$25/hour** (NYC) — **Yes** if you accept the posted intern range.
5. Excel preferred; SQL and/or Python preferred — **Python, SQL: Yes** (on the PDF through use). **Excel as a claimed skill: No.** Pandas-on-irregular-Excel-exports is the honest analog. Do not check Bloomberg / Snowflake / Databricks / Tableau.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on sponsorship, GPA, class year, or invented Excel/Bloomberg.

Quoted eligibility (live `ExternalDescriptionStr`, 2026-10-06): *"Currently pursuing a bachelor's degree in Finance, Data Analytics, Computer Science, Information Systems, Economics, Mathematics, or a related field."*

---

## What was extracted from the live page (2026-10-06)

Pulled without creating an account, without creating an apply draft, without uploading a resume, and without submitting.

### Job posting (public REST + apply SPA chrome)

`GET https://ecnf.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails?finder=ById;Id=301946,siteNumber=CX` returned **HTTP 200**.

| Label / field on the posting | Value |
| --- | --- |
| Title | **Summer 2027 Data Management Internship** |
| Job Identification | **301946** |
| RequisitionId | **300000134983199** |
| Primary location | **New York, NY, United States** |
| Work location | **US, NY, 245 Park Ave** |
| Posted | **2026-10-06T13:29:54Z** |
| End date | **null** (`ApplyWhenNotPostedFlag` true) |
| Pay (JD body) | **$22–$25 hourly** if performed in the city of New York |
| Team | Data Management: securities **reference data**, onboarding, validation, **security master** |
| Apply | `/hcmUI/CandidateExperience/en/sites/CX/job/301946/apply` **HTTP 200** (SPA shell) |

Guest `recruitingCEApplyFlows` returned **empty** (`count: 0`) without a saved draft. `recruitingCEQuestionnaires` **HTTP 404** as a guest. **Do not POST a job application or draft from this agent.**

### Exact form questions visible without an account

The apply route is an Oracle CE SPA (`oj-hcm-ce` 2604.25). Visible without login / without a draft:

**Job page chrome (public):**

- Title **Summer 2027 Data Management Internship**
- Location **New York, NY, United States**
- Apply control that routes to `/job/301946/apply`

**Apply SPA first screen (Oracle CE guest chrome — same i18n keys as this tenant's CE bundle; labels match Arconic/BNY/Lazard guest apply on Oracle CE):**

| Exact label (CE i18n / guest chrome) | Answer |
| --- | --- |
| Email Address * | **verdent06@gmail.com** |
| Helper (typical CE copy) | "You don't need to have an account — Get started right away by simply using your email." Guest apply — do **not** create a second account with the UMich email |
| I agree with the terms and conditions * (`apply-flow.legal-disclaimer.i-agree-with-terms-and-conditions`) | Check **Yes** only after reading the live T&Cs (required to proceed; not an employment yes) |

Cookie banner: accept or reject as you prefer. Do not allow location tracking if a separate toggle exists.

**Later wizard pages (personal info, resume, education, experience, application questions, EEO, e-sign) were not returned as questionnaire items without a draft.** Do **not** invent extra essay prompts. If the signed-in form differs, answer the actual question with the same facts below.

CE bundle keys confirm later sections *exist as chrome* (not Tradeweb-specific essays): Drop Resume / Drop Cover Letter, First/Last name, phone, address, education, experience, optional cover letter, optional "more about you" / disqualification questions **if configured for this req**. Those Tradeweb-specific knockout radios were **not visible**. Use the kit table; if a later step shows different wording, keep the same facts.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI Software Engineer Co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular only.**
- **SignalWeaver = project, not a job.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA **3.7**, Junior.
- Languages you can defend on **this** PDF: **Python, SQL**. Do **not** check Excel-as-analytics, Bloomberg, Snowflake, Databricks, Tableau, Copilot, Fusion.

---

## Knockout / structured fields (fill exactly)

### Contact / identity (after email + T&Cs)

| Field | Answer |
| --- | --- |
| Last Name * | Desai |
| First Name * | Vedant |
| Title | **Mr.** if required; else blank |
| Middle Name | leave blank |
| Preferred First Name | blank unless required |
| Email Address | **verdent06@gmail.com** (pre-fill; overwrite school email if it appears) |
| Phone Number * | **248-704-4852** · country **United States (+1)** · **Mobile** |
| Country * | United States |
| Address Line 1 * | **49032 Freestone Dr** |
| Address Line 2 / 3 | blank |
| Postal Code * | **48168** |
| City * | **Northville** (not Ann Arbor, not New York — current home) |
| State * | **Michigan** |

### Documents and URLs

| Field | Answer |
| --- | --- |
| Drop Resume Here * / Upload Resume | `applications/2027/tradeweb/data-management-intern/Vedant Desai Resume.pdf` (match SHA-256 above) |
| Drop Cover Letter Here | Optional. Use the letter below if attaching. Skip if speed-applying — the PDF is the screen (`companies.md`: bottleneck is the resume) |
| Link 1 | https://linkedin.com/in/vedantde06 |
| + Add Another Link | https://github.com/Verdent06 · optional third: https://vyletdata.com |

### Education

| Field | Answer |
| --- | --- |
| School | **University of Michigan** / Ann Arbor — not Dearborn/Flint. If typeahead misses it: **Other** → University of Michigan |
| Degree | B.S. Computer Science and Economics (pick **Computer Science** if one major; add **Economics** as a second major row if required) |
| Highest level of education obtained | **High School Diploma / GED** (bachelor's in progress; do **not** pick Bachelor's Degree) |
| Did you graduate? | **No** |
| Start | **08/31/2025** |
| Graduation / expected | **May 2028** (picker day: **05/01/2028** if needed) |
| GPA | **3.7 / 4.0** — do **not** type 3.66 |
| Currently enrolled | **Yes** |
| Class standing | **Junior** (Expected May 2028; Summer 2027 = after sophomore year / rising junior) |

High school row only if a second education line is required: Northville High School, Northville MI, graduated **05/19/2025**.

### Work history on the form (not the PDF)

| Role | How to enter |
| --- | --- |
| Vylet · Founder | **Job.** May 2026 – Present. Automated lead-sourcing platform; $1,500 MRR, three clients. vyletdata.com |
| CaseStudyPrep.AI · Software Engineer Co-op (Voice AI) | **Job.** Dec 2025 – May 2026. Remote. Titled prior co-op. |
| Michigan Data Consulting (MDC) | **Extracurricular only.** Data Engineer project for Michigan Campaign Finance Network, Jan 2026 – May 2026. Do **not** list as an internship/job even though it is Experience on the PDF |
| Lyndbrook Capital | **Do not add as a job.** Consulting engagement; essays only if they ask |
| SignalWeaver | **Project**, not a job |

### Typical Oracle CE application questions (not visible as a guest — confirm live labels)

If a later step shows these (or the JD qualifications restated as radios), use:

| If the live label is | Answer |
| --- | --- |
| Currently pursuing a bachelor's in Finance / DA / CS / IS / Economics / Math or related? | **Yes** — B.S. Computer Science and Economics |
| Are you legally authorized to work in the United States? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship (H-1B, CPT, OPT, etc.)? | **No** |
| Citizenship | **US citizen** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |
| GPA | **3.7 / 4.0** |
| Expected graduation | **May 2028** |
| Class standing | **Junior** |
| Returning to school after the internship? | **Yes** — Fall 2027 and Winter 2028 remain |
| Willing / able to work in New York, NY (245 Park Ave) for Summer 2027? | **Yes** — relocate from Northville, MI for the term |
| Desired pay / salary | Posted intern range **$22–$25/hr**. If a dropdown is annualized summer pay, pick the band that covers ~$22–$25 × hours, not a $100k+ FTE band |
| Ever worked for Tradeweb? | **No** |
| Relatives at Tradeweb? | **No** |
| Employee referral? | **No.** `network.md` has **no Tradeweb contact**. Do **not** invent a name |
| How did you hear about this position? | **Vedant must pick the true source.** Airtable source is **GitHub/SimplifyJobs**. If you opened the Oracle CX URL directly: company website / Oracle CE. If LinkedIn: Job Board → LinkedIn. **Not** Employee Referral |
| Python | **Yes** — through use on the PDF |
| SQL | **Yes** — Vylet injection-safe SQL timestamp / re-scrape on the PDF. Ranking/ETL was Pandas. Do not claim warehouse JOIN SQL |
| Excel / pivot tables | **No** as a claimed skill. Pandas on irregular Excel exports is the analog |
| Bloomberg / Snowflake / Databricks / Tableau / Copilot | **No** |
| Fixed Income familiarity | **Coursework/econ interest only — not a desk.** Do not check "expert" / "professional experience" |
| I consent to SMS recruiting | **No, I do not consent** unless you actually want texts (answer is required if shown; consent is optional) |
| Background check (if asked) | **Yes** if you will take the seat |

Voluntary EEO / disability / veteran: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Skip for volume (`recruiting.md` Part I §2).

### E-signature

| Field | Answer |
| --- | --- |
| Full Name * | **Vedant Desai** |
| Submit | **Do not click.** Human submits after paste-check |

---

## Cover letter (optional upload)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Tradeweb Markets LLC — Data Management
245 Park Ave, New York, NY

Re: Summer 2027 Data Management Internship (Oracle CX 301946)

I am applying for the Summer 2027 Data Management Internship in New York — securities reference-data validation, reconciliation, and security-master maintenance, not Data Product Manager intern 301932, not Data Platform intern 301904, and not a Quantitative intern seat. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.7). I am a U.S. citizen and do not need visa sponsorship. I can relocate from Northville, MI to New York for the internship term and return to Michigan afterward.

I have not used Bloomberg, vendor security-master tools, Snowflake, Databricks, or Tableau, and I do not list Excel as a claimed skill. What I can defend is messy multi-source data → validation / discrepancy catch → a ranked or served artifact a non-builder used.

What I can defend:

- **Irregular filings → ETL → ranking → served API.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month contract.
- **Discrepancy investigation + SQL freshness.** I run Vylet (vyletdata.com; $1,500 MRR, three clients): injection-safe SQL timestamp checks that re-scrape stale records, and a name-collision defect I diagnosed that was incorrectly rejecting valid targets (qualification 79% → 89%). Ranking work on this resume is Python/Pandas; SQL is freshness, not a warehouse JOIN.
- **Multi-source entity unification.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a PWSID entity database (800+ Day-1 targets) and built a Review Velocity score that cut the list to 280 leads at 35% precision against the fund's revenue criteria.
- **A dashboard a non-builder can click.** SignalWeaver: React/TypeScript dashboard over scores persisted in Postgres for 90 tickers. Research assistant, not investment advice.

I want Summer 2027 on Data Management 301946 keeping a security-master analog true — Python, SQL, validation, and honest process automation — not a PM intern and not a data-platform SRE intern.

Sincerely,
Vedant Desai

---

## Short paste blurb (if a later step adds a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.7) applying to Tradeweb's NYC Data Management intern seat (301946) — securities reference-data validation/reconciliation, not PM intern 301932 and not Data Platform intern 301904. I ship applied data work: a Requests + Pandas ETL on irregular campaign-finance filings that cut ~800 hours of pulls across 400 PACs; a Flask report API on EC2; EPA/MassGIS entity scoring that shortlisted 800 targets to 280 at 35% precision; and SQL timestamp freshness plus a 79%→89% collision catch on a live lead pipeline. I have not used Bloomberg, Snowflake, Databricks, or Tableau. I am a U.S. citizen and do not need sponsorship. I can be in New York for Summer 2027.

---

## "Why Tradeweb / why Data Management?" (if a recruiter asks — not on the live guest form)

I want Summer 2027 on the team that keeps securities reference data and the security master true, not a market-data PM intern and not a data-platform ingest intern. Dual CS + Economics is the degree I already have. The analog I can defend is MDC (messy Excel → PAC ranking → Flask for a nonprofit) plus Vylet's stale-record / name-collision RCA. I will not invent Bloomberg or analysis-SQL JOINs the page cannot support.

---

## "Tell us about a project" / data validation / SQL / Python

**MDC (messy filings → ETL → ranking → API).** Irregular Excel exports and portal caps; Requests + Pandas ETL; PAC ranking; Flask on EC2; ~800 hours / 400 PACs. Best ingest → transform → stakeholder output story.

**Vylet (discrepancy + SQL freshness).** Injection-safe SQL timestamp / re-scrape; name-collision reject 79% → 89%. If they ask for SQL as analysis (JOIN that produced a ranking): Pandas/Python did that work; SQL on this resume is freshness (`grade.md`).

**Lyndbrook (entity resolution + score).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision. Public operational data, not Tradeweb reference data. Say that out loud if they ask about domain.

**SignalWeaver (dashboard analog).** React/Postgres; 90 tickers; out-of-sample regression 3.39% R². Research assistant, not advice. Do not lead with LoRA — this is not a Quant intern.

**CaseStudyPrep.AI (only if they ask about the co-op line on the form).** Voice-AI co-op. Do not lead with this for Data Management.

---

## Availability

Full-time, paid, **New York, NY (245 Park Ave)**, **Summer 2027**. Term dates not printed on 301946 — confirm with the recruiter; do not invent sibling SWE dates. Returning to the University of Michigan after the internship (Expected May 2028). US citizen; no sponsorship. Comp: accept posted **$22–$25/hr**. Housing: this JD does not print it — do not claim company housing.

**NYC housing / living plan (if a free-text box appears): do not invent an address or roommate plan Vedant has not given.** Kit fact only: willing to relocate from Northville, MI for the term at own cost unless Tradeweb later offers housing. If they require a specific housing paragraph, **Vedant writes it.**

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Oracle CX field.** Override Autofill. Never type `vedantde@umich.edu`. Never email this packet — App Man pulls via `gh`.
- **GPA is 3.7 on the PDF and on every form field.** Do not type 3.66.
- **Highest education obtained = High School Diploma / GED.** Bachelor's is in progress.
- **Jobs on the form = Vylet + CaseStudyPrep only.** MDC stays extracurricular.
- **Do not check Excel-as-claimed-skill, Bloomberg, Snowflake, Databricks, Tableau, Copilot, Fusion.** Honest: Python, SQL, Pandas, PostgreSQL, Flask, AWS EC2, Docker, Git.
- **This is Data Management 301946**, not 301932, not 301904.
- **No Tradeweb contact in `network.md`.** How you heard: pick the true board. Airtable says GitHub/SimplifyJobs — **Vedant confirms**.
- **Funnel:** resume is the bottleneck (`persona.md` / `companies.md`). No published OA. Prep STAR (MDC stakeholder scoping; Vylet 79%→89% RCA) and walk SQL as freshness. Confirm US citizen, GPA 3.7, May 2028, NYC Summer 2027.
- **This agent did not submit.**
