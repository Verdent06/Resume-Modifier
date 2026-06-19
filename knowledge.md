# The Field & The Recruiting Game

> **Scope of this file.** This is the authority on *how software engineering hiring actually works*: the funnel, the timeline, where jobs live, how the interview loop is composed, how to network, and how to negotiate. It is organized along two axes that do not overlap: **lifecycle stage** (intern, new grad, experienced) and **industry track** (general SWE, DevOps, AI/ML, robotics).
>
> **What does NOT live here.** How to build the resume document (formatting, ATS parsing rules, bullet construction, what a recruiter wants on paper). That is `resume.md`. The two files cross-reference; they do not duplicate. When this file says "a robotics resume needs ROS," it means *that field hires for ROS*; the *how-to-write-the-bullet* is in `resume.md`.
>
> **Reliability convention.** Claims are tagged inline where it matters: **[solid]** = official source or peer-reviewed study; **[directional]** = vendor data or aggregated candidate reports, true in shape but not audited; **[forecast]** = projection about a moving target. Default to skepticism on anything not tagged solid. Full sourcing caveats in Part IV.

---

## PART I — UNIVERSAL RECRUITING MECHANICS

*True across every stage and track. Stage-specific deltas live in Part II; track-specific deltas in Part III.*

### 1. The Funnel & The Real Gates

The pipeline for a high-volume engineering role is a sequence of filters, each with its own elimination rate:

```
apply → binary knockout gates → resume screen → online assessment (OA)
      → technical phone screen → onsite/virtual loop → team match → offer → negotiation
```

**The binding gates are not the resume.** Most students over-index on resume polish and under-index on the two filters that actually eliminate them:

- **Binary knockout questions** run before any human or model reads a word: work authorization / visa sponsorship, "are you a current student," and the graduation window. These are auto-reject and absolute. Know your exact status and answer honestly. International students should target programs that do not filter on sponsorship and confirm "returning to school after the internship" eligibility (Microsoft states this explicitly). **[solid]**
- **The online assessment (OA)** is the highest-elimination stage for big-tech high-volume pipelines. Per amazon.jobs (How We Hire), the SDE Online Assessment is the first step for full-time and internship SDE roles; the stated format is ~90 minutes for two coding questions, a systems-design scenario block, and a Work Style Survey tied to Leadership Principles. Candidate reports consistently describe the OA as the stage with the highest elimination rate. **[solid for existence/format, directional for elimination rate]**
- Meta has moved an asynchronous CodeSignal coding screen to the front: a ~90-minute proctored single-problem test in progressive stages, completed *before* meaningful resume or team-match review (new as of 2025). **[directional]**

**Implication:** for Amazon/Meta-class pipelines, LeetCode and data-structures fluency is the real first filter. The resume's depth wins the *team-match and interview*, not the screen. For startups and mid-size firms on Greenhouse/Lever, a human reads the PDF early, so the resume carries more of the front-end weight. **The single most important strategic fact for Ankur: OA is the gate. Treat it as the real filter, not the resume.**

### 2. The Volume & Timing Game

**Volume is a probability machine.** Take a brutal acceptance rate of 1% per application. The chance of zero offers after N applications is `0.99^N`. After 300 applications that is `0.99^300 ≈ 4.9%`, i.e. ~95% odds of at least one offer; after 500 it is `~0.66%`. You do not get an offer by being the perfect candidate at one company; you get it by being a good candidate at enough companies that the math turns in your favor. **The sweet spot cited by practitioners is ~300 applications.** **[directional — illustrative model, not measured rates]**

**Apply early. This is non-negotiable and it is where most students lose.** Three independent reasons:

1. **Apps close fast.** Many high-value reqs open in a window and fill within days to a couple of weeks. A late application is often a closed application regardless of fit.
2. **The early applicant pool is smaller.** Same req, far fewer competitors in the first wave.
3. **Interviews harden later.** The first wave gets the easier loops and the open headcount; by the second wave (roughly Nov→Jan for the summer cycle) interviews get materially harder and slots are scarcer.

**Operationalize it:** applications are rolling, so treat applying as a continuous process with a daily target (e.g. 5 companies/day → ~150/month). Apply until you have an offer in hand, ideally before November. Fill only the required fields; skip optional address/self-ID/etc. unless required, to keep volume high.

**Lining up timelines.** The goal is to have multiple offers live *at the same time*, because simultaneous offers are the only real negotiation leverage (Part I §7). When an early offer threatens to expire before others land, you "punt" it (extend the deadline) and "expedite" the others (compress their timeline). Done right, three offers converge in the same window and you negotiate them against each other. Done wrong, they arrive sequentially and each expires before the next lands, leaving you with zero leverage.

