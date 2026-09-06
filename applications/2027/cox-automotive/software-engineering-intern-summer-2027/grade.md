# Software Engineering Intern - Summer 2027 (North Hills, NY) at Cox Automotive

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** Eligible — currently enrolled BA/BS CS + Economics, Expected May 2028 (still a student for Summer 2027). No GPA or exclusive class-year gate on this JD. US citizen / no OPT, CPT, STEM OPT, or future sponsorship. North Hills NY onsite is acceptable.
- **Track:** dev-ops + automotive-marketplace (Dealertrack / Autotrader / KBB / Manheim)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is a Dockerized pipeline with Redis/Celery workers (30x speedup) plus SQL freshness automation — the intern DevOps bar (containers, workers, databases), not a notebook.
- SignalWeaver Docker Compose + GitHub Actions CI, Flask on AWS EC2, and S3 presigned-URL failure handling cover CI/CD, preferred AWS, and deploy/reliability. GPA 3.66 and a live GitHub clear the resume-first C-tier intern screen.
- Binding dings: Lyndbrook is one GTM automation line; nothing on the page is dealer/auto-retail. A platform screener still has Docker, GHA, and AWS in the top half.

### Demerits

- **minor** · `Lyndbrook Capital` · single-bullet GTM automation, not platform/CI — EPA/Maps deal-sourcing that saved a search-fund Principal 15 hours/week. Automation, but not containers, CI/CD, or cloud deploy.
- **minor** · `resume` · company-fit differentiator absent — Differentiator is Cox Automotive marketplace platforms; the page is PE lead-gen, campaign-finance ETL, voice-AI uploads, water-utility sourcing, and financial-research serving.

### Misreads

- A Dealertrack screener skimming titles could bucket this as a PE/search-fund founder resume and miss Docker Compose, GitHub Actions, Celery workers, and AWS EC2.
- A keyword pass for Kubernetes / Terraform / Linux-as-a-named-OS could file the page as “no infra” if they do not read the Docker/GHA/AWS bullets.

### Interview angles

- **Lead with:** Vylet Docker + Redis/Celery (manual process → recurring workers, 30x) as the analog to infrastructure automation; SignalWeaver Docker Compose + GitHub Actions (frontend build, pytest, API image on main) as CI/CD; MDC Flask on AWS EC2 as cloud deploy; CaseStudyPrep S3 URL regeneration as failure-handling in a pipeline.
- **Defend:** No Dealertrack / Autotrader / Manheim / Kubernetes / Terraform / Copilot / Windows-sysadmin work exists in the pool — say so, then map Docker/GHA/AWS onto “enterprise platforms, deployment pipelines, public cloud preferably AWS.” Lyndbrook is honest GTM automation, not a platform story. *(out of rails: pool has no auto-retail marketplace bullet; Lyndbrook pool is GTM-only; no_bullet_deletion blocks dropping it)*
- **Depth prep:** Walk Docker Compose services (API, Postgres/pgvector, nginx) and the GitHub Actions graph; Celery/Redis worker cycle and SQL stale-timestamp re-scrape; S3 presigned-URL expiry; how you would add a packaging/deploy step without claiming Jenkins/K8s.

## Likelihood

- **Resume screen:** High — Docker/GHA/AWS/Celery through use, Python in the spine, sized automation metrics, live GitHub, 3.66 GPA clear the abstract pass signals on a resume-first C-tier screen.
- **Overall hire odds:** Medium — Cox Automotive intern loops are unpublished and resume-weighted (`companies.md` C-tier ~15–25%; `recruiting.md` mid-size / non-tech-tech). Clearing the PDF is most of the front end; a live coding or take-home plus North Hills onsite still eliminate if they want K8s/Terraform or if Long Island onsite is a no.
- **Funnel filters:** Workday ATS **R202682171**; no standard intern OA published. Recruiter auth/location/enrollment, then unpublished intern loop (FT analog: take-home or live coding + panel). US work-auth / no OPT/CPT/STEM OPT knockout (met). Posted 2026-09-04; Workday `endDate` 2026-10-16. Onsite North Hills (no remote option).
- **Outside the resume:** Apply in this window. No Cox contact in `network.md` — a Dealertrack/Long Island alum beats cold Workday (`recruiting.md`: HM > recruiter > engineer > cold apply). Mock the Compose + GHA walkthrough; keep STAR for the behavioral filter. See `written-answers.md`.
