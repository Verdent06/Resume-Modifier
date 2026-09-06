# Apex — Simulation Software Intern (Summer 2027) · Company notes

Apply packet for Ashby posting `d3e21f84-3637-4521-833d-fd07b3ca5f2e`. **Not** the Ground Software intern twin (`2d5ad921-241f-4e7a-b9ff-9d01763da88c`). **Not** the Embedded Systems intern twin. **Not** Apex Systems staffing (`applications/2026/apex-systems/`).

Apply: https://jobs.ashbyhq.com/apex-technology-inc/d3e21f84-3637-4521-833d-fd07b3ca5f2e/application
Company intel: `applications/2027/apex/company.md` (write-once; Ground Software brief — Simulation deltas live here)
Persona (essay lens): `persona.md`
Grade: `grade.md` · Worth-it: `WORTH_IT.md` (YES, 7/10)

## What Apex is

Productized satellite buses (Aries / Nova / Comet) manufactured at Factory One, Playa Vista. Founded 2022 (Ian Cinnamon, Max Benassi). $2.3B val (Jun 2026, Reuters); JD: >$500M raised. This intern seat is **closed-loop spacecraft test** (6DOF / SITL / HITL) to V&V satellite performance — not the ground-ops stack that *operates* satellites, and not firmware. Careers page: Alvin Garcia is Director of GNC, HITL, and Mission Ops (org signal, not a named referral). Octopus is Apex's factory OS — do not claim it.

## This req vs the twins

| | Simulation Software (this packet) | Ground Software (already applied) | Embedded Systems (do not apply with this PDF) |
| --- | --- | --- | --- |
| Ashby id | `d3e21f84-3637-4521-833d-fd07b3ca5f2e` | `2d5ad921-241f-4e7a-b9ff-9d01763da88c` | different posting |
| Work | 6DOF / SITL / HITL closed-loop V&V | Ground stack that operates satellites | Firmware / microcontrollers / flight-adjacent |
| Required stack | C/C++; modeling/embedded plus | Architecture; preferred Rust/C/C++ + Vue/React | C/C++ embedded (sibling) |
| Grad window (JD text) | Fall 2026 or Spring 2027 | Fall 2027 or Spring 2028 | check that posting |
| This resume | Robotics spine + C++ real-time + test/CI analog | Full-stack + React | Do not re-package as firmware |

## Term / location / pay

- **Summer 2027 only.** JD also lists Spring 2027; Spring requires pausing academics. No season dropdown on Ashby — state Summer 2027 in Why Apex / additional info.
- Onsite Los Angeles (Playa Vista). Relocate: **Yes**.
- $45/hr. 12 weeks.
- **Eligibility (computed):** JD text Fall 2026 / Spring 2027 vs Expected May 2028 → ineligible as written. Sibling Ground Software window (Fall 2027 / Spring 2028) would pass. Form does not collect graduation date.

## Knockouts (form + JD)

1. **US Person / export control** — required Boolean. Answer **Yes** (US citizen). `No` is an auto-reject. Do not claim clearance.
2. **Graduation window** — written Fall 2026 or Spring 2027. May 2028 fails that text. Not a form field. State Expected May 2028 honestly; do not backdate.
3. **Do not invent** 6DOF, SITL, HITL, ROS, Gazebo, MATLAB/Simulink, standalone C, Octopus, satellite/flight internships, or firmware ownership.
4. **Wrong posting** — do not attach this PDF to Ground Software or Embedded Systems. Do not attach the Ground Software PDF here.

## Funnel (`companies.md` / `company.md`)

Ashby resume → recruiter → HM → practical/coding assessment (OA **unpublished** for Simulation) → LA onsite → offer. Bottleneck: resume + tech. ~5–8% **[directional]**. Embedded intern reports (sibling, directional): 2 LC-medium / 70m, then coding + light sys design + behavioral.

## Ashby form map (live GraphQL, 2026-09-06)

Form id `b68f080c-92a4-4085-bc85-bee890318f2f`. Same org form as Ground Software.

**About You:** Full Name*, Preferred First Name, Resume*, Email*, Phone*, Location*, Current Employer (opt).
**Links:** LinkedIn URL*, GitHub URL (opt).
**Export Control Eligibility:** US Person?* (Boolean).
**Why Apex:** Why Apex? (opt LongText); Additional Information / cover letter (opt LongText).
**EEO surveys:** optional — skip for volume (`recruiting.md` Part I §2).

No internship-season checkbox. No GPA field (GPA is on the PDF). No sponsorship question beyond US Person. No graduation-date picker.

## What wins on this page

Persona: C++ through use; real-time / deterministic / test-verify in the top half; no invented SITL/HITL/ROS; not firmware-led; not the Ground Software React spine. Shipped PDF: CaseStudyPrep real-time, Granular C++, MDC Flask/EC2, SignalWeaver FastAPI+CI. Binding dings live in `grade.md` (Granular metric-free; Vylet PE/LangGraph skim; SignalWeaver financial/MPNet).
