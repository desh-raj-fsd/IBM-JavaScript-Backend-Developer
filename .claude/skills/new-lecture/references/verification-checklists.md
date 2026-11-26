# Verification Checklists (shared by /new-lecture, /sdlc-sync, /repo-audit)

**How checking works in `/new-lecture`:** `scripts/audit.py` (coverage via `--keys`, `--leak-file`, `--acronyms`, `--rules`, links, anchors, Mermaid, SVG, names, badge/quiz-line count) and `riskcheck.py` are the checks. The SDLC sync runs automatically, followed by one light model review (no web) that covers the note and the SDLC change together. `/sdlc-sync` and `/repo-audit` still use the stricter per-chunk passes below when the user asks for a deep review.

---

## A. Notes — what a good note has (self-check while writing)

- [ ] Section order and rules of `master-prompt.md` §6 (Jargon → Topics → Deep Dive → Examples → Code → Related Concepts).
- [ ] Every key phrase of the transcript is present (`--keys`).
- [ ] Jargon: official definition + simple words + analogy; acronyms expanded; B1 English.
- [ ] One Mermaid `flowchart TD` per major topic; no `( ) < > "` in edge labels.
- [ ] Modern Best Practice blocks: "Lecture says / Industry today" quote, real tools, the why, a table or code.
- [ ] Every corrected claim: `⚠️ **Correction:**` badge + `**Lecture wording (for the quiz):**` line, and the wrong wording nowhere else (`--leak-file`).
- [ ] Every fact you added is correct (verified once online, Phase 1); code examples were run and their output pasted.
- [ ] Often-missed parts and a "done enough when…" checklist; summary table with a `✅ Modern best practice` column; 2+ SVGs embedded.

## B. Notes — final deep check

Replaced by the scripted checks and the single review described at the top.

## C. SDLC chunk (one phase file, README, or template)

LumenVenture uses this guide on **real client projects with real money**. A wrong rule costs money and trust.

- [ ] Gap table done first: practice → already in the guide? (where) → action (add / correct / none). Do not duplicate what exists — extend it and link to it.
- [ ] Correction sweep of the guide: search every SDLC file for each wrong term or claim the note corrected (`grep -rn`), and fix it.
- [ ] Content follows the phase file shape: Jargon → the job → Waterfall vs. modern → practices → "done when" → **LumenVenture Standard** (owners, required outputs per project type, gate checklist, rules, templates).
- [ ] Rules use **must / should / may** correctly; numbered rules continue the existing list (never renumber old rules — other files link to them).
- [ ] New rules do not contradict existing rules in any phase file or the README (search for the topic in all files).
- [ ] Practical for a **4–8 person team**; owners named by role; defaults are stated (numbers, time limits) and can be tailored in the project brief.
- [ ] Each new practice has a diagram (SVG in the phase's `images/` folder and/or Mermaid) where it helps, and a **template or filled example** when teams must produce an artifact.
- [ ] New templates are listed in the phase file's Templates table, README §8, and (if they live in `docs/`) the README §7 tree.
- [ ] Phase file "Last reviewed / Next review due" dates updated (next = +6 months).
- [ ] B1 English; every acronym expanded on first use in that file.

## D. Internet verification (SDLC and time-sensitive note facts)

- [ ] List every **time-sensitive** fact you added or changed: standard editions (OWASP, ASVS, ISO, WCAG, OpenAPI, Scrum Guide…), laws and deadlines (GDPR, EAA, CRA…), tool and runtime versions and behavior (Node.js LTS lines, npm, Express, GitHub Actions…), statistics, RFC numbers.
- [ ] Check each one against a **primary source** (the standard's own site, official docs, the RFC, the law's official page) with WebSearch, and read the page (WebFetch or the web-fetch agent) when the search result is not clear. Not blogs or opinion posts.
- [ ] Fix anything that is wrong or outdated — in the SDLC **and** in the note it came from.
- [ ] Record the sources in the CHANGELOG entry ("Sources checked") and update "Last checked" in README §10. Anything you could not verify is listed under "Not re-checked" and marked "next review" — never presented as verified.
- [ ] Never add a tool, version or statistic you could not verify.
