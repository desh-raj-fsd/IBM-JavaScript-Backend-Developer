# Repository Setup and Walking Skeleton Checklist

> Do this in **Sprint 0 / week 1**, before feature work. Goal: a minimal "hello world" that goes from `git push` to **staging** through the real pipeline, with health checks and monitoring. Owner: Tech Lead.

## Repository
- [ ] Repository created in the LumenVenture organization; access by team, least privilege
- [ ] `main` is protected: PR required, ≥ 1 approval, CI must pass, no force-push
- [ ] `CODEOWNERS` file
- [ ] `README.md`: what it is, how to run, test, deploy
- [ ] `.gitignore` (includes `.env`), `.env.example` with fake values
- [ ] Runtime version pinned (for example `.nvmrc`, `.tool-versions`)
- [ ] Lockfile committed; CI uses a clean, locked install (for example `npm ci`)
- [ ] `.github/pull_request_template.md` copied from this guide
- [ ] `docs/` folder created with the structure from the guide README

## Code quality
- [ ] Linter and formatter configured and run in CI (and pre-commit)
- [ ] Type checking (if the language supports it)
- [ ] Layered structure agreed (for example routes → services → repositories)
- [ ] Config read from the environment and **validated at startup**
- [ ] Central error handler with one error format (for example RFC 9457 Problem Details)
- [ ] Structured logging with request IDs; no secrets or personal data in logs

## Pipeline and environments
- [ ] CI runs: lint, type check, unit + integration tests, dependency scan, secret scan, SAST
- [ ] Build **one** versioned artifact/image per commit; push to the registry
- [ ] Automatic deploy to **staging**; production through an approval gate (or Continuous Deployment where allowed)
- [ ] Secrets in a secret manager / CI secrets; no long-lived cloud keys (prefer OIDC)
- [ ] Health endpoints (liveness / readiness)

## Observability
- [ ] Logs collected centrally
- [ ] Basic metrics (rate, errors, duration) and a dashboard
- [ ] Error tracking connected
- [ ] One test alert routed to the team

## Security
- [ ] Dependency update bot (for example Dependabot / Renovate) enabled
- [ ] Secret scanning enabled
- [ ] Security headers / CORS / rate limiting defaults in place (web APIs)

**Done when:** a commit to `main` reaches staging automatically, the health check is green, logs and metrics appear on the dashboard, and the test alert reaches the team.
