# Muon Space — Flight Software Engineering Intern (Summer 2027) · Written Application Answers

Draft answers for Greenhouse job **5247725007** / req **501** / internal **4685263007**. Grounded in `persona.md` (full-stack spine + aerospace / LEO-satellite / flight-software / real-time differentiator), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** C as distinct from C++, ROS, MCU firmware, orbital mechanics, satellite/flight internships, rocket club, RTOS, SIL/HIL, a clearance, Granular xrun/latency/CPU numbers, MDC API traffic/latency.

**Do not submit from this agent.** Packet only. **Never email `verdent06@gmail.com` (or any address) with this packet / PDF / answers.** App Man downloads via `gh`.

Apply: https://job-boards.greenhouse.io/muonspace/jobs/5247725007
Resume: `applications/2027/muon-space/flight-software-engineering-intern/Vedant Desai Resume.pdf`
SHA-256: `f314a2a38bc3cfe998056f9aa7f0c082ce2775f307317e300cdc7631f1b1b533`

**Pulled from the live Greenhouse apply page + questions API** (`boards-api.greenhouse.io/v1/boards/muonspace/jobs/5247725007?questions=true`) on **2026-10-01**. Labels below are exact. `*` = required. Hidden `longitude` / `latitude` are filled by the Location picker — do not type them.

**Form / PDF email MUST be `verdent06@gmail.com`.** Never `vedantde@umich.edu`. Autofill may still pull umich from a prior Greenhouse profile; overwrite.

This is **Flight Software Engineering Intern (Summer 2027)** only. **Not** Applied Science Intern. **Not** a generic cloud-SWE intern.

Airtable: `rec85Awkk7DF9MHGd`

---

## Knockouts (read first)

1. U.S. Person / export control — **US Citizen.** (`context.md`). LPR / Protected Person also qualify; **None** is auto-reject. Do not claim a clearance.
2. On-site for the internship — JD is **Mountain View or San Jose, CA**, full-time, May–September window. Vedant can relocate to CA for the term and return to Michigan Fall 2027.
3. **Form leftover:** required question still says **Woodbridge, VA** on this San Jose posting (Muon has a VA BD listing; intern JD is CA). Answer **Yes** meaning on-site for *this* intern (CA). Do not treat Woodbridge as the work location.
4. Currently a student — **clears** (UMich CS + Economics, Expected May 2028).
5. Returning to school after the term — Fall 2027 / Winter 2028 remain.

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on citizenship or onsite.

Posting carries Greenhouse AI Talent Matching disclaimer. Opt-out URL exists (`http://app7.greenhouse.io/ai_opt_out_request/job_post/5247725007/ai_opt_out`). Do not treat opt-out as required.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact labels on the live Greenhouse apply form for job **5247725007**.

| Field | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | **verdent06@gmail.com** (never `vedantde@umich.edu`). PDF header matches. Overwrite Autofill if it inserts umich. |
| Phone * | (248) 704-4852 |
| Resume/CV * | `applications/2027/muon-space/flight-software-engineering-intern/Vedant Desai Resume.pdf` — attach the PDF |
| Cover Letter | Optional. Leave blank **or** paste the short letter below. PDF is the screen (`companies.md`: bottleneck resume). |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 |
| Please provide your permanent address (city, state, zip code). We use this information to determine eligibility for relocation assistance for the internship. A permanent address is your long-term, stable home base used for legal identity, government records, and official mail. * | **Northville, MI 48168** (street if a later page asks: 49032 Freestone Dr) |
| Please confirm you are willing to be on-site for the duration of the internship in Woodbridge, VA. * | **Yes** — meaning on-site for **this** intern in **San Jose / Mountain View, CA** as the JD states. The Woodbridge, VA label is a leftover on a CA FSW intern req. Do **not** pick No (likely auto-reject). Do **not** plan to report to Woodbridge. |
| U.S. Export Control laws require that access to certain technical information be limited to U.S. Persons (U.S. Citizens and Lawful Permanent Residents/Green Card Holders) and individuals granted appropriate authorization. Please indicate your current Immigration and Work Authorization status. Verification will be required upon hire.* * | **US Citizen.** Do **not** pick Lawful Permanent Resident / Protected Person unless that is actually true. Do **not** pick **None**. Do not claim a clearance. |
| Anticipated Graduation Date | **May 2028** |
| Location * | Ann Arbor, MI (school city on the resume). Relocate to San Jose / Mountain View for the term: **Yes**. Hidden lat/long come from the picker. |
| School / degree / GPA (not on this form; on the PDF) | University of Michigan · B.S. Computer Science and Economics · GPA **3.66 / 4.0** · Expected **May 2028** · Junior now (Oct 2026); Summer 2027 = after junior year, returning Fall 2027 |
| Languages you can interview in | **C++, Python, TypeScript/JavaScript (Angular), SQL**. Do **not** check C-as-distinct-from-C++, Rust, Java, ROS, or firmware. |
| Gender (Voluntary Self-Identification) | Optional. **Decline To Self Identify** for volume (`recruiting.md` Part I §2). |
| Race (Voluntary Self-Identification) | Optional. **Decline To Self Identify**. |
| VeteranStatus (Voluntary Self-Identification) | Optional. **I don't wish to answer**. |

