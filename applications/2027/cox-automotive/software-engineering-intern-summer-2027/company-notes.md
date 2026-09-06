# Cox Automotive — intern notes (Summer 2027 SWE intern, North Hills NY)

Intern-facing packet notes for Workday **R202682171**. Not a rewrite of `company.md`. Cite `company.md` / `companies.md` / `recruiting.md` in shorthand.

## What Cox Automotive builds

Auto-retail technology arm of family-owned Cox Enterprises (Atlanta HQ): **Autotrader**, **Kelley Blue Book**, **Manheim**, **vAuto**, **Dealertrack**. This intern sits at **Dealertrack's Long Island campus** (North Hills, 3400 New Hyde Park Rd) on a family-wide Software Development Intern template aimed at **enterprise platforms, CI/CD, containers, and cloud**, not Cox Communications and not an Autotrader UI intern.

## This req

- **Title:** Software Engineering Intern - Summer 2027 (North Hills, NY) · onsite (Workday: no remote option) · **$29.09–$43.61/hr**
- **Site:** 3400 New Hyde Park Rd, North Hills, NY (Long Island). 5% travel. Day shift. Full time intern
- **ATS:** Workday **R202682171** · https://cox.wd1.myworkdayjobs.com/Cox_External_Career_Site_1/job/Long-Island-NY/Software-Engineering-Intern---Summer-2027--North-Hills--NY-_R202682171-1
- **Posted:** 2026-09-04 · Workday `endDate` **2026-10-16** — first wave (`recruiting.md` Part II §8)
- **Work:** infrastructure provisioning automation, config management, CI/CD, code packaging/deploy, performance tracking, AWS preferred, containers + databases, Agile (Scrum/Kanban) familiarity, AI-assist tools as familiarity only
- **Cap:** apply to no more than three Cox internships in 90 days

## Stack they hire vs what Vedant has

| They name | Inventory |
| --- | --- |
| One high-level language / scripts | Python through use (MDC, Vylet, SignalWeaver). SQL through use |
| Containers | Docker, Docker Compose. **No Kubernetes** |
| Databases | PostgreSQL, Redis, pgvector. asyncpg DAL |
| Source / build / deploy / CI | Git, GitHub Actions (frontend build, pytest, API image). **No Jenkins, no Terraform** |
| Public cloud, preferably AWS | AWS EC2, S3. **No GCP/Azure claimed** |
| Linux / Windows | Docker implies Linux. **No Windows sysadmin, no named Linux homelab** — do not invent |
| AI tools for SDLC | **No Copilot.** Do not check it. LangGraph is product-side, not an IDE copilot |
| Auto-retail / Dealertrack | Analog only: shipped pipelines. **Not** Manheim, Autotrader, Dealertrack, or Cox platforms |

## Funnel

C-TIER (`companies.md`): Workday resume → recruiter phone → unpublished intern loop (FT analog: take-home or live coding + panel) · intern OA unpublished · no intern sys design · **bottleneck: resume** · ~15–25%. Mid-size / non-tech-tech is resume-first (`recruiting.md` Part I §1 vs OA-gated big tech).

## Knockouts

1. Work auth / no OPT/CPT/STEM OPT / no future sponsorship — **clears** (US citizen).
2. Enrolled BA/BS CS or related — **clears** (Expected May 2028; Junior; 96 credits by Summer 2027).
3. North Hills onsite Summer 2027 — **Yes** (relocate).
4. Kubernetes / Terraform / Copilot — **not knockouts**. Do not invent them.

## What to lead with

Vylet Docker + Redis/Celery. SignalWeaver Docker Compose + GitHub Actions. MDC Flask on AWS EC2. CaseStudyPrep S3 retries. Then say you will ramp Dealertrack/Cox platforms rather than invent them (`persona.md`).

## Do not invent

Kubernetes, Terraform, Jenkins, Copilot, Snowflake, Databricks, Tableau, Fusion, Sentry, Windows sysadmin, Linux homelab, Dealertrack/Manheim/Autotrader internships, Cox internal tools.

## Form kit

Apply email **`verdent06@gmail.com`** (never `vedantde@umich.edu` on Workday). Phone 248-704-4852. Address 49032 Freestone Dr, Northville, MI 48168. US citizen. Valid US DL **Yes**. DOB **12/16/2006**. SAT **1510** if asked. High school **Northville High School** graduated **05/19/2025**. UMich start **08/31/2025**. No Cox contact in `network.md` — pick **Job board / career site**, not Employee Referral.

Full paste table: `written-answers.md`.

## PDF

`applications/2027/cox-automotive/software-engineering-intern-summer-2027/Vedant Desai Resume.pdf`

**SHA-256:** `36114020480db2d3c4c0ec2b37af70405693bb1375527516f0e0e3c42c2684c0`

Header email on the PDF is **verdent06@gmail.com** (packet hard rule). Form uses the same.

## Worth-it vs persona / pool

**YES.** Pipeline score **8.0 / 10** (2 minor: Lyndbrook GTM leftover; automotive-marketplace differentiator absent). See `WORTH_IT.md` and `grade.md`.
