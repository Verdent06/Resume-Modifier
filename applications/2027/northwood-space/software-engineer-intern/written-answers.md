# Northwood Space — Software Engineering Intern (2027 Summer Internship) · Written Application Answers

Draft answers for Ashby job `ce3d4b73-461e-4128-a6f1-f933897e8119`. Grounded in `persona.md` (full-stack spine + space-infra / ground-station data-plane / distributed-systems differentiator), `grade.md` Interview angles, and real `context.md` inventory only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Rust, Golang, Terraform, FPGA/firmware, C (as distinct from C++), clearance in hand, Granular latency/xrun/CPU/user numbers, a Northwood referral, graduation 2029.

**Do not submit from this file.** Artifacts only; no website apply.

Apply: https://jobs.ashbyhq.com/NorthwoodSpace/ce3d4b73-461e-4128-a6f1-f933897e8119/application
Resume: `applications/2027/northwood-space/software-engineer-intern/Vedant Desai Resume.pdf`

This is the **Software Engineering Intern** (data-plane / networking / distributed systems), **not** the Embedded Software Engineering Intern posting. Torrance, 5 days/week, $36/hr, Summer 2027.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| Legal Name (First Last) * | Vedant Desai |
| Preferred Name | Vedant |
| Email * | **verdent06@gmail.com** only. Never `vedantde@umich.edu` on this form. (The PDF header is still the locked template address; Ashby must be gmail.) |
| Phone Number * | (248) 704-4852 |
| Resume * | `applications/2027/northwood-space/software-engineer-intern/Vedant Desai Resume.pdf` |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Website/Portfolio | https://github.com/Verdent06/granular-synth (highest-signal for this req). Extra if the field allows two: https://github.com/Verdent06 and https://vyletdata.com. Do not invent a portfolio PDF. |
| School / degree (if asked) | University of Michigan · B.S. Computer Science and Economics · GPA **3.66 / 4.0** · Expected **May 2028** |
| Class standing | Junior at apply; Summer 2027 is junior-year summer / rising senior. Returning Fall 2027 and Winter 2028. |
| Languages you can interview in | **C++, Python, TypeScript/JavaScript (Angular), SQL**. Do **not** check Rust, Golang, Terraform, FPGA, or C. |

Voluntary EEO / race / gender / veteran / disability: skip (`recruiting.md` Part I §2). Do not invent.

---

## Share a project you're especially proud of and explain what made your contribution meaningful (2-3 sentences or bullet points) *

Paste this. Granular is the `grade.md` lead: C++ systems / real-time constraint — the only JD language in inventory (`persona.md`: C++ in bullets, not Skills-only; do not collapse into embedded/firmware).

I built a C++/JUCE real-time audio engine whose `processBlock()` callback cannot allocate or take a lock — a missed deadline is an audible glitch, not a retry. I pre-allocated a `MemoryPool<Grain, 64>` slab per voice so grain slots come off a free-list (`processBlock()` never calls `new`/`delete` after `prepareToPlay()`), and a 64-slot lock-free SPSC FIFO with atomic acquire/release so slider changes never block the audio thread. I shipped VST3 and AU from one CMake codebase after auditing every `processBlock()` path for zero heap allocations and zero lock acquisitions. github.com/Verdent06/granular-synth

If they want a production data-movement story instead (same 2–3 sentence cap), swap in CaseStudyPrep — do not paste both into the box:

At CaseStudyPrep.AI I closed a 27% audio-upload failure rate: expired S3 presigned URLs and Angular MIME rejection were dropping WAV files mid-session. I wrote fault-tolerant RxJS that regenerates expired URLs in-flight and negotiates MIME types the client had silently rejected, and I moved audio processing off the UI thread into a Web Worker so main-thread blocking stayed under 5ms at 60 FPS.

---

## How did you hear about this job? *

**Jobright.**

No Northwood contact in `network.md` — do not invent a referral or employee name. If the box wants a sentence: Jobright (job board).

---

## What is the earliest date you are available to start this position? *

**May 2027.** Date picker: **2027-05-17** as the conventional Summer 2027 intern start used on other packets. Do not pick a 2026 date. Do not invent a Winter 2027 finals day; if you will still be in Ann Arbor that week, slide the picker to the first Monday you can actually be in Torrance.

---

## This role requires working in person at our Torrance, CA office five days per week. Does this work for you? *

**Yes.**

---

## Export Control Eligibility *

Select: **A United States citizen or national**

Live options (single-select): United States citizen or national · lawful permanent resident · refugee under 8 U.S.C. 1157 · asylee under 8 U.S.C. 1158 · None of the Above.

ITAR is a binary knockout (`persona.md` Team & Bar; `recruiting.md` Part I §1). Do not pick None of the Above.

---

## Are you authorized to work in the U.S.? *

**Yes**

---

## Will you require sponsorship from Northwood for employment now or in the future (i.e. H1-B visa) *

**No**

---

## Notes for the applicant (not for submission)

- **This is general SWE, not embedded.** FPGA is "collaborate with," not intern work (`persona.md` Role Summary). Do not volunteer firmware, HDL, or the Embedded Software intern req.
- **Do not claim Rust, Golang, Terraform, or FPGA.** Inventory has C++ among the JD languages; AWS and Docker are pluses already on the PDF (`grade.md` Defend).
- **Do not invent a Granular runtime metric.** Pool has no xrun / callback-latency / CPU / user count. If they probe impact, narrate the safety checklist and what you would measure next.
- **No TCP/IP on the page.** Networking-adjacent stories: S3/presigned-URL recovery and lock-free UI-to-audio handoff (`grade.md` Defend). Do not fake socket/TCP coursework.
- **If they ask about Vylet:** Docker/Redis/Celery workers and the 79%→89% defect fix — not the PE/agentic product story (`grade.md`).
- **Cover letter:** none on this Ashby form. Do not attach one.
- **Referral:** none in `network.md`. A real Northwood name beats Jobright; a fake name is a knockout (`recruiting.md` Part I §4).
- **Binding filters after apply:** Ashby human resume screen, then an unpublished intern tech loop — do not assume HackerRank (`companies.md` / `grade.md`).
- **Email:** Ashby = `verdent06@gmail.com`. Never `vedantde@umich.edu` on this application.
