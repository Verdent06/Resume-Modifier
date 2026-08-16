# Intern Data Engineers - AI & Analytics - 2027 at IBM

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 + Summer 2027 intern; currently pursuing B.S. Computer Science and Economics; JD requires a listed Bachelor's in progress; no class-year knockout, no GPA floor, no clearance named
- **Track:** ai-ml
- **Pipeline:** 4 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular filings → Pandas ETL (~800 hours / 400 PACs) → aggregation → Flask API on EC2. Ingest → transform → serve for a CIC data-engineer intern, not the Software Developer Intern spine.
- Vylet carries SQL freshness (asyncpg timestamp validation) plus a Dockerized pipeline and a 79→89% qualification fix; Lyndbrook is multi-source entity resolution and an 800→280 scoring closer.
- Binding dings are both minor: SQL is one DAL/freshness beat, and SignalWeaver’s witnesses are latency and ticker count, not score quality.

### Demerits

- **minor** · `resume` · SQL is one DAL/validation beat — Python pipelines are everywhere; SQL appears as asyncpg plus injection-safe timestamp validation on Vylet, not a transform or qualify step
- **minor** · `SignalWeaver` · no quality or lift metric on the scores — 49ms/99ms search, 9.1s scoring p50, and 90 tickers size an API experiment, not whether the composite scores were accurate or useful

### Misreads

- A skim that stops on Vylet's PE/search-fund founder tagline can file this as startup SaaS and miss the SQL DAL / pipeline work the CIC screen wants.
- SignalWeaver's financial-research framing plus p50/p99 can read as a latency-bench ML demo rather than a data product.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery; Vylet injection-safe SQL freshness / re-scrape plus the 79→89% qualification fix; Lyndbrook PWSID entity DB + Review Velocity (800 → 280)
- **Defend:** SQL is freshness/validation, not a warehouse transform — walk the asyncpg DAL and what you would query next. SignalWeaver p50/p99 is instrumentation, not client impact — walk the dashboard / persisted scores as the analytics analog. Lyndbrook 35% is the 280/800 keep-rate *(out of rails: 3-bullet pool; cannot rewrite the metric)*. Vylet SQL line has no stale-rate *(out of rails: only SQL bullet; inventing a freshness number is forbidden)*
- **Depth prep:** easy HackerRank DS&A (IBM bottleneck is resume, then OA); walk one ingest → transform → validate → serve path (MDC) and one SQL-quality path (Vylet DAL). STAR for client-adjacent scoping (MDC/MCFN). Behavioral is a filter round (`recruiting.md` §6). Do not claim Java, IBM Cloud, watsonx, Tableau, or day-one CIC platform ownership

## Likelihood

- **Resume screen:** High — pipeline/ETL/client-delivery page for a resume-gated CIC data intern req; eligible class year, GPA, Python/SQL through use
- **Overall hire odds:** Medium — B-tier ~10–15%; screen is the hard gate and this page clears it, then easy HackerRank and 2–3 easy technical/behavioral rounds still eliminate. Remaining risk is the OA, a consulting behavioral, and committing to onsite Monroe CIC
- **Funnel filters:** Resume screen (bottleneck) → HackerRank (easy) → 2–3 easy technical/behavioral rounds; no intern systems-design. Apply channel is LED FastStart / Monroe CIC, not the hybrid Software Developer Intern Avature req. Comp posted $45,760
- **Outside the resume:** Timed easy HackerRank; a referral or alumni IBMer into the CIC/data practice; 2–3 client-collaboration stories for the behavioral filter (`recruiting.md` §4, §6)
