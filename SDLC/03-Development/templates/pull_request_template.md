<!-- Copy to .github/pull_request_template.md in every LumenVenture repository -->

## What and why
<!-- What does this change do, and why? Link the story/requirement: Closes #123 (REQ-07) -->

## How to test
<!-- Commands, requests or steps a reviewer can follow -->

## Risk and rollout
- [ ] Low risk / [ ] Behind a feature flag / [ ] Needs a migration (backward compatible?)
- Rollback: <how to undo this change>

## Checklist (Definition of Done)
- [ ] Meets the acceptance criteria
- [ ] Tests added or updated (unit / integration); CI is green
- [ ] Input validated; authorization checked; no secrets in code or logs
- [ ] Errors go through the central error handler
- [ ] API contract / docs / CHANGELOG updated if needed
- [ ] PR is small and focused (one concern)
- [ ] AI-assisted code (if any) was read, understood and tested like my own code
