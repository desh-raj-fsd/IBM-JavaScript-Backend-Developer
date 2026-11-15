# Phase 3 — Development: "Small Changes, Automated Rules"

**SDLC series — Phase 3 of 6.** How professional backend teams do **Development** today: the lecture's core tasks, the Waterfall way vs. the modern way, and the industry practices the lecture does not cover.

> **Last reviewed:** 2026-11-13 · **Next review due:** 2027-05-13 · **Review owner:** Tech Lead · [Review rule](../README.md#91-review-schedule) · [Review log](../CHANGELOG.md)

[← Design](../02-Design/Design.md) · [Guide README](../README.md) · [Overview](../../6-Phases-of-SDLC-Modern-Best-Practices.md) · [Testing →](../04-Testing/Testing.md)

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
- **Core tasks from the lecture (still true in every model):**
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

## 4. Industry practices the lecture does not cover

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
- Conventional Commits can **generate the changelog and the next version number automatically** (tools like semantic-release or release-please).

```bash
git commit -m "feat(reviews): add rating 1-5 to book reviews (REQ-07)"
git commit -m "fix(reviews): return 409 when user already reviewed the book"
git commit -m "docs(api): document 409 response in openapi.yaml"
# feat = MINOR bump, fix = PATCH bump, "BREAKING CHANGE:" in the body = MAJOR bump
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

- More rules with examples: [7 Coding Laws of Senior Developer](../../7-Coding-Laws-of-Senior-Developer.md) and [10 Backend Design Patterns](../../10-Backend-Design-Pattern-Laws-of-Senior-Engineers-and-Architects.md).
- **Keep functions small automatically:** turn on lint rules such as ESLint `complexity`, `max-depth` and `max-lines-per-function`, so very complex code fails CI instead of waiting for a reviewer to notice.
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

### 4.8 Dependencies and supply-chain security

- **Choose packages carefully:** active maintenance, many users, small size, a clear license that your company allows (MIT, Apache-2.0, BSD are usually fine; check **copyleft** licenses like GPL with your legal team).
- **Fewer dependencies = smaller attack surface.** Do not add a package for a 3-line function.
- **Lockfile + `npm ci`** so every machine installs the **exact** same versions.
- **Automated updates and scanning:** Dependabot or Renovate, `npm audit`.
- **Supply-chain attacks are real:** typosquatting (a fake package with a similar name) and hijacked maintainer accounts. Check names carefully; prefer packages with **npm provenance**; be careful with packages that run **install scripts**.
- **SBOM (Software Bill of Materials):** a list of every component in your software (formats **CycloneDX** or **SPDX**; `npm sbom` creates one); required by many enterprise and government customers.
- **Recent attacks show why this matters:** in **2025**, attackers phished npm maintainers and published malware inside very popular packages (for example `chalk` and `debug` in September 2025), and a self-spreading worm ("Shai-Hulud") stole tokens from developer machines and CI. **OWASP Top 10:2025** now lists **Software Supply Chain Failures** as risk **A03**.
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
| **SQL / NoSQL injection** | Always use **parameterized queries** (`$1`, `?`) or a safe ORM; never build queries with string concatenation |
| **Broken access control** (#1 in the OWASP Top 10:2025) | Check **ownership/permissions on the server** for every request (for example only the author can delete a review) |
| **Mass assignment** | Validate the body with a schema that **rejects unknown fields**; set owner fields (`userId`, `role`, `isApproved`) on the **server**, never from `req.body` |
| **SSRF (Server-Side Request Forgery)** — now part of A01 | Never fetch a URL from user input without an **allow-list**; block internal addresses (for example the cloud metadata IP `169.254.169.254`) |
| **Mishandling exceptional conditions** (new A10 in 2025) | **Fail closed**: if an auth or permission check throws, deny access; one central error handler; never leak stack traces |
| **XSS (Cross-Site Scripting)** | Escape output; set a **Content-Security-Policy**; never put raw user HTML into pages |
| **Weak headers** | Use **helmet** to set secure HTTP headers |
| **Brute force / abuse** | **Rate limiting** on login and write endpoints |
| **CORS (Cross-Origin Resource Sharing) mistakes** | Allow only known origins; never `*` together with credentials |
| **Passwords** | Hash with **Argon2id** (OWASP's first choice; minimum settings in the OWASP Password Storage Cheat Sheet: 19 MiB memory, 2 iterations, 1 thread). **bcrypt** (work factor ≥ 10) only for existing systems; rehash to Argon2id at the next login. Use async functions |
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
- **Check every new package an AI suggests.** AI tools sometimes invent package names that do not exist, and attackers register those names with malware ("slopsquatting"). Confirm the package exists, is popular and is maintained **before** installing it.
- **AI agents that run commands** (in your editor or CI) get the **least privilege** they need: no production credentials, no access to secrets they do not need, and every change still goes through a PR.
- **If your product itself uses an LLM (Large Language Model)**, also follow the **OWASP Top 10 for LLM Applications (2025)** — for example **prompt injection**: never let model output decide permissions or run commands without checks.

### 4.12 Collaboration and documentation

- **Pair programming** (two developers, one task) and **mob/ensemble programming** (the whole team, one task) spread knowledge and catch mistakes early.
- **Docs as code:** a **README** (what it is, how to run it, how to test it), API docs generated from OpenAPI, JSDoc on public functions, ADRs, and a **CHANGELOG** — all in Git and reviewed in PRs.
- **Comments explain *why*, not *what*.** The code shows *what*.

## 5. Development is "done" when... (a typical Definition of Done)

- [ ] The code meets the story's **acceptance criteria** and follows the **design** (API contract, layers, ADRs).
- [ ] **Unit and integration tests** are written and pass in CI.
- [ ] **Lint, format and type checks** pass.
- [ ] **Security checks** pass: input validated, authorization checked, no secrets, parameterized queries, dependency scan clean.
- [ ] Errors go through the **central error handler**; logs are structured with no sensitive data.
- [ ] The **PR is small**, has a clear description, and is **approved** by at least one reviewer.
- [ ] **Docs** (README, OpenAPI, CHANGELOG) are updated where needed.
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
| SBOM per release | **may** | **should** | — | **must** |

### 6.3 Gate G3 — Story done

**When:** every story / pull request. **Who decides:** the reviewer approves the PR; the Product Owner accepts the story.

- [ ] All ★ items of the [Definition of Done](templates/definition-of-done.md) are true
- [ ] CI is green: lint, types, tests, dependency/secret/SAST scans
- [ ] At least **one approval** from someone other than the author
- [ ] Merged to `main` and deployed to staging by the pipeline
- [ ] Product Owner accepted the story against its acceptance criteria

### 6.4 Rules

1. **must** — `main` is protected: PR, ≥ 1 approval, green CI; no direct pushes, no force-push.
2. **must** — **Trunk-based** or **GitHub Flow**: branches live ≤ 2 days where possible; unfinished work hides behind feature flags. (GitFlow only with an ADR, for example for versioned libraries.)
3. **must** — **No secrets** in code, config files, images or logs. A leaked secret is **rotated at once**.
4. **must** — All input is validated at the boundary with a schema that **rejects unknown fields** (no mass assignment); database access uses **parameterized queries** or a safe ORM.
5. **must** — Dependencies are installed from the **lockfile**; new dependencies need a check of maintenance, license and security.
6. **must** — AI-assisted code is **read, understood, tested and reviewed** like any other code; no confidential data in unapproved AI tools.
7. **should** — PRs stay small (aim for a few hundred changed lines at most) and focused on one concern.
8. **should** — Commits follow **Conventional Commits**; releases use **SemVer**.
9. **should** — Reviews start within **one working day**.
10. **should** — Config is validated at startup; errors go through one central handler; logs are structured with request IDs.
11. **may** — Pair or mob programming for complex or risky work and for onboarding.
12. **should** — Lint rules limit **complexity** (for example `complexity`, `max-depth`, `max-lines-per-function`), checked in CI.
13. **should** — Dependency updates wait a short **cooldown** (for example 3–7 days) before they are merged, **except security fixes**; new packages suggested by AI are checked to exist and be trusted before install.

### 6.5 Templates

| Template | Copy to |
|----------|---------|
| [repo-setup-checklist.md](templates/repo-setup-checklist.md) | Use once at project start (track as a Sprint 0 story) |
| [pull_request_template.md](templates/pull_request_template.md) | `.github/pull_request_template.md` |
| [definition-of-done.md](templates/definition-of-done.md) | `docs/definition-of-done.md` |

---

[← Design](../02-Design/Design.md) · [Guide README](../README.md) · [Overview](../../6-Phases-of-SDLC-Modern-Best-Practices.md) · [Testing →](../04-Testing/Testing.md)
