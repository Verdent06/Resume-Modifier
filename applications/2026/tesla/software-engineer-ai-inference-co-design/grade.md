# Internship, Software Engineer, AI Inference Co Design (Fall 2026/Winter 2027) at Tesla

## Verdict

- **Score:** 0.0 / 10 (11 demerits — 0 emergency, 3 major, 2 minor)
- **Eligibility:** eligible — Expected May 2028 satisfies JD graduation of 2028 or earlier
- **Track:** ai-ml + autonomy / edge-robotics systems
- **Pipeline:** 2 cycle(s) · exit: writer_peak

## Screen Review

### First read

- Leads with on-device Silero VAD via ONNX Runtime (40% inference-cost cut) plus real-time audio latency — credible edge-inference signal for Tesla AI.
- SignalWeaver adds quantized LoRA fine-tune (81%→96%) and low-latency embedding search; Granular supplies C++ real-time systems / architecture depth.
- Binding dings: CUDA wholly absent, PyTorch Skills-only, and a campaign-finance MDC line that reads as filler on an inference co-design screen.

### Demerits

- **major** · `resume` · CUDA wholly absent — JD lists Experience with CUDA as a bring requirement; the page has no CUDA, GPU kernel, or adjacent GPU-runtime evidence anywhere
- **major** · `resume` · PyTorch only in Skills — JD requires PyTorch proficiency; PyTorch appears only on the Skills line — LoRA/quantized Llama fine-tuning never names the framework
- **major** · `Michigan Data Consulting (MDC)` · reads as filler for inference co-design — Single campaign-finance Pandas ETL bullet with no neural nets, inference, or systems/architecture signal
- **minor** · `Vylet` · agentic lead-gen off-axis for edge inference — Shipped LangGraph/eval product does not map to quantization, edge lowering, or real-time inference co-design
- **minor** · `Granular Synthesizer Plugin` · metric-free systems bullets — C++ zero-allocation and lock-free SPSC depth supports architecture credibility but neither bullet lands a sized impact metric

### Misreads

- A screener may bucket this as “voice-AI / agentic product eng” and miss the edge-inference + quantization thread before reaching SignalWeaver.
- Skills-line PyTorch may be dismissed as keyword stuffing when no bullet names the framework — fine-tune work reads as API/LoRA without framework proof.
- CUDA gap may be read as “no GPU systems experience” despite ONNX Runtime on-device and C++ real-time depth.

### Interview angles

- **Lead with:** CaseStudyPrep ONNX on-device VAD and inference-cost win; SignalWeaver quantized LoRA fine-tune + held-out eval; Granular C++ zero-allocation / lock-free audio-thread systems as architecture credibility for ASIC co-design conversations.
- **Defend:** CUDA absent — honest gap; closest adjacent signal is ONNX Runtime on-device inference and C++ real-time constraints *(out of rails: no CUDA/GPU-kernel bullet in pool)*; PyTorch Skills-only — narrate LoRA/quantized Llama fine-tune as the train/deploy proof even though the framework token is missing on-page *(out of rails: no PyTorch-named bullet)*; MDC filler — keep answers short if asked, redirect to inference/systems work *(out of rails: cannot omit MDC in loop; pool has no on-axis alternate)*; Granular metrics — walk the real-time safety checklist and memory-pool design without inventing numbers *(out of rails: Granular pool has no impact-metric bullets)*.
- **Depth prep:** Quantization vs accuracy trade-offs; ONNX / edge-runtime deployment; computer architecture (caches, memory pools, lock-free queues); HackerRank mediums for Tesla OA; Tesla AI5/edge performance-per-watt framing.

## Likelihood

- **Resume screen:** Medium — ONNX edge lead, quantized LoRA fine-tune, and C++ real-time systems are credible, but CUDA absence, Skills-only PyTorch, and MDC filler will cost callbacks.
- **Overall hire odds:** Low — Tesla B-tier funnel with HackerRank OA and tech-round bottleneck (~5–8%); resume clears a partial ML/systems story, but missing CUDA/framework proof plus OA performance dominate hire odds.
- **Funnel filters:** Resume screen → HackerRank OA (medium) → technical rounds → behavioral (ownership/speed); class-year gate is grad 2028 or earlier (met); onsite Palo Alto; ~12 weeks full-time.
- **Outside the resume:** Apply early in the Fall 2026 window; Tesla AI/autonomy referral; drill HackerRank mediums; rehearse ONNX edge inference, LoRA/quantization, and C++ real-time memory constraints.
