# Waymo — 2027 Summer Intern, BS, Software Engineer, Driver Refinement Foundations · Written Application Answers

Draft answers for Greenhouse job **8224900** (req **5451**, internal **3559589**). Labels and dropdowns captured from the live apply page `https://boards.greenhouse.io/embed/job_app?for=waymo&token=8224900` and `https://boards-api.greenhouse.io/v1/boards/waymo/jobs/8224900?questions=true` on **2026-09-26** (`first_published` / `updated_at` **2026-09-25T16:20:21-04:00**; office **Mountain View (US-MTV-EMF680)**). Grounded in `persona.md` (full-stack spine + autonomy / AV reasoning-platform differentiator), `grade.md` Interview angles, and `context.md` identity/metrics only.

**Do not invent:** ROS/ROS2, Linux as a claimed environment, Waymo/AV internships, onboard planner work, CUDA, Bazel, Go, Java, Granular latency/xrun/CPU/user numbers, MDC API traffic/latency, MatchStream / FRC (commented out of the pool).

Apply: https://careers.withwaymo.com/jobs?gh_jid=8224900
Greenhouse embed: https://boards.greenhouse.io/embed/job_app?for=waymo&token=8224900
Resume: `applications/2027/waymo/software-engineer-intern-driver-refinement-foundations/Vedant Desai Resume.pdf`

**Pulled from the posting:** Waymo · 2027 Summer Intern, BS, Software Engineer, Driver Refinement Foundations · Mountain View, CA · hybrid onsite · **$60/hr** · Reasoning Platform (C++ autolabeler / event mining / GT labeling / quality eval). Rolling until filled. Apply to each role individually; top 3.

This is **Summer 2027, BS only** — not the MS/PhD SWE twins, not Maneuvering Tech, not SysEng.

**Do not submit from this agent. Do not email verdent06@gmail.com.** App Man downloads via `gh`.

---

## Knockout / structured fields (fill exactly)

Questions below are the exact labels on the live Greenhouse apply page (token **8224900**). `*` = required on the form. Hidden `Longitude` / `Latitude` are filled by the Location picker — do not type them.

| Field | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Email * | **verdent06@gmail.com** (never `vedantde@umich.edu`) |
| Country * (phone) | United States |
| Phone * | (248) 704-4852 |
| Candidate Location * | **Ann Arbor, Michigan, United States** (use the picker). Legal/home address in `context.md` is Northville, MI 48168 — school-year location is Ann Arbor. |
| Resume/CV * | `applications/2027/waymo/software-engineer-intern-driver-refinement-foundations/Vedant Desai Resume.pdf` |
| Cover Letter | Optional. Paste the letter below if attaching / entering manually. |
| Website | https://github.com/Verdent06 |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| How did you hear about this opportunity? | **Waymo Careers Page** (the URL you were given). Do **not** invent a referral — none in `network.md`. Listed options: A personal contact at Google/Alphabet told me about the opportunity · A personal contact at Waymo told me about the opportunity · Academic Contact (professor recommendation, classmate, etc.) · Agency Recruiter Outreach · Alphabet's Internal Job Board (Grow) · Glassdoor · Handshake · Indeed · LinkedIn · Media (blog post, news article, etc.) · Social Media (Facebook, Twitter, etc.) · University Event (info session, tech talk, luncheon, etc.) · University Job Board · Waymo Careers Page · Waymo Industry Event (conference, career fair, etc.) · Waymo Recruiter Outreach · Waymo Advertising · Word of Mouth · Other |
| Do you require work authorization? * | **No** (U.S. citizen; the follow-up treats this as sponsorship). Do **not** select Yes. |
| If yes, what kind? (If you do not require work authorization sponsorship please select Not Applicable.) * | **Not applicable** |
| Would you require an export license under the circumstances described below? * | **No** — U.S. citizen. License rules target most-recent citizenship/PR of Cuba, Iran, North Korea, Syria, or Ukrainian territories Crimea / DNR / LNR; US citizens/nationals/LPRs/refugees/asylees do not need the license. Do **not** select Yes or I'm not sure if that is true. |
| Are you a current or former Alphabet employee, intern, vendor, contractor, or temp (including Google and other Alphabet subsidiaries)? * | **Never worked at Alphabet** |
| If yes, please provide your LDAP. | Leave blank |
| Please review and acknowledge our Candidate Privacy Policy linked below: * | **I acknowledge that I have read and understood the terms of the Waymo Applicant and Candidate Privacy Policy.** Read https://careers.withwaymo.com/candidate-privacy-policy first. |
| Please provide your full legal name as it appears on your government ID * | Vedant Desai (`context.md` has no middle name) |
| …Waymo prohibits the use of unauthorized outside assistance during the interview process… * | **I acknowledge the above policies** |
| Please provide the state/region in which you currently reside. * | **Another State in the US** (Michigan is not New York or Illinois). Options: New York · Illinois · Another State in the US · APAC · EMEA · Other |
| School / degree (if a recruiter asks; not on this embed) | University of Michigan · B.S. Computer Science and Economics · GPA 3.66 / 4.0 · Expected May 2028 |
| Languages you can interview in | **C++, Python, TypeScript/JavaScript (Angular), SQL**. Do **not** claim ROS, Java, Go, or Linux-as-daily-driver. |

