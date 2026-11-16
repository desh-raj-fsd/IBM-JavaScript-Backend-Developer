---
name: sdlc-sync
description: Update the LumenVenture SDLC guide (SDLC/ folder) with the modern practices from one or more course notes — gap analysis, correction sweep, phase-file changes with diagrams, SVGs and templates, two-pass checks, online verification against primary sources, CHANGELOG, commit and push. Use when the user asks to update the SDLC folder from a note.
argument-hint: "<note number(s) or path, e.g. 08 or 06 07>"
disable-model-invocation: true
---

# /sdlc-sync — course note → LumenVenture SDLC guide

Input: the note(s) in `$ARGUMENTS` (a number like `08`, several numbers, or a path). If empty, use the newest note that has no CHANGELOG entry yet and say which one you picked.

**Why this is strict:** the `SDLC/` folder is the implementation guide LumenVenture uses on **real client projects** — many people and real money depend on it. An incorrect or outdated practice must never enter it. When the course and current industry practice disagree, the guide follows **current practice** (README §9).

Read first: `SDLC/README.md` (roles, project types, gates, §6 working rhythm, §9 change rules, §10 standards), `SDLC/CHANGELOG.md` (style of entries), the input note(s), and [../new-lecture/references/verification-checklists.md](../new-lecture/references/verification-checklists.md) (checklists C and D).

---

## Phase 1 — Gap analysis (no edits yet)

1. From the note, list every practice in its **Modern Best Practice** blocks, **Often-missed parts**, **done-when checklist**, **corrections** and **code examples**.
2. For each one, `grep -rn` the `SDLC/` folder for existing coverage.
3. Write a **gap table** in the scratchpad: practice → where it already is → target file and section → action (**add**, **correct**, **extend**, **none**) → artifact needed (rule, gate item, diagram, template, example).
4. List the **wrong claims** the note corrected, as search phrases, for the correction sweep.
5. Plan **chunks**: one chunk per target file (README, each phase file, each template). Large files can be split by section.

Show the user the gap table summary in 5–10 lines, then continue (ask only if a choice is really theirs, for example a new company-wide default such as a notice period).

## Phase 2 — Correction sweep

Search every SDLC file for each corrected claim and outdated term; fix them first (they are the highest risk).

## Phase 3 — Implement, chunk by chunk

For each chunk: edit → **pass 1** (checklist C) → **pass 2** (subagent: give it the changed file, the note, the gap table rows for this chunk and checklist C; ask what is wrong, missing, contradictory with other rules, or impractical for a 4–8 person team) → fix → `audit.py` on the file → next chunk.

What each chunk usually needs:
- **Explanation** in the phase file's existing structure, in B1 English, linking to existing sections instead of repeating them.
- **LumenVenture Standard:** owners, required outputs per project type, gate items, numbered **must / should / may** rules (append; never renumber).
- **Diagrams:** an SVG in that phase's `images/` folder (or `SDLC/images/` for README) and/or a Mermaid flow (`flowchart TD`, no `( ) < > "` in edge labels).
- **Templates or filled examples** when teams must produce an artifact; register them in the phase Templates table, README §8 and, if they go into `docs/`, the README §7 tree.
- **Dates:** "Last reviewed" = today, "Next review due" = +6 months, on every phase file you changed.

## Phase 4 — Internet verification (checklist D) — never skip

1. List every time-sensitive fact you added or changed (standards and editions, laws and dates, tool and runtime versions and behavior, RFCs, statistics).
2. Verify each against a **primary source** online (WebSearch; read the page with WebFetch / the web-fetch agent when needed).
3. Fix anything wrong in the SDLC **and** in the source note.
4. Update README §10 "Last checked" for each verified standard; anything not verified stays "next review" and is listed under "Not re-checked".
5. **Second verification round:** a fresh subagent re-checks the 5–10 riskiest facts independently (give it the list and the claimed sources; it reports agree / disagree with evidence). Resolve disagreements by reading the primary source yourself.

## Phase 5 — Record and ship

1. CHANGELOG entry at the top, in the existing format: Files · Scope (targeted change, not a full review) · Reviewers (placeholders) · What changed (per file) · Sources checked · Not re-checked · Next review due.
2. `python .claude/skills/new-lecture/scripts/audit.py SDLC` → 0 problems.
3. Commit to `main` (`SDLC: add note-NN <topic> practices`), run `.githooks/pre-commit` first, push.
4. Report: rules added (by number), templates and diagrams added, corrections made in the guide, sources verified, anything not verified.
