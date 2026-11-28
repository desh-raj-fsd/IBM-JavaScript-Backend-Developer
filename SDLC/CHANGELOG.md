# LumenVenture SDLC Guide — Review Log

> One entry per review or significant change, **newest first**. Rules: [README §9.1 Review schedule](README.md#91-review-schedule).
> Each entry lists the date, the files, the reviewers, what changed (or "no changes needed") and the sources checked.

## 2026-11-28 — RACI table in every phase file

- **Files:** `README.md` (§3.1 footnotes, §9.2 item 3), `Planning.md` (§8.1), `Design.md`, `Development.md`, `Testing.md`, `Deployment.md`, `Maintenance.md` (§6.1), `tools/check.py`
- **Scope:** **structural change**, asked for in the README review; no owner or rule changed.
- **Reviewers:** <Tech Lead>, <Delivery Lead> — *to be filled in when the pull request is approved*
- **What changed:** each phase file's short Owners table (Accountable / Responsible / Consulted) is replaced by that phase's full RACI table from README §3.1, with the legend and a link back to the README; everything in the old tables is covered by the RACI rows. Footnotes ¹–⁴ now sit under the table that uses them (README and phase files), instead of once after all six tables. `tools/check.py` has a new **RACI** check that fails when a phase file's table differs from its README copy (tested by changing one cell in a copy of the folder); README §9.2 lists it.
- **Sources checked:** none needed (internal structure).
- **Not re-checked:** —
- **Next review due:** unchanged (2027-05-28 for all phase files and the README).

## 2026-11-28 — RACI split by phase and completed

- **Files:** `README.md` (§3.1 only)
- **Scope:** **structural change** to the RACI, asked for in the README review; no rule changed.
- **Reviewers:** <Tech Lead>, <Delivery Lead> — *to be filled in when the pull request is approved*
- **What changed:** §3.1 is now six tables, one per phase (3.1.1 Planning … 3.1.6 Maintenance), each with a link to its phase file. Activities went from 12 to 65: every gate (G1–G5 and the Definition of Ready), every activity in the phase files' owners and required-outputs tables, and every rule with a named owner, including the new track B, C and E work. New **SEC (Security Champion)** column (footnote ⁴). Role names and RACI letters are written in full in every cell (for example "C (Consulted)"); "—" means not involved. Rule links were removed from activity names. Each row has exactly one Accountable, and it matches the owner named in the rule.
- **Sources checked:** none needed (internal structure; owners taken from the phase files).
- **Not re-checked:** —
- **Next review due:** README 2027-05-28 (unchanged).

## 2026-11-28 — Fit the guide to LumenVenture's services and fix the problems from our own projects

- **Files:** `README.md` (header, §2 step 2, §3.3 rule 9, §4 two choices + new §4.1 delivery tracks + new §4.2 problem table, §6.1 rewritten by track with dual-track and shared-sprint diagram, §6.6 rules 10–14, §7 tree, §8, §10 three rows), `Planning.md` (§4.5, §8.4 rules 25–28, §8.5, §8.6.5, new §8.7), `Design.md` (§4.9 design flow, new §4.15, §6.1, §6.3, rules 27–32, §6.5), `Development.md` (new §4.16, rules 31–33), `Testing.md` (§4.16, new §4.17, rules 20–23), `Deployment.md` (new §4.11, rules 25–27, §6.5), `Maintenance.md` (new §4.13 and §4.14, rules 21–25, §6.6); templates changed: `user-story.md` (Definition of Ready), `project-brief.md` (track, capacity, visual quality bar), `pull_request_template.md` (ticket, design, QA told), `definition-of-done.md`, `service-review.md` (device fleet); **new templates:** `idea-validation.md`, `design-brief.md`, `sprint-delivery-note.md`, `takeover-audit.md`, `project-closure.md`.
- **Scope:** **significant change** requested by the company: the guide must solve the problems our team listed in its last project retrospective and fit the services we sell. Every new rule is linked to a problem in README §4.2 (P1–P13).
- **Reviewers:** <Tech Lead>, <Delivery Lead> — *to be filled in when the pull request is approved* (new **must** rules need both guide owners).
- **What changed:** each project now records a **type** (internal / client / prototype) **and a delivery track** (A product build, B connected product (IoT), C AI agents, D launch and brand, E support, takeover and small jobs), all Agile. New working rules: one shared sprint and board across projects; design one sprint ahead (dual-track); no work without a ticket and QA always informed; formal closure of stopped work. Design briefs with one approver, written feedback, 2-day turnaround and an escalation after 2 rounds; component library chosen by designer and Tech Lead together. Definition of Ready now needs an approved design, a tech note and QA review. Discovery interviews every decision-maker and observes the current system; a visual quality bar is agreed. Internal products need idea validation (build → measure → learn) with stop criteria. IoT: device-to-cloud-to-app design, firmware practices, layered device testing with a hardware-in-the-loop rig, signed staged OTA rollouts with abort and fallback, fleet review. AI: evals before the build, human approval for actions with outside effect, cost budget. Mobile: staged store releases. Client hand-off: sprint delivery note, closure report. Takeover audit for products from other vendors; small fixed-price jobs with before/after evidence; one knowledge base.
- **Sources checked (2026-11-28):** etsi.org deliverables folder for EN 303 645 (latest published 03.01.03); developer.apple.com "Release a version update in phases" (7-day schedule 1–100%, pause up to 30 days); Play Console Help "Release app updates with staged rollouts" (updates only); AWS IoT Core Developer Guide "Job rollout, scheduling, and abort configurations".
- **Not re-checked:** hardware milestone names (EVT/DVT/PVT) are common industry terms, not a standard; "dual-track" and "three amigos" are widely used practice names, not standards. Example numbers (2-day review turnaround, 5% first OTA stage, 2% abort threshold, 5 interviews) are our defaults, not external facts.
- **Next review due:** all changed files 2027-05-28.

## 2026-11-27 — Self-contained guide and pull request rule

- **Files:** `README.md` (§9, new §9.2, §1), all phase files (header, navigation, section titles), `Planning.md`, `Design.md`, `Development.md`, `Testing.md`, `Deployment.md`, `Maintenance.md`, three SVGs, `CHANGELOG.md`, new `tools/check.py`
- **Scope:** **structural change**, no practice changed. The guide no longer links to anything outside this folder (the root overview, five reference guides, and 17 links to course notes) and no longer mentions lectures, courses or notes.
- **Reviewers:** <Tech Lead>, <Delivery Lead> — *to be filled in when the pull request is approved*
- **What changed:** removed the "Overview" navigation links; replaced links to reference guides with public sources (OWASP cheat sheets, OpenAPI specification, refactoring catalog, design patterns catalog, Circuit Breaker article, *Use The Index, Luke*); removed "from course note" lines and "More:" links; phase sections renamed ("Core tasks", "Industry practices beyond the classic tasks"); old CHANGELOG entries no longer name course notes. README §9 now states that the folder is self-contained, and §9.2 settles the pull request rule (branch protection, 2 approvals, guide owners for **must** rules, required check, CHANGELOG entry, emergency path). New `tools/check.py` checks links, anchors, links that leave the folder, rule numbers, unlinked templates and images, course references and overdue reviews.
- **Sources checked (2026-11-27):** all new external links return HTTP 200 (refactoring.com, refactoring.guru, use-the-index-luke.com, spec.openapis.org, OWASP cheat sheets, martinfowler.com, postgresql.org).
- **Not re-checked:** GitHub branch-protection option names (settings screens change; check when setting up the repository).
- **Next review due:** README 2027-05-27.

## 2026-11-27 — Review: ISO 29148 status and spelling of OWASP

- **Files:** `README.md` (§10 ISO 29148 row)
- **Scope:** **targeted** re-check of time-sensitive facts.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** ISO/IEC/IEEE 29148 row: confirmed by ISO in 2024, a revision is under way (re-check at the next review). OWASP is spelled out as Open Worldwide Application Security Project.
- **Sources checked (2026-11-27):** iso.org 29148:2018 (status page); owasp.org.
- **Not re-checked:** facts in older entries.
- **Next review due:** 2027-05-27.

## 2026-11-27 — Full SDLC folder review: broken-item check, fact check, missing practices

- **Files:** `README.md` (§10 rows, dates), `01-Planning/Planning.md`, `02-Design/Design.md`, `05-Deployment/Deployment.md`, `06-Maintenance/Maintenance.md`
- **Scope:** **full-folder check** (links, anchors, images, templates, rule numbers, code syntax, versions, standards) plus targeted additions. Result: 0 broken internal links or anchors (all 6 phase files plus root overview), every template and image registered, 19 JavaScript blocks syntax-checked, `audit.py SDLC --rules` 0 problems.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** Design rule 26 and §4.5: **MFA** for staff and admin accounts, **passkeys** offered to end users. Maintenance rule 20 and §4.4: **CISA KEV** known-exploited vulnerabilities count as critical; **EPSS** to order the rest. Maintenance: **TLS certificate lifetimes** are shrinking (200 days now, 100 from Mar 2027, 47 from Mar 2029). Planning: **EU AI Act** dates (as amended by the Digital Omnibus) and **NIS2**. Deployment: CI example actions updated to current majors (`checkout@v7`, `setup-node@v7`, `login-action@v4`, `build-push-action@v7`), Node.js 26 (Active LTS) in examples, new rule 24 (pin third-party Actions to a full commit SHA). README §10: new rows for EU AI Act, NIS2, NIST SP 800-63-4, KEV/EPSS, certificate lifetimes.
- **Sources checked (2026-11-27):** owasp.org (Top 10 2025, ASVS 5.0.0, API 2023, LLM 2026, MFA cheat sheet); csrc.nist.gov (SSDF Rev. 1 still draft, SP 800-63-4 final July 2025, SP 800-52 revision planned); w3.org (WCAG 2.2 Recommendation; WCAG 3.0 is only a Working Draft); slsa.dev (v1.2); scrumguides.org (2020); nodejs.org and `nodejs/Release` schedule.json (v26 Active LTS, v24 and v22 Maintenance, v20 end of life 30 Apr 2026); pcisecuritystandards.org (v4.0.1); AI Act Service Desk timeline; NIS2 page; cisa.gov KEV; first.org EPSS; GitHub release APIs for the Actions versions; Docker Hub `node:26-alpine`; GitHub Actions secure-use guide; letsencrypt.org (45-day plan).
- **Not re-checked:** EAA date (EUR-Lex page would not load; the 28 June 2025 date is unchanged from the earlier check), GDPR text, ISTQB errata date, npm token limits, NIST SP 800-52 Rev. 3 (still only planned).
- **Next review due:** README, Planning, Design, Deployment, Maintenance 2027-05-27.

## 2026-11-27 — Review: architecture and deployment additions (corrections)

- **Files:** `02-Design/Design.md` (§4.12 item 6 wording)
- **Scope:** **targeted fact check** of the latest architecture and deployment additions (Design §4.1–§4.2 and §4.12, Development §4.7 `trust proxy` row). Not a full review.
- **What changed:** Design §4.12 item 6 now says VPC (AWS, Google Cloud) / VNet (Azure). The API gateway, choreography vs. orchestration and `trust proxy` guidance were re-checked and kept.
- **Sources checked (2026-11-27):** `nginx.org` load-balancing and upstream docs (`least_time` open source since 1.31.0; `health_check` commercial); `expressjs.com/en/guide/behind-proxies.html`; `martinfowler.com` microservices article (choreography preference); `12factor.net` processes and dev-prod parity; `kubernetes.io` Service page; `rfc-editor.org/info/rfc9457`.
- **Not re-checked:** AWS/Azure/GCP naming of the private-network term beyond common usage.
- **Next review due:** Design 2027-05-27.

## 2026-11-27 — Reverse proxy `trust proxy` pitfall

- **Files:** `03-Development/Development.md` (§4.7 Node.js pitfalls table extended with **Missing `trust proxy` behind a reverse proxy**)
- **Scope:** **targeted** 1-row extension to `Development §4.7` (load balancers, health checks, multi-AZ HA replicas, CDN, TLS, and backups were already present in `Design §4.12`, `Deployment §4.2`, and `Maintenance §4.6`).
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** Added a row to `Development §4.7` instructing Express services behind reverse proxies/load balancers to configure `app.set('trust proxy', N)` to the exact proxy hop count rather than leaving it unset or blindly setting `true`.
- **Sources checked (2026-11-27):** `expressjs.com/en/guide/behind-proxies.html` (`trust proxy` and internal IP behavior); `nginx.org/en/docs/http/load_balancing.html` (load-balancing algorithms and health checks).
- **Next review due:** Development 2027-05-27.

## 2026-11-27 — Cloud hosting models & VPC defense

- **Files:** `02-Design/Design.md` (§4.12 item 6 added on public vs. private/hybrid/on-premises selection and defense-in-depth beyond perimeter firewalls)
- **Scope:** **targeted** extension to existing `Design §4.12` (staging/production pipelines, immutable Docker promotion, IaC, Twelve-Factor dev/prod parity, and shared cloud responsibility were already covered in `Design §4.12` and `Deployment.md §3`).
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** Added `Design §4.12` point 6 establishing managed **public cloud** in private **VPC** subnets with TLS/auth everywhere as default, requiring an ADR + ownership assignment for **private/hybrid/on-premises** deployments.
- **Sources checked (2026-11-27):** `12factor.net/dev-prod-parity` (keeping development, staging, and production similar).
- **Next review due:** Design 2027-05-27.

## 2026-11-27 — API Gateway & choreography vs. orchestration

- **Files:** `02-Design/Design.md` (§4.2 extended with thin **API gateway** boundaries and **choreography vs. orchestration** guidance)
- **Scope:** **targeted** extension to existing `Design §4.2` (modular monolith, microservices, serverless, event-driven patterns, combination guidance, and `AsyncAPI` were already present).
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** Added guidance in `Design §4.2` keeping API gateways thin (routing/auth/TLS/rate limits only) and choosing between event-driven **choreography** vs. central **orchestration**.
- **Sources checked (2026-11-27):** `martinfowler.com/articles/microservices.html` ("smart endpoints and dumb pipes"); `martinfowler.com/articles/201701-event-driven.html` ("Event Notification").
- **Next review due:** Design 2027-05-27.

## 2026-11-27 — High cohesion & loose coupling

- **Files:** `02-Design/Design.md` (§4.2 module boundaries bullet extended with explicit **high cohesion** and **loose coupling**)
- **Scope:** **targeted** extension to existing `Design §4.2` (Mermaid/PlantUML diagrams as code, C4 levels, ports & adapters, fitness functions, and state-transition testing in `Testing.md` were already present).
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** Named **high cohesion** inside each bounded module and **loose coupling** across module boundaries in `Design §4.2`.
- **Sources checked (2026-11-27):** `c4model.com/introduction`, `mermaid.js.org/syntax/sequenceDiagram.html`, `mermaid.js.org/syntax/stateDiagram.html`, `omg.org/spec/UML/` (UML 2.5.1).
- **Next review due:** Design 2027-05-27.

## 2026-11-27 — Quality attributes interoperability & manageability

- **Files:** `02-Design/Design.md` (§4.1 quality-attributes table extended with **Interoperability** and **Manageability**; `Last reviewed` updated to `2026-11-27`)
- **Scope:** **targeted** extension to existing `Design §4.1` (architecture styles, C4 diagrams, ADRs, OpenAPI contracts, tech stack ADRs, fitness functions, and production load-balanced stateless rules were already present in `§4.2`, `§4.8`, `§4.14`, and rules 1–25).
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** Added an explicit **Interoperability** row (OpenAPI/AsyncAPI contracts, RFC 9457, versioning, vendor adapters) and paired **Manageability** with **Observability** (health checks and externalized validated config) in `Design §4.1`.
- **Sources checked (2026-11-27):** `c4model.com`, `adr.github.io`, `martinfowler.com/architecture/`, `omg.org/spec/UML/` (UML 2.5.1).
- **Next review due:** Design 2027-05-27.

## 2026-11-27 — Full-folder fact check (corrections)

- **Files:** `README.md` (§10 standards table), `02-Design/Design.md`, `03-Development/Development.md`, `04-Testing/Testing.md` (+ `images/sdlc-modern-v-model-in-ci.svg`), `05-Deployment/Deployment.md`
- **Scope:** a **review**, not new content: recent changes and the time-sensitive facts of the whole guide were re-checked against primary sources.
- **Reviewers:** <Tech Lead> — *to be filled in when the pull request is approved*
- **What changed:** OWASP Top 10 for LLM Applications is now the **2026** edition (was "2025"; README row and Development §4.8); SLSA row now **v1.2**; NIST SSDF row notes the **Rev. 1 / v1.2 initial public draft**; OpenAPI row adds patch **3.2.1** (10 Sept 2026); **ZAP** is now "ZAP by Checkmarx" (was "OWASP ZAP"; Testing, one diagram, root overview); MySQL `max_execution_time` limits only read-only `SELECT` statements (Development §4.15); the "lookup object" advice now says to read keys with `Object.hasOwn` or use a `Map` (a plain object returns inherited keys such as `constructor`); Docker QEMU wording hedged (Deployment §4.1); the Design execution-model bullet points to the stack ADR (rule 24); "Last checked" dates updated for every row verified today.
- **Verified today (primary sources):** owasp.org (Top 10:2025 list incl. A10 and SSRF inside A01, ASVS 5.0.0 published 30 May 2025, SAMM, API Security 2023, LLM Top 10 2026); pcisecuritystandards.org (v4.0.1); iso.org (29148:2018, 25010:2023, 14764:2022); semver.org 2.0.0; conventionalcommits.org 1.0.0; spec.openapis.org (3.2.0 of 19 Sept 2025, 3.2.1 of 10 Sept 2026); rfc-editor.org (9457, 9745, 8594, 9116); dora.dev (five metrics); European Commission CRA page (reporting from 11 Sep 2026, main obligations from 11 Dec 2027); GitHub changelog (npm classic tokens revoked 9 Dec 2025); docs.github.com (Dependabot default 3-day cooldown, not for security updates); docs.npmjs.com (`min-release-age`, trusted publishing); expressjs.com (Express 5 rejected promises call `next`); OWASP Password Storage cheat sheet (Argon2id 19 MiB, 2 iterations, 1 degree of parallelism); zaproxy.org; nodejs.org release rules; Docker multi-platform docs; PostgreSQL `statement_timeout`; MySQL optimizer-hints/blog (via search).
- **Not re-checked:** European Accessibility Act date and GDPR (stable law, general knowledge); ISTQB CTFL v4.0.1 errata date; npm "granular tokens at most 90 days"; Node.js LTS line numbers (read 2026-11-26).
- **Next review due:** README at the next full-guide review (2027-05-13); changed phase files 2027-05-27.

## 2026-11-27 — Composition & encapsulation

- **Files:** `03-Development/Development.md` (§4.4 extended with composition-over-inheritance and `#private`/closure state encapsulation)
- **Scope:** **targeted** 1-bullet extension to existing §4.4 (modular layered architecture, SOLID, and stateless processes were already present). Correction sweep: no wrong claims found.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** `Development §4.4` recommends favoring small pure functions and composition over deep class inheritance trees, and using `#private` fields or closures when classes guard internal invariants.
- **Sources checked (2026-11-27):** MDN (`developer.mozilla.org` — Functions guide, Arrow functions, Parameter glossary, Private `#` class properties).
- **Next review due:** Development 2027-05-27.

## 2026-11-27 — Constants, immutability & container choice

- **Files:** `03-Development/Development.md` (§4.4 extended with `const`/magic-number discipline, shared-object immutability, and `Map`/`Set`/`TypedArray` selection)
- **Scope:** **targeted** 1-bullet extension to existing §4.4 (runtime config validation and `N+1`/DB bounds were already present). Correction sweep: no wrong claims found.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** `Development §4.4` recommends defaulting to `const` (ESLint `prefer-const`), avoiding magic numbers, freezing/cloning shared config objects, picking `Map`/`Set` over repeated scans on large sets, and bounding dynamic arrays (`TypedArray`/streaming for large binary payloads).
- **Sources checked (2026-11-27):** MDN (`developer.mozilla.org` — `const` reassignment vs object mutation, JS `Array` resizable behavior, `TypedArray`); `cppreference.com` (`std::vector` contiguous memory and capacity reallocation).
- **Next review due:** Development 2027-05-27.

## 2026-11-27 — Branching hygiene & guard clauses

- **Files:** `03-Development/Development.md` (§4.4 extended with flat branching / guard clauses, strict `===`, and `switch` fall-through prevention)
- **Scope:** **targeted** 1-bullet extension to existing §4.4 (ESLint `complexity`/`max-depth`, `===`, and event-loop safety were already present). Correction sweep: no wrong claims found.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** `Development §4.4` recommends guard clauses (early returns), strict equality (`===`/`!==`), and preventing `switch` fall-through via `break`/`return` + `default`, a `Map` (or a lookup object read with `Object.hasOwn`), or ESLint `eqeqeq` and `no-fallthrough`.
- **Sources checked (2026-11-27):** MDN (`developer.mozilla.org` — JavaScript `switch` fall-through & `for` pre-check); Python docs (`docs.python.org` — compound statements); Oracle Java SE docs (`docs.oracle.com` — unused `goto` keyword).
- **Next review due:** Development 2027-05-27.

## 2026-11-27 — Query plans & DB least privilege

- **Files:** `03-Development/Development.md` (§4.15 extended with `EXPLAIN` / timeouts, `jsonb` GIN indexes, and least-privilege runtime DB role; rule 26 updated)
- **Scope:** **targeted** change extending existing §4.15 (least privilege, JSONB, parameterized queries, and migrations were already present). Correction sweep: no wrong claims found.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** `Development §4.15` and rule 26 add `EXPLAIN` query-plan checks, query timeouts (`statement_timeout` / `max_execution_time`), `jsonb` GIN index note, and separating the runtime CRUD DB role (including sequence `USAGE`) from shared/production DDL migrations.
- **Sources checked (2026-11-26/27):** PostgreSQL docs (`postgresql.org/docs/current/datatype-json.html`, `runtime-config-client.html`, `ddl-priv.html`, `sql-explain.html` — `jsonb` + GIN indexing, `statement_timeout`, sequence `USAGE`, `EXPLAIN`); Apache Cassandra docs (`cassandra.apache.org` — CQL typed table schemas); MongoDB docs (`mongodb.com` — JSON Schema validation).
- **Next review due:** Development 2027-05-27.

## 2026-11-26 — Execution model & target CPU builds

- **Files:** `02-Design/Design.md` (§4.14 execution model and memory-safety bullet), `05-Deployment/Deployment.md` (§4.1 target CPU architecture `--platform` bullet, rule 23), `05-Deployment/templates/pipeline-checklist.md` (target architecture build item)
- **Scope:** **targeted** change adding execution-model selection guidance and explicit target CPU architecture container builds. Correction sweep: no wrong claims found.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:** `Design §4.14` adds AOT vs. JIT/bytecode cold-start and memory-safety trade-offs plus optional WebAssembly; `Deployment §4.1`, `pipeline-checklist.md`, and **should** rule 23 recommend pinning the explicit target CPU architecture in CI (default `linux/amd64`).
- **Sources checked (2026-11-26):** Docker Docs Multi-platform builds (`docs.docker.com/build/building/multi-platform/` — `--platform linux/amd64,linux/arm64`); WebAssembly (`webassembly.org`); V8 (`v8.dev`), Python glossary (`docs.python.org/3/glossary.html`), .NET managed execution (`learn.microsoft.com`), Android (`developer.android.com/kotlin/first`), Lua (`lua.org/about.html`).
- **Next review due:** Design, Deployment 2027-05-26.

## 2026-11-26 — Stacks

- **Files:** `02-Design/Design.md` (new §4.14, rules 24–25), `03-Development/Development.md` (§4.8 license bullet, §4.10 Compose bullet)
- **Scope:** **targeted**. Already covered: ADR for new dependencies (Design rule 5), layered structure, front-end framework choice (§4.13), build vs buy, managed services. Correction sweep: none of the wrong claims (LAMP tied to Linux, relational databases cannot hold unstructured data, MongoDB as open source, React as a framework, Vue as "much newer") was found in the guide.
- **What changed:** Design §4.14 (software stack vs technology stack, layers, a criteria table for choosing a stack, data and license notes); rule 24 (stack ADR with two alternatives, license check, support dates; must on client and internal projects, should on prototypes; an acronym is not a decision), 25 (default to one primary database; extra store types need an ADR); source-available licenses such as SSPL can add duties (checked by the Tech Lead with the client's legal contact); Compose: containers use service names, `depends_on` does not wait for readiness.
- **Sources checked (2026-11-26):** MongoDB docs (multi-document ACID transactions); OSI "The SSPL is Not an Open Source License"; MySQL 8.4 manual (JSON data type, via search); PostgreSQL docs (json and jsonb); Microsoft docs (ASP.NET Core cross-platform); Docker Compose docs (service-name networking; Compose "does not wait until a container is ready", `service_healthy`).
- **Reviewers:** <Tech Lead> — *to be filled in when the pull request is approved*
- **Review:** a light independent review (no web) was applied: rules 24–25 tailored by project type with an owner, checklist and gate items added, license wording softened (MongoDB's own text says the SSPL targets offering MongoDB as a service), a former rule 26 folded into rule 24.
- **Not re-checked:** "default to one primary database" is a LumenVenture default, not an industry rule.
- **Next review due:** Design, Development 2027-05-26.

## 2026-11-26 — Build and package tools

- **Files:** `03-Development/Development.md` (§4.8 publishing bullet, §4.14 build-tool row, rule 30), `05-Deployment/Deployment.md` (§4.1 OS packages, rule 22)
- **Scope:** **targeted**; earlier changes (entry below) covered related topics. Most of this topic was already covered: CD vs deployment table (Deployment §3), build once and promote, pinned actions, trusted publishing, SBOM, lockfile and `npm ci`. Correction sweep: none of the wrong claims (CD as "deploy to staging", WebAssembly as a build tool, dpkg as a full package manager, "Red Hat Package Manager") was found in the guide. WebAssembly has no SDLC rule (no gap worth a rule).
- **What changed:** Dockerfile OS packages with `apt-get` (not `dpkg -i`), one layer, clean lists; CI feedback in about 10 minutes (rule 22); package `files` allowlist and `npm pack --dry-run` before publish (rule 30); build-tool row for front ends and back ends. Numbering corrected before commit: the pairing rules of the entry below are 27–29 (a clash with rule 26, published earlier, was caught by the new `audit.py --rules`). After the independent review: rule 22 now says "pull-request pipeline" and has an owner and a 1-hour default (consistent with Testing rule 14, and Testing §3 now says CI runs the pull-request test set); rule 30 fails the release job on forbidden paths; the build-tool row is front-end only.
- **Sources checked (2026-11-26):** Martin Fowler, Continuous Integration ("XP guideline of a ten minute build"); Docker build best practices (`apt-get update && apt-get install -y --no-install-recommends`, `rm -rf /var/lib/apt/lists/*`); Debian Reference (dpkg does not resolve dependencies); npm docs (`files`, `.npmignore`, `npm pack` `dry-run` and `json`); Docker best practices (pin base images, digests).
- **Not re-checked:** that every modern project reaches a 10-minute build (Fowler says "most"); Vite, esbuild and Rollup as the common choices (general practice).
- **Next review due:** Development, Deployment, Testing 2027-05-26.

## 2026-11-26 — Pairing and tools

- **Files:** `03-Development/Development.md` (§4.12, §4.8, rules 27–29), `02-Design/Design.md` (§4.13), `01-Planning/templates/working-agreement.md`
- **Scope:** **targeted**, small delta (most was already covered: pairing and mob rule 11, dependency checks §4.8, strangler pattern in Maintenance §4.10, ADR for new dependencies in Design rule 5). Correction sweep: none of the wrong claims (version control "tied to storage", Git "resolving" conflicts, frameworks "can't be incorporated" later, pairing as a "type of Agile") was found in the guide.
- **What changed:** pairing styles, remote pairing and `Co-authored-by` credit (§4.12); rules 27 (credit both), 28 (pairing does not replace the pull request review), 29 (`git diff --check` fails leftover conflict markers); library check now asks "do we need it?" and "how hard to replace?"; Design §4.13 describes the minimal-to-opinionated range of frameworks and step-by-step migration; working-agreement pairing line.
- **Sources checked (2026-11-26):** git-scm.com `git diff --check` ("Warn if changes introduce conflict markers or whitespace errors", non-zero exit); GitHub Docs co-author trailer format and Git vs GitHub; Fowler's inversion-of-control and pair-programming articles; Falco's strong-style post. 
- **Not re-checked:** whether a pair partner may count as the PR approver (we chose the safe default: an outside approval). A light review (separate subagent, no web) was run later the same day on this change; its 20 findings were applied: rule 28 is now a pointer to rule 1 and gate G3 (must), rule 29 gives the command and the tailoring (must on client and regulated), sources added for Git usage, React and Vue claims. Spot-checked later the same day: Git as a distributed VCS (Pro Git book), NestJS (docs.nestjs.com: out-of-the-box architecture, Express default, Fastify option) and pair programming as an XP practice (extremeprogramming.org and Beck's 1999 book, via a search result).
- **Next review due:** Development, Design 2027-05-26.

## 2026-11-26 — Teamwork

- **Files:** `README.md` (§2 step 5a, §3.3 rule 8, §6.6 rules 7–9, §7 docs tree, §8 templates, §10 Scrum Guide and new team-research rows), `01-Planning/Planning.md` (§8 required output, Gate G1 item, template table), `03-Development/Development.md` (§4.12 pair programming detail), new template `01-Planning/templates/working-agreement.md`
- **Scope:** **targeted** change: team practices from a source review that the guide was missing. Not a full review; README "Last reviewed" stays at the last full-guide review (2026-11-13). Planning review date moved to 2026-11-26. Correction sweep: "squad leader", "up to 10 developers" and "retrospective at project end" were not found in the guide.
- **Reviewers:** <Delivery Lead>, <Tech Lead> — *to be filled in when the pull request is approved*
- **What changed:**
  - **README §6.6 rules 7–9:** written working agreement at kickoff (must), team health check about every 3 sprints (should; never to rate individuals), deliberate knowledge sharing with bus factor of at least 2, buddy and onboarding (should).
  - **README §3.3 rule 8:** how to read "squad" (similar to a Scrum team; 10 or fewer people in total, default 4–8; no extra "squad leader" role: PO, TL and DL split the duties).
  - **README §2 step 5a, §7, §8:** working agreement in the kickoff steps, the docs tree and the template list.
  - **Planning:** working agreement as a required output (must for internal and client projects; should for prototypes) and a Gate G1 checklist item.
  - **Development §4.12:** driver and navigator, swap often, at most about 6 hours a day, spike for large unknowns.
  - **New template:** `working-agreement.md` (goal, communication, ways of working, treatment of each other, knowledge sharing, 5-question health check).
  - **Already covered, so not added again:** retrospective every sprint (README §6.6 rule 2), review within one working day and CODEOWNERS (Development), pair and mob programming rule 11, blameless postmortems (Maintenance), team roles and backups (README §3.3).
- **Sources checked (2026-11-26):** scrumguides.org Scrum Guide 2020 ("typically 10 or fewer people", "self-managing", "no sub-teams or hierarchies", Sprint Retrospective purpose and that it concludes the Sprint); Google re:Work "Understand team effectiveness" (five dynamics; read through a web-search result because the direct page URLs I tried returned 404); Spotify engineering model paper, 2012 (squad similar to a Scrum team, no formally appointed squad leader but a product owner, agile coach access, tribe, chapter, guild, Dunbar number); martinfowler.com "On Pair Programming" (driver, navigator, rotation, about 6 hours); Melvin Conway, "How Do Committees Invent?" (1968); GitHub Docs about code owners.
- **Not re-checked:** Brooks's law and The Mythical Man-Month (1975); Tuckman's team stages; Team Topologies' four team types (checked in the 2026-11-16 roles entry); the Google study itself (only the re:Work summary was read).
- **Next review due:** Planning, Development 2027-05-26; README §6.6 at the next full-guide review (2027-05-13).

## 2026-11-26 — Back-end baseline & payments

- **Files:** `README.md` (§10 standards table: `OWASP API Security Top 10` updated, new `PCI DSS` row, `RFC 9457` and `Node.js release schedule` dates updated), `02-Design/Design.md` (§4.4 status codes + `API4:2023`, §4.5 BOLA `API1:2023` + PCI DSS v4.0.1 tokenization, rule 23), `03-Development/Development.md` (§4.9 ORM expansion, `API4:2023` rate limiting, payment/card data row, new §4.15 Database access, ORMs, and migrations, rule 26)
- **Scope:** **targeted** change: add the back-end practices from a source review that the guide was missing or needed to harden. Not a full review; README "Last reviewed" stays at the last full-guide review (2026-11-13); Design and Development review dates stay 2026-11-26. Correction sweep: none of corrected claims ("API is code", "route is a path to a website", "Node.js is a framework", storing raw credit card numbers) was found in the guide.
- **Reviewers:** <Tech Lead>, <Security Champion>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Design §4.4, §4.5 & rule 23:** added `405` / `422` / `429` status codes (`OWASP API4:2023` Unrestricted Resource Consumption), explicitly referenced `OWASP API1:2023` BOLA (Broken Object Level Authorization), and added PCI DSS v4.0.1 payment tokenization guidance plus **must** rule 23 forbidding raw PAN/CVV storage in application databases or logs.
  - **Development §4.9, §4.15 & rule 26:** added the PCI DSS v4.0.1 payment/card data row and `OWASP API4:2023` reference in §4.9; added §4.15 covering connection pooling, `N+1` query prevention (eager loading / explicit `JOIN`s and dev SQL logging), ORM vs. raw parameterized SQL trade-offs, bounded/indexed searches, and versioned backward-compatible schema migrations; added **should** rule 26.
  - **README §10:** updated `OWASP API Security Top 10` (2023), `RFC 9457`, and `Node.js release schedule` check dates to `2026-11-26`; added `PCI DSS v4.0.1` row.
- **Sources checked (2026-11-26):** PCI Security Standards Council Document Library (`pcisecuritystandards.org` — PCI DSS v4.0.1 active standard, Requirements 3 & 12.5.2 tokenization scope reduction); OWASP API Security Top 10 (`owasp.org` — 2023 edition, `API1:2023` BOLA, `API4:2023` Unrestricted Resource Consumption); OWASP Top 10 (`owasp.org` — 2025 edition); RFC Editor (`rfc-editor.org` — RFC 9457 *Problem Details for HTTP APIs*, July 2023, obsoletes RFC 7807); Node.js release schedule (`nodejs.org` — v20 EOL April 30, 2026; v22 Maintenance LTS EOL April 30, 2027; v24 Maintenance LTS; v26 Active LTS; annual cycle from v27); Express.js docs/blog (`expressjs.com` — Express 5.1.0+ default on npm, Node.js 18+, automatic async rejection forwarding); Python (`python.org` — 3.15 stable, 3.14 bugfix), Django (`djangoproject.com` — 6.1 stable, 5.2 LTS), Flask (`pypi.org` / `palletsprojects.com` — 3.1.3), FastAPI (`pypi.org` — 0.165.0). A second independent reviewer (subagent) verified all 6 primary-source claims and agreed with all 6; a separate Checklist C reviewer caught acronym expansions (`PCI DSS`, `ORM`, `BOLA`, `PAN`/`CVV`), `API4:2023` cross-references, and `eager loading` gloss, all fixed before `audit.py`.
- **Not re-checked:** RFC 9745, RFC 8594, RFC 9116 (dates in README §10 kept as-is); ORM/tool names used as examples (Prisma, Drizzle, SQLAlchemy, Django ORM).
- **Next review due:** Design, Development 2027-05-26.

## 2026-11-26 — Front end

- **Files:** `README.md` (§8 template row, §10 standards rows: WCAG updated, new Core Web Vitals and browser-security rows), `02-Design/Design.md` (new §4.13, rules 18–22, done-when and G2 items), `03-Development/Development.md` (new §4.14, rules 20–25, Definition of Done line), `04-Testing/Testing.md` (new §4.16, rules 18–19, exit-criteria line), `05-Deployment/Deployment.md` (§4.10 browser-security bullets, rules 20–21, G4 item), `06-Maintenance/Maintenance.md` (new §4.12, rules 18–19, healthy-service item), new template `03-Development/templates/frontend-checklist.md`, templates `definition-of-done.md`, `05-Deployment/templates/pipeline-checklist.md`, `06-Maintenance/templates/service-review.md`
- **Scope:** **targeted** change: add the front-end practices from a source review that the guide was missing. Not a full review; README "Last reviewed" stays at the last full-guide review (2026-11-13). Review dates of the five edited phase files moved to 2026-11-26. Correction sweep: none of corrected claims (HTML "physical structure" and "formatting", JavaScript "object-oriented", "SAS", "Learner Style Sheets", React "Facebook", "Vue layer") was found in the guide.
- **Reviewers:** <Tech Lead>, <QA Engineer>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Design §4.13:** front-end decisions with defaults: approach and ADR with framework end-of-life date; responsive, mobile-first, same content on every device; written browser support policy; WCAG 2.2 AA and Core Web Vitals targets; one styling approach; shared components and design tokens. Rules 18–22.
  - **Development §4.14:** front-end code habits: native HTML elements, accessibility checks, TypeScript, one styling approach, Sass `@use` instead of `@import`, mobile-first CSS and the viewport tag, API error handling, "the browser is untrusted", cookie flags, third-party scripts and SRI, bundle size. Rules 20–25.
  - **Testing §4.16:** layers (unit, component, a few cross-browser end-to-end tests), accessibility (automated plus manual keyboard and screen reader), responsive checks, lab and field performance, XSS cases. Rules 18–19.
  - **Deployment §4.10:** CSP (strict, Report-Only first), cookie flags, SRI, source maps kept out of public reach. Rules 20–21.
  - **Maintenance §4.12:** real-user Core Web Vitals, front-end error tracking, end-of-life tracking (AngularJS, Vue 2, Sass `@import`, INP replacing FID). Rules 18–19.
  - **New template:** `frontend-checklist.md` (decisions, tooling, every UI change, security, performance, after release).
  - **README §10:** WCAG row now records the 12 December 2024 republication and removal of 4.1.1; new Core Web Vitals and browser-security rows.
- **Sources checked (2026-11-26):** web.dev Core Web Vitals (thresholds, 75th percentile, INP replaced FID in 2024); W3C WCAG 2.2 and the Understanding page for 2.5.8 (Recommendation of 12 Dec 2024, 4.1.1 removed, contrast 4.5:1, target size 24×24 CSS px at AA); MDN Set-Cookie, Content-Security-Policy implementation guide, Subresource Integrity and Viewport meta element; sass-lang.com (`@import` deprecated since Dart Sass 1.80.0, removal in 3.0.0; also reproduced locally with Dart Sass 1.108); lesscss.org ("Leaner Style Sheets"); angular.dev releases page (v20 28 May 2025, v21 19 Nov 2025, v22 3 June 2026; 12-month major cycle from v22); docs.angularjs.org (support ended January 2022); vuejs.org FAQ (Vue 3 current, Vue 2 end of life 31 Dec 2023); react.dev (framework recommendation, React Foundation launched 24 Feb 2026, React 19.3 on 9 Sep 2026); GoogleChrome/web-vitals repository; playwright.dev browsers page. Two independent reviewers (separate subagents) re-checked the changes. They agreed on all verified facts (Core Web Vitals, WCAG 2.2, Sass, cookies, CSP, SRI, viewport, web-vitals, Playwright, AngularJS and Vue 2 end of life). They found three wrong Angular dates in an earlier draft (Baseline dates, not release dates; fixed from the angular.dev releases page) and several wording and strength problems in the guide: accessibility table vs rule 18, rule 18 scope for internal tools, rule 19 overlap with Maintenance rule 9, CSP `unsafe-inline` scope, a missing CSRF note (`SameSite=Lax` is not a full defence), the `browserslist` example, and missing acronym expansions. All are fixed.
- **Not re-checked:** the `eslint.config.js` flat config claim is from an earlier entry; Sass first release date (2006) comes from a secondary source (Wikipedia); tool names such as axe, Lighthouse, Stylelint, Testing Library, Dependabot and Renovate are not re-verified.
- **Next review due:** Design, Development, Testing, Deployment, Maintenance 2027-05-26.

## 2026-11-26 — Web and cloud baseline (second pass)

- **Files:** `README.md` (§10 standards table), `02-Design/Design.md` (new §4.12, done-when and G2 items, rules 14–17), `03-Development/Development.md` (Twelve-Factor map in §4.5, rules 18–19, duplicate §4.11 renumbered), `05-Deployment/Deployment.md` (new §4.10, done-when and G4 items, rules 16–19), `06-Maintenance/Maintenance.md` (new §4.4.1, rules 16–17), templates `05-Deployment/templates/pipeline-checklist.md` and `06-Maintenance/templates/go-live-checklist.md`
- **Scope:** **targeted** change: the web and cloud practices from a source review that the guide was missing. Not a full review; README "Last reviewed" stays at the last full-guide review (2026-11-13). Review dates of the four edited phase files moved to 2026-11-26.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Design §4.12:** delivery style per part (static, SSR, SPA, API), CDN and cache-header defaults, cloud service models with shared responsibility, availability zones (multi-AZ default; multi-region only with an ADR and RTO/RPO), link to Twelve-Factor. Rules 14–17: stateless and 2+ instances in 2+ zones, CDN and cache headers, multi-region needs an ADR, provider vs our responsibilities listed.
  - **Development §4.5:** the 12 factors mapped to where each lives in the guide. Rules 18–19. The second "4.11" (environments and editor standards) is now **§4.13** (it clashed with "Using AI coding assistants well").
  - **Deployment §4.10:** go-live web baseline: DNS TTL and IaC, HTTPS-only with redirect, TLS 1.2 minimum / 1.3 preferred, HSTS, cache-header checks with `curl -I`, check from outside the network. Rules 16–19, gate G4 and done-when items.
  - **Maintenance §4.4.1:** triage by four boundaries (client, edge and network, application, persistence). Rules 16–17.
  - **Templates:** pipeline checklist and go-live checklist got DNS, HTTPS, HSTS, CDN and multi-AZ checks.
  - **Fixes to earlier additions:** "valid TLS 1.3 certificate" corrected (a certificate has no TLS version) and `.eslintrc` replaced by the ESLint flat config.
- **Gap-analysis note:** the first keyword search had a wrong pattern and listed graceful shutdown, readiness/liveness probes and environment-variable config as missing. They are already in Deployment §4.2, §3 and Development §4.5, so they were **not** added again.
- **Sources checked:** 12factor.net (12 factors, last updated 2017); MDN Strict-Transport-Security and Cache-Control; NIST SP 800-52 Rev. 2 page (TLS 1.2 baseline, TLS 1.3 support by 1 Jan 2024; a Rev. 3 is planned); AWS Shared Responsibility Model and AWS Availability Zones whitepaper; eslint.org flat config page.
- **Not re-checked:** RFC numbers (6797, 8446, 8996, 9111, 8246) were taken from memory, not re-read; the AWS pages are one provider's wording (Azure and GCP use the same idea); no second independent verification round was run.
- **Next review due:** Design, Development, Deployment, Maintenance 2027-05-26.

## 2026-11-16 — Development environment

- **Files:** `03-Development/Development.md` (new §4.11 Development environments and editor standards), `03-Development/templates/repo-setup-checklist.md` (Repository section: `.editorconfig` and DevContainers)
- **Scope:** **targeted** change: add editor configuration and containerized development environment standards from a source review. Correction sweep: confirmed Atom is not referenced in the SDLC guide, and legacy unmaintained editors are formally retired in §4.11.
- **Reviewers:** <Tech Lead>, <Developers> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Development §4.11:** Development environments and editor standards: required `.editorconfig` in repository root (UTF-8, LF, 2 spaces, trim whitespace, final newline); containerized reproducible setups via DevContainers (`.devcontainer/devcontainer.json`); retirement of unmaintained editors (e.g. Atom, sunset Dec 2022) in favor of modern LSP-driven tools.
  - **Templates:** `repo-setup-checklist.md` updated under `## Repository` with explicit checks for `.editorconfig` and documented development environments / DevContainers.
- **Sources checked:** EditorConfig specification (editorconfig.org); Development Containers Specification (containers.dev); GitHub announcement of Atom sunset (December 15, 2022).
- **Not re-checked:** None.
- **Next review due:** Development 2027-05-16.

## 2026-11-16 — Roles
- **Files:** `README.md` (§2 kickoff step 1, §3 DL row and hats note, §3.1 two RACI rows, new §3.2 optional and shared roles, new §3.3 role rules 1–7, §7 docs tree, §8 templates, §10 Scrum Guide row), `01-Planning/Planning.md` (§8.2 required outputs, §8.3 Gate G1, §8.5 templates), new template `01-Planning/templates/team-roles.md`
- **Scope:** **targeted** change: add the role practices from a source review that the guide was missing. Not a full review of the phase files; README "Last reviewed" stays the last **full-guide** review (2026-11-13). Correction sweep: none of corrected claims ("in Agile the equivalent role [of a project manager] is called a Scrum master", stakeholders are only "the people for whom the product is being designed", "SRE, sometimes called … ops engineer", the PO/PM "leading development efforts") was found in the guide (Development §1 "a project manager assigns all tasks" is in the Waterfall column, which is correct).
- **Reviewers:** <Delivery Lead>, <Tech Lead>; Planning: <Product Owner> — *to be filled in when the pull request is approved*
- **What changed:**
  - **README §3.2 optional and shared roles:** UX / product designer, technical writer, SRE / platform team (shared), business analyst, solution architect, line manager (outside the team) — when we add each one, and who covers it if absent; SRE is not "ops" and never takes over the team's on-call; the Delivery Lead is not a task-assigning project manager (PM work split between PO, Developers, DL and Sponsor); product manager ≠ Product Owner; Mermaid "who decides what".
  - **README §3.3 role rules 1–7:** team-roles record with backups (PO and TL from kickoff, on-call from go-live); PO decides what, TL and Developers decide how it is built; DL does not assign tasks or report on individuals; the building team stays on call; people management outside PO and DL; at most 3 hats (Developer, on-call and backup duty not counted), PO ≠ DL where possible; designer for projects with changing screens, solution architect for multi-system client projects.
  - **README §3.1 RACI:** rows for UX design and usability tests, and user documentation (A = PO, matching §7.1).
  - **New template:** `team-roles.md`: core and optional roles, share of time, backups, line managers, checks before G1, RACI changes; filled example for the Book Review API.
  - **Planning:** team-roles record is a required output (prototypes: should) and a Gate G1 check.
- **Sources checked:** scrumguides.org (2020 Scrum Guide text, still "Official Current Version"; Scrum Master and Product Owner accountabilities; "typically 10 or fewer people"); github.com/ScrumGuides/ScrumGuide-ExpansionPack (Expansion Pack is "an optional companion", not a replacement); PMI stakeholder definition (PMBOK Guide wording; PMI Lexicon v5.0 confirmed to exist, but its exact word order was not readable, so the guide quotes the PMBOK wording); sre.google/sre-book/introduction (SRE definition, 2003, 50% ops cap); ACM Queue "A Conversation with Werner Vogels" (2006, "You build it, you run it"); teamtopologies.com/key-concepts (four team types); GitHub Docs (PR authors cannot approve their own pull requests). A second, independent verification round by a separate reviewer agreed on all of these except the PMI word order, which is now avoided.
- **Not re-checked:** the PRINCE2 expansion (only secondary sources found; not used in the guide).
- **Next review due:** Planning 2027-05-16; README §3 at the next full-guide review (2027-05-13).

## 2026-11-16 — Documentation

- **Files:** `README.md` (§7 docs tree, new §7.1 documentation map, new §7.2 documentation rules 1–9, §8 templates), `03-Development/Development.md` (§4.12, §5, §6.2, pointer in §6.4, §6.5), new template `03-Development/templates/sop.md`, templates `definition-of-done.md`, `pull_request_template.md`, `05-Deployment/templates/pipeline-checklist.md`, `06-Maintenance/templates/service-review.md`, `06-Maintenance/templates/runbook.md`
- **Scope:** a **targeted** change: add the documentation practices from a source review that the guide was missing. Not a full review of the phase files; the README "Last reviewed" date stays at the last **full-guide** review (2026-11-13), as for the earlier targeted changes. Correction sweep: none of corrected claims ("process documentation describes how to complete a task", "user acceptance specifications", working papers as technical documentation, "updating documentation happens during the maintenance phase") were found in the guide.
- **Reviewers:** <Delivery Lead>, <Tech Lead>; Development: <a developer>; Maintenance templates: <Security Champion> — *to be filled in when the pull request is approved*
- **What changed:**
  - **README §7.1 documentation map:** product documentation (requirements, design, technical, QA, user) and process documentation (plans and standards, reports and notes, SOPs and runbooks), each with documents, owner role (consistent with the RACI), audience and when it is updated; Mermaid diagram.
  - **README §7.2 documentation rules 1–9:** docs in Git with an owner; docs updated **in the same PR** (help center: same release), never "later"; no secrets or personal data in docs; API reference generated from OpenAPI; docs checks in CI (must on regulated); SOPs for repeated project-specific procedures, with tool-enforced steps (must on client and regulated projects for "merge to `main`"; the release checklist is the release SOP); review dates for SOPs and runbooks; working papers are process docs — decisions into ADRs or the decisions log; user documentation for user-facing features (must on client projects, accessible).
  - **New template:** `sop.md` — SOP structure plus the filled example "Merging a change to `main`".
  - **Development:** §4.12 docs in the same PR, product vs. process docs, SOPs enforced by tools, docs checks in CI with pinned tools (YAML excerpt); §5 DoD line; §6.2 rows for SOPs and docs checks; §6.4 points to README §7.2.
  - **Templates:** Definition of Done docs item is now ★ (same PR or "no docs change"); PR template docs line; pipeline checklist docs checks; service review lists overdue SOPs and runbooks; runbook gets Last reviewed / Next review due.
- **Sources checked:** EPA QA/G-6 *Guidance for Preparing Standard Operating Procedures* (April 2007 — SOP definition, update when the procedure changes, periodic review "e.g. every 1–2 years"); GitHub Docs "About code owners" and rulesets (any one listed owner is enough; last matching pattern wins); markdownlint-cli2 README (`"#node_modules"` negation); Redocly CLI docs (`lint`, `build-docs --output`); Diátaxis (diataxis.fr); also ISO/IEC/IEEE 29119-3:2021 and ISO/IEC/IEEE 26514:2022 (IEEE SA and ISO catalogue pages) and agilemanifesto.org. Second, independent verification round by a separate reviewer: all facts agreed.
- **Not re-checked:** lychee-action version (left as a placeholder to pin); WCAG 2.2 row in §10 stays "next review".
- **Next review due:** Development 2027-05-16; README §7 at the next full-guide review (2027-05-13).

## 2026-11-16 — Testing

- **Files:** `04-Testing/Testing.md` (jargon, §1, §3, §4.1, §4.2, new §4.13–§4.15, §5, §6.2, §6.3, rules 11 example, 13–17, §6.5), new template `04-Testing/templates/test-case.md`, `04-Testing/templates/test-strategy.md` (§2.1, §2.2, §5), `04-Testing/templates/bug-report.md`, `03-Development/templates/definition-of-done.md`, `05-Deployment/templates/release-checklist.md`, `06-Maintenance/Maintenance.md` (§4.5, §5, rule 5), `README.md` (§7 docs tree, §8 templates, §10 standards); new diagram `04-Testing/images/sdlc-modern-regression-cadence.svg`
- **Scope:** a **targeted** change: add the testing practices from a source review that the guide was missing. Not a full review of the phase files. Correction sweep: none of corrected claims (for example "error-free software", "regression testing, also called maintenance testing", "system testing validates", "acceptance testing during maintenance") were found in the guide.
- **Reviewers:** <QA Engineer>, <Tech Lead>; Maintenance: <Security Champion> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Testing:** §1 testing cannot prove the absence of defects; §3 what each level is for (integration can be black- or white-box; system **verifies**; acceptance **validates, before release**); §4.1 grey-box, change-related testing, the what / how / why classification (Mermaid), usability and accessibility are non-functional (ISO/IEC 25010:2023), maintenance testing contains confirmation and regression testing; §4.2 confirmation, compatibility, documentation, recovery, UAT, OAT and contract / regulatory acceptance; new §4.13 the seven ISTQB testing principles; new §4.14 test-case fields and test design techniques (equivalence partitioning, boundary values, decision tables, state transition) with a `node:test` example; new §4.15 regression schedule (PR affected / `main` full / nightly / release commit / after deploy), test impact analysis, one bug-ID test per fix; §5 exit criteria; §6.2 nightly regression and written test cases; G4 now requires the **full** suite on the release commit. Rules 13–17 (design techniques, regression schedule, bug-ID test that fails without the fix, compatibility matrix and docs checked against OpenAPI, written test cases for manual / UAT / OAT tests). Rule 11 example ID changed to `REQ-10` (REQ-09 already meant "one review per user per book" in Design).
  - **New template:** `test-case.md` — written test cases plus an execution record with sign-off, for tests that cannot be automated (should on client projects, must on regulated projects).
  - **Templates:** test strategy gets a regression schedule, test design techniques, supported platforms, compatibility / recovery / documentation targets; bug report and Definition of Done require the bug-ID test that fails without the fix; release checklist requires the full regression suite on the release commit.
  - **Maintenance:** hotfix text and rule 5 point to Testing rule 15 (bug-ID regression test).
- **Sources checked:** ISTQB CTFL syllabus v4.0.1 (istqb.org — seven principles, v4.0 released 21 April 2023, maintenance testing §2.3); ISO/IEC 25010:2023 foreword (interaction capability, inclusivity and user assistance, safety, flexibility); Vitest CLI docs (`--changed` with a branch or commit); Jest CLI docs (`--changedSince`); GitHub Actions docs (schedule cron in UTC). Second, independent verification round by a separate reviewer.
- **Not re-checked:** WCAG 2.2 and the other README §10 rows still marked "next review"; tool names used only as examples (k6, Playwright, Pact, Testcontainers, Stryker, fast-check).
- **Next review due:** Testing, Maintenance 2027-05-16; README §7, §8 and §10 at the next full-guide review (2027-05-13).

## 2026-11-16 — Versioning and compatibility

- **Files:** `03-Development/Development.md` (§4.2.1, §4.8, §4.11, §6.2, rules 8 and 14–17, §6.5), new template `03-Development/templates/versioning-policy.md`, `02-Design/Design.md` (§4.4.1, rules 12–13), `05-Deployment/Deployment.md` (§4.5, §4.7, rule 15), `05-Deployment/templates/release-checklist.md`, `06-Maintenance/Maintenance.md` (§4.9), `README.md` (§7 docs tree, §8 templates, §10 standards); new diagrams `03-Development/images/sdlc-modern-one-version-everywhere.svg`, `02-Design/images/sdlc-modern-api-compatibility.svg`
- **Scope:** a **targeted** change: add the versioning and compatibility practices from a source review that the guide was missing. Not a full review of the phase files.
- **Reviewers:** <Tech Lead>, <a developer>; Design: <Security Champion>; Deployment: <Delivery Lead> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Development:** §4.2.1 versioning policy — SemVer is **3 parts** and is about **compatibility, not size**; pre-release labels and npm dist-tags; build metadata after `+` (four-part numbers are not SemVer); `0.y.z` only before the first client; released versions are immutable; one version everywhere; compare versions with a SemVer library; a `/version` route example. §4.8 version-range table (`^`, `~`, exact, `^0.x`) and runtime version (`engines`, `.nvmrc`, Docker base image, CI matrix). §4.11 AI tools suggest outdated APIs and versions. Rules 14–17; rule 8 now points to the versioning policy.
  - **New template:** `versioning-policy.md` (what is versioned and how, bump rules, supported versions, deprecation periods, how to see the running version) — required on internal, client and regulated projects.
  - **Design:** §4.4.1 API compatibility — backward vs. forward compatibility (tolerant reader for responses and events; requests still reject unknown fields), breaking-change table, `/v2` in parallel, notice periods (≥ 6 months external, ≥ 1 month internal), usage tracking, OpenAPI diff in CI. Rules 12–13.
  - **Deployment:** post-deploy smoke test checks `/version`; image tags = version + commit SHA, production by tag or digest, never `latest`; pre-releases never reach production; rule 15. Release checklist: release types now **Major / Minor / Patch** (the old "Minor / Major / Hotfix" list had no Patch), Git tag field, version and `/version` checks.
  - **Maintenance:** §4.9 usage per API version and client; errors split by `service.version`; supported-versions list checked in the service review.
- **Sources checked:** a source review (SemVer 2.0.0 rules and precedence; npm range semantics, checked by running the `semver` package; RFC 9745 / RFC 8594 headers; Ubuntu 18.04 point-release dates). **Not re-checked against primary sources in this change** — the SemVer and Conventional Commits rows in README §10 are marked "next review".
- **Next review due:** Development, Design, Deployment, Maintenance 2027-05-16.

## 2026-11-16 — Working rhythm and methodology

- **Files:** `README.md` (§6 rewritten and extended, §10 standards table), `01-Planning/Planning.md` (§4.17, step 7 of §8.6.2, rules 23–24), `01-Planning/templates/project-brief.md` (§9), `04-Testing/Testing.md` (§4.12, rule 12), `05-Deployment/Deployment.md` (rule 14), `06-Maintenance/Maintenance.md` (rule 15); new diagrams `images/sdlc-modern-methodology-by-project-type.svg`, `images/sdlc-modern-sprint-cadence.svg`, `01-Planning/images/sdlc-modern-fixed-time-flex-scope.svg`, `04-Testing/images/sdlc-modern-v-model-in-ci.svg`
- **Scope:** a **targeted** change: write down **how LumenVenture works** (methodology), using the practices from a source review. Not a full review of the phase files.
- **Reviewers:** <Delivery Lead>, <Tech Lead>; Planning: <Product Owner>; Testing: <QA Engineer> — *to be filled in when the pull request is approved*
- **What changed:**
  - **README §6:** rhythm table corrected to Scrum Guide 2020 terms (**Sprint Review**, **Sprint Goal**, Sprint Retrospective; refinement is an activity, not an event); the sprint is **no longer called a "planning-to-release loop"** — releases follow the pipeline. New §6.1 methodology by project type (default Scrum; Kanban for prototypes and after go-live; V-model discipline for regulated work; phase gates kept as governance, not as Waterfall delivery); §6.2 Scrum accountabilities and artifacts mapped to our roles; §6.3 Kanban lane with WIP limit; §6.4 releases are not tied to sprints; §6.5 anti-patterns (Water-Scrum-Fall, mini-waterfall, cargo-cult Agile, velocity as a target); §6.6 six working-rhythm rules.
  - **Planning:** §4.17 fix time and cost, flex scope; cone of uncertainty; throughput (Monte Carlo) forecasting with the 85% date; contract models for client projects; rules 23–24. Discovery step 7 now says Sprint Review instead of "demo".
  - **Project brief template:** §9 now records the methodology, the delivery / contract model and the forecast method.
  - **Testing:** §4.12 the V-model idea done continuously (each design artifact gets its test in the same sprint; verification vs. validation; full V per increment for ISO 26262 / IEC 62304 / GAMP 5 work); rule 12 — no testing-only sprint or phase.
  - **Deployment:** rule 14 — releases are not tied to the sprint end.
  - **Maintenance:** rule 15 — maintenance and support in a Kanban lane with a WIP limit, same backlog.
- **Sources checked:** a source review (Scrum Guide 2020 accountabilities, events, timeboxes and "Sprint Review is not a gate to releasing value"; Agile Manifesto 2001; Royce 1970; Kanban, XP, Lean). **Not re-checked against primary sources in this change** — the Scrum Guide row in README §10 is marked "next review".
- **Next review due:** README §6 at the next full-guide review (2027-05-13); Planning, Testing, Deployment, Maintenance 2027-05-16.

## 2026-11-16 — Planning (+ Testing)

- **Files:** `01-Planning/Planning.md`, `01-Planning/templates/` (`user-story.md`, `stakeholder-register.md`, `project-brief.md`), `01-Planning/images/` (4 new SVGs), `04-Testing/Testing.md` (rule 11), `README.md` (§8 template list, §10 standards table)
- **Scope:** a **targeted** change: add the requirement practices from a source review that the guide was missing. Not a full review of either phase file.
- **Reviewers:** <Product Owner>, <Delivery Lead>; Testing rule: <QA Engineer> — *to be filled in when the pull request is approved*
- **What changed:**
  - **Planning:** new §2.1 **six-step requirements process** (stakeholders → goals → elicit → document → confirm → prioritize) and the three moments it runs; §4.1 expanded with the **power / interest grid**, personas, often-forgotten groups and the one-decision-maker rule; §4.4 constraint vs. assumption (an assumption is a risk); new §4.10 **goals, SMART objectives, OKRs**, outcome over output, `OBJ-n` IDs; §4.11 **elicitation toolbox** + interview rules; §4.12 **EARS** patterns, vague vs. testable, the four SRS categories; §4.13 **ISO 29148 quality characteristics**, validation vs. verification, written approval and baseline; §4.14 **RICE, WSJF, Kano**, value vs. effort; §4.15 **URS / SRS / SysRS** vs. ISO names (BRS, StRS, SyRS, SRS) and what LumenVenture writes; GAMP 5 URS for GxP clients; §4.16 often-missed requirement areas. Jargon, §7 checklist, §8.2 outputs, Gate G1 and rules 18–22 updated.
  - **Templates:** user story gets type, priority, objective, source, EARS rules and a quality-check DoR item; stakeholder register gets power / interest / strategy, a named decision-maker and the forgotten-groups checklist; project brief §2 becomes goals → `OBJ-n` key results.
  - **Testing:** rule 11 — requirement traceability check in CI (should; must on regulated projects).
  - **Diagrams:** `sdlc-modern-requirements-six-steps.svg`, `sdlc-modern-stakeholder-grid.svg`, `sdlc-modern-goal-to-test-chain.svg`, `sdlc-modern-requirement-documents.svg`, plus Mermaid flows in §2.1 and §4.13.
- **Sources checked:** a source review (which cites ISO/IEC/IEEE 29148:2018, EARS — Mavin et al., Rolls-Royce 2009, GAMP 5 2nd edition 2022, MoSCoW / DSDM, RICE, WSJF / SAFe, Kano). **Not re-checked against primary sources in this change** — GAMP 5 is marked "next review" in README §10.
- **Next review due:** Planning 2027-05-16; Testing 2027-05-16.

## 2026-11-13 — Targeted review of all phases + current facts

- **Files:** all six phase files, `README.md` (new §10 Standards table), templates `project-brief.md`, `pipeline-checklist.md`, `service-review.md`
- **Scope:** a **targeted** review: (1) add practices from a source review that the guide was missing, (2) re-check time-sensitive facts against current sources. It was not a line-by-line rewrite of every section.
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
- **What changed:** guide created; LumenVenture Standard sections (owners, outputs, gates, rules, templates) added to each phase.
- **Next review due:** Design, Development, Testing, Deployment, Maintenance — 2027-05-10.
