# Phase 4 — Testing: "Shift-Left, Automate, Pyramid"

**SDLC series — Phase 4 of 6.** How professional backend teams do **Testing** today: the lecture's core tasks, the Waterfall way vs. the modern way, and the industry practices the lecture does not cover.

> **Last reviewed:** 2026-11-13 · **Next review due:** 2027-05-13 · **Review owner:** QA Engineer · [Review rule](../README.md#91-review-schedule) · [Review log](../CHANGELOG.md)

[← Development](../03-Development/Development.md) · [Guide README](../README.md) · [Overview](../../6-Phases-of-SDLC-Modern-Best-Practices.md) · [Deployment →](../05-Deployment/Deployment.md)

---

## 0. Jargon Translation (Read This First)

| Term | Official Definition | Simple Words | Analogy |
|------|--------------------|--------------|---------|
| **SDLC (Software Development Life Cycle)** | A systematic process to build high-quality software in a predictable time and budget. | The steps a team follows from idea to running software. | A recipe for a big meal. |
| **Waterfall** | A model where each phase is fully finished before the next starts, with no going back. | One straight pass: plan everything, then build everything, then test everything. | Water falling down steps. |
| **Agile** | A way of working in short loops that deliver small, working pieces of software and adapt to feedback. | Build a little, show it, learn, repeat. | Cooking one dish at a time and tasting each before the next. |
| **Sprint / Iteration** | A fixed time-box (usually 1–4 weeks) in which a team delivers a small set of features. | One short loop of work. | One lap of a running track. |
| **DevOps** | A culture and set of practices where development and operations work as one team, with heavy automation. | The people who build the software also release and run it. | A chef who also serves the food and hears what guests think. |
| **Shift-left** | Moving testing and security work earlier in the timeline. | Test early, not at the end. | Checking ingredients before cooking, not after serving. |
| **TDD (Test-Driven Development)** | Writing a failing test first, then the code that makes it pass, then cleaning up. | Write the exam question before the answer. | Drawing the target before shooting the arrow. |
| **CI (Continuous Integration)** | Merging code into the main branch often, with an automated build and tests on every change. | A robot checks every change as soon as you push it. | A spell-checker that runs on every sentence you type. |
| **Acceptance criteria** | Clear yes/no conditions a story must meet to be accepted. | The checklist that says "this story is done". | "Tap does not leak; hot and cold both work". |
| **Gherkin** | A plain-language format (Given / When / Then) for writing acceptance criteria that tools can run as tests. | Test steps written like simple sentences. | A recipe card: "Given flour, when you add water, then you get dough." |
| **Verification vs. validation** | Verification: "did we build it right?" (against the spec). Validation: "did we build the right thing?" (against real needs). | Right *way* vs. right *thing*. | Following the recipe exactly vs. the guests actually liking the dish. |
| **Black-box / white-box testing** | Testing without looking at the code (black-box) vs. using knowledge of the code's internals (white-box). | Test from outside vs. from inside. | Test-driving a car vs. inspecting the engine. |
| **Regression test** | A test that checks old features still work after a change. | "Did we break anything that used to work?" | Re-checking all the lights after fixing one switch. |
| **Smoke test** | A quick, basic test that the build starts and the most important features work. | "Does it even turn on?" | Turning on a new appliance to see that it powers up, before testing every button. |
| **Exploratory testing** | Unscripted testing where a tester learns the app and designs tests while using it. | Testing by curious exploring. | A detective looking for clues, not following a checklist. |
| **Load test** | A test that measures speed and errors under expected (or higher) traffic. | "Is it fast enough when many people use it?" | Testing a bridge with many trucks at once. |
| **Test double (mock, stub, fake, spy)** | A replacement for a real dependency, used in a test. | A stand-in for the real thing. | A crash-test dummy instead of a real driver. |
| **Code coverage** | The share of code lines or branches that the tests run. | How much of the code the tests touch. | How many rooms of a house the inspector walked into. |
| **Mutation testing** | Making small deliberate changes to code to check that the tests notice. | Testing the tests. | A teacher adding a wrong answer to see if the student spots it. |
| **Flaky test** | A test that sometimes passes and sometimes fails with no code change. | An unreliable test. | A smoke alarm that goes off at random. |
| **Severity vs. priority** | Severity = technical impact of a bug; priority = how urgently to fix it. | How bad vs. how urgent. | A small stain on a wedding dress: low damage, but very urgent. |
| **Chaos engineering** | Deliberately injecting failures to prove a system can recover. | Breaking things on purpose, safely. | A fire drill. |

---

## 1. The job

- Prove the software is **stable**, **secure**, and **meets the requirements** — and find problems as **early and cheaply** as possible.
- **Core tasks from the lecture (still true in every model):**
  1. Code is **thoroughly tested**: **stable**, **secure**, and **meets the requirements** (the SRS or the acceptance criteria).
  2. Testing is **manual**, **automated**, or a **hybrid** of both.
  3. Large projects may have **dedicated testing (QA — Quality Assurance) teams**.
  4. **The bug cycle:** bugs are **reported**, **tracked**, **fixed**, and the code is **retested** until it is stable.
  5. Testing happens at several **levels**: **unit**, **integration**, **system**, **acceptance**.
- **Two questions testing must answer** (a classic interview topic):

  | | **Verification** | **Validation** |
  |---|---|---|
  | **Question** | "Did we build the product **right**?" | "Did we build the **right** product?" |
  | **Checks against** | The specification / design / acceptance criteria | The real needs of users and stakeholders |
  | **Examples** | Code review, unit and integration tests, contract tests | Acceptance testing / UAT, usability tests, beta testing |

## 2. Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **When testing happens** | After all coding is complete | **During** coding (shift-left), on **every push** in CI, and some checks **in production** (shift-right) |
| **Manual / automated / hybrid** | Mostly manual test scripts | **Hybrid, mostly automated**: automated tests for every rule; manual **exploratory testing** for usability and unexpected cases |
| **Who tests** | A separate QA team at the end | **Developers** write unit and integration tests; **QA engineers** work inside the team: test strategy, end-to-end automation, exploratory testing. Quality is the **whole team's** job |
| **Report → track → fix → retest** | Bug reports in a spreadsheet or tool, fixed in a later round | Bugs tracked in Jira / GitHub Issues with **severity and priority**; each fix comes with a **regression test**; CI **retests everything automatically** |
| **Testing levels** | Run one after another, each as its own stage | **All levels run in the pipeline**, in pyramid proportions; acceptance criteria are often automated |

## 3. How modern teams do it

- **Shift-left testing:** testing starts **while** coding, not after.
- **TDD (Test-Driven Development)** cycle:
  1. **Red** — write a test; it fails.
  2. **Green** — write the smallest code that passes.
  3. **Refactor** — clean up; the test proves nothing broke.
- **CI runs every test on every push and PR.** A red build blocks the merge.
- **The test pyramid:** many fast unit tests, fewer integration tests, few end-to-end tests. The lecture's four levels map onto it like this:

  | Level (lecture) | What it tests | Speed | How many | Node.js tools |
  |-----------------|---------------|-------|----------|---------------|
  | **Unit** | One function or module alone | Milliseconds | Many | `node:test`, Jest, Vitest |
  | **Integration** | Parts together (route + service + real database) | Seconds | Some | Supertest, Testcontainers (real database in Docker) |
  | **System** | The **whole** system, end to end — **functional** (E2E user flows) **and non-functional** (performance, security, reliability) | Minutes | Few | Playwright (E2E), k6 (load), OWASP ZAP (security) |
  | **Acceptance** | Does it meet the user's needs? | — | Per story | Automated acceptance criteria (for example Gherkin/Cucumber) + customer/product owner review on staging (UAT) |

- **Pyramid vs. "testing trophy":** some teams (especially in JavaScript) prefer the **testing trophy**, which puts **more weight on integration tests**, because they give high confidence for their cost. Both agree on the main rule: **many fast tests, few slow ones, and no ice-cream cone** (mostly manual and E2E tests — slow and fragile).
- **Contract testing:** checks that a provider and its consumers still agree on the API. Two common forms:
  - **Schema validation:** responses are checked against the **OpenAPI** contract in tests.
  - **Consumer-driven contracts** (for example **Pact**): each client publishes what it expects, and the provider's CI checks it still delivers that — useful between microservices.
- **Automated security testing (DevSecOps):**

  | Check | What it does | Example tools |
  |-------|-------------|---------------|
  | **SAST (Static Application Security Testing)** | Scans source code for unsafe patterns | CodeQL, Semgrep |
  | **Dependency / SCA (Software Composition Analysis)** | Finds npm packages with known vulnerabilities | `npm audit`, Dependabot, Snyk |
  | **Secret scanning** | Finds passwords and keys in commits | GitHub secret scanning, gitleaks |
  | **DAST (Dynamic Application Security Testing)** | Attacks the running app in a test environment | OWASP ZAP |
  | **Container image scanning** | Finds vulnerable OS packages in Docker images | Trivy, Grype |

- **Shift-right testing:** some checks continue **in production** — canary releases, synthetic monitoring, feature flags and chaos experiments (see [4.10](#410-shift-right-testing-in-production)).
- **Regression tests for every bug:** each fixed bug gets a test, so if the bug ever comes back, CI **catches it at once**.

![The test pyramid: many unit tests, some integration tests, few end-to-end tests](images/sdlc-modern-test-pyramid.svg)

```javascript
// test/unit/rating.test.js — TDD: these tests were written BEFORE isValidRating existed
const test = require('node:test');
const assert = require('node:assert');
const { isValidRating } = require('../../src/services/rating');

test('accepts whole numbers 1 to 5', () => {
  for (const r of [1, 2, 3, 4, 5]) assert.strictEqual(isValidRating(r), true);
});

test('rejects edge cases from the acceptance criteria', () => {
  for (const r of [0, 6, 4.5, '5', null]) assert.strictEqual(isValidRating(r), false);
});
```

**What happens if... you only test the happy path?**

```javascript
// ❌ Passes even if the code wrongly accepts rating 99
test('rating works', () => assert.strictEqual(isValidRating(3), true));
// The bug escapes to production and is found by users — the most expensive place.
```

## 4. Industry practices the lecture does not cover

### 4.1 Ways to classify tests

| Classification | Meaning | Example |
|----------------|---------|---------|
| **Static testing** | Checking **without running** the code | Code review, linting, type checking, SAST |
| **Dynamic testing** | Checking **by running** the code | Unit, integration, E2E, load tests |
| **Black-box testing** | Testing inputs and outputs **without** looking at the code | QA sends requests to the API and checks responses |
| **White-box testing** | Testing **with knowledge of** the code's internal paths | A developer writes tests to cover every `if` branch |
| **Functional testing** | Does it do the **right thing**? | Rating 6 → HTTP 400 |
| **Non-functional testing** | Does it do it **well enough**? | 95% of requests under 200 ms at 500 users |

### 4.2 Common test types (and when they run)

| Type | Purpose | When |
|------|---------|------|
| **Smoke test** | "Does the build start and do the most basic things work?" | After every build and every deployment |
| **Sanity test** | A quick, narrow check that one specific fix or feature works | After a small fix |
| **Regression test** | Old features still work after a change | Every CI run |
| **Exploratory test** | A tester freely explores the app to find unexpected problems | During each sprint, by humans |
| **Performance / load test** | Speed under expected traffic | Before big releases, and regularly |
| **Stress / spike / soak test** | Behavior beyond normal load / sudden load / load for many hours (finds memory leaks) | Before big events or launches |
| **Security / penetration test** | Experts try to break in | Regularly and before major releases (often required by customers) |
| **Accessibility test** | Can people with disabilities use it (WCAG)? | Automated checks in CI (for example axe) + manual checks |
| **Property-based test** | The tool generates hundreds of inputs to break a rule ("a valid rating is always a whole number 1–5"); it **shrinks** a failure to the smallest example (for example **fast-check**) | In CI, for validation, parsing and calculation logic |
| **Fuzz test** | Sends random or malformed input to find crashes and security bugs | Nightly or before release, for parsers and public APIs |
| **Visual regression test** | Compares screenshots with approved ones to catch unwanted UI changes (for example Playwright screenshots) | In CI, for UI components and key pages |
| **Alpha / beta test** | Real users try a pre-release version (internal = alpha, external = beta) | Before general availability |

### 4.3 Non-functional testing: a load test example

```javascript
// load/reviews.k6.js — run with: k6 run load/reviews.k6.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 200,                         // 200 virtual users at the same time
  duration: '2m',
  thresholds: {
    http_req_duration: ['p(95)<200'], // the SLO from planning: 95% of requests under 200 ms
    http_req_failed: ['rate<0.001'],  // fewer than 0.1% errors (99.9% success)
  },
};

export default function () {
  const res = http.get('https://staging.example.com/books/9780132350884/reviews');
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);                         // each user waits 1 second between requests
}
// If a threshold fails, k6 exits with an error, so the CI pipeline fails too.
```

### 4.4 Writing good tests

- **AAA pattern:** **Arrange** (set up data) → **Act** (do one thing) → **Assert** (check the result).
- **FIRST** principles: tests are **F**ast, **I**ndependent (no order dependence), **R**epeatable (same result every time), **S**elf-validating (pass/fail with no human check), **T**imely (written with or before the code).
- **Test behavior, not implementation:** test what the API returns, not which private function was called. Then refactoring does not break the tests.
- **One reason to fail:** each test checks one behavior, with a name that says what it checks.

```javascript
// test/integration/reviews.test.js — integration test with Supertest (AAA pattern)
const test = require('node:test');
const assert = require('node:assert');
const request = require('supertest');
const app = require('../../src/app');          // the app WITHOUT app.listen()

test('POST /books/:isbn/reviews rejects rating 6 with 400 Problem Details', async () => {
  // Arrange
  const token = await loginAsTestUser();         // helper creates a user and returns a JWT

  // Act
  const res = await request(app)
    .post('/books/9780132350884/reviews')
    .set('Authorization', `Bearer ${token}`)
    .send({ rating: 6 });

  // Assert
  assert.strictEqual(res.status, 400);
  assert.match(res.headers['content-type'], /application\/problem\+json/);
  assert.strictEqual(res.body.status, 400);
});
```

### 4.5 Test doubles: mocks, stubs, fakes, spies

| Double | What it does | Example |
|--------|--------------|---------|
| **Stub** | Returns a fixed answer | `getBook()` always returns one test book |
| **Mock** | Checks that it was called in the expected way | "`sendEmail` was called once with the author's address" |
| **Spy** | Records calls to a real function | Count how many times the logger was called |
| **Fake** | A simple working version | An in-memory repository instead of PostgreSQL |

- **Mock at the boundaries** (email provider, payment API, clock) — not your own business logic.
- **Prefer a real database in integration tests** (Testcontainers) over mocking the database: many bugs live in SQL, constraints and transactions.

```javascript
// test/unit/reviewService.test.js — mock the email adapter (an external boundary)
const test = require('node:test');
const assert = require('node:assert');
const { createReviewService } = require('../../src/services/reviewService');

test('notifies the book author after a new review', async (t) => {
  const email = { send: t.mock.fn(async () => {}) };            // mock: records calls
  const repo = { insert: async (r) => ({ id: 1, ...r }) };       // fake repository
  const service = createReviewService({ repo, email });          // dependencies injected

  await service.addReview(7, '9780132350884', { rating: 5 });

  assert.strictEqual(email.send.mock.callCount(), 1);           // called exactly once
});
```

### 4.6 Test data and environments

- **Never use real production personal data** in tests. Use **synthetic** data (generated, for example with a library like Faker) or properly **anonymized** data.
- **Each test creates its own data** and does not depend on other tests (use factories or fixtures; reset the database between tests or run each test in a transaction that is rolled back).
- **Ephemeral preview environments:** many teams spin up a temporary environment **per pull request**, so reviewers and QA can test the change before merging. It is deleted after the merge.

### 4.7 Code coverage and its limits

- **Coverage** = the share of code lines or branches that tests run. Node.js has it built in: `node --test --experimental-test-coverage` (Jest and Vitest also report it).
- **Branch coverage** (every `if`/`else` path) says more than line coverage.
- **Coverage is a warning light, not a goal.** 100% coverage does not mean the tests check anything useful. Many teams use a minimum (for example 80%) to catch **untested areas**, not to prove quality.
- **Mutation testing** (for example **Stryker**) measures test **quality**: it makes small changes ("mutants") to the code, such as turning `>=` into `>`. If no test fails, the tests are too weak.

### 4.8 Flaky tests

- A **flaky test** sometimes passes and sometimes fails **with no code change**. It destroys trust in CI.
- **Common causes:** depending on time or dates, test order, shared data, real network calls, race conditions, fixed `sleep()` waits.
- **Fixes:** control the clock with fake timers, isolate data, mock external services, wait for **conditions** instead of fixed times. **Quarantine** a flaky test (move it out of the blocking suite) and fix it quickly — never just "re-run until green".

```javascript
// ❌ Flaky: fails when the test runs exactly at midnight, or in another time zone
test('review date is today', () => {
  const review = createReview();
  assert.strictEqual(review.date, new Date().toISOString().slice(0, 10));
});

// ✅ Control time with node:test fake timers (Date mocking needs Node 20.11+)
test('review date uses the current time', (t) => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-11-10T09:00:00Z') });
  const review = createReview();
  assert.strictEqual(review.date, '2026-11-10');
});
```

### 4.9 Bugs: severity, priority and lifecycle

- **Severity** = how bad the **technical impact** is. **Priority** = how **urgently** it must be fixed. They are different:

  | Example | Severity | Priority |
  |---------|----------|----------|
  | Payment page crashes for everyone | Critical | Highest — fix now |
  | Company logo wrong on the home page | Low | High — very visible |
  | Crash in a rarely used admin export | High | Medium |
  | Typo in a help page nobody reads | Low | Low |

- **Bug lifecycle:** New → Triaged → In progress → Fixed → Verified (retested) → Closed. If it appears again → **Reopened**.
- **A good bug report** contains: title, environment and version, **steps to reproduce**, **expected** result, **actual** result, logs/screenshots, severity.

```markdown
**Title:** POST /books/:isbn/reviews returns 500 when text is longer than 2000 chars
**Environment:** staging, api v1.5.0
**Steps:** 1. Log in  2. POST a review with rating 4 and 2,500-character text
**Expected:** 400 Problem Details "text: too long"
**Actual:** 500 Internal Server Error (log reqId 9f2c…)
**Severity:** Medium   **Priority:** High (any user can trigger it)
```

### 4.10 Shift-right: testing in production

- **Synthetic monitoring:** a robot runs key user flows (log in, post review) every few minutes against production.
- **Canary analysis:** compare error rate and latency of the new version against the old one before full rollout.
- **Feature flags:** turn a new feature on for internal users first ("dogfooding").
- **Chaos engineering:** carefully break things on purpose (kill a pod, slow the database) to prove the system recovers — start in staging, with a clear plan and a stop button.

### 4.11 Using AI in testing

- AI tools can **suggest test cases and edge cases**, generate test data, and draft test code.
- **Review generated tests carefully:** AI often writes tests that only repeat what the code already does, so they pass even when the code is wrong. Make sure each test checks a **requirement**.
- If the product **itself uses an AI model**, normal assertions are not enough because answers vary. Teams add **evaluations ("evals")**: a fixed set of example inputs with scoring rules, run on every change to the prompt or model.

## 5. Testing is "done enough" when... (exit criteria)

- [ ] Every **acceptance criterion** has a passing test (automated where possible).
- [ ] **Unit, integration and system** tests pass in CI; the suite is **not flaky**.
- [ ] Every fixed bug has a **regression test**.
- [ ] **Non-functional** targets are proven: performance (load test vs. SLOs), security scans clean, accessibility checks pass.
- [ ] **Coverage** is above the team minimum, and important paths (auth, payments, data changes) are well covered.
- [ ] No open **critical or high-severity** bugs (or each has an agreed plan).
- [ ] **Smoke tests** pass on staging; **UAT / product owner acceptance** is done.
- [ ] Test data contains **no real personal data**.

---

## 6. LumenVenture Standard

> **What we do on every project.** See the [guide README](../README.md) for roles, gates and project types. **must** = required · **should** = default (skip only with a written reason) · **may** = optional.

### 6.1 Owners

| Activity | Accountable | Responsible | Consulted |
|----------|-------------|-------------|-----------|
| Test strategy | QA Engineer | QA, Tech Lead | Developers, PO |
| Unit and integration tests | Tech Lead | Developers | QA |
| System (E2E and non-functional) tests | QA Engineer | QA, developers | Tech Lead, Security Champion |
| Bug triage (severity and priority) | Product Owner | QA | Tech Lead |
| UAT / acceptance | Product Owner | QA, PO (+ client) | Delivery Lead |

### 6.2 Required outputs

| Output | Internal | Client | Prototype | + Regulated |
|--------|----------|--------|-----------|-------------|
| Test strategy ([template](templates/test-strategy.md)) | **must** | **must** | **may** | **must** |
| Automated unit + integration tests in CI | **must** | **must** | **should** | **must** |
| Automated E2E tests for key flows | **should** | **must** | — | **must** |
| Load test against SLOs before go-live and major releases | **should** | **must** | — | **must** |
| Security scans in CI (dependency, secret, SAST) | **must** | **must** | **should** | **must** |
| DAST / penetration test | **may** | **should** (or as the contract says) | — | **must** before go-live |
| Accessibility checks (user-facing UI) | **should** | **must** | — | **must** |
| UAT sign-off ([template](templates/uat-signoff.md)) | PO **must** | Client + PO **must** | — | **must**, kept for audit |
| Bug reports ([template](templates/bug-report.md)) | **must** | **must** | **should** | **must** |

### 6.3 Gate input for G4 — Testing exit criteria

The release goes to [G4 in Deployment](../05-Deployment/Deployment.md#6-lumenventure-standard) only when:

- [ ] Every acceptance criterion in the release has a passing test (automated where possible)
- [ ] Unit, integration and system tests pass on the release commit; no known flaky tests in the blocking suite
- [ ] Coverage is at or above the project minimum; critical paths are covered
- [ ] Non-functional targets proven (load vs. SLOs, scans clean, accessibility) as the project type requires
- [ ] No open **S1/S2** bugs (or an agreed, signed plan for each)
- [ ] **UAT / acceptance signed**

### 6.4 Rules

1. **must** — Tests are written **with** the code (shift-left); a story is not done without them.
2. **must** — Every bug fix includes a **regression test**.
3. **must** — **No real personal data** in test environments; use synthetic or properly anonymized data.
4. **must** — Bugs are tracked with **severity and priority** (S1–S4, P1–P4) as defined in the test strategy.
5. **must** — A failing or flaky test is never "re-run until green": fix it, or **quarantine** it with a ticket and an owner within one working day.
6. **should** — Follow the test pyramid/trophy: many fast tests, few slow ones; use a real database in integration tests (for example Testcontainers).
7. **should** — Mock only at system boundaries (external APIs, email, clock).
8. **should** — Coverage minimum of **80%** for new code, used as a warning light, not a goal.
9. **should** — Exploratory testing by QA each sprint for new user-facing features.
10. **may** — Mutation testing on critical modules; preview environments per PR; **property-based tests** for validation and parsing logic; **fuzzing** for public parsers and APIs.

### 6.5 Templates

| Template | Copy to |
|----------|---------|
| [test-strategy.md](templates/test-strategy.md) | `docs/test-strategy.md` |
| [bug-report.md](templates/bug-report.md) | Your tracking tool (issue template) |
| [uat-signoff.md](templates/uat-signoff.md) | `docs/releases/<version>-uat.md` |

---

[← Development](../03-Development/Development.md) · [Guide README](../README.md) · [Overview](../../6-Phases-of-SDLC-Modern-Best-Practices.md) · [Deployment →](../05-Deployment/Deployment.md)
