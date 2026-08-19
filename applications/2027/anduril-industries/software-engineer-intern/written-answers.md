# Anduril Industries — 2027 Software Engineer Intern (Seattle, onsite) · Written Application Answers

Draft answers for Greenhouse token `5148079007`. Grounded in `persona.md` (full-stack spine + autonomy / mission-critical defense differentiator), `grade.md` Interview angles, and real `context.md` work only. First-person, honest, defensible under "walk me through this."

**Do not invent:** Snowflake, Databricks, Copilot, Fusion, Tableau, Go, Rust, Java, ROS, Lattice internships, sensor-fusion internships, clearance in hand, or Granular latency/xrun/CPU/user numbers.

Apply: https://boards.greenhouse.io/embed/job_app?token=5148079007
Jobright: https://jobright.ai/jobs/info/6a2a29e72cde2824469c0471
Resume: `applications/2027/anduril-industries/software-engineer-intern/Vedant Desai Resume.pdf`

This posting is a **generic 2027 SWE intern catch-all** (Atlanta, Boston, Costa Mesa, Irvine, Reston, Seattle). Recruiter outreach when a matching team opens. **Seattle is the location to select.** Review begins August 2026 for Summer 2027.

---

## Knockout / structured fields (fill exactly)

| Field | Answer |
| --- | --- |
| First / Last name | Vedant Desai |
| Email | vedantde@umich.edu |
| Phone | (248) 704-4852 |
| Country | United States |
| School | University of Michigan |
| Degree | Bachelor's |
| Discipline | Computer Science (also Economics — pick CS if only one) |
| End date | May 2028 |
| LinkedIn | https://linkedin.com/in/vedantde06 |
| Website | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/anduril-industries/software-engineer-intern/Vedant Desai Resume.pdf` |
| Cover Letter | Optional on Greenhouse. Paste the letter below if attaching/entering manually. |
| Are you willing to work in-person for 12 weeks during the internship? | **Yes** |
| What is your top location preference? | **Seattle, Washington** |
| Will you be returning to school at the end of the internship to continue academic studies for at least one quarter/semester? | **Yes** — Fall 2027 and Winter 2028 remain after Summer 2027 (Expected May 2028) |
| EXPORT CONTROLS / U.S. Person / "protected individual" (8 U.S.C. 1324b(a)(3)) | Answer **truthfully**. This JD requires **U.S. Person** status (export-controlled data), not a clearance in hand. Other 2027 defense applications in this repo treat you as a **U.S. citizen**. If that is true: check U.S. citizen / U.S. Person. If it is not, stop — this is an auto-reject, not a resume problem. Do not guess. `context.md` has no citizenship field. |
| Are you authorized to work in the United States? | **Yes** if that is true (same honesty rule as above). |
| Will you require sponsorship from Anduril for employment now or in the future (e.g. H-1B)? | **No** if you are a U.S. citizen / do not need a visa. Do not guess. |
| How did you hear about Anduril? | **Jobright**. If Jobright is not listed: **Other** → Jobright. |
| If other, please specify | Jobright (https://jobright.ai/jobs/info/6a2a29e72cde2824469c0471) |
| GPA (only if asked) | **3.66 / 4.0** |
| Languages you can interview in | **C++, Python, TypeScript/JavaScript (Angular), SQL**. Do **not** check Go, Rust, or Java. |

---

## Cover letter (paste)

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

Anduril Industries — 2027 Software Engineer Intern
Seattle, WA (onsite)

Dear Anduril recruiting team,

I am applying for the Summer 2027 Software Engineer intern role, with Seattle as my top location. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I can work in person for the full 12-week term, and I return to Michigan afterward.

Anduril ships software that other people depend on in the field — Lattice, autonomy, sensor fusion — and this intern job is the generic SWE version of that: write code on deployed products, scale capability, debug with metrics, and root-cause failures. That is the work I already do. I do not have a defense internship. I do have production ownership, operational debugging, and C++ that cannot miss a real-time deadline.

What I would bring:

- **Debug and root-cause on a live product.** At CaseStudyPrep.AI I eliminated a 27% audio-upload failure rate with fault-tolerant RxJS that regenerates expired S3 presigned URLs mid-flight and negotiates MIME types Angular was silently rejecting. I moved audio processing off the UI thread into a Web Worker, holding main-thread blocking under 5ms at 60 FPS, and cut cloud inference cost 40% by running Silero VAD client-side via ONNX Runtime so dead air never hit Whisper.
- **C++ under a hard constraint.** I built a granular synthesizer plugin in C++/JUCE whose `processBlock()` path cannot allocate or take a lock. A per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO with atomic acquire/release keep the audio thread off the heap and off mutexes. I ship VST3/AU from one CMake codebase after a real-time safety audit (zero heap, zero locks). github.com/Verdent06/granular-synth
- **Shipped Python services, sole owner.** As the only engineer on a five-month Michigan Campaign Finance Network contract I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL across 400 tracked committees and delivered a production Flask REST API on AWS EC2. At Vylet (live product, $1,500 MRR) I Dockerized a LangGraph pipeline on Redis/Celery and fixed a name-collision defect that lifted lead-qualification from 79% to 89%.

I have not shipped Go, Rust, or Java. I interview in C++ and Python. I want the Seattle intern seat writing and debugging software that has to work, not a generic feature-factory rotation.

Sincerely,
Vedant Desai

---

## If the recruiter asks "Why Anduril / why Seattle?" (≈90 words)

I want to write software that is deployed to people who depend on it, then debug it when it fails — the intern posting's actual job, and Anduril's product shape (Lattice, fielded autonomy). Seattle is my top site. Closest analog I have: CaseStudyPrep (27% upload-failure recovery, on-device VAD, sub-5ms UI-thread offload) and C++ that cannot allocate on the audio thread. I do not have ROS, computer vision, or a defense internship. I have production ownership and real-time systems discipline, and I will ramp on the team's stack (including Go/Rust/Java) rather than claim them.

---

## If they ask "Tell us about a project / a time you rooted a failure"

**CaseStudyPrep.AI (operational debug).** Audio uploads failed 27% of the time. Root cause: expired S3 presigned URLs plus Angular rejecting WAV MIME types. I added RxJS retry that regenerates URLs mid-flight and negotiates MIME types. Same product: most Whisper frames were dead air, so Silero VAD on-device via ONNX cut inference cost 40%.

**Granular (systems constraint).** The audio callback cannot heap-allocate or take a lock. I pre-allocate `MemoryPool<Grain, 64>` per voice and a lock-free SPSC FIFO so UI changes never block `processBlock()`. I have no callback-latency / xrun / CPU number — I would measure those next; the constraint I actually enforced is zero heap and zero locks after `prepareToPlay()`.

**Vylet (ownership / bias for action).** Name-collision in ownership verification was rejecting valid targets. Fix lifted qualification 79% → 89% with no change in sourcing volume.

---

## Availability

Summer 2027, paid, **onsite Seattle**, 12 weeks. Available to start May 2027. Returning to the University of Michigan after the internship (Expected May 2028). GPA 3.66.

---

## Notes for the applicant (not for submission)

- **This is the same Greenhouse req already pipelined** (`company.md` cites token 5148079007). Track: full-stack + autonomy / mission-critical defense. Score 8.0 / 10. Do not re-tailor for "robotics intern."
- **Do not claim Go, Rust, Java, ROS, Lattice, sensor fusion, Snowflake, Databricks, Copilot, Fusion, or Tableau.** JD names Go/Rust/Java as a proficiency set; inventory does not have them (`grade.md` Defend).
- **Do not invent a Granular runtime metric.** Pool has no xrun / callback-latency / CPU / user count.
- **U.S. Person is a form knockout**, not a resume line (`persona.md` Team & Bar). Answer honestly. Jobright's "U.S. Citizen Only" tag is stricter than the JD's U.S. Person language (citizen, LPR, asylee, or refugee all qualify as U.S. Persons).
- **Cover letter is optional.** Attach it; the PDF is the screen. Binding filters after that: Medium HackerRank, then 4-hour practical Super Day (`companies.md`: bottleneck 4-hr onsite, ~3–5%).
- **Referral:** none in `network.md`. A real Anduril name beats Jobright; a fake name is a knockout.
- **Location:** pick **Seattle** only as top preference. Other listed cities are on the same catch-all req; do not split the difference on the form.
