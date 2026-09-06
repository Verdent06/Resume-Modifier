# Full Stack Intern at Keysight Technologies

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is Spring 2028 vs JD Spring/Winter 2028; undergrad CS; US citizen / US Person; no sponsorship
- **Track:** full-stack
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Opens on Michigan Data Consulting: a sole-engineer production Flask REST API on AWS EC2 shipped into a nonprofit's public-facing workflow, then quantified ETL (~800 hours / 400 PACs) and stakeholder ownership — enterprise IT analog, not RF firmware.
- Angular+S3 debug (CaseStudyPrep), React/TypeScript + FastAPI + Postgres + Docker Compose / GitHub Actions CI (SignalWeaver), and Dockerized production with a 79%→89% defect fix (Vylet) clear the JD's "at least two" floor through use.
- Binding dings are framing: SignalWeaver is still a 90-ticker research harness, and the Flask REST / ranking lines have no API size.

### Demerits

- **minor** · `SignalWeaver` · research-harness framing, not enterprise IT users — leading with Docker/CI still sits on 90 self-run tickers and batch p50/p99, not an internal tool operators would use.
- **minor** · `Michigan Data Consulting (MDC)` · Flask REST and ranking bullets still unquantified — ETL is sized (~800 hours / 400 PACs); the production Flask REST on AWS EC2 and PAC-ranking lines are not.

### Misreads

- SignalWeaver's "not investment advice" tagline plus ticker metrics can be bucketed as a class project rather than the only end-to-end React + API + DB + CI build.
- CaseStudyPrep can be skimmed as "audio ML intern" and miss that it is the employed Angular/RxJS + S3 debug story the JD frontend list actually names.

### Interview angles

- **Lead with:** MDC sole-engineer Flask REST on EC2 for a nonprofit stakeholder (IT/API analog); SignalWeaver as the React/TypeScript/Postgres/CI sample you can walk layer-by-layer, especially the GitHub Actions pytest/image pipeline; Vylet as Docker + production defect ownership (79%→89%); CaseStudyPrep as Angular + S3 recovery (27% upload-failure).
- **Defend:** SignalWeaver has no external/enterprise users — don't invent Keysight operators; point to MDC's nonprofit workflow and Vylet's three paying clients *(out of rails: SignalWeaver pool is personal 90-ticker / 90-run metrics)*. Flask API and PAC-ranking lines have no QPS *(out of rails: MDC pool has one metric-bearing bullet — the ETL — already on the page)*. Do not claim Kubernetes, Copilot, Jenkins, Vue, Express, Django, DynamoDB, Glue, Lambda, or Java. C++ is in Skills only — interview in Python/TypeScript unless they ask; do not pretend the audio plugin is Keysight work.
- **Depth prep:** Project walkthrough + light coding (Python/JS-family/SQL), not a LeetCode gauntlet and not India-campus CN/OS. Flask vs FastAPI, why Postgres, what each CI stage guards, Angular MIME/S3 debug. Behavioral: ambiguity, global time zones, ask questions. Colorado Springs vs Open-to-Remote is a logistics answer, not a stack answer.

## Likelihood

- **Resume screen:** High — eligibility is on the page, the lead is stakeholder-facing Flask/AWS production, React and Angular plus Docker/CI are through use, and a human reads the iCIMS PDF early.
- **Overall hire odds:** Medium — B-tier measurement company, unpublished intern loop, bottleneck is the resume (~10–15% directional). Remaining filter is a project walkthrough plus US Person / site logistics.
- **Funnel filters:** iCIMS resume screen → recruiter → unpublished technical/HM · Easy–Med **[directional]** · No standard intern OA published for this US IT intern · No intern sys design · Bottleneck: resume · ~10–15% · US Person / no sponsorship · Colorado Springs (Open to Remote: Yes)
- **Outside the resume:** Apply on iCIMS 54165 immediately (posted 2026-09-04). No Keysight contact in `network.md`. Do not invent K8s/Copilot/Jenkins/Java. See `written-answers.md`.
