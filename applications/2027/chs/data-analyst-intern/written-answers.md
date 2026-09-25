# CHS — Data Analyst Intern (Job ID 25111) · Written Application Answers

Draft answers for SuccessFactors RMK `careers.chsinc.com` / CAS company **CHSProd** req **25111** (posting **1433568700**). Grounded in `persona.md`, `grade.md` Interview angles, and `context.md` metrics only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Power BI, Tableau, Snowflake, Dataiku, DAX, Excel-as-claimed-tool, Power Apps, Power Automate, Copilot, Fusion, CHS TMS/ERP, grain-trading internships.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** PDF header is **verdent06@gmail.com**. Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Job (live ATS): https://careers.chsinc.com/job/Inver-Grove-Heights-Data-Analyst-Intern-MN-55077-1721/1433568700/?ats=successfactors

Apply: https://careers.chsinc.com/talentcommunity/apply/1433568700/?locale=en_US

Resume: `applications/2027/chs/data-analyst-intern/Vedant Desai Resume.pdf`

**SHA-256:** `81d141b8a4fde24f30b539c6b861e4dee042cb4be6ceb69de054d6ffbc367e94`

Posted **2026-09-24**. **This is Transportation/Supply Chain Data Analyst Intern 25111 — not Refined & Renewable Fuels Trading Intern 25116, not Strategic Sourcing Intern 25087, not a SWE intern.**

---

## What was extracted from the live page (2026-09-25)

Pulled without creating an account, without uploading a resume, and without submitting.

### Job posting (public RMK)

| Label / field on the posting | Value |
| --- | --- |
| Title | **Data Analyst Intern** |
| Company | **CHS, Inc.** |
| Location | **Inver Grove Heights, MN, US, 55077-1721** |
| Date posted | **Sep 24, 2026** |
| Employment Type | **Hourly** |
| Schedule | **Seasonal** |
| Job ID | **25111** |
| Work Arrangement | **On-Site** (body: **Hybrid** 3–4 days in the office) |
| Salary Range | **$17.00 - $25.00 /hr** |
| RMK posting id | **1433568700** |
| Apply control (verbatim) | **Apply now »** → `/talentcommunity/apply/1433568700/?locale=en_US` |
| LinkedIn apply | **disabled** (`applyWithLinkedIn2Config.enabled: false`; `internalId` `25111-en_US`) |
| Source id | `JATS-CHSProd` |
| CAS / SSO | `ssoCompanyId` **CHSProd** · `ssoUrl` **https://career4.successfactors.com** · `useCASWorkflow` **true** |
| Site note (verbatim) | *PLEASE NOTE: Due to a system change on March 29, 2021, you will need to create a new account to apply to a job.* |

### Apply chrome (live JS, 2026-09-25)

Clicking **Apply now »** runs `j2w.Apply.handleApplyNowButton` → CAS `collectForCASWorkflow` (`POST /services/cas/createpayload/`) → SSO POST to `career4.successfactors.com` (company **CHSProd**, `career_job_req_id` **25111**). Unauthenticated `/services/applycontroller/apply/?jobid=1433568700` 307s to `/services/apply/redirectnotc/1433568700` then 302s to career4, which 302s back to `/job-invite/25111/` (the JD).

**Later wizard pages (My Information, experience, job-specific questions, EEO) were not visible.** Do not invent extra essay prompts. If later pages differ, answer the actual question.

### Account / apply field labels (verbatim from live `strings_en_US.js` on this careers host)

These are the RMK i18n strings this site actually loads (`careers.chsinc.com/platform/js/localized/strings_en_US.js`). They are **form labels / validation copy**, not JD knockouts.

