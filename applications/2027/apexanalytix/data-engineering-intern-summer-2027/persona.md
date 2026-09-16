# Data Engineering Intern (Summer 2027) at apexanalytix

Recruiter lens shared by the writer and grader. Abstract bar signals only — no candidate entry names, no include/omit table.

## Role Summary

A paid Summer 2027 intern as **Data Engineering Intern (Summer 2027)** (Rippling **52353bce-cb36-423f-ae0a-f2057ef3b5d9**) at **apexanalytix**. Department: **R&D — Archimedes**. Location: **Greensboro, NC — onsite**. Term: **May through August 2027** (form: able to work in Greensboro May 2027 through August 2027). Compensation: unlisted (C-tier intern $22–38/hr band). Work type: Internship, paid (company-wide benefits language; intern pay unpublished).

**This is not** the Data Science Intern sibling (ML model development), **not** the Data Analyst Intern (on-prem QA), and **not** the IT & Cloud Intern. Do not import a notebook-`model.fit()` spine, a LoRA-as-lead spine, or a generic product-SWE spine. Do **not** mix with Apex Space (`applications/2027/apex/`).

The intern sits on **Archimedes** (cognitive-innovation R&D) and is responsible for developing and deploying **data applications**, deploying into Kubernetes clusters, and building **data pipelines**. Day-to-day: design, develop, and deploy containerized applications; ensure scalability, reliability, and performance; work with LLMs to integrate AI-powered features into products; collaborate with data scientists on pipelines, architectures, and tools that support AI products; troubleshoot pipelines and tools; build UI prototypes (Streamlit or similar) to gather user feedback; stay current on AI, data engineering, and cloud computing.

JD surface is **applied data engineering** (pipelines, Python, SQL, large datasets, containerized data apps, supporting AI products). Company identity for *this* req is procure-to-pay / supplier-data (apexportal + Archimedes R&D) — domain emphasis inside `ai-ml`, not a second engineering track.

## Track Decision

- **screen_track:** `ai-ml`
- **differentiator:** procure-to-pay / supplier-data platform (apexportal + Archimedes R&D)
- **track_divergence:** false

Must-haves: currently pursuing a bachelor's or higher in Computer Science, Data Science, Mathematics, Statistics, Engineering, or related (or associate degree with relevant skills); strong Python with data engineering, data science, or related experience; SQL and database management systems; knowledge of LLMs and their applications in AI product development; familiarity with Docker and Kubernetes; familiarity with NLP, text analysis, and machine learning; problem-solving independently and collaboratively; communication and documentation for non-technical stakeholders.

What the posting *literally tests* is data pipelines, Python, SQL, large datasets, and supporting AI products. That routes to `ai-ml` per `resume.md` Part III §14 (end-to-end data workflow: ingest → transform → insight/serve, **not** `model.fit()` alone) and `recruiting.md` Part III §13 (applied data: ship pipelines and analytics; intern MLOps is a bonus). Same routing as Citizens DE **49285**, Blackstone DE **45022**, Kodiak DE, and TD Bank GTS DE.

It is **not** `full-stack`: title is Data Engineering Intern; the JD does not test product UI or general software delivery as the primary bar. Not `dev-ops` as the spine (Kubernetes is hosting, not SRE; K8s is not in candidate inventory). Not `robotics`. Not ML research (that is the Data Science Intern sibling).

The P2P / supplier-data identity is **domain emphasis inside `ai-ml`**, not a second engineering track (`track_divergence: false`). Spine stays pipelines / Python / SQL. LLMs are product-feature integration (RAG / embeddings / agent orchestration as supporting), not LoRA-as-lead. Do not invent Snowflake, Databricks, Tableau, Copilot, Fusion, Kubernetes-as-claimed-ops, or Streamlit if not in inventory. Docker is inventory; Kubernetes is not. Streamlit is on the JD but not in inventory — omit from bullets; do not Skills-list it.

**Languages JD names:** Python, SQL. (Streamlit / Docker / Kubernetes / LLMs are tools, not languages.)

## Team & Bar

