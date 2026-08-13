# Sentry — Software Engineer, Intern (Summer 2027) · Screening / Cover-Letter Answers

Draft answers to Sentry's likely application prompts (Ashby), grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented experience or metrics. The Sentry Ashby form may only expose a subset of these fields (often a single "anything else / why Sentry" box); trim to each form's length limit before submitting, and lead with the "Why Sentry" paragraph if only one box is offered.

---

## "Why do you want to work at Sentry?"

Because Sentry is the rare place where the JD's promise — write real code that ships to production, own a project end-to-end, contribute to open source every day — is the actual job, not a recruiting line. Almost everything I've built, I've shipped and owned end-to-end: I delivered a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract, and I founded Vylet, a lead-sourcing product that's live and generating $1,500 MRR across three paying clients. I also care about how software actually works under the hood — I built a granular synthesizer in C++/JUCE from scratch specifically to understand real-time constraints and memory ordering rather than read about them. Sentry sits at the exact intersection I want to build in: a Python/Django + React/TypeScript codebase that millions of developers depend on, open source at its core, and leaning into the AI-native future of development — which is the same direction my own work (agentic LangGraph pipelines, LLM eval) has been heading.

---

## "Tell us about something you've built and shipped."

**SignalWeaver** — a multi-signal financial research platform I built end-to-end, which maps closely to how this role is framed (spec → build → test → ship, full ownership across the stack):

- **Backend:** async REST endpoints in FastAPI wrapping fundamentals, sentiment, and a regression model, instrumented end-to-end at 9.1s p50 / 15.2s p99 across 90 runs.
- **Retrieval:** semantic search over stored news with `pgvector` cosine similarity on 768-d embeddings, benchmarked at 49ms p50 / 99ms p99.
- **ML:** lifted financial-sentiment accuracy from 81% to 96% by LoRA fine-tuning a quantized Llama-3.1-8B model on 3,454 labeled entries, evaluated on a held-out set.
- **Frontend + delivery:** a React/TypeScript dashboard, containerized with Docker Compose (API + Postgres/pgvector + nginx), and a GitHub Actions CI pipeline (frontend build, pytest, image build on main).

The reason I like it as a work sample is that I can defend every layer's trade-off — why FastAPI, why Postgres, what each CI stage guards — which is exactly the "no HackerRank, narrate your decisions" bar this role screens for. Code: github.com/Verdent06/SignalWeaver.

---

## "How do you use AI tooling in your workflow?"

I build with it and I build on it. Vylet is a Dockerized LangGraph agentic pipeline (Redis/Celery workers) that turns a ~30-minute manual research task per business into ~30 scored leads in 30 minutes — a 30x speedup — and I treat the LLM parts like any other unreliable dependency: I engineered a LangSmith eval pipeline over 20 adversarial test cases across 13 archetype labels and layered deterministic Pydantic consensus gates to lift extraction faithfulness from 50% to 90%. I also diagnosed a name-collision defect in the ownership-verification logic that lifted lead-qualification precision from 79% to 89%. Day-to-day I use AI coding tools as part of the workflow, but the discipline I care about is the same one Sentry cares about: measure whether the output is actually correct before you trust it.

---

## "Availability / relocation"

Yes — I'm available to start May 2027 and can relocate to San Francisco for the internship (I appreciate that housing/relocation is covered). I'm a Computer Science + Economics student at the University of Michigan (expected May 2028), returning to school after the internship, and I'm authorized to work in the US without visa sponsorship.

---

## Notes for the applicant (not for submission)

- **Lead with production ownership and open source.** The two things Sentry's JD rewards are (1) code you shipped to real users end-to-end and (2) a real public GitHub. Open every conversation with SignalWeaver (full-stack, CI, clickable) and the MDC production API / Vylet live product — not the C++ synth, which is craft signal, not dev-tooling signal.
- **Close the open-source gap for real.** Your GitHub is all personal repos. Before or right after applying, open one genuine PR into a Sentry public repo (getsentry/sentry or an SDK) — even a small, well-scoped one. It converts "has a GitHub" into "already works the way we work" and directly answers the one fit gap on the resume.
- **React vs Angular:** your shipped titled-role frontend is Angular/RxJS; your React is in SignalWeaver (a project). Don't overclaim React production depth — say plainly that your React is project-scale and that you pick up frameworks fast (the C++/JUCE from-scratch build is your proof you can learn a new stack and ship).
- **Referral > cold apply**, and apply within ~72 hours of the req opening — the intern cycle is early and the first wave gets the open headcount.