### 3. Process-Level Leverage Tactics

These are universal levers; the exact email scripts are reusable patterns, not one-offs.

- **Punting (deadline extension).** When an offer's expiry is too early, the cleanest lever is your university's recruitment policy. Many career centers publish a guideline (e.g. "offers must remain open until a fixed date such as Nov 30"). Cite it politely and ask the company to align your offer with the policy. This is a legitimate, low-friction extension that recruiters honor routinely. Verify MSU's current career-center policy before citing it.
- **Expediting (process compression).** When you have a competing exploding deadline, tell the *other* companies early and ask if anything can be done to accelerate. A polite, specific note ("I have an exploding deadline on [date], I'm genuinely excited about [company], can we expedite?") frequently moves a process from weeks to days. Recruiters would rather fast-track a motivated candidate than lose them.
- **The 48-hour exploding offer.** If an offer explodes in 48 hours, decline the timeline, not the offer: state plainly that no responsible decision is possible in 48 hours, that you are mid-process elsewhere, and that you take the commitment seriously. They will not rescind for a polite, reasonable ask.

### 4. Networking & Referrals

**Referrals multiply interview odds.** A referral does not guarantee an interview, but it moves your application from the cold pile to a warm read and is the single highest-leverage non-technical action. Build a referral spreadsheet early and work it deliberately.

**Order of who can actually get you an offer** (network up this ladder, not down):

```
Hiring Manager  >  Recruiter  >  Engineer  >  Cold Apply
```

The hiring manager has the most power; an engineer's referral is useful but weaker than a recruiter relationship, which is weaker than HM attention.

**Networking is a two-way street, and people see through transactional outreach instantly.** Reaching out only when you need something leaves a bad impression of you and everything you represent. Genuine relationships mean following up, caring how people are doing, offering your hand when you can, and thanking people when something good happens. This is not a soft nicety; it is the mechanism. Real relationships produce opportunities cold outreach cannot.

**Mechanics** (the detailed outreach scripts live in your outreach playbooks):
- Warm intros first: prior interns, school alumni at the company, community connections.
- Cold email works when it is specific and non-robotic: who you are, a real reason you care about *this* company, one or two genuine accomplishments, no portfolio dump, no ask in the first message for cold contacts.
- Post-conversation: follow up within 24 hours, attach your resume, ask if anything should change before they submit the referral.
- For sourcing contacts: LinkedIn to find the person, an email-finder tool to reach them; this can be partly automated.

### 5. Where Opportunities Live

| Channel | Funnel shape | How to source |
|---|---|---|
| **Big tech (FAANG/MANGO)** | Workday/Greenhouse + OA-gated; resume matters post-OA | Company career pages, internal referrals, aggregators |
| **Startups** | Greenhouse/Lever; a human reads your PDF early; founder-direct works | VC portfolio company pages (YC, a16z, Sequoia, etc.), LinkedIn/X, founder DMs, VC fellowships (Neo, Contrary) |
| **Quant / HFT** | Earliest cycle, highest bar; CP + math heavy | Firm sites, trading competitions, early-engagement programs |
| **Mid-size / non-tech-tech** | Often resume-first, less OA gauntlet | Aggregators, LinkedIn, career fairs |

**Sourcing tools and lists:** Simplify (autofill + tracking), levels.fyi/internships (comp + listings), community-maintained internship GitHub lists, and VC portfolio pages for startups. Career fairs convert well if worked correctly: arrive before booths set up or right as they tear down, go in with a ranked target list, and do not leave a booth without the recruiter's email and notes written on your resume.

### 6. The Interview Loop by Type

Four interview types recur. Which appear, and in what weight, depends on company and level.

- **Coding / DS&A.** The dominant filter. Pattern-based: arrays/strings (two pointers, sliding window), hashing, linked lists, stacks/queues, trees, graphs (BFS/DFS, topological sort), recursion/backtracking, dynamic programming, heaps/intervals. The bar at top firms: comfortably *solve* a LeetCode medium in under ~20 minutes, where solve = understand + code + test. Prep is pattern-first (Grokking/NeetCode/Blind 75), with deliberate timed practice and a running doc of every OA/interview question you encounter.
- **OOP / Low-Level Design (LLD).** "Design a parking lot / elevator / file system / library." Tests class modeling, not distributed systems. Use classes by default; demonstrate inheritance, encapsulation, polymorphism, abstraction; handle edge cases with clean error output; readable naming. Knowledge rarely exceeds intro-OOP plus core data structures.
- **Systems Design.** Mostly new-grad-plus and experienced; rare for interns beyond a light scenario. Resources: ByteByteGo, the standard system-design primers. Quant firms generally skip this (only infra roles ask).
- **Behavioral.** A *filter* round, not a differentiator: doing well does not get you hired, but doing badly gets you rejected. It is low-hanging fruit because it is highly preppable. Keep a journal of what you did; map ~10-12 concrete stories to the company's values framework (for Amazon, the Leadership Principles). This is the gate students most often neglect; allocate explicit time to it.

