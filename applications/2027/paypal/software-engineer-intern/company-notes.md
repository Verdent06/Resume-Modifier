# PayPal — intern notes (Software Engineer Intern, Summer 2027)

Intern-facing packet notes for Eightfold **R0137285** / pid **274922260559**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What PayPal builds

PayPal is a two-sided digital-payments network: consumer wallet + merchant acquiring, payouts, and risk across PayPal, Venmo, Braintree, Xoom, and Paydiant (`company.md`). This intern is a **generic full-stack SWE seat** that may land on any product team — not a fraud-research seat, not a trading desk, not Braintree-only.

## This req

- **Title:** Software Engineer Intern · Summer 2027 only (Spring/Fall 2027 not offered)
- **Locations:** San Jose, CA (primary); Austin, TX; Chicago, IL · hybrid 3 days office / 2 home or office · relocate to assigned hub
- **Comp (this JD):** SJ **$32–$55/hr**; Austin **$28–$49/hr**; Chicago **$28–$49/hr**
- **Work:** design/implement/test/deploy; triage production; Java / Python / Node.js / React / SQL / REST (responsibilities); min quals are *one of* Java, Python, C++, JavaScript, or similar
- **Posted:** 2026-09-04 — first wave (`recruiting.md` Part II §8)
- **ATS:** Eightfold. Canonical: https://paypal.eightfold.ai/careers/job/274922260559
- **Apply:** https://paypal.eightfold.ai/careers/apply?pid=274922260559&domain=paypal.com
- **Simplify (source listing):** https://simplify.jobs/p/30829caf-2d43-4e4c-aeb6-aa37a19f224b

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| Java, Python, C++, JavaScript, or similar | Python, TypeScript, C++, SQL — **no Java, no Node.js**. "Or similar" is the honest frame (same as Java at Mastercard) |
| React, REST, SQL, databases / data integrity | React (SignalWeaver), Flask REST (MDC), FastAPI REST (SignalWeaver), PostgreSQL, injection-safe SQL (Vylet) |
| Debug / test / deploy / SDLC | CaseStudyPrep 27% S3 recovery; Vylet 79%→89%; GitHub Actions + pytest |
| AWS / cloud (not required, implied by deploy) | AWS EC2 (MDC Flask), S3 (CaseStudyPrep), Docker |

## Funnel

B-TIER (`companies.md`): Eightfold resume → HackerRank (Easy–Med) · recruiter/sourcer phone → HM · no intern sys design · **bottleneck: OA** · ~5–8%. Resume still has to clear; OA is what eliminates (`recruiting.md` Part I §1 vs Greenhouse resume-first).

## Knockouts

1. Return to school Fall 2027 — **clears** (Expected May 2028).
2. CS / related bachelor's in progress — **clears**.
3. Work authorized in the US — **Yes** (US citizen).
4. Future sponsorship — **No**. JD: sponsorship not available now or later.
5. Summer 2027 only; hybrid 3/2 at SJ / Austin / Chicago — **Yes** (relocate).

## What to lead with

MDC production Flask REST on AWS EC2 + ETL. Vylet SQL integrity + named production defect. SignalWeaver FastAPI + React + CI. CaseStudyPrep 27% S3 recovery as production-debug analog. Then say you will ramp Java/Node rather than invent them (`persona.md`).

## Location pick

JD primary is **San Jose** (highest posted band). Chicago is closest to Northville, MI. Austin is the third hub. If the form asks for one location, pick **San Jose** unless you prefer Chicago for travel. Confirm relocate **Yes**.

## Do not invent

Java, Node.js, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry, PCI, PayPal/Venmo/Braintree platform experience, card rails, payment-processor SDKs.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Eightfold). Phone 248-704-4852. US citizen. No PayPal contact in `network.md` — pick **Job Board**, not Employee Referral / Direct Source. Full knockouts and essays: `written-answers.md`.
