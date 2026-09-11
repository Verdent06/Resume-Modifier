# Brevan Howard — 2027 Summer Internship Program – Systematic Trading Technology Software Engineer, New York (JR101597) · Workday answers

Draft answers for the live Workday apply on `wd3.myworkdaysite.com` (`BH_ExternalCareers`, job req **JR101597**). Grounded in `persona.md` (full-stack SWE screen + systematic-trading-tech / low-latency / market-data differentiator — **not** JR101591 Systematic Trading / AI&Quant, **not** a trading desk, **not** Java/Excel/VBA/R invention) and `context.md` identity. First-person, honest, defensible under "walk me through this."

**Form-kit email is `verdent06@gmail.com`. Never use `vedantde@umich.edu` on Workday.** Resume PDF header still shows the UMich address (template-fixed). That is the document. The **form** uses Gmail.

**Do not invent Java, Excel, VBA, R, Snowflake, Databricks, Copilot, Fusion, or Tableau.** Honest stack: Python, TypeScript, SQL, C++, Docker, AWS, Git. Trim to each field's limit before submitting.

**Employer / title / location from the live page (2026-09-11):** USIM Brevan Howard US Investment Management LP · **2027 Summer Internship Program – Systematic Trading Technology Software Engineer, New York** · New York (Workday loc New York (1345)), United States · Full time · 10 weeks · **$150,000 annualized** (prorated) + housing stipend + internship completion bonus · posted 2026-09-10.

**Prefer this ATS URL:**
https://wd3.myworkdaysite.com/recruiting/brevanhoward/BH_ExternalCareers/job/New-York/XMLNAME-2027-Summer-Internship-Program---Systematic-Trading-Technology-Software-Engineer--New-York_JR101597

**This agent did not submit.** The public page has **Apply only**. **No form questions were visible without clicking Apply.** Workday questionnaire (`questionnaireId` `426b40bffb5e1001ae6b8c3d0f8f0000`) + apply/start returned **HTTP 406** without an account. This packet does **not** click Apply and does **not** submit. Use the standard Workday identity/knockouts below if the wizard asks them after Apply. Do not invent extra Workday fields as if they were on the page. Paste the cover letter only if a later wizard step has a box.

**Sibling JR101591 Systematic Trading (quant/research) is a different role — do not mix packets.** JD: you may only submit **one** application to the Summer Internship Program globally.

---

## Exact form questions visible on the posting (no Apply click)

None. The public Workday page did not expose screening questions, cover-letter prompts, or knockouts without Apply. The questionnaire API returned HTTP 406. Do not invent extra Workday fields. If the post-Apply wizard asks the usual campus knockouts, use the facts in the next section.

---

## Form-kit identity (Workday — never school email)

| Field | Answer |
| --- | --- |
| Legal First Name | Vedant |
| Legal Last Name | Desai |
| Legal Middle Name | (blank) |
| Email | **verdent06@gmail.com** |
| Phone | **248-704-4852** (Mobile) |
| Address | **49032 Freestone Dr**, Northville, MI **48168** |
| School | University of Michigan |
| Degree / major | B.S. Computer Science and Economics |
| Graduation date | **May 2028** |
| GPA | **3.66 / 4.0** |
| Class | Junior · Expected **May 2028** · Summer 2027 = rising junior / after sophomore year (`context.md`) |
| US citizen | **Yes** |
| Sponsorship now or later | **No** |
| Authorized to work in the U.S. | **Yes** |
| LinkedIn | https://www.linkedin.com/in/vedantde06 |
| GitHub | https://github.com/Verdent06 |
| Resume/CV | `applications/2027/brevan-howard/systematic-trading-technology-software-engineer/Vedant Desai Resume.pdf` |

---

## Knockouts (answer factually)

| Question | Answer | Why |
| --- | --- | --- |
| U.S. citizen / authorized to work | **Yes** | Citizen; no visa |
| Require visa sponsorship (now or later) | **No** | Citizen |
| Currently enrolled / penultimate year undergraduate or junior | **Yes** | Junior, Expected May 2028 — JD bar |
| Degree awarded before July 2028 | **Yes** | May 2028 is before July 2028 |
| Willing to work the 10-week program onsite New York, Summer 2027 | **Yes** | Can relocate for the summer |
| GPA | **3.66** | No numeric floor printed on this JD |
| Languages you can interview in | **Python, TypeScript, SQL, C++** | Do **not** check Java, Excel, VBA, or R |
| Prior Brevan Howard application / employee | **No** | Unless that changes |
| Already applied to another 2027 SIP role globally | **No** (confirm before submit) | JD: one global SIP application |
| Financial / trading-desk experience | **No** | Not required. Do not invent a desk |

If a skills tagger appears, type only: Python, TypeScript, SQL, C++, Linux, Git, Docker, AWS. **Never** Java, Excel, VBA, R, Snowflake, Databricks, Copilot, Fusion, Tableau.

---

## Optional cover / "why this role" paste (only if a later wizard has a box)

Public posting had no cover-letter field. Use only if Workday shows a cover-letter upload, "Additional information," or a free-text box. ~160 words.

I am applying to Brevan Howard’s 2027 Summer Internship Program as a Systematic Trading Technology Software Engineer in New York (JR101597). I want ten weeks on the live trading platform and market-data stack this posting describes — real-time execution services, data capture/normalization/delivery, PM tooling, tests and monitoring — not the Systematic Trading research sibling and not a generic product-SWE summer.

The closest analog I have to low-latency production work is a real-time audio DSP plugin I built from scratch in C++/JUCE. The audio thread cannot allocate or take a lock, so I pre-allocate a `MemoryPool<Grain, 64>` slab per voice and deliver UI parameters through a lock-free SPSC FIFO so `processBlock()` never blocks on the heap or a mutex.

Alongside that I ship Python ingestion and APIs. As the sole engineer on a five-month contract with the Michigan Campaign Finance Network I replaced ~800 hours of manual PAC research with a Requests + Pandas ETL and delivered a production Flask REST API on AWS EC2. I also run production Docker/AWS services (GitHub Actions CI) and have worked messy public datasets into scored, queryable outputs.

I do not have Java, Excel, VBA, or R; Python, TypeScript, SQL, and C++ are the languages I can defend. I do not have a trading-desk internship. I am a Computer Science and Economics student at the University of Michigan (GPA 3.66, Expected May 2028), a U.S. citizen, and I can work the 10-week program in New York.

---

## "Why Brevan Howard / why STT?" (only if a later wizard has a box — ≈90 words)

Systematic Trading Technology is the platform every systematic strategy at the firm uses to reach the market, plus the market-data those strategies depend on. That is the engineering identity I want to sit next to for ten weeks — order execution, market-data delivery, production support — not JR101591 research and not a CRUD shop. I already practice the two signals this screen rewards: lock-free C++ under a hard real-time constraint, and Python/SQL pipelines and APIs that have to be correct in production. I will not invent Java or a desk.

---

## Availability / location

Summer **2027**, 10-week program, **New York**. Available to relocate for the internship. Returning to Michigan after (Expected May 2028). One global SIP application — this is the role and region.

---

## Notes for the applicant (not for submission)

- **Workday email = verdent06@gmail.com.** PDF header is still umich. Fix autofill.
- **No live form questions were found.** Questionnaire API 406. Re-read the live wizard after creating an account; drop any prompt that is not on the page. Do not invent extra essays.
- **Cover letter was not on the public page.** Use the letter only if a box appears.
- **Citizenship YES, sponsorship NO.** No clearance gate on this posting.
- **Never claim Java, Excel, VBA, R, Snowflake, Databricks, Copilot, Fusion, or Tableau.** Java is a JD requirement; it is an honest gap (`persona.md` anti-patterns).
- **No Brevan Howard contact in `network.md`.** How did you hear: Company website / Internet search. Not employee referral.
- **One global SIP application.** Do not also apply to JR101591 or another region with this packet.
- **Funnel (`persona.md` / `companies.md`):** resume + tech are the published bottleneck (~2–5% **[directional]**). Intern OA/loop unpublished; generic sketch is recruiter + 45–60m tech + behavioral. Quant-adjacent bar (`recruiting.md` Part I §5); loop is still general SWE (`recruiting.md` III §11). Resume polish will not hire you if a coding screen appears.
- **This agent did not apply.**
