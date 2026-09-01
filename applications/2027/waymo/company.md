# Waymo

Waymo is Alphabet's autonomous-driving subsidiary and the commercial operator of the Waymo Driver — the robotaxi stack that began as the Google Self-Driving Car Project (2009) and spun out in 2016. The Driver powers a fully autonomous ride-hail service and other vehicle platforms; the JD cites 10M+ rider-only trips, 100M+ public-road miles, and tens of billions of simulated miles. Mountain View HQ; this intern seat is hybrid onsite in San Francisco on Systems Engineering (Commercialization Testing). Strongest AV name on the A-TIER list (`reference/companies.md`: Alphabet lineage, elite eng bar).

## Quick Facts

- **Tier:** A-TIER — Excellent / Strong Signal (`reference/companies.md`)
- **HQ / offices:** Mountain View, CA (HQ). This intern: San Francisco, CA (hybrid onsite). Other intern sites historically include Mountain View and Warsaw (Formation Program) **[directional]**
- **Valuation / signal:** Doctrine: strongest AV name, Alphabet lineage. Web (Feb 2026 Series D): ~$126B post-money / $16B raise (Wikipedia / Sacra); earlier ~$45B (Oct 2024). Lead with the doctrine prestige marker; treat $126B as a 2026 update
- **Product focus:** Waymo Driver — autonomy stack for robotaxi + other vehicle platforms; Systems Engineering sets performance standards and designs the tests that validate them
- **Intern comp (2027 Data Science - Commercialization Testing, MS/PhD):** Masters $70/hr; PhD $85/hr (this JD). Broader intern band $48–$85/hr by track/education (Extern, Levels.fyi SWE intern analogs)
- **Work model:** Paid intern, hybrid onsite, Summer 2027. Rolling review until filled. Apply to each role individually (top 3)
- **Clearance / eligibility:** This req: enrolled in a **graduate program (Master's or PhD)** in Data Science, Statistics, Operations Research, Civil Engineering (traffic/mobility analytics), or a highly quantitative field. No citizenship/export-control line on this posting. Broader intern programs often require a term remaining after the internship **[directional — other reqs]**

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Human + ATS (Greenhouse gh_jid=8167323) | Rolling until filled; PDF is read early (`recruiting.md` Greenhouse). This req is MS/PhD Data Science, not generic SWE |
| Recruiter screen | ~30 min (intern reports) | Background, AV interest, team alignment, hybrid SF availability |
| OA | HackerRank (doctrine SWE row) | `companies.md` Waymo: Med–Hard HackerRank. Intern-cycle reports (Extern, Jul 2026) say **no separate OA** — live CoderPad instead. DS loops (InterviewQuery / candidate blogs) weight Python + SQL. Lead with doctrine; treat no-OA as a 2026 intern-report delta |
| Tech screen | Live coding / SQL+Python (DS reports) | Doctrine bottleneck: tech rounds. DS: stats, small-sample inference, fleet/telemetry-style analytics — not a ROS/perception specialist round |
| Virtual onsite | 2–5 rounds | Coding, stats/ML, project deep-dive, behavioral (safety mindset, collaboration). Sys design more for PhD/senior (`companies.md`: Yes) |
| Behavioral | Safety / collaboration | Filter round (`recruiting.md` §6); correctness and statistical limitations matter because the product is safety-critical |

**Estimated funnel:** 4 rds · Med–Hard · HackerRank · Yes · Bottleneck: tech rounds · ~3–5% (`reference/companies.md` Waymo row). This posting is Systems Engineering Commercialization Testing DS, not the SWE intern req — screen still Greenhouse-first; binding filter remains technical rounds.

## Stack & Hiring Signal

- **Languages:** Python and SQL (this JD, named as production Python + large-scale DB query/synthesis). Broader Waymo SWE intern JDs skew C++ (`recruiting.md` §14); do not invent C++ on this DS packet if the page does not already carry it through use
- **Domains:** Bayesian forecasting on small-sample tests; predictive analytics for fleet ops / vehicle behavior; experimental design (closed course + simulation); high-dimensional vehicle-log / depot datasets; systems-engineering test coverage
- **What wins:** Applied stats + data pipelines on the page (`resume.md` §14 / `recruiting.md` §13): Python and SQL through use, messy high-dimensional data → method (inference, forecasting, scoring) → measured output, plus honest limits when talking to non-technical partners. Autonomy/AV identity is the differentiator after the literal DS screen — fleet/ops/test-adjacent analytics, not a robotics-only resume and not notebook `model.fit()`. Do not invent Snowflake, Databricks, Tableau, Copilot, Fusion, or Sentry

## Sources

- JD: https://careers.withwaymo.com/jobs?gh_jid=8167323 (Greenhouse 8167323)
- `reference/companies.md` A-TIER Waymo row (interview format, bottleneck, acceptance estimate, AV/Alphabet Notes)
- `reference/recruiting.md` Part I §1 (Greenhouse), Part II §8 (intern eligibility/timing), Part III §13 (AI/ML) and §14 (robotics/autonomy)
- Extern intern guide (Jul 2026): https://www.extern.com/post/waymo-internship-guide
- Wikipedia / Sacra: Feb 2026 Series D ~$126B (valuation update vs doctrine prestige marker)
- InterviewQuery Waymo DS guide (DS loop flavor, not intern-official): https://www.interviewquery.com/interview-guides/waymo-data-scientist
