---
name: new-lecture
description: Full pipeline for one IBM course lecture — turn a pasted transcript into notes and SVG images following master-prompt.md, deep-check them twice, update the LumenVenture SDLC guide with the modern practices, verify the SDLC changes against primary sources online, then commit and push to main. Use when the user gives a lecture title and transcript.
argument-hint: "<lecture title>  (paste the transcript in the same message)"
disable-model-invocation: true
---

# /new-lecture — transcript → notes → SDLC → verified → main

The user gives a **lecture title** (`$ARGUMENTS`) and pastes the **transcript**. If either is missing, ask for it and stop.

Work through the phases **in order**. Each phase is broken into **chunks**; finish, check and fix a chunk before starting the next. Every chunk is checked **twice** (pass 1 self-check, pass 2 independent subagent), as described in [references/verification-checklists.md](references/verification-checklists.md). Read that file now.

Keep the user informed with one short line at the start of each phase ("Phase 2/7: writing the Deep Dive, chunk 3 of 6"). Do not ask for confirmation between phases unless something is blocked or a decision is genuinely theirs.

---

## Phase 0 — Set up

1. `git pull` on `main`; stop and tell the user if the working tree is not clean or `main` cannot be updated.
2. Read `master-prompt.md` completely. It is the contract for the notes. If it disagrees with this skill, **the master prompt wins for notes**; this skill wins for the workflow.
3. Find the target folder: `course-N-<course-title>/module-N-<module-title>/` (lowercase, hyphens, Windows-safe). Continue the current module unless the title clearly starts a new module or course — then ask the user for the course and module names.
4. Next number `NN` = highest existing note number in that module + 1. File names: `notes/NN-<topic>.md`, `images/NN-<topic>-<short-name>.svg`.
5. Save the transcript to `.transcripts/<course-folder>/<module-folder>/NN-<topic>.txt` (the folder is git-ignored, out of respect for the course's terms; it lets `/repo-audit` re-check the note later on this machine).

## Phase 1 — Analyze and plan (no note writing yet)

Write `ledger.md` in the scratchpad with:

1. **Fact ledger:** every statement in the transcript, numbered (F1, F2, …), in transcript order — definitions, lists, examples, pros/cons, numbers, summary points. Nothing is too small.
2. **Correction candidates:** each statement that is wrong, outdated, an oversimplification, or confusing, with the correct version and your source. These become ⚠️ Correction badges **and** a correction sweep.
3. **Modern-practice plan:** for each lecture topic, what professional teams do today (Modern Best Practice blocks), checked against the coverage areas in master prompt §6.4, plus the "often-missed parts" a senior engineer would add.
4. **Time-sensitive facts to verify online** (versions, standards, dates, tool behavior).
5. **Chunk plan:** the note split into chunks (usually: Jargon · Topics · one chunk per major Deep Dive topic · Often-missed + checklist + Summary · Examples · Code · Related Concepts), and the 2–4 images.

Verify the time-sensitive facts now (checklist D) so the notes are right the first time.

## Phase 2 — Write the notes, chunk by chunk

For each chunk: write it → **pass 1** (checklist A; tick the ledger facts it covers) → **pass 2** (subagent on that chunk, only for Deep Dive chunks; small chunks may be checked together) → fix → next chunk.

Rules that are easy to forget:
- Every correction: badge + `**Lecture wording (for the quiz):** "<exact words>"` + correction sweep. The lecture's wrong words never appear elsewhere (except "Lecture" table columns).
- Your own additions are checked as strictly as the lecture.
- Run code examples in the scratchpad when they need no external services (install packages there, never in the repo).

## Phase 3 — Images

Create the planned SVGs (hand-written, white background, the repo's existing style). Embed each where it explains the concept. Validate with `audit.py`; check text fits inside its boxes.

## Phase 4 — Deep check of the notes (checklist B)

1. `python .claude/skills/new-lecture/scripts/audit.py <note> <its images> --leak "<wrong phrase>" …` (one `--leak` per corrected phrase) → 0 problems.
2. Ledger: every fact ticked; add anything missing.
3. Modern-practice gap check — if anything important is missing, add it and check it (do this twice if the first round added content).
4. **Pass 2 on the whole note:** spawn one general-purpose subagent with the note path, the transcript path, `master-prompt.md` and checklist B. Fix its valid findings, re-run `audit.py`.
5. Commit to `main` (`notes: add NN <Title>`), run `.githooks/pre-commit` first, push.
6. Post the **topic summary** (numbered list of the lecture's major topics — master prompt §5 step 7) and a short list of the corrections.

## Phase 5 — Update the SDLC guide

Run the full procedure in [../sdlc-sync/SKILL.md](../sdlc-sync/SKILL.md) with this note as input (gap table → correction sweep → chunks per file with diagrams and templates → checks → online verification → CHANGELOG → commit). Do not skip its Phase 4 (internet verification).

## Phase 6 — Final cross-check

1. `python .claude/skills/new-lecture/scripts/audit.py` on the **whole repo**: no **new** problems compared with before Phase 2 (list any old ones in the report, do not fix them silently — that is `/repo-audit`'s job).
2. Re-read the note's corrections and confirm the SDLC does not still teach any corrected claim.
3. If the online check in Phase 5 changed a fact, confirm the note was fixed too.

## Phase 7 — Report

Short report to the user: files created/changed, corrections, modern practices added, SDLC rules and templates added, sources checked online, anything not verified, commits pushed. Offer the next step.