**Mock interviewing is the scrimmage.** You cannot perform in a real loop without reps. Cadence: 2-3/week in the prep season, ~1/week the week before a real interview. Use interviewing.io, Pramp, peers, and engineers. Schedule real interviews and mocks on Tue/Thu/Fri when possible, and keep a post-interview "reflections" doc of questions, approaches, and what to improve.

### 7. Negotiation — The Offer Game

**Why negotiate:** companies open with their lowest viable number assuming you will sign. You are expensive to hire (a single hire can cost a company well into five figures across sourcing, screens, and interviewer time), which is exactly why they will move for a candidate they have already chosen. They will not rescind for a polite, reasonable ask.

**Leverage, in order of strength:**

```
Competing offers (same industry)  >  Past experience / proven value
    >  Strong alternatives & stated reasons  >  Personal circumstances
```

Competing offers in the *same* industry negotiate best (tech vs tech, quant vs quant). It is hard to negotiate quant against tech. Same-geography comparisons are cleanest (Bay vs Bay, NYC vs NYC) because of cost-of-living adjustments.

**Dimensions you can move** (it is never just base): base salary, signing bonus, equity (RSUs/options), end-of-year bonus, relocation, start date, team/tech assignment, promotion velocity. For interns, comp numbers are usually fixed — negotiate anyway for the practice; full-time is genuinely negotiable.

**The rules that matter most:**
1. Never give the first number. If pushed, deflect to fit; if pushed again, anchor to a market figure rather than your own target.
2. Never sign until the last day — preserve optionality.
3. Get everything in writing.
4. Always keep the door open; be overwhelmingly positive.
5. Don't be the sole decision-maker (a family/external consult is a legitimate, pressure-relieving frame).
6. Have a stated reason for every ask; be motivated by more than money; understand what *they* value; stay winnable.

**Common recruiter plays and the counter:** when a recruiter offers an increase *only if you commit to signing*, they are removing your leverage. Acknowledge the gesture, restate that you cannot commit before your real decision date, and ask them to proceed in good faith. The recruiter is your advocate (they get paid when you do); make them like you, and negotiate like you are making dinner plans with a friend, not issuing ultimatums.

---

## PART II — RECRUITING BY LIFECYCLE STAGE

### 8. Internship Recruiting

**This is Ankur's current stage.** The defining features:

- **Absurdly early cycle.** For a given summer, the strongest reqs open the prior **Aug–Oct** and quant opens even earlier (June). The first wave closes by ~November; the second wave (Nov–Jan) is harder and thinner. Apply within ~72 hours of a req opening.
- **OA-gated at scale.** For big tech, the OA is the real gate (Part I §1). The resume mostly determines team-match after you clear it.
- **Eligibility is a hard gate.** Current-student status and a return-to-school-after-internship expectation are checked; the graduation window must match the program's target class.
- **Underclassman / early-identity programs** exist specifically for freshmen/sophomores and are resume+essay rather than OA-heavy: Google STEP, Microsoft Explore, Meta University, Uber, IBM, and various diversity-forward programs. These are disproportionately valuable early because they convert.
- **Return offers are the prize.** A strong internship converts to a return offer, which is the cleanest path to a new-grad seat (see §9). Optimize the internship itself for conversion: communicate return-offer intent to your manager early so they scope a project that can succeed and showcase you.
- **Prestige is a tiebreaker, not a gate.** No published school filter exists for interns; the documented hard filters are eligibility/knockouts and (for high-volume roles) the OA. School and brand-name prior internships buy a few extra seconds of recruiter attention, nothing more.

### 9. New Grad Recruiting

The first full-time role out of undergrad. A distinct req type ("New Grad" / "University Grad") with its own funnel.

