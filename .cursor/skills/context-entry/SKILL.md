---
name: context-entry
description: >-
  Writes a canonical Experience or Project entry into context.md — a unique
  Lane, a fixed header, and a DRAW/AR bullet pool the resume writer copies
  verbatim. Use when the user adds, logs, captures, or describes a new
  internship, job, co-op, contract, founded product, club build, or personal
  project, or asks to upgrade an entry in the resume bullet pool.
---

# Context Entry

The resume writer copies bullets verbatim from `context.md`. Swap-set substitution is the only later edit. A weak pool line cannot be saved when a job is tailored. This skill is how new work becomes a selectable, defensible entry.

Do not edit a `.tex`, spawn the resume pipeline, or grade. Do not edit `reference/resume.md` or `reference/recruiting.md`. Write `context.md` only.

## Read first

1. `context.md` in full: profile, every Lane, swap sets, skills buckets, the section-membership rule, and the bullet-length ceiling.
2. `reference/resume.md` §4 (DRAW / AR), §5 (what counts as experience vs project vs a skill), §8 (failure modes), and the Part III track this work actually signals.

Existing Lanes are the bar for voice and for uniqueness. Michigan Data Consulting is the experience shape. Granular Synthesizer Plugin is the project shape.

## Classify

| Put it here | When |
|---|---|
| `### Experience:` | Internship, job, co-op, consulting contract, or a founded product with a title. Club *builds* that shipped count; memberships do not. |
| `### Project:` | Personal or class build with a live GitHub link. |

Section membership is fixed. Do not plan to promote a project into Experience later. A titled role stays an experience even when a project is the stronger engineering signal.

If the work restates a Lane already in the file, do not add a thinner twin. Find a distinct angle the user actually did, or stop and say the pool already covers that signal.

## Facts before prose

Extract only what the user stated. Never invent a metric, date, title, city, headcount, technology, customer, or ownership claim.

If any blocker below is missing, ask in one message and wait. Do not draft around the gap.

- Experience: org, title, month-year dates, city or Remote. Project: GitHub URL and a one-line what-it-is.
- What they personally owned, and whether anyone else shared it.
- The architectural decision and the constraint that forced it (why this store, queue, model, or thread model).
- One impact number — before/after, scale, latency, cost, hours, or revenue — or an explicit "no number exists."
- What broke, if something did, and the before/after of the fix.

A missing number stays missing. Write the true bullets and name the screen signal that remains out of rails. Vanity metrics (uptime, lines of code, coverage %) do not fill the gap.

## Lane

One or two sentences: "The only entry that …". Name the signal no other entry can carry, including what it is *not* (so a later tailor does not treat it as a duplicate of Vylet, Granular, MDC, or SignalWeaver).

Per-track fit is volume on this lane later. Do not write a lane that tries to be every track.

## Pool

Write 4–6 bullets. Each bullet is a different fact the writer can select alone. Do not rephrase one story across the pool.

1. **Lead.** Experience: human problem or outcome first, then the decision, metric last. Technology is not the opener. Project: strongest engineering decision. The descriptor already says what the project is.
2. **Tradeoff.** One line an interviewer can probe: what you chose, what you refused, what broke.
3. **Witness.** A real impact number as the closer, when one exists. About one metric per two bullets.
4. **Angles.** Remaining lines cover a second stack layer, ownership, or a failure fix so a later resume can lead SWE, data, or AI without new prose.

Author with DRAW (Decision → Reasoning → Action → Witness), then compress to AR (action verb + result) at two tight lines.

- Past tense. Verbs that imply skill: architected, shipped, eliminated, engineered, replaced.
- The tool name sits inside the decision that justified it.
- Bullet body after the `N. ` prefix targets **230–240 characters**. Cross 250 only when the extra clause is a second fact. Under ~180 usually means the line is a technology list or has no outcome.
- Every line must survive "walk me through this": the tradeoff, what failed, and what you measured.

## Header

Experience — month and year on both ends. `Present` is allowed. The role is the tagline, so there is no descriptor line.

```
Org Name                                          Mon YYYY -- Mon YYYY
Role — Team or client                               City, ST
```

Project — no dates. The link occupies the location slot. Leave `{tech derived from selected bullets}` literal; the writer fills it from the bullets it selects.

```
Project Name  |  {tech derived from selected bullets}    github.com/Verdent06/<repo>
One line stating what it is.
```

## Write

Append under Canonical Entries: new experiences after the last `### Experience:`, new projects after the last `### Project:`. Use fenced header and fenced numbered pool, one bullet per line, matching Michigan Data Consulting.

```
### Experience: Short Name

**Lane:** The only entry that …

**Header:**

```
…
```

**Bullet pool:**

```
1. …
2. …
```
```

Then update inventory only for tools a bullet uses in a decision:

- Add the tool to an existing skills bucket when the user can interview in it or defend the design. Do not add a language they cannot interview in.
- Add a swap-set row only for a single-token equivalent the user confirms (`llm-apis` is the pattern). A swap is not a way to claim a keyword they never used.

On an upgrade of an existing entry: keep the Lane unless the new work changes the unique signal. Append a bullet or replace one the user says is wrong. Leave true bullets in the pool.

## Gate

Count bodies before saving:

```bash
python3 - <<'PY'
bullets = [
    # paste each body without the "N. " prefix
]
for i, b in enumerate(bullets, 1):
    n = len(b)
    flag = "ok" if 180 <= n <= 250 else ("long" if n > 250 else "thin")
    print(f"{i} {n} {flag}")
PY
```

Fix `long` and `thin` before writing, unless a `long` line earns the third line with a second fact.

- Lane is unique against every existing Lane.
- Section label will not need reclassification.
- Nothing in the entry was inferred beyond the user's facts.
- Lead follows the experience-hook or project-decision rule.
- Bullets are distinct facts, not keyword lists.
- Every new skills-bucket item appears inside a bullet.

## Report

After the edit, say three things: the lane in one sentence, which track that lane can lead, and the one gap that is still out of rails.
