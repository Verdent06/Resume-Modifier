# Kimley-Horn — Software Developer Intern (Summer 2027)

Cover letter for the typical iCIMS application. Grounded in `persona.md` and real `context.md` work only — no invented projects or metrics. Trim if the form has a character cap.

---

Vedant Desai
(248) 704-4852 · vedantde@umich.edu
linkedin.com/in/vedantde06 · github.com/Verdent06

Kimley-Horn — Technology & Innovation
Cary / Raleigh, NC

Re: Software Developer Intern — Summer 2027 (in-office, Raleigh office)

Dear Kimley-Horn hiring team,

I am applying for the Software Developer Intern role on the corporate team in Raleigh for Summer 2027. I am a B.S. Computer Science and Economics student at the University of Michigan (Expected May 2028, GPA 3.66). I am legally authorized to work in the U.S. without employer sponsorship, and I can work in-office in Cary/Raleigh for the summer.

Kimley-Horn’s Technology & Innovation team builds internal software that practicing engineers actually use — not demo apps. That matches how I like to work: ship a service, sit with the people who depend on it, then fix what breaks.

What I would bring to an iterative, client-facing intern seat:

- **Shipped REST to a real stakeholder.** At Michigan Data Consulting I was the only engineer on a 5-month contract with the Michigan Campaign Finance Network. I delivered a production Flask REST API on AWS EC2 and replaced ~2-hour manual committee pulls with a Requests + Pandas ETL, eliminating ~800 hours of work across 400 tracked PACs. I scoped delivery directly with MCFN — ingestion through REST endpoints — with no backend team behind me.
- **Front-end reliability in Angular/TypeScript.** At CaseStudyPrep.AI I cut a 27% audio-upload failure rate with RxJS logic that regenerates expired S3 presigned URLs mid-flight and negotiates MIME types for WAV files Angular was silently rejecting, and moved processing into a Web Worker so the UI stayed under 5ms of main-thread blocking at 60 FPS.
- **Full-stack web with a database and a deploy.** SignalWeaver is a React/TypeScript dashboard over async FastAPI REST endpoints and Postgres, containerized with Docker Compose and a GitHub Actions CI pipeline (frontend build, pytest, API image). I also run Vylet, a live lead-sourcing product ($1,500 MRR, three paying clients) where I diagnosed a name-collision defect that lifted lead-qualification from 79% to 89% with no change in sourcing volume — the bug-fix / enhancement loop this intern role describes.

I do not have professional C#/.NET or MS SQL Server on my resume. My production backend work is Python (Flask, FastAPI, asyncpg/SQL) and TypeScript/Angular/React on the front end. I am a polyglot OOP intern who has shipped APIs, UIs, relational data, and deploys, and I would ramp onto Kimley-Horn’s Microsoft stack rather than pretend I already have it.

I want this seat because it is internal product work next to the people who use it, in an iterative environment, with a real post-deployment support loop. I would welcome the chance to talk through the MCFN API delivery, the Angular upload-path work, or how I would ramp onto .NET.

Sincerely,
Vedant Desai

---

## iCIMS screening (typical knockout answers)

- **Legally authorized to work in the U.S. without employer sponsorship?** Yes. I do not require sponsorship now or in the future.
- **Pursuing a Bachelor's in CS / IT / related?** Yes — B.S. Computer Science and Economics, University of Michigan, Expected May 2028.
- **Available in-office, Cary/Raleigh, Summer 2027?** Yes. Office hours 7:30a–5:30p Mon–Thu and 7:30a–11:30a Fri are workable for the internship term.
- **Willing to work with business partners / non-engineer users?** Yes — MCFN stakeholder scoping on the 5-month contract is the closest analog; I can walk through requirements → API design → deploy without a backend team behind me.
