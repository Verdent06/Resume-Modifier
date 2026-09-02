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
| Years of backend development | * | **1** — paste block below. Python backend only (MDC Jan 2026–May 2026 + Vylet May 2026–present). Not Java. |
| Years of Java development | * | **0**. MatchStream is commented out of `context.md` and is not claimable. |
| Java frameworks / libraries used | * | Leave checkboxes empty. Do not check Spring / Hibernate / JUnit. Use Other only if you must type **none**. |
| Describe a backend service or system you designed and built. Key technical decisions and why? | * | Paste block below. MDC Flask REST on EC2 only. |
| AI coding tools you've used | * | Paste block below. No named checkboxes. Other: LangGraph, LangSmith, Gemini, Claude, OpenAI. |
| Describe a specific example where you used an AI agent or LLM tool to build, debug, or ship something. | * | Paste block below. Vylet LangGraph + LangSmith. |
| Familiarity with AI agent frameworks (LangChain, LlamaIndex, Claude Agents API, OpenAI Assistants) | * | **Intermediate — built prototypes** — paste block below. Do not pick Advanced or Expert. |
| Experience integrating third-party APIs — API, challenge, and solution | * | Paste block below. CaseStudyPrep S3 + Lyndbrook Google Maps + Vylet crawl/registry. |
| How do you approach testing? Walk us through how you tested something you built. | * | Paste block below. pytest + LangSmith evals. |
| Most challenging bug you've debugged — root cause and fix | * | Paste block below. Vylet name-collision 79%→89%. |
| Cloud platforms / services you've worked with | | **AWS** (EC2, S3). Optional field. |
| How do you approach code reviews — both reviewing others and being reviewed? | * | Paste block below. Sole-engineer + CI + eval gates. Do not invent a teammate PR culture. |
| Are you currently based in the NYC tri-state area (NY, NJ, or CT)? | * | **No** |
| Available to work part-time (20 hrs/week), including $1 in-office day/week in NYC? | | Optional. **Yes** only if the 20 hrs and the NYC day are both true. |

Submit button: **Submit & start quiz**. Timed quiz is behind submit — not captured.

---

## Notes for the applicant (not for submission)

- **Java is a real knockout.** `grade.md` 5.0/10, 1 major: zero Java. Do not check Spring/JUnit/Copilot to paper over it.
- **NYC tri-state is a hard JD gate.** Pipeline eligibility is ineligible from Ann Arbor. Applying with No on both location questions is honest; Yes is a fabrication unless you will be there.
- **$17–$19/hr**, May–August, ≥20 hrs/week, hybrid ≥1 day/week (`companies.md` D-tier).
- Cover letter is not a Greenhouse field on this req.

---

## PASTE-READY — Dev Matcher essays

Grounded in `persona.md`, `context.md`, and `grade.md` only. Email on this form: **verdent06@gmail.com**. Apply worker: paste the block under each label exactly. Do not add Java, Spring, JUnit, Copilot, Snowflake, Databricks, Fusion, Tableau, Sentry, an NYC address, or MatchStream.

### 1. Years of backend development

```
1
```

### 2. Describe a backend service or system you designed and built. Key technical decisions and why?

```
I designed and shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month Michigan Campaign Finance Network contract. Researchers were doing portal searches the Bureau of Elections capped, irregular Excel exports, and about two hours of hand normalization per committee. I replaced that with a Requests and Pandas ETL that ingest filings directly, then a deterministic aggregation engine that parses those exports, normalizes contribution amounts, and ranks PACs by total funding volume. The API wired ingested data and those rankings into MCFN's public-facing research workflow. I chose Flask and EC2 because I owned ingestion through deploy with no backend team sharing infrastructure or API design, and I scoped that delivery directly with MCFN stakeholders. This is Python services work I can walk through. I would measure PAC-rank freshness and endpoint latency next; the aggregation step itself has no separate impact number beside the ETL's roughly 800 hours saved across 400 tracked PACs.
```

### 3. AI coding tools you've used

Checkboxes: leave **all** named boxes unchecked (GitHub Copilot, Claude Code, Windsurf, Continue.dev, Cursor, ChatGPT / Codex, Lovable, Aider).

Other (comma-separated), paste:

```
LangGraph, LangSmith, Gemini, Claude, OpenAI
```

### 4. Describe a specific example where you used an AI agent or LLM tool to build, debug, or ship something.

