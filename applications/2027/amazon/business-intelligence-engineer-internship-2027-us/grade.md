# Business Intelligence Engineer Internship - 2027 (US) at Amazon

## Verdict

- **Score:** 9.0 / 10 (1 demerits — 0 emergency, 0 major, 1 minor)
- **Eligibility:** eligible — Expected May 2028 is inside Oct 2027–Dec 2030; Summer 2027 leaves Fall 2027 + Winter 2028; US-enrolled B.S. CS; 18+; Master's path is preferred, not an undergrad exclusion
- **Track:** ai-ml
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Lead is MDC: irregular Excel filings → Requests+Pandas ETL (~800 hours / 400 PACs) → PAC ranking → Flask REST on AWS EC2. Ingest → transform → report for a Business Intelligence Engineer intern, not SDE 10552937 and not Data Engineer 10553907.
- Vylet carries injection-safe SQL freshness / re-scrape and a 79%→89% name-collision RCA. Lyndbrook is a PWSID entity database plus 800→280 scoring. SignalWeaver opens on a React/Postgres dashboard and a held-out linear regression (3.39% R²).
- Binding ding is minor: SQL is a DAL/freshness beat rather than a query that produced a ranking or dashboard.

### Demerits

- **minor** · `Vylet` · SQL is freshness/DAL not a BI query or model — required SQL appears as injection-safe timestamp validation that triggers re-scrapes, not a query, aggregation, or model that produced a report, ranking, or dashboard *(out of rails: pool has no JOIN/GROUP BY/window SQL analysis bullet)*

### Misreads

- A keyword-first pass for Tableau / QuickSight / Excel-as-viz can bucket this as "wrong stack" even though Pandas-on-Excel-exports, PAC rankings, a React dashboard, and regression are on the page.
- SQL on the Languages line plus the Vylet DAL can file as analysis SQL, then bounce when the only SQL story is timestamp plumbing.
- Vylet's PE/search-fund founder tagline can file as startup SaaS if the reader never reaches the SQL freshness / RCA lines.
- SignalWeaver's financial-research descriptor can file as notebook ML if the reader never reaches the dashboard / regression lines.

### Interview angles

- **Lead with:** MDC Requests+Pandas ETL on irregular filings and sole-engineer MCFN delivery on EC2; Vylet injection-safe SQL freshness / re-scrape plus the 79%→89% defect fix; Lyndbrook PWSID entity DB + Review Velocity (800 → 280); SignalWeaver React/TypeScript dashboard and out-of-sample linear regression
- **Defend:** SQL is freshness/validation, not a warehouse or BI-query transform — walk the asyncpg DAL and what you would query next *(out of rails: only SQL bullet in the pool)*. Do not claim Tableau, QuickSight, MicroStrategy, PowerBI, Excel-as-a-visualization-tool, t-test, Chi-squared, Java, or R. Walk the React dashboard and the regression analog instead. This is Job **10553765**, not SDE **10552937** and not DE **10553907**.
- **Depth prep:** Amazon BIE intern OA is **not confirmed** as the SDE coding OA. Practice timed **SQL** (joins, aggregations, window functions) and **Python** data transformation; complete any Workstyles / Leadership Principles survey the email names. Loop **[directional]**: SQL + dashboard/analysis walk + LP STAR. No intern sys design (`companies.md`). Map stories to Ownership, Dive Deep, Bias for Action, Customer Obsession from MDC production API and Vylet pipeline RCA.

## Likelihood

- **Resume screen:** High — one-page BIE spine with Python/SQL through use, conferral in window, dashboard + regression analog; remaining ding is SQL flavor, not SQL absence
- **Overall hire odds:** Medium — A-tier ~1–2% large class; resume is not the first elimination; SQL/Python OA plus LP loop still drop most of the intern class
- **Funnel filters:** amazon.jobs resume → OA (SQL/Python data work + LPs **[directional for BIE; official OA page is SDE]**) · 1–2 rds · Bottleneck: **OA** · ~1–2% · in-person US BIE intern sites · conferral Oct 2027–Dec 2030 + remaining term after internship · Seattle listed pay **$86,615**
- **Outside the resume:** Timed SQL + Python data-transform practice; LP Work Style consistency; apply in this first wave; Summer 2027 first, Winter 2027 OK, do not select Fall 2027; keep distinct from the SDE intern and the DE intern packets. See `written-answers.md`
