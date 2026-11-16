---
name: repo-audit
description: Periodic re-check of the whole repo (or part of it) against current best practices — course notes, the LumenVenture SDLC guide and the top-level guides. Verifies time-sensitive facts online, fixes outdated or wrong content, brings old files up to the current master-prompt rules, records SDLC reviews in the CHANGELOG, and commits chunk by chunk. Use when the user asks to check, verify or refresh the repo.
argument-hint: "[all | notes | sdlc | guides | <file or folder>]  (default: all)"
disable-model-invocation: true
---

# /repo-audit — keep the whole repo correct and current

Scope: `$ARGUMENTS` — `all` (default), `notes`, `sdlc`, `guides` (the top-level `*-Laws-*.md` and `6-Phases-*.md` files), or a file/folder path.

Facts, tools and standards change over time. This skill re-checks content that was correct when written but may not be now, and brings older files up to today's rules. Read [../new-lecture/references/verification-checklists.md](../new-lecture/references/verification-checklists.md) and `master-prompt.md` first.

---

## Phase 0 — Baseline

1. `git pull` on `main`; stop if the tree is not clean.
2. Run `python .claude/skills/new-lecture/scripts/audit.py <scope>` and save the output as the baseline.
3. Build the **chunk list** in the scratchpad — one chunk = one note, one SDLC phase file (with its templates), the SDLC README, or one top-level guide. Order: SDLC files whose "Next review due" date has passed → SDLC README §10 standards table → notes → guides.
4. Show the user the chunk list and the baseline problem count, then continue chunk by chunk. For a big scope, after every 3 chunks give a one-line progress update.

## Phase 1 — For each chunk

1. **Mechanical fixes:** everything `audit.py` reports for the chunk (links, anchors, Mermaid rules, SVG XML, names, correction badges without a quiz-wording line).
2. **Rule upgrades (notes):** bring the note up to the current master prompt — especially the correction rule (badge + "Lecture wording (for the quiz)" line + correction sweep everywhere), the section order, Modern Best Practice blocks, summary table with a modern column, at least 2 images. If `.transcripts/` has the source, re-check coverage against it.
3. **Time-sensitive facts:** list them (standards and editions, laws and deadlines, runtime and tool versions and behavior, statistics, RFCs, prices) and verify each online against a primary source (checklist D). Fix what changed. Also ask "is there a newer, widely adopted practice that replaced something we recommend?" and update the content if yes.
4. **Consistency:** the same fact must say the same thing in the notes, the SDLC guide and the top-level guides. When you fix it in one place, `grep -rn` and fix it everywhere.
5. **Pass 1** (checklist A/C/D as fits) → **pass 2** (fresh subagent on the changed chunk: wrong, outdated, missing, contradictory?) → fix → `audit.py` on the chunk → 0 problems.
6. **SDLC chunks only:** update the file's "Last reviewed / Next review due" dates and README §10 "Last checked" for each standard you verified; add a CHANGELOG entry (title `Review: <file> <yyyy-mm>`, "What changed" or "no changes needed", sources checked) — README §9.1 rules.
7. Commit the chunk to `main` (`audit: <file> — <short summary>`), run `.githooks/pre-commit` first, push.

## Phase 2 — Wrap up

1. Run `audit.py` on the whole scope again; compare with the baseline.
2. Report: chunks done, facts corrected (old → new, with source), rules or templates changed, items that could not be verified (left as "next review"), remaining problems and why.
3. Suggest the next audit date (the earliest "Next review due" in the SDLC files).
