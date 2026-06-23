# 2027 Software Engineer Intern at Anduril Industries

## Verdict

| Field | Value |
| ----- | ----- |
| Gates | PASS |
| Weighted demerits | 4 (emergency 0 / major 1 / minor 1) |
| Display score | 6.0 / 10 |
| Pass bar | weighted < 5 AND no emergency AND gates pass |
| Demerit result | PASS |
| Ship status | Shipped — gates pass & demerits clear |
| Iterations | 1 |
| Eligibility | eligible — rising senior at Summer 2027 internship term |
| Track | full-stack + autonomy |

## Reviewer Persona

I'm screening SWE intern apps for a defense-autonomy company where the JD looks generic but the floor ships C++, perception, and field-deployed systems. I have thirty seconds and a stack of resumes from strong CS programs. I advance candidates who show they ship real software under real constraints *and* have a thread of autonomy, robotics, or perception — not pure club ops, not notebook ML, and not a skills list that claims languages the bullets never touch.

## Scored Defects

| Entry | Severity | Defect | Why | Weight |
| ----- | -------- | ------ | --- | ------ |
| resume | major | C++ not demonstrated in body | JD lists C++ proficiency and Anduril ships C++ on autonomy/embedded systems; Languages claims C++ but no bullet names it — the gap is louder at a defense-autonomy company than at a generic SaaS shop. | 3 |
| fliks | minor | single thin bullet | One Postgres-queue line is the only Go evidence beyond the skills list; reads compressed relative to the depth shown elsewhere. | 1 |

### What Would Take This to the Next Level

- Put C++ in a bullet, not just the skills line — even one FRC or ROS2 line naming it would quiet the biggest screen objection at this company.
- Give fliks a second quantified line or fold Go depth into a stronger systems entry so Go isn't a one-liner.

## Mechanical Gates

**hard_gates_pass:** true

| Gate | Result | Detail |
| ---- | ------ | ------ |
| required_languages | PASS | All JD languages the candidate has are present: c++, go, java, python. |
| no_orphans | PASS | No orphaned framework/library skills. |
| no_bullet_deletion | PASS | Skipped (iteration 1 or fit-check phase). |
| min_entries | PASS | 5 entries (floor 5). |
| protected_depth | PASS | Protected entries retain depth. |
| lead_signal | PASS | Differentiator entry in top 2: Secure and Efficient Autonomous Systems Lab. |
| fit_protection | PASS | Fit drops were project-scoped and protected entries intact. |
| page_fill | PASS | 10 bullets (no pdfplumber; bullet-count proxy). |

**Metric density:** ratio 0.5 · metric-free entries: Dadei, fliks · exemptions applied: Secure and Efficient Autonomous Systems Lab

**Parsed entries:**

| Entry | Section | Bullets |
| ----- | ------- | ------- |
| MindMosaic | experience | 3 |
| Secure and Efficient Autonomous Systems Lab | experience | 2 |
| Robostangs (FRC Team 548) | experience | 2 |
| Dadei | projects | 2 |
| fliks | projects | 1 |

**Skills parsed:** Python, Java, Go, C++, JavaScript/TypeScript, SQL, Bash · AWS (EC2, S3, RDS), Docker, Terraform · Spring Boot, FastAPI · PostgreSQL, Neo4j, Redis · ROS2, Gazebo, AprilTag

## Likelihood

**Resume screen pass:** Medium — strong shipped-intern + ROS2/Gazebo research + FRC sensor fusion in the top half, but C++ gap and Anduril's ~3–5% funnel keep this from "easy yes."

**Overall hire odds:** Medium-Low — resume should clear a human screen at a defense shop with the autonomy thread visible; HackerRank OA and the 4-hr practical onsite are the binding filters per companies.md (~3–5% end-to-end).

**Binding funnel filters:** HackerRank OA (medium LC) → 4-hr practical onsite → behavioral; bottleneck is the practical; ~3–5% acceptance end-to-end.

**What moves the needle (outside the resume):** Apply early (review opens August 2026); target Seattle or Costa Mesa office preference; prep HackerRank medium LC + practical systems questions; a warm referral from an Anduril engineer materially improves screen odds.

## Interview Prep

### What the recruiter is looking for

- Shipped product engineering under real constraints — MindMosaic leads correctly.
- JD languages backed by bullets, not just Skills — especially C++ at a company that ships it on the floor.
- Storage + cloud through use (dual-database routing, Terraform/AWS, Docker/CI).
- Autonomy/perception signal visible early — SEAS Lab in slot 2 satisfies the differentiator without going pure robotics.
- Metrics on production-scale work; triage/debugging/monitoring themes are a plus if organic.

### Gaps on the page

- **Major — C++ skills-only:** The JD names C++ and Anduril's stack is C++-heavy; claiming it in Languages with zero bullet evidence reads as keyword padding at this company.
- **Minor — fliks compressed:** Go depth is one unquantified Postgres-queue line; thinner than the rest of the resume's systems entries.

### Possible misreads

- **C++ in Skills, nowhere in bullets:** A 30-second screen will assume you list C++ for ATS but don't actually use it — worse at Anduril than at a generic SaaS shop.
- **fliks one-liner:** Recruiter may underrate Go/systems depth if this is the only Go evidence beyond the skills line.

### Out of rails (writer could not close)

- C++ not demonstrated in body — no selected bullet names C++ without a swap that would drop higher-priority spine or differentiator signal; remains a skills-list claim only.

## Pipeline Config

<details>
<summary>gate_inputs.json (audit)</summary>

```json
{
  "jd_languages": ["C++", "Go", "Rust", "Java", "Python"],
  "jd_required_keywords": [
    "algorithms",
    "data structures",
    "storage systems",
    "cloud infrastructure",
    "front-end frameworks",
    "metrics",
    "monitoring",
    "debugging"
  ],
  "candidate_languages": ["Python", "Java", "Go", "JavaScript/TypeScript", "C++", "SQL", "Cypher", "Bash"],
  "exempt_entries": ["Secure and Efficient Autonomous Systems Lab"],
  "protected_entries": [
    "Secure and Efficient Autonomous Systems Lab",
    "Robostangs (FRC Team 548)"
  ],
  "lead_signal_window": 2,
  "min_entries": 5,
  "iter1_counts": {
    "MindMosaic": 3,
    "Secure and Efficient Autonomous Systems Lab": 2,
    "Robostangs (FRC Team 548)": 2,
    "Dadei": 2,
    "fliks": 1
  },
  "prefit_counts": {
    "MindMosaic": 3,
    "Secure and Efficient Autonomous Systems Lab": 2,
    "Robostangs (FRC Team 548)": 2,
    "Dadei": 2,
    "fliks": 1
  }
}
```

</details>
