# Resume Grading Report — Iteration 1
**Role:** Software Engineer, Intern - Summer 2026 at Visa

---

## REVIEWER PERSONA

I'm hiring for Visa's Technology org in Austin. We place interns in real teams—platform, payments, internal tools, data—and expect them to ship something concrete over the summer. We care about: one strong language (Java/Python/JS), ability to write testable code and follow CI/CD, and clear communication. Past intern projects include Kafka on K8s, chatbots, payment automation, and testing/monitoring tools. I need to see evidence of hands-on coding, testing, and collaboration; keywords like Kubernetes, REST, unit test, and automation matter for both ATS and my skim. I'm comparing this resume to hundreds of others; hooks and role fit need to land in the first pass.

---

## DIMENSION SCORES

| Dimension | Grade | Rationale |
|-----------|--------|------------|
| Hook Quality | B | First bullets are outcome-led and clear (onboarding eliminated, latency cut, agentic assistant, hackathon win). MindMosaic opens with Neo4j/PostgreSQL—slightly tech-first for a 7-second read; still strong. |
| ATS Coverage | C | ~44% of JD keywords appear in bullets (Software Engineer, Python, Docker, REST, CI/CD, unit test, automation, deployment, API). Kubernetes, MySQL, NoSQL, Jenkins, testing principles are in skills only; Selenium, Cassandra, microservices, RDBMS missing. Bullets carry more weight; 80% not reached. |
| Metric Density | A | Before/after latency, percentages with absolutes, FPS/lag, coverage counts. No vanity metrics. |
| Tech Justification | A | Technologies tied to decisions (Neo4j for traversals, Redis/Celery for async, Docker for deployment, GitHub Actions for gates). |
| Role Relevance | B | Full-stack template fits. CI/CD, testing, and APIs are surfaced; ordering is reasonable. Kubernetes and testing could be slightly more prominent in bullets. |
| Narrative Coherence | A | Clear thread: automation, backend/data, APIs, deployment, quality. Reads as one engineer. |

**OVERALL GRADE: B-**

---

## ENTRY BREAKDOWN

**Entry: Claude Builder Club @ MSU**  
- **Hook Grade:** A  
- **Keep:** Yes  
- **Hook Assessment:** "Eliminated manual onboarding" lands immediately; 97%, 30 seconds, 100+ members give scale and impact.  
- **Weakest Bullet:** QR check-in — less directly relevant to Visa's stack; still shows automation and systems thinking.  
- **Strongest Bullet:** GitHub Actions CI/CD with unit test coverage — direct match to JD.  
- **Role Fit:** High — automation, CI/CD, testing, collaboration.

**Entry: MindMosaic**  
- **Hook Grade:** B  
- **Keep:** Yes  
- **Hook Assessment:** Strong technically (Neo4j, latency cut) but leads with tech; "Introduced Neo4j" is slightly tool-first.  
- **Weakest Bullet:** OAuth/JWT bullet — valuable for security but not top for this JD.  
- **Strongest Bullet:** GitLab CI/CD with Docker, unit test, 85% coverage — aligns with JD.  
- **Role Fit:** High — RDBMS (PostgreSQL), CI/CD, Docker, unit testing.

**Entry: Mira**  
- **Hook Grade:** A  
- **Keep:** Yes  
- **Hook Assessment:** "Agentic voice assistant" and "dispatches real tasks" signal product + systems; outcome-first.  
- **Weakest Bullet:** Electron/OAuth callback — more client detail than Visa needs.  
- **Strongest Bullet:** REST API 73% reduction + Redis/Celery; cold-start 86% reduction — clear impact and stack.  
- **Role Fit:** High — REST, APIs, async, deployment, ML-adjacent (JD likes agentic/ML).

**Entry: WizViz**  
- **Hook Grade:** A  
- **Keep:** Yes  
- **Hook Assessment:** "Won Interactive Media Track" + gesture-controlled duel — immediate differentiation.  
- **Weakest Bullet:** 2D vector physics engine — impressive but less aligned to Visa's backend/tooling.  
- **Strongest Bullet:** 60 FPS, sub-20ms lag, MediaPipe — shows performance mindset.  
- **Role Fit:** Medium — Python, performance; not directly payments/infra.

---

## WHAT WOULD MAKE ME PASS THIS IMMEDIATELY

1. **Kubernetes or Jenkins/GitHub Actions in a bullet** — not just skills (e.g., "CI/CD with Docker and Kubernetes" or "GitHub Actions" already in Claude Builder Club—good; one more explicit K8s or pipeline tool in a bullet would help).  
2. **Explicit "software testing" or "root cause analysis"** in one bullet — JD stresses testing principles and defect resolution.  
3. **RDBMS or NoSQL in a bullet** — e.g., "RDBMS (PostgreSQL) and NoSQL (MongoDB/Neo4j)" in MindMosaic or Mira so ATS and I see it in context.

---

## WHAT WOULD MAKE ME REJECT THIS IMMEDIATELY

1. No evidence of testing or quality (we have it).  
2. No collaboration or team signal (Vice President + multi-member setup is enough).  
3. Wrong graduation date (May 2028 fits Dec 2026–Aug 2027 for *intern* cohort; JD says Dec 2026–Aug 2027 graduation—that's for interns graduating in that window. Ankur Expected May 2028 is one year later, so he'd be summer-after-sophomore. JD says "graduation date in December 2026-August 2027" — that targets students a year ahead. This could be a gap; I won't reject for it but it's a possible screen. Actually re-read: "graduation date in December 2026-August 2027" means the *intern* class is for people graduating then, i.e. undergrads finishing in that window. Ankur May 2028 would be graduating a year later, so he might be in the next year's cohort. I'll note it in gaps, not as reject.)

---

## CHANGES REQUIRED BEFORE NEXT PASS

**Priority 1 (blocks passing):**  
- **ATS in bullets:** Get 2–3 more JD keywords into bullets, not only skills. Add "Kubernetes" or "containerized" in the MindMosaic Docker/CI bullet; add "RDBMS" or "NoSQL" in the MindMosaic Neo4j/PostgreSQL bullet (e.g., "offload recursive queries from PostgreSQL (RDBMS) to Neo4j (NoSQL)"); add "software testing" or "test design" in the Claude Builder Club or MindMosaic testing bullet.

**Priority 2 (significantly improves score):**  
- **Hook for MindMosaic:** Optionally rephrase the first bullet to lead with outcome (e.g., "Cut p95 latency 48% by offloading recursive relational queries from PostgreSQL to Neo4j...") so the hook is impact-first, not "Introduced Neo4j."  
- **One "testing principles" or "root cause" phrase** in a bullet to match JD language.

**Priority 3 (marginal):**  
- WizViz is fine; no change needed for this role.

---

## ITERATION VERDICT

**Needs another write pass.**

@resume-writing should: (1) Inject into bullets: Kubernetes/containerized in MindMosaic CI/CD bullet; RDBMS and/or NoSQL in MindMosaic database bullet; "software testing" or "test design" in a testing bullet. (2) Consider making MindMosaic hook outcome-first (latency cut first, then Neo4j). (3) Add one "root cause analysis" or "defect" or "testing principles" phrase if it fits without padding. Do not change metrics or add new sections.
