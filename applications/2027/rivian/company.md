# Rivian

Rivian (Nasdaq: **RIVN**) is a U.S. EV OEM that designs and builds Electric Adventure Vehicles — the **R1T** pickup, **R1S** SUV, the volume **R2** SUV (customer production at Normal started April 2026; first deliveries June 2026), and Amazon **EDV** commercial vans — plus vertically integrated software, autonomy, and propulsion. HQ is **Irvine, CA**; sole operating plant is **Normal, IL** (installed capacity up to **215,000** vehicles/year on the FY2025 10-K). A second plant at Stanton Springs North, Georgia, is under construction (late-2028 R2/R3 capacity). Q2 2026: **$1.658B** revenue, **12,613** vehicles produced at Normal. **This folder is Rivian OEM internships on `careers.rivian.com` — not RV Tech (the Rivian–VW Group SDV JV infotainment intern on Ashby).** This intern req is **Engineering Intern - Supply Chain Data, AI and Business Intelligence (Spring 2027 Co-op)** iCIMS **33800**: Supply Chain & Logistics team allocation at hire; applied ML, optimization, data pipelines, and CI/CD against factory/logistics bottlenecks — not infotainment, not generic SWE.

## Quick Facts

- **Tier:** B-TIER (`reference/companies.md`)
- **HQ / offices:** Irvine, CA (HQ — vehicle engineering/design, supply chain and logistics, IT/software). This intern: **Normal, IL** (Normal factory). Also Plymouth MI (vehicle engineering / prototyping / supply chain), Palo Alto CA (software/autonomy), Carson CA, plus Georgia plant under construction
- **Valuation / signal:** Public **RIVN**. IPO Nov 2021; raised >$13.5B post-IPO. Q2 2026 revenue **$1.658B** (+27% YoY) and gross profit **$179M**. Volkswagen Group investment (2024) funds the separate RV Tech JV — do not mix packets
- **Product focus:** EV OEM manufacturing + factory supply-chain / logistics operations. Intern work is applied data/ML/optimization on Supply Chain & Logistics, not vehicle firmware or infotainment
- **Intern comp (2027 Supply Chain Data/AI/BI co-op, iCIMS 33800):** **$25–$51/hr** for Normal, Illinois (JD pay disclosure)
- **Work model:** Paid Spring Co-Op **Jan–Aug 2027**, **40 hours/week**, **onsite Normal IL** for the entire duration. If unavailable in spring, JD points to the Summer Internship Program. Posted **2026-09-18**. Team allocation discussed at hire
- **Clearance / eligibility:** Must be an **undergraduate or graduate** student in an accredited program **during the entire co-op term** (Role Summary). Qualifications list a Master's in a quantitative field — intern-req copy-paste risk vs Role Summary that still allows current undergrad. No citizenship/export-control line on this posting. iCIMS TCAI matching is opt-out; humans decide

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | iCIMS + TCAI matching (opt-out) + human | AI assists screening/highlighting; humans decide (`companies.md`). First-wave intern stack (`recruiting.md` Part II §8). Bottleneck: resume + tech |
| OA | None published | OEM analog: no standard OA. Do not invent HackerRank/CodeSignal |
| Recruiter / HM | Phone / virtual | Student status through Aug 2027, Normal onsite 40h Jan–Aug, why supply-chain data/ML vs generic SWE |
| Technical | Unpublished intern loop | OEM analog (`companies.md`): **3 rds · Easy–Med · no standard OA**. Applied Python/SQL + ML/pipeline walk more likely than LC grind **[directional]** |
| Behavioral | Filter throughout | Partner with logistics coordinators, demand planners, business leaders (`recruiting.md` §6) |

**Estimated funnel:** iCIMS resume (+ TCAI matching) → unpublished intern loop (OEM analog: 3 rds · Easy–Med · no standard OA) · No intern sys design published · Bottleneck: resume + tech · ~8–12% (`reference/companies.md`)

## Stack & Hiring Signal

- **Languages:** JD floor is **Python and SQL** through use. Named ML frameworks: PyTorch, TensorFlow, Scikit-learn, XGBoost. **Do not invent** Gurobi, COIN-OR, OR-Tools, Spark, Databricks, Snowflake, SAP IBP, Oracle SCM, Blue Yonder, or TensorFlow/XGBoost if they are not in inventory. Honest analogs: Python+SQL pipelines, PyTorch/Pandas through use, AWS (EC2/S3), GitHub Actions CI, GenAI/RAG/agentic only when actually used
- **Domains:** Applied ML + mathematical optimization + data engineering for EV-OEM factory supply chain and logistics (inventory/S&OP analog, demand/logistics bottlenecks). Not ML research. Not LoRA-as-lead. Not audio DSP as lead. Spine: pipelines, analytics, Python, SQL, applied AI
- **What wins:** End-to-end ingest → transform → evaluated model or scored insight → CI/CD analog (`resume.md` Part III §14; `recruiting.md` Part III §13). Python + SQL in bullets, not Skills alone. Resume is the intern gate (iCIMS + human). Dual CS + Economics with stats coursework is the honest quantitative-adjacent degree — do not rewrite the major. Master's-as-qual is not a binary knockout given Role Summary

## Sources

- JD: https://careers.rivian.com/jobs/33800?icims=1 (iCIMS **33800**; JSON-LD `datePosted` 2026-09-18)
- Clera mirror (do not apply here): https://www.getclera.com/jobs/rivian/engineering-intern-supply-chain-data-ai-and-business-intelligence-spring-2027-co-op-cyiw2d18c2v8
- `reference/companies.md` B-TIER **Rivian** row (interview format, bottleneck, acceptance estimate). **Not** the RV Tech row
- Q2 2026 results: https://rivian.com/newsroom/article/rivian-releases-second-quarter-2026-financial-results
- Company / Normal plant: https://rivian.com/our-company
- `reference/recruiting.md` Part I §1 / §5 (knockouts; mid-size resume-first vs OA-gated big tech), Part II §8 (intern eligibility/timing), Part III §13 (applied ML)
