# Software Engineering Intern – Summer 2027 at K2 Space Corporation

## Verdict

- **Score:** 7.0 / 10 (3 demerits — 0 emergency, 0 major, 3 minor)
- **Eligibility:** eligible — enrolled B.S. Computer Science at Michigan through Expected May 2028 (Junior in Fall 2027), C++ satisfies the Rust/C/C++/Go requirement, well over six months of out-of-classroom engineering, available for 12+ weeks in person in Torrance, and a U.S. citizen for the ITAR U.S. Person gate; the JD sets no class-year floor
- **Track:** full-stack + high-power satellite flight software / real-time, fault-tolerant, mission-critical systems
- **Pipeline:** 3 cycle(s) · exit: writer_peak

## Screen Review

### First read

- CaseStudyPrep leads with real-time engineering stated as constraints — audio processing moved off the UI thread to hold main-thread blocking under 5ms at 60 FPS, then a 27% upload failure rate eliminated with fault-tolerant retry logic — so the differentiator lands in the top third of the page.
- The general-SWE spine holds underneath: a founder product with a diagnosed defect (79% → 89% qualification rate) and an adversarial test harness (50% → 90% faithfulness), a production Flask REST API on EC2 owned solo, and a containerized stack with a GitHub Actions CI pipeline.
- Binding ding: the C++ real-time entry — zero-allocation audio thread, lock-free SPSC FIFO, real-time safety audit before release — is the most convincing engineering on the page and carries no number, and the closest-to-flight-software signals (bare-metal/RTOS, Linux drivers, HITL) are absent.

### Demerits

- **minor** · `SignalWeaver` · single undescribed bullet, no metric — one containerization line with no descriptor of what the project is and no sized outcome closes the page; against four substantive entries above it, it reads as space-filler
- **minor** · `Granular Synthesizer Plugin` · metric-free — the strongest company-fit entry (zero-allocation audio thread, lock-free SPSC FIFO, real-time safety audit) has no quantified outcome, so a screener cannot size what the discipline bought
- **minor** · `resume` · no embedded, Linux-systems, or hardware-in-the-loop context — real-time depth shown is desktop audio and browser threading; nothing touches bare-metal or RTOS work, Linux systems programming or drivers, HITL/HOTL rigs, or state-machine and control logic

### Misreads

- Without a latency, CPU, or dropout figure, the granular synth can be skimmed as hobby DSP rather than the hard real-time discipline K2's flight software actually rewards.
- A one-line closing project invites the read that the page was padded to length, which slightly discounts the four entries above it.
- Real-time evidence rooted in audio and browser threading can be bucketed as "application software with good latency habits" rather than as adjacency to embedded, bare-metal, or spacecraft-subsystem work.

### Interview angles

- **Lead with:** the granular synthesizer as a real-time systems story — zero-allocation `processBlock()`, the hand-rolled SPSC FIFO with acquire/release ordering, and the pre-release real-time safety audit — then CaseStudyPrep as production real-time work under latency constraints (Web Worker handoff, sub-5ms main-thread blocking, 60 FPS during active inference).
- **Defend:** no quantified outcome on the C++ real-time work *(out of rails: the entry's pool carries only configuration constants — pool size, LUT entries, voice count — never a measured latency or CPU figure)*; no bare-metal, RTOS, Linux-driver, or HITL exposure *(out of rails: nothing in the pool touches firmware, kernel, drivers, or hardware test rigs)* — answer both by naming what you would instrument (worst-case block time, allocation audits, dropout counts) and by mapping the audio-thread constraint model onto a control-loop deadline. Also be ready to explain why the systems-language proof is a personal project rather than a titled role: the JD accepts project experience, so narrate scope and defensibility, not apology.
- **Depth prep:** lock-free concurrency and memory ordering; real-time scheduling and worst-case timing; C++ memory model, allocation strategies, and RAII; state machines for subsystem lifecycle and fault handling; anomaly investigation as a method (the name-collision diagnosis is the transferable story); CI/build systems and test design (CMake, GitHub Actions, adversarial test cases); basic control-systems and computer-architecture vocabulary since K2 lists them as nice-to-haves.

## Likelihood

- **Resume screen:** High — C++ real-time depth with explicit allocation and locking constraints, two before/after fixes with numbers, a measured test harness, and clearly more than six months of shipped out-of-classroom engineering on one clean page.
- **Overall hire odds:** Medium — the page clears the screen and should survive a recruiter call, but a single-seat req with no published intern OA is decided by a practical coding and systems round. Against a ~5–10% funnel where resume plus technical rounds are the bottleneck **[directional]**, the missing firmware/RTOS exposure is what has to be carried live.
- **Funnel filters:** Greenhouse resume screen → recruiter screen → technical (coding/systems, JD languages Rust/C/C++/Go) → behavioral · no standard intern OA published **[directional]** · ITAR U.S. Person gate · ≥12 weeks in person in Torrance.
- **Outside the resume:** Apply within days of the req opening, since a ~300-person company reads its Greenhouse pile early and one intern seat fills fast; work a warm referral into the Torrance software org; and run timed practical coding plus one mock per week on real-time and debugging narratives before the technical round.