| Exact string | Use |
| --- | --- |
| First Name is required. | First Name |
| Last Name is required. | Last Name |
| Primary Email is required. | Primary Email |
| Email address is required. / Email is required. | Email Address |
| Phone Number is required. | Phone Number |
| A Resume is required. | Resume upload |
| Upload Your Resume | Resume upload control |
| Password is required. | Password |
| Confirm Password is required. | Confirm Password |
| Password and Confirm Password must match. | Confirm |
| Forgot Password? | Returning user |
| Country/Region is required. | Country/Region |
| The Data Privacy Consent Statement must be reviewed. | DPCS |

Password rules (verbatim `tcpwrequirements` + live `passwordRegEx`): **6–20 characters**; at least one alpha; at least one number or special; no more than three consecutive identical characters; no unicode/spaces.

### Create Account / Sign In (CAS login wall)

Exact later-page widgets were **not rendered** without an account. Use:

| Exact label (from live i18n) | Answer |
| --- | --- |
| Email / Primary Email / Email Address | **verdent06@gmail.com** (never vedantde@umich.edu) |
| Password | **Your real password.** Not stored in this repo. 6–20 chars per the regex above |
| Confirm Password | Same |
| First Name | Vedant |
| Last Name | Desai |
| Phone Number | **2487044852** / **(248) 704-4852** |
| Country/Region | **United States** |
| Resume | `applications/2027/chs/data-analyst-intern/Vedant Desai Resume.pdf` |
| Data Privacy Consent Statement | Read and accept if accurate |
| Forgot Password? | Only if you already have a **CHSProd** account from after 2021-03-29 |

Do **not** have this agent create the account or complete the apply.

---

## Knockouts (read first)

1. Currently enrolled in Business Analytics, MIS, Statistics, Mathematics, **Economics**, Business Administration, International Business, Supply Chain, or related — **clears.** B.S. Computer Science and Economics.
2. Entering junior or senior year, or recent graduate — **clears.** Summer 2027 = entering junior year; Expected May 2028.
3. Hybrid commute to Inver Grove Heights HQ (3–4 days in office), May/June 2027 full-time — **Yes.** Relocate from Northville, MI for the term. Do not claim a Twin Cities commute from Michigan.
4. Microsoft suite / Power BI or Tableau — **do not check Power BI or Tableau.** Walk Pandas-on-Excel-exports and SignalWeaver React/Postgres. Microsoft Office for coursework only if they ask proficiency — do not claim Excel as an interview tool.
5. DAX and SQL (additional) — SQL **Yes** (on the PDF through use as DAL freshness). **Do not check DAX.**
6. Work authorization — **not printed on this JD.** Answer **US citizen / no sponsorship** if asked.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on location, dates, Power BI, Snowflake, or Dataiku.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **SpaceXAI Campus Lead Ambassador = extracurricular if asked.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66, Junior, 96 credits by Summer 2027.
- Languages you can defend: **Python, SQL** (on this PDF). TypeScript/React if they ask about the dashboard. **Do not check Power BI, Tableau, Snowflake, Dataiku, DAX, Excel as a skill you interview in.**

---

## Knockout / structured fields (fill exactly)

### Profile / My Information (login wall — confirm live labels)

| If the live label is | Answer |
| --- | --- |
| Country / Country/Region | **United States** |
| First Name | Vedant |
| Last Name | Desai |
| Address Line 1 | **49032 Freestone Dr** |
| City | **Northville** (not Ann Arbor) |
| State | **Michigan** |
| Postal Code | **48168** |
| Email / Primary Email | **verdent06@gmail.com** |
| Phone | **(248) 704-4852** · Mobile · **United States (+1)** |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub / Website | https://github.com/Verdent06 · https://vyletdata.com if a second URL |
| How did you hear about us? | The board you actually used. **No CHS contact in `network.md` — do not pick Employee Referral.** If you opened careers.chsinc.com: **Company website**. If LinkedIn: **Job Board → LinkedIn**. |
| Willing to relocate / commute to Inver Grove Heights? | **Yes** — relocate for Summer 2027 |
| Start May/June 2027 full-time? | **Yes** |
| Age 18+ | **Yes** |
| Date of birth (if asked) | **12/16/2006** |
| SAT (if asked) | **1510** |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### Education

| Exact label | Answer |
| --- | --- |
| School or University | **University of Michigan** (Ann Arbor — not Dearborn/Flint) |
| Degree | **Bachelor of Science (BS)** |
| Field of Study | **Economics** if they want a listed major; **Computer Science** if one major and CS is accepted as related. Dual: add the second if a second row exists |
| Overall Result (GPA) | **3.66** |
| From | **08/2025** (started **08/31/2025**) |
| To (Actual or Expected) | **05/2028** |
| Currently enrolled | **Yes** |
| Class standing | **Junior** |
| High School | **Northville High School** |
| High School graduation date | **05/19/2025** |

### Work history on the form (not the PDF)

| Employer | How to enter |
| --- | --- |
| Vylet | **Job.** Founder. May 2026 – Present. Remote / Northville, MI. |
| CaseStudyPrep.AI | **Job.** Software Engineer Co-op (Voice AI). Dec 2025 – May 2026. Remote. |
| Michigan Data Consulting (MDC) | **Extracurricular / organization / project only.** |
| Lyndbrook Capital | **Omit from the form** (still on the PDF). |
| SpaceXAI Campus Lead Ambassador | **Extracurricular only.** |
| Granular Synthesizer / SignalWeaver | **Not jobs.** |
| Awards / honors | **None.** |

### Job-specific questions (not visible — login wall)

Do **not** invent essays. If a later step restates the JD qualifications as radios, use:

| If the live label is | Answer |
| --- | --- |
| Currently enrolled in Business Analytics / MIS / Stats / Math / Economics / Business / Supply Chain or related? | **Yes** — B.S. Computer Science and Economics, University of Michigan |
| Entering junior or senior year (or recent graduate)? | **Yes** — Junior; Expected May 2028 |
| Available May/June 2027 full-time? | **Yes** |
| Can you work hybrid (3–4 days) at Inver Grove Heights HQ? | **Yes** — will relocate from Northville, MI for the term |
| Are you legally authorized to work in the United States? | **Yes** |
| Will you now or in the future require visa sponsorship? | **No** |
| Citizenship | **US citizen** |
| Returning to school after the internship? | **Yes** — Expected May 2028 |
| Graduation date | **May 2028** |
| Ever worked for CHS? | **No** |
| Power BI / Tableau / Dataiku / Snowflake / DAX | **No** — do not check. Walk SignalWeaver React/Postgres dashboard and Pandas ETL |
| Microsoft Office / Excel / Teams / Outlook | **Yes** for coursework / reports if they ask proficiency. Do **not** list Office on the resume or claim you interview in Excel. Walk Pandas on irregular Excel exports instead |
| Python / SQL | **Yes** if asked — both through use on the PDF |
| How did you hear | Company website / the board you used. **Not** Employee Referral |
| Pay $17–$25/hr | **Yes** — accept the posted intern range |

Voluntary EEO / disability / veteran: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

Review: check email is **verdent06@gmail.com**, IGH hybrid, dates, PDF attached. Do not submit from this agent.

---

## Cover letter / additional information (paste if SuccessFactors has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

CHS Inc. — Data Analyst Intern (Job ID 25111)
Inver Grove Heights, MN (hybrid)

I am applying for the Summer 2027 Data Analyst Intern seat on CHS's Transportation/Supply Chain Business Intelligence team in Inver Grove Heights — Job ID 25111 — not the fuels trading intern, not Strategic Sourcing, and not a SWE intern. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work full-time hybrid at HQ from May/June 2027 and return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

I have not used Power BI, Tableau, Snowflake, Dataiku, or DAX. What I can defend is messy operational data → ranking/KPI → a report or dashboard a non-builder used.

What I would bring:

- **Irregular Excel → KPI report for a stakeholder.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month contract. That is the analog I will walk for extract/clean/integrate and stakeholder reporting.
- **Scoring / shortlist in an ops window.** At Lyndbrook Capital I built a Review Velocity score that filtered 800 acquisition targets to a 280-lead shortlist (35% precision) from multi-source public data. Closest analog to transportation/ops KPIs with a deadline.
- **Data freshness / accuracy testing.** On Vylet I wrote SQL timestamp checks that re-scrape stale records, and a name-collision fix that lifted qualification from 79% to 89%. If you ask for SQL as analysis (JOIN that produced a ranking): Pandas/Python did that work; SQL on this resume is freshness.
- **A dashboard you can click.** SignalWeaver: React/TypeScript dashboard over 90 tickers persisted in Postgres. Not Power BI/Dataiku.

I will relocate to Inver Grove Heights for the hybrid 3–4 day schedule.

Vedant Desai

---

## Short paste blurb (if the form has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to Data Analyst Intern 25111 — Transportation/Supply Chain BI in Inver Grove Heights, not trading and not sourcing. I ship analytics: Pandas ETL on irregular Excel filings that cut ~800 hours of pulls across 400 PACs, a Flask report API for MCFN, a 800→280 scored shortlist at 35% precision, and a React/Postgres dashboard. I have not used Power BI, Tableau, Snowflake, or Dataiku. U.S. citizen; no sponsorship. IGH hybrid May/June 2027.

---

## "Why CHS / why this intern?"

I want Summer 2027 hybrid at IGH on Job ID 25111 — Transportation/Supply Chain BI: extract messy sources, make a dataset a stakeholder can trust, and put the KPI on a dashboard. I have not interned on Power BI or Snowflake. The analog I can defend is MDC (messy Excel → PAC ranking → Flask report for a nonprofit) plus Lyndbrook if they ask how I score a list against a criterion. I will not invent a childhood-ag or Cenex story the page cannot support.

---

## "Tell us about a project" / experience with data / dashboards

**MDC (messy Excel → pipeline → ranking → stakeholder report).** Irregular filings; Pandas ETL; PAC ranking; ~800 hours / 400 PACs; Flask REST on EC2 to researchers. Best analog to retrieve/clean/integrate + dashboard/report + comms.

**Lyndbrook (KPI / logistics analog).** Review Velocity 800 → 280 at 35% precision; 800+ Day-1 targets in an engagement window. Water-utility operators, not CHS grain/energy. Say that out loud if they ask about domain.

**Vylet (data quality + SQL).** 79%→89% qualification; SQL timestamp / re-scrape. If they ask for analyst SQL, walk freshness — ranking was Pandas (`grade.md`).

**SignalWeaver (dashboard analog).** React/Postgres; 90 tickers. Not Power BI/Dataiku. Research assistant, not advice. Do not lead with LoRA.

---

## Availability

Full-time intern, **hybrid Inver Grove Heights HQ (3–4 days in office)**, **May/June 2027** (treat as the official **12-week** intern program unless the form prints dates). Returning to the University of Michigan (Expected May 2028). Housing: this JD does not print it — do not claim company housing. Comp: **$17–$25/hr** as posted.

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every SuccessFactors field and on the PDF header.** Do not type `vedantde@umich.edu`.
- **Do not claim Power BI, Tableau, Snowflake, Dataiku, DAX, or Excel as an interview skill.** Walk Pandas-on-Excel-exports and SignalWeaver as the dashboard analog (`persona.md` anti-pattern).
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). Awards = **None**.
- **IGH hybrid relocate is not a skip.** Say yes. Northville is not a commute.
- **Referral:** none in `network.md`. A real CHS / early-careers name beats Company Website; a fake name is a knockout.
- **Cover letter:** skip unless the form asks; paste from the letter above if it does.
- **Resume is the intern bottleneck** (`companies.md` C-tier, no published OA, ~20–30%). Posted **2026-09-24** — apply this wave (`recruiting.md` §8).
- **Transcript:** upload unofficial UMich transcript if a later step requires it. Not stored in this repo.
- **Do not apply from this agent. Do not email this packet.**