---

## Cover letter (optional — paste only if attaching)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Muon Space — Flight Software Engineering Intern (Summer 2027)
San Jose / Mountain View, CA (onsite)

Dear Muon Space recruiting team,

I am applying for the Summer 2027 Flight Software Engineering Intern role. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work onsite in San Jose or Mountain View for the May–September intern window and I return to Michigan afterward. I am a U.S. citizen and do not need sponsorship.

This intern job is software that runs on spacecraft, plus the tests and tools used to prove it — not a generic CRUD rotation and not the Applied Science intern. I have not shipped RTOS, ROS, or satellite flight software. I have shipped C++ that cannot miss a deadline, Python services other people use, and debugging when software and "hardware-shaped" constraints (audio callbacks, on-device inference, S3 upload failures) interact.

What I would bring:

- **C++ under a hard constraint.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit. github.com/Verdent06/granular-synth
- **Debug + tests.** At CaseStudyPrep.AI I closed a 27% audio-upload failure rate (expired S3 URLs + MIME mismatch) and held main-thread blocking under 5ms at 60 FPS. At Vylet I diagnosed a name-collision defect that lifted lead-qualification from 79% to 89%, and I wrote a pure-Python consensus gate that hard-fails bad leads before a score threshold.
- **Python others depend on.** As the only engineer on a five-month Michigan Campaign Finance Network contract I delivered a production Flask REST API on AWS EC2 after replacing ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 committees.

I interview in C++ and Python. I want the San Jose / Mountain View FSW intern seat writing spacecraft software and the tests that back it.

Sincerely,
Vedant Desai

---

## Availability

Summer 2027, paid, **onsite San Jose or Mountain View, CA**, May–September window per university schedule. Start **May 17, 2027** (Monday; can shift ±1 week to match the intern cohort). End **August 6, 2027** (Friday — 12 weeks from May 17) unless Muon runs later into September. Returning to the University of Michigan (Expected May 2028). GPA 3.66. US citizen; no sponsorship. Comp: accept posted **$40/hour** (bachelor's).

---

## Notes for the applicant (not for submission)

- **Woodbridge, VA is a form bug on a CA intern req.** Confirm the live label before submit. If it still says Woodbridge, select **Yes** for on-site CA as posted. If Muon has split this req to a real VA intern, stop and do not use this packet.
- **Do not claim C, ROS, MCU firmware, orbital mechanics, a satellite internship, RTOS, or a clearance.** Honest mapping: C++ real-time (Granular) + Python production (MDC) + intern debug (CaseStudyPrep / Vylet).
- **Do not invent a Granular runtime metric.** Pool has no xrun / callback-latency / CPU / user count. Walk MemoryPool, lock-free SPSC, and the `processBlock` audit.
- **Vylet still reads PE/LangGraph on a skim.** If asked, pivot to the name-collision fix and the pure-Python hard-fail gate — not the GTM story (`grade.md` Defend).
- **Cover letter is optional.** Attach it if you want; the PDF is the screen. Binding filter after that: unpublished intern tech (`companies.md`: bottleneck resume, ~5–8%).
- **Referral:** none in `network.md`. A real Muon name beats Greenhouse; a fake name is a knockout.
- **Email is `verdent06@gmail.com` on the PDF and every Greenhouse field.** Never `vedantde@umich.edu`.
- **This agent did not apply.** Packet only. App Man downloads via `gh`. Never email this pack.
