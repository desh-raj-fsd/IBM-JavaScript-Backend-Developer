---
name: new-lecture
description: Fast, checked path for one IBM course lecture — transcript to notes and SVG images following master-prompt.md. Facts are verified with a cheap script, risky claims are flagged by a script, and a light review runs automatically when the risk is high or the SDLC changes. Flags on the first line - `--sdlc` (add the SDLC delta), `--review` / `--no-review` (force or skip the review), `--commit`, `--push`.
---

# /new-lecture — fast path, with checks that scale with risk

Input: lecture title + transcript (ask and stop if missing). Optional flags on the first line: `--sdlc`, `--review`, `--no-review`, `--commit`, `--push`.

**Cost rules:** one `Write` for the note (fix with `Edit`); no read-back of files you wrote; do not re-read `master-prompt.md` if it is in context. **Length budget:** note ≈ 0.4 lines per transcript word (cap 350); jargon ≤ 15 terms; one visual per idea; 2 SVGs (3 if 3 separate ideas); Modern Best Practice blocks only where the lecture is wrong, outdated or oversimplified; the rest in one "Often-missed parts" section. Keep master-prompt minimums.

## Steps

1. **Prep:** `python .claude/skills/new-lecture/scripts/prep.py <slug>` (pull, module, number, folders). Save key points (~300 words) to the TRANSCRIPT path.
2. **Plan, in one call write** `keys.txt` (30–50 exact transcript phrases) and `leaks.txt` (wrong phrases you will correct). List the corrections and the few real modern-practice blocks.
3. **Verify facts cheaply and widely.** For every number, date, version, standard or quoted wording you plan to state, run
   `python .claude/skills/new-lecture/scripts/fetchgrep.py <primary-url> "<regex>" …`
   (a script: only the matching snippets enter the conversation; run several in parallel; **no fixed cap**, about 10–15 checks is normal). Use `WebSearch`/`WebFetch` only when a page fails or needs JavaScript. One retry per URL, then hedge or drop the claim.
4. **Write** the note (one `Write`) and SVGs. Run code only for technical lectures (no external service); paste real output.
5. **Check (fix, rerun once):**
   `python .claude/skills/new-lecture/scripts/audit.py <note> <svgs> --keys keys.txt --note <note> --leak-file leaks.txt --acronyms`
   `python .claude/skills/new-lecture/scripts/riskcheck.py <note>` — every `??` line must become **verified** (add the source: "(official docs)", "per <source>"), **hedged** ("a common team choice", "general knowledge, not verified") or **removed**. Target: 0 unmarked.
6. **Review (automatic when needed):** run one light review (below) if `--review`, or if riskcheck says `REVIEW RECOMMENDED` (12+ checkable claims), or if there are 3+ corrections, or with `--sdlc`. Skip only with `--no-review`.
7. **Finish.** Report in ≤ 15 lines: numbered topics, corrections, **what was verified by source, what was hedged or not verified**, audit/riskcheck result, whether a review ran, and "SDLC not updated: run `/sdlc-sync NN`" unless `--sdlc`. Never commit `HANDOFF.md`. Commit only with `--commit`/`--push` (`notes: add NN <Title>`); push only with `--push`.

## Light review (one subagent, `model: "sonnet"`, no web)

Give it: the note path(s), the transcript path, `git diff --stat`, and the audit and riskcheck output. Ask only: (a) transcript points missing or distorted; (b) wrong, outdated or invented claims, and any claim without a source or hedge; (c) with `--sdlc`: SDLC rules that contradict existing rules (README tables vs phase files, prototype/client tailoring, must/should strength) or are impractical for 4–8 people; (d) beginner confusion. Tell it not to browse or re-run scripts; findings only, ≤ 20, with line numbers. **Verify each finding yourself** (use `fetchgrep.py` for facts) before applying. Use a deeper web-checking review only if the user asks.

## `--sdlc` (SDLC delta, checked)

1. `python .claude/skills/new-lecture/scripts/gaps.py "pattern|alt" …` (one pattern per practice; `<- GAP` = add, hits = extend or link, never duplicate) and one grep for the corrected wrong phrases.
2. Edit only real gaps: ≤ 1 subsection per affected phase file; append rules **after the current last number of that list** (check with `grep -n "^[0-9]*\. \*\*" file`; never renumber); ≤ 1 template (register in the phase table and README §8); README §10 row only for a new standard; update "Last reviewed/Next review due" only in changed files.
3. Re-verify the 5 riskiest new SDLC facts with `fetchgrep.py` (second round, cheap). CHANGELOG entry ≤ 10 lines with Sources and Not re-checked.
4. `python .claude/skills/new-lecture/scripts/audit.py SDLC --rules` → 0 problems (the `--rules` flag catches duplicate or skipped rule numbers). The light review (step 6) always runs. Commit separately (`SDLC: add note-NN <topic> practices`) only with `--commit`.
