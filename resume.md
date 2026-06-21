# Building a Resume That Converts

> **Scope of this file.** This is the authority on *the document*: what a resume is for, how it survives ATS/AI/human review, how to structure it, and how to write every bullet. It encodes the resume doctrine refined over 50+ iterations (see `write-resume` skill) and layers external validation onto it.
>
> **What does NOT live here.** How hiring works — the funnel, timeline, networking, interview loop, negotiation, where jobs live. That is `knowledge.md`. The industry sections in *both* files share names but answer different questions: here, "the robotics resume" means *what the document must contain and lead with*; in `knowledge.md` it means *how that field hires*.
>
> **Relationship to the pipeline.** The Cursor pipeline (`resume-writing.mdc`, `resume-grading.mdc`, `resume-pipeline.mdc`) operationalizes this doctrine. `context.md` holds the canonical bullet pool; the writer selects verbatim with swap-sets; the grader scores against a per-role persona. This file is the *why* behind those rules. **[reliability tags](knowledge.md):** **[solid]** = official source/study, **[directional]** = vendor/aggregated, **[forecast]** = projection.

---

## PART I — UNIVERSAL RESUME DOCTRINE

### 1. What the Document Is For

A resume is a **persuasion document, not a record of employment.** Every decision — what to include, how to phrase it, where to put it — serves one question: *does this make the reader want to meet me?*

It has **three audiences that read the same page simultaneously**, and most candidates optimize for one and fail the other two. Every bullet must satisfy all three:

1. **The ATS / parser** — extracts structured fields and indexes keywords.
2. **The AI screening layer** — semantically scores relevance and increasingly flags synthetic/AI-written resumes.
3. **The human recruiter** — ~7.4 seconds on the first pass. **[solid — Ladders 2018 eye-tracking]**

Hard constraints that follow from this:
- **One page, one column. Never two columns.** Limited content on a clean single column looks substantial and scannable; two columns break parsers.
- **It tells a story.** A reader should be able to state, in one sentence, who you are as an engineer after the first pass ("a SWE with distributed-systems, ML, and production experience").
- Real estate is expensive. Reduce whitespace; every line earns its place.

### 2. ATS / AI Parsing Survival

The modern pipeline is three layers (classic parser → LLM semantic screen → sometimes an AI-detection pass), near-universal at scale (98%+ of Fortune 500 use an ATS). **[solid/directional]**

**Format rules (non-negotiable):**
- Single column, standard section labels ("Experience," "Education," "Skills" — never "My Journey"). No tables, graphics, skill-bars, or images.
- **Contact info in the document body, not the header/footer.** Parsers frequently ignore the header XML layer — candidates have submitted with "no email" because it lived only in the footer.
- Text-based PDF by default; DOCX for stricter parsers (iCIMS, Taleo, Workday auto-fill). Never an image-PDF.
- Platform notes: **Lever** acts on the parsed card first (a parse failure there is costlier); **Greenhouse** stores file + parsed profile and added LLM summaries in late 2025; **Workday** forces extended auto-fill and hosts the knockout questions. **[directional]**

**The #1 student-specific parsing failure: the graduation date.** Gold standard is `Expected May 2027` — the word "Expected" + an abbreviated/spelled-out month + a four-digit year, on its own line in the education entry.
- **Always include the month.** A year-only "2027" is the most common student mistake: parsers cannot tell January from December and may default to Jan 1, distorting the timeline. "Expected May 2027" parses correctly across Workday, Greenhouse, iCIMS, Taleo, and Lever. **[directional]**
- Never leave it blank or write "TBD."

**Keywords: density without stuffing.** Modern NLP understands that "Python programming," "Python development," and "Python scripting" are the same competency, and weights *contextual* use (a tool inside a described project) over a bare skills-list mention. So technologies never appear in isolation — they appear inside the architectural decision that justified them (Redis in a bullet that explains *why* Redis decoupled ingestion from inference). This simultaneously satisfies ATS matching, gives the interviewer something to probe, and gives the recruiter a reason to believe you actually used it.

**The AI-detection pass.** Generic AI-written resumes collapse on screening calls: asked "walk me through this bullet," a candidate who can't narrate the trade-off exposes that the work was generated, not lived. Do not ship bullets you cannot defend.

