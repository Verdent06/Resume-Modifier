# Notion — Software Engineer Intern (Summer 2027) · Written Application Answers

Draft answers for Ashby `3fba1c39-c5cb-47d7-9ad2-1cec4d7e9d0c`. Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented internships, Notion product usage, Node.js, CRDT/block-editor work, or metrics. Trim to each form’s length limit before submitting.

Apply: https://jobs.ashbyhq.com/notion/3fba1c39-c5cb-47d7-9ad2-1cec4d7e9d0c/application
Jobright: https://jobright.ai/jobs/info/6a7f67b119ce4e6e9d9379a1
Resume: `applications/2027/notion/software-engineer-intern/Vedant Desai Resume.pdf`

Location is not a skip: SF or NY hybrid, Anchor Days Mon/Tue/Thu, relocate required.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| Full Name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| Resume/CV | `applications/2027/notion/software-engineer-intern/Vedant Desai Resume.pdf` |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Github Link | https://github.com/Verdent06 |
| Current Location | 49032 Freestone Dr, Northville, MI (from other 2027 applications; not in `context.md`) |
| Pronouns | UNKNOWN (not in `context.md`; use Prefer not to say, or leave blank) |
| Anchor Days Mon/Tue/Thu in office | **Yes** |
| Willing to relocate to NY or SF | **Yes** |
| Locations interested | **New York, NY** and **San Francisco, CA** (both) |
| Authorized to work lawfully in the United States? | **Yes** — US citizen (recorded on other 2027 applications) |
| Sponsorship for this internship (J1 / F1 / None / Other) | **None** |
| Future sponsorship (OPT / H1B / TN / None / Other) | **None** |
| School | University of Michigan |
| Graduation Date | **May 2028** |
| Degree Type | **Undergraduate/Bachelors** — B.S. Computer Science and Economics |
| GPA | 3.66 / 4.0 (not an Ashby field on this form; do not invent if asked elsewhere) |

EEO / veteran self-ID: voluntary. Do not invent. Decline to self-identify if you do not want to answer.

---

## 1) Why do you want to work at Notion?

I want to spend Summer 2027 writing, testing, and debugging full-stack product software on a collaborative workspace — web services, databases, and UI — where AI is a product feature, not a side chatbot. That is the work this posting describes, and it is the work I already ship.

I founded Vylet, a live lead-sourcing product ($1,500 MRR, three paying clients): a Dockerized LangGraph pipeline that turns a ~30-minute manual process into 30 scored leads in 30 minutes, with a LangSmith eval harness and Pydantic consensus gates that lifted extraction faithfulness from 50% to 90%, plus a name-collision debug that lifted qualification from 79% to 89%. I built SignalWeaver end-to-end — FastAPI, a React/TypeScript dashboard, and pgvector semantic search over 768-d embeddings (49ms p50). At CaseStudyPrep.AI I cut cloud inference cost 40% by running Silero VAD client-side via ONNX and fixed a 27% audio-upload failure rate. At Michigan Data Consulting I shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract.

I have not interned at Notion and I do not have block-editor, CRDT, or Node.js production experience — the JD is TypeScript, Node.js, *or* Python; I have TypeScript and Python in production-shaped work. I will relocate to San Francisco or New York and work Anchor Days (Mon/Tue/Thu) in office. I return to Michigan afterward (B.S. Computer Science and Economics, Expected May 2028). I am a US citizen and do not need sponsorship.

---

## 2) What are some AI specific technologies you are comfortable with?

LangGraph (Vylet pipeline; SignalWeaver 5-node graph in the pool), LangSmith eval harness, embeddings (Gemini embeddings in Vylet’s asyncpg DAL; 768-d MPNet embeddings + pgvector cosine search in SignalWeaver), ONNX Runtime + Silero VAD (client-side on-device inference at CaseStudyPrep.AI), Whisper (cloud inference that VAD was filtering for). Skills inventory also includes RAG, Agentic Workflows, and LLM-as-a-Judge; LoRA fine-tuning of Llama 3.1-8B is real SignalWeaver pool work but is **not** on the shipped resume (persona: do not lead with research-only LoRA). Do not list Copilot, Notion AI internals, or Node.js LLM SDKs.

---

## 3) Do you have experience with LLMs?

**Yes.**

Vylet is a LangGraph + LangSmith product (LLM extraction with eval gates and Gemini embeddings). SignalWeaver uses LLM-derived sentiment, a LangGraph pipeline, and (in the pool, not on the page) LoRA on Llama 3.1-8B. CaseStudyPrep.AI is voice-AI around Whisper, not an LLM-app in the chat sense — do not hang the Yes solely on Whisper.

---

## 4) Have you built a personal project using LLMs?

**Yes.**

SignalWeaver is a personal project (FastAPI + React/TypeScript + pgvector embeddings + LangGraph). Vylet is a founded live product using LangGraph/LangSmith, not a class assignment. Either supports Yes. Do not mark Yes from Copilot use.

---

## 5) What type of engineering role are you interested in?

**Product.**

Persona: this req is product-SWE with AI features, not an `ai-ml` research rotation. Real experience is shipping product (Vylet, CaseStudyPrep.AI, SignalWeaver React UI, MDC public research API). Do not pick AI as the primary — that mis-routes vs. the full-stack intern JD. Do not pick Infra / Security / Android / iOS (no supporting entries). Data is real (MDC, Lyndbrook) but is not the role this posting is hiring.

---

## 6) How many prior internships have you had?

**1.**

Counted: CaseStudyPrep.AI — Software Engineer Co-op (Voice AI), Dec 2025–May 2026.

Not counted (titled consulting / founder, not internships): Michigan Data Consulting (Data Engineer), Lyndbrook Capital (Data Engineering Consultant), Vylet (Founder). Do not mark 2 or 3+ to look stronger. The JD’s “previous internship experience” is met by the co-op.

---

## 7) How did you hear about this opportunity?

**LinkedIn.**

Ashby options are LinkedIn / Glassdoor / Notion Blog / Notion Employee / Notion Website / Billboard / Conference. Jobright sourced this listing but is not on the form. No Notion employee in `network.md`. LinkedIn is the honest selectable answer.

---

## Notes for the applicant (not for submission)

- **Lead with Vylet + CaseStudyPrep + SignalWeaver.** Screen is full-stack product-SWE with LLM/embeddings as built features (`persona.md`).
- **Do not claim Node.js, CRDTs, or Notion editor internals.** Defend TypeScript + Python as the JD’s or.
- **Internship count is 1.** Co-op only.
- **Role interest is Product**, not AI.
- **Referral:** none in `network.md`. A UMich alum on Notion eng still beats cold Ashby.
- **Loop:** Ashby screen → CodeSignal (primary) / reported CoderPad text-editor practical → recruiter → tech rounds. Binding filter is the OA/practical, not this PDF (`grade.md` / `companies.md`).
