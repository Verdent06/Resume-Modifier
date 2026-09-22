# GE HealthCare — intern notes (Software Engineering Summer Intern 2027, Salt Lake City)

Intern-facing packet notes for Workday **R4046481**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What GE HealthCare builds

Nasdaq: **GEHC** (Jan 2023 GE spinoff). Medical technology: imaging, ultrasound, patient-care solutions, pharmaceutical diagnostics. ~$20.6B / ~54k colleagues (Extern 2026, directional). This intern is **OEC Medical Systems, Salt Lake City** — Surgery Imaging / mobile C-arm software (test, defect triage, V&V), **not** EEDP Waukesha, **not** GE Vernova, **not** GE Aerospace.

## This req

- **Title:** Software Engineering Summer Intern 2027 · Salt Lake City, UT · Workday `timeType` **Full time**
- **ATS:** Workday **R4046481** · hiring org **F39055 OEC Medical Systems, Inc.**
- **JD:** https://gehc.wd5.myworkdayjobs.com/GEHC_ExternalSite/job/Salt-Lake-City/Software-Engineering-Summer-Intern-2027_R4046481-1
- **Apply:** https://gehc.wd5.myworkdayjobs.com/GEHC_ExternalSite/job/Salt-Lake-City/Software-Engineering-Summer-Intern-2027_R4046481-1/apply
- **CXS:** https://gehc.wd5.myworkdayjobs.com/wday/cxs/gehc/GEHC_ExternalSite/job/Salt-Lake-City/Software-Engineering-Summer-Intern-2027_R4046481-1
- **Posted:** 2026-09-21 · no `endDate` — first wave (`recruiting.md` Part II §8)
- **Work:** automated test frameworks / regressions on Surgery Imaging sub-components; defect triage; V&V; reliability analysis; peer code reviews; design/requirements docs
- **Comp:** unpublished on this JD. Relocation assistance **Yes**. Term length unpublished (do not copy EEDP's 10-week minimum onto the form unless asked)
- **Not:** EEDP Software intern (Waukesha; Java/C++/Python required) · Hardware Intern · Electrical Engineering intern at the same SLC site
- **Apply path:** Workday. Create Account wall on Autofill and Apply Manually. Questionnaire `d6f9802f922a100197d14d8073960000` and later wizard pages **HTTP 406** without an account — do not invent Application Questions wording

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| No languages on **R4046481** | Python, C++, SQL through use |
| Automated test / regressions | SignalWeaver pytest + GitHub Actions CI |
| Defect triage / root-cause / fix | CaseStudyPrep 27% S3 recovery; Vylet 79%→89% name-collision |
| V&V / reliability / correctness | Granular processBlock real-time safety checklist (zero heap / zero locks) |
| Software implementation / APIs | MDC Flask REST on AWS EC2; Requests + Pandas ETL |
| Java, Snowflake, Databricks, Tableau, Copilot, Fusion | **Not in inventory.** Do not invent |
| C-arm / OEC Elite / firmware internships | **Not in inventory.** Analog only |

## Funnel

B-TIER (`companies.md`): Workday resume → recruiter phone (auth, SLC relocate) → one video behavioral + light technical 30–60m · no standardised US intern OA · no intern sys design · **bottleneck: resume** · ~10–15% (peer Medtronic / GE Aerospace / GE Vernova). Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. CS / SWE / BME — **clears** (B.S. Computer Science and Economics).
2. Sophomore year minimum — **clears** (Junior; Summer 2027 is after sophomore year).
3. GPA 3.0 — **clears** (3.66).
4. US work-auth — **clears** (US citizen).
5. Sponsorship now or later — **No**.
6. Salt Lake City onsite / relocate — **Yes** (valid US DL). Relocation assistance is listed **Yes**.

## What to lead with

MDC Flask REST + ETL (shipped software). CaseStudyPrep debug (27% failure recovery). Vylet named defect (79%→89%). Granular C++ correctness (tools, not a C-arm). Then say you will ramp Surgery Imaging / OEC rather than invent it (`persona.md`).

## Do not invent

Java, Snowflake, Databricks, Tableau, Copilot, Fusion, C-arm internships, OEC Elite/OEC 3D product work, embedded firmware, EEDP placement. Do not write this as an ML-research intern. Do not apply this PDF to the Waukesha EEDP Software intern req.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. UMich start **08/31/2025**. HS **Northville High School** graduated **05/19/2025**. Credits by Summer 2027: **96**. No GE HealthCare contact in `network.md` — pick **Company website / LinkedIn**, not Employee Referral.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/ge-healthcare/software-engineering-summer-intern/Vedant Desai Resume.pdf`

**SHA-256:** `ec5d650980eec1907e539ffccecce3e5b34a4e134019b338e298053b3069d074`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **9.0 / 10** (1 minor: Granular metric-free). See `WORTH_IT.md` and `grade.md`.
