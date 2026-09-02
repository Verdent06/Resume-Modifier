# Eulerity — Backend Developer Intern (Summer 2027, NYC) · Written Application Answers

Greenhouse job `4709040006` (`first_published` 2026-09-01). Labels and dropdowns from `https://boards-api.greenhouse.io/v1/boards/eulerity/jobs/4709040006?questions=true` plus the live apply page. Grounded in `persona.md`, `grade.md`, and `context.md` only.

**Do not invent:** Java, Spring, JUnit, Snowflake, Databricks, Copilot, Fusion, Tableau, Sentry, NYC address, MatchStream.

**Form + PDF email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu`.** Phone **(248) 704-4852**. Junior · Expected May 2028 · GPA 3.66 · US citizen, no sponsorship.

**Do not submit from this agent.** Paste pack only.

Apply: https://job-boards.greenhouse.io/eulerity/jobs/4709040006
Resume: `applications/2027/eulerity/backend-intern/Vedant Desai Resume.pdf`
Required extra form (JD: applications without it are discarded): https://dev-matcher-pro.lovable.app/

---

## Knockout / structured fields (Greenhouse)

Exact Greenhouse labels. `*` = `required: true` on the API.

| Field (exact label) | Required | Answer |
| --- | --- | --- |
| First Name | * | Vedant |
| Last Name | * | Desai |
| Email | * | **verdent06@gmail.com** |
| Phone | | (248) 704-4852. UI shows a country-code widget next to Phone; API has no separate Country question. United States +1. |
| Resume/CV | * | `applications/2027/eulerity/backend-intern/Vedant Desai Resume.pdf` (pdf/doc/docx/txt/rtf) |
| LinkedIn Profile | * | https://linkedin.com/in/vedantde06 |
| Are you legally authorized to work in the United States? | * | **Yes** |
| Do you now, or will you in the future, require sponsorship for employment visa status (e.g. H-1B visa status, etc.) to work legally for our company in the United States? | * | **No** |
| Do you have any experience testing or using testing libraries, such as JUnit? | * | **Yes** is defensible only as *testing libraries in general* (SignalWeaver GitHub Actions runs **pytest**). Do **not** claim JUnit. If they will probe JUnit/Spring tests, select **No**. |
| Please provide any links to your Github or Portfolio | | https://github.com/Verdent06 |
| What are you looking for in an internship at Eulerity? | * | Paste the short answer below. |
| Are you currently based in the NYC tri-state area? | * | **No** (Ann Arbor, MI). Do not invent Yes. |
| Are you able to come to the NYC office at least once per week? | * | **No** unless you will actually be in NYC weekly May–August 2027. Do not select Yes from Ann Arbor without a real housing/travel plan. |
| How did you hear about this opportunity? | * | **Other** (job URL / Greenhouse). Live options (multi-select): Mailing List · Indeed · Handshake · LinkedIn · Other. Do not pick Handshake or LinkedIn unless that is how you found it. |

Phone country-code widget on the live page is not a Greenhouse `questions[]` field.

---

## "What are you looking for in an internship at Eulerity?" * (textarea)

I want to own backend services from design through deploy — APIs, workers, and the tests/CI that keep them honest — at a company whose product is an agentic marketing OS, not a tutorial CRUD intern. Closest analog I have: a production Flask REST API on AWS EC2 I shipped as the only engineer on a five-month Michigan Campaign Finance Network contract (Requests + Pandas ETL that replaced ~800 hours of manual PAC research across 400 committees), plus Vylet, a live Dockerized LangGraph + Redis/Celery pipeline with LangSmith eval gates (extraction faithfulness 50%→90%) and a name-collision defect fix that lifted lead-qualification from 79% to 89%. I integrate third-party APIs under failure (S3 presigned-URL retry on CaseStudyPrep). I do not have a year of Java/Spring. I interview in Python (Flask/FastAPI), and I use LLM/agent frameworks in product (LangGraph, LangSmith), not as a Copilot line-item. UMich CS + Economics, Junior, Expected May 2028, GPA 3.66; U.S. citizen, no sponsorship.

---

## Dev Matcher form (required by the JD; not Greenhouse)

Page title: **Backend Engineer Screening**. Subtitle: "Fill out the form below. After submission, you'll complete a timed quiz." Host: https://dev-matcher-pro.lovable.app/

Identity / logistics only — do not invent Java years, Spring frameworks, Copilot, or NYC.

| Field (exact label) | Required | Answer |
| --- | --- | --- |
| Full Name | * | Vedant Desai |
| Email Address | * | **verdent06@gmail.com** |
| LinkedIn Profile URL | * | https://linkedin.com/in/vedantde06 |
| GitHub Profile URL | * | https://github.com/Verdent06 |
| Resume | * | Paste PDF text, or the `.tex`/PDF from this folder. |
| Years of backend development | * | Count only live-pool backend (MDC Flask/EC2, Vylet LangGraph/Celery, SignalWeaver FastAPI). Do not inflate. Do not count Java. |
| Years of Java development | * | **0**. MatchStream is commented out of `context.md` and is not claimable. |
| Java frameworks / libraries used | * | Leave checkboxes empty. Do not check Spring / Hibernate / JUnit. Use Other only if you must type **none**. |
| Describe a backend service or system you designed and built. Key technical decisions and why? | * | MDC Flask REST on EC2 and/or Vylet Docker/Redis/Celery — see `grade.md` Interview angles. No Java rewrite. |
| AI coding tools you've used | * | Cursor and Claude are JD examples; Copilot is a company benefit, **not** inventory — do not check GitHub Copilot. Check only tools you have actually used. |
| Describe a specific example where you used an AI agent or LLM tool to build, debug, or ship something. | * | Vylet LangGraph + LangSmith eval / Pydantic consensus gates. Do not invent Copilot stories. |
| Familiarity with AI agent frameworks (LangChain, LlamaIndex, Claude Agents API, OpenAI Assistants) | * | **Intermediate — built prototypes** is the honest ceiling unless you will defend production agents at Eulerity's bar; Vylet is a shipped LangGraph product with paying clients. Do not pick Expert. |
| Experience integrating third-party APIs — API, challenge, and solution | * | CaseStudyPrep S3 presigned-URL retry; Vylet website crawl / state registry; Google Maps API on Lyndbrook if you include that story. |
| How do you approach testing? Walk us through how you tested something you built. | * | SignalWeaver pytest in GitHub Actions; Vylet LangSmith eval suite (20 adversarial cases). Not JUnit. |
| Most challenging bug you've debugged — root cause and fix | * | Vylet name-collision ownership-verification defect (79%→89%). |
| Cloud platforms / services you've worked with | | **AWS** (EC2, S3). Optional field. |
| How do you approach code reviews — both reviewing others and being reviewed? | * | Honest process answer; do not invent a Java team. |
| Are you currently based in the NYC tri-state area (NY, NJ, or CT)? | * | **No** |
| Available to work part-time (20 hrs/week), including $1 in-office day/week in NYC? | | Optional. **Yes** only if the 20 hrs and the NYC day are both true. |

Submit button: **Submit & start quiz**. Timed quiz is behind submit — not captured.

---

## Notes for the applicant (not for submission)

- **Java is a real knockout.** `grade.md` 5.0/10, 1 major: zero Java. Do not check Spring/JUnit/Copilot to paper over it.
- **NYC tri-state is a hard JD gate.** Pipeline eligibility is ineligible from Ann Arbor. Applying with No on both location questions is honest; Yes is a fabrication unless you will be there.
- **$17–$19/hr**, May–August, ≥20 hrs/week, hybrid ≥1 day/week (`companies.md` D-tier).
- Cover letter is not a Greenhouse field on this req.
