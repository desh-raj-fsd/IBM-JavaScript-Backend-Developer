# Release Checklist (Gate G4) — <Project> <version>

> Copy to `docs/releases/<version>.md`, or attach it to the release ticket. Accountable: Tech Lead. With Continuous Deployment, the **pipeline** must check the automatable items on every release; this checklist is then used for **major** releases.

| Field | Value |
|-------|-------|
| **Version / image tag or digest** | |
| **Release type** | Major (breaking) / Minor (feature) / Patch (fix or hotfix) — per the [versioning policy](../../03-Development/templates/versioning-policy.md) |
| **Git tag / commit SHA** | `v…` / |
| **Planned date and time** | (avoid late Friday and known peak periods) |
| **Release owner** | |

## Quality
- [ ] All stories in the release meet the **Definition of Done**
- [ ] CI green on the exact commit being released
- [ ] Testing exit criteria met (system, non-functional, security scans) — see test strategy
- [ ] No open S1/S2 bugs, or each has an agreed plan
- [ ] **UAT / acceptance signed** (PO; client on client projects) — link:

## Safety
- [ ] The **same image** that passed staging is being promoted (by version tag or digest — never `latest`)
- [ ] The version number matches the changes (breaking → MAJOR; API breaking changes have a new API version); `CHANGELOG.md` entry written; not a pre-release
- [ ] After deploy: `GET /version` returns this version and commit SHA
- [ ] Release strategy chosen: rolling / canary / blue-green; feature flags set
- [ ] Database migrations backward compatible; tested on staging with realistic data
- [ ] **Rollback plan** written and possible: <how, and how long it takes>
- [ ] Config and secrets for production verified (no secrets in the image)

## Operations
- [ ] Dashboards and alerts cover the new behavior
- [ ] On-call person knows the release is happening
- [ ] Runbooks updated for new alerts
- [ ] Client / users / support informed if behavior changes

## After release
- [ ] Smoke tests passed in production
- [ ] Error rate and latency normal for 30 minutes (or canary analysis passed)
- [ ] Release tagged; release notes / CHANGELOG published
- [ ] Release recorded (change record for regulated data projects)

| Role | Name | Go / No-go | Time |
|------|------|------------|------|
| Tech Lead | | | |
| QA Engineer | | | |
| Product Owner | | | |
