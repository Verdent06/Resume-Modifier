# Genesis Molecular AI

Genesis Molecular AI (founded 2019 as Genesis Therapeutics) builds foundation models for small-molecule drug design. The product is GEMS (Genesis Exploration of Molecular Space): generative and predictive models that couple AI with physics, including Pearl, a generative diffusion model for protein–ligand structure prediction. The intern software seat sits next to ML engineers and medicinal chemists — visualization, workflow tooling, and the infra that runs large deep-learning and molecular-dynamics jobs — not a wet-lab rotation and not the sibling ML-research intern reqs.

## Quick Facts

- **Tier:** B (`reference/companies.md` — Good / Solid Resume Addition; AI-drug-discovery peer of Cohere / Mistral intern brand, below Anthropic / OpenAI)
- **HQ / offices:** San Mateo, CA (HQ, 101 S Ellsworth Ave). Fully integrated laboratory in San Diego. New York, NY office. Older public copy still says Burlingame; live intern posting is **San Mateo, CA** with secondary **New York, NY**.
- **Valuation / signal:** Private. JD: **>$300M** raised (a16z, NVentures/NVIDIA, Menlo, Rock Springs, T. Rowe, Fidelity, Radical, BlackRock). Later-stage **$120M** announced May 2026 **[directional, PitchBook]**. Pharma collaborations: Gilead (2024), Incyte expansion (Forbes / GEN May 2026; JD: several-billion potential deal value).
- **Product focus:** GEMS + Pearl — generate and optimize drug molecules; internal pipeline plus AI-pharma partnerships
- **Intern comp (2027 Software Engineer Intern):** Unlisted on this Ashby JD. Do not paste the Fall 2026 BuiltIn/Zero-G scrape ($2,910/mo) as 2027 pay — it is not on this posting and is out of band for Bay Area AI internships **[unverified]**
- **Work model:** Paid Intern. Live posting does not name term length, hybrid vs onsite, or start date. Form asks **start date** and a location pick (San Mateo / San Diego / NYC / Remote). Fall 2026 SWE intern was **onsite San Mateo** **[directional, stale twin]**
- **Clearance / eligibility:** No class-year or GPA printed. Current-student intern implied by title **Software Engineer Intern - 2027**. Form knockouts: US work authorization; sponsorship now or later. No export-control Boolean on this form.

## Interview Process

| Stage | Format | Notes |
| ----- | ------ | ----- |
| Knockouts | Ashby form | US work auth; sponsorship Boolean; location pick; anticipated graduation; internship start date. Binary gates fire before a fair PDF read (`recruiting.md` Part I §1) |
| Resume screen | Ashby (scale-up; human reads the PDF earlier than OA-gated big-tech) | Generic SWE + productionize-ML / infra signal. Do not screen as the PhD ML-research intern |
| OA | None named on this intern req | Unpublished intern loop. Keep Medium Python DS&A warm |
| Technical | Unpublished intern loop | FTE analog: algorithms, scientific computing, light sys design **[directional, InterviewQuery Genesis Therapeutics SWE]** |
| Behavioral | Filter round (`recruiting.md` §6) | First-principles / mission curiosity (JD: biochemistry interest is *willingness to learn*, not a chem degree) |

**Estimated funnel:** Ashby resume → unpublished intern loop · Medium Python DS&A · no named intern OA · light intern sys design unpublished · Bottleneck: **resume** then tech · ~3–8% **[directional, Cohere / Mistral AI intern peer]** (`reference/companies.md`)

## Stack & Hiring Signal

- **Languages:** JD names none. Production software at a molecular-AI lab is Python-heavy (ML, workflows, infra) with TypeScript/React on visualization surfaces. Do **not** invent RDKit, CUDA, PyTorch-as-required, C++/HPC for MD, or biochemistry coursework.
- **Domains:** Molecule/protein visualization, ML-model analysis tooling, chemical-workflow systems, productionizing molecular-property-prediction methods, infra for large DL and molecular-dynamics job fan-out
- **What wins:** Shipped software (APIs, pipelines, containers) **and** applied-ML / ML-infra in the top half (eval, serving, embeddings, inference cost) without pivoting the page to a research-PhD intern. Anti-patterns: notebook `model.fit()` as the lead; invented chemistry stack; club-ops; treating San Diego CMC as the SWE seat.

## Sources

- Live JD / apply: https://jobs.ashbyhq.com/genesis-molecular-ai/44e3cbdc-949c-426e-a80a-b41c73ad6a99/application
- Ashby GraphQL `ApiJobPosting` (`jobs.ashbyhq.com/api/non-user-graphql`; posting `44e3cbdc-949c-426e-a80a-b41c73ad6a99`; form id `f182e4b1-9798-4c6d-b769-0c22e276e15b`; `surveyForms` empty)
- Ashby job-board posting API: published **2026-09-24T17:10:48Z**; department **AI**; team **Engineering**; location San Mateo + NYC secondary
- `reference/companies.md` B-TIER Genesis Molecular AI row
- Company: https://genesis.ml/ · careers https://www.genesis.ml/careers
- Pearl: https://www.businesswire.com/news/home/20251028030745/en/Genesis-Molecular-AI-Unveils-Pearl-a-Field-Leading-Foundation-Model-that-Achieves-Unprecedented-Performance-in-Drug-Protein-Structure-Prediction
- Incyte: https://www.forbes.com/sites/innovationrx/2026/05/20/inside-incytes-120-million-ai-for-drug-development-deal/
- FTE interview analog **[directional]**: https://www.interviewquery.com/interview-guides/genesis-therapeutics-software-engineer
