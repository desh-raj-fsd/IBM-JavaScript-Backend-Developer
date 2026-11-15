# Design: <feature or system name>

| Field | Value |
|-------|-------|
| **Author(s)** | |
| **Reviewers** | Tech Lead + at least one developer (+ Security Champion if security-relevant) |
| **Requirements / stories** | <IDs> |
| **Status** | Draft / In review / Approved / Superseded |

> Copy to `docs/design/<short-name>.md`. Open it as a **pull request** for review. Write only what is needed — 1–5 pages is typical.

## 1. Context and problem
<Why are we doing this? What is the current situation?>

## 2. Goals and non-goals
- **Goals:**
- **Non-goals (explicitly out):**

## 3. Quality attributes that drive this design
| Attribute | Target | How the design meets it |
|-----------|--------|-------------------------|
| Performance | | |
| Availability | | |
| Security | | |
| Scalability | | |
| Cost | | |

## 4. Proposed design
### 4.1 High-level (HLD)
<C4 context/container diagram (Mermaid/PlantUML), main components, technology choices.>

### 4.2 Low-level (LLD)
- **Data:** schema / collections, constraints, indexes, migrations
- **API:** endpoints or events (link to OpenAPI / AsyncAPI file), error format, pagination, versioning
- **Modules:** responsibilities and boundaries

## 5. Alternatives considered
| Option | Pros | Cons | Why not chosen |
|--------|------|------|----------------|
| | | | |

## 6. Security and privacy
- Threat model link and main mitigations
- Personal / sensitive data: what, where stored, retention, who can access

## 7. Reliability and operations
- Failure cases and behavior (timeouts, retries, degradation)
- Logs, metrics, traces, alerts, health checks
- Backups / recovery needs

## 8. Rollout, migration and rollback
- Feature flag? Migration steps (expand → migrate → contract)? Rollback plan?

## 9. Testing plan
- Unit / integration / system / non-functional tests needed

## 10. Open questions
-

## 11. Decision
| Role | Name | Date | Decision |
|------|------|------|----------|
| Tech Lead | | | |