```
I used LangGraph and LangSmith to ship Vylet, a live lead-sourcing product on a recurring Dockerized pipeline with Redis and Celery workers. The pipeline turns a roughly 30-minute manual process per business into 30 scored leads in 30 minutes. LLM extraction was unfaithful, so I built a LangSmith eval spanning 20 adversarial business test cases across 13 archetype labels — manufacturers, SaaS tools, PE holding companies, geographic mismatches — then layered deterministic Pydantic consensus gates, lifting extraction faithfulness from 50% to 90%. I also built Node 3 as a pure-Python triangulated consensus gate with no LLM calls: it fuzzy-matches the query, state business registry, and live website crawl in a weakest-link check, then hard-fails on legal status, industry, geography, or independence before the score threshold. Embeddings are Gemini, stored through an asyncpg data layer next to source records. That is agent-framework work in a product with paying clients, not a notebook prompt.
```

### 5. Familiarity with AI agent frameworks (LangChain, LlamaIndex, Claude Agents API, OpenAI Assistants)

```
Intermediate — built prototypes
```

### 6. Experience integrating third-party APIs — API, challenge, and solution

```
On CaseStudyPrep, audio uploads to S3 were failing 27% of the time because presigned URLs expired mid-flight and Angular silently rejected WAV MIME types. I wrote fault-tolerant RxJS logic that detects an expired URL, regenerates it, and renegotiates MIME types so the upload can finish instead of dropping the file. That is a third-party storage API under real failure, not a happy-path tutorial call. At Lyndbrook I crossed EPA ECHO and MassGIS records with the Google Maps API to surface unlisted water-utility acquisition targets, cutting about 15 hours of manual prospecting per week for the fund's Principal and delivering 800-plus validated Day-1 targets. On Vylet, Node 3 live-crawls the business website and checks the state registry as two of three consensus inputs before a lead can score. I debug APIs from the failure mode first: expiry, mismatch, and stale data, then the retry or refresh path.
```

### 7. How do you approach testing? Walk us through how you tested something you built.

```
I test at two layers: deterministic checks in CI, and evals when an LLM is in the path. For SignalWeaver I containerized FastAPI, Postgres with pgvector, and the frontend, then ran a GitHub Actions pipeline on main that builds the frontend, runs pytest, and builds the API image. pytest is the merge gate I actually rerun. For Vylet I built a LangSmith eval pipeline spanning 20 adversarial business test cases across 13 archetype labels, then added Pydantic consensus gates so a bad extraction cannot ship as a qualified lead. Faithfulness moved from 50% to 90% on that suite. Node 3 is a non-LLM check I can unit-test: fuzzy-match three sources and hard-fail on legal status, industry, geography, or independence. I would rather fail a lead in eval than invent a passing test I cannot rerun.
```

### 8. Most challenging bug you've debugged — root cause and fix

```
On Vylet, ownership-verification was incorrectly rejecting valid acquisition targets that shared a name with an unrelated business somewhere else. The root cause was a name-collision: the checker treated a string match as proof the entity was the wrong company, so good leads died even when legal status, geography, and the live site were fine. I diagnosed that defect in the verification logic, then fixed the match so a shared name is not enough to hard-fail. Qualification rose from 79% to 89% with zero change to sourcing volume, which told me the pipeline was not starved for leads — it was throwing away true positives. The bug lived in a Dockerized LangGraph pipeline with Redis and Celery workers. I keep the before and after because a bug without a rate is a story I cannot defend, and I can walk through the three-way consensus path that now sits in front of the score threshold.
```

### 9. How do you approach code reviews — both reviewing others and being reviewed?

```
I have mostly been the only engineer on the backend I ship, so I will not invent a pull-request culture I did not have. On the Michigan Campaign Finance Network contract I scoped ingestion through REST endpoints on EC2 directly with MCFN stakeholders; there was no backend team to share API design or deployment ownership, which meant their review was product and correctness, not a queue of teammates. I still want a mechanical second reader: SignalWeaver's GitHub Actions run pytest and an API image build on main, so a change that breaks tests does not quietly land. On Vylet I review agent output the same way I would review a teammate: LangSmith evals and Pydantic consensus gates, plus Node 3's non-LLM weakest-link check, before a lead is allowed to score. When someone reviews me, I want the defect named with a reproduce path — expired URL, name collision, failed eval case — not a vibe.
```