- **Return-offer-first reality.** Most new-grad headcount is filled by converting prior interns. The open-market new-grad funnel competes for the residual seats, which makes it tighter than the intern funnel. The single best new-grad strategy is to have already interned there (or somewhere strong) and convert.
- **Funnel is similar to intern** (OA → loop) but the bar is a notch higher and prior internship experience now carries real weight on the resume.
- **Timeline** runs alongside but slightly behind the intern cycle for the same fall; many new-grad reqs open in the fall of the final year.
- **What changes vs intern:** systems design starts appearing in loops; behavioral expects more substantive ownership stories; the resume leads with internship impact rather than projects/coursework (see `resume.md` Part II).

### 10. Experienced / Lateral Hire Recruiting (1+ years)

Once you have shipped real production work, the game inverts. This is the long-arc target after the first job, not Ankur's near-term cycle, but the structure is worth knowing now because it shapes which early choices compound.

- **The funnel is recruiter- and referral-driven, not OA-gauntlet-driven.** High-volume OA screens largely fall away. The front door is a recruiter reach-out (inbound, often via a strong LinkedIn presence and prior-company brand) or a referral straight to a hiring manager. Cold applications matter far less than at the student stage.
- **Loops shift toward design and depth.** Systems design becomes central; coding rounds remain but are calibrated to level; behavioral becomes scope-and-impact interrogation ("tell me about a system you owned, what broke, what you decided"). Domain-specific deep dives appear (see Part III tracks).
- **Leverage is structural.** Your current total compensation is the floor and an anchor; competing offers and a credible willingness to stay put are real leverage in a way a student never has. Negotiation (Part I §7) is fully in play and the dimensions widen (level, scope, team, refreshers, sign-on to offset unvested equity).
- **Brand and network are the sourcing engine.** Who knows your work, where you worked, and what you shipped drive inbound. This is why the playbook advice to build genuine relationships and a public presence early is not vanity: it is the experienced-hire pipeline forming years in advance.
- **What this means for choices made now:** pick early roles where you ship measurable, narratable production systems; cultivate the relationships and public footprint that later become inbound; treat compounding skills and reputation as the asset, because at this stage they *are* the funnel.

---

## PART III — INDUSTRY / SPECIALIZATION TRACKS

*Each track is self-contained. General SWE / Full-Stack is the foundation every specialization assumes; the three industry tracks describe how that field hires differently. The matching resume guidance is in `resume.md` Part III.*

### 11. General SWE / Full-Stack — The Foundation

The default track and the baseline the others build on. Hiring here is the funnel described in Part I in its purest form: OA-gated at big tech, resume-and-project-first at startups, DS&A-dominant loops, with LLD and (at higher levels) systems design.

- **What it tests:** general CS fundamentals and the ability to ship a working product end-to-end (frontend, backend, API, data, deploy). No domain specialization assumed.
- **Where the jobs are:** the broadest market — every tech company, every startup, most non-tech companies with engineering orgs.
- **Interview flavor:** DS&A coding is the spine; full-stack roles add practical "build/extend a small app or API" rounds at startups. Trade-off fluency (why REST vs WebSocket, why this caching layer) is what separates real from tutorial-grade.
- **The signal that matters:** one or more genuinely engineered, shippable products you can narrate decision-by-decision.

### 12. DevOps / Platform / Infrastructure

Hiring weights deployment fundamentals and operational maturity over feature-building.