---

## Candidate Demographic Survey (required on the page; decline is allowed)

Header on the live page: completion is voluntary; responses (including choosing not to respond) are confidential and not used in hiring. `recruiting.md` Part I §2: skip for volume. Each of these is marked `*` but includes **I don't wish to answer**.

| Field | Answer |
| --- | --- |
| Please indicate your gender * | **I don't wish to answer** |
| Please indicate your race / ethnic group (choose all that apply) * | **I don't wish to answer** |
| Please indicate if you are a veteran or active member of the United States Armed Forces. * | **I don't wish to answer** |

No separate OFCCP disability questionnaire was on this embed as of 2026-09-26.

---

## Cover letter (paste)

Vedant Desai
(248) 704-4852 · verdent06@gmail.com
linkedin.com/in/vedantde06 · github.com/Verdent06

Waymo — 2027 Summer Intern, BS, Software Engineer, Driver Refinement Foundations
Mountain View, CA (hybrid onsite)

Dear Waymo recruiting team,

I am applying for the Summer 2027 BS Software Engineer intern role on Driver Refinement Foundations (Reasoning Platform) in Mountain View. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work the hybrid-onsite term, I return to Michigan for Fall 2027 and Winter 2028, and I am a U.S. citizen who does not need sponsorship or an export license.

This intern job is performant C++ autolabeler code that mines useful events from everyday driving, plus ground-truth labeling, quality evaluation, and metrics. I have not shipped robot or AV software. I have C++ that cannot allocate on a real-time thread, stream-side filtering of useful events, and eval harnesses with before/after quality numbers.

What I would bring:

- **C++ under a hard constraint.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO with atomic acquire/release keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit (zero heap, zero locks). github.com/Verdent06/granular-synth
- **Mining useful events from a stream, then measuring quality.** At CaseStudyPrep.AI I filtered dead-air frames with on-device Silero VAD via ONNX Runtime (40% cloud-inference cost cut) and eliminated a 27% audio-upload failure rate with fault-tolerant RxJS around expired S3 URLs. At Vylet I built a LangSmith eval over 20 adversarial cases that lifted extraction faithfulness from 50% to 90%, and I fixed a name-collision defect that lifted lead-qualification from 79% to 89%.
- **Data pipelines you can ship.** As the only engineer on a five-month Michigan Campaign Finance Network contract I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees and delivered a production Flask REST API on AWS EC2. SignalWeaver adds pytest + GitHub Actions CI on a FastAPI service instrumented at 9.1s p50 / 15.2s p99.

I interview in C++ and Python. I want the Mountain View intern seat writing tested autolabeler C++ and reporting what actually works, not a generic feature rotation.

Sincerely,
Vedant Desai

---

## Notes for the applicant (not for submission)

- **Email is verdent06@gmail.com on the resume and on this form.** Never school email.
- **Do not claim ROS, Linux, or autonomous-robot internships.** Preferred on the JD; not in inventory. Honest mapping: C++ real-time (Granular) + event filtering (VAD) + quality eval (Vylet).
- **Granular has no runtime metric on the page.** If asked, say so — walk MemoryPool, lock-free SPSC, and the processBlock audit. Do not invent xrun/CPU numbers.
- **MDC Flask/EC2 has no traffic/latency number.** Point to 400 PACs / ~800 hours on the ETL bullet and sole-engineer delivery.
- **Work-authorization wording is sponsorship.** U.S. citizen → **No** / **Not applicable**.
- **Export license:** U.S. citizen → **No**. If that is ever not true, stop and answer honestly — this is a knockout.
- **Funnel:** Greenhouse knockouts → human screen → recruiter → HackerRank (`companies.md`) or live CoderPad **[directional, Extern 2027 guide]**. Confirm the invite. Prep C++ DS&A.
- **Do not apply to MS/PhD Waymo SWE twins with this packet.** This packet is BS Driver Refinement Foundations **8224900** only.
- Rolling as of 2026-09-25. JD: apply to each role individually; top 3.
