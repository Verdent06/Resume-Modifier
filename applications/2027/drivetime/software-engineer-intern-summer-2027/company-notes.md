# DriveTime Workday — company notes (R16294)

Tenant: `drivetime` · site: `DriveTime` · host: `drivetime.wd1.myworkdayjobs.com`

Req: **R16294** · Software Engineering Intern (Summer 2027) · Tempe Home Office (1720 W Rio Salado Pkwy, Tempe, AZ 85281)

Apply: https://drivetime.wd1.myworkdayjobs.com/DriveTime/job/1720-W-Rio-Salado-Pkwy-Tempe-AZ-85281/Software-Engineer-Intern--Summer-2027-_R16294

Probed live **2026-09-04**. Application **not submitted**. Throwaway account used only to reach My Experience / Application Questions.

## SHA-256 (packet PDF)

File: `applications/2027/drivetime/software-engineer-intern-summer-2027/Vedant Desai Resume.pdf`

```
580ca115731115e30579fca6868d7b76b6776eec956f0a779798a3f536670435
```

Worth-it: **YES** (`WORTH_IT.md`). Pipeline score: **5.0 / 10** (`grade.md`).

## School / university field (the "No Items" check)

**This tenant does not use a school typeahead.**

| Item | Live behavior |
| --- | --- |
| Wizard step | My Experience → Education 1 |
| Exact label | **School or University *** (required) |
| Control type | **Plain text input** — no autocomplete dropdown |
| `University of Michigan` | Accepted as typed. **No dropdown. No "No Items."** |
| `Michigan` | Same — free text, no dropdown |
| Other queries (`UMich`, `Ann Arbor`, `University of Michigan - Ann Arbor`, `U of M`) | Not needed; there is no list to miss |

**Contrast with other 2027 Workday boards:** several tenants typeahead against a school catalog and recently returned **No Items** for University of Michigan. DriveTime's school field is not that control. You cannot get stuck on a missing catalog row here.

**Paste:** `University of Michigan - Ann Arbor`  
Also accepted: `University of Michigan`. Prefer the Ann Arbor form so it matches the PDF city line.

Related Education controls (not school typeahead):

- **Degree *** — closed dropdown (pick **Bachelor of Science (BS)**). Options listed in `written-answers.md`.
- **Field of Study** — searchable dropdown. Query `Computer Science` → **Computer and Information Science**. Not required.
- **Overall Result (GPA)** — free text (`3.66`).
- **From / To** — year dropdowns (YYYY). Use **2025** / **2028**.

## Apply wall

- **No guest path.** Autofill with Resume / Apply Manually / Use My Last Application / Apply With LinkedIn all require Create Account or Sign In.
- Wizard: My Information → My Experience → Application Questions → Voluntary Disclosures → Self Identify → Review.
- **No cover letter** and **no free-text essay** on the live wizard.
- Resume upload is the **Autofill with Resume** action on Start Your Application. My Information on the saved-draft session did not re-show an upload well — upload the packet PDF at Autofill, then fix parsed email/address.

## Knockouts (Application Questions — 7 items, one page)

GPA 3.5 and Dec 2027–May 2028 are **not** re-asked here; they live on Education + the JD. The wizard knockouts are: work authorization, visa sponsorship (incl. F-1/OPT/STEM OPT), meet minimum qualifications, **valid driver's license**, previous DriveTime employment (optional), current-employee internal-apply flag, relatives at DriveTime / Bridgecrest / SilverRock.

Full paste table: `written-answers.md`.

## Do not invent

C#, .NET, Azure, Node.js, Java, GraphQL, Ionic, Snowflake, Databricks, Tableau, Copilot, Fusion, Sentry. Angular is through-use debug, not owned DriveTime UI.