- **Where the jobs are:** platform/infra/SRE teams at scaled companies, plus cloud-heavy startups. Demand is steady and less saturated than general SWE at the student level.
- **Stack the field hires for:** Linux + Bash, Python scripting, Docker, Kubernetes, a CI/CD system (GitHub Actions/Jenkins), Infrastructure-as-Code (Terraform is the dominant keyword; Ansible/CloudFormation secondary), a cloud (AWS/GCP/Azure), observability (Prometheus/Grafana).
- **Interview flavor:** DS&A still gates entry, but loops add Linux/networking depth, "debug this broken pipeline/deployment," and scenario questions about reliability, rollback, and on-call. Operational thinking (what breaks, how you'd detect and recover) is the differentiator.
- **The intern-level bar:** *demonstrated deployment curiosity and fundamentals*, not production SRE experience. A documented homelab is increasingly respected by hiring managers as genuine initiative — but only if you can back the claims with hard answers. Tie every tool to a problem you solved; vague "configured a firewall" reads as anyone-with-a-Raspberry-Pi. **[directional]**

### 13. AI / ML

A split field — research, applied ML, and MLOps are three different hiring profiles — but all weight math foundations and demonstrated framework fluency for early-career candidates.

- **Subfields:** *Research* (publications, novel methods, often grad-school-adjacent); *Applied ML* (ship models into products, the largest hiring bucket); *MLOps/ML platform* (serve and scale models — a *bonus* for interns, a *requirement* for full-time; this inversion is the key delta).
- **Where the jobs are:** dedicated ML/AI teams at big tech and AI labs, plus a fast-growing GenAI startup layer (RAG, agents, eval/governance).
- **Stack the field hires for:** Python (lingua franca), PyTorch and TensorFlow (deep learning), scikit-learn/Keras (classical), NumPy/pandas (data), Matplotlib/Seaborn (viz); C/C++ where speed/embedded matters. Math foundations (linear algebra, calculus, probability, statistics) are treated as fundamental and recruiters look for them in coursework/GPA.
- **Interview flavor:** DS&A coding still gates; loops add ML-specific rounds (model design, data-pipeline reasoning, error analysis, sometimes a take-home or live notebook). Demonstrating the *end-to-end workflow* (preprocessing → feature engineering → model selection → cross-validation → error analysis) signals you understand real ML, not just `model.fit()`.
- **Third-party validation that catches ML-recruiter attention:** independent GitHub ML projects, a concrete Kaggle result ("top 5% of 3,000 teams"; even "top 25%" is notable), and any research/publication. Kaggle rank is recognized by ML recruiters specifically but not universally understood; it complements, never replaces, fundamentals and communication. **[directional]**

### 14. Robotics / Autonomy

**Ankur's second track.** Hiring is heavily skewed toward CS fundamentals plus first-hand build/sim experience and an understanding of the hardware-software boundary.

- **Where the jobs are:** autonomy/AV companies (Waymo, Tesla, Aurora, Applied Intuition, Zoox, Cruise), drone/robotics firms, and robotics teams inside larger companies. Production roles dominate over pure-research roles.
- **Stack the field hires for:** C++ and Python are the core (MATLAB common in controls/academia); ROS/ROS2 is near-universal for anything beyond pure research; Gazebo is the headline simulator (also Webots, PyBullet, Isaac); Linux throughout; Git. Concepts: kinematics/dynamics, basic control, sensor fusion, SLAM, localization, navigation, perception. **[solid — multiple 2024–2026 posting studies converge here]**
- **The CS-fundamentals skew is real:** posting studies find the strong majority of robotics-software employers prefer CS expertise, with C++/Python dominant and ROS/ROS2 nearly universal outside research. Translation: DS&A still gates the loop; robotics depth is what wins it.
- **Interview flavor:** DS&A coding (often C++-flavored), plus domain rounds on ROS architecture, coordinate frames/transforms, sensor fusion, control basics, and "walk me through a system you built." Simulation exposure (Gazebo/PyBullet) is read as a maturity signal: you can plan and test before hardware.
- **Competition pedigree is gold and recognized:** FIRST Robotics (FRC/FTC) is a sponsor-valued pipeline (Qualcomm and others recruit FIRST alumni directly). It is a legitimate entry on an autonomy resume, especially before research produces narratable output. **[solid]**
- **Hands-on proof matters more than a skills list:** a portfolio/site and a robotics GitHub are strongly encouraged for this track specifically.

---

## PART IV — Caveats & Sourcing

- **Source quality varies and is tagged inline.** Official career pages (Amazon SDE OA, Microsoft eligibility) and named studies (Ladders eye-tracking; The Construct and CareersInRobotics posting analyses) are high-reliability. Vendor parsing percentages and OA "highest elimination rate" claims are directional, often candidate-reported and sometimes cycle- or region-specific (India-cycle OA reports, for instance). Treat them as shape-of-the-truth, not gospel.
- **The volume math is a model, not a measurement.** The `0.99^N` framing is an illustrative argument for applying broadly, not an empirical acceptance rate. Real per-application rates vary enormously by candidate, company, and timing.
- **No big-tech firm publishes a numeric GPA cutoff.** "3.5" is a market convention, not a Google/Amazon/Meta policy. Reported acceptance rates and cutoffs are estimates.
- **The AI-screening and regulatory landscape is moving fast.** Adoption statistics and regulation timelines (NYC Local Law 144, Illinois HB 3773, Colorado AI Act, EU AI Act high-risk provisions) are in flux; future-tense adoption figures are forecasts.
- **University-specific levers must be verified.** Recruitment-policy deadlines and program eligibility change yearly. Confirm MSU's current career-center policy and any program's stated eligibility before relying on them.
- **Cross-reference:** all resume construction, ATS parsing rules, and bullet/format doctrine live in `resume.md`. This file owns the process; that file owns the document.