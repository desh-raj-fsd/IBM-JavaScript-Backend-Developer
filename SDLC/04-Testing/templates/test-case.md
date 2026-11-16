# Test Cases — <Project> · <area, e.g. Reviews>

> For tests that **cannot be automated** or need a **signed record**: UAT scripts for the client, OAT (Operational Acceptance Testing), manual accessibility checks, regulated projects ([Testing §4.14](../Testing.md#414-test-cases-and-test-design-techniques), rule 17). Automated tests do **not** need this file — the test code is the test case.
> Copy to `docs/test-cases/<area>.md`. Write each case **as soon as its requirement is agreed**, before the test session. Owner: QA Engineer.

## 1. Test cases

| ID | Title | Requirement | Preconditions | Steps and input data | Expected result | Priority | Technique |
|----|-------|-------------|---------------|----------------------|-----------------|----------|-----------|
| TC-<req>-<n> | | REQ-… | | 1. … 2. … | | High / Medium / Low | Equivalence class · Boundary · Decision table · State transition · Journey |

**Filled example (Book Review API):**

| ID | Title | Requirement | Preconditions | Steps and input data | Expected result | Priority | Technique |
|----|-------|-------------|---------------|----------------------|-----------------|----------|-----------|
| TC-07-01 | Rating 5 is accepted | REQ-07 | Test user `asha` logged in; book `978-0132350884` exists; `asha` has not reviewed it | 1. Open the book page 2. Choose 5 stars, type "Great" 3. Click **Post** | Review shows with 5 stars; average rating updated | High | Boundary (upper limit) |
| TC-07-02 | Rating above 5 is rejected | REQ-07 | As TC-07-01 | 1. Send `POST /v1/books/978-0132350884/reviews` with `{ "rating": 6 }` | `400`, Problem Details "Rating must be between 1 and 5"; no review saved | High | Boundary (just outside) |
| TC-12-01 | Keyboard-only user can post a review | REQ-12 (WCAG 2.2 AA) | As TC-07-01; screen reader on; no mouse | 1. Tab to the rating control 2. Choose 4 with the arrow keys 3. Tab to **Post**, press Enter | Focus is always visible; the screen reader announces the rating and the success message | High | Journey (accessibility) |

> Use **test data only** — no real personal data. Write expected results so that anyone can decide pass or fail without asking.

## 2. Execution record

> Copy this part to `docs/releases/<version>-tests.md` for each test session. Regulated projects: keep it for audit.

| Field | Value |
|-------|-------|
| **Release / version and commit** | |
| **Environment** | staging / UAT, URL: |
| **Tester(s)** | |
| **Date** | |

| Test case | Actual result | Status (Pass / Fail / Blocked / Not run) | Bug ID (if failed) |
|-----------|---------------|------------------------------------------|--------------------|
| TC-07-01 | | | |

| Summary | Number |
|---------|--------|
| Passed | |
| Failed (each has a bug report) | |
| Blocked / not run (with reason) | |

| Role | Name | Date | Signature / approval link |
|------|------|------|---------------------------|
| Tester | | | |
| QA Engineer | | | |
| Product Owner / client (UAT sessions — or link the [UAT sign-off](uat-signoff.md)) | | | |
