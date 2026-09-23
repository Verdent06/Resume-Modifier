# Software Engineer Backend Intern (Summer 2027) at Astranis

## Role Summary

A paid, 12-week, hourly internship on Astranis's Platform team in San Francisco ($29.00/hr). The intern designs and owns backend and infrastructure features used to send commands to space: services that autonomously control satellites, monitor telemetry for anomalies, and give operators real-time situational awareness, plus core services the rest of the software org depends on. The JD surface is Python + databases (Postgres) + pub/sub/streaming (RabbitMQ, Flink as examples), with Kubernetes and fleet-management as bonuses. Astranis's identity is micro-GEO communications satellites and mission-critical fleet-ops ground software — not consumer CRUD, not ML research, and not the Flight Software intern twin.

Form knockouts (US person; SF HQ 5 days/week; 55 hours/week) are apply-form gates, not resume lines. Currently enrolled B.S./M.S. CS; already-graduated candidates are pointed at Associate Engineer.

## Track Decision

- **screen_track:** full-stack
- **differentiator:** aerospace / GEO-satellite / mission-critical / fleet-ops ground software
- **track_divergence:** true

Required qualifications test Python proficiency, relational databases, and pub/sub/streaming understanding — general SWE/backend intern filters (`recruiting.md` Part III §11; `resume.md` Part III §12). They do not name ML frameworks, ROS, or CI/CD-as-the-bar, so the spine is not `ai-ml`, `robotics`, or `dev-ops`. Bonus Kubernetes is not enough to flip the screen track. The differentiator is Astranis's B-tier micro-GEO identity (`companies.md`: Platform services for command, telemetry, anomaly detection, real-time awareness). The resume leads with a full-stack/backend spine (Python services, Postgres-shaped data, async/queue/streaming-adjacent work, APIs, deploy) and keeps real-time / systems / mission-critical reliability prominent and deep — it does not collapse into a DSP specialist page or a generic consumer-web resume.

## Team & Bar

The reviewer is an Astranis Platform intern screener on Greenhouse (human + ATS, AI Talent Matching disclaimer on the posting) before an unpublished intern OA/Coderbyte-or-live-coding step and a Medium tech loop (`companies.md`: bottleneck **resume** then tech; ~5–8% **[directional]**). Recruiter voice: can this intern own a backend/infra feature other operators and satellites depend on — not a tutorial CRUD app, not a notebook. Strong signals: Python in service/API bullets; databases demonstrated through use (Postgres or equivalent relational work); pub/sub, queues, or streaming-shaped systems in bullets rather than Skills-only; visible real-time constraints or reliability/failure recovery so the satellite-ops identity is memorable. Prestige is a tiebreaker, not a gate (`recruiting.md` §8). US person and the 55hr/5-day SF form are knockouts off the page. Inventing Kubernetes, RabbitMQ, Flink, or a fleet-management internship is worse than omitting them.

## Screen Criteria

- JD languages shown through use in bullets where the inventory supports them — Python at minimum — not only on the Skills line (`resume.md` §12 keywords-through-use).
- Databases as a decision (schema, query path, persistence), not a Skills-line slogan. Postgres is the JD example; equivalent relational evidence counts; inventing RabbitMQ/Flink/Kubernetes does not.
- Pub/sub or streaming-shaped work visible as architecture (queues, workers, async delivery, backpressure) — examples on the JD are illustrative, not a license to name tools that were never used.
- Software architecture across backend + infra: APIs/services, data, deploy/cloud. Frontend may appear as supporting evidence; it should not be the lead story for a Backend Intern req.
- Metrics that size real outcomes (latency, throughput, failure recovery, scale) rather than vanity counts or club-ops filler.
- Differentiator visible in the top half: real-time constraints, systems discipline, or mission-critical reliability — without turning the page into a firmware/flight-software document (that's a sibling req) or a consumer-SaaS page with zero systems adjacency.
- Ownership via shipped systems used by others and end-to-end backend/infra delivery — not membership filler.
- Anti-patterns: Skills-only Python/Postgres; invented Kubernetes, RabbitMQ, Flink, ROS, satellite internships, fleet-ops titles, or clearance-in-hand; firmware/FSW packaging as the lead story; notebook ML; club-ops without engineering depth; a PE/GTM or Voice-AI product story that buries the backend/queue/data evidence the Platform screen actually tests.

## ATS Keywords

Python, PostgreSQL, Postgres, databases, pub/sub, streaming, backend, infrastructure, telemetry, satellite, mission-critical, real-time, REST, APIs, Docker, Redis, AWS, CI/CD, reliability, fleet
