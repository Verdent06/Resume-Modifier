# Transcard Payments — 2027 Artificial Intelligence Intern (Paylocity 4476416) · Written Application Answers

Draft answers for Paylocity req **4476416**. Grounded in `persona.md` (applied product AI intern — Python + ML/NLP/LLM features, not ML research, not the sibling SWE intern) and `context.md`. First-person, honest, defensible under "walk me through this." **Do not invent Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, C#, Blazor, SQL Server, Azure, GitHub Copilot, AP/AR, ACH, SMART Suite internals, or Virtual CFO domain work.** Trim to the form's length limit before submitting.

Apply (do not submit from this agent): https://recruiting.paylocity.com/Recruiting/Jobs/Details/4476416

**This agent did not submit.** Paylocity's Apply URL returned an "outdated browser" gate from this environment, so **exact field labels were not captured**. Fill from the kit below; if a knockout is worded differently, answer the *intent* honestly. Official portal only — JD forbids contacting hiring managers.

**Form-kit identity (use on Paylocity — never `vedantde@umich.edu`):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · US citizen, no sponsorship · GPA **3.66** · Expected **May 2028** · Address **49032 Freestone Dr, Northville, MI 48168** · LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06 · SAT **1510** if asked · DOB **12/16/2006** if asked.

The resume PDF header still uses the school email from `context.md`. That is the document. The **form** uses verdent06@gmail.com.

