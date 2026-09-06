# Skillz Inc — intern notes (Co-op, Software Engineer, Winter 2027)

Intern-facing packet notes for Greenhouse **8168006** / **TAH-296**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

Apply: https://job-boards.greenhouse.io/skillzinc/jobs/8168006

**Do not submit from this agent.** Full paste table: `written-answers.md`.

Resume PDF: `applications/2027/skillz/software-engineer-co-op-winter-2027/Vedant Desai Resume.pdf`

**SHA-256 (sha256sum of the shipped PDF):**

```
6859aa5721d6a52ae6e0e27e29ee392f118fd496532fe52a75a4789d4ce6a9f6
```

Form email: **verdent06@gmail.com** (never `vedantde@umich.edu` on Greenhouse). Phone 248-704-4852. US citizen. No Skillz contact in `network.md` — pick **Job Boards**, not Employee Referral.

## What Skillz builds

Skillz is the competition layer inside mobile games: matchmaking, identity, payments, fraud, and developer tools so studios can run real-money skill-based tournaments at scale (JD: 800k+ daily tournaments, $7.5B lifetime prizes, 90M registered users). It sits under **FIRY** with RZR (ads) and Beamable (LiveOps). This co-op is **Skillz Engineering payments/platform backend**, not RZR, not Beamable, not a game-client seat (`company.md`).

## This req

- **Title:** Co-op, Software Engineer · Las Vegas, NV · $32/hr · onsite 5 days / 40h · relocation support
- **Term:** Jan 11 2027 – Aug 20 2027 (~7.5 months; 6–12 month program)
- **Work:** backend services and APIs for payment infrastructure and deposit/withdrawal/payout; sprint/reviews; production debug; payment/platform docs
- **Posted:** first_published 2026-09-03 — first wave (`recruiting.md` Part II §8)
- **Form recapture:** 2026-09-06 (API still `updated_at` 2026-09-03)

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Java, Go, or similar | Python, TypeScript, C++, SQL — **no Java, no Go**. "Or similar" is the honest frame (same as Java at Mastercard / BNY) |
| REST + microservices | Flask REST (MDC), FastAPI REST (SignalWeaver), Docker/Celery workers (Vylet) |
| Git + CI/CD | Git; GitHub Actions + pytest (SignalWeaver) |
| AWS preferred | AWS EC2 (MDC Flask), S3 (CaseStudyPrep) |
| Payments / financial data integrity / distributed transactions (preferred) | Analog only: campaign-finance ETL + Flask API; injection-safe SQL freshness; production defect 79%→89%. **Not** PCI, card rails, or Skillz payout services |

## Funnel

C-TIER (`companies.md`): Greenhouse resume → recruiter phone → HackerRank (full-time analog; intern OA unpublished) · no intern sys design · **bottleneck: resume** (+ OA if issued) · ~15–25% among eligible. Mid-size Greenhouse is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. **Graduation window (binding).** Enrolled at start **and** graduate ≤1 year after program begins → by **Jan 11 2028**. May 2028 is after that. Greenhouse Yes/No = **No**. Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not answer Yes. Packet is for apply-anyway; form stays honest.
2. GPA 3.3 — **clears** (3.66).
3. CS bachelor's enrolled — **clears**.
4. Las Vegas 5-day onsite for the full term — **Yes** (relocate).
5. Work auth / no future sponsorship — **Yes / No** (US citizen).

## What to lead with

MDC production Flask REST on AWS EC2 + ETL. Vylet SQL integrity + named production defect. SignalWeaver FastAPI + CI. CaseStudyPrep 27% S3 recovery as production-debug analog. Then say you will ramp Java/Go rather than invent them (`persona.md`).

## Do not invent

Java, Go, Kubernetes, Jenkins, Terraform, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, PCI, payment-processor SDKs, Skillz platform, card rails, deposit/withdrawal/payout ownership, distributed-transaction libraries.

## Worth-it vs persona / pool

**YES on skill fit (8 / 10).** Pipeline score **10.0 / 10** (0 demerits). **Form knockout remains** (May 2028 vs Jan 11 2028 window). See `WORTH_IT.md` and `grade.md`.

## PDF

Header email on the PDF is **vedantde@umich.edu** (`context.md` / template — writer cannot change header). **Form uses verdent06@gmail.com.** Autofill will try umich — change it.

## Greenhouse gotchas on this req

| Issue | What to do |
| --- | --- |
| Email parses as `vedantde@umich.edu` | Change to **verdent06@gmail.com** |
| Graduation window Yes/No | **No** — do not lie to pass the filter |
| Location (City) / Locate me | **Northville, Michigan, United States** — current city, not Las Vegas |
| Reside in required location | **No**; relocate **Yes** |
| Education widget is required | University of Michigan · Bachelor's · Computer Science · start **08/31/2025** · expected **May 2028** · Did you graduate? **No** |
| How you heard | **Job Boards** — no Skillz contact in `network.md` |
| Desired compensation | **$32/hour** |
| Cover letter | Optional. Skip for speed; paste from `written-answers.md` if you attach one |
| EEO / demographics | Decline unless you want to self-ID |

School typeahead: search `Michigan` → **University of Michigan**. Do not pick Dearborn/Flint/MSU.

Posting: first_published **2026-09-03**. No `application_deadline` on the API.
