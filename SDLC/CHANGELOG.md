# LumenVenture SDLC Guide — Review Log

> One entry per review or significant change, **newest first**. Rules: [README §9.1 Review schedule](README.md#91-review-schedule).
> Each entry lists the date, the files, the reviewers, what changed (or "no changes needed") and the sources checked.

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
