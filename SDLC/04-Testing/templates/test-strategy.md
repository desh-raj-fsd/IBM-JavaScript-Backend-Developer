# Test Strategy — <Project name>

> Copy to `docs/test-strategy.md` in Sprint 0. Owner: QA Engineer (Accountable), with the Tech Lead. One to three pages.

## 1. Quality goals
- What "good enough" means for this project (link the non-functional requirements and SLOs).

## 2. Test levels and ownership
| Level | What we test | Tools (examples) | Who writes it | Runs when |
|-------|--------------|------------------|---------------|-----------|
| Unit | Functions/modules alone | | Developers | Every push |
| Integration | API + real database / services | | Developers | Every push |
| System — functional (E2E) | Key user flows | | QA | Every merge to main / nightly |
| System — non-functional | Load, security, accessibility | | QA + TL + Security Champion | Before releases; regularly |
| Acceptance | Acceptance criteria / UAT | | QA + PO (+ client) | Per story; before release |

### 2.1 Regression schedule ([Testing §4.15](../Testing.md#415-regression-testing-what-runs-when), rule 14)
| When | What runs | Command / CI job |
|------|-----------|------------------|
| Every pull request | All tests. Affected tests only when: <e.g. the suite takes more than 10 minutes> | |
| Every merge to `main` | Full automated suite | |
| Nightly (rule 14) | Full suite + <slow E2E, fuzz, visual, short load test> | |
| Before every release | Full suite on the release commit + <load, DAST, accessibility> | |

### 2.2 Test design
- Techniques we use: equivalence partitioning and boundary values for every validated input; decision tables for: <rules>; state-transition tests for: <status fields>
- Supported platforms tested in the CI matrix (rule 16; the list comes from `docs/versioning-policy.md`): <Node.js LTS lines, browsers, API client versions>
- Tests that stay manual (written with the [test-case template](test-case.md)): <UAT scripts, OAT, manual accessibility checks>

## 3. Coverage and quality targets
- Minimum line/branch coverage: <e.g. 80%> (a warning light, not a goal)
- Critical paths that need extra tests: <auth, payments, data changes…>
- Mutation testing: yes / no (where)

## 4. Test data and environments
- Test data: synthetic / anonymized — **never** real personal data
- Environments: local · CI · preview per PR (yes/no) · staging
- How the database is reset between tests

## 5. Non-functional tests
| Type | Target | Tool | Frequency |
|------|--------|------|-----------|
| Load | e.g. p95 < 200 ms at <N> users | | |
| Security (SAST / DAST / dependency) | No high/critical open | | |
| Penetration test | Required? (regulated / client contract) | | |
| Accessibility | e.g. WCAG 2.2 AA | | |
| Compatibility | All supported platforms in §2.2 | | Every PR (CI matrix) |
| Recovery (restore drill) | Within the documented RPO / RTO ([Maintenance §4.6](../../06-Maintenance/Maintenance.md#46-backups-and-disaster-recovery)) | | At least every quarter |
| Documentation | API docs match the OpenAPI contract | | Every PR |

## 6. Bugs
- Tracking tool:
- Severity levels (S1 critical … S4 low) and the expected response time for each
- Who triages, and when

## 7. Release exit criteria
- Link: LumenVenture **G4** checklist (`05-Deployment/templates/release-checklist.md`) plus any project-specific items.

## 8. Risks to quality
- <e.g. no production-like data volume in staging; external API without a sandbox>