### 3. Structure & Hierarchy

**Front-load credibility.** The reader's eye lands on the top-left first (F-pattern); the bottom-right is nearly invisible on the first pass. Put your strongest material where the eye lands.

**Section order:** Education (top, because for students with little work history it is one of the six elements recruiters fixate on), then **Experience before Projects** — titled roles, even self-created ones, carry more institutional weight than personal work — then Skills.

**Order within a section by impact density, not chronology.** The strongest entry leads regardless of date.

**The pyramid of what matters** (top = most weight):

```
Shipping code (real, deployed, owned work)
Research / Industry-Adjacent / Leadership
Projects / Products
Clubs / Awards
GPA
Everything else
```

**Education block specifics:**
- Full degree name + abbreviation, school, `Expected Month Year`.
- **GPA only if ≥ 3.5**, combined on a line with honors/awards. Below 3.0, omit it and lean on projects, OA performance, and referrals.
- **Coursework only if it earns its place** — relevant to the role (DS&A for SWE), or a distinctive/specialized offering (OS, distributed systems, ML). Not a course dump.
- Links high and clickable: email, LinkedIn, GitHub, personal site. A missing GitHub is a competitive disqualifier for an engineer.

### 4. Bullets — DRAW (primary), AR (compression), STAR (spoken only)

**One arc at three resolutions.** Lead with the human-readable problem/decision; close with the metric that proves it. The frameworks are the same shape; pick the resolution the moment calls for.

- **DRAW — the authoring model.** **D**ecision (the architectural choice made) → **R**easoning (why; what problem it solved) → **A**ction/feature (what it enables) → **W**itness (the metric, as the *closer*, not the opener).
- **AR — the bullet-level compression.** Action + Result. The situation is embedded in a strong action verb; the result is a number. STAR is too verbose for a resume line — its Situation/Task collapse into the verb. Use AR to tighten a DRAW draft into two scannable lines.
- **STAR — spoken behavioral answers only.** Reserve Situation-Task-Action-Result for the verbal behavioral round, never the page.

**The first bullet of every entry is the hook.** It carries the most weight because it is what gets read when everything else is skimmed. Lead it with the most interesting, human-readable version of *what you built and why it mattered* — the outcome or the problem, **not the technology**. "Replaced paper sign-in sheets with..." beats "Built attendance system" because the reader feels the problem before the solution lands. If a reader sees only the first bullet, they should still leave with a complete, compelling impression. The remaining bullets are technical evidence, going progressively deeper.

**Metrics are non-negotiable — but only the right kind.**
- **Impact metrics only:** latency improvements, throughput, percentage reductions in user-facing wait, scale (concurrent users, members, requests/sec). Lead with the narrative, land the number as the closer.
- **Vanity metrics are rejected:** uptime, lines of code, test-coverage percentages. The test for any number: *does it change how impressive the bullet feels?* If removing it doesn't hurt, it shouldn't be there.
- Target density: roughly **one metric per two bullets**. Not every line needs a number; forcing them produces vanity metrics.

**Economy of language as respect for the reader.** Target **two tight lines per bullet** — long enough to carry depth, short enough to scan. A three-line bullet almost always hides one clause restating something already implied. Editing process: find the least important clause in each bullet, ask whether it earns its space, cut or compress.

**Defensibility test.** Every bullet must survive "tell me about this." If you cannot narrate the trade-off (why this DB, why this caching strategy, what broke and how you debugged it), the bullet is a liability, not an asset.

**Verb discipline.** Past-tense, skill-implying action verbs (architected, optimized, shipped, deployed, engineered, consolidated, orchestrated, refactored, eliminated). When brainstorming an entry, run the *things-to-consider* checklist to surface material: design/architecture, stakeholder collaboration, implementation, testing, deployment/monitoring, visualization, A/B testing, documentation, who you presented to.

### 5. Experience vs Projects vs Skills

