# Middleware Intern [Winter 2027] at Figure

## Role Summary

Figure is hiring a Winter 2027 Middleware Software Intern (Platform Software, San Jose onsite 5 days/week, $40–$45/hr, minimum 10 weeks) to build the core platform that keeps the humanoid running: C++ on embedded Linux, Python scripts that investigate and resolve issues, and test infrastructure that keeps fixes stable. The JD surface is robot IPC at ~320M messages/hour, data capture/storage, and developer visualization — not firmware board bring-up, not Helix/VLA research, and not a generic product-SWE rotation. The company identity is general-purpose humanoid robotics (Figure 03, Helix 02, BMW Spartanburg logistics).

## Track Decision

- **screen_track:** robotics
- **differentiator:** humanoid AI robotics / real-time platform middleware
- **track_divergence:** false

Required qualifications literally test C++ and Python, Linux, computer architecture, networking protocols, and hardware/software projects outside coursework (`recruiting.md` Part III §14: C++/Python core, Linux throughout, hardware–software boundary; `resume.md` Part III §15). They do not test ROS, perception, controls, or ML training, so the page is a CS-fundamentals robotics/systems resume — not a research-robotics or notebook-ML document. Company identity and screen track agree: humanoid platform software. Lead with first-hand build work and timing-sensitive / lock-free C++ depth; Python debugging and test discipline support the listed responsibilities.

## Team & Bar

The reviewer is an A-tier Greenhouse screener on a specialized Platform Software intern seat before a C++/Python coding challenge and 1–2 systems interviews (`companies.md` Figure: bottleneck resume then C++/lock-free tech; ~2–5% directional intern, peer Applied Intuition / Waymo). Recruiter voice: can this intern ship C++ that cannot miss a deadline on embedded Linux, then write Python to find why it broke? Strong signals: lock-free or shared-memory designs, timing-sensitive hot paths, hardware-adjacent projects outside class, Python used to investigate defects, TypeScript only as a bonus surface. Prestige is a tiebreaker (`recruiting.md` §8). Class-year is a binary knockout on this posting (final-year / graduate student / degree by end of 2026 or 2027) — the resume cannot paper over that form gate.

## Screen Criteria

- C++ and Python demonstrated through use in bullets, not Skills-only (`resume.md` §2 keywords-through-use). TypeScript is a bonus, not a floor.
- Hardware/software or real-time systems work outside coursework — a required JD filter. Audio/DSP or other hard real-time C++ counts; club membership does not.
- Timing-sensitive, lock-free, or shared-memory evidence is the differentiator read once the language floor clears (`resume.md` §15: CS engineer who builds under constraint, not a hobbyist).
- Python for investigation/debug/test, not only ETL or LLM wrappers. Testing-infrastructure adjacency (CI, safety audits, regression-style checks) supports the third responsibility.
- Metrics that size latency, failure recovery, throughput, or allocation constraints — vanity coverage/LOC does not.
- Anti-patterns: Skills-only C++/Linux stuffing; notebook ML or agentic SaaS as the identity of the page; ROS/perception claims the JD does not test and the candidate cannot defend; a consumer-web resume with zero systems/C++ signal; metric-free architecture tours; claiming Bazel or Linux fluency with no backing work.

## ATS Keywords

middleware intern, C++, Python, Linux, embedded Linux, computer architecture, networking protocols, lock-free, shared memory, timing-sensitive, Bazel, TypeScript, testing infrastructure, robot IPC, data capture, visualization, hardware/software projects, San Jose
