# Skillz Inc — intern notes (Co-op, Software Engineer, Winter 2027)

Intern-facing packet notes for Greenhouse **8168006** / **TAH-296**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Skillz builds

Skillz is the competition layer inside mobile games: matchmaking, identity, payments, fraud, and developer tools so studios can run real-money skill-based tournaments at scale (JD: 800k+ daily tournaments, $7.5B lifetime prizes, 90M registered users). It sits under **FIRY** with RZR (ads) and Beamable (LiveOps). This co-op is **Skillz Engineering payments/platform backend**, not RZR, not Beamable, not a game-client seat (`company.md`).

## This req

- **Title:** Co-op, Software Engineer · Las Vegas, NV · $32/hr · onsite 5 days / 40h · relocation support
- **Term:** Jan 11 2027 – Aug 20 2027 (~7.5 months; 6–12 month program)
- **Work:** backend services and APIs for payment infrastructure and deposit/withdrawal/payout; sprint/reviews; production debug; payment/platform docs
- **Posted:** first_published 2026-09-03 — first wave (`recruiting.md` Part II §8)

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

1. **Graduation window (binding).** Enrolled at start **and** graduate ≤1 year after program begins → by **Jan 11 2028**. May 2028 is after that. Greenhouse Yes/No = **No**. Binary knockouts auto-reject (`recruiting.md` Part I §1). Do not answer Yes.
2. GPA 3.3 — **clears** (3.66).
3. CS bachelor's enrolled — **clears**.
4. Las Vegas 5-day onsite for the full term — **Yes** (relocate).
5. Work auth / no future sponsorship — **Yes / No** (US citizen).

## What to lead with

MDC production Flask REST on AWS EC2 + ETL. Vylet SQL integrity + named production defect. SignalWeaver FastAPI + CI. CaseStudyPrep 27% S3 recovery as production-debug analog. Then say you will ramp Java/Go rather than invent them (`persona.md`).

## Do not invent

Java, Go, Kubernetes, Jenkins, Terraform, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, PCI, payment-processor SDKs, Skillz platform, card rails, deposit/withdrawal/payout ownership, distributed-transaction libraries.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Greenhouse). Phone 248-704-4852. US citizen. No Skillz contact in `network.md` — pick **Job Boards**, not Employee Referral.