- **What counts as an "experience":** internships, any jobs, club *projects* (not memberships), org leadership, shipped products. Self-created titled roles count and outrank personal projects.
- **Projects:** hit the buzzwords through real use (frontend frameworks, backend services, APIs, cloud). List personal projects first, class projects only if needed to fill. Each needs a working GitHub + README. Aim to build 1–2 real projects per semester; "no perfect project exists" — ship and narrate.
- **Skills:** only languages you can actually *interview in* — not a glossary of everything you've touched. Tie tools to the projects that prove them. Include genuine interests (conversation starters with HMs). **Never use star-bars or 1–5 self-ratings.** Be careful what you claim; you will be asked.

### 6. The Iterative Process & Review

The end product takes many iterations (the original doctrine cites ~7 per entry). Per entry:
1. Blank doc, **one experience at a time.**
2. Brain-dump everything you did (aim for 5–10 items) using the things-to-consider checklist.
3. Consolidate to 2–5 items.
4. Apply DRAW, then compress with AR to two lines.
5. Get it reviewed by **many** people; trade resumes with peers to learn from each other.
6. Apply.

AI resume-graders (VMock-style, and your own pipeline grader) are useful for surfacing weak spots — read the *areas to improve*, don't fixate on the score.

### 7. The Modular Resume Principle

A single static resume is a compromise. The endgame is a **base document with swappable components**: projects hot-swapped to the role's stack, bullets reordered to front-load the most relevant work. The resume sent to a DevOps role should *feel* different from the one sent to a product-engineering role even when 80% of the content is identical. This is exactly what the Cursor pipeline automates — verbatim bullet selection from `context.md` with swap-sets, reordered by per-role persona. The doctrine and the tooling are the same idea.

### 8. Common Failure Modes (the no-pile list)

- Year-only graduation date (parser ambiguity).
- Two columns / tables / graphics / skill-bars (parser breakage).
- Generic or business-school templates; contact info trapped in the header/footer.
- Lying or claiming skills you can't defend.
- Vanity metrics (uptime, LOC, coverage %).
- Generic AI-written bullets that collapse under "walk me through this."
- Club-membership padding instead of one deep, measurable involvement.
- The "more is merrier" fallacy: three tight, defensible entries beat five diluted ones.

---

## PART II — RESUME BY LIFECYCLE STAGE

*Brief deltas off Part I. The doctrine is constant; the emphasis shifts.*

### 9. Intern Resume

- Projects and relevant coursework carry **more** weight here than at any later stage — you have little work history, so engineered projects + leadership + a live GitHub are the substance.
- For big-tech high-volume programs, remember the resume mostly determines team-match *after* the OA; invest accordingly (OA prep is the higher-leverage spend), but the resume must still pass the ~7-second scan and hold up in interviews.
- Lead with your single most-engineered project or strongest titled role; education at top with `Expected Month Year` and GPA if ≥3.5.

### 10. New Grad Resume

- **Internships now lead.** Real, titled internship impact moves to the front; personal projects recede to supporting evidence and may drop entirely if internship content is strong.
- Coursework largely disappears; quantified production impact from real roles replaces it.
- Still one page. The bar is a notch higher, so every entry must be defensible at interview depth.

### 11. Experienced / Lateral Resume (1+ years)

- **Impact, scope, and ownership replace coursework and most projects.** The question shifts from "can this person build?" to "what has this person owned and scaled?"
- Reverse-chronological role depth; lead each role with the most consequential system you owned and the measurable outcome.
- Drop the education-heavy framing (degree stays, GPA goes); drop personal projects unless one is genuinely exceptional and role-relevant.
- This resume feeds a recruiter/referral-driven funnel (see `knowledge.md` §10), so it is read by a human early — narrative coherence and quantified scope matter more than keyword survival, though both still apply.

---

## PART III — RESUME BY INDUSTRY / TRACK

*Standalone, not diffs. Each says what the document must lead with, the keywords to hit through real use, and the project archetypes that signal the track. How each field hires is in `knowledge.md` Part III.*

### 12. General SWE / Full-Stack Resume

- **Lead with:** a genuinely engineered, shippable product — ideally one multi-tenant / cloud-native app with real auth and a CI step — narrated decision-by-decision.
- **Keywords through use:** frontend framework (React/Next.js), backend (Node/FastAPI/Spring Boot), APIs (REST/GraphQL), a database, cloud (AWS/GCP), CI/CD.
- **Project archetype:** full-stack app where you can defend every layer's trade-off (why this DB, why this caching strategy, why REST over WebSocket).
- **Signal:** breadth across the stack + depth in at least one layer.

