# Lyft — Software Engineer Intern, Backend (Summer 2027) · Written Application Answers

Draft answers for CareerPuck / Greenhouse `gh_jid=8767726002` (posting ID 111132). Grounded in `persona.md` (full-stack spine, rideshare marketplace / realtime-backend lens) and `context.md` identity/inventory only. First-person, honest, defensible. Do not invent tools, metrics, Go, mobile apps, or rideshare-domain internships.

**Form email MUST be `verdent06@gmail.com`. Never `vedantde@umich.edu`.** Phone **248-704-4852**. US citizen, no sponsorship. Address **49032 Freestone Dr, Northville, MI 48168**, ZIP **48168**. Junior, Expected May 2028, GPA **3.66**. LinkedIn https://linkedin.com/in/vedantde06 · GitHub https://github.com/Verdent06.

**Do not submit from this agent.** Packet log only. No Lyft contacts in `network.md` — do not mark referral.

Apply: https://app.careerpuck.com/job-board/lyft/job/8767726002?gh_jid=8767726002
Resume: `applications/2027/lyft/software-engineer-intern-backend/Vedant Desai Resume.pdf`

---

## Knockouts (read first)

1. **Graduation window.** Role requires bachelor's or master's graduation between December 2027 and Summer 2028. Expected **May 2028**. **Yes. Clears.**
2. **Degree.** Currently pursuing B.S. Computer Science (and Economics), University of Michigan. **Yes.**
3. **Summer 2027 in San Francisco.** Available; will relocate for hybrid Mon/Wed/Thu. **Yes.**
4. **Work authorization.** US citizen. No sponsorship now or later. **Authorized / No sponsorship.**
5. **Essential functions (hybrid 3 days/week SF).** Can perform with or without reasonable accommodation. **Yes.**
6. **Prior Lyft employment.** None. **No.**

Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not lie on sponsorship, graduation month, or SF hybrid.

---

## Basic Information

| Field | Answer |
| --- | --- |
| First Name* | Vedant |
| Last Name* | Desai |
| Email* | **verdent06@gmail.com** |
| Country* | United States |
| Phone* | 248-704-4852 |
| Location (City)* | Northville, MI (current). Do not spoof a San Francisco home address; relocation is answered below. |
| Resume/CV* | `applications/2027/lyft/software-engineer-intern-backend/Vedant Desai Resume.pdf` |
| LinkedIn Profile | https://linkedin.com/in/vedantde06 |
| Zip / postal code* | **48168** |

---

## Employment History

Add each row with **+ Add Another Employment**. Dates are month/year from `context.md`. Check **current role** only on Vylet.

| Company name | Title | Start | End | Current? |
| --- | --- | --- | --- | --- |
| Vylet | Founder | May 2026 | Present | Yes |
| Michigan Data Consulting (MDC) | Data Engineer — Michigan Campaign Finance Network | Jan 2026 | May 2026 | No |
| CaseStudyPrep.AI | Software Engineer Co-op (Voice AI) | Dec 2025 | May 2026 | No |
| Lyndbrook Capital | Data Engineering Consultant | Feb 2026 | Apr 2026 | No |

Do not invent Lyft, internships, or titles not in `context.md`.

---

## Education & Eligibility

| Field | Answer |
| --- | --- |
| Current University* | University of Michigan |
| Anticipated graduation month and year* | **May 2028** (inside December 2027–Summer 2028) |
| Please enter your relevant employment and military service above using the + Add Another Employment link.* | Done — rows above |
| May we contact your current employer?* | **No** — current role is self-founded (Vylet). Prior employers: MDC and CaseStudyPrep.AI have ended; contact if they insist after an offer, not while those are listed as past. |
| Can you perform these essential functions of the job with reasonable accommodation?* | **Yes** (hybrid Mon/Wed/Thu in San Francisco) |
| Please describe any need for a reasonable accommodation for this hiring process | Leave blank unless you actually need one. |

---

## Work Authorization & Legal

| Field | Answer |
| --- | --- |
| Work Authorization* | **US citizen; legally authorized to work in the United States; will not require sponsorship now or in the future** |
| Lyft Candidate Privacy Policy (United States) | Acknowledge / agree |
| Please share your gender pronouns.* | If the field is required and open-text: **he/him**. If skippable, skip. |
| Have you been employed by Lyft, or any subsidiary, affiliate, or business unit of Lyft, in the past?* | **No** |
| This position is based in the United States. Do you currently reside in commutable proximity to our Lyft Office located in San Francisco or are you open to relocating?* | **Open to relocating** to San Francisco for Summer 2027 (hybrid Mon/Wed/Thu). Current residence: Northville, MI 48168. |

---

## Certification

| Field | Answer |
| --- | --- |
| Electronic signature (full name) | Vedant Desai |
| Today's date | **2026-09-13** |

Voluntary self-ID: **skip** unless the form blocks submit without it.

---

## If a free-response "Why Lyft" / "Why backend" appears

I want to work on backend that has to be correct while two sides of a marketplace are live — matching, location, and the APIs that actually move a driver or a passenger. I have not interned at a rideshare company and I will not pretend I have. What I can defend:

- **Shipped APIs and a database.** Sole engineer on a 5-month Michigan Data Consulting contract: Requests/Pandas ETL that replaced about 800 hours of manual pulls across 400 PACs, plus a production Flask REST API on AWS EC2. At Vylet I wrote an asyncpg data-access layer with injection-safe SQL freshness checks and Redis/Celery workers on a recurring cycle (30 scored leads in 30 minutes).
- **Reliability when something fails.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate by regenerating expired S3 URLs mid-flight. At Vylet I diagnosed a name-collision in ownership verification that was dropping valid leads; the fix moved qualification from 79% to 89% with no change in sourcing volume.
- **Real-time constraints.** I moved CaseStudyPrep audio off the UI thread (under 5ms blocking, 60 FPS visualizer). Separately I built a C++/JUCE audio plugin whose `processBlock()` path cannot allocate or take a mutex (github.com/Verdent06/granular-synth). That is not dispatch software — it is the closest I have to "the deadline is the product."
- **Testing / CI as how work ships.** SignalWeaver runs pytest and an image build on GitHub Actions (frontend build, pytest, API image on main). I do not have a load-test suite on the Flask or Redis services; I would not claim otherwise.

I can be in the San Francisco office Monday/Wednesday/Thursday next summer. I do not need immigration sponsorship. No one at Lyft referred me.

---

## Notes for the applicant (not for submission)

- **Do not claim Go, Kafka, Envoy, mobile, or OSS contributions to Envoy.** Not in inventory.
- **Do not invent load tests or rideshare matching projects.**
- **Email on every field:** verdent06@gmail.com.
- **Cover letter:** not listed as required on this form; skip unless the flow blocks without one.
- **Behavioral:** MDC sole-engineer scoping; CaseStudyPrep 27% upload recovery; Vylet 79%→89% defect; Granular zero-alloc audio thread.
