# Versioning Policy — <Project name>

> Copy to `docs/versioning-policy.md` in Sprint 0. Owner: Tech Lead. Change it only with an ADR. Rules: [Development §4.2](../Development.md#42-commits-and-versioning), [Design §4.4.1](../../02-Design/Design.md#441-api-compatibility-and-versioning).

## 1. What we version, and how

| Thing | Scheme | Where the version lives | Example |
|-------|--------|-------------------------|---------|
| Service / app | SemVer `MAJOR.MINOR.PATCH` | `package.json` `"version"`, Git tag `vX.Y.Z`, image tag | `2.5.0` |
| Public REST API | Major version in the path (`/v1`, `/v2`) | OpenAPI `info.version` (full SemVer) | `/v2`, `info.version: 2.5.0` |
| Shared npm package / SDK | SemVer; pre-releases with labels and a dist-tag | npm registry | `3.0.0-beta.1` (`@beta`) |
| Event / message schemas | Version field in the schema name or header | AsyncAPI document | `review.posted.v1` |
| <other, e.g. mobile app> | <SemVer or CalVer — say why> | | |

## 2. When we increase which number

| Change | Bump |
|--------|------|
| Breaking change for any client (see the list in Design §4.4.1) | **MAJOR** — and a new API version if the public API breaks |
| New backward-compatible feature | **MINOR** |
| Backward-compatible bug or security fix | **PATCH** |
| Docs, tests, internal refactoring only | No release (or PATCH if it must ship) |

- Commit messages follow **Conventional Commits**; `<release tool, e.g. release-please / semantic-release / Changesets>` picks the next version and writes `CHANGELOG.md`.
- `0.y.z` is allowed only **before** the first real client. The first release real clients use is **`1.0.0`**.
- A released version is **never changed or re-published**. A fix is always a new version.
- Pre-releases (`-alpha.n`, `-beta.n`, `-rc.n`) never reach production.

## 3. Supported versions

| Item | Supported | End of support |
|------|-----------|----------------|
| Node.js runtime (`engines`, `.nvmrc`, Docker base image) | <e.g. 24.x LTS> | <EOL date from nodejs.org> |
| API versions | <e.g. /v2 (current), /v1 (deprecated)> | <Sunset date of /v1> |
| <framework, database> | | |

## 4. Deprecation

- Notice period before removing an API version or feature: **≥ <6> months** for external / partner clients, **≥ <1> month** for internal-only clients.
- Deprecated endpoints send `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers and link to the migration guide.
- Usage of deprecated versions is tracked per client until it reaches zero, then the version is removed.

## 5. How anyone can see the running version

- `GET /version` → `{ "version": "…", "commit": "…" }`
- Logs and traces: `service.version`
- Images: `<name>:<version>` and `<name>:<commit SHA>`; production deploys by **digest**

## 6. Approval

| Role | Name | Date |
|------|------|------|
| Tech Lead | | |
