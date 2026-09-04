# Primer — Spring/Summer 2027 Engineering Intern · Written Application Answers

Paste-ready answers for the **live Ashby form** (captured 2026-09-04) plus the **real submit path** they printed on the page. Grounded in `persona.md` (full-stack PrimerOS intern: TypeScript/React/Postgres through use, stakeholder-facing shipping — **not** Node/GraphQL/Prisma/Next/Relay) and the form kit. First-person, honest, defensible under "walk me through this."

**Employer / title / location from the live page:** Primer · **Spring/Summer 2027 Engineering Intern** · Engineering · San Francisco · Intern · Ashby `edd1667b-6323-444a-adc1-40bae5b9a3b0`.

Apply URL (do not Submit from this agent): https://jobs.ashbyhq.com/primer/edd1667b-6323-444a-adc1-40bae5b9a3b0/application

**This agent did not submit** and did not POST to `api.primer.com`.

**Form-kit identity (use everywhere — never school email):**
Email **verdent06@gmail.com** · Phone **248-704-4852** · US citizen, no sponsorship · GPA **3.66** · Expected **May 2028** (Junior) · Address **49032 Freestone Dr, Northville, MI 48168** · LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06

PDF: `applications/2027/primer/software-engineer-intern-full-stack-summer-2027/Vedant Desai Resume.pdf`
SHA-256: `ed500e0ecf6d9ebe1dad01b78b80eed483b13131175bdb4fb81b538bd77a1c0d`

---

## CRITICAL — real submit path (printed on the Ashby page)

> Do not click apply to submit your application; we will not review it. Instead, send a POST request to https://api.primer.com/swe-application with the following fields in the json body of the request: full_name (string), email (string), github_url (string), and resume_url (string).

Ashby **Submit Application** is the decoy. Host this packet PDF at a **public** `resume_url`, then POST. Example (replace `RESUME_PUBLIC_URL`):

```bash
curl -X POST 'https://api.primer.com/swe-application' \
  -H 'Content-Type: application/json' \
  -d '{
    "full_name": "Vedant Desai",
    "email": "verdent06@gmail.com",
    "github_url": "https://github.com/Verdent06",
    "resume_url": "RESUME_PUBLIC_URL"
  }'
```

You still fill the Ashby fields below so a human who opens the ATS row sees the essays. **Do not click Submit** unless you have already POSTed and still want a duplicate ATS row.

---

## Live Ashby fields (captured 2026-09-04)

### Autofill / identity

| Exact label | Required | Answer |
| --- | --- | --- |
| Autofill from resume | | Upload the packet PDF first. Then **fix email** if it parses `vedantde@umich.edu` → **verdent06@gmail.com**. |
| Name * | * | Vedant Desai |
| Email * | * | **verdent06@gmail.com** |
| GitHub Profile * | * | https://github.com/Verdent06 |
| Resume * | * | `Vedant Desai Resume.pdf` (this packet) |

### Essays / location / proof of work

| Exact label | Required | Answer |
| --- | --- | --- |
| Why are you interested in Primer, and this role in particular? * | * | Paste **Why Primer** below |
| Where are you located? * | * | **Northville, Michigan, United States** (kit address). Relocating to SF for the intern term — do not pick San Francisco as current location unless you already live there. |
| What's something you've built, led, or improved that you're most proud of? * | * | Paste **Proud of** below. Helper text: goal / your part / impact. **250 words or less.** |
| Proof of work - What you've built (Website link) * | * | **https://github.com/Verdent06/SignalWeaver** (React/TypeScript + FastAPI + Postgres + CI). Optional second surface if the field allows only one URL: keep SignalWeaver here; mention https://vyletdata.com in Why Primer. File upload AND/OR link. Do **not** upload confidential employer material. |

### Knockouts (Yes / No buttons)

| Exact label | Answer |
| --- | --- |
| This is an early-stage, high-intensity role that sometimes requires nights and weekends during key sprints. Is this type of environment something you are actively looking for right now? * | **Yes** — only if that is actually true. **No** is likely a screen-out. Do not lie. |
| Are you able to work in San Francisco 5 days a week? * | **Yes** |
| Are you currently authorized to work in the United States? * | **Yes** |
| Will you now, or in the future, require sponsorship for employment visa status (e.g. H-1B visa status)? * | **No** (US citizen). JD offers J-1/F-1; still answer **No**. |

No start-date picker and no education block on the live form. Put Summer 2027 / Expected May 2028 in Why Primer.

---

## Why are you interested in Primer, and this role in particular? (paste)

I'm applying because the intern job is PrimerOS — an operating system teachers, students, and families actually use — not a shadow project. I want to ship product for non-engineers in an operational setting. That is the closest analog I have: as the sole engineer on a five-month Michigan Campaign Finance Network contract, I delivered a production Flask REST API on AWS EC2 into a nonprofit's public-facing research workflow, after replacing about 800 hours of manual filing pulls across 400 PACs. I also run Vylet (vyletdata.com), a live lead-sourcing product with three paying clients and a production defect I diagnosed (qualification 79% to 89%).

On stack, I can defend TypeScript, React, and Postgres through use. SignalWeaver is a React/TypeScript dashboard on FastAPI and Postgres/pgvector, containerized with Docker Compose, with GitHub Actions CI (frontend build, pytest, API image). I have not used Node, GraphQL, Prisma, Next, or Relay on a team. I will ramp; I will not list them as if they are already mine.

I can work in San Francisco five days a week for Summer 2027 (May or June start). I am a Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66), a US citizen, and I do not need visa sponsorship. I return to Ann Arbor for Fall 2027, so I cannot honestly commit to a 4–8 month leave. If a summer term still works, I want the seat.

---

## What's something you've built, led, or improved that you're most proud of? (paste · ≤250 words)

Goal: stop Michigan campaign-finance researchers from spending about two hours per committee on Bureau of Elections portal searches and irregular Excel exports.

Part I played: sole engineer on a five-month Michigan Campaign Finance Network contract. I built a Requests + Pandas ETL that ingested filings directly, a deterministic aggregation engine that ranked PACs by funding volume, and a production Flask REST API on AWS EC2 that wired those rankings into the nonprofit's public-facing workflow. I scoped delivery with MCFN stakeholders myself — no backend team to share API design or deploy.

Impact: about 800 hours of manual pulls eliminated across 400 tracked PACs, and a live API researchers actually use. That is the closest thing I have to PrimerOS: software non-engineers depend on, owned end-to-end, shipped on a deadline.

(~140 words)

---

## Notes for the applicant (not for submission)

- **POST is the application.** Ashby Submit without the JSON POST is what they said they will not review.
- **Never school email.** Autofill will try `vedantde@umich.edu`. Override every time.
- **Do not invent Node / GraphQL / Prisma / Next / Relay.** Persona anti-pattern. Ramp story is allowed; Skills stuffing is not.
- **Summer 2027 only.** Preferred 4–8 months is on the JD, not on the form. The Why essay already discloses it. Do not "yes, and" a leave of absence you will not take.
- **SF 5 days/week = Yes** is a hard work-model gate. You said relocate Yes.
- **Proof of work:** SignalWeaver GitHub, not a confidential MDC dump. Vylet is the live-product URL if they ask for a second link.
- **No Primer contact in `network.md`.** Cold apply. First-wave req (posted 2026-09-04) — apply inside ~72 hours (`recruiting.md` §8).
- Cover letter: none on the live form beyond the two textareas. Do not attach an extra letter unless a later step asks.
