# Palantir Technologies — Software Engineer, Internship (Palo Alto, on-site) · Written Application Answers

Draft answers for Lever `e27af7ab-41fc-40c9-b31d-02c6cb1c505c`. Grounded in `persona.md` (full-stack spine + defense/gov + operational data platforms), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Java, Go, Spark, Cassandra, Elasticsearch, Gradle, Palantir product usage (Gotham/Foundry/Apollo/AIP), clearance in hand, high school name/year, citizenship, Granular latency/xrun/CPU/user numbers.

**Do not submit from this run.** Artifacts only.

Job: https://jobs.lever.co/palantir/e27af7ab-41fc-40c9-b31d-02c6cb1c505c
Apply form (do not submit): https://jobs.lever.co/palantir/e27af7ab-41fc-40c9-b31d-02c6cb1c505c/apply
Resume: `applications/2027/palantir/software-engineer-intern/Vedant Desai Resume.pdf`

This posting is **Dev / Internship / Product Development SWE** in **Palo Alto, CA, on-site** — not FDSE. Term: **Summer 2027** (Expected May 2028 = final internship before graduating).

---

## Identity / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| Full name | Vedant Desai |
| Preferred name | Vedant |
| Name pronunciation | **NEED APPLICANT** — do not invent a phonetic spelling. Common public reading of Vedant is along the lines of "VAY-dahnt"; confirm before submitting. |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| Current location | Ann Arbor, MI (school city on the resume). Other 2027 apps mention Northville, MI for mailing — do not invent a zip. |
| Current company | Founder, Vylet (May 2026–Present) if they want a current role; otherwise omit |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Portfolio / website | **Omit** (`context.md`: omit from resume header). GitHub is the honest site if a URL is required. |
| Resume | `applications/2027/palantir/software-engineer-intern/Vedant Desai Resume.pdf` |
| Language skill(s) (spoken) | **English only.** Do **not** check Gujarati / Marathi / Hindi — not in `context.md`. |
| Upcoming offer deadlines? | **No** (TRACKER: 0 offers) |
| If so, dates | Leave blank |
| Anticipated start date (Month/Year) | **May 2027** (Summer 2027 intern; semester calendar, typically late May) |
| Applying to (this req) | **Palo Alto, CA** — on-site. Willing to intern onsite Palo Alto Summer 2027. Not fully remote. |
| Preferred locations 1–3 **in addition to** Palo Alto | **New York, NY** and **Denver, CO** (Palantir PD offices). **Assumption:** TRACKER shows Bay + NYC intern applications; Denver is a Palantir PD office, not a ranked personal pick. Do **not** add DC unless you will intern there for gov/Gotham. Flag if you will not intern onsite NYC or Denver — uncheck those. |
| Further location context | Not fully remote. This packet commits to Palo Alto. |
| Is this your final internship before graduating? | **Yes** — Expected May 2028; Summer 2027 is the last internship before graduating. Matches the JD. |
| Legally authorized to work in the US? | Answer **truthfully**. Other 2027 packets treat you as a **US citizen**. If that is true: **Yes**. If it is not, stop and answer honestly — do not guess. `context.md` has no citizenship field. |
| Future sponsorship (H-1B)? | **No** if you are a US citizen / do not need a visa. Same honesty rule. Do not guess. |
| High school name & graduation year | **NEED APPLICANT — not in context.md. Do not invent.** |
| University | **University of Michigan** (Ann Arbor — pick the listed Michigan option) |
| Year of graduation | **2028** |
| How did you hear about this job? | **Palantir Website** (this run was handed a Lever URL). Do **not** pick Friend / Recruiter / Ambassador / Referral. |
| Preferred Palantir product(s) (1–2) | **Foundry**, then **Apollo**. Honest context: **no Palantir product experience.** Foundry is the analog for data integration / operational datasets (ETL, entity-style records, APIs). Apollo is the analog for shipping/infra (Docker, CI, production deploy). Do not pick Gotham unless you can defend mission-critical/systems without claiming intel work. |
| Which SWE role resonates? | **Software Engineer (Dev / Product Development)** — see essay 4. Confirm checkbox: **Yes** — this answer matches the SWE/PD application. **Not FDSE.** |
| Programming languages you can interview in | **C++, Python, TypeScript/JavaScript, SQL**. Do **not** check Java, Go, Spark, Cassandra, Elasticsearch. |
| AI Notetaker consent | Default **Yes, I consent** (optional; does not impact candidacy). Change if you prefer No. |
| Additional information | Optional. 2–3 sentences pointing at the PDF + essays is enough. No cover letter required on Lever. |
| EEO / veteran / disability | Voluntary. **Decline** unless you want to answer. Do not invent. |

---

## Essay 1 — If Palantir didn't exist, what kind of company or work would you be most excited and interested in working at/on? (≈200 words) REQUIRED

If Palantir didn't exist I would still want to write software that other people use to make operational decisions from messy data — a productized platform, not a one-off dashboard and not a consumer CRUD app.

That is the work I already ship. As the only engineer on a five-month Michigan Campaign Finance Network contract I replaced portal-search / hand-normalized Excel pulls (~2 hours per committee) with a Requests + Pandas ETL, eliminating ~800 hours of manual pulls across 400 tracked PACs, and delivered a production Flask REST API on AWS EC2 into their public research workflow. The ranking was the product.

