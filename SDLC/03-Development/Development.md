# Phase 3 — Development: "Small Changes, Automated Rules"

**SDLC series — Phase 3 of 6.** How professional backend teams do **Development** today: the core tasks, the Waterfall way vs. the modern way, and the industry practices modern teams add.

> **Last reviewed:** 2026-11-27 · **Next review due:** 2027-05-27 · **Review owner:** Tech Lead · [Review rule](../README.md#91-review-schedule) · [Review log](../CHANGELOG.md)

[← Design](../02-Design/Design.md) · [Guide README](../README.md) · [Testing →](../04-Testing/Testing.md)

---

## 0. Jargon Translation (Read This First)

| Term | Official Definition | Simple Words | Analogy |
|------|--------------------|--------------|---------|
| **SDLC (Software Development Life Cycle)** | A systematic process to build high-quality software in a predictable time and budget. | The steps a team follows from idea to running software. | A recipe for a big meal. |
| **Waterfall** | A model where each phase is fully finished before the next starts, with no going back. | One straight pass: plan everything, then build everything, then test everything. | Water falling down steps. |
| **Agile** | A way of working in short loops that deliver small, working pieces of software and adapt to feedback. | Build a little, show it, learn, repeat. | Cooking one dish at a time and tasting each before the next. |
| **Sprint / Iteration** | A fixed time-box (usually 1–4 weeks) in which a team delivers a small set of features. | One short loop of work. | One lap of a running track. |
| **DevOps** | A culture and set of practices where development and operations work as one team, with heavy automation. | The people who build the software also release and run it. | A chef who also serves the food and hears what guests think. |
| **Definition of Done (DoD)** | A team-wide checklist every item must pass before it counts as finished. | The team's quality rules for "done". | A restaurant's rule: "plate is clean, food is hot, order is correct". |
| **Trunk-based development** | A branching strategy where everyone merges small changes into the main branch at least daily. | Everyone works on one shared line of code, in small steps. | A relay team passing the baton often instead of one runner doing the whole race. |
| **Pull request (PR)** | A request to merge a set of code changes, where teammates review and CI checks them first. | "Please check my change before it goes in." | Handing your essay to a friend to proofread before you submit it. |
| **Code review** | Teammates reading and checking a change for correctness, security and clarity before it is merged. | A second pair of eyes on every change. | A co-pilot checking the pilot's flight plan. |
| **Linter** | A tool that checks code for errors and style problems without running it. | An automatic code checker. | A spell-checker for code. |
| **Conventional Commits** | A standard format for commit messages: `type(scope): summary`. | A fixed pattern for writing commit messages. | A fixed format for writing dates, so everyone reads them the same way. |
| **SemVer (Semantic Versioning)** | A version format `MAJOR.MINOR.PATCH` that tells users if a change is breaking, a new feature, or a fix. | Version numbers that mean something. | A traffic light: red = breaking, yellow = new, green = fix. |
| **Lockfile** | A file (`package-lock.json`) that records the exact version of every installed dependency. | A list that freezes exact package versions. | A recipe that names the exact brand and size of every ingredient. |
| **Parameterized query** | A database query where values are sent separately from the SQL text, so they can never change the query. | The safe way to put user input into SQL. | Filling a form's blanks instead of letting someone rewrite the form. |
| **Supply-chain attack** | An attack that hides malicious code inside a dependency or build tool you trust. | A poisoned package you install without knowing. | A bad ingredient from a supplier that ruins every dish. |
| **SBOM (Software Bill of Materials)** | A complete list of every component and version inside a piece of software. | The ingredient list of your software. | The ingredients label on food packaging. |
| **Event loop** | The single thread in Node.js that runs JavaScript and handles all requests, one task at a time. | Node's one worker that serves everyone. | One very fast waiter serving all tables — if he stops for one table, everyone waits. |
| **Pair programming** | Two developers working together on one task at one computer (or shared screen). | Two people, one keyboard. | A driver and a navigator in a rally car. |
| **Feature flag** | A setting that turns a feature on or off without deploying new code. | A light switch for a feature. | A shop that is built but has its door closed until opening day. |
| **Technical debt** | The future cost of shortcuts taken in code today. | Messy code you must "pay back" later. | Not washing dishes: easy now, harder tomorrow. |
| **CI (Continuous Integration)** | Merging code into the main branch often, with an automated build and tests on every change. | A robot checks every change as soon as you push it. | A spell-checker that runs on every sentence you type. |

---

## 1. The job

- Turn the design into **working, readable, secure, tested code** that the next developer can change easily.
- **Other names:** the **"building"** phase or the **"implementation"** phase.
- **Core tasks (still true in every model):**
  1. Coding starts from a **design** (the design document or the contract for this slice).
  2. **Project planners use the design to determine and assign coding tasks**.
  3. Developers use **programming tools**, **programming languages** and **software stacks**.
  4. Developers follow the organization's **standards and guidelines**.

## 2. Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **Start from a design** | Coding starts only when the **whole** design document is complete | Coding starts when the design for **this slice** is ready (for example the OpenAPI contract is agreed) |
| **Determine and assign tasks** | A project manager assigns all tasks at the start | The **team** splits stories into tasks in **sprint planning**; developers **pull** tasks from a board (Scrum or Kanban) |
| **Tools, languages, stacks** | Chosen once for the whole project | Chosen early, recorded in ADRs; the dev setup is **reproducible** for everyone (`.nvmrc`, dev containers, Docker Compose, `package.json` scripts) |
| **Follow standards and guidelines** | A written style guide that people must remember | Standards **enforced automatically**: ESLint, Prettier, type checks, pre-commit hooks, branch protection, required code review |

## 3. How modern teams do it

- **Trunk-based development:** short-lived branches, merged into `main` within a day or two.
- **Small pull requests (PRs):** easy to review, easy to test, easy to undo. Many teams aim for a few hundred changed lines at most.
- **Required code review:** at least one teammate approves every PR (see [4.3](#43-code-review)).
- **Standards enforced by tools, not memory:**

  | Tool | What it enforces |
  |------|------------------|
  | **ESLint** (v9 uses `eslint.config.js`, the "flat config") | Code rules and common bug patterns |
  | **Prettier** | One code format for everyone |
  | **TypeScript / JSDoc types** | Correct data shapes before the code runs |
  | **Husky + lint-staged** | Run checks before each commit |
  | **Branch protection** | No merge if CI fails or review is missing |
  | **CODEOWNERS** file | The right people are asked to review each part of the code |

- **Secure coding:**
  - **No secrets in code** — use environment variables or a secret manager; commit a `.env.example` with fake values, and add `.env` to `.gitignore`.
  - **Validate all input** at the boundary (for example with `zod` or `express-validator`) — and **reject unknown fields**.
  - **Lock dependencies** with `package-lock.json`; install with `npm ci` in CI.
- **Use an LTS (Long-Term Support) Node.js line that is still supported** (check the release schedule on nodejs.org; pin it in `.nvmrc`, CI and the Dockerfile, and upgrade before it reaches end-of-life) and keep Express up to date (Express 5 passes errors from rejected promises in async handlers to the error middleware automatically).
- **AI coding assistants** (Claude Code, GitHub Copilot): useful for speed, but **the developer stays responsible** (see [4.11](#411-using-ai-coding-assistants-well)).
- **Feature flags:** merge unfinished features safely, hidden behind a flag.

```javascript
// src/routes/reviews.js — validate input at the boundary, errors in one standard format
const express = require('express');
const { z } = require('zod');                         // schema validation library
const reviewService = require('../services/reviewService');

const router = express.Router();

// Schema mirrors the OpenAPI contract from the design phase.
// .strict() REJECTS unknown fields (plain z.object() would silently drop them).
const ReviewInput = z.object({
  rating: z.number().int().min(1).max(5),
  text: z.string().max(2000).optional(),
}).strict();

router.post('/books/:isbn/reviews', async (req, res) => {
  const parsed = ReviewInput.safeParse(req.body);     // never trust client input
  if (!parsed.success) {
    // RFC 9457 Problem Details — the same error shape as every other endpoint
    return res.status(400).type('application/problem+json').json({
      type: 'https://api.example.com/problems/invalid-input',
      title: 'Invalid input',
      status: 400,
      detail: parsed.error.issues.map((i) => `${i.path.join('.')}: ${i.message}`).join('; '),
    });
  }
  // Business rules live in the service layer, not in the route
  const review = await reviewService.addReview(req.user.id, req.params.isbn, parsed.data);
  res.status(201).json(review);
  // In Express 5, if addReview() rejects, the error goes to the error middleware automatically
});

module.exports = router;
```

**What happens if... you hard-code a secret?**

```javascript
// ❌ The password is now in Git history. Deleting the line later does NOT remove it
//    from old commits, forks or clones.
const db = connect('postgres://admin:SuperSecret123@prod-db:5432/app');

// ✅ Read it from the environment; set it in CI/CD or a secret manager
const db2 = connect(process.env.DATABASE_URL);
// If a secret was ever committed: ROTATE it (create a new one, disable the old one) at once.
// Removing it from history is a second step, not a replacement for rotation.
```

## 4. Industry practices beyond the classic tasks

### 4.1 Branching strategies

| Strategy | How it works | Good for | Watch out for |
|----------|--------------|----------|---------------|
| **Trunk-based development** | Everyone merges small changes into `main` at least daily; unfinished work hidden behind feature flags | Teams with good CI and frequent releases — **the common modern default** | Needs strong automated tests |
| **GitHub Flow** | Short feature branch → PR → review → merge to `main` → deploy | Web apps and APIs with continuous delivery | Branches must stay short-lived |
| **GitFlow** | Long-lived `develop` and `main`, plus feature, release and hotfix branches | Software with planned, versioned releases (installed apps, libraries) | Heavy process; painful merges; slow for web services |

![Trunk-based development: short-lived branch, pull request, CI checks and review, then merge](images/sdlc-modern-pr-workflow.svg)

### 4.2 Commits and versioning

- **Small, focused commits** with clear messages. A common standard is **Conventional Commits**: `type(scope): summary`.
- **Semantic Versioning (SemVer)** — `MAJOR.MINOR.PATCH`:
  - **MAJOR:** breaking change (clients must change).
  - **MINOR:** new feature, backward compatible.
  - **PATCH:** bug fix, backward compatible.
- Conventional Commits can **generate the changelog and the next version number automatically** (tools like semantic-release, release-please or Changesets).

```bash
git commit -m "feat(reviews): add rating 1-5 to book reviews (REQ-07)"
git commit -m "fix(reviews): return 409 when user already reviewed the book"
git commit -m "docs(api): document 409 response in openapi.yaml"
# feat = MINOR bump, fix = PATCH bump, "feat!:" or a "BREAKING CHANGE:" footer = MAJOR bump
```

#### 4.2.1 Our versioning policy (details)

Every project writes down its rules in a [versioning policy](templates/versioning-policy.md) in Sprint 0. The defaults:

- **Scheme: SemVer** (semver.org 2.0.0) for services, APIs and packages — **three** parts, `MAJOR.MINOR.PATCH`. What matters is **compatibility**, not size: a small rename is MAJOR; a large new feature that breaks nothing is MINOR. (CalVer — date-based versions such as `2026.11` — is allowed only for products **no other code depends on**, with an ADR.)
- **Optional labels:**
  - **Pre-release** after `-`: `3.0.0-alpha.1` → `-beta.1` → `-rc.1` → `3.0.0`. A pre-release is **lower** than the final version and **never reaches production**. Shared npm packages publish pre-releases with a **dist-tag** (`npm publish --tag beta`), so normal installs do not pick them up.
  - **Build metadata** after `+` (`2.5.0+build.812`) records a build number or date; SemVer **ignores it** when ordering versions. Four-part numbers like `2.5.0.812` are **not** SemVer — do not use them.
- **`0.y.z`** only until the first real client; the first version real clients use is **`1.0.0`**.
- **A released version is never changed.** No re-tagging, no re-publishing, no new image under an old tag — a fix is always a new version.
- **One version everywhere:** the same number appears in `package.json`, the Git tag (`v2.5.0`), `CHANGELOG.md` (for example in the "Keep a Changelog" format), the image tag, the `/version` endpoint and the telemetry attribute `service.version`.
- **Compare versions with a SemVer library** (for example the `semver` package), never as strings: `"1.10.0" > "1.9.0"` is **false** in JavaScript.

![One version, seen everywhere: from commit types to package.json, Git tag, changelog, image tags, /version endpoint and telemetry](images/sdlc-modern-one-version-everywhere.svg)

```js
// src/routes/version.js — every service reports what is running (Express 5)
import { readFile } from "node:fs/promises";
const pkg = JSON.parse(await readFile(new URL("../../package.json", import.meta.url), "utf8"));

export function versionRoute(app) {
  app.get("/version", (req, res) =>
    res.json({
      version: pkg.version,                     // the SemVer release, e.g. "2.5.0"
      commit: process.env.GIT_SHA ?? "unknown", // injected by CI at image build time
      node: process.versions.node,              // runtime version, useful when debugging
    }));
}
```

### 4.3 Code review

- **Purpose:** find bugs, share knowledge, keep the code consistent — **not** to argue about style (tools handle style).
- **What reviewers check:**
  - Does it do what the story and acceptance criteria say?
  - Is it **correct** in edge cases and error cases?
  - Is it **secure** (input validation, authorization, no secrets, safe queries)?
  - Is it **tested**, and are the tests meaningful?
  - Is it **readable**, with good names and simple flow?
  - Does it follow the **design** (layers, API contract, ADRs)?
- **Good review habits:** review within hours, not days; comment on the code, never the person; separate "must fix" from "suggestion" (many teams prefix optional comments with `nit:`).

```markdown
<!-- .github/pull_request_template.md — every PR gets this checklist -->
## What and why
Closes #42 (REQ-07). Adds rating 1–5 to reviews.

## How to test
`npm test` · manual: POST /books/{isbn}/reviews with rating 6 → 400

## Checklist
- [ ] Tests added or updated
- [ ] OpenAPI contract updated
- [ ] No secrets, no console.log left behind
- [ ] Database migration is backward compatible
- [ ] Docs / CHANGELOG updated if needed
```

### 4.4 Code structure and coding principles

- **Layered structure** (from the design): **routes/controllers** (HTTP only) → **services** (business rules) → **repositories** (database only). Each layer can be tested and changed alone.
- **Principles every senior developer is expected to know:**

  | Principle | Meaning |
  |-----------|---------|
  | **KISS** (Keep It Simple, Stupid) | The simplest solution that works is usually the best. |
  | **DRY** (Don't Repeat Yourself) | One rule should live in one place. (But a little duplication is better than the wrong shared abstraction.) |
  | **YAGNI** (You Aren't Gonna Need It) | Do not build features "just in case". |
  | **SOLID** | Five object-oriented design rules; the most used is **Single Responsibility**: one module, one reason to change. |
  | **Boy Scout Rule** | Leave the code a little cleaner than you found it. |

- More examples: Martin Fowler's [refactoring catalog](https://refactoring.com/catalog/) and the [design patterns catalog](https://refactoring.guru/design-patterns) (external).
- **Keep functions small automatically:** turn on lint rules such as ESLint `complexity`, `max-depth` and `max-lines-per-function`, so very complex code fails CI instead of waiting for a reviewer to notice.
- **Keep branching flat and explicit:** use **guard clauses** (early `return` on invalid inputs) instead of deeply nested `if/else` trees, prefer strict equality (`===` / `!==`) over loose `==`, and prevent unintentional `switch` fall-through with `break`/`return` (and `default`), a `Map` (or a lookup object read with `Object.hasOwn`, because a plain object also returns inherited keys such as `constructor`), or ESLint `eqeqeq` and `no-fallthrough`.
- **Use explicit constants, immutability, and the right container:** default to `const` (ESLint `prefer-const`), replace magic numbers/literals with named constants or validated startup config (and freeze or clone shared `const` objects/arrays when mutation would leak across requests), choose `Map` or `Set` over repeated `Array.find()` scans on large in-memory sets, and bound dynamic arrays or use `TypedArray` / streaming for large binary payloads.
- **Prefer small functions, composition, and strict encapsulation:** favor small pure functions and **composition** (passing dependencies via parameters) over deep class inheritance chains, and when a class owns stateful invariants, enforce them with `#private` fields or closures rather than exposing mutable public internals.
- **Ports and adapters** ([Design 4.2](../02-Design/Design.md#42-choose-an-architecture-style)): services receive their repositories and external clients as parameters, so tests can pass in fakes.

```text
src/
├── app.js                  # builds the Express app (no listen) — easy to test
├── server.js               # starts the server: app.listen(...)
├── config.js               # reads and VALIDATES environment variables
├── routes/reviews.js       # HTTP: parse, validate, call service, send response
├── services/reviewService.js   # business rules (one review per user per book)
├── repositories/reviewRepo.js  # SQL only
├── middleware/auth.js      # JWT check
├── middleware/errors.js    # one error handler → Problem Details JSON
└── lib/logger.js           # structured logger
test/
├── unit/
└── integration/
```

### 4.5 Configuration: fail fast at startup

- Follow the **Twelve-Factor App** rule: **config lives in the environment**, not in the code.
- **Validate config when the app starts.** If something is missing, crash **immediately** with a clear message — not hours later on the first request.

```javascript
// src/config.js — validate environment variables once, at startup
const { z } = require('zod');

const Env = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().int().default(3000),       // env vars are strings; coerce to number
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),                    // too-short secrets are rejected
});

const result = Env.safeParse(process.env);
if (!result.success) {
  console.error('Invalid configuration:', result.error.issues.map((i) => i.path.join('.')).join(', '));
  process.exit(1);                                   // fail fast: do not start a broken server
}

module.exports = result.data;
```

**The Twelve-Factor App** (12factor.net) is the standard checklist for a cloud-ready service. Where each factor lives in this guide:

| # | Factor (rule) | In this guide |
|---|---------------|---------------|
| I | **Codebase:** one codebase in Git, many deploys | [4.1 Branching](#41-branching-strategies) |
| II | **Dependencies:** declare and isolate them | Lockfile, rule 5 and [4.8](#48-dependencies-and-supply-chain-security) |
| III | **Config:** store it in the environment | This section |
| IV | **Backing services:** databases and queues are attached resources, swapped by changing config | [Design 4.7](../02-Design/Design.md#47-integrations-and-build-vs-buy) (adapters) |
| V | **Build, release, run:** strictly separate stages | [Deployment](../05-Deployment/Deployment.md) rule 2 (build once, promote) |
| VI | **Processes:** stateless, share nothing | [Design rule 14](../02-Design/Design.md#64-rules) |
| VII | **Port binding:** the app serves HTTP itself on `PORT` | `config.js` above |
| VIII | **Concurrency:** scale out with more processes | [Deployment 4.4](../05-Deployment/Deployment.md#44-autoscaling-and-capacity) |
| IX | **Disposability:** fast start, graceful shutdown | [Deployment 4.2](../05-Deployment/Deployment.md#42-zero-downtime-deploys-graceful-shutdown) |
| X | **Dev/prod parity:** keep environments alike | [4.10](#410-local-development-environment), [4.13](#413-development-environments-and-editor-standards) |
| XI | **Logs:** write events to stdout as a stream; the platform collects them | [4.6](#46-error-handling-and-logging-in-code) |
| XII | **Admin processes:** migrations and one-off tasks run as separate, versioned jobs | [Deployment 4.6](../05-Deployment/Deployment.md#46-rollback-vs-roll-forward) (migrations) |

- The Twelve-Factor text is from 2017 and is still the common baseline. Treat it as a **minimum**, not the full list (it says nothing about security, tracing or containers).
- **Check:** can a new instance start from the image plus environment variables alone, and can any instance be killed at any time without losing data? If not, a factor is broken.

### 4.6 Error handling and logging in code

- **One central error middleware** turns every error into the standard error format. Routes do not build error responses by hand for unexpected errors.
- **Structured logs** (JSON) with a fast logger like **pino**, including a **request ID** so one request can be followed through all logs.
- **Never log secrets or personal data** (passwords, tokens, full card numbers).
- **Never send stack traces to the client** in production.

```javascript
// src/middleware/errors.js — register LAST: app.use(errorHandler)
const logger = require('../lib/logger');

function errorHandler(err, req, res, next) {
  const status = err.status || 500;
  logger.error({ err, reqId: req.id, path: req.originalUrl }, 'request failed'); // full details in logs
  res.status(status).type('application/problem+json').json({
    type: 'about:blank',
    title: status === 500 ? 'Internal Server Error' : err.message, // no internals leak to the client
    status,
  });
}

module.exports = errorHandler;
```

### 4.7 Node.js-specific pitfalls

| Pitfall | What goes wrong | Fix |
|---------|-----------------|-----|
| **Blocking the event loop** | One slow sync task (`fs.readFileSync`, big `JSON.parse`, heavy loop, `bcrypt.hashSync`) freezes **every** request | Use async APIs; move CPU-heavy work to **worker threads** or a queue |
| **Unhandled promise rejections** | Since Node 15, an unhandled rejection **crashes the process** | Always `await` inside `try/catch` or let Express 5 / the error middleware handle it |
| **Forgotten `await`** | Code continues before the database write finishes; errors are lost | ESLint rules such as `no-floating-promises` (typescript-eslint) |
| **Memory leaks** | Caches or listeners that grow forever | Limit cache size (LRU — Least Recently Used), remove listeners, watch memory metrics |
| **No graceful shutdown** | Deploys cut off requests in the middle | On `SIGTERM`, stop accepting new requests, finish current ones, close the database pool, then exit |
| **Missing `trust proxy` behind a reverse proxy** | Express sees the load balancer's internal IP (`req.ip`) and `http` instead of the real client, breaking rate limits and cookies | Set `app.set('trust proxy', N)` to the exact trusted proxy hop count (per `expressjs.com/en/guide/behind-proxies.html`), never `true` blindly |

### 4.8 Dependencies and supply-chain security

- **Choose packages carefully:** first ask whether the platform or a few lines of code can do the job; then check active maintenance, many users, small size, known vulnerabilities, a clear license that your company allows (MIT, Apache-2.0, BSD are usually fine; check **copyleft** licenses like GPL with your legal team), and **how hard it is to replace later** (exit plan, see [Design rule 5](../02-Design/Design.md#64-rules)). Licenses that are **"source available" but not OSI open source** (for example MongoDB's SSPL) can add duties, often when you redistribute the software or offer it as a service to others; the Tech Lead checks the terms with the client's legal contact (a database server is a stack decision: [Design §4.14](../02-Design/Design.md#414-choosing-the-technology-stack)).
- **Fewer dependencies = smaller attack surface.** Do not add a package for a 3-line function.
- **Lockfile + `npm ci`** so every machine installs the **exact** same versions.
- **Version ranges in `package.json`:**

  | Range | Allows | Our default for |
  |-------|--------|-----------------|
  | `^5.1.0` (caret) | Any `5.x.y` from `5.1.0` — never `6.0.0` | Normal runtime dependencies (npm's default) |
  | `~5.1.0` (tilde) | Only `5.1.x` patches | Packages known to break in minor versions |
  | `5.1.0` (exact) | Only this version | Build and release tools where every change must be deliberate |
  | `^0.4.2` (caret on `0.x`) | Only `0.4.x` — `0.y.z` may break anytime | Treat `0.x` packages as risky; prefer stable ones |

  The range says what **may** be installed; the **lockfile** says what **is** installed. Upgrades arrive as pull requests from the update bot and pass CI first.
- **Runtime version:** declare supported Node.js versions in `package.json` → `"engines"` (for example `">=24"`), pin the local version in `.nvmrc`, use the same LTS line in the Docker base image, and run CI on every supported line. A service may also **check `engines` at startup** and exit with a clear message if the runtime is too old.
- **Automated updates and scanning:** Dependabot or Renovate, `npm audit`.
- **Supply-chain attacks are real:** typosquatting (a fake package with a similar name) and hijacked maintainer accounts. Check names carefully; prefer packages with **npm provenance**; be careful with packages that run **install scripts**.
- **SBOM (Software Bill of Materials):** a list of every component in your software (formats **CycloneDX** or **SPDX**; `npm sbom` creates one); required by many enterprise and government customers.
- **Recent attacks show why this matters:** in **2025**, attackers phished npm maintainers and published malware inside very popular packages (for example `chalk` and `debug` in September 2025), and a self-spreading worm ("Shai-Hulud") stole tokens from developer machines and CI. **OWASP Top 10:2025** now lists **Software Supply Chain Failures** as risk **A03**.
- **Publishing a package?** List what ships with the `files` field in `package.json` (an allowlist) and run `npm pack --dry-run` to see the contents before `npm publish`: no `.env`, test data or secrets (see rule 30).
- **Practical defenses:**
  - Install with **`npm ci`**; consider **`--ignore-scripts`** in CI when your dependencies do not need install scripts.
  - **Wait a few days before adopting brand-new versions** (a "cooldown"), **except** for security fixes — many malicious versions are found and removed within days:
    - in npm itself: `min-release-age=7` in the project `.npmrc` (days; available since npm 11.10.0, off by default);
    - in update bots: Renovate `minimumReleaseAge` or Dependabot `cooldown` (Dependabot's default is 3 days and it never delays **security** updates).
  - Use a **supply-chain scanner** (for example Socket, Snyk) that flags new install scripts, network access or obfuscated code in updates.
  - **npm account security changed in late 2025:** npm **revoked all classic tokens on 9 December 2025**; write-enabled granular tokens now last **at most 90 days** and need 2FA by default. For publishing, use **trusted publishing** (OIDC from GitHub Actions or GitLab CI/CD) instead of stored tokens (see [Deployment 4.7](../05-Deployment/Deployment.md#47-release-management)).

### 4.9 Secure coding checklist (code level)

| Risk | Secure code habit |
|------|-------------------|
| **SQL / NoSQL injection** | Always use **parameterized queries** (`$1`, `?`) or a safe **ORM (Object-Relational Mapping)** tool; never build queries with string concatenation |
| **Broken access control** (#1 in the OWASP Top 10:2025) | Check **ownership/permissions on the server** for every request (for example only the author can delete a review) |
| **Mass assignment** | Validate the body with a schema that **rejects unknown fields**; set owner fields (`userId`, `role`, `isApproved`) on the **server**, never from `req.body` |
| **SSRF (Server-Side Request Forgery)** — now part of A01 | Never fetch a URL from user input without an **allow-list**; block internal addresses (for example the cloud metadata IP `169.254.169.254`) |
| **Mishandling exceptional conditions** (new A10 in 2025) | **Fail closed**: if an auth or permission check throws, deny access; one central error handler; never leak stack traces |
| **XSS (Cross-Site Scripting)** | Escape output; set a **Content-Security-Policy**; never put raw user HTML into pages |
| **Weak headers** | Use **helmet** to set secure HTTP headers |
| **Brute force / abuse** | **Rate limiting** on login and write endpoints (**OWASP API4:2023**) |
| **CORS (Cross-Origin Resource Sharing) mistakes** | Allow only known origins; never `*` together with credentials |
| **Passwords** | Hash with **Argon2id** (OWASP's first choice; minimum settings in the OWASP Password Storage Cheat Sheet: 19 MiB memory, 2 iterations, 1 thread). **bcrypt** (work factor ≥ 10) only for existing systems; rehash to Argon2id at the next login. Use async functions |
| **Payment and card data (PCI DSS, Payment Card Industry Data Security Standard, v4.0.1)** | **Never** store raw credit card numbers (**PAN**, Primary Account Number) or **CVV/CVC** (Card Verification Value / Code) in application databases or logs; tokenize via a PCI DSS-certified payment processor and send an `Idempotency-Key` header on charges |
| **Sensitive data in errors and logs** | Generic messages to clients; redact secrets in logs |

```javascript
// ❌ SQL injection: isbn = "1' OR '1'='1" returns every row
db.query(`SELECT * FROM reviews WHERE isbn = '${req.params.isbn}'`);

// ✅ Parameterized query: the driver sends the value separately from the SQL
db.query('SELECT * FROM reviews WHERE isbn = $1', [req.params.isbn]);
```

### 4.10 Local development environment

- **"Works on my machine" must not happen.** Every developer gets the same setup in minutes:
  - `.nvmrc` (Node version), `npm ci`, `.env.example`.
  - **Docker Compose** for the database, cache and other services.
    - Containers reach each other by **service name** (`db`), not `localhost` (inside a container, `localhost` is that container). `depends_on` only waits until a container is **running**, not **ready**: if one service needs another, add a `healthcheck` and `condition: service_healthy`, or retry the connection.
  - **Seed data** and a one-command start (`npm run dev`).
  - Optional **dev containers** for a fully identical editor environment.

```yaml
# compose.yaml — start local dependencies with: docker compose up -d
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app_local_only     # local-only password, never used in production
      POSTGRES_DB: book_reviews
    ports: ["5432:5432"]
  cache:
    image: redis:7
    ports: ["6379:6379"]
```

### 4.11 Using AI coding assistants well

- **Give context:** the story, acceptance criteria, the design and the relevant files.
- **Read every line** of the generated code. Check for invented (non-existent) packages or APIs, missing error handling, and security holes.
- **Tests and review are not optional** for AI code — the same CI, review and security scans apply.
- **Never paste secrets** or confidential customer data into tools your company has not approved.
- Watch for **licensing**: follow your company's policy on AI-generated code.
- Keep AI changes **small**, like any other PR.
- **Check versions in AI suggestions.** AI tools learn from older code, so they often suggest **outdated APIs** or old package versions (for example Express 4 patterns in an Express 5 project). Check the version you actually use and its official docs.
- **Check every new package an AI suggests.** AI tools sometimes invent package names that do not exist, and attackers register those names with malware ("slopsquatting"). Confirm the package exists, is popular and is maintained **before** installing it.
- **AI agents that run commands** (in your editor or CI) get the **least privilege** they need: no production credentials, no access to secrets they do not need, and every change still goes through a PR.
- **If your product itself uses an LLM (Large Language Model)**, also follow the **OWASP Top 10 for LLM Applications (2026 edition; the 2025 edition is the previous one)** — for example **prompt injection**: never let model output decide permissions or run commands without checks.

### 4.12 Collaboration and documentation

- **Pair programming** (two developers, one task) and **mob/ensemble programming** (the whole team, one task) spread knowledge and catch mistakes early. In a pair, the **driver** types and thinks about the small goal; the **navigator** reviews and keeps the bigger picture; **swap roles often** and do not pair all day (Fowler suggests about 6 hours a day as a ceiling, with breaks). Good for onboarding and hard problems; for large unknowns do a short **spike** first.
  - **Three common styles:** **driver/navigator** (the default; swap on a timer, about every 15–30 minutes), **ping-pong** (one person writes a failing test, the other makes it pass; good for TDD (test-driven development)), **strong-style** (an idea must go through the other person's hands; the expert navigates, the learner types; teams often add a short recap with questions afterwards). Use a **spike** first for big unknowns.
  - **Remote pairing** works well with a shared editor or screen, a headset and a timer; agree who drives first, the swap time and the breaks.
  - **Credit both people:** add a `Co-authored-by: Name <email>` trailer (after a blank line) to the commit message. **Pairing is an extra review layer, not a replacement for the pull request** (rule 28; the second author's trailer is rule 27).
- **Docs as code:** a **README** (what it is, how to run it, how to test it), API docs generated from OpenAPI, JSDoc on public functions, ADRs, and a **CHANGELOG** — all in Git and reviewed in PRs.
- **Comments explain *why*, not *what*.** The code shows *what*.
- **Docs change in the same PR as the code.** Documentation is updated **with** each change, in every phase — not "later" or "in the maintenance phase". If users read the old docs for weeks, the docs are wrong ([README §7.2](../README.md#72-documentation-rules), rule 2).
- **Product vs. process docs:** product docs describe the software (requirements, design, technical, QA, user); process docs describe how we work (plans, standards, reports, **SOPs**). Working papers and meeting notes are **process** docs — move any decision in them into an ADR. The full map with owners is in [README §7.1](../README.md#71-documentation-map-what-we-keep-who-owns-it-when-it-changes).
- **SOPs (Standard Operating Procedures)** describe a repeated, project-specific procedure step by step — for example **how we merge to `main`** ([SOP template with this filled example](templates/sop.md)). Put every step a tool can check **into the tool** (branch protection, `CODEOWNERS`, the PR template, CI); the SOP keeps the reasons and the human steps.
- **Generate and check docs:** the API reference comes from OpenAPI; CI should run Markdown lint, a link check and an OpenAPI lint on every PR ([README §7.2](../README.md#72-documentation-rules), rule 5). Pin the tools in `devDependencies` and run them as npm scripts, so CI uses the lockfile versions (rule 5).

```yaml
# .github/workflows/docs.yml (excerpt) — docs are checked like code
on:
  pull_request:
    paths: ["**/*.md", "openapi.yaml"]
# ... checkout and setup-node ...
      - run: npm ci                                            # tools pinned in devDependencies
      - run: npx --no-install markdownlint-cli2 "**/*.md" "#node_modules"   # Markdown format rules
      - run: npx --no-install @redocly/cli lint openapi.yaml   # the API contract is valid
      - uses: lycheeverse/lychee-action@<pinned version or SHA> # broken-link check
# Not a required status check: with a paths filter, PRs without docs changes never run it.
```

### 4.13 Development environments and editor standards

- **Consistent editor configuration (`.editorconfig`):** every project must include an `.editorconfig` file in the repository root. This ensures that regardless of whether a developer uses VS Code, Neovim, WebStorm, or Sublime Text, basic formatting rules remain consistent across macOS, Linux, and Windows:
  - UTF-8 character encoding without byte-order marks (`charset = utf-8`);
  - Consistent indentation style and size (e.g. 2 spaces, no tabs);
  - Unix-style line endings (`end_of_line = lf`);
  - Trailing whitespace trimmed automatically on save (`trim_trailing_whitespace = true`);
  - Newline inserted at the end of every file (`insert_final_newline = true`).
- **Reproducible containerized environments (DevContainers):** teams should consider providing a `.devcontainer/devcontainer.json` configuration for complex services. DevContainers package the required Node.js LTS version, system libraries, database clients, and recommended editor extensions into a Docker container, eliminating machine-specific configuration drift.
- **Retire unmaintained legacy editors:** developers must use actively maintained editors supporting the Language Server Protocol (LSP) and modern security tooling. Legacy tools like Atom (officially sunset on December 15, 2022) must not be used on company projects due to unpatched security vulnerabilities.

### 4.14 Front-end code standards

> Design decisions for web UIs are in [Design 4.13](../02-Design/Design.md#413-front-end-design-decisions).

| Habit | What to do | Why |
|-------|-----------|-----|
| **Native elements first** | `button` for actions, `a href` for navigation, `label` + `input` for forms, landmarks (`header`, `nav`, `main`, `footer`). No clickable `div` | Keyboard and screen-reader users get it for free; custom widgets need a lot of extra code |
| **Accessibility checks while coding** | Accessibility lint rules in the editor and CI, plus a keyboard-only test of every changed screen | Automated tools find only part of the problems |
| **TypeScript** | New front-end code is TypeScript | Catches many mistakes before the browser runs the code |
| **One styling approach** | Plain CSS (custom properties, nesting), CSS Modules, utility CSS or Sass. Lint with Stylelint | A mix of systems is hard to maintain |
| **Sass: `@use`, not `@import`** | `@import` is deprecated since Dart Sass 1.80.0 and will be removed in 3.0.0 | The old rule makes every name global and loads the same file many times |
| **Mobile-first CSS** | Base styles for small screens, then `min-width` media or container queries. `<meta name="viewport" content="width=device-width">`; never block zoom | Phones are a large part of traffic; without the tag phones show a shrunk desktop page |
| **API calls** | Check `res.ok` (`fetch` does not throw on 404 or 500), set a timeout, show loading, empty and error states | The most common front-end bug is using an error body as if it were data |
| **The browser is untrusted** | No secrets in the bundle. The server validates and authorizes every request. Never insert untrusted data as HTML (`innerHTML`, `dangerouslySetInnerHTML`, `v-html`); use `textContent` or the framework's escaping | Users can read and change everything in the browser |
| **Cookies and tokens** | Session cookies: `HttpOnly` (JavaScript cannot read it), `Secure` (HTTPS only) and `SameSite` (`Lax` by default; `None` needs `Secure`). Avoid long-lived tokens in `localStorage`. `SameSite` does not stop all CSRF: add a CSRF token or `Origin` check | An XSS bug can steal anything JavaScript can read |
| **Third-party scripts** | Each one runs with your page's rights: approve it, load as few as possible, and add **SRI** to CDN files | A hacked third party becomes your breach |
| **Build tool (front end)** | Use a maintained build tool run through `npm run build` in CI, for example Vite, esbuild or Rollup (Webpack in older projects); the choice is recorded in an ADR ([Design rule 5](../02-Design/Design.md#64-rules)). **Inject environment settings at runtime** (or per environment), never bake secrets into the bundle (rule 21) | Reproducible builds; the same artifact moves to every environment ([Deployment rule 2](../05-Deployment/Deployment.md#64-rules)) |
| **Bundle size** | Code splitting, lazy loading, a size budget in CI | JavaScript must be downloaded, parsed and run; too much of it slows the page |

```html
<!-- SRI: the browser refuses the file if its hash does not match -->
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-<hash>" crossorigin="anonymous"></script>
```

```http
Set-Cookie: sid=<value>; Secure; HttpOnly; SameSite=Lax; Path=/
```

- **Checklist for every UI change and release:** [frontend-checklist.md](templates/frontend-checklist.md).
- Server-side counterparts (CORS, rate limiting, validation) are in [4.9](#49-secure-coding-checklist-code-level).

### 4.15 Database access, ORMs, and migrations

> Using an **ORM (Object-Relational Mapping)** tool speeds up CRUD (Create, Read, Update, Delete) code, but does not remove the need to understand SQL and database performance.

- **Use connection pooling:** Reuse a bounded pool of open database connections instead of opening a new connection on every HTTP request.
- **Prevent N+1 query loops:** Never load a list of `N` records in one query and then run `N` separate queries inside a loop to fetch related rows. Inspect generated SQL logs in development and use **eager loading** (loading related rows upfront in one query instead of inside a loop) or an explicit SQL `JOIN`.
- **Keep SQL fundamentals sharp:** Use typed ORMs or query builders (for example Prisma, Drizzle ORM, SQLAlchemy, or Django ORM) for standard queries and bound parameters, and drop to parameterized raw SQL when complex reports or tuned indexes need it.
- **Inspect query plans and set timeouts:** Check slow `SELECT` queries with `EXPLAIN` (and add indexes before shipping), and enforce query timeouts (for example `statement_timeout` in PostgreSQL; in MySQL `max_execution_time` limits read-only `SELECT` statements only, so also use client-side or driver timeouts) so one slow query cannot exhaust the connection pool.
- **Bound every list and search:** Enforce pagination (`limit` and cursor/offset) on search and list endpoints, and back search filters with proper indexes (such as PostgreSQL full-text indexes and `jsonb` GIN, Generalized Inverted Index, indexes) instead of unindexed `LIKE '%term%'` scans on large tables.
- **Separate runtime and migration DB (Database) roles:** Run the application with a least-privilege DB role (`SELECT`, `INSERT`, `UPDATE`, `DELETE` plus schema/sequence `USAGE` where needed — never `DROP` or `GRANT`), and reserve DDL (Data Definition Language: `CREATE`, `ALTER`, `DROP`) on shared and production databases for the pipeline's migration step.
- **Track every schema change with versioned migrations:** Store database schema changes as reviewed migration files in Git, keep them backward-compatible during rolling deploys (add new columns before dropping old ones), and run migrations as a controlled pipeline step before or alongside app rollout.

## 5. Development is "done" when... (a typical Definition of Done)

- [ ] The code meets the story's **acceptance criteria** and follows the **design** (API contract, layers, ADRs).
- [ ] **Unit and integration tests** are written and pass in CI.
- [ ] **Lint, format and type checks** pass.
- [ ] **Security checks** pass: input validated, authorization checked, no secrets, parameterized queries, dependency scan clean.
- [ ] Errors go through the **central error handler**; logs are structured with no sensitive data.
- [ ] **User-facing changes** pass the front-end checks (§4.14): native elements, keyboard test, works at 320 px and on desktop, accessibility check passes.
- [ ] The **PR is small**, has a clear description, and is **approved** by at least one reviewer.
- [ ] **Docs** (README, OpenAPI, user help, runbooks, SOPs, CHANGELOG) are updated **in the same PR** (help-center content: in the same release) — or the PR says "no docs change".
- [ ] Database **migrations** are backward compatible.
- [ ] Unfinished user-facing work is hidden behind a **feature flag**.
- [ ] The change is **merged to `main`** and deployable.

---

## 6. LumenVenture Standard

> **What we do on every project.** See the [guide README](../README.md) for roles, gates and project types. **must** = required · **should** = default (skip only with a written reason) · **may** = optional.

### 6.1 Owners

| Activity | Accountable | Responsible | Consulted |
|----------|-------------|-------------|-----------|
| Repository setup and standards | Tech Lead | Tech Lead | Developers |
| Writing code and tests | Tech Lead | Developers | QA |
| Code review | Tech Lead | Developers (not the author) | Security Champion (security-relevant changes) |
| Dependency choices | Tech Lead | Developers | Security Champion |

### 6.2 Required outputs

| Output | Internal | Client | Prototype | + Regulated |
|--------|----------|--------|-----------|-------------|
| Repository + walking skeleton ([checklist](templates/repo-setup-checklist.md)) | **must** | **must** | **should** (repo, CI) | **must** |
| PR template in `.github/` ([template](templates/pull_request_template.md)) | **must** | **must** | **should** | **must** |
| Team Definition of Done ([template](templates/definition-of-done.md)) | **must** | **must** | **may** | **must** |
| README (run, test, deploy) | **must** | **must** | **must** | **must** |
| CHANGELOG + SemVer releases | **should** | **must** | — | **must** |
| Versioning policy ([template](templates/versioning-policy.md)) | **must** | **must** | — | **must** |
| SBOM per release | **may** | **should** | — | **must** |
| SOPs for repeated project-specific procedures ([template](templates/sop.md)) — at least "merge to `main`" (the release checklist is the release SOP) | **should** | **must** | — | **must** |
| Docs checks in CI (Markdown lint, links, OpenAPI lint) | **should** | **should** | — | **must** |

### 6.3 Gate G3 — Story done

**When:** every story / pull request. **Who decides:** the reviewer approves the PR; the Product Owner accepts the story.

- [ ] All ★ items of the [Definition of Done](templates/definition-of-done.md) are true
- [ ] CI is green: lint, types, tests, dependency/secret/SAST scans
- [ ] At least **one approval** from someone other than the author
- [ ] Merged to `main` and deployed to staging by the pipeline
- [ ] Product Owner accepted the story against its acceptance criteria

### 6.4 Rules

> Documentation rules for all phases (same PR, SOPs, docs checks, review dates) are in [README §7.2](../README.md#72-documentation-rules).


1. **must** — `main` is protected: PR, ≥ 1 approval, green CI; no direct pushes, no force-push.
2. **must** — **Trunk-based** or **GitHub Flow**: branches live ≤ 2 days where possible; unfinished work hides behind feature flags. (GitFlow only with an ADR, for example for versioned libraries.)
3. **must** — **No secrets** in code, config files, images or logs. A leaked secret is **rotated at once**.
4. **must** — All input is validated at the boundary with a schema that **rejects unknown fields** (no mass assignment); database access uses **parameterized queries** or a safe ORM.
5. **must** — Dependencies are installed from the **lockfile**; new dependencies need a check of maintenance, license and security.
6. **must** — AI-assisted code is **read, understood, tested and reviewed** like any other code; no confidential data in unapproved AI tools.
7. **should** — PRs stay small (aim for a few hundred changed lines at most) and focused on one concern.
8. **should** — Commits follow **Conventional Commits**; releases follow the project's **versioning policy** (SemVer by default, §4.2.1).
9. **should** — Reviews start within **one working day**.
10. **should** — Config is validated at startup; errors go through one central handler; logs are structured with request IDs.
11. **may** — Pair or mob programming for complex or risky work and for onboarding.
12. **should** — Lint rules limit **complexity** (for example `complexity`, `max-depth`, `max-lines-per-function`), checked in CI.
13. **should** — Dependency updates wait a short **cooldown** (for example 3–7 days) before they are merged, **except security fixes**; new packages suggested by AI are checked to exist and be trusted before install.
14. **must** — Every deployable service reports its **version and commit SHA** (a `/version` or health endpoint) and sets **`service.version`** in its logs and telemetry.
15. **must** — A released version is **never changed or re-published**; tags and published packages are immutable, and a fix is always a new version.
16. **should** — `package.json` declares `"engines"`; `.nvmrc`, the Docker base image and the CI matrix use the same supported **LTS** Node.js line(s).
17. **should** — Code compares versions with a **SemVer library**, never with string comparison.
18. **must** — A new instance starts from the **image plus environment variables only**: no local files, no manual steps, no state kept in the process (Twelve-Factor III, VI, IX; table in §4.5).
19. **should** — When a bug is hard to place, check the **four boundaries** in order (client, edge and network, application, persistence) before changing code ([Maintenance 4.4.1](../06-Maintenance/Maintenance.md#441-where-is-it-broken-triage-by-boundary)).
20. **must** — Interactive elements use **native HTML elements** (`button`, `a href`, `label` with `input`); a clickable `div` fails code review.
21. **must** — The browser is **untrusted**: no secrets in front-end code or bundles; untrusted data is never inserted as HTML; the server validates and authorizes every request (§4.14).
22. **must** — Session cookies are `HttpOnly`, `Secure` and `SameSite` (`Lax` unless an ADR says otherwise). `SameSite=Lax` is **not a full CSRF (Cross-Site Request Forgery) defence**: state-changing requests that use cookie sessions also need a CSRF token or an `Origin` header check.
23. **should** — Every API call checks for HTTP errors, has a timeout, and the UI shows loading, empty and error states.
24. **should** — New front-end code is **TypeScript** (or JavaScript with JSDoc types checked in CI); a project uses **one** styling approach; Sass code uses `@use`, not `@import`.
25. **should** — Third-party scripts are approved by the Tech Lead or listed in the project's dependency list, and scripts and stylesheets loaded from a CDN use **SRI** (Subresource Integrity: `integrity` + `crossorigin`).
26. **should** — Database access uses **connection pooling**, query timeouts, **least-privilege runtime roles** (no `DROP` or `GRANT` in app credentials), and **versioned schema migrations**; developers check slow queries with `EXPLAIN` and inspect generated ORM queries in development to prevent `N+1` query loops (§4.15). Owner: Tech Lead.
27. **should** — A commit made by a pair carries a `Co-authored-by: Name <email>` trailer for the second person (the first is the commit author), so both are credited in Git history. Use the email linked to the person's GitHub account, or their GitHub no-reply address.
28. **must** (restates rule 1 for pairs) — **Pairing never replaces review:** every pull request is approved by someone **outside the pair**, as rule 1 and gate G3 already require. Pairing is an extra layer and a good way to onboard. On a team too small to have an outsider (a prototype), the Tech Lead or another LumenVenture developer reviews; write that arrangement in the project brief §10.
29. **should** (**must** on client and regulated projects) — CI runs `git diff --check origin/main...HEAD` (with full-depth checkout) so that leftover **conflict markers** (`<<<<<<<`) fail the build; whitespace warnings follow the repository's `core.whitespace` / `.gitattributes` settings (Markdown line breaks, lockfiles and generated files are excluded). A pre-commit hook may run `git diff --cached --check` as an early warning, but CI is the enforcement. Conflicts are resolved by a developer who has **read both sides**.
30. **should** (**must** for packages published outside the company) — A published package (npm or an internal registry) has a `files` allowlist (never `files: ["."]` or a broad glob; `.npmignore` only as a fallback). The release job runs `npm pack --dry-run --json` and **fails** if forbidden paths appear (`.env`, `*.pem`, `test/`, `.git*`). Owner: Tech Lead. This applies to packages that are **published**, not to services that are only deployed. Publishing itself follows [Deployment rule 12](../05-Deployment/Deployment.md#64-rules).

### 6.5 Templates

| Template | Copy to |
|----------|---------|
| [repo-setup-checklist.md](templates/repo-setup-checklist.md) | Use once at project start (track as a Sprint 0 story) |
| [pull_request_template.md](templates/pull_request_template.md) | `.github/pull_request_template.md` |
| [definition-of-done.md](templates/definition-of-done.md) | `docs/definition-of-done.md` |
| [versioning-policy.md](templates/versioning-policy.md) | `docs/versioning-policy.md` (Sprint 0) |
| [sop.md](templates/sop.md) | `docs/sop/<short-name>.md` (filled example: merging to `main`) |
| [frontend-checklist.md](templates/frontend-checklist.md) | Web UIs: use at project start and before each release |

---

[← Design](../02-Design/Design.md) · [Guide README](../README.md) · [Testing →](../04-Testing/Testing.md)
