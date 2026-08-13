# Recruiter Persona — Software Engineer, AI Inference Co Design (Fall 2026/Winter 2027) @ Tesla

The shared recruiter lens for the writer and grader. Describes who is screening, what the role tests, and what bar signals look like in the abstract. It names no candidate entries and prescribes no include/omit table.

## Role Summary

Tesla AI is hiring an intern to put large neural networks into production for efficient real-time inference on compute-constrained edge devices — CPU, GPU, and Tesla’s custom AI ASIC. The work sits at the ML/systems intersection: frameworks and infrastructure that train, deploy, and run networks powering vehicles and Optimus. Dual mandate — experiment with novel architectures under tight constraints, then ship the production stack that extracts maximum performance-per-watt from next-gen edge chips (AI5 and beyond).

- **JD surface (what the requirements literally test):** PyTorch (or major ML framework), hands-on training and deploying neural networks, solid computer systems / architecture, CUDA, Python required; C/C++ a strong plus. Day-to-day themes: quantization, compression, distillation, edge-lowering frameworks, fine-tune infrastructure, ASIC co-design for minimum latency.
- **Company identity (what makes a candidate memorable here):** Tesla’s EV + Optimus autonomy stack — real-time, power-constrained silicon in vehicles and humanoid robots, not generic cloud ML. Production-critical ownership and bias for shipping on the most demanding edge hardware.

## Track Decision

- **screen_track:** `ai-ml` — requirements gate on PyTorch, neural-net training/deploy, CUDA, quantization/compression/distillation, edge inference efficiency.
- **differentiator:** autonomy / edge-robotics systems — vehicles + Optimus, custom AI ASIC, real-time power-constrained silicon, HW/SW co-design.
- **track_divergence:** **true.** The literal screen is an applied ML / inference-systems bar; Tesla’s distinguishing identity is autonomy and edge robotics. The page must lead with an AI/ML + inference spine **and** keep real-time systems / constrained-compute / C++ depth prominent — not collapse to notebook ML or generic full-stack.

## Team & Bar

- **Funnel:** B-tier Tesla process — resume screen (human + ATS), HackerRank OA (medium), technical rounds, behavioral for ownership/speed. Bottleneck: tech rounds. Acceptance ~5–8%.
- **Bar:** not a typical internship — ownership of production-critical inference stack pieces. Expects demonstrated model work (train/deploy), systems fluency (architecture, latency, efficiency), and enough low-level or edge signal that CUDA/C++ claims are believable.
- **Recruiter voice:** Tesla AI engineer screening for someone who can reason about performance-per-watt, quantization trade-offs, and shipping inference under hard latency/power caps — not research-only papers or CRUD web apps.
- **Evidence that wins:** end-to-end model workflows with metrics; on-device / edge / ONNX-style inference; systems and architecture depth (memory, threading, latency); Python + C++ polyglot proof in bullets; production ownership and measurable efficiency wins.

## Screen Criteria

**Pass signals (abstract):**
- Python and (ideally) C/C++ demonstrated in bullets, not Skills alone; CUDA or adjacent GPU/edge-runtime evidence when present.
- PyTorch or equivalent ML framework shown through real train/deploy or fine-tune work with honest metrics — not Skills-line decoration.
- Edge / on-device / constrained-compute inference signal (latency, cost, runtime efficiency) near the top of the page.
- Computer-systems depth: architecture-aware engineering (memory pools, real-time constraints, throughput/latency) that maps to ASIC co-design credibility.
- Quantization, compression, distillation, or fine-tuning themes when the page can support them honestly.

**Anti-patterns (no-pile):**
- Notebook ML with no deployment or delivery path.
- Pure full-stack / client-web spine that buries ML and systems signals.
- CUDA/C++ only in Skills with zero bullet evidence.
- Club-ops or GTM/data-consulting filler leading an inference co-design screen.
- Unsupportable “edge AI” claims that collapse under “walk me through this.”

## ATS Keywords

PyTorch, CUDA, quantization, compression, distillation, neural networks, edge inference, real-time inference, computer architecture, computer systems, Python, C++, C, ONNX, fine-tuning, latency, performance-per-watt, AI ASIC, Optimus, Tesla AI, machine learning frameworks, deployment, infrastructure