The same shape shows up when the operator is a search-fund principal. At Lyndbrook I unified EPA ECHO and MassGIS into a PWSID entity database and delivered 800+ Day-1 targets. At Vylet (live product, $1,500 MRR) I run a Dockerized scoring pipeline and I fixed a name-collision defect that was rejecting valid targets — qualification 79% → 89% with no change in sourcing volume.

I have not used Gotham, Foundry, or Apollo. I am not applying because defense is a brand. I want to build data platforms high-stakes operators actually run on, at a company whose intern job is contributing code to that platform.

---

## Essay 2 — What is the hardest technical challenge you've faced as part of work experience or a personal project? (≈200 words) REQUIRED

The hardest constraint I have actually enforced is the audio thread in a C++/JUCE granular synthesizer I built from scratch (github.com/Verdent06/granular-synth).

`processBlock()` is a real-time callback. If it heap-allocates or takes a mutex, the product glitches. I do **not** have a callback-latency, xrun, or CPU number — I would measure those if asked, and I will not invent them. The constraint I can defend: after `prepareToPlay()`, that callback never calls `new` or `delete` and never takes a lock.

The decision was to treat memory as a compile-time budget. I pre-allocate a `MemoryPool<Grain, 64>` slab per voice at startup — a fixed free-list — so grain acquire/release never touches the heap. The UI still has to deliver slider changes. A mutex would make the audio thread wait on a human; I rejected it. I built a 64-slot SPSC FIFO with atomic head/tail (acquire/release) so updates are non-blocking, and WAV buffers hand off with an atomic `shared_ptr` swap.

I also pre-compute ADSR rates as samples-per-step so the hot loop does not divide, and I run 16-voice polyphony with age-based stealing. That is systems discipline under a deadline the CPU will not extend.

---

## Essay 3 — Tell us one thing that's not on your resume that you're proud of. (optional — fill)

Vylet's Node 3 consensus gate is not on the attached resume. After the LLM-heavy extraction steps, I wrote a pure-Python triangulated check — no model calls — that fuzzy-matches the query, the state business registry, and a live website crawl, then hard-fails on legal status, industry, geography, or independence before a 0–100 score even applies. I am proud of it because the pipeline got more trustworthy by *removing* an LLM from the critical path, not by adding one. That is the data-correctness instinct I would bring to a Foundry-shaped intern project. I have not used Foundry.

---

## Essay 4 — Forward Deployed Software Engineer vs Software Engineer. Which resonates and why?

**Software Engineer (Dev / Product Development).** This application is the PD intern req. I am **not** applying to FDSE with this packet.

Dev owns one capability for many customers — a slice of Foundry, Gotham, or Apollo. Delta / FDSE owns one customer and many capabilities, on-site. I have done Delta-adjacent work: I was the sole engineer facing MCFN stakeholders for five months, and I run Vylet for paying clients. That taught me to scope with non-engineers and ship into a real workflow. It is not the job I want this summer.

I want to build the platform those deployment people configure. MDC, Vylet, and SignalWeaver are APIs, pipelines, and UIs meant to be reused, not a one-customer customization. Palantir's intern posting is contributing code to products used across institutions, on a small PD team, with a mentor, through the full lifecycle. That is Dev.

Confirm checkbox: **Yes** — this answer matches Software Engineer / Product Development.

---

## Preferred products (short honest context)

- **Foundry** — analog: ETL, entity-style records, APIs over operational datasets (MDC PAC rankings, Lyndbrook PWSID database, Vylet scoring). I have not used Foundry.
- **Apollo** — analog: Docker, CI, production deploy (Vylet Docker/Redis/Celery; SignalWeaver Docker Compose + GitHub Actions in the pool, not all on this PDF). I have not used Apollo.

---

## Additional information (optional; paste if you want a box filled)

PDF resume attached. Essays above are for the PD SWE intern seat in Palo Alto, Summer 2027 — not FDSE. I have not used Palantir products. I interview in C++, Python, TypeScript/JavaScript, and SQL.

---

## Notes for the applicant (not for submission)

- **This is an apply packet, not a submitted application.** Upload the PDF and paste essays yourself on Lever.
- **Do not claim Java, Go, Spark, Cassandra, Elasticsearch, Gradle, or Palantir products.** JD: languages at join do not matter if you learn quickly.
- **Do not invent a Granular runtime metric.** Pool has no xrun / callback-latency / CPU / user count (`grade.md` Defend).
- **Work authorization / sponsorship:** `context.md` has no citizenship field. Answer truthfully. If you are a US citizen: Yes / no sponsorship. If you are not, do not copy other packets.
- **High school** must come from you. Blank is better than a guess.
- **Locations:** Palo Alto is the commit for this req. NYC + Denver are extras **only if** you will intern onsite there. Do not add DC by default.
- **Referral:** none assumed. Do not pick Friend/Recruiter/Ambassador.
- **Binding filters after the PDF:** recruiter screen (bottleneck, <2–3%), then Karat / Decomposition — not more resume polish (`companies.md`, `grade.md`).
- **Spoken languages:** English only unless you want to add others that are actually true.