apexanalytix is C-TIER in `reference/companies.md`: privately held P2P / supplier-management + recovery audit; intern DE is Archimedes R&D, Greensboro onsite. Funnel: **Rippling ATS resume → unpublished intern loop (project walk + STAR)**; intern OA unpublished — do not invent HackerRank/CodeSignal; no intern sys design published. **Bottleneck: resume** (~15–25% **[directional, peer of ENFOS / Innovative Systems]**). `recruiting.md` Part II §8: intern eligibility is a hard gate; apply in the first wave. Recruiter voice: an Archimedes / R&D hiring manager or campus recruiter looking for an eligible CS student who can build Python/SQL pipelines and containerized data apps that support AI products — not a research-only ML intern, not a generic SWE intern, not someone claiming Kubernetes/Streamlit/Snowflake they cannot defend.

**Class-year / eligibility (computed, not argued):** JD requires currently pursuing bachelor's or higher (or associate with relevant skills). No class-year exclusive; no GPA floor. Summer 2027 + Expected May 2028 = Junior / rising junior (after sophomore year). Eligible. Resume is the binding intern gate (`recruiting.md` Part II §8). Behavioral remains a filter round (`recruiting.md` §6). Comp unlisted. Onsite Greensboro May–August 2027.

Winning *kinds* of evidence: Python and SQL shown inside real ingest → transform / ETL → quality or monitoring analog → serve (API, database, or product consumer) with a witness metric; Docker containerization of a real pipeline or service through use; LLM/RAG/embeddings as supporting product-AI, not the lead; large or messy / multi-source datasets; documentation or stakeholder-facing delivery. Kubernetes and Streamlit buzzwords without inventory fail. Math/stats coursework and GPA ≥ 3.5 are genuine ai-ml signals (`resume.md` §14). Intern-stage weighting still favors engineered projects + live GitHub (`resume.md` Part II intern). Absence of Kubernetes, Streamlit, Snowflake, Databricks, Tableau is honest — do not invent them.

## Screen Criteria

**Pass signals (abstract — the writer discovers which entries carry them):**
- Python and SQL demonstrated through use in bullets, not only the Skills line (`resume.md` keyword-through-use). Both are required and both are in inventory.
- End-to-end data workflow: ingest messy or multi-source / large data → ETL / transform / normalize → validate, quality-check, or monitoring analog → database, API, or product consumer → measured outcome (`resume.md` §14; `recruiting.md` §13).
- Data pipelines and data applications as the lead story — analog to "building data pipelines" and "developing and deploying data applications" without claiming Archimedes production ownership of Kubernetes.
- Docker containerization of a real pipeline or service through use — analog to "containerized applications" / "familiarity with Docker." Do not claim Kubernetes operations.
- LLM product-feature integration as supporting evidence (RAG, embeddings, agent orchestration with a quality/eval gate) — not LoRA-as-lead, not notebook ML. Analog to "work with LLMs to develop and integrate AI-powered features."
- NLP / text analysis analog through real use (text pipelines, embeddings, retrieval) — familiarity, not a research paper.
- Collaboration with data-science-adjacent consumers — analog to "collaborate with data scientists to develop and deploy data pipelines."
- Stakeholder communication / documentation analog — explain technical work to non-technical users.
- Quantitative coursework (stats, calc) visible in Education; class-year shows current enrollment (`Expected May 2028` vs Summer 2027). GPA on the page (3.66; no JD floor, still a genuine signal).

**Anti-patterns:**
- Generic SWE / full-stack product resume that never shows pipelines, ETL, Pandas, or SQL — wrong role.
- Unmodified GenAI-agentic product lead with no data-engineering analog — this JD is data applications + pipelines supporting AI products, not a product-agent persona as the spine.
- Notebook ML or LoRA-as-lead / `model.fit()` with no pipeline, no quality step, no measured outcome — that is the Data Science Intern sibling, not this req.
- Voice-AI, audio-DSP, or embedded C++ as the lead with no data-pipeline analog.
- Skills-only Python/SQL/Docker/Kubernetes/Streamlit/LLMs with no bullet proof.
- Invented Snowflake, Databricks, Tableau, Copilot, Fusion, Kubernetes-as-claimed-ops, or Streamlit claims (`resume.md` §8 fabrication smell). K8s and Streamlit are JD tools not in inventory — stuffing them is a no.
- Club-ops or community-growth filler occupying prime slots.
- Vanity metrics (uptime, LOC, coverage %) standing in for impact.
- Claiming day-one ownership of enterprise P2P warehouses or production Kubernetes clusters.

## ATS Keywords

Python, SQL, data pipelines, Docker, Kubernetes, LLMs, NLP, machine learning, data applications, monitoring, Streamlit, containerization, data quality, Pandas, PostgreSQL, RAG, embeddings, cloud, Git, FastAPI, ETL
