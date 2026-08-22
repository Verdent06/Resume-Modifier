# General Matter — Summer 2027 Internship - Software Engineering · Written Application Answers

Approved copy for Greenhouse job **5377118008**. Dropdown labels captured from `https://boards-api.greenhouse.io/v1/boards/generalmatter/jobs/5377118008?questions=true` on 2026-08-22. Grounded in `persona.md` (reliability / real-time / C++-Python systems), `grade.md` Interview angles (proudest = reliability story), and `context.md` metrics only.

**Do not invent:** Granular xrun / callback-latency / CPU / user counts; MDC API traffic or latency; active clearance; Fall 2026 or Spring 2027 availability; a nuclear/control-systems internship.

**Do not submit from this run.** Artifacts only. No website apply.

Apply: https://job-boards.greenhouse.io/generalmatter/jobs/5377118008
Resume: `applications/2027/general-matter/software-engineer-intern/Vedant Desai Resume.pdf`
Transcript: Drive GrokBot `frstyr_transcript.pdf` (unofficial OK)

---

## Worker notes (fill, do not skip)

| Field | Answer |
| --- | --- |
| First Name | Vedant |
| Last Name | Desai |
| Preferred First Name | (leave blank) |
| Email | **verdent06@gmail.com**. If the form rejects personal mail or a later step requires `.edu`: **vedantde@umich.edu**. GM Greenhouse does not require `.edu`. |
| Country | United States |
| Phone | (248) 704-4852 |
| Location (City) | Ann Arbor, MI (school). Mailing used on other 2027 apps: Northville, MI. Do not invent a zip if the widget is city-only. |
| Resume/CV * | `applications/2027/general-matter/software-engineer-intern/Vedant Desai Resume.pdf` |
| Cover Letter | Optional — leave blank. PDF is the screen. |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 |
| School | University of Michigan |
| Degree | Bachelor's |
| Discipline | Computer Science (dual CS + Economics — pick CS if one) |
| Education end | May 2028 |
| Education start | Unknown in `context.md` — do **not** invent a month/year. Leave blank if the widget allows; otherwise use the real UMich start from his transcript. |
| GPA * | **3.66** |
| Academic Transcript * | Attach Drive GrokBot **`frstyr_transcript.pdf`** (unofficial acceptable). |
| What year do you intend to complete your degree? * | **2028** |
| Do you have, or are you currently pursuing, a college degree? * | **Yes** |
| Are you legally authorized to work in the United States? * | **I am authorized to work in the United States for any employer** |
| When are you available for a 12 week internship? * | Check **Summer 2027** only. Do **not** check Fall 2026 or Spring 2027. Must be available the full 12 weeks. |

---

## Required dropdowns (exact option text)

### Clearance Eligibility *

**Select: `Yes, I am eligible for a U.S. security clearance`**

Live options (single-select):

- `Yes, I hold an active U.S. security clearance` — **do not select** (no clearance history)
- `Yes, I am eligible for a U.S. security clearance` — **select this** (U.S. citizen; never held a clearance)
- `No`

Do not claim an active clearance. Do not pick `No` — that is a knockout for a role that may require eligibility to obtain/maintain a U.S. clearance (`persona.md` / form help text).

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

Do not check Secret, Q, TS, or Expired.

### Confirm that you will be able to commute to and from our HQ in the South Bay Area of Los Angeles through your full internship duration. *

**Select: `Yes`**

Live options: `Yes` / `No`

He can relocate/travel for summer internships. This is a term-commute yes, not a claim he already lives in LA. Use the optional clarify box below so they do not read it as "I already commute from the South Bay."

---

## Optional: Please use this space if you would like to clarify any answers above

Paste:

I am a U.S. citizen. I have never held a U.S. security clearance and I am eligible to obtain and maintain one if this internship requires it. I am authorized to work in the United States for any employer and do not need sponsorship.

I live in Michigan during the school year (University of Michigan, Ann Arbor; Expected May 2028). I will relocate to the South Bay / Los Angeles for the full 12-week Summer 2027 internship so I can commute to HQ daily. I am available Summer 2027 only — not Fall 2026 or Spring 2027.

---

## Tell us about your proudest accomplishment * (paste)

At CaseStudyPrep.AI I was a Software Engineer Co-op on a live voice-AI product (Dec 2025–May 2026). My proudest work was turning a production reliability failure into a system that recovered in flight and stayed inside a real-time budget — the same class of problem this intern role screens for (reliability, performance, software other disciplines will depend on).

Audio uploads were failing 27% of the time. Root cause: S3 presigned URLs expired mid-session, and Angular silently rejected WAV MIME types. I wrote fault-tolerant RxJS that detects expired URLs, regenerates them in-flight, and negotiates MIME types. That eliminated the 27% failure mode.

Same product: most frames sent to Whisper were dead air. I ran Silero VAD client-side via ONNX Runtime so silence never hit the cloud, cutting inference cost 40%. I moved audio processing off the UI thread into a Web Worker with an async stream handoff, holding main-thread blocking under 5ms and the visualizer at 60 FPS during inference.

I do not have a nuclear or control-systems internship. What I can defend is diagnosing a live failure, putting a recovery path in, and keeping the hot path off the thread that cannot miss.

---

## Notes for the applicant / worker (not for submission)

- **Proudest is CaseStudyPrep, not Granular or Vylet.** `grade.md` says frame this box as a reliability/real-time story. Granular is the C++ differentiator on the PDF but has no allowlisted xrun/latency/CPU metric — do not invent one here. Vylet ($1,500 MRR, 79%→89%) is ownership, off-mission for enrichment. MDC (~800 hours / 400 PACs) has no API traffic/latency number.
- **Do not analogize so hard it sounds like plant-control software.** Voice-AI recovery ≠ enrichment control loops. The mapping is *kind of engineering* (fault tolerance, real-time constraint).
- **Clearance:** eligible + never held. DOE Q is on the active-clearance list because this is a nuclear-fuel company — still do not check it.
- **Availability:** Summer 2027 checkbox only.
- **Referral:** none in `network.md`. Do not invent a General Matter name.
- **Binding filters after submit:** human Greenhouse PDF screen, then unpublished coding/systems loop (`grade.md`). Transcript is required.
- Cover letter is optional; skip it. This box plus the PDF carry the screen.
