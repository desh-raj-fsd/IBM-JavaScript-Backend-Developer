# Verification Checklists (shared by /new-lecture, /sdlc-sync, /repo-audit)

Every chunk of work is checked **twice**:

- **Pass 1 — self-check:** you, right after writing the chunk, against the checklist below.
- **Pass 2 — independent check:** a **fresh subagent** (general-purpose) that did not write the chunk. Give it the file paths, the source (transcript or note), the master prompt and the checklist. Ask it for a list of findings with line numbers, each marked "wrong fact", "missing", "outdated", "rule broken" or "unclear". It must not edit files. Fix every valid finding, then re-run `audit.py`.

A chunk is done only when both passes find nothing left to fix and `audit.py` reports 0 problems for the files you touched.

---

## A. Notes chunk (one master-prompt section)

- [ ] Follows the section order and format of `master-prompt.md` §6 (Jargon → Topics → Deep Dive → Examples → Code → Related Concepts).
- [ ] Every fact in this part of the **fact ledger** (`ledger.md` in the scratchpad) appears in the chunk. Tick it in the ledger with the heading it went under.
- [ ] Every jargon term: official definition + simple words + analogy. Every acronym expanded on first use.
- [ ] B1 English: short sentences, simple words, technical terms explained.
- [ ] Each major concept has its own heading, nested bullets/tables, and at least one Mermaid diagram per major topic (`flowchart TD`; quoted node labels with special characters; no `( ) < > "` in edge labels; margin node in `direction TB` subgraphs).
- [ ] Modern Best Practice blocks open with the two-line "Lecture says / Industry today" quote and name real tools, the "why", and a table/diagram/code where useful.
- [ ] **Corrections:** every wrong, outdated or confusing lecture statement has a `⚠️ **Correction:** wrong → right` badge **and** a `**Lecture wording (for the quiz):**` line — and the **correction sweep** is done: the correct version is used in the text, tables, jargon, Mermaid, SVG text and captions, examples, code comments, topics list and summary. The lecture's words appear only in the quiz line and in "Lecture" columns.
- [ ] No softer "Clarification" badge for something that is actually wrong.
- [ ] Every fact **you added** (names, dates, versions, standards, tool flags, API behavior) is correct. If unsure, check it on the web (section D).
- [ ] Code: minimal working example, comments on significant lines, a "What happens if…" variation; JavaScript/Node.js first; current Node.js LTS / Express 5 APIs; run it in the scratchpad when it needs no external services.

## B. Notes — final deep check (after all chunks)

- [ ] `audit.py <note> --leak "<each wrong phrase you corrected>"` → 0 problems (a leak inside a "Lecture" table column is allowed).
- [ ] Fact ledger: **every** item ticked. Write the untouched ones in, then re-check.
- [ ] **Modern-practice gap check** — for each coverage area in master prompt §6.4 ask "does this lecture topic touch it, and is it covered?": Agile and iterative delivery · CI/CD and DevOps · shift-left testing and TDD · security by design (OWASP, DevSecOps, secrets, dependency scanning) · observability (logs, metrics, traces, SLOs) · cloud-native deployment (containers, Kubernetes, safe releases) · current Node.js/Express versions and APIs · responsible use of AI tools. Then: "what would a senior engineer add that the lecture never mentions?" → an "Often-missed parts" section and a "done enough when…" checklist.
- [ ] Summary table has a `✅ Modern best practice` column.
- [ ] At least 2 SVG images, embedded with `../images/NN-topic-short-name.svg`, valid XML, no text overlapping boxes or lines (estimate text width ≈ 0.6 × font-size × characters).
- [ ] Pass 2 (subagent) done on the **whole** note; findings fixed; `audit.py` re-run.

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
