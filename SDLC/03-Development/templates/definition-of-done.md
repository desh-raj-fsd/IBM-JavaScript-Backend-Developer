# Definition of Done — <Project name>

> The team's shared quality bar (Gate **G3**). Agree it in Sprint 0; review it in retrospectives. A story is **done** only when **every** item is true. Teams may **add** items, not remove the LumenVenture minimum (marked ★).

## Code
- [ ] ★ Meets every acceptance criterion of the story
- [ ] ★ Follows the design (API contract, module boundaries, ADRs)
- [ ] ★ Lint, format and type checks pass
- [ ] ★ Reviewed and approved by at least one other developer
- [ ] Small, focused PR with a clear description
- [ ] User-facing UI: native elements, keyboard test, works at 320 px and on desktop, accessibility check passes ([frontend-checklist.md](frontend-checklist.md))
- [ ] ★ UI matches the **Approved** design (all states), checked by QA or the designer (Testing rule 20)
- [ ] ★ Firmware (track B): tested on the **target hardware**, not only in a simulator (Testing rule 21)
- [ ] ★ AI features (track C): eval set passes its threshold (Testing rule 23)

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
- [ ] Client projects: included in this sprint's **delivery note**, with user-guide changes (Deployment rule 27)
