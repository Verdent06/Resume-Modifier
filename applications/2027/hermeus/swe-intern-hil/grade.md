# Software Engineering Intern (HIL) — Spring/Summer 2027 at Hermeus

## Verdict

- **Score:** 5.0 / 10 (5 demerits — 0 emergency, 1 major, 2 minor)
- **Eligibility:** eligible — GPA 3.66 ≥ 3.0; B.S. CS Expected May 2028; Spring/Summer 2027 internship while enrolled (returns Fall 2027); U.S. person (US citizen) for 22 C.F.R. § 120.62
- **Track:** robotics
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Granular leads: C++ zero-alloc `processBlock`, lock-free SPSC, real-time safety audit — the HIL-adjacent systems read is in slot one.
- CaseStudyPrep backs it with operational debug (27% upload recovery) and a hard real-time constraint (sub-5ms / 60 FPS); MDC is Python scripts/tools on a real contract.
- Binding ding: nothing on the page looks like a bench, board, bus, or comms protocol — a HIL screener can no-pile on the hardware-integration requirement.

### Demerits

- **major** · `resume` · no hardware-integration or embedded-computer evidence — C++ real-time plugin leads, but the page still has no bench, board, sensor, bus, or comms-protocol work. JD hardware-integration / embedded-computer requirement remains unmet.
- **minor** · `Granular Synthesizer Plugin` · metric-free — Zero-allocation pool, lock-free SPSC, and a release-path audit are the right shape for HIL, but there is no sized latency, underrun, or CPU number to size the constraint.
- **minor** · `Vylet` · PE/GTM framing at a HIL intern screen — Header is a PE/search-fund lead-sourcing product at $1,500 MRR. Eval and defect bullets are test-adjacent; a rushed HIL read still buckets this as agentic GTM.

### Misreads

- Granular without a hardware noun or a runtime number can read as hobby DSP rather than test-stand / HIL systems discipline.
- Vylet's PE/search-fund header can erase the eval/root-cause bullets on a 7-second HIL skim.

### Interview angles

- **Lead with:** Granular — zero-alloc `processBlock`, lock-free SPSC, CMake/real-time safety audit; CaseStudyPrep 27% upload-failure recovery and Web Worker / sub-5ms / 60 FPS; Vylet LangSmith eval gates and 79%→89% defect fix as automated-test + root-cause
- **Defend:** No Raspberry Pi / Arduino / STM32 / HIL bench on the page *(out of rails: pool has none; MatchStream is commented out; swap sets cannot bridge)* — say so, then map to signal/debug (audio-thread constraints, WAV/S3 failure recovery). Granular has no xrun/latency/CPU metric *(out of rails: all six pool bullets are architecture/constraint)*. Vylet header is PE/GTM *(out of rails: cannot rewrite header; cannot drop the entry in-loop)* — pivot to eval/root-cause. Do not claim Julia, MATLAB, ROS, or a flight-software internship.
- **Depth prep:** first-principles walkthrough of the audio thread (why no heap, why no mutex); test-planning / failure-analysis on the 27% upload bug; no documented intern OA — recruiter 20–30 min, technical/role-based 30–60 min, final team 15–30 min. Confirm loop with recruiter.

## Likelihood

- **Resume screen:** Medium — Granular-first C++ plus Python scripts, 3.66 GPA, and Expected May 2028 clear the language/GPA/enrollment floor; the hardware-integration hole is the ding that can still no-pile a HIL req.
- **Overall hire odds:** Low — Unrated tiny hypersonic intern cohort; Lever human screen then recruiter 20–30 min and a role-based technical 30–60 min. No embedded/hardware story to defend when the loop asks how you brought up a board or a bench; no OA to equalize.
- **Funnel filters:** Lever resume screen → Recruiter Conversation 20–30 min → Technical or Role-Based Interview(s) 30–60 min → Final Team Interview 15–30 min. No documented intern OA. U.S. person (22 C.F.R. § 120.62) is a form knockout. Bottleneck: resume, then the role-based technical. Acceptance unpublished.
- **Outside the resume:** Apply in the first wave; answer U.S. person and no-sponsorship honestly on Lever; prep an honest hardware-gap map plus a first-principles Granular walkthrough; referral into Atlanta HIL / Flight Software if one exists — this packet is Atlanta HIL only, not LA Modeling & Simulation
