━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUME GRADING REPORT
Role: LLM Research and Development Technician at Michigan State University (ICER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REVIEWER PERSONA
ICER hires student technicians who can ship Python in a real repo, live in terminals and shared environments, and treat LLM features like systems to test rather than demos to tweet. The bar is not “knows what ChatGPT is”; it is whether you can collaborate with staff, instrument behavior, and explain tradeoffs with evidence. I compare you against other MSU CS students who have coursework projects and maybe a club repo; the differentiator is shipped agentic LLM work plus disciplined CI.

DIMENSION SCORES
─────────────────
Hook Quality:          A — Claude, Dadei, and WizViz hooks all lead with outcomes or wins, not bare stack dumps.
ATS Coverage:          B — 16/21 tracked JD keywords appear in bullets with context; the HPCC/SLURM/research-forum cluster is intentionally absent (honest gap vs. fabrication).
Metric Density:        B — Strong scale and before/after signals on Claude and WizViz; Dadei emphasizes architecture over fresh quantified offline evals.
Tech Justification:    A — pgvector fusion, Redis/RQ, pytest-backed CI, and Gemini tool-calling read as motivated choices, not keyword stuffing.
Role Relevance:        A — Dadei + Claude Builder map directly to agent building, repo collaboration, testing/validation, and CLI-oriented delivery.
Narrative Coherence:   B — Story is “agentic ML systems + disciplined software practice at MSU”; WizViz adds CV/ML breadth but is less central to ICER’s agent job.
Skills Line Fit:       A — Four skill rows read as single-line rows in the compiled PDF (XeLaTeX); no visible wrap in the final artifact.
Page Fit:              A — One page after tightening coursework phrasing, shortening long Dadei lines, and dropping the third WizViz bullet.

OVERALL GRADE: B+

ENTRY BREAKDOWN
─────────────────
Entry: Claude Builder Club @ MSU
Hook Grade: A
Keep: Yes
Hook Assessment: Clear automation outcome with repository collaboration and a hard time/scale signal.
Weakest Bullet: “Hardened how the club ships software…” → Still strong; slightly generic “review standards” compared to the specificity of the first bullet.
Strongest Bullet: “Replaced multi-day manual onboarding…” → Concrete APIs, repositories, channels, and a 97% setup-time story recruiters remember.
Role Fit: Direct evidence of GitHub-centric collaboration and validation culture (coverage gates) that mirrors ICER’s repo + testing expectations.

Entry: Dadei — Ambient AI Assistant
Hook Grade: A
Keep: Yes
Hook Assessment: Immediately reads as an agentic LLM system with tool use and grounding, which is the heart of the JD.
Weakest Bullet: Hybrid retrieval bullet → Dense; a non-ML ICER screener may need a second read, but it still signals retrieval evaluation literacy.
Strongest Bullet: First bullet → Agent framing + Gemini tool-calling + grounded outputs; this is why you get a second look for an LLM technician role.
Role Fit: Strongest project for this posting; closest analog to “build and evaluate an assistant for a technical workflow.”

Entry: WizViz — SpartaHack X
Hook Grade: A
Keep: Yes but deprioritize
Hook Assessment: Win + clear product hook; good credibility signal even if not agent-centric.
Weakest Bullet: (removed third bullet for page fit) — N/A in final resume.
Strongest Bullet: Win bullet → Differentiates you from students with only class projects.
Role Fit: Supports Python + ML runtime discipline; less directly on LLM agents/HPC than Dadei.

WHAT WOULD MAKE ME PASS THIS IMMEDIATELY
─────────────────────────────────────────
1. Any defensible exposure to batch schedulers or Linux cluster basics (even coursework/lab) named explicitly in a bullet.
2. A single line about presenting measurement outcomes (poster, club tech talk, internal demo) if true—ICER explicitly cares about forums and leadership readouts.
3. A tighter one-line “evaluation harness” story (datasets, golden tasks, regression tests for prompts) if you can describe it without unverifiable metrics.

WHAT WOULD MAKE ME REJECT THIS IMMEDIATELY
──────────────────────────────────────────
1. Claiming SLURM/HPCC fluency without a plausible interview story.
2. Inflated offline ML metrics on Dadei that you cannot reproduce or explain.
3. A resume that drifts to two pages or wraps skills—reads as not ready for a support-heavy research computing culture.

CHANGES REQUIRED BEFORE NEXT PASS
───────────────────────────────────
Priority 1 (blocks passing): None for honesty; remaining gap is domain (HPCC/SLURM), which should be handled in a cover letter or interview prep, not fabricated on the resume.
Priority 2 (significantly improves score): Add one sentence in application materials (not necessarily the resume) about how you learn unfamiliar infra from docs and minimal examples—this JD calls that out explicitly.
Priority 3 (marginal improvement): If you ship any small evaluation notebook or pytest suite for agent outputs, reference it succinctly in a bullet.

LIKELIHOOD ESTIMATE
────────────────────
Resume Screen Pass:   High
Rationale: You are an MSU CS student with on-campus leadership and a serious agentic LLM project; for a $15/hr part-time technician role, the signal is unusually strong relative to typical applicants.

Overall Hire Odds:    Medium–High
Rationale: The resume will read as technically overqualified for the pay band, which is good for screening but can raise “will they stay?” questions; the main risk is domain fit on HPC workflows, not coding ability.

Ceiling Without Changes: Interview likely if the hiring manager values LLM implementation depth; may still probe SLURM/filesystems in the conversation.
What Would Move the Needle: Spend 2–3 hours with ICER’s public HPCC getting-started docs and be able to describe a minimal `sbatch` mental model in one paragraph; mention that explicitly in the cover letter.
