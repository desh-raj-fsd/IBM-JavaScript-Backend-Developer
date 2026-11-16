# Definition of Done — <Project name>

> The team's shared quality bar (Gate **G3**). Agree it in Sprint 0; review it in retrospectives. A story is **done** only when **every** item is true. Teams may **add** items, not remove the LumenVenture minimum (marked ★).

## Code
- [ ] ★ Meets every acceptance criterion of the story
- [ ] ★ Follows the design (API contract, module boundaries, ADRs)
- [ ] ★ Lint, format and type checks pass
- [ ] ★ Reviewed and approved by at least one other developer
- [ ] Small, focused PR with a clear description

## Tests
- [ ] ★ Unit and integration tests written and passing in CI
- [ ] ★ Every bug fix includes an automated test named with the bug ID that fails without the fix (Testing rule 15)
- [ ] Acceptance criteria automated where practical
- [ ] No new flaky tests

## Security and data
- [ ] ★ Input validated; authorization (ownership) checked on the server
- [ ] ★ No secrets in code, config files or logs
- [ ] ★ Dependency, secret and SAST scans pass (no new high/critical issues)
- [ ] Personal data handled as the design says (retention, access)

## Operations
- [ ] ★ Database migrations are backward compatible
- [ ] Logs, metrics and alerts added for new behavior where needed
- [ ] Unfinished user-facing work is behind a feature flag

## Docs
- [ ] ★ Docs affected by the change (README, OpenAPI, user help, runbook, SOP, CHANGELOG) updated **in this PR** (help-center content: in the same release) — or "no docs change" stated ([README §7.2](../../README.md#72-documentation-rules), rule 2)
- [ ] ADR written for any significant decision

## Delivery
- [ ] ★ Merged to `main` and deployed to staging by the pipeline
- [ ] Accepted by the Product Owner
