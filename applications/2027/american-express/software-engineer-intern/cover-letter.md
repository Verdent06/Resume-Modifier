Vedant Desai (248) 704-4852 | [vedantde@umich.edu](mailto:vedantde@umich.edu) | github.com/Verdent06 | linkedin.com/in/vedantde06

Dear American Express Campus Recruiting Team,

I'm applying for the 2027 Software Engineer internship with Enterprise Technology Services in Sunrise. I want to spend the summer writing software other people depend on in production — APIs, services, and the pipelines behind them, delivered on a scrum team with real stakeholders. That is what ETS does, and most of what I've built already lives on the finance-adjacent side of that work.

**Production APIs with a real owner on the other end.** At Michigan Data Consulting I was the sole engineer on a five-month contract for the Michigan Campaign Finance Network. I replaced manual campaign-finance research — portal searches capped by the Bureau of Elections, irregular Excel exports, two hours of hand normalization per committee — with a Requests + Pandas ETL that ingests filings directly, eliminating 800 hours of manual pulls across 400 tracked PACs. I then shipped a Flask REST API on AWS EC2 that wired that data and PAC rankings into the nonprofit's public research workflow. I scoped it with MCFN stakeholders myself; there was no backend team to hand ingestion, API design, or deployment to.

**Debugging a live system under constraints.** At CaseStudyPrep.AI I eliminated a 27% audio upload failure rate with fault-tolerant RxJS logic that detects expired S3 presigned URLs, regenerates them mid-flight, and negotiates MIME types Angular was silently rejecting — on an Angular/TypeScript codebase that was already in users' hands. Separately, I cut cloud inference costs 40% by running voice-activity detection client-side so silent frames never left the browser.

**Shipping, then maintaining.** Vylet, the lead-sourcing platform I founded, runs as a Dockerized pipeline with Redis/Celery workers for three paying clients at $1,500 MRR. The part that maps to an ETS sprint isn't the automation — it's the defect work: I traced a name-collision bug in ownership-verification logic that was rejecting valid targets sharing a name with an unrelated business, and the fix lifted lead qualification from 79% to 89% with no change in sourcing volume. SignalWeaver, my financial-research project, is the same discipline: async FastAPI endpoints instrumented at 9.1s p50 / 15.2s p99 across 90 tickers, a React/TypeScript dashboard, Postgres persistence, and Docker Compose plus GitHub Actions CI running pytest on every push to main.

I write Python and TypeScript daily, with SQL alongside them. I haven't shipped Java, Go, or C#, and I'd rather say so than pad a skills line — I'd ramp on whatever my team runs the same way I ramped on Angular and RxJS inside a live product. I graduate in May 2028, I'm authorized to work in the U.S. without visa sponsorship, and I can be in Sunrise on a hybrid schedule for the summer.

Thank you for your time.

Vedant Desai
