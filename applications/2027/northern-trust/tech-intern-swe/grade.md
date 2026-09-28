# Technology Intern – Software Engineering at Northern Trust

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside Dec 2027–Summer 2028; GPA 3.66 ≥ 3.0; US citizen / no sponsorship
- **Track:** full-stack + fintech-backend / custody-wealth asset-servicing platforms
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Eligible UMich CS+Econ intern (May 2028, 3.66) with a quantified campaign-finance ETL, a production Flask REST API on AWS EC2, SQL in a live product, and FastAPI/React/CI — this is a SWE intern screen, not InfoSec/Infra/DS.
- Finance-adjacent work sits in the lead window (PAC pipeline; PE/search-fund product; financial-research platform).
- Binding ding: the MCFN API is unsized, and the PAC-ranking engine has no number.

### Demerits

- **minor** · `MDC` · production API unsized — The Flask REST API on AWS EC2 still has no callers, endpoints, or traffic; the ETL leads with ~800 hours / 400 PACs, but a SWE-intern screener cannot size the service that is the role's closest analog.
- **minor** · `MDC` · aggregation engine unquantified — The third bullet ranks PACs by funding volume with no count, precision, or time saved; it reads soft next to the ETL metric and does not size the analytical engine.

### Misreads

- A rushed screener might bucket the Flask line as a student deploy because the service has no size next to a strong ETL metric.
- A keyword pass might miss SQL (one DAL bullet + Skills) and treat the page as Python-only despite Postgres/asyncpg through use.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL (~800 hours / 400 PACs) plus Flask REST on EC2 shipped to MCFN; Vylet name-collision debug 79%→89% plus injection-safe SQL DAL and Docker/Redis/Celery; SignalWeaver FastAPI + React/TypeScript + GitHub Actions pytest.
- **Defend:** No Java / Azure DevOps — inventory is Python/TypeScript/SQL/C++; ramp on JVM or Azure DevOps if the rotation uses them. MCFN API has no request/latency/user number *(out of rails: MDC pool does not size the service)*. PAC-ranking engine has no count *(out of rails: unused MDC bullet is also metric-free stakeholder scoping)*.
- **Depth prep:** Intern coding-OA platform unpublished — treat as Easy–Med DS&A in Python if invited. Walk Flask/EC2 deploy, Vylet ownership-verification defect + SQL timestamp gates, SignalWeaver CI. STAR behavioral (`recruiting.md` §6). Financial-markets curiosity: campaign-finance PAC pipeline, PE/search-fund product, SignalWeaver research assistant (not investment advice). Not Copilot, not custody-platform theater.

## Likelihood

- **Resume screen:** High — eligible class year/GPA, production Python API + SQL + CI, finance-adjacent flavor in the lead window.
- **Overall hire odds:** Medium — B-tier resume-gated intern (~8–12%); paper should convert to a virtual interview, then unpublished coding screen plus a behavioral filter still eliminate.
- **Funnel filters:** Workday knockouts (GPA 3.0, grad window, no sponsorship) → official FAQ virtual interview. Intern coding-OA unpublished. No intern sys design. NA cap: 3 postings/season.
- **Outside the resume:** Apply in this first wave (posted 2026-09-01; rolling close Oct 9, 2026 11:59pm Central). Timed mediums in Python. No Northern Trust contact in `network.md` — a real employee referral would warm the pile.
