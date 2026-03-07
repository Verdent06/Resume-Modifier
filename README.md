# Resume System

A modular, multi-track resume system built for fast, targeted applications. One shared class file. Three base templates. Unlimited company-specific outputs.

---

## Directory Structure

```
resume/
├── resume.cls                          # Shared LaTeX class — do not duplicate
├── README.md
├── context.md                          # Candidate context for resume-writing (graduation year, personal info)
│
├── templates/
│   ├── full-stack/
│   │   ├── Ankur Desai Resume.tex      # Base template for product/full-stack SWE roles
│   │   └── Ankur Desai Resume.pdf
│   ├── ai-ml/
│   │   ├── Ankur Desai Resume.tex      # Base template for ML/AI engineering roles
│   │   └── Ankur Desai Resume.pdf
│   └── dev-ops/
│       ├── Ankur Desai Resume.tex      # Base template for DevOps/infra-focused roles
│       └── Ankur Desai Resume.pdf
│
└── applications/
    └── [Company]/
        ├── company.md                  # Company description and research notes
        └── [role]/                     # One folder per role applied to
            ├── Ankur Desai Resume.tex  # Tailored copy of the relevant base template
            ├── Ankur Desai Resume.pdf
            └── job.md                  # Parsed job information + ATS information
```

**Example:**
```
applications/
└── visa/
    ├── company.md
    └── insight-day-technology/
        ├── Ankur Desai Resume.tex
        ├── Ankur Desai Resume.pdf
        └── job.md
```

---

## Workflow

### 1. Identify the track
Pick the base template that best matches the role's primary focus:

| Track | Use when the JD emphasizes... |
|---|---|
| `full-stack` | Product features, frontend/backend, system design, auth, databases |
| `ai-ml` | Models, inference pipelines, training, embeddings, data engineering |
| `dev-ops` | CI/CD, IaC, container orchestration, observability, cloud infra |

When in doubt, full-stack is the default. Never send a generic resume.

### 2. Create the company folder
```
applications/[Company]/
```
Copy the appropriate base template into it. Never edit the base templates directly — they are the source of truth.

### 3. Tailor
- Paste the full job description into the chat.
- Run the Cursor resume-pipeline rule (Agent mode).
- The pipeline will:
  - Parse the JD and extract: company/role names, slugs, core responsibilities, required/preferred skills, ATS keywords, and template choice.
  - Create (if needed) the company folder and `company.md` (never overwrite existing company.md; it is written once per company).
  - Create the position folder and copy in the correct base template (`Ankur Desai Resume.tex`, etc.), fixing class path as needed.
  - Populate `job.md` for the role, including parsed facts, ATS keyword lists, bullet mapping, and honest gap analysis.
  - Run initial tailoring via `@resume-writing`, updating only the position's working `.tex`.
  - Enter an iterative write→grade loop (max 7 passes) until all grading dimensions are A/B and ATS coverage is 90%+, or iteration cap is hit.
  - After the loop: check skills line & page fit, recompile, and save the final grade to `grade.md`.
  - Append an application log entry to `INTERNSHIPS.md`.

- Role-specific tailoring and keyword/ATS focus is always performed in the working application folder, never directly on the templates.
- The pipeline always uses the existing `[Company]/company.md` for research context, not per-role notes.

### 4. Compile
From the folder containing the `.tex` file:
```bash
xelatex "Ankur Desai Resume.tex"
```

---

## Base Template Philosophy

Each template shares the same structure but differs in **project selection** and **bullet emphasis**:

- **full-stack**: Leads with MindMosaic (architectural improvement + auth story) and Mira (voice/real-time client). Emphasizes system design, database architecture, and OAuth implementation.
- **ai-ml**: Leads with Mira (ML inference, Sentence-BERT, Whisper deployment, cold-start optimization). MindMosaic is deprioritized or dropped. WizViz (MediaPipe, real-time CV) moves up.
- **dev-ops**: Leads with Claude Builder Club (CI/CD, GitHub Actions, automation). Mira surfaces for its Lambda deployment and cold-start reduction story. Auth and graph architecture bullets are cut.

---

## Key Rules

1. **`resume.cls` is never duplicated.** All templates reference a single shared class file. Changes to formatting propagate everywhere.
2. **Base templates are never sent directly.** Every application gets its own folder and its own tailored copy.
3. **One page, hard constraint.** If a bullet doesn't earn its space for this specific role, cut it.
4. **Technologies need architectural justification.** Never list a tool without a bullet that explains why it was the right choice.
5. **Every application folder gets logged in `INTERNSHIPS.md`** after submission — this feeds the pipeline's calibration over time.