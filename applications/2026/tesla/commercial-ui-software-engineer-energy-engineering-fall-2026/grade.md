# Internship, Commercial UI Software Engineer, Energy Engineering (Fall 2026) at Tesla

## Verdict

- **Score:** 1.0 / 10 (9 demerits — 0 emergency, 2 major, 3 minor)
- **Eligibility:** eligible — Expected May 2028 with a Fall 2026 internship maps to a returning student in good standing for a current-student CS internship
- **Track:** full-stack + energy IoT
- **Pipeline:** 6 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Strong full-stack and real-time signals: React dashboards, WebSocket streaming, Redis Streams reliability, Postgres concurrency patterns, and a 30 Hz device control loop.
- The page reads as a credible production engineer, but the first scan is not a sharp Tesla Energy Commercial UI match — Node.js and GraphQL are missing from demonstrated work, and the energy/IoT fleet story is inferential rather than explicit.
- Page is dense and gate-clean: one page, required languages present, protected differentiator in the top two entries.

### Demerits

- **major** · `resume` · Node.js and GraphQL absent from demonstrated evidence — the role screens for JavaScript/TypeScript, Node.js, React, and preferably GraphQL; the page shows React, FastAPI, Spring Boot, Go, and databases, but no Node.js or GraphQL work, weakening the exact JD stack match
- **major** · `resume` · Tesla energy/IoT differentiator is weakly surfaced — real-time streaming and robot-control evidence exists, but the top story is club operations and generic full-stack infrastructure rather than monitoring, aggregation, or control of device/energy data
- **minor** · `Technical Skills` · TypeScript is listed but not clearly proven in bullets — the skills line claims JavaScript/TypeScript, while the bullets say React and React Query without naming TypeScript-specific implementation or code-quality evidence
- **minor** · `header` · no general GitHub profile link in contact block — for an intern full-stack screen, the header gives a website and LinkedIn but not a direct GitHub profile, leaving the reviewer one step farther from code proof
- **minor** · `Dadei` · approval-control impact is unquantified — the LLM side-effect approval bullet is relevant to reliability and safety, but without a metric, usage count, or failure reduction, the recruiter cannot size the impact

### Misreads

- A rushed recruiter may bucket this as generic club-ops full-stack because the lead experience is a student platform, even though the bullets show React Query, realtime subscriptions, CI/CD, and concurrency-safe RPC work.
- The SEAS lab line can read as pure robotics research rather than device-adjacent control infrastructure, even though the 30 Hz control loop is directly relevant to Tesla Energy's operational surfaces.
- MindMosaic's graph/database depth may be misread as backend-only data engineering with no UI relevance, underselling the shipped product surface.

### Interview angles

- **Lead with:** Dadei real-time WebSocket captions and Redis Streams reliability; Claude Builder Club React Query + live subscription + GitHub Actions deploy path; SEAS 30 Hz physical robot control loop; MindMosaic dual-database latency win.
- **Defend:** Node.js gap — backend depth is FastAPI/Spring Boot/Go with production trade-offs; no pool bullet names Node.js and a second skills line overflows at iter-1 bullet floors *(out of rails: Node.js absent)*. GraphQL gap — not in inventory or bullet pool *(out of rails: GraphQL absent)*. TypeScript — React/TS stack is real but bullets do not name TypeScript verbatim *(out of rails: TypeScript listed but not demonstrated)*.
- **Depth prep:** WebSocket vs polling for live device dashboards; Redis Streams consumer groups, dead-letter routing, and stale-claim recovery; idempotent RPC/check-in concurrency; dual-database read routing; HackerRank medium OA cadence per Tesla funnel.

## Likelihood

- **Resume screen:** Medium — credible full-stack and real-time evidence, but missing demonstrated Node.js/GraphQL and weak explicit energy/IoT framing for this specific req.
- **Overall hire odds:** Low — selective B-tier funnel with HackerRank OA as the binding gate; resume can earn a read but does not de-risk coding screens.
- **Funnel filters:** HackerRank OA (medium) · ~3 rounds · tech rounds bottleneck · ~5–8% estimated offer rate · current-student eligibility.
- **Outside the resume:** Timed DS&A/OA prep and a warm referral/recruiter touchpoint are the highest-leverage moves.
