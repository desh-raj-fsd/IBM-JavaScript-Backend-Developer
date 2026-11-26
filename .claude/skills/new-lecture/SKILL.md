---
name: new-lecture
description: Lean pipeline for one IBM course lecture — turn a pasted transcript into notes and SVG images following master-prompt.md, add the matching modern practices to the LumenVenture SDLC guide, verify time-sensitive facts online once, check with scripts plus one independent review. Use when the user gives a lecture title and transcript. Flags on the first line - `--notes-only` (skip SDLC), `--commit` (commit when done), `--push` (commit and push).
---

# /new-lecture — transcript → notes → SDLC delta (lean)

Input: a **lecture title** and the **transcript**. If either is missing, ask and stop. Optional flags on the first line: `--notes-only`, `--commit`, `--push`.

**Budget rules (why this skill is lean):**
- Target about **40 tool calls** and **one subagent**. Do not read back files you just wrote. Patch with `Edit` or a short Python replace, never rewrite a whole note.
- Deterministic checks (`audit.py`) replace most model review. A model reviews only what a script cannot.
- Verify each time-sensitive fact **once**, in **one parallel batch**, with narrow `WebFetch` prompts (ask for the number, date or quote, nothing else).
- The note is the product. The SDLC change is a **small delta**, not a second rewrite.

---

## Phase 0 — Set up (3 calls)

1. `git pull`. Continue even if `HANDOFF.md` or other unrelated files are untracked; stop only if tracked files are modified in the folders you will touch.
2. Read `master-prompt.md` once (it is the contract for notes; it wins over this skill for notes). Do **not** re-read it later.
3. Target folder: continue the newest `course-N-*/module-N-*/` (ask only if the title clearly starts a new module). Next number `NN` = highest note number there + 1; names `notes/NN-<topic>.md`, `images/NN-<topic>-<short-name>.svg`.
4. Save the transcript to `.transcripts/<course>/<module>/NN-<topic>.txt` (git-ignored).

## Phase 1 — Plan in one scratch file (`plan.md`, at most ~40 lines)

Write only:
1. **`keys.txt`** — 30–60 short phrases that must appear in the note (every definition, list item, example and number of the transcript, one phrase each, copied from the transcript). This replaces a full fact ledger.
2. **Corrections** — lecture claim → correct version → source, one line each (these become badges and `--leak` phrases in `leaks.txt`).
3. **Modern-practice topics** per lecture topic (master prompt §6.4 areas that apply; skip areas the lecture does not touch) plus what a senior engineer would add.
4. **Facts to verify** — only versions, dates, numbers, standards, tool behavior you will write. Skip anything README §10 or a CHANGELOG entry already shows as verified in the last 30 days.

Then **verify all facts in one parallel batch** of `WebFetch` calls (primary sources only). Record the sources; reuse them for the SDLC delta and the CHANGELOG. Unverifiable → leave the claim out or mark it "not verified".

## Phase 2 — Write the note (about 4 chunks, self-check only)

Chunks: (1) title, jargon, topics · (2–3) Deep Dive, grouped by topic · (4) examples, code, related concepts, summary table.
- Follow `master-prompt.md` §6 order and rules (badge + quiz line + correction sweep, Modern Best Practice blocks, one Mermaid per major topic, B1 English, acronyms expanded, 5 related concepts, "What happens if" code).
- After each chunk, tick it against `keys.txt` mentally; do not spawn a reviewer per chunk.
- **Run code examples** when they need no external service (scratchpad only); paste the real output into the note.
- **2–3 SVG images** (not more unless the lecture is dense), master-prompt style, embedded with `../images/…`.

## Phase 3 — Scripted checks (one command, then fix)

```
python .claude/skills/new-lecture/scripts/audit.py <note> <images…> --keys keys.txt --note <note> --leak-file leaks.txt --acronyms
```

Fix everything it reports. Allowed leftovers: a wrong phrase in a summary-table "Lecture" column. Repeat until clean. This covers coverage, leaks, links, anchors, Mermaid rules, SVG validity, file names, badge/quiz-line count and acronym expansion.

## Phase 4 — SDLC delta (skip with `--notes-only`)

1. **Gap table with one grep command per topic** against `SDLC/` (use `grep -rniE "a|b|c" SDLC --include='*.md' | cut -d: -f1 | sort | uniq -c`). Mark each practice: already there / extend / add. **Never duplicate**; link to existing sections.
2. **Correction sweep:** one grep for the note's wrong phrases over `SDLC/`.
3. **Edit only where there is a real gap:** at most one new subsection per affected phase file, a few numbered rules (append; never renumber; must/should/may; owner by role; defaults stated; practical for 4–8 people), one template only if teams must produce an artifact (register it in the phase Templates table and README §8), no new SVG unless a diagram is essential. Update "Last reviewed / Next review due" (+6 months) in changed phase files only.
4. Use the facts already verified in Phase 1. Verify only facts that are new to the SDLC text (one more parallel batch if needed). Add README §10 rows for new standards.
5. CHANGELOG entry at the top (existing format: Files · Scope · Reviewers · What changed · Sources checked · Not re-checked · Next review due).
6. `python .claude/skills/new-lecture/scripts/audit.py SDLC` → 0 problems.

## Phase 5 — One independent review (one subagent, `model: "sonnet"`)

Spawn **one** subagent for note **and** SDLC diff together. Give it: the file paths, `git diff --stat`, the transcript path, and the `audit.py` result (so it does not redo scripted checks). Ask only for: (a) transcript statements missing from the note, (b) wrong or outdated facts — verify **at most 8** of the riskiest online against primary sources, (c) SDLC rules that contradict existing rules or are impractical for a small team, (d) anything a beginner could misread. Findings only, numbered, with line numbers, no edits, under 30 items. **Verify its claims yourself before applying** (it can be wrong: check the source). Fix, re-run `audit.py`.

## Phase 6 — Finish

- Run `.githooks/pre-commit`. **Commit only with `--commit` or `--push`** (default: leave changes uncommitted and say so). One commit for notes (`notes: add NN <Title>`) and one for SDLC (`SDLC: add note-NN <topic> practices`); push only with `--push`. Never commit `HANDOFF.md`.
- Final report (short): topic list (numbered), corrections (one line each), what was added to the SDLC (rules by number, templates), sources checked, what was **not** verified, audit result, and any shortcuts taken.
- Offer the next step.