### 13. DevOps / Platform Resume

- **Lead with:** an infrastructure project where you solved a real operational problem — a documented **homelab listed under Projects** (not hobbies) is a respected, interview-starting signal *if* you can back it with hard answers. **[directional]**
- **Keywords through use:** Linux, Bash, Python, Docker, Kubernetes (k3s/Kind/Minikube count), Terraform (dominant keyword), GitHub Actions/Jenkins, AWS/GCP, Prometheus/Grafana.
- **Project archetype:** "Deployed a k3s cluster migrating 8 Docker-Compose services to enable rolling updates"; "Implemented Prometheus/Grafana monitoring." Each tool tied to a problem.
- **Avoid the entry-level trap:** never list "familiar with Docker" with no demonstrated use. Vague "configured a firewall" bullets that "could describe anyone with a Raspberry Pi" add nothing.

### 14. AI / ML Resume

- **Lead with:** a framework project that shows the **end-to-end workflow** (preprocessing → feature engineering → model selection → cross-validation → error analysis), not just `model.fit()`. "Built and trained a CNN that improved image-classification accuracy 15%" is exactly right for an intern.
- **Surface the math:** list linear algebra, calculus, probability, statistics as relevant coursework; a strong GPA in them matters.
- **Keywords through use:** Python, PyTorch/TensorFlow, scikit-learn/Keras, NumPy/pandas, Matplotlib/Seaborn; C/C++ where relevant.
- **Third-party validation:** a concrete **Kaggle result** ("top 5% of 3,000 teams"; even "top 25%" notable), independent ML GitHub projects, any research/publication. **[directional]**
- **MLOps is a bonus for interns, a requirement for full-time** — don't fake production-scale serving; show the modeling workflow instead.

### 15. Robotics / Autonomy Resume

- **Lead with:** first-hand build experience and, where available, simulation work. **FRC/FTC is a legitimate, sponsor-valued entry** — frame it with technical specifics and impact ("Led 8 engineers to design, build, and program a competitive robot in C++/Java; advanced to FIRST World Championship"); mentoring/outreach reads as genuine teaching-pipeline leadership. Use it as a bridge entry until research produces narratable output, then compress it.
- **Keywords through use:** ROS/ROS2, Gazebo (also Webots/PyBullet), C++, Python, Linux, Git; concepts: kinematics/dynamics, control, sensor fusion, SLAM, localization, navigation, perception.
- **Project archetype:** "Built a Gazebo simulation environment that accelerated testing"; "Developed robotic-arm control software in C++ to optimize picking speed 20%"; "Created a SLAM pipeline that reduced mapping error 15%."
- **The CS-fundamentals skew is real** — the field hires C++/Python + ROS heavily, so the resume should read as a strong CS engineer who builds robots, not a hobbyist.
- **Portfolio + GitHub strongly encouraged for this track specifically** — hands-on proof beats a skills list. Note: the Cursor pipeline currently has no robotics `.tex` template (only full-stack, ai-ml, dev-ops); add one if this track stays active.

---

## PART IV — Caveats & Sourcing

- **Tags are inline.** Format rules and the eye-tracking 7.4s figure are well-sourced; specific parse-fidelity percentages and the homelab/Kaggle weighting are vendor- or community-reported and directional. The grad-date and single-column rules are the highest-confidence, highest-leverage moves.
- **Parsers are imperfect even on clean docs** — best commercial parsers top out near 87% field-level accuracy vs ~96% for humans, so ~1 in 8 fields can break on a clean resume. This is *why* the format rules are strict, not pedantic.
- **The AI-screening landscape moves fast** — AI-detection adoption and synthetic-resume flagging are partly forecast; don't treat any single adoption statistic as settled.
- **Cross-reference:** the funnel, timeline, networking, interview loop, and negotiation all live in `knowledge.md`. This file owns the document; that file owns the process. The pipeline `.mdc` files operationalize this doctrine; `context.md` is the canonical bullet pool.