# Deloitte — Consultative Offerings Summer Scholar, Data & AI Solutions Engineering (Atlanta) · Written Application Answers

Draft answers for Avature req **363475** (FY27 sourcing). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this." **Do not invent Snowflake, Databricks, Copilot, Fusion, Tableau, Informatica, Hadoop, Spark, Power BI, R, Java, TensorFlow, or a second messy-dataset story.** Trim to the form's length limit before submitting.

**This is not** Forensic Analytics and **not** GPS AI and Data Engineering (req 362479). Title: Consultative Offerings — Summer Scholar — Data & AI Solutions Engineering. Target office: **Atlanta, GA**. Use this folder's PDF.

Apply: https://apply.deloitte.com/en_US/careers/JobDetail/Consultative-Offerings-Summer-Scholar-Data-AI-Solutions-Engineering/363475

Simplify: https://simplify.jobs/p/2440120c-cae1-4ca3-8e9b-73e8ca4bfac9

Recruiting ends **11/01/2026**. $48/hour. Onsite; travel up to 50%. Apply in this wave (`recruiting.md` §8).

Avature **Register** (jobId=363475) is structured knockouts only — no essay, cover-letter, or "Why Deloitte" box on profile create. Later wizard steps after login were not reachable without submitting. Paste the letter only if a later step or recruiter asks. Recruiter/phone screen still tests why this scholar, Atlanta commute, 50% travel, and no-sponsorship (`company.md`).

---

## Knockout / structured fields (fill exactly)

From the live Register form at `apply.deloitte.com/en_US/careers/Register?jobId=363475`. Application Methods first: **Upload Resume from Device** (.pdf/.doc/.docx, max 30MB) — use this folder's PDF. Do not Apply with LinkedIn if it will overwrite bullets.

| Field | Answer |
| --- | --- |
| First name (legal) | Vedant |
| First name (preferred) | Vedant |
| Middle name | leave blank unless the form requires it |
| Last name | Desai |
| Preferred email | vedantde@umich.edu |
| Phone number | (248) 704-4852 |
| Address line 1 / 2, city, state, zip | **Your real current mailing address.** Not in `context.md`. Do not invent a street. Education location is Ann Arbor, MI. |
| Country | United States |
| Resume/CV | `applications/2027/deloitte/data-ai-solutions-engineering-summer-scholar/Vedant Desai Resume.pdf` |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Do you have or plan to pursue a CPA license? | **I do not have or plan to pursue a CPA license** — this is Data & AI Solutions Engineering, not Audit |
| As of today, have you completed this degree/program? | **No** |
| Expected graduation date | **May 2028** (Month/Year) |
| School | **University of Michigan** (search the school list; if missing: Other → University of Michigan) |
| Education Level | **Bachelor's** |
| Primary Major/Program | **Computer Science** (Economics is the second major — if the form allows a second major/program, add Economics. Both are listed majors on this JD.) |
| GPA Overall | **3.66** |
| GPA Scale | **4.0** |
| Major GPA (if N/A please enter 0.0) | **0.0** unless you have a separate major GPA recorded — `context.md` has overall 3.66 only |
| Legally authorized to work in US? | **Yes** — other 2027 applications treat you as a US citizen. Answer truthfully. `context.md` has no citizenship field. |
| Will you now or in the future require sponsorship for employment visa status (for example, H-1B Visa)? | **No** — JD: no employer sponsorship now or in the future. This is a knockout. |
| Former U.S.-based Deloitte employee? | **No**. Leave personnel ID / prior Deloitte email / birth MM-DD blank unless the form still requires **N/A** when No. |
| Office / location preference (if a later step asks) | **Atlanta, GA**. Same req is posted in 18 cities including Detroit. This packet is Atlanta. Willing to relocate to Atlanta for Summer 2027 and commute daily. |
| Travel up to 50%? | **Yes** |
| How did you hear about this role? | **Simplify** / Other → Simplify.jobs. No Deloitte contact in `network.md`. |
| Pay $48/hr | **Yes** — accept the posted intern wage estimate |
| Maryland / Massachusetts / Rhode Island notice | Check **I acknowledge** |
| Privacy Notice | Check **I acknowledge** (https://www.deloitte.com/us/en/legal/privacy-notices.html) |
| Languages / tools you can interview in | **Python, SQL, Pandas, LangGraph, pgvector, AWS (EC2/S3), Docker.** Do **not** check Tableau, Power BI, Informatica, Hadoop, Spark, R, Java, TensorFlow, Snowflake, Databricks, Copilot, or Fusion |

---

## Cover letter / "Why Deloitte / why Data & AI Solutions Engineering?" (paste if a later step has a box)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

Deloitte Consulting LLP — Consultative Offerings, Data & AI Solutions Engineering
Atlanta, GA

Re: Consultative Offerings — Summer Scholar — Data & AI Solutions Engineering (Job 363475)

Dear Data & AI Solutions Engineering hiring team,

I am applying to the Summer 2027 Data & AI Solutions Engineering Summer Scholar seat in Consultative Offerings — Atlanta onsite — not Forensic Analytics and not GPS AI and Data Engineering. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am authorized to work in the United States without visa sponsorship. I will relocate to Atlanta for the term and can travel up to 50%.

The scholar job is applied data and AI delivery in a client environment: extract/transform/analyze, pipelines that make models usable, and agentic systems with checkpoints — not a research rotation and not a generic SWE intern. That is the work I already do. I have not interned at a Big Four firm. I have shipped the path — messy sources in, a pipeline or API out, a number on what it changed — scoped with a real stakeholder.

What I can defend:

- **Messy filings → Pandas ETL → client API.** At Michigan Data Consulting I replaced portal searches and irregular Excel exports (~2 hours per committee) with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2 to Michigan Campaign Finance Network researchers, eliminating ~800 hours of manual pulls across 400 tracked PACs. I scoped ingestion through REST endpoints with MCFN as the only engineer on a five-month contract. Analog to forward-deployed delivery; not a Deloitte engagement.
- **Agentic pipeline + eval gates.** I run Vylet, a live PE/search-fund lead-sourcing product ($1,500 MRR, three paying clients). I shipped a Dockerized LangGraph pipeline (30 scored leads in 30 minutes, a 30x speedup) and a LangSmith eval over 20 adversarial cases that lifted extraction faithfulness from 50% to 90% with Pydantic consensus gates. SQL is in the production DAL (asyncpg, injection-safe timestamp checks, automatic re-scrapes). That is observe/decide/act with a fail-closed checkpoint — not a notebook.
- **Consultant-shaped scoring.** At Lyndbrook Capital I aggregated EPA ECHO and MassGIS into a PWSID entity database (800+ Day-1 targets) and built a Review Velocity score from public compliance data that cut the list to 280 leads at 35% precision against the fund's revenue criteria.

I have not used Tableau, Informatica, Hadoop, Spark, Power BI, R, Java, Snowflake, Databricks, Copilot, or Fusion. I would ramp on the team's approved stack rather than pretend I already have it. SQL on my page is freshness/validation in the Vylet DAL, not a warehouse transform — I will say that if you ask.

I can be onsite in Atlanta for Summer 2027. I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

Sincerely,
Vedant Desai

---

## Short paste blurb (if Avature has a small additional-information box)

I'm a Computer Science & Economics student at Michigan (Expected May 2028, GPA 3.66) applying to Consultative Offerings Data & AI Solutions Engineering Summer Scholar in Atlanta (req 363475) — not Forensic Analytics, not GPS AI and Data Engineering. I ship Python pipelines and client delivery: a Pandas ETL that cut ~800 hours of PAC research, a LangGraph agentic pipeline with a 50%→90% eval gate, and a consultant scoring model (800→280 at 35% precision). SQL is a production freshness check, not a warehouse. I have not used Tableau or Informatica. I will relocate to Atlanta, travel up to 50%, and do not need visa sponsorship.

---

## Likely later-step / recruiter short answers

Exact post-register essay text was not visible without creating a profile. If a box appears, paste a trimmed version of the matching block. Do not invent.

### Why this scholar / why Consultative Offerings Data & AI (not GPS, not Forensic Analytics)?

I want the applied delivery seat: pipelines, genAI/agentic activation, and client stakeholders. Consultative Offerings packages that as solutions engineering, not a one-off staff-aug ticket and not a government AI/data engineering posting. Forensic Risk can show up as a *project type* on this scholar seat (`persona.md`); I am not applying to the Forensic Analytics scholar req. I have not done e-discovery or forensic accounting.

### Why Atlanta? Can you commute / relocate?

Yes. I will relocate to Atlanta for Summer 2027 and commute daily to the assigned office. I am currently in Michigan (UMich; 248 area code). The commute-distance rule is for the internship term, not a claim that I already live in Georgia. Same req lists Detroit; this application is Atlanta as specified.

### Tell us about a project / messy data / pipelines / SQL

**MDC (messy filings → Pandas ETL → Flask API).** Irregular Excel exports and portal caps; ~800 hours / 400 PACs; scoped with MCFN. This is the grounded messy-dataset story.

**Vylet (agentic + SQL + eval).** LangGraph 30x; LangSmith 50%→90% with fail-closed Pydantic gates; asyncpg SQL timestamp validation and re-scrapes. If they ask for a SQL *transform* metric: there isn't one in the pool — walk the control (stale row → re-scrape) honestly (`grade.md` Defend).

**Lyndbrook (consultant scoring).** EPA ECHO + MassGIS → 800 targets → 280-lead shortlist at 35% precision.

**SignalWeaver (vector search / dashboard).** pgvector 49ms p50 over financial news; React dashboard. Research assistant, not investment advice. Do not call this Tableau. LoRA 81%→96% is in the pool if they ask about model work; it is not on this resume page.

### Tell us about working with a non-technical / client stakeholder

MDC: ingestion through REST endpoints with MCFN researchers (nonprofit, not engineers). Lyndbrook: Principal of a search fund, 15 hours/week of prospecting removed. That is the consulting analog. I have not been staffed on a Fortune-500 client site.

### Willing to travel 50%?

Yes.

---

## Availability

Summer 2027, onsite Atlanta. Available to start May/June 2027. Returning to the University of Michigan after the internship (Expected May 2028). Travel up to 50%.

---

## Notes for the applicant (not for submission)

- **Use this PDF.** Do not paste a full-stack SWE resume into Avature.
- **Sponsorship is a knockout.** JD: no employer sponsorship now or in the future (`recruiting.md` §1). Answer the visa question truthfully.
- **Do not claim Tableau, Informatica, Hadoop, Spark, Power BI, R, Java, TensorFlow, Snowflake, Databricks, Copilot, or Fusion.** Named as examples on the JD; not demonstrated. Honest Python/SQL/Pandas/LangGraph beats a keyword lie (`persona.md` anti-pattern; `resume.md` §8).
- **SQL honesty.** One DAL/validation beat on Vylet — not a warehouse (`grade.md` minor demerit). Script the walkthrough before the recruiter screen.
- **Do not invent a second messy-dataset bullet.** MDC irregular filings is the real one.
- **Atlanta is not a skip.** Relocate for the term. Detroit is on the same req; do not silently switch offices in this packet.
- **No Deloitte contact in `network.md`.** A UMich alum in the Atlanta consulting practice still beats a cold Avature pile (`recruiting.md`: HM > recruiter > engineer > cold apply).
- **Cover letter is optional on Register.** If a later step offers an upload, use the letter above. Recruiter screen still asks why this scholar (`company.md`).
- **Next loop:** no coding OA (`companies.md` Deloitte Tech). STAR + a candidate-led case. Lead with Vylet eval gates, MDC client ETL, Lyndbrook scoring (`grade.md` Interview angles).
