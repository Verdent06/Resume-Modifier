# Virtu Financial — 2027 Internship - Software Engineer · Screening Answers

Draft answers for Virtu’s Greenhouse application (token 8624410002). Grounded in `context.md` and the recruiter lens in `persona.md`. First-person, honest, defensible under “walk me through this” — no invented projects, metrics, Java, or trading-desk internship. Trim to each form’s length limit. Duplicate of the Application Form Answers section in `persona.md`.

Apply: https://boards.greenhouse.io/embed/job_app?token=8624410002

---

## Identity

- **Name:** Vedant Desai
- **Phone:** (248) 704-4852
- **Email:** vedantde@umich.edu
- **LinkedIn:** https://linkedin.com/in/vedantde06
- **GitHub:** https://github.com/Verdent06
- **Resume/CV:** attach `Vedant Desai Resume.pdf` from this folder

---

## Knockouts / facts

**Which university are you currently attending?**
University of Michigan

**Overall GPA**
3.66

**What is your expected graduation year?**
2028

**Will you be ready for full-time employment in 2028?**
Yes. B.S. Computer Science and Economics, Expected May 2028.

**Do you have any outstanding offers or deadlines?**
No.

**What is your office location preference? (Note: The Software Engineer Internship is only available in New York and Austin, not Chicago).**
New York (also available for Austin).

**How did you hear about this internship?**
Jobright

**Are you interested in our Women's Winternship program?**
No

**Do you now, or will you in the future, need sponsorship from an employer in order to obtain, extend or renew your authorization to work in the United States?**
No. US citizen.

**Please only apply to one internship position. If you are interested in other internship tracks, please select them below:**
None — SWE only. Do not select Quantitative Research/Strategist, Quantitative Trading, Site Reliability Engineer, or Trading Operations.

---

## Cover letter (optional)

I want to write software that has to be both fast and correct, and that actually ships. Virtu’s Software Engineer intern role is that job: proprietary low-latency trading systems and tools, scoped to real problems, with senior mentors who expect the work to improve scalability, performance, and efficiency. I am applying to this SWE track only — not Quantitative Research/Strategist, Quantitative Trading, SRE, or Trading Operations.

The work I already do sits on that axis. In C++, I built a granular synthesizer plugin in JUCE where `processBlock()` cannot allocate or take a lock — a per-voice `MemoryPool<Grain, 64>` slab and a lock-free SPSC FIFO so the UI never blocks the audio thread — and I ship it as VST3/AU. In Python, I launched Vylet, a live lead-sourcing product ($1,500 MRR) on Docker/Redis/Celery, and I delivered a production Flask REST API on AWS EC2 as the sole engineer on a five-month nonprofit contract. I do not have a trading-desk internship. I do have CS + Economics at Michigan (Expected May 2028, GPA 3.66), I am a US citizen, and I built SignalWeaver as a financial-research assistant (not investment advice, not a trading desk) with measured p50/p99 on search and scoring.

I am available onsite in New York or Austin for the June 7–August 13 2027 program (free to travel). New York is my preference as HQ and a training-week hub; Austin is fully acceptable. I want to spend ten weeks next to engineers who treat microseconds and production correctness as the job.

---

## Notes for the applicant (not for submission)

- **Do not invent Java or a trading-desk internship.** Interview in C++ or Python. JavaScript is a plus; TypeScript/React on the page is the honest frontend proof.
- **Do not invent a SignalWeaver GitHub.** Link granular-synth: https://github.com/Verdent06/granular-synth
- **OA is the real gate after the resume.** HackerRank 5Q / 75min Easy–Med. Timed C++/Python until a medium is a ~20-minute solve; add probability/brainteaser reps for HR + tech (`recruiting.md`: intern OA; quant/HFT is CP + math heavy).
- **Apply to one intern req.** Do not check other tracks.
- Official weekly: $5,000–$5,800 (JD). Housing/sign-on/meals extra.