Resume upload: `applications/2027/transcard/artificial-intelligence-intern/Vedant Desai Resume.pdf`

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | **verdent06@gmail.com** |
| Phone | (248) 704-4852 |
| Address | 49032 Freestone Dr, Northville, MI 48168 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/transcard/artificial-intelligence-intern/Vedant Desai Resume.pdf` |
| Cover letter | Optional on many Paylocity flows. Upload the letter below if there is an upload; skip if none. |
| Location / willing to work Chattanooga | **Yes.** Prefer onsite Chattanooga for Summer 2027. Remote is acceptable if they place that way (JD: remote for qualified US residents). |
| Currently pursuing Bachelor's in CS / related? | **Yes** — B.S. Computer Science and Economics, University of Michigan, Expected May 2028 |
| Graduation date | **May 2028** |
| Did you graduate? | **No** |
| GPA | **3.66 / 4.0** |
| Class standing at internship | **Rising senior** (Summer 2027; return Fall 2027; Expected May 2028) |
| Work authorization / sponsorship | **Yes, authorized to work in the U.S. without employer sponsorship.** US citizen. This posting: reside in the US; unable to offer visa sponsorship. |
| Will you now or in the future require sponsorship (incl. OPT/CPT)? | **No** |
| Must reside in the US | **Yes** — Northville, MI |
| How did you hear about this role? | **Company website** (transcard.com/careers / this Paylocity posting). **No Transcard contact in `network.md`.** Do not pick Employee Referral. |
| Desired salary / compensation | Paid intern, rate unpublished. If required: **$25–30 / hour** (C-tier intern band in `recruiting.md`; qualifications-based per JD). Prefer Hour not Year. Do not invent an annual FTE. |
| Are you 18+ | **Yes** |
| Previously employed by Transcard | **No** |
| Willing to work Mon–Fri business hours | **Yes** |
| Languages you can interview in | **Python, SQL, TypeScript, C++.** Do **not** check C#, Blazor, Azure, Copilot, Snowflake, Databricks, Tableau, Fusion, or Sentry. |

---

## "Why Transcard / why this internship?"

I want Summer 2027 building and testing AI features that a payments product actually ships — sprint/scrum, code review, reliability/safety — not a research notebook and not a generic SWE rotation. That is this Artificial Intelligence Intern seat (Paylocity 4476416).

What I can defend:

- **AI-powered application features.** I run Vylet, a live lead-sourcing product ($1,500 MRR, three paying clients). I shipped a Dockerized LangGraph pipeline (30 scored leads in 30 minutes, a 30x speedup) and a LangSmith eval harness over 20 adversarial cases that lifted extraction faithfulness from 50% to 90% with Pydantic consensus gates. Node 3 is a pure-Python triangulated consensus gate with no LLM calls — a weakest-link check that hard-fails leads on legal status, industry, geography, or independence before the score threshold applies. That is build + test + a safety analog, which is this intern's job.
- **Conversational / on-device AI (preferred chatbot).** At CaseStudyPrep.AI I ran Silero VAD client-side via ONNX Runtime so Whisper stopped scoring dead air, cutting cloud inference cost 40%, and I fixed a 27% S3 upload failure with RxJS URL regeneration. That is a voice-AI product, not a chatbot demo.
- **APIs + cloud (preferred).** SignalWeaver serves financial-research scores through FastAPI (9.1s p50 / 15.2s p99 on 90 tickers) and pgvector search (49ms p50). At Michigan Data Consulting I shipped a Flask REST API on AWS EC2 as the sole engineer on a 5-month MCFN contract. I have not interned on SMART Suite, Virtual CFO, AP/AR, or Azure. I would ramp on Transcard's product with the SVP of Technology rather than pretend I already have that domain.

I can be onsite in Chattanooga for Summer 2027 (or remote in the US if that is how you staff). I return to Michigan afterward (Expected May 2028). I do not need sponsorship.

---

## "Tell us about a project" / Python / ML / NLP / LLM

**Vylet** (vyletdata.com). LangGraph + Redis/Celery; LangSmith eval across 13 archetype labels; deterministic consensus gates. A name-collision bug in ownership verification was rejecting valid targets; the fix lifted lead-qualification from 79% to 89% with no change in sourcing volume. Closest analog to "troubleshoot AI-powered applications" and responsible-AI-adjacent gates.

**CaseStudyPrep.AI.** Voice-AI: Silero VAD / ONNX on-device, 40% inference-cost cut; S3 failure recovery. Preferred conversational-AI hit. Remote co-op — independence analog for the JD's remote clause.

**SignalWeaver** (github.com/Verdent06/SignalWeaver). LoRA fine-tune of Llama-3.1-8B on Financial PhraseBank: 81% → 96% sentiment accuracy on a held-out test set; FastAPI + pgvector. Research assistant, not investment advice — not an ML-research intern claim.

---

## "Describe experience with APIs, cloud, or chatbot/conversational AI" (preferred)

APIs: Flask REST on AWS EC2 (MDC); FastAPI REST (SignalWeaver). Cloud: AWS EC2/S3, Docker. Conversational/voice: CaseStudyPrep ONNX VAD + Whisper cost path. I have not shipped a text chatbot and I have not used Azure or Copilot.

---

## "Interest in responsible AI / data privacy / security / AI safety"

On Vylet, Node 3 is a no-LLM consensus gate that hard-fails leads before a score is trusted — structured checks instead of letting the model be the last word. LangSmith eval is a held-out adversarial set, not a vibe check. I have not configured production IAM for an AI product. I would treat Transcard's "review security and access-related configurations" as learning under the SVP of Technology, not as experience I already have.

---

## Availability

Summer 2027, full-time, **Chattanooga, TN onsite preferred**; remote in the US if that is the assignment. Available to start May 2027. Returning to the University of Michigan after the internship (Fall 2027 / Winter 2028). Class standing at the internship: **rising senior**.

---

## Cover letter (only if Paylocity shows an upload)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Transcard Payments — 2027 Artificial Intelligence Intern (Paylocity 4476416)
Chattanooga, TN (onsite preferred; remote if placed that way)

I am applying for the Summer 2027 Artificial Intelligence Intern seat. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am a U.S. citizen, I do not need sponsorship, and I can work onsite in Chattanooga for Summer 2027. I return to Michigan in Fall 2027.

I want this seat because the posting is applied product AI — features, sprint/scrum, testing, and translating business needs into AI-driven solutions — not a research-scientist intern and not the sibling SWE intern.

What I can defend:

- **Shipped AI features with eval.** Vylet: Dockerized LangGraph pipeline, LangSmith eval (50%→90% faithfulness), pure-Python consensus/hard-fail gates, and a production defect fix (79%→89%). Live product, $1,500 MRR.
- **Conversational / on-device AI.** CaseStudyPrep.AI: Silero VAD via ONNX Runtime, 40% cloud-inference cost cut; S3 upload recovery.
- **Python APIs and cloud.** SignalWeaver FastAPI + held-out LoRA NLP eval; MDC Flask REST on AWS EC2 for a real nonprofit stakeholder. I interview in Python. I have not used C#, Azure, Copilot, Snowflake, Databricks, or Tableau, and I have not interned on payment rails — I will not claim those.

Sincerely,
Vedant Desai

---

## Notes for the applicant (not for submission)

- **Do not submit from this agent.** Exact Paylocity labels were not visible (browser-compat gate). Watch for work-auth / sponsorship knockouts.
- **Form email is verdent06@gmail.com.** Never vedantde@umich.edu on Paylocity.
- **This is 4476416 AI intern, not the sibling SWE intern.** Separate packet.
- **Do not invent Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, C#, Blazor, SQL Server, Azure, GitHub Copilot, SMART Suite, Virtual CFO, AP/AR, or ACH.**
- **Chattanooga = Yes.** User can travel anywhere Summer 2027. Remote is a fallback the JD already offers.
- **No Transcard contact in `network.md`.** Do not pick referral. A Chattanooga / UMich alum still beats cold Paylocity (`recruiting.md`: HM > recruiter > engineer > cold apply) — but JD says do not contact hiring managers outside the portal.
- **Resume is the intern bottleneck** (`persona.md` / `companies.md` C-tier ~20–30%). No published OA.
- **MDC on the resume** is Python/API/cloud + stakeholder translation, not the AI proof. If a form asks for "AI project," lead with Vylet, then CaseStudyPrep, then SignalWeaver.
