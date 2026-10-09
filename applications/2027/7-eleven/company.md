# 7-Eleven

7-Eleven Inc. is the world’s largest convenience retailer — operator, franchiser, and licensor of convenience stores and one of the nation’s largest independent gasoline retailers. The JD prints **86,000+** locations in the brand family and **77,000+** global stores; Irving, TX is the U.S. Shared Services Center (SSC) and a primary intern hub. Parent is **Seven & i Holdings** (TSE: **3382**). Flagship digital products that sit next to this intern’s work: **7NOW** delivery and **7Rewards** loyalty, plus in-store merchandising at convenience scale. **This intern is not merchandising, not infrastructure, and not a store job.** It sits on a multidisciplinary team of senior engineers, API engineers, and AI engineers building **customer-facing AI products** (conversational shopping and customer support agents) and the **AI platform** behind them: an AI gateway with model routing, an agent-builder framework, MCP services, and observability / evaluation tooling.

## Quick Facts

- **Tier:** C-TIER (`reference/companies.md`) — Fortune-class convenience-retail brand; this *intern* is applied LLM / agent engineering at Irving SSC, peer of Hy-Vee Digital SWE intern / Dick’s Sporting Goods corporate SWE intern / Target Tech intern (retail-tech, resume-first unless an OA is published)
- **HQ / offices:** 7-Eleven Inc. U.S. SSC / intern hub **3200 Hackberry Road, Irving, Texas 75063**. Secondary intern hub **Enon, OH**. This posting: **SSC Irving TX**, on-site
- **Valuation / signal:** World’s largest convenience retailer (JD). Speedway acquisition **~$21B** **[directional, Extern]**. Indeed company rating **3.4/5** from 17k+ reviews **[directional, Extern]**. Military Friendly Employer (Extern)
- **Product focus:** Convenience retail + fuel. **This seat is customer-facing conversational agents + AI platform** (gateway / model routing / agent builder / MCP / eval / observability) — **not** Merchandising Intern **R26_5950**, **not** Infrastructure Specialist Intern **R26_5985**, **not** a generic IT intern
- **Intern comp (2027 AI Engineer Intern, R26_5974):** Unlisted on this JD. Corporate intern **~$24/hr** (Indeed estimate; range **~$23–$27/hr**) + **15¢/gal** gas discount **[directional, Extern]**. Do not treat as this req’s offer
- **Work model:** Paid full-time intern, Summer 2027, typically **10–12 weeks** (careers.7-eleven.com internships page). Workday `timeType` Full time. **On-site Irving, TX** (careers page: currently all internships in person). Posted **2026-10-08**; no Workday `endDate`; `canApply: true` as of **2026-10-09**
- **Clearance / eligibility:** Currently pursuing Bachelor’s or Master’s in Computer Science, Software Engineering, Data Science, Machine Learning, Mathematics, or related, with expected graduation **at least one semester and no more than one year after the internship**. Internships page: graduating within **12 months after completion**. No GPA line on this JD. No citizenship-only / clearance line. Visa sponsorship not printed on this posting — answer the live form honestly (Vedant: US citizen, no sponsorship)

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Resume screen | Workday (`my7elevenhr.wd12` / `Careers`) + human | Mid-size / non-tech-tech retail is resume-first (`recruiting.md` Part I §5). Bottleneck: **resume**. Posted 2026-10-08 — first wave (`recruiting.md` Part II §8). Official: apply → shortlist → recruiter phone → virtual or in-person → offer |
| Recruiter phone | ~20–30 min **[directional, Extern]** | Qualifications, availability, Irving onsite, Summer 2027 |
| Hiring manager | Virtual or in-person | Behavioral + functional (agents / RAG / eval / Python+TS) + convenience-retail fit **[directional, Extern + careers internships page]** |
| OA | Unpublished for **this intern req** | Extern: no formal OA documented for intern candidates. Do **not** invent HackerRank/CodeSignal/HireVue |
| Behavioral | STAR throughout | Filter round (`recruiting.md` §6). JD: present project to team and leadership at end of summer |

**Estimated funnel:** Workday resume → recruiter phone → HM interview (Easy–Med project walk + STAR) · intern OA unpublished · No intern sys design · Bottleneck: **resume** + **Irving onsite relocate** + graduation window · ~15–25% **[directional, C-tier peer of Hy-Vee Digital SWE ~15–25% / Dick’s Sporting Goods SWE intern]**

## Stack & Hiring Signal

- **Languages:** **Python** required; working knowledge of **JavaScript/TypeScript (Node.js) or Java**. Candidate inventory intersection: **Python, TypeScript**. Do **not invent** Java, Node.js-as-used, LangChain (inventory is **LangGraph**), Langfuse, OpenTelemetry, Amazon Bedrock, MongoDB Atlas, OpenSearch
- **Domains:** LLM features (tool/function calling, RAG, multi-step agents) in Python and/or Node.js; eval harnesses (golden datasets, regression tests, automated scoring, trace review); observability (tracing, prompt/version tracking, tool-call monitoring, latency, token usage, cost); model comparison; small services / API integrations / SDK samples / developer tooling on the AI gateway and agent framework; responsible-AI (guardrails, PII, safety testing)
- **What wins:** Python + TypeScript through use (not Skills alone); a shipped LangGraph (or honest analog) agent with an eval loop (LangSmith); RAG / embeddings / pgvector; REST API + AWS/Docker; cost/latency instrumentation as the observability analog. Resume is the intern gate. Dual CS + Economics, GPA **3.7**, U.S. citizen / no-sponsor, Expected May 2028 (inside the one-semester-to-one-year window after Summer 2027), willing to relocate to Irving, are clean knockouts (`recruiting.md` §1 / §8)

## Sibling packets (do not mix)

- **This packet:** Workday **R26_5974** / jobPostingId **AI-Engineer-Intern_R26_5974-1** **AI Engineer Intern**, SSC Irving TX, Summer 2027. Folder: `applications/2027/7-eleven/ai-engineer-intern/`
- **Not this packet:** Infrastructure Specialist Intern **R26_5985** (grad Dec 2027 or May 2028); Merchandising Intern **R26_5950** (business/merchandising; entering final year)

## Sources

- JD: https://my7elevenhr.wd12.myworkdayjobs.com/Careers/job/SSC-Irving-TX/AI-Engineer-Intern_R26_5974-1 (Workday **R26_5974**, posted **2026-10-08**, no `endDate`, CXS `jobPostingInfo.id` `dc53b2410f031012f7b3b58882220000`)
- CXS: `https://my7elevenhr.wd12.myworkdayjobs.com/wday/cxs/my7elevenhr/Careers/job/AI-Engineer-Intern_R26_5974-1` (`includeResumeParsing: true`, `questionnaireId` `5aa85038500d100729e7c8d81ff10000`, hiringOrganization **7-Eleven Inc**, `canApply: true`)
- Careers mirror: https://careers.7-eleven.com/job/irving/ai-engineer-intern/45445/101731048416
- Internships program: https://careers.7-eleven.com/internships (10–12 weeks; Irving + Enon; in person; graduating within 12 months after completion; recruiter phone → interview → offer)
- Extern intern guide (2026-08-27, updated Oct 2026): ~$24/hr; no documented intern OA; rolling Sep–Dec **[directional]**
- `reference/companies.md` C-TIER 7-Eleven row (interview format, bottleneck, acceptance estimate)
- `reference/recruiting.md` Part I §1 / §5 (knockouts; mid-size resume-first), Part II §8 (intern eligibility/timing), Part III §13 (applied ML / GenAI)
