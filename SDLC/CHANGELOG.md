# LumenVenture SDLC Guide — Review Log

> One entry per review or significant change, **newest first**. Rules: [README §9.1 Review schedule](README.md#91-review-schedule).
> Each entry lists the date, the files, the reviewers, what changed (or "no changes needed") and the sources checked.

## 2026-11-16 — Documentation: note-09 "Software Documentation" findings

- **Files:** `README.md` (§7 docs tree, new §7.1 documentation map, new §7.2 documentation rules 1–9, §8 templates), `03-Development/Development.md` (§4.12, §5, §6.2, pointer in §6.4, §6.5), new template `03-Development/templates/sop.md`, templates `definition-of-done.md`, `pull_request_template.md`, `05-Deployment/templates/pipeline-checklist.md`, `06-Maintenance/templates/service-review.md`, `06-Maintenance/templates/runbook.md`
- **Scope:** a **targeted** change: add the documentation practices from the course note "09 Software Documentation" that the guide was missing. Not a full review of the phase files; the README "Last reviewed" date stays at the last **full-guide** review (2026-11-13), as for the earlier targeted changes. Correction sweep: none of the note's corrected lecture claims ("process documentation describes how to complete a task", "user acceptance specifications", working papers as technical documentation, "updating documentation happens during the maintenance phase") were found in the guide.
- **Reviewers:** <Delivery Lead>, <Tech Lead>; Development: <a developer>; Maintenance templates: <Security Champion> — *to be filled in when the pull request is approved*
- **What changed:**
  - **README §7.1 documentation map:** product documentation (requirements, design, technical, QA, user) and process documentation (plans and standards, reports and notes, SOPs and runbooks), each with documents, owner role (consistent with the RACI), audience and when it is updated; Mermaid diagram.
  - **README §7.2 documentation rules 1–9:** docs in Git with an owner; docs updated **in the same PR** (help center: same release), never "later"; no secrets or personal data in docs; API reference generated from OpenAPI; docs checks in CI (must on regulated); SOPs for repeated project-specific procedures, with tool-enforced steps (must on client and regulated projects for "merge to `main`"; the release checklist is the release SOP); review dates for SOPs and runbooks; working papers are process docs — decisions into ADRs or the decisions log; user documentation for user-facing features (must on client projects, accessible).
  - **New template:** `sop.md` — SOP structure plus the filled example "Merging a change to `main`".
  - **Development:** §4.12 docs in the same PR, product vs. process docs, SOPs enforced by tools, docs checks in CI with pinned tools (YAML excerpt); §5 DoD line; §6.2 rows for SOPs and docs checks; §6.4 points to README §7.2.
  - **Templates:** Definition of Done docs item is now ★ (same PR or "no docs change"); PR template docs line; pipeline checklist docs checks; service review lists overdue SOPs and runbooks; runbook gets Last reviewed / Next review due.
- **Sources checked:** EPA QA/G-6 *Guidance for Preparing Standard Operating Procedures* (April 2007 — SOP definition, update when the procedure changes, periodic review "e.g. every 1–2 years"); GitHub Docs "About code owners" and rulesets (any one listed owner is enough; last matching pattern wins); markdownlint-cli2 README (`"#node_modules"` negation); Redocly CLI docs (`lint`, `build-docs --output`); Diátaxis (diataxis.fr); for the note also ISO/IEC/IEEE 29119-3:2021 and ISO/IEC/IEEE 26514:2022 (IEEE SA and ISO catalogue pages) and agilemanifesto.org. Second, independent verification round by a separate reviewer: all facts agreed.
- **Not re-checked:** lychee-action version (left as a placeholder to pin); WCAG 2.2 row in §10 stays "next review".
- **Next review due:** Development 2027-05-16; README §7 at the next full-guide review (2027-05-13).

## 2026-11-16 — Testing: note-08 "Software Testing" findings

- **Files:** `04-Testing/Testing.md` (jargon, §1, §3, §4.1, §4.2, new §4.13–§4.15, §5, §6.2, §6.3, rules 11 example, 13–17, §6.5), new template `04-Testing/templates/test-case.md`, `04-Testing/templates/test-strategy.md` (§2.1, §2.2, §5), `04-Testing/templates/bug-report.md`, `03-Development/templates/definition-of-done.md`, `05-Deployment/templates/release-checklist.md`, `06-Maintenance/Maintenance.md` (§4.5, §5, rule 5), `README.md` (§7 docs tree, §8 templates, §10 standards); new diagram `04-Testing/images/sdlc-modern-regression-cadence.svg`
- **Scope:** a **targeted** change: add the testing practices from the course note "08 Software Testing" that the guide was missing. Not a full review of the phase files. Correction sweep: none of the note's corrected lecture claims (for example "error-free software", "regression testing, also called maintenance testing", "system testing validates", "acceptance testing during maintenance") were found in the guide.
- **Reviewers:** <QA Engineer>, <Tech Lead>; Maintenance: <Security Champion> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Testing:** §1 testing cannot prove the absence of defects; §3 what each level is for (integration can be black- or white-box; system **verifies**; acceptance **validates, before release**); §4.1 grey-box, change-related testing, the what / how / why classification (Mermaid), usability and accessibility are non-functional (ISO/IEC 25010:2023), maintenance testing contains confirmation and regression testing; §4.2 confirmation, compatibility, documentation, recovery, UAT, OAT and contract / regulatory acceptance; new §4.13 the seven ISTQB testing principles; new §4.14 test-case fields and test design techniques (equivalence partitioning, boundary values, decision tables, state transition) with a `node:test` example; new §4.15 regression schedule (PR affected / `main` full / nightly / release commit / after deploy), test impact analysis, one bug-ID test per fix; §5 exit criteria; §6.2 nightly regression and written test cases; G4 now requires the **full** suite on the release commit. Rules 13–17 (design techniques, regression schedule, bug-ID test that fails without the fix, compatibility matrix and docs checked against OpenAPI, written test cases for manual / UAT / OAT tests). Rule 11 example ID changed to `REQ-10` (REQ-09 already meant "one review per user per book" in Design).
  - **New template:** `test-case.md` — written test cases plus an execution record with sign-off, for tests that cannot be automated (should on client projects, must on regulated projects).
  - **Templates:** test strategy gets a regression schedule, test design techniques, supported platforms, compatibility / recovery / documentation targets; bug report and Definition of Done require the bug-ID test that fails without the fix; release checklist requires the full regression suite on the release commit.
  - **Maintenance:** hotfix text and rule 5 point to Testing rule 15 (bug-ID regression test).
- **Sources checked:** ISTQB CTFL syllabus v4.0.1 (istqb.org — seven principles, v4.0 released 21 April 2023, maintenance testing §2.3); ISO/IEC 25010:2023 foreword (interaction capability, inclusivity and user assistance, safety, flexibility); Vitest CLI docs (`--changed` with a branch or commit); Jest CLI docs (`--changedSince`); GitHub Actions docs (schedule cron in UTC). Second, independent verification round by a separate reviewer.
- **Not re-checked:** WCAG 2.2 and the other README §10 rows still marked "next review"; tool names used only as examples (k6, Playwright, Pact, Testcontainers, Stryker, fast-check).
- **Next review due:** Testing, Maintenance 2027-05-16; README §7, §8 and §10 at the next full-guide review (2027-05-13).

## 2026-11-16 — Versioning and compatibility: note-07 "Software Versions" findings

- **Files:** `03-Development/Development.md` (§4.2.1, §4.8, §4.11, §6.2, rules 8 and 14–17, §6.5), new template `03-Development/templates/versioning-policy.md`, `02-Design/Design.md` (§4.4.1, rules 12–13), `05-Deployment/Deployment.md` (§4.5, §4.7, rule 15), `05-Deployment/templates/release-checklist.md`, `06-Maintenance/Maintenance.md` (§4.9), `README.md` (§7 docs tree, §8 templates, §10 standards); new diagrams `03-Development/images/sdlc-modern-one-version-everywhere.svg`, `02-Design/images/sdlc-modern-api-compatibility.svg`
- **Scope:** a **targeted** change: add the versioning and compatibility practices from the course note "07 Software Versions" that the guide was missing. Not a full review of the phase files.
- **Reviewers:** <Tech Lead>, <a developer>; Design: <Security Champion>; Deployment: <Delivery Lead> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Development:** §4.2.1 versioning policy — SemVer is **3 parts** and is about **compatibility, not size**; pre-release labels and npm dist-tags; build metadata after `+` (four-part numbers are not SemVer); `0.y.z` only before the first client; released versions are immutable; one version everywhere; compare versions with a SemVer library; a `/version` route example. §4.8 version-range table (`^`, `~`, exact, `^0.x`) and runtime version (`engines`, `.nvmrc`, Docker base image, CI matrix). §4.11 AI tools suggest outdated APIs and versions. Rules 14–17; rule 8 now points to the versioning policy.
  - **New template:** `versioning-policy.md` (what is versioned and how, bump rules, supported versions, deprecation periods, how to see the running version) — required on internal, client and regulated projects.
  - **Design:** §4.4.1 API compatibility — backward vs. forward compatibility (tolerant reader for responses and events; requests still reject unknown fields), breaking-change table, `/v2` in parallel, notice periods (≥ 6 months external, ≥ 1 month internal), usage tracking, OpenAPI diff in CI. Rules 12–13.
  - **Deployment:** post-deploy smoke test checks `/version`; image tags = version + commit SHA, production by tag or digest, never `latest`; pre-releases never reach production; rule 15. Release checklist: release types now **Major / Minor / Patch** (the old "Minor / Major / Hotfix" list had no Patch), Git tag field, version and `/version` checks.
  - **Maintenance:** §4.9 usage per API version and client; errors split by `service.version`; supported-versions list checked in the service review.
- **Sources checked:** the course note `07-software-versions.md` (SemVer 2.0.0 rules and precedence; npm range semantics, checked by running the `semver` package; RFC 9745 / RFC 8594 headers; Ubuntu 18.04 point-release dates). **Not re-checked against primary sources in this change** — the SemVer and Conventional Commits rows in README §10 are marked "next review".
- **Next review due:** Development, Design, Deployment, Maintenance 2027-05-16.

## 2026-11-16 — Working rhythm and methodology: note-06 "Software Development Methodologies" findings

- **Files:** `README.md` (§6 rewritten and extended, §10 standards table), `01-Planning/Planning.md` (§4.17, step 7 of §8.6.2, rules 23–24), `01-Planning/templates/project-brief.md` (§9), `04-Testing/Testing.md` (§4.12, rule 12), `05-Deployment/Deployment.md` (rule 14), `06-Maintenance/Maintenance.md` (rule 15); new diagrams `images/sdlc-modern-methodology-by-project-type.svg`, `images/sdlc-modern-sprint-cadence.svg`, `01-Planning/images/sdlc-modern-fixed-time-flex-scope.svg`, `04-Testing/images/sdlc-modern-v-model-in-ci.svg`
- **Scope:** a **targeted** change: write down **how LumenVenture works** (methodology), using the practices from the course note "06 Software Development Methodologies". Not a full review of the phase files.
- **Reviewers:** <Delivery Lead>, <Tech Lead>; Planning: <Product Owner>; Testing: <QA Engineer> — *to be filled in when the pull request is approved*
- **What changed:**
  - **README §6:** rhythm table corrected to Scrum Guide 2020 terms (**Sprint Review**, **Sprint Goal**, Sprint Retrospective; refinement is an activity, not an event); the sprint is **no longer called a "planning-to-release loop"** — releases follow the pipeline. New §6.1 methodology by project type (default Scrum; Kanban for prototypes and after go-live; V-model discipline for regulated work; phase gates kept as governance, not as Waterfall delivery); §6.2 Scrum accountabilities and artifacts mapped to our roles; §6.3 Kanban lane with WIP limit; §6.4 releases are not tied to sprints; §6.5 anti-patterns (Water-Scrum-Fall, mini-waterfall, cargo-cult Agile, velocity as a target); §6.6 six working-rhythm rules.
  - **Planning:** §4.17 fix time and cost, flex scope; cone of uncertainty; throughput (Monte Carlo) forecasting with the 85% date; contract models for client projects; rules 23–24. Discovery step 7 now says Sprint Review instead of "demo".
  - **Project brief template:** §9 now records the methodology, the delivery / contract model and the forecast method.
  - **Testing:** §4.12 the V-model idea done continuously (each design artifact gets its test in the same sprint; verification vs. validation; full V per increment for ISO 26262 / IEC 62304 / GAMP 5 work); rule 12 — no testing-only sprint or phase.
  - **Deployment:** rule 14 — releases are not tied to the sprint end.
  - **Maintenance:** rule 15 — maintenance and support in a Kanban lane with a WIP limit, same backlog.
- **Sources checked:** the course note `06-software-development-methodologies.md` (Scrum Guide 2020 accountabilities, events, timeboxes and "Sprint Review is not a gate to releasing value"; Agile Manifesto 2001; Royce 1970; Kanban, XP, Lean). **Not re-checked against primary sources in this change** — the Scrum Guide row in README §10 is marked "next review".
- **Next review due:** README §6 at the next full-guide review (2027-05-13); Planning, Testing, Deployment, Maintenance 2027-05-16.

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
