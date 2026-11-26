---
name: new-lecture
description: Fast path for one IBM course lecture — transcript to notes and SVG images following master-prompt.md, checked by scripts. The SDLC update, an independent review and commits are opt-in flags. Use when the user gives a lecture title and transcript. Flags on the first line - `--sdlc` (add the small SDLC delta), `--review` (one light review subagent), `--commit`, `--push`.
---

# /new-lecture — fast path (notes only by default)

Input: lecture title + transcript (ask and stop if missing). Flags on the first line, all optional: `--sdlc`, `--review`, `--commit`, `--push`.

**Where the tokens go, so do the opposite:** long output (the note itself), web pages returned in full, subagents that browse, and the SDLC delta. Rules:
- **Length budget.** Note ≈ 0.4 lines per transcript word (700 words → about 280 lines; hard cap 350). Jargon table ≤ 15 terms. One visual per topic: a Mermaid diagram **or** an image, never the same idea as table + diagram + image. 2 SVGs (3 only if the lecture has 3 separate ideas). A Modern Best Practice block **only** where the lecture is outdated, oversimplified or wrong; everything else goes in one "Often-missed parts" section. Keep master-prompt minimums (a Mermaid per major topic, ≥ 2 images, ≥ 5 related concepts, "What happens if" code where code exists); skip code for non-technical lectures except one tiny config example.
- **Output once.** Write the note in **one** `Write` call (two at most). Never rewrite it; fix with `Edit`/Python replace. Do not read back files you wrote. Do not re-read `master-prompt.md` if it is already in context.
- **Web budget: at most 6 fetches in one parallel batch.** Verify only numbers, dates, versions and named standards you will state as fact. For one-line facts use `WebSearch` (cheaper than guessing page URLs); one retry per failed URL, then drop the claim or write "not verified". Well-known process or people facts: hedge, do not fetch. Narrow prompts ("quote the sentence and the date").
- **No subagent unless `--review`.** Scripts replace the model review.

## Steps

1. **Prep (1 call):** `python .claude/skills/new-lecture/scripts/prep.py <topic-slug>` — pulls, finds the newest module, next number, creates folders, prints the paths. Then save the transcript's **key points only (~300 words)** to the printed TRANSCRIPT path. Read `master-prompt.md` once if it is not already in context.
2. **Plan in your head, write two small files in one call:** `keys.txt` (30–50 short transcript phrases, one per line, copied exactly) and `leaks.txt` (wrong phrases the note corrects, one per line). Decide corrections, the few real modern-practice blocks, and the facts to verify.
3. **Verify (one parallel batch, ≤ 6 fetches).** Keep sources for the note and the CHANGELOG.
4. **Write** the note and the SVGs (one `Write` each; SVGs in master-prompt style, text kept inside boxes). Run code examples only when the lecture is technical and needs no service; paste real output.
5. **Check (one command, fix, rerun once):**
   `python .claude/skills/new-lecture/scripts/audit.py <note> <svgs> --keys keys.txt --note <note> --leak-file leaks.txt --acronyms`
   Allowed leftover: a wrong phrase in a summary-table "Lecture" column.
6. **Finish.** Run `.githooks/pre-commit` only if committing. Report in ≤ 15 lines: numbered topic list, corrections (one line each), not verified, audit result, and "SDLC not updated: run `/sdlc-sync NN` (best for 3–4 notes at once)" unless `--sdlc`. Never commit `HANDOFF.md`. Commit only with `--commit`/`--push` (`notes: add NN <Title>`), push only with `--push`.

## Optional: `--sdlc` (small delta, reuse step 3 facts)

1. `python .claude/skills/new-lecture/scripts/gaps.py "pattern1|alt" "pattern2" …` — one call, one pattern per practice; `<- GAP` means add, hits mean extend or link, never duplicate. One more grep for the corrected wrong phrases.
2. Edit only real gaps: ≤ 1 new subsection per affected phase file, appended numbered rules (must/should/may; never renumber), ≤ 1 template (register it in the phase table and README §8), no new SVG. Dates "Last reviewed/Next review due" only in changed files. README §10 row only for a new standard.
3. CHANGELOG entry ≤ 10 lines (Files · Scope · What changed · Sources · Not re-checked). `audit.py SDLC` → 0 problems. Commit separately (`SDLC: add note-NN <topic> practices`) only with `--commit`.

## Optional: `--review` (one light subagent, `model: "sonnet"`, no web)

Give it the note path, the transcript path, the `git diff --stat` and the audit result. Ask only: (a) transcript points missing or distorted, (b) claims presented as fact that the note did not verify, (c) SDLC rules that contradict existing ones (with `--sdlc`), (d) beginner confusion. **Tell it not to browse or re-run scripts.** Findings only, ≤ 15, with line numbers. Check each claim yourself before applying. For a deep fact-check with web access, the user must ask for it (`--review` plus the words "verify online").
