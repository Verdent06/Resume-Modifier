# Notion — Software Engineer Intern (Winter 2027) · Written Application Answers

Draft answers for Ashby `e66c6658-9e65-4c58-8db2-844628b6e8f8`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented internships, Notion product usage, Node.js, CRDT/block-editor work, or metrics. Trim to each form’s length limit before submitting.

**Do not submit from this run.** Artifacts only.

Apply: https://jobs.ashbyhq.com/notion/e66c6658-9e65-4c58-8db2-844628b6e8f8/application
Resume: `applications/2027/notion/software-engineer-intern-winter/Vedant Desai Resume.pdf`

This req is **Winter 2027 (January 25 – April 16)** only — distinct from Summer 2027 (already Applied). Form captured live from Ashby GraphQL on 2026-08-22 (not submitted).

**Class-year knockout:** JD and `persona.md` require graduation **before December 2027**. Education on the resume and this form is **May 2028**. Enter the real date. Do not backdate.

Location is not a skip: SF or NY hybrid, Anchor Days Mon/Tue/Thu, relocate required.

---

## Knockout / structured fields (fill exactly)

Questions and dropdowns captured from the live Ashby form (three sections).

| Field (exact form wording) | Required | Answer |
| --- | --- | --- |
| Full Name | Yes | Vedant Desai |
| Email | Yes | vedantde@umich.edu |
| Phone | Yes | (248) 704-4852 |
| Resume | Yes | `applications/2027/notion/software-engineer-intern-winter/Vedant Desai Resume.pdf` |
| LinkedIn Profile | Yes | https://linkedin.com/in/vedantde06 |
| Current Location | Yes | Northville, MI (mailing city on other 2027 apps; school city on the resume is Ann Arbor, MI). Form is city-level — do not invent a zip if the widget only wants city. |
| What pronouns would you like our team to use when addressing you? | Yes | **Prefer not to say** — UNKNOWN in `context.md`; do not invent |
| We work from our offices on Mondays, Tuesdays, and Thursdays (Anchor Days)… Are you able to commit to working from one of our offices on Anchor Days each week? | Yes | **Yes** |
| This role requires that you are willing to relocate to one of the following locations New York, NY, USA or San Francisco, CA, USA. Please confirm that you are willing to relocate for this role? | Yes | **Yes** |
| Please indicate all of the locations that you would be interested in relocating to for this position. | Yes | **New York, NY** and **San Francisco, CA** (both) |
| Are you authorized to work lawfully in the United States? | Yes | **Yes** — US citizen (recorded on other 2027 applications) |
| For this specific internship, will you require any of the below sponsorship for employment? | Yes | **None** (options: J1 / F1 / None / Other) |
| Will you now or at any time in the future require sponsorship for employment visa status (e.g. H1B, OPT)? | Yes | **None** (options: OPT / H1B / TN / None / Other) |
| How did you hear about this opportunity? (select all that apply) | No | **LinkedIn.** Options: LinkedIn / Glassdoor / Notion Blog / Notion Employee / Notion Website / Billboard/Outdoor Ads / Conference or Meetup. No Notion employee in `network.md`. Do not pick Notion Employee. |
| How many prior internships have you had? | Yes | **1** (options: 0 / 1 / 2 / 3+) |
| What type of engineering role are you interested in? | Yes | **Product** (options: Product / Growth / Infra / Security / Data / AI / Android / iOS) |
| What are some AI specific technologies you are comfortable with? | Yes | See long-text below |
| Why do you want to work at Notion? | Yes | See long-text below |
| Github Link | Yes | https://github.com/Verdent06 |
| School | Yes | University of Michigan |
| Graduation Date | Yes | **May 2028** — do not enter 2027 to clear the JD window |
| Degree Type | Yes | **Undergraduate/Bachelors** — B.S. Computer Science and Economics (options: Undergraduate/Bachelors / Master's / PhD / MBA) |

EEO / veteran self-ID: not on this Ashby form dump. If a post-submit survey appears, decline to self-identify if you do not want to answer. Do not invent.

Mailing address used on other apps (if a later field asks): 49032 Freestone Dr, Northville, MI.

---

## 1) Why do you want to work at Notion?

I want to spend Winter 2027 (January 25 – April 16) writing, testing, and debugging full-stack product software on a collaborative workspace — web services, databases, and UI — where AI is a product feature, not a side chatbot. That is the work this posting describes, and it is the work I already ship.

I founded Vylet, a live lead-sourcing product ($1,500 MRR, three paying clients): a Dockerized LangGraph pipeline that turns a ~30-minute manual process into 30 scored leads in 30 minutes, with a LangSmith eval harness and Pydantic consensus gates that lifted extraction faithfulness from 50% to 90%, plus a name-collision debug that lifted qualification from 79% to 89%. I built SignalWeaver end-to-end — FastAPI, a React/TypeScript dashboard, and pgvector semantic search over 768-d embeddings (49ms p50). At CaseStudyPrep.AI I cut cloud inference cost 40% by running Silero VAD client-side via ONNX and fixed a 27% audio-upload failure rate. At Michigan Data Consulting I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract.

I have not interned at Notion and I do not have block-editor, CRDT, or Node.js production experience — the JD is TypeScript, Node.js, *or* Python; I have TypeScript and Python in production-shaped work. I will relocate to San Francisco or New York and work Anchor Days (Mon/Tue/Thu) in office. I return to Michigan afterward (B.S. Computer Science and Economics, Expected May 2028). I am a US citizen and do not need sponsorship.

---

## 2) What are some AI specific technologies you are comfortable with?

LangGraph (Vylet pipeline; SignalWeaver 5-node graph in the pool), LangSmith eval harness, embeddings (Gemini embeddings in Vylet’s asyncpg DAL; 768-d MPNet embeddings + pgvector cosine search in SignalWeaver), ONNX Runtime + Silero VAD (client-side on-device inference at CaseStudyPrep.AI), Whisper (cloud inference that VAD was filtering for). Skills inventory also includes RAG, Agentic Workflows, and LLM-as-a-Judge; LoRA fine-tuning of Llama 3.1-8B is real SignalWeaver pool work but is **not** on the shipped resume (`persona.md`: do not lead with research-only LoRA). Do not list Copilot, Notion AI internals, or Node.js LLM SDKs.

---

## 3) How many prior internships have you had?

**1.**

Counted: CaseStudyPrep.AI — Software Engineer Co-op (Voice AI), Dec 2025–May 2026.

Not counted (titled consulting / founder, not internships): Michigan Data Consulting (Data Engineer), Lyndbrook Capital (Data Engineering Consultant), Vylet (Founder). Do not mark 2 or 3+ to look stronger. The JD’s “previous internship experience” is met by the co-op.

---

## 4) What type of engineering role are you interested in?

**Product.**

`persona.md`: this req is product-SWE with AI features, not an `ai-ml` research rotation. Real experience is shipping product (Vylet, CaseStudyPrep.AI, SignalWeaver React UI, MDC public research API). Do not pick AI as the primary — that mis-routes vs. the full-stack intern JD. Do not pick Infra / Security / Android / iOS (no supporting entries). Data is real (MDC, Lyndbrook) but is not the role this posting is hiring. Multi-select: Product only.

---

## 5) How did you hear about this opportunity?

**LinkedIn.**

Optional. Ashby options are LinkedIn / Glassdoor / Notion Blog / Notion Employee / Notion Website / Billboard/Outdoor Ads / Conference or Meetup. No Notion employee in `network.md`. LinkedIn is the honest selectable answer.

---

## Notes for the applicant (not for submission)

- **Lead with Vylet + CaseStudyPrep + SignalWeaver.** Screen is full-stack product-SWE with LLM/embeddings as built features (`persona.md`).
- **Do not claim Node.js, CRDTs, or Notion editor internals.** Defend TypeScript + Python as the JD’s or.
- **Internship count is 1.** Co-op only.
- **Role interest is Product**, not AI.
- **Graduation Date is May 2028.** The JD’s “before December 2027” window is a binary intern knockout (`recruiting.md` §8). `grade.md` resume-screen likelihood is Low for that reason. A referral cannot override class year. Confirm whether the cutoff is a form/copy error before spending recruiter cycles.
- **Referral:** none in `network.md`. A UMich alum on Notion eng still beats cold Ashby — it does not rewrite May 2028.
- **Loop:** Ashby screen → CodeSignal (primary) / reported CoderPad text-editor practical → recruiter → tech rounds. Binding filter after a clean class-year is the OA/practical (`grade.md` / `companies.md`).
- Winter form does **not** ask the Summer pair “Do you have experience with LLMs?” / “Have you built a personal project using LLMs?” Do not invent those fields.
