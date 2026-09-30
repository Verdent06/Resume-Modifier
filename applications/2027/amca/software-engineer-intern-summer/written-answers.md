# EMAIL HARD RULE

**Application email is `verdent06@gmail.com` ONLY. Never `vedantde@umich.edu`.**
Override any Greenhouse / LinkedIn / browser autofill. The PDF header email is already `verdent06@gmail.com` — do not change it.

---

# Amca — Software Engineering Internship (Summer 2027) · Written Application Answers

Draft answers for Greenhouse job **4425120009** / req **110** / internal **4246500009**. Grounded in the **live Greenhouse questions API** (`boards-api.greenhouse.io/v1/boards/amca/jobs/4425120009?questions=true`) plus the job-board page, `persona.md` (full-stack spine + manufacturing-software / factory-tools / document-digitization), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Go, MES, PLM, CAD-as-SWE, RAPID internals, a factory/Protoshop internship, a clearance-in-hand, Granular xrun/latency/CPU numbers, MDC API traffic/latency.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Apply: https://job-boards.greenhouse.io/amca/jobs/4425120009
Resume: `applications/2027/amca/software-engineer-intern-summer/Vedant Desai Resume.pdf`
SHA-256: `22c5a13895ac74aa4cc9d493a9071af60d3adba3d9d1001a060aa989300d29a2`

**Pulled from the live Greenhouse questions API** on 2026-09-30. Labels below are exact. `*` = required. `demographic_questions` is null — no EEO block unless Greenhouse injects one after account login. `location_questions` is empty. **No Cover Letter field** on this posting.

**Form / PDF email MUST be `verdent06@gmail.com`.** Never `vedantde@umich.edu`. Autofill may still pull umich from a prior Greenhouse profile; overwrite.

This is **Summer 2027** only. **Not** the Electrical Engineering intern. **Not** Open Application, Engineering. **Not** FT Product SWE **4366398009**.

Airtable: `recPjaK0wQ1E9mQzA` (GrokBot Applications). Status stays **In Progress** until a human actually submits. Do not mark Applied in Airtable from this agent.

---

## Knockouts (read first)

1. Currently pursuing B.S./M.S. CS / computer or software engineering / math / physics / related — **clears** (UMich CS + Economics, Expected May 2028).
2. **ITAR U.S. person** — **U.S. Citizen.** (`context.md`). LPR / protected person also qualify; **Not Applicable** is auto-reject.
3. El Segundo **5 days/week onsite** — **Yes** if you actually mean it. This is a real knockout, not a vibe question. $30–$50/hr.
4. Returning to school after the term — Expected May 2028; Fall 2027 / Winter 2028 remain.
5. **"Using any AI will automatically disqualify your application"** on the "put into the world" question. **Type that answer yourself.** The draft below is a fact sheet, not something to paste blindly.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on citizenship or onsite.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact labels on the live Greenhouse apply form for job **4425120009**.

| Field | Required | Answer |
| --- | --- | --- |
| First Name | * | Vedant |
| Last Name | * | Desai |
| Preferred First Name | | Vedant |
| Email | * | **verdent06@gmail.com** (never `vedantde@umich.edu`). PDF header matches. Overwrite Autofill if it inserts umich. |
| Phone | * | (248) 704-4852 |
| Resume/CV | * | `applications/2027/amca/software-engineer-intern-summer/Vedant Desai Resume.pdf` — attach the PDF. |
| LinkedIn Profile | * | https://linkedin.com/in/vedantde06 |
| Portfolio | | https://github.com/Verdent06 (optional). Do not invent a personal site you do not have. |
| Tell us about something you've put into the world for others to use or experience. It can be a project, product, event, community, initiative, anything. | * | **Do not paste AI.** Type from the fact sheet below. Description on the form: "You can share in any format: video, deck, writing. Using any AI will automatically disqualify your application." |
| What do you think you have the potential to be top 0.01% in the world at? It can be personal, professional, anything you can think of. | * | Type the short `input_text` below in your own words. This field is `input_text`, not a long textarea. |
| GPA (undergraduate) | * | **3.66** (4.0 scale). Matches the PDF. Description: "Please specify your undergraduate GPA on a 4.0 scale." |
| ITAR Status | * | **U.S. Citizen.** Do **not** pick Green Card / protected person unless that is actually true. Do **not** pick **Not Applicable**. Do not claim a clearance. |
| Onsite Availability | * | **Yes** — 5 days/week El Segundo, CA for Summer 2027. Relocating from Michigan. |
| School / degree (Greenhouse `education_required` widget — not in the custom `questions` array) | * | University of Michigan · B.S. Computer Science and Economics · start **Aug 2025** · end **May 2028** (Expected). Junior. |
| Mailing address if asked | | 49032 Freestone Dr, Northville, MI 48168. School city on the resume: Ann Arbor, MI. |
| Languages you can interview in | | **Python, C++, TypeScript/JavaScript (Angular + React), SQL**. Do **not** check Go, Java, C#, MES, or PLM. |
| Voluntary self-ID | | Not on the public questions API (`demographic_questions: null`). If Greenhouse injects Gender / Race / Veteran after login: skip / **Decline To Self Identify** (`recruiting.md` Part I §2). |

