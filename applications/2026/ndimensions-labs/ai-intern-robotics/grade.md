# AI Intern, Robotics at Ndimensions Labs

## Verdict

- **Score:** 2.0 / 10 (8 demerits — 0 emergency, 2 major, 2 minor)
- **Eligibility:** Eligible — Expected May 2028; current student with no JD class-year gate
- **Track:** ai-ml + embodied robotics / robotics AI systems
- **Pipeline:** 2 graded cycle(s) · exit: writer_peak

## Screen Review

### First read

- Strong opening for a robotics-AI startup: adversarial robot-policy evaluation, Gazebo-to-hardware sim-to-real, and vision-based autonomy are visible immediately.
- Python ML depth is credible through Dadei's trained wake-word/speaker-ID work, WizViz perception pipeline, and fliks' labeled-data ML loop.
- Binding dings are structural: PyTorch appears only in Skills, and the page still does not read like multimodal/robotics fine-tuning work — the JD's core training stack.

### Demerits

- **major** · `resume` · PyTorch only in skills — The JD names PyTorch as a core ML framework, but the only PyTorch mention is in Skills with no project or research bullet showing model training, fine-tuning, or framework use.
- **major** · `resume` · missing fine-tuning spine — The posting centers on training and fine-tuning multimodal/robotics models plus ablation and policy evaluation; the page shows evaluation and custom-model training, but nothing that reads like foundation-model adaptation, fine-tuning loops, or robotics-policy training.
- **minor** · `fliks` · single bullet, no metric — The ML rating and labeled-data loop is relevant, but one unquantified line makes the data/training contribution hard to size.
- **minor** · `Dadei` · metric-free retrieval path — Hybrid pgvector retrieval and the dual Deepgram/Whisper split are strong systems work, but neither bullet lands a number, so the ML impact reads softer than the quantified speaker-ID and wake-word lines.

### Misreads

- A rushed reviewer may bucket you as a robotics/security researcher rather than an ML training intern because the lab evaluation story leads so strongly.
- A reviewer may read Dadei as generic LLM product work unless you open the interview on the trained wake-word, speaker-ID, and labeled-data loops.

### Interview angles

- **Lead with:** lab adversarial evaluation at 80% and Gazebo-to-hardware deployment; Dadei wake-word training at 90% recall; Robostangs regression A/B model selection against measured shot data.
- **Defend:** PyTorch has no bullet proof because the pool has no verbatim PyTorch bullet *(out of rails: no pool bullet names PyTorch)*; fine-tuning/VLA/robotics-policy training is absent because the pool has no foundation-model or policy-training bullets *(out of rails: pool lacks fine-tuning/RL/imitation-learning bullets)*; fliks scale is thin because a second bullet overflowed the page *(out of rails: second fliks bullet caused 2-page overflow)*.
- **Depth prep:** how you ran the adversarial attack loop, sim-to-real validation on RoboMaster, wake-word training methodology, geometric CV in WizViz, and how you would extend your eval/training experience to multimodal robotics data pipelines.

## Likelihood

- **Resume screen:** Medium — On-axis for embodied AI and evaluation, with real Python ML and robotics evidence, but underweight on the JD's explicit training/fine-tuning stack.
- **Overall hire odds:** Medium — Plausible at a small startup that reads resumes closely and values hands-on experimentation; conversion depends heavily on portfolio links, project walk-through depth, and whether they weight research appetite over missing PyTorch/fine-tuning proof.
- **Funnel filters:** Likely human resume screen at a small team; no OA platform listed; practical ML/robotics discussion expected; Fall 2026 full-time onsite in Boston.
- **Outside the resume:** Submit GitHub/demo links as requested, apply early, and lead your note with the lab eval + sim-to-real story plus one trained-model example from Dadei.
