# General Matter — Summer 2027 Internship - Embedded Software Engineering · Written Application Answers

Approved copy for Greenhouse job **5377131008**. Dropdown labels captured from `https://boards-api.greenhouse.io/v1/boards/generalmatter/jobs/5377131008?questions=true` on 2026-09-03. Grounded in `persona.md` (C++/Python low-level adjacency, no fabricated firmware), `grade.md` Interview angles (proudest = reliability / real-time story), and `context.md` metrics only.

**Do not invent:** Granular xrun / callback-latency / CPU; MDC API traffic or latency; firmware, MCUs, PLC/SCADA, oscilloscopes, Rust, nuclear, or active clearance; Fall 2026 or Spring 2027 availability; Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry.

**Do not submit from this run.** Artifacts only. No website apply.

Apply: https://job-boards.greenhouse.io/generalmatter/jobs/5377131008
Resume: `applications/2027/general-matter/embedded-software-engineering-intern/Vedant Desai Resume.pdf`
SHA256: `661280e34cec0fd35d526d494b99757e3a036d34e5dd9f21717be28769a24660` (1 page; verified 2026-09-03)
Transcript: **required.** Unofficial OK. Recent UMich transcript is available externally to the apply worker — attach that file. Do not skip this field.

**Form email is `verdent06@gmail.com` only.** Never `vedantde@umich.edu` on this Greenhouse form. The PDF header still shows the school address from `context.md` / the template; that is the document. The form field is Gmail.

---

## Worker notes (fill, do not skip)

| Field | Answer |
| --- | --- |
| First Name * | Vedant |
| Last Name * | Desai |
| Preferred First Name | (leave blank) |
| Email * | **verdent06@gmail.com** (only). Do not use `vedantde@umich.edu` if the form rejects personal mail — stop and flag; do not switch emails on this packet. |
| Country | United States |
| Phone * | (248) 704-4852 |
| Location (City) * | Ann Arbor, MI (school). Mailing used on other 2027 apps: Northville, MI. Do not invent a zip if the widget is city-only. |
| Resume/CV * | `applications/2027/general-matter/embedded-software-engineering-intern/Vedant Desai Resume.pdf` |
| Cover Letter | Optional — leave blank. PDF is the screen. |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 |
| School * | University of Michigan |
| Degree * | Bachelor's |
| Discipline * | Computer Science (dual CS + Economics — pick CS if one) |
| Education end | May 2028 |
| Education start | Unknown in `context.md` — do **not** invent a month/year. Leave blank if the widget allows; otherwise use the real UMich start from the transcript you attach. |
| GPA * | **3.66** |
| Academic Transcript * | **Required.** Attach the recent unofficial UMich transcript the apply worker already has. Unofficial transcripts are acceptable. |
| What year do you intend to complete your degree? * | **2028** |
| Do you have, or are you currently pursuing, a college degree? * | **Yes** |
| Are you legally authorized to work in the United States? * | **I am authorized to work in the United States for any employer** |
| When are you available for a 12 week internship? * | Check **Summer 2027** only. Do **not** check Fall 2026 or Spring 2027. Must be available the full 12 weeks. |

---

## Required dropdowns (exact option text)

### Clearance Eligibility *

**Select: `Yes`**

Live options on **5377131008** (single-select) — **not** the SWE intern (5377118008) three-way list:

- `Yes` — **select this** (U.S. citizen; never held a clearance; eligible to obtain/maintain one)
- `No` — knockout for a role that may require eligibility to obtain/maintain a U.S. clearance

Do not claim an active clearance. `Yes` here means eligibility, not that he holds a clearance. Pair with **Never held a clearance** below. Use the optional clarify box so they do not read `Yes` as "I currently hold a clearance."

### Active Security Clearance(s) *

**Select: `Never held a clearance`** (multi-select; pick this one only)

Live options:

- `Top Secret SCI with Polygraph`
- `Top Secret SCI/SAP`
- `Top Secret`
- `DOE Level Q`
- `Secret`
- `Expired Clearance`
- `Never held a clearance` — **select this**
- `Do not wish to disclose`

Do not check Secret, Q, TS, Expired, or Do not wish to disclose.

### Confirm that you will be able to commute to and from our HQ in the South Bay Area of Los Angeles through your full internship duration. *

**Select: `Yes`**

Live options: `Yes` / `No`

He can relocate for summer internships. This is a term-commute yes, not a claim he already lives in LA. Use the optional clarify box so they do not read it as "I already commute from the South Bay."

---

## Optional: Please use this space if you would like to clarify any answers above

