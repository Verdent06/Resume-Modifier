# Embedded Software Engineering Intern at CoStar Group

## Verdict

- **Score:** 8.0 / 10 (2 demerits — 0 emergency, 0 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 is inside Dec 2027–Jun 2028; GPA 3.66 ≥ 3.0; Junior at Summer 2027 with Fall 2027 remaining (return-to-school); U.S. citizen / no sponsorship
- **Track:** ai-ml + Matterport hardware / 3D capture / camera-LiDAR sensor-test infrastructure (embedded-adjacent)
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- One-page UMich CS intern resume: Voice-AI co-op (ONNX Silero VAD, 40% inference-cost cut; 27% S3 upload recovery), then Pandas ETL on irregular campaign-finance exports (~800 hours / 400 PACs) plus a Flask REST API on AWS EC2, then a LangSmith eval (50%→90%), then LoRA held-out eval (81%→96%) and C++ lock-free / zero-alloc **plugin** — on-axis for a Hardware Systems intern whose requirements test ML/data on messy sensor-like measurements, not firmware.
- Python and C++ are proven in bullets; MATLAB, OpenCV, TensorFlow, MCU firmware, ROS, and a camera/LiDAR internship are not invented.
- Binding ding: Granular has no sized runtime metric (latency / xrun / CPU).

### Demerits

- **minor** · `Granular Synthesizer Plugin` · metric-free — MemoryPool slab and lock-free SPSC show real-time C++ discipline next to a camera/LiDAR test team, but nothing sizes callback latency, xruns, or CPU — a skim can file this as hobby DSP instead of hardware-adjacent systems
- **minor** · `Vylet` · single bullet, PE tagline — One LangSmith eval line (50% to 90%) is real ML-eval evidence, but the founder/PE-search-fund tagline plus a lone bullet reads thinner than CaseStudyPrep/MDC and can skim as GTM SaaS on a Hardware Systems intern page

### Misreads

- Granular without a number can file as "hobby audio intern, no embedded/hardware" before the lock-free C++ / zero-alloc constraint lands.
- Vylet's PE/search-fund tagline plus a lone eval bullet can skim as GTM SaaS; the on-page work is a 20-case LangSmith faithfulness lift.
- Title "Embedded" plus no OpenCV/MATLAB/lab can file as the wrong twin (firmware intern or marketplace Technology Intern) if the reader never reaches the requirements (Python/C++ ML/data on imperfect measurements).

### Interview angles

- **Lead with:** Granular `MemoryPool` / lock-free SPSC (deterministic C++ next to a test-bench team); MDC irregular-Excel Pandas ETL (~800 hours / 400 PACs) as imperfect-data analog; SignalWeaver LoRA 81%→96% held-out + OOS R²; CaseStudyPrep on-device ONNX VAD (40%)
- **Defend:** Granular has no xrun/latency/CPU metric on the page. *(out of rails: pool has no verbatim impact-metric bullet; swap sets cannot invent one.)* Vylet is one LangSmith line under a PE tagline. *(out of rails: adding name-collision overflowed to two pages; tagline is the fixed header.)* No MATLAB, OpenCV, PyTorch-through-use, TensorFlow, MCU firmware, ROS, or camera/LiDAR internship. Voice-AI co-op is on-device inference + upload recovery, not a Matterport camera claim. This is R39950 Hardware Systems / sensor-test — not Irvine Technology Intern, not Vision & Learning
- **Depth prep:** C++ real-time (slab allocators, SPSC, `processBlock` constraints); Python on messy tabular/sensor-like data (Pandas ETL, quality gates); evaluated ML (held-out LoRA, LangSmith adversarial cases); unpublished intern coding analog — LC-mediums in Python or C++. Do not fake OpenCV, MATLAB, LiDAR calibration, or MCU bring-up

## Likelihood

- **Resume screen:** High — eligible, Python through use on imperfect data, held-out ML eval, C++ real-time in the Projects lead window, one clean page; two minors dent the skim, they do not flip it to a no
- **Overall hire odds:** Medium — no published OA, so most front-end elimination is this PDF, then an unpublished Easy–Med practical loop at a ~8–12% B-tier intern accept rate. Sunnyvale relocate and "why hardware / why not firmware" still filter
- **Funnel filters:** Workday `costar.wd1` / `Costar_Campus` resume (`includeResumeParsing: true`, R39950) → recruiter/HM (grad window, GPA 3.0, return-to-school, 10-week/40h, US work-auth / no sponsor, Sunnyvale) → unpublished tech · intern OA unpublished · No intern sys design published · Bottleneck: **resume** · ~8–12% **[directional]** · paid FULL_TIME intern · **$40–$45/hr** · 10 weeks
- **Outside the resume:** Apply in this first-wave window (posted 2026-10-01). Form email `verdent06@gmail.com`. U.S. Citizen; Sunnyvale **Yes**. No CoStar contact in `network.md`
