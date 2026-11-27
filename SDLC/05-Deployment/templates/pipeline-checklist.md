# CI/CD Pipeline and Environments Checklist

> Use when setting up a new project's pipeline (with the repo setup checklist). Owner: Tech Lead.

## Environments
- [ ] **Local** (one-command start, containers for dependencies)
- [ ] **CI** (clean, reproducible build on every push and PR)
- [ ] **Preview per PR** (should, for web apps/APIs where practical)
- [ ] **Staging / UAT** (production-like: same image, same config shape, realistic data volume, no real personal data)
- [ ] **Production** (access only through the pipeline; human access is break-glass and logged)

## Pipeline stages
- [ ] Pull-request pipeline feedback in about 10 minutes (ceiling 15); a red `main` is fixed or reverted within 1 hour ([Deployment rule 22](../Deployment.md#64-rules))
- [ ] Install with lockfile → lint → type check → unit tests → integration tests
- [ ] Security: dependency scan, secret scan, SAST; container image scan
- [ ] Web UIs: accessibility check, bundle-size budget and lab performance check ([Testing rules 18–19](../../04-Testing/Testing.md#64-rules))
- [ ] Docs checks: Markdown lint, broken links, OpenAPI lint ([README §7.2](../../README.md#72-documentation-rules), rule 5)
- [ ] Build **once** in CI for the pinned target CPU architecture (default `linux/amd64`; [Deployment rule 23](../Deployment.md#64-rules)); tag with commit SHA (and version); push to the registry
- [ ] Deploy to staging automatically → smoke tests
- [ ] Production: approval gate (client and regulated projects **must**) or Continuous Deployment (internal products **may**)
- [ ] Safe rollout (rolling / canary / blue-green) with health checks
- [ ] Post-deploy smoke tests; automatic rollback where supported

## Security of the pipeline
- [ ] Short-lived credentials (OIDC) instead of stored cloud keys
- [ ] Least-privilege permissions per job
- [ ] Protected environments with required reviewers for production
- [ ] Third-party pipeline actions/plugins pinned to versions (or commit SHAs)
- [ ] Image signing and SBOM (should for client and regulated projects)

## Infrastructure
- [ ] Infrastructure as Code in Git, reviewed by PR
- [ ] Resource requests/limits and autoscaling rules set
- [ ] Backups configured (see Maintenance)
- [ ] TLS certificates renewed automatically
- [ ] DNS records in Infrastructure as Code; registrar lock and 2FA on the domain account
- [ ] HTTPS-only: HTTP redirects to HTTPS, TLS 1.2 minimum (1.3 preferred), HSTS sent on HTTPS responses
- [ ] CDN in front of public files; cache headers set (hashed files immutable, HTML `no-cache`, personal responses `private`)
- [ ] Production runs at least 2 instances in at least 2 availability zones behind a health-checked load balancer

## Measurement
- [ ] DORA metrics visible: change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate
