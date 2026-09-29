# Verizon Communications — Business Intelligence Intern (R-1101387) · Written Application Answers

Draft answers for Workday `verizon.wd12` / `verizon-careers` req **R-1101387**. Grounded in `persona.md`, `grade.md` Interview angles, and `context.md` metrics only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Tableau, Looker, GCP, GECX, ConvoIQ, LangChain, AutoGPT, NotebookLM, Snowflake, Databricks, Copilot, Fusion, fiber-tech field work, Verizon internal support-center systems.

**Form kit email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu` on this apply flow.** PDF header is **verdent06@gmail.com**. Phone **248-704-4852**. Address **49032 Freestone Dr, Northville, MI 48168**. US citizen, no sponsorship. Work-authorized **Yes**.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Job (live ATS): https://verizon.wd12.myworkdayjobs.com/verizon-careers/job/Irving-Texas/Verizon-Network-and-Technology--Business-Intelligence-Summer-2027-Internship_R-1101387

Apply: https://verizon.wd12.myworkdayjobs.com/verizon-careers/job/Irving-Texas/Verizon-Network-and-Technology--Business-Intelligence-Summer-2027-Internship_R-1101387/apply

Resume: `applications/2027/verizon/business-intelligence-intern/Vedant Desai Resume.pdf`

**SHA-256:** `5856636cf1fa6f891c14e431aa2c1ff7ac3636668bb538f97a0ebde7b6d50c66`

**This is FE&O Business Intelligence intern R-1101387 (Fiber Engineering & Operations Transformation & Business Enablement / Center Operations Agile Transformation) — not Data Science Summer 2027 Internship R-1101384, not Irving V Teamer for a Day DS R-1101386, not a SWE intern.** Submit a separate application for each Verizon req (`recruiting.md` / JD: "Interested in multiple roles? Please submit a separate application").

---

## What was extracted from the live page (2026-09-29)

Pulled without creating an account, without uploading a resume, and without submitting. Chrome/Puppeteer dump of the public posting, Apply modal, `/apply`, `/apply/applyManually`, `/apply/autofillWithResume`, Sign in with email, and Create Account. Workday CXS job JSON confirmed the same posting metadata. Questionnaire endpoints returned **HTTP 406** without an account.

### Job posting (public)

| Label / field on the posting | Value |
| --- | --- |
| Title | **Verizon Network and Technology: Business Intelligence Summer 2027 Internship** |
| Company | Verizon Communications (hiringOrganization: **9108 Verizon Data Services LLC**) |
| Requisition | **R-1101387** · jobPostingId `Verizon-Network-and-Technology--Business-Intelligence-Summer-2027-Internship_R-1101387` · jobPostingInfo.id `85bd72cb8e901001fd896c01759b0000` |
| Location | **Irving, Texas** · **700 Hidden Ridge, Irving, TX (TX0330)** |
| Time type | **Full time** |
| Posted | **Posted Today** · `startDate` **2026-09-29** |
| End date | **October 3, 2026** (3 days left to apply on capture) · Workday `endDate` **2026-10-03** |
| Term (JD body) | **June 2027 to August 2027**, 10-week hybrid, 40 hours/week |
| Apply URL | Workday `/apply`. `includeResumeParsing: true` · `canApply: true` |
| Nav chrome | **Sign In** · **Careers Home** |

### Start Your Application (verbatim modal after Apply)

Exact labels on the live SPA (2026-09-29), `data-automation-id`s: `autofillWithResume`, `applyManually`, `useMyLastApplication` (DOM also had `applyWithLinkedIn`; it was **not** in the visible text dump):

- Heading: **Start Your Application**
- Subtitle: **Verizon Network and Technology: Business Intelligence Summer 2027 Internship**
- **Autofill with Resume**
- **Apply Manually**
- **Use My Last Application**

### Workday apply chrome (progress bar — verbatim)

**Apply Manually** (`/apply/applyManually`): **7** steps.

1. **Create Account/Sign In** ← live stop (login wall)
2. **My Information**
3. **My Experience**
4. **Application Questions 1 of 2**
5. **Application Questions 2 of 2**
6. **Voluntary Disclosures**
7. **Review**

**Autofill with Resume** (`/apply/autofillWithResume`): **8** steps. Extra step is **Autofill with Resume** (step 2). Remaining: My Information, My Experience, Application Questions 1 of 2, Application Questions 2 of 2, Voluntary Disclosures, Review.

No **Self Identify** step on this progress bar (unlike some other Workday tenants). Do not invent one. If a later page adds it, decline to self-ID unless you choose otherwise.

### Create Account / Sign In (verbatim live fields)

Exact labels on `/apply/applyManually` after **Sign in with email** and **Create Account** (2026-09-29). Did **not** create an account.

Visible before Create Account:

- Consent: *By continuing, I agree that I have read the Verizon Candidate Privacy Notice. Verizon's career portal is operated by Workday, and you will be directed to Workday to continue your application.*
- **Sign in with Google**
- **Sign in with LinkedIn**
- **OR**
- **Sign in with email**

After **Sign in with email** (verbatim):

| Exact label | Answer |
| --- | --- |
| Email Address* | **verdent06@gmail.com** (never vedantde@umich.edu) |
| Password* | **Your real password.** Not stored in this repo |
| Sign In | Only if you already have a Verizon Workday account |
| Don't have an account yet? **Create Account** | Use this path if new |
| **Forgot your password?** | Only if you already have an account |
| Enter website (honeypot) | **Leave blank.** Live label: *Enter website. This input is for robots only, do not enter if you're human.* |

After **Create Account** (verbatim):

**Password Requirements:** (live order)

- An alphabetic character
- A lowercase character
- An uppercase character
- A minimum of 8 characters
- A numeric character
- A special character

| Exact label | Answer |
| --- | --- |
| Email Address* | **verdent06@gmail.com** |
| Password* | **Your real password.** Not stored in this repo |
| Verify New Password* | Same as Password |
| Consent | *By continuing, I agree that I have read the Verizon Candidate Privacy Notice.* Read it. |
| **I agree** | **Check** (`createAccountCheckbox`) |
| **Create Account** | Click after the above. Do not submit the job from this agent |
| Already have an account? **Sign In** | Use if you already have a Verizon Workday account |
| **Forgot your password?** | Only if you already have an account |
| Enter website (honeypot) | **Leave blank.** |

### Questionnaire API

- `questionnaireId`: `ae7f4698be281001c8c1a953f6d10000`
- `secondaryQuestionnaireId`: `1639cec528b01001ac0f7bd8dfb00000`
- CXS `/application` and `/questionnaire/{id}` returned **HTTP 406** without an account
- **Application Questions 1 of 2, Application Questions 2 of 2, My Information, My Experience, Voluntary Disclosures, Review were not visible.** Do not invent extra essay prompts. If later pages differ, answer the actual question.

---

## Knockouts (read first)

1. Currently enrolled bachelor's, graduation **December 2027 – June 2028** — **clears.** Expected **May 2028**.
2. Full-time hybrid 10-week intern **June 2027 – August 2027** — **Yes.** Relocate from Northville, MI to Irving, TX for the term; return to Michigan afterward.
3. Work authorization without restrictions or future sponsorship — **clears.** US citizen; **no** sponsorship now or later.
4. Willing and able to **travel** — **Yes** (Intern Marquee, Basking Ridge, NJ).
5. Willing and able to **relocate** — **Yes** (Irving, TX hybrid).
6. Preferred major CS / BI / analytics — **clears** (B.S. Computer Science and Economics). Not a hard knockout.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on Irving, dates, sponsorship, Tableau, or LangChain.

---

## Form-kit reminders

- **Prior jobs on the form:** CaseStudyPrep.AI SWE co-op **and** founder of **Vylet** only.
- **MDC = extracurricular / student-org client project** (still on the PDF as Experience).
- **Lyndbrook = consulting on the PDF; do not add as a third W-2 job.**
- **Awards / honors: None.**
- Education: UMich B.S. CS + Economics, Expected May 2028, GPA 3.66, Junior.
- Languages you can defend: **Python, SQL** (on this PDF). **LangGraph** and **Gemini** through use. **Do not check Tableau, Looker, GCP, GECX, ConvoIQ, LangChain, AutoGPT, NotebookLM.**

---

## Knockout / structured fields (fill exactly)

### My Information (login wall — standard Workday; confirm live labels)

| Exact label (typical Workday) | Answer |
| --- | --- |
| Country * | **United States of America** |
| First Name * | Vedant |
| Last Name * | Desai |
| Address Line 1 | **49032 Freestone Dr** |
| City | **Northville** (not Ann Arbor) |
| State | **Michigan** |
| Postal Code | **48168** |
| Email Address | **verdent06@gmail.com** |
| Phone Device Type * | **Mobile** |
| Country Phone Code | **United States of America (+1)** |
| Phone Number | **(248) 704-4852** |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub / Website | https://github.com/Verdent06 · https://vyletdata.com if a second URL |
| How Did You Hear About Us? | The board you actually used. **No Verizon contact in `network.md` — do not pick Employee Referral.** If you opened verizon.wd12: **Career Websites** / Company website. If LinkedIn: **Job Board → LinkedIn**. |

After Autofill: confirm email is **verdent06@gmail.com**. If MDC lands under Work Experience, **move it to extracurricular**.

### My Experience · Education

| Exact label | Answer |
| --- | --- |
| School or University * | **University of Michigan** (University of Michigan-Ann Arbor if the typeahead has it) |
| Degree * | **Bachelor of Science (BS)** |
| Field of Study | **Computer Science** (add **Economics** if a second row / dual-degree field is required) |
| Overall Result (GPA) | **3.66** |
| From | **08/2025** (started **08/31/2025**) |
| To (Actual or Expected) | **05/2028** |
| Currently enrolled | **Yes** |
| High School | **Northville High School** |
| High School graduation date | **05/19/2025** |

### Work history on the form (not the PDF)

| Employer | How to enter |
| --- | --- |
| Vylet | **Job.** Founder. May 2026 – Present. Remote / Northville, MI. |
| CaseStudyPrep.AI | **Job.** Software Engineer Co-op (Voice AI). Dec 2025 – May 2026. Remote. |
| Michigan Data Consulting (MDC) | **Extracurricular / organization / project only.** |
| Lyndbrook Capital | **Omit from the form** (still on the PDF). |
| Granular Synthesizer / SignalWeaver | **Not jobs.** |
| Awards / honors | **None.** |

### Application Questions 1 of 2 and 2 of 2 (login wall — confirm live labels; do not invent wording)

Two questionnaire pages exist on the progress bar (`questionnaireId` `ae7f4698be281001c8c1a953f6d10000`, `secondaryQuestionnaireId` `1639cec528b01001ac0f7bd8dfb00000`). Both were **HTTP 406** / not visible. If a later step restates the JD qualifications as radios, use:

| If the live label is | Answer |
| --- | --- |
| Currently enrolled in a Bachelor's program with graduation between December 2027 and June 2028? | **Yes** — Expected **May 2028**, University of Michigan |
| Available full-time hybrid June 2027 – August 2027 (10 weeks)? | **Yes** |
| Are you legally authorized to work in the United States without restrictions? | **Yes** — US citizen |
| Will you now or in the future require visa sponsorship? | **No** |
| Willing and able to travel? | **Yes** — Intern Marquee, Basking Ridge, NJ |
| Willing and able to relocate? | **Yes** — Irving, TX for the intern term; return to Michigan afterward |
| Hybrid Irving, TX (≥3 days/week in office)? | **Yes** |
| Class standing | **Junior** (Expected May 2028; Summer 2027 = after junior year / rising senior) |
| Graduation date | **May 2028** |
| Major | **Computer Science** (Economics as second field if allowed) |
| GPA | **3.66 / 4.0** |
| Ever worked for Verizon? | **No** |
| Tableau / Looker / GCP / GECX / ConvoIQ | **No** — do not check. Walk SignalWeaver React/Postgres dashboard |
| LangChain / AutoGPT / NotebookLM | **No** — do not check. Walk **LangGraph** + **Gemini** (both on the PDF) |
| Google Gemini | **Yes** if asked — embeddings in the Vylet DAL bullet |
| Python / SQL | **Yes** if asked — both through use on the PDF |
| Agile / Scrum | Coursework/team analog only if they ask experience. Do **not** invent a certified Scrum role. Walk MDC sole-engineer delivery inside a fixed engagement window |
| How did you hear | Company website / the board you used. **Not** Employee Referral |
| Returning to school after the internship? | **Yes** — Expected May 2028 |

Voluntary Disclosures: **I do not want to answer** / **Decline To Self Identify** unless you choose to self-ID. Not used in hiring.

Review: check email is **verdent06@gmail.com**, Irving, June–August 2027, PDF attached, **R-1101387** not the Data Science sibling. Do not submit from this agent.

---

## Cover letter / additional information (paste if Workday has a box)

Vedant Desai
248-704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Verizon Network and Technology — Business Intelligence Summer 2027 Internship (R-1101387)
Fiber Engineering & Operations / Center Operations Agile Transformation
Irving, TX (hybrid)

I am applying for the Summer 2027 Business Intelligence intern seat on Fiber Engineering & Operations Transformation & Business Enablement in Irving — Workday R-1101387 — not the Data Science intern (R-1101384) and not Irving V Teamer for a Day. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work full-time hybrid in Irving from June 2027 through August 2027, travel to Basking Ridge for Intern Marquee, and return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

I have not used Tableau, Looker, GCP, GECX, ConvoIQ, LangChain, AutoGPT, or NotebookLM. What I can defend is messy operational data → a score or ranking a stakeholder used, plus a LangGraph / Gemini pipeline I can walk.

What I would bring:

- **GenAI pipeline + data architecture.** On Vylet I shipped a Dockerized LangGraph pipeline that turns a ~30-minute manual process into 30 scored leads in 30 minutes (30x), and a SQL freshness layer over Gemini embeddings that re-scrapes stale records. That is the analog I will walk for agentic backlog work and LLM-log hygiene — not a claim of ConvoIQ or LangChain.
- **Irregular Excel → KPI report for a stakeholder.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL, then ranked PACs by funding volume so Michigan Campaign Finance Network researchers stopped rebuilding spreadsheets. That eliminated ~800 hours of manual pulls across 400 tracked PACs. I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month contract.
- **Scoring / shortlist.** At Lyndbrook Capital I built a Review Velocity score that filtered 800 acquisition targets to a 280-lead shortlist (35% precision) and delivered 800+ validated Day-1 targets inside the window.
- **A dashboard you can click.** SignalWeaver: React/TypeScript dashboard over 90 tickers persisted in Postgres. Not Tableau/Looker.

I can relocate to Irving for the term and travel for Intern Marquee.

Vedant Desai

---

## Short paste blurb (if the form has a small text box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to Business Intelligence intern R-1101387 — FE&O Transformation in Irving, not Data Science R-1101384. I ship analytics plus a GenAI pipeline: LangGraph scored leads (30x), Gemini embeddings with SQL freshness, a Pandas ETL that cut ~800 hours of pulls across 400 PACs, a 800→280 scored shortlist at 35% precision, and a React/Postgres dashboard. I have not used Tableau, Looker, GCP, or LangChain. U.S. citizen; no sponsorship. Irving hybrid June–August 2027; yes to travel.

---

## "Why Verizon / why this intern?"

I want Summer 2027 on R-1101387 — FE&O Center Operations Agile Transformation in Irving: take a live backlog item, turn customer/ops data into a number a support lead can use, and work next to an agentic pipeline I can actually walk (LangGraph + Gemini, not a claimed Tableau/LangChain stack). I have not interned in fiber repair or dispatch. The analog I can defend is MDC and Lyndbrook (messy public/ops data → ranked or scored output) plus Vylet if they ask how I keep a GenAI pipeline honest. I will not invent a childhood-telecom story the page cannot support.

---

## "Tell us about a project" / experience with data / dashboards / GenAI

**Vylet (GenAI + data architecture).** Dockerized LangGraph; 30 scored leads / 30 minutes; Gemini embeddings; SQL timestamp / re-scrape. Closest analog to "fine-tune agentic AI" and "LLM performance logs" without claiming ConvoIQ. If they ask for LangChain: I used LangGraph, not LangChain — say that.

**MDC (messy Excel → pipeline → ranking → stakeholder report).** Irregular filings; Pandas ETL; PAC ranking; ~800 hours / 400 PACs; Flask REST on EC2 to researchers. Best analog to gather/validate/organize + report + comms.

**Lyndbrook (predictive / scoring analog).** Review Velocity 800 → 280 at 35% precision; 800+ Day-1 targets. Public operational data, not fiber tickets.

**SignalWeaver (dashboard analog).** React/Postgres; 90 tickers; composite score with out-of-sample 3.39% R². Not Tableau/Looker. Research assistant, not advice. Do not lead with LoRA.

---

## Availability

Full-time intern, **hybrid Irving, TX** (700 Hidden Ridge / TX0330; ≥3 days/week in office), **June 2027 – August 2027**, 10 weeks, 40 hours/week. Returning to the University of Michigan (Expected May 2028). Intern Marquee travel to Basking Ridge, NJ: **Yes**. Relocation to Irving for the term: **Yes**; return to Michigan afterward. Comp: accept posted intern pay (unlisted; Verizon intern band **[directional]**).

---

## Notes for the applicant (not for submission)

- **Email is `verdent06@gmail.com` on every Workday field and on the PDF header.** Do not type `vedantde@umich.edu`.
- **Window is three days.** Posted 2026-09-29; `endDate` **2026-10-03**. Apply this wave (`recruiting.md` §8).
- **This is R-1101387 only.** Do not upload this PDF to Data Science **R-1101384** or V Teamer-for-a-Day **R-1101386**.
- **Do not claim Tableau, Looker, GCP, GECX, ConvoIQ, LangChain, AutoGPT, or NotebookLM.** Walk LangGraph + Gemini and SignalWeaver as the dashboard analog (`persona.md` anti-pattern).
- **Form jobs = CaseStudyPrep.AI + Vylet only.** MDC = extracurricular (still on the PDF). Awards = **None**.
- **Irving relocate + Marquee travel are not skips.** Say yes.
- **Referral:** none in `network.md`. A real FE&O / early-careers name beats Career Website; a fake name is a knockout.
- **Cover letter:** skip unless the form asks; paste from the letter above if it does.
- **Resume is the intern bottleneck** (`companies.md` C-tier, no published coding OA, ~15–25%). ADEPT-15 + 6-question video are **[directional, Extern]** — complete them if Workday issues them; they are not LeetCode.
- **Transcript:** upload unofficial UMich transcript if a later step requires it. Not stored in this repo.
- **Do not apply from this agent. Do not email this packet.**