Paste:

I am a U.S. citizen. I have never held a U.S. security clearance. Clearance Eligibility = Yes means I am eligible to obtain and maintain one if this internship requires it — not that I currently hold a clearance. I am authorized to work in the United States for any employer and do not need sponsorship.

I live in Michigan during the school year (University of Michigan, Ann Arbor; Expected May 2028). I will relocate to the South Bay / Los Angeles for the full 12-week Summer 2027 internship so I can commute to HQ daily. I am available Summer 2027 only — not Fall 2026 or Spring 2027.

---

## Tell us about your proudest accomplishment * (paste)

At CaseStudyPrep.AI I was a Software Engineer Co-op on a live voice-AI product (Dec 2025–May 2026). My proudest work was turning a production reliability failure into a system that recovered in flight and stayed inside a real-time budget — diagnosing a live failure, putting a recovery path in, and keeping the hot path off the thread that cannot miss.

Audio uploads were failing 27% of the time. Root cause: S3 presigned URLs expired mid-session, and Angular silently rejected WAV MIME types. I wrote fault-tolerant RxJS that detects expired URLs, regenerates them in-flight, and negotiates MIME types. That eliminated the 27% failure mode.

Same product: most frames sent to Whisper were dead air. I ran Silero VAD client-side via ONNX Runtime so silence never hit the cloud, cutting inference cost 40%. I moved audio processing off the UI thread into a Web Worker with an async stream handoff, holding main-thread blocking under 5ms and the visualizer at 60 FPS during inference.

Separately, the C++ real-time work on my resume is a granular-synth plugin: a zero-allocation audio thread (`processBlock` never heap-allocates after setup), a lock-free SPSC UI-to-audio FIFO, and a CMake release audit that every hot-path has zero heap allocations and zero lock acquisitions. I do not have a firmware, MCU, PLC, or nuclear internship, and I do not have a measured callback/xrun/CPU number for that plugin. What I can defend is the constraint and the checklist.

---

## Notes for the applicant / worker (not for submission)

- **Transcript is a hard form gate.** Greenhouse help text: transcripts required for all applicants; unofficial acceptable; they look at relevant coursework and grade trends. Attach the recent UMich transcript the apply worker has. Do not submit without it.
- **Proudest is CaseStudyPrep numbers, plus an honest Granular sentence.** `grade.md` says frame this box as a reliability/real-time story. Granular is the C++ differentiator on the PDF but has no allowlisted xrun/latency/CPU metric — do not invent one. Vylet ($1,500 MRR, 79%→89%) is ownership, off-mission for enrichment control. MDC (~800 hours / 400 PACs) has no API traffic/latency number.
- **Do not analogize so hard it sounds like plant-control or firmware.** Voice-AI recovery ≠ enrichment control loops. Granular audio thread ≠ MCU firmware. The mapping is *kind of engineering* (real-time constraint, fault tolerance, systems debugging).
- **Clearance on this req is Yes/No**, unlike SWE intern 5377118008 (`Yes, I am eligible for a U.S. security clearance`). Pick `Yes` + `Never held a clearance`. DOE Q is on the active-clearance list because this is a nuclear-fuel company — still do not check it.
- **Availability:** Summer 2027 checkbox only.
- **Email:** `verdent06@gmail.com` only on this form.
- **Referral:** none in `network.md`. Do not invent a General Matter name.
- **Binding filters after submit:** human Greenhouse PDF screen, then unpublished coding/systems loop (`grade.md`). Honest C++ adjacency can clear a human read; a firmware-first screener who wants MCU/lab time can still no-pile.
- Cover letter is optional; skip it. This box plus the PDF carry the screen.

## Knockout / filter checklist

| Gate | Risk | What to do |
| --- | --- | --- |
| Academic Transcript * | Form knockout if missing | Attach unofficial UMich transcript (worker has a recent copy) |
| Clearance Eligibility * `No` | Form knockout | Select `Yes` (eligibility). Never held. |
| Active clearance claimed | Fabrication | `Never held a clearance` only |
| South Bay commute `No` | Form knockout | `Yes` + clarify relocate for summer |
| Fall 2026 / Spring 2027 checked | Availability lie | Summer 2027 only |
| Sponsorship required | Work-auth knockout | Any-employer option; US citizen, no sponsorship |
| Resume claims firmware / Rust / MCU / nuclear | Screen reject + integrity | PDF does not; do not type them into the form |
| `vedantde@umich.edu` on this form | Packet rule | Use `verdent06@gmail.com` only |
