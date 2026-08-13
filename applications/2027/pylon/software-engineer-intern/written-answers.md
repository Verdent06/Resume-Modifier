# Pylon — Software Engineer, Intern (Summer 2027) · Screening / Cover-Letter Answers

Draft answers to Pylon's likely Ashby application prompts, grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented experience, metrics, or stack (no Go/GraphQL). The Ashby form may only expose a subset of these fields (often a single "anything else / why Pylon" box); trim to each form's length limit before submitting, and lead with the "Why Pylon" paragraph if only one box is offered.

Apply: https://jobs.ashbyhq.com/pylon-labs/fcea8b52-81f1-4b0c-b575-d7b180faec4d/application

---

## "Why do you want to work at Pylon?"

Because Pylon is building the product I already spend my time on: AI that does real customer-facing work, owned end-to-end, shipped to paying users — not a research demo bolted onto a ticket queue. I founded Vylet, a live lead-sourcing product generating $1,500 MRR across three paying clients, as a Dockerized LangGraph pipeline with Redis/Celery workers; I treat the LLM like any other unreliable dependency (LangSmith eval over 20 adversarial cases, Pydantic consensus gates, 50%→90% extraction faithfulness). That's the same "humans and agents collaborate on customer work" shape Pylon is hiring interns to build for post-sales teams. I also want the environment the JD actually describes — high autonomy, prototype-and-ship, non-waterfall with PMs and designers — which matches how I've already worked: sole engineer on a five-month production Flask API on AWS EC2 for a real nonprofit, and a voice-AI co-op where I cut cloud inference cost 40% and killed a 27% upload-failure rate without a large team around me. I'm a CS + Econ student at Michigan (expected May 2028), and I'm ready to be in San Francisco for Summer 2027.

---

## "Tell us about something you've built and shipped."

**Vylet** (live, vyletdata.com) — the closest analog to "own a product feature end-to-end under ambiguity":

- Turned a ~30-minute manual research task per business into a Dockerized LangGraph pipeline that generates 30 scored leads in 30 minutes (30x), with Redis/Celery workers on a recurring cycle.
- Built a LangSmith eval suite (20 adversarial cases, 13 archetype labels) and layered deterministic Pydantic consensus gates to lift extraction faithfulness from 50% to 90%.
- Diagnosed a name-collision defect in ownership-verification logic that was rejecting valid targets; the fix lifted lead-qualification from 79% to 89% with no change in sourcing volume.
- Three paying subscription clients within six weeks of launch; $1,500 MRR.

**SignalWeaver** (github.com/Verdent06/SignalWeaver) — the full-stack work sample:

- React/TypeScript dashboard over composite scores persisted in Postgres.
- Async FastAPI REST wrapping fundamentals, sentiment, and regression logic (9.1s p50 / 15.2s p99 across 90 runs).
- Docker Compose (API + Postgres/pgvector + nginx) and GitHub Actions CI (frontend build, pytest, image build on main).

I can defend every layer's trade-off. I will not claim Go or GraphQL — those are not in my shipped work. React in production-titled work is Angular/RxJS at the co-op; React is project-scale on SignalWeaver.

---

## "How do you use AI for software development?" / "How do you leverage AI?"

I build *on* it and I don't trust it blindly. Vylet is an agentic LangGraph pipeline in production for paying clients; the LLM is wrapped in eval (LangSmith) and deterministic gates (Pydantic consensus, a non-LLM triangulation check) so a bad extraction fails closed instead of shipping a bad lead. Day-to-day I use AI coding tools as part of the loop, but the habit I would bring to Pylon is the one the JD is actually buying: juggle the model as one workstream among several, measure whether the output is correct, and still own the product end-to-end.

---

## "A time you owned something end-to-end / worked in ambiguity"

Michigan Data Consulting: I was the only engineer on a five-month contract with the Michigan Campaign Finance Network. I scoped delivery with the stakeholder, built a Requests + Pandas ETL that replaced ~800 hours of manual pulls across 400 PACs, and shipped a production Flask REST API on AWS EC2 with no backend team to share API design or deployment. That's the "high autonomy, project-manage your own work" bar in the JD — not a class team with a staff engineer behind me.

---

## "Are you in SF or willing to relocate?" / Availability

Yes — I can relocate to San Francisco for the Summer 2027 internship. I'm a Computer Science and Economics student at the University of Michigan (expected May 2028), available to start with the intern class, and authorized to work in the US without visa sponsorship.

---

## Notes for the applicant (not for submission)

- **Lead with Vylet + CaseStudyPrep, then SignalWeaver as the React/full-stack sample.** Pylon is hiring product-feature builders who leverage AI, not a Go expert. Do not open with MDC ETL or any C++ story.
- **Do not claim Go or GraphQL.** They are explicit bonuses. If asked, say you haven't shipped them and that you've picked up new stacks to ship (Angular/RxJS in the co-op; FastAPI + React on SignalWeaver).
- **React honesty:** titled-role frontend is Angular; React is SignalWeaver. Overclaiming React production depth is the fastest way to fail the practical screen.
- **Referral > cold Ashby.** Network to an engineer or the hiring manager. Apply immediately — intern reqs fill in the first wave.
