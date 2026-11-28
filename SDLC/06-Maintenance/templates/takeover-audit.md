# Takeover Audit — <Product taken over from another vendor>

> Use when we take over software, firmware or cloud systems that someone else built ([Maintenance §4.13](../Maintenance.md#413-taking-over-a-product-from-another-vendor), rule 21). Run it as a **fixed-length audit sprint** (default 1–2 weeks, paid) **before** we promise any feature, date or price for new work. Owner: Tech Lead. Keep in `docs/takeover/audit.md`.

## 1. Ownership and access (transfer, then rotate)
Every item must be **owned by the client** (or by us under contract), never by a former vendor's personal account.

| Asset | Current owner | Transferred to | Credentials rotated | Done |
|-------|---------------|----------------|---------------------|------|
| Source repositories (all, including firmware and scripts) | | | | [ ] |
| Cloud accounts (root / admin), billing | | | | [ ] |
| Domains, DNS, TLS certificates | | | | [ ] |
| App store accounts (Apple, Google), signing keys | | | | [ ] |
| Firmware signing keys, device certificates, IoT registry | | | | [ ] |
| Third-party services (payments, email, maps, AI APIs) | | | | [ ] |
| CI/CD, secrets store, monitoring, error tracking | | | | [ ] |
| Documentation, designs, test data, hardware drawings | | | | [ ] |

## 2. Can we rebuild and release it?
- [ ] We built every component **from source** on our machines and in CI
- [ ] We deployed to a staging environment (and, for devices, flashed a bench device)
- [ ] Versions running in production / on devices match a commit we have (record any mismatch)

## 3. Baseline: how it works today (before we change anything)
- Architecture sketch (C4 context + containers), data flows, device ↔ cloud ↔ app links
- Current metrics: errors, uptime, monthly cloud cost, device fleet size and firmware versions
- Existing tests and how much they cover; manual steps nobody wrote down

## 4. Risk report for the client
| # | Finding | Impact | Likelihood | Recommendation | Cost range |
|---|---------|--------|------------|----------------|------------|
| 1 | e.g. "Admin password shared in a chat group" | High | High | Rotate now, add MFA | small |

Sort by risk. Separate **fix now** (security, data loss, things that stop us working) from **plan later**.

## 5. Decision with the client
- [ ] Risk report presented and accepted in writing
- [ ] First backlog built from the findings (Planning §8)
- [ ] Support model agreed (Kanban lane, response times, retainer hours)
- [ ] Former vendor's access removed
