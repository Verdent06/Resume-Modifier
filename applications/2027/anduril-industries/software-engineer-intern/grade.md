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
| Iterations | 2 (+ fit pass) |
| Eligibility | eligible — Expected May 2028 ⇒ rising senior for Summer 2027 |
| Track | full-stack + autonomy |

## Reviewer Persona

You are an Anduril technical recruiter screening intern resumes before the HackerRank OA. You have 30 seconds. You want rising seniors who have shipped code to real users or field systems, can work in C++/Go/Python, and show ownership on hard problems—not club logistics. Defense contractors pass on resumes that read like generic web-dev portfolios with no mission-relevant systems signal.

## Scored Defects

| Entry | Severity | Defect | Why | Weight |
| ----- | -------- | ------ | --- | ------ |
| resume | major | C++ skills-only | C++ is listed in Languages but no bullet demonstrates it; Anduril's Notes column flags C++ for embedded/autonomy, so this reads as keyword padding at a company where it is a floor signal. | 3 |
| fliks | minor | single bullet, no metric | Go architectural choice is credible but one unquantified line undersells the storage and media pipeline depth the JD's storage-systems language invites. | 1 |

### What Would Take This to the Next Level

- C++ is on the page in Skills but nowhere in Experience or Projects—at Anduril that looks like ATS padding for a language they actually ship in autonomy and embedded stacks.
- fliks is a single Go line with no throughput or scale number, so the storage-systems depth the posting asks for is harder to size in a quick scan.

## Mechanical Gates

**hard_gates_pass:** true

| Gate | Result | Detail |
| ---- | ------ | ------ |
| required_languages | PASS | All JD languages the candidate has are present: c++, go, java, python. |
| no_orphans | PASS | No orphaned framework/library skills. |
| no_bullet_deletion | PASS | Skipped (fit-check phase). |
| min_entries | PASS | 6 entries (floor 5). |
| protected_depth | PASS | Protected entries retain depth. |
| lead_signal | PASS | Differentiator entry in top 2: Secure and Efficient Autonomous Systems Lab. |
| fit_protection | PASS | Fit drops were project-scoped and protected entries intact. |
| page_fill | PASS | One page, 95% filled. |

**Metric density:** ratio 0.6 · metric-free entries: Claude Builder Club @ MSU, fliks · exemptions applied: Secure and Efficient Autonomous Systems Lab

**Parsed entries:**

| Entry | Section | Bullets |
| ----- | ------- | ------- |
| MindMosaic | experience | 2 |
| Secure and Efficient Autonomous Systems Lab | experience | 2 |
| Robostangs (FRC Team 548) | experience | 2 |
| Claude Builder Club @ MSU | experience | 1 |
| Dadei | projects | 1 |
| fliks | projects | 1 |

**Skills parsed:** Languages: Python, Java, Go, C++, JavaScript/TypeScript, SQL · Frameworks: Spring Boot, FastAPI · Cloud: AWS (EC2, S3, RDS), CI/CD · Robotics: ROS2, Gazebo, AprilTag · Databases: PostgreSQL, Neo4j, Redis

## Likelihood

**Resume screen pass:** Medium — Strong autonomy spine (ROS2 lab + FRC vision in top half) and shipped intern work, but C++ is skills-only at a company where that language is a known hiring signal; early apply window helps.

**Overall hire odds:** Medium — ~3–5% funnel acceptance per company data; bottleneck is the 4-hr practical onsite after HackerRank. Profile is directionally aligned (autonomy + systems + Go/Python) but not a shoo-in against target-school competition.

**Binding funnel filters:** HackerRank OA (medium) → 4-hr practical onsite (bottleneck) · ~3–5% acceptance

**What moves the needle (outside the resume):** Apply early (review begins August 2026); confirm U.S. Person and in-person availability on the Greenhouse form; prep HackerRank medium LC + systems-style practical; referral if any defense/autonomy contact exists in network.

## Interview Prep

### What the recruiter is looking for

- Shipped software with measurable impact (latency, scale, concurrency)—not just project descriptions
- Autonomy or robotics depth: ROS2, simulation, vision, real-time threads
- Multi-language fluency with bullet proof, especially C++/Go at Anduril
- Cloud/storage and operational thinking (metrics, debugging, triage language from JD)
- Mission orientation and ownership—bias for action, low ego

### Gaps on the page

- **Major:** C++ appears only in Skills; no FRC/C++ bullet exists in the pool to close this within rails.
- **Minor:** fliks compressed to one line for page fit—Go/storage story is present but thin.

### Possible misreads

- **C++ skills-only:** A 30-second scan may assume you listed a floor language without systems C++ experience—FRC almost certainly used C++/Java but it is not named on the page.
- **fliks single bullet:** May read as a side project rather than a full storage/media pipeline unless you narrate the Postgres queue and transcode worker in the interview.

### Out of rails (writer could not close)

- **C++ demonstration:** No verbatim pool bullet names C++; Robostangs work is Java/WPILib-framed. Removing C++ from Skills would fail the required-language gate. Gap remains until a defensible C++ bullet is added to `context.md`.

## Pipeline Config

<details>
<summary>gate_inputs.json (audit)</summary>

```json
{
  "jd_languages": ["C++", "Go", "Rust", "Java", "Python"],
  "jd_required_keywords": [
    "algorithms", "data structures", "storage systems", "cloud infrastructure",
    "front-end frameworks", "metrics", "debugging", "monitoring",
    "C++", "Go", "Java", "Python", "Docker", "AWS", "PostgreSQL",
    "CI/CD", "React", "ROS2", "real-time"
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
    "MindMosaic": 2,
    "Secure and Efficient Autonomous Systems Lab": 2,
    "Robostangs (FRC Team 548)": 2,
    "Claude Builder Club @ MSU": 1,
    "fliks": 1
  },
  "prefit_counts": {
    "MindMosaic": 2,
    "Secure and Efficient Autonomous Systems Lab": 2,
    "Robostangs (FRC Team 548)": 2,
    "Claude Builder Club @ MSU": 1,
    "Dadei": 2,
    "fliks": 1
  }
}
```

</details>