---

## "Tell us about something you've put into the world for others to use or experience." * (textarea)

**STOP — AI knockout.** The form text is: "You can share in any format: video, deck, writing. Using any AI will automatically disqualify your application." Do **not** paste the paragraph below into Greenhouse. Type it in your own words from these facts. A slightly messy first-person version you typed is safer than a polished paste.

**Facts you can use (all from `context.md`):**

- Product: **Vylet** — vyletdata.com — live lead-sourcing tool for PE/search-fund.
- Users: **3 paying subscription clients** (workforce-software, landscaping, geography-first).
- Money: **$1,500 MRR**.
- What they used to do: ~30 minutes of manual work per business.
- What they get now: 30 scored leads in 30 minutes (30x) on a Dockerized LangGraph pipeline with Redis/Celery workers.
- A real bug other people felt: name-collision in ownership verification was rejecting valid targets; fix lifted qualification **79% → 89%** with no change in sourcing volume.
- You are the founder. You own git, production, and the defect.

**Hand-typed draft (rewrite before paste — do not submit this paragraph as-is):**

I shipped Vylet (vyletdata.com), a live lead-sourcing product three PE/search-fund clients actually pay for ($1,500 MRR). They used to spend about 30 minutes researching one business by hand. The tool runs a Dockerized pipeline on Redis/Celery and returns 30 scored leads in 30 minutes. After launch I found a name-collision bug that was throwing out real companies because they shared a name with an unrelated business somewhere else; fixing that raised the qualification rate from 79% to 89% without changing how many leads we sourced. I am the only engineer. I do not have a factory or CAD internship. Closest analog to Amca's intern work is software other people use, on a recurring cycle, that I have to fix when it is wrong.

If you would rather write about a GitHub artifact instead of a paid product: **Granular synthesizer** (github.com/Verdent06/granular-synth) is VST3/AU other people can install. It is C++/JUCE, not factory software. Prefer Vylet for this Amca intern.

---

## "What do you think you have the potential to be top 0.01% in the world at?" * (`input_text` — keep short)

**Type this yourself.** Suggested honest line (one or two sentences):

Turning messy public records into a tool a non-engineer will actually use, then staying on the hook when it breaks. That is the through-line on the MCFN filings pipeline and on Vylet — not a claim that I am a 0.01% coder.

Do not write "AI" or "hustle" or "defense manufacturing." Do not invent factory-floor greatness.

---

## Availability

Summer **2027**, paid, **onsite El Segundo HQ 5 days/week**. Start ~**May 17, 2027** (Monday; can shift ±1 week to match the intern cohort). UMich winter term is over by then. End ~**August 7, 2027** (typical 12-week block; JD does not print dates). Returning to Michigan for Fall 2027 (Expected May 2028). GPA **3.66**. U.S. citizen; no sponsorship. Comp: accept posted **$30–$50/hr**.

---

## Notes for the applicant (not for submission)

- **Do not claim Go, MES, PLM, CAD-as-SWE, RAPID internals, a factory internship, or a clearance.** JD prefers TypeScript / React / Go / Python / SQL as an or-list. Honest mapping: Python + TypeScript/React + SQL + AWS/Docker/Postgres. Ramp Go in the interview; do not check it.
- **Do not invent a Granular runtime metric.** Pool has no xrun / callback-latency / CPU / user count.
- **Vylet still reads as PE/LangGraph on the PDF.** If asked, pivot to Docker/Redis/Celery, the 79%→89% defect, and SQL freshness — not the GTM story (`grade.md` Defend).
- **El Segundo 5-day is a form knockout.** Housing is on you. Only submit if you will actually relocate for the summer.
- **The "put into the world" answer is the binding non-resume filter.** Type it. Video/deck/writing are all allowed; AI is not.
- **No Cover Letter field** on this Greenhouse posting. Do not email a letter to `verdent06@gmail.com` or to Amca from this agent.
- **Referral:** none in `network.md`. A real Amca name beats Greenhouse; a fake name is a knockout.
- **Email is `verdent06@gmail.com` on the PDF and every Greenhouse field.** Never `vedantde@umich.edu`.
- **Funnel:** resume is the bottleneck (`grade.md` 8.0 / High screen; `companies.md` ~5–10%). No published OA. Prep the filings ETL + React/Postgres walk (`grade.md` Interview angles).
- **This agent did not submit.**
