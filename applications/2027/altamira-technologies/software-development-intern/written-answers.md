# Altamira Technologies — Software Development Intern (2027) · Screening / Cover-Letter Answers

Draft answers for Altamira's Jobvite application, grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under "walk me through this" — no invented experience or metrics. Trim to each form's length limit; if only one free-text box is offered, lead with "Why Altamira."

**Hard knockout:** this req requires U.S. citizenship. `context.md` does not record citizenship. Do not submit unless that is true. Do not claim Java.

---

## "Are you a U.S. Citizen?" / work authorization

**Only if true:** Yes — I am a U.S. citizen and authorized to work in the United States without sponsorship.

If that is not true, do not apply. This is a binary Jobvite reject, not something the resume can paper over.

---

## "Why Altamira / why this internship?"

I want to spend a summer writing software that turns messy, multi-source data into something an operator can actually use — which is the job Altamira describes, not a generic intern rotation. That is the work I already do: I replaced a manual campaign-finance research process with a Requests + Pandas ETL and shipped a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract, eliminating ~800 hours of pulls across 400 PACs. For a search fund I aggregated EPA ECHO and MassGIS regulatory data into a unified entity database and delivered 800+ validated Day-1 acquisition targets. Altamira's Fairborn team sits in the Wright-Patt ecosystem doing the same class of problem at national-security scale — data processing and intelligence extraction over real requirements, with C++, Python, TypeScript, and PostgreSQL/PostGIS in the mix. I can show all of those in shipped work, and I built a C++/JUCE real-time audio engine from scratch specifically to learn a hard stack and apply it. I would relocate to Fairborn for Summer 2027.

---

## "Tell us about a project / something you've built."

Two that map onto this team's work:

**Lyndbrook Capital (data engineering consultant)** — contracted pre-LOI to build acquisition intelligence for water-utility operators. I aggregated EPA ECHO and MassGIS regulatory data into a unified PWSID entity database, delivered 800+ validated Day-1 targets, and automated off-market sourcing by cross-referencing 2,500+ legal entities against Google Maps API data, cutting ~15 hours of manual prospecting per week. That is multi-source + geospatial entity resolution — the closest analog I have to the intelligence-extraction work in the JD.

**SignalWeaver** — a full-stack research platform I own end-to-end: semantic search over stored news with pgvector (49ms p50 / 99ms p99), a React/TypeScript dashboard with scores persisted to Postgres, and a Docker Compose + GitHub Actions CI pipeline (frontend build, pytest, API image build on main). Code: github.com/Verdent06/SignalWeaver.

---

## "Describe a time you learned a new technology and applied it."

I wanted to understand real-time constraints rather than read about them, so I built a granular synthesizer plugin from scratch in C++/JUCE — a stack I did not already ship in. The audio thread cannot allocate or take a lock, so I pre-allocated a `MemoryPool<Grain, 64>` slab per voice and wired UI-to-audio delivery through a hand-rolled SPSC FIFO (atomic head/tail, no mutex) with WAV handoff via atomic `shared_ptr` swap. That is the same "learn it, then apply it to the assigned constraint" motion this JD asks for, just in a DSP setting instead of a mission system.

---

## "Availability / onsite Fairborn"

Yes — I can work onsite in Fairborn, OH for Summer 2027 (available to start May 2027). I am a Computer Science and Economics student at the University of Michigan (expected May 2028) and would return to school after the internship.

---

## Notes for the applicant (not for submission)

- **Lead with data pipelines, not the synth.** Open with MDC + Lyndbrook (ETL, entity resolution, geospatial). Granular is the C++/learn-new-stack proof, not the mission story.
- **Do not claim Java.** It is on the JD list; it is not in your pool. "Familiarity with some of" is the bar — Python, TypeScript, C++, SQL/Postgres, HTML/CSS is enough.
- **Citizenship is the real gate.** Confirm it on the form. A referral into Fairborn / Parsons D&I / Wright-Patt beats another resume pass.
- Jobvite may only show citizenship + resume upload + a short "additional information" box. If so, paste a trimmed Why Altamira paragraph.
