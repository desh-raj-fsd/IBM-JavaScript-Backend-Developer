# LumenVenture SDLC Guide — Review Log

> One entry per review or significant change, **newest first**. Rules: [README §9.1 Review schedule](README.md#91-review-schedule).
> Each entry lists the date, the files, the reviewers, what changed (or "no changes needed") and the sources checked.

## 2026-11-16 — Planning (+ Testing): note-05 "Requirements" findings

- **Files:** `01-Planning/Planning.md`, `01-Planning/templates/` (`user-story.md`, `stakeholder-register.md`, `project-brief.md`), `01-Planning/images/` (4 new SVGs), `04-Testing/Testing.md` (rule 11), `README.md` (§8 template list, §10 standards table)
- **Scope:** a **targeted** change: add the requirement practices from the course note "05 Requirements" that the guide was missing. Not a full review of either phase file.
- **Reviewers:** <Product Owner>, <Delivery Lead>; Testing rule: <QA Engineer> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Planning:** new §2.1 **six-step requirements process** (stakeholders → goals → elicit → document → confirm → prioritize) and the three moments it runs; §4.1 expanded with the **power / interest grid**, personas, often-forgotten groups and the one-decision-maker rule; §4.4 constraint vs. assumption (an assumption is a risk); new §4.10 **goals, SMART objectives, OKRs**, outcome over output, `OBJ-n` IDs; §4.11 **elicitation toolbox** + interview rules; §4.12 **EARS** patterns, vague vs. testable, the four SRS categories; §4.13 **ISO 29148 quality characteristics**, validation vs. verification, written approval and baseline; §4.14 **RICE, WSJF, Kano**, value vs. effort; §4.15 **URS / SRS / SysRS** vs. ISO names (BRS, StRS, SyRS, SRS) and what LumenVenture writes; GAMP 5 URS for GxP clients; §4.16 often-missed requirement areas. Jargon, §7 checklist, §8.2 outputs, Gate G1 and rules 18–22 updated.
  - **Templates:** user story gets type, priority, objective, source, EARS rules and a quality-check DoR item; stakeholder register gets power / interest / strategy, a named decision-maker and the forgotten-groups checklist; project brief §2 becomes goals → `OBJ-n` key results.
  - **Testing:** rule 11 — requirement traceability check in CI (should; must on regulated projects).
  - **Diagrams:** `sdlc-modern-requirements-six-steps.svg`, `sdlc-modern-stakeholder-grid.svg`, `sdlc-modern-goal-to-test-chain.svg`, `sdlc-modern-requirement-documents.svg`, plus Mermaid flows in §2.1 and §4.13.
- **Sources checked:** the course note `05-requirements.md` (which cites ISO/IEC/IEEE 29148:2018, EARS — Mavin et al., Rolls-Royce 2009, GAMP 5 2nd edition 2022, MoSCoW / DSDM, RICE, WSJF / SAFe, Kano). **Not re-checked against primary sources in this change** — GAMP 5 is marked "next review" in README §10.
- **Next review due:** Planning 2027-05-16; Testing 2027-05-16.

## 2026-11-13 — Targeted review of all phases: note-04 findings + current facts

- **Files:** all six phase files, `README.md` (new §10 Standards table), templates `project-brief.md`, `pipeline-checklist.md`, `service-review.md`
- **Scope:** a **targeted** review: (1) add practices from the course note "04 Building Quality Software" that the guide was missing, (2) re-check time-sensitive facts against current sources. It was not a line-by-line rewrite of every section.
- **Reviewers:** <review owners> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Planning:** European Accessibility Act (since 28 June 2025); abuse cases and privacy by design; Argon2id; OWASP Top 10:2025 and ASVS 5.0; new §4.9 workshops (story mapping, example mapping, EventStorming); rules 16–17.
  - **Design:** DDD bounded contexts, ports and adapters, architecture fitness functions; `Deprecation` (RFC 9745) / `Sunset` (RFC 8594) headers; OpenAPI 3.2 and AsyncAPI; Argon2id; OWASP Top 10:2025 new risks; jitter, bulkheads and rate limits; rules 10–11.
  - **Development:** complexity lint rules; 2025 npm supply-chain attacks, cooldowns, `--ignore-scripts`, scanners; npm token changes (classic tokens revoked 9 Dec 2025, granular ≤ 90 days, trusted publishing); secure-coding table: mass assignment, SSRF, fail-closed error handling, Argon2id settings; AI package hallucination, agent least privilege, OWASP Top 10 for LLM Applications; rules 4 (updated), 12–13.
  - **Testing:** property-based, fuzz and visual regression tests; rule 10 extended.
  - **Deployment:** DORA updated from four to **five** metrics (failed deployment recovery time, deployment rework rate); OpenFeature; SBOM formats; RC naming and changelog; npm trusted publishing; EU Cyber Resilience Act dates; rules 11–13.
  - **Maintenance:** SLO burn-rate alerts; golden signals, RED and USE methods; `security.txt` (RFC 9116) and disclosure policy; CRA 24 h / 72 h reporting; Deprecation/Sunset RFCs; rules 12–14.
  - **Fixes:** OWASP's name ("Open **Worldwide** Application Security Project", renamed in 2023); "bcrypt or argon2" → Argon2id first.
- **Sources checked:** GitHub Docs (Dependabot `cooldown`); npm CLI `min-release-age` (npm 11.10.0); owasp.org Top 10:2025; OWASP ASVS 5.0; OWASP Password Storage Cheat Sheet; dora.dev metrics guide and history; EU Commission CRA reporting page and law-firm summaries; GitHub changelog (npm classic token revocation, 9 Dec 2025); OpenAPI 3.2.0 spec (spec.openapis.org); RFC 9745 (rfc-editor.org); Node.js release-schedule announcement (nodejs.org).
- **Not yet re-checked** (marked "next review" in README §10): OWASP API Top 10, OWASP LLM Top 10, SAMM, NIST SSDF, SLSA, ISO/IEC 25010, WCAG, EAA, GDPR, RFC 9457/8594/9116.
- **Next review due:** all phase files 2027-05-13.

## 2026-11-13 — Planning: client discovery + review schedule

- **Files:** `01-Planning/Planning.md`, `01-Planning/templates/` (6 new templates), `README.md`
- **Reviewers:** <Product Owner>, <Delivery Lead> — *to be filled in when the pull request is approved*
- **What changed:**
  - Added **§8.6 Client Discovery** for non-technical clients: paid discovery, same-day meeting summaries, clickable prototype, MVP workshop (MoSCoW), plain-language client PRD, written approval, swap-or-change-request rule.
  - New templates: `discovery-proposal.md`, `discovery-questions.md`, `meeting-summary.md`, `assumptions-and-decisions-log.md`, `mvp-workshop.md`, `client-prd.md`.
  - Planning §8 updated: jargon, owners, required outputs, Gate G1 item, rules 10–15, templates table.
  - README: kickoff step 2a, project-types table, `docs/discovery/` folder, templates list, and the new **§9.1 Review schedule** with review dates on every phase file.
- **Sources checked:** SRS structure (IEEE 830 → ISO/IEC/IEEE 29148:2018) against standards catalogs; MoSCoW "Must ≤ about 60% of effort" guideline (DSDM / Agile Business Consortium).
- **Next review due:** Planning 2027-05-13; full guide 2027-05-13.

## 2026-11-10 — First version of the guide

- **Files:** `README.md`, all six phase files and their templates
- **What changed:** guide created from the modern-best-practice SDLC notes; LumenVenture Standard sections (owners, outputs, gates, rules, templates) added to each phase.
- **Next review due:** Design, Development, Testing, Deployment, Maintenance — 2027-05-10.
