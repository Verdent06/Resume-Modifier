# Software Engineer, Intern (Summer 2027) at Aquatic Capital Management

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** Eligible — Expected May 2028 maps to a current CS undergrad returning to school after Summer 2027; within the JD's Fall 2027–Spring 2028 graduation window
- **Track:** full-stack
- **Pipeline:** 4 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Strong quant-systems screen: MindMosaic leads with a measured 48% latency cut and dual-database routing; Dadei carries Redis Streams at-least-once delivery, worker recovery, and sub-300ms WebSocket streaming — directly on the low-latency distributed-systems bar.
- Python, C++, Go, and concurrency evidence are visible in bullets (not Skills alone): Postgres SKIP LOCKED queueing, atomic RPC check-ins, C++ verifier node with sub-20ms control loop.
- Residual dings are sizing gaps, not missing spine — several throughput/reliability bullets read architecturally strong but unquantified at Aquatic's S-tier bar.

### Demerits

- **minor** · `Claude Builder Club @ MSU` · cache optimization impact is unquantified — React Query cache-tier tuning reads plausible but has no refetch, latency, or load metric to size the win.
- **minor** · `Dadei` · reliability work lacks operating scale — Redis Streams and three-layer restart show judgment, but no event volume, worker count, failure rate, or recovery-time figure.
- **minor** · `fliks` · throughput signal is under-measured — Go worker and Postgres queue are on-axis, but no jobs-per-minute, video volume, or concurrency metric proves high-throughput performance.

### Misreads

- A rushed reviewer may skim the club entry's React Query bullet as frontend product tuning rather than a performance-oriented cache architecture decision — the metric gap makes that misread easier.
- A reviewer may treat Dadei's Redis Streams stack as tutorial event-bus wiring unless you can narrate consumer groups, dead-letter routing, and stale-claim recovery under real load in the interview.
- fliks may read as a small self-hosted side project rather than a throughput pipeline because the queue/worker bullets carry no sizing numbers.

### Interview angles

- **Lead with:** Dadei's Redis Streams event bus (at-least-once delivery, dead-letter after 5 retries, stale-claim recovery) and worker exit-zero recovery; MindMosaic's 48% latency migration and dual-store routing; SEAS Lab C++ verifier and sub-20ms WiFi control loop.
- **Defend:** React Query cache tiers have no refetch/latency metric in the pool *(out of rails: no metric-bearing club cache bullet; onboarding swap trades cache signal for ops)*; fliks throughput is unquantified *(out of rails: all five fliks pool bullets lack throughput/latency numbers)*; Dadei reliability lacks scale numbers *(out of rails: no event-volume/recovery-time metric in pool)*; C++ appears only in robotics-framed SEAS bullets *(out of rails: pool's only C++ is ROS2/Gazebo/RoboMaster)*; no top-level GitHub link *(out of rails: fixed header template)*.
- **Depth prep:** Why Redis Streams over pub/sub for at-least-once; SELECT FOR UPDATE SKIP LOCKED vs external queue; Neo4j vs recursive SQL for graph reads; Deepgram vs Whisper latency split; per-step C++ verifier design; timed medium/hard DS&A and systems-flavored OA prep for quant funnel.

## Likelihood

- **Resume screen:** High — page is tightly aligned with backend/systems SWE and shows real latency, concurrency, queueing, C++, Python, and reliability evidence.
- **Overall hire odds:** Low — Aquatic is an S-tier quant funnel; the binding filters are DS&A/OA and technical depth under interview pressure, not this page. Lack of quant/trading-domain or math-competition signal keeps overall odds low despite a strong resume.
- **Funnel filters:** Greenhouse apply; quant-peer OA/tech screen (algorithms, Python/C++, systems); 4–5 rounds; Chicago onsite Summer 2027; graduation window Fall 2027–Spring 2028; application asks math-competition and prior HFT/prop internship history.
- **Outside the resume:** Apply in the earliest quant wave; pursue warm referral into Chicago quant shops; grind timed DS&A until medium problems are consistent; prep narratable defense of every queue, datastore, and latency decision on the page.
