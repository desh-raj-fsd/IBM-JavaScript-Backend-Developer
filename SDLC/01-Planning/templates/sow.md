# Statement of Work (SOW) — <Project name>, <Phase name>

> The signed agreement on **what we build, for how much and by when**, for one phase of a client project ([Planning rule 10](../Planning.md#84-rules)). Write it **after** the client PRD is approved and the client has **accepted a proposal** ([estimate and proposal](estimate-and-proposal.md), Planning rule 29), and **before** any build work starts. Copy scope, timeline and price from the accepted option. Owner: Product Owner writes it; the Sponsor signs for LumenVenture; the client's named decision-maker signs for the client. Keep the signed copy in `docs/sow/<phase>.md` (and the signed PDF where the contract lives).
>
> This template covers the **delivery** content. Legal terms (liability, governing law, termination, payment penalties) belong in the master agreement or are added by whoever handles contracts; have a qualified person review the first SOW for each new client.

| Field | Value |
|-------|-------|
| Client (legal name) | |
| Client decision-maker (signs) | <name, role> |
| LumenVenture signatory | <Sponsor> |
| Master agreement / NDA | <reference and date, or "none"> |
| SOW version and date | v1.0, <date> |
| Delivery track(s) | A / B / C / D / E ([README §4.1](../../README.md#41-delivery-tracks-by-service)) |

## 1. Background and goal
- One paragraph: the client's problem and what this phase achieves.
- Success measures for this phase (from the PRD / project brief `OBJ-n`).

## 2. Scope
**In scope** (from the approved client PRD, version <x>, approved on <date>):

| ID | Feature or deliverable | Priority (MoSCoW) |
|----|------------------------|-------------------|
| F-01 | | Must |

**Out of scope** (written so nobody assumes it is included):
- e.g. "Admin dashboard", "iOS app", "content writing", "hosting costs after go-live", "hardware manufacturing"

## 3. Deliverables
- [ ] Working software in production (or on devices / in the stores), as listed in section 2
- [ ] Source code in a repository the client owns or receives at hand-over
- [ ] User guide and release notes for delivered features ([README §7.2](../../README.md#72-documentation-rules) rule 9)
- [ ] Sprint delivery note after every sprint ([template](../../05-Deployment/templates/sprint-delivery-note.md))
- [ ] Closure report and hand-over at the end ([template](../../06-Maintenance/templates/project-closure.md))
- [ ] <track-specific: firmware images and signing hand-over, eval report for AI features, brand files…>

## 4. Timeline
| Milestone | Content | Date range (85% confidence) |
|-----------|---------|-----------------------------|
| Start | Kickoff, Sprint 1 | |
| <Milestone> | | |
| Go-live | | |

Dates are **ranges** (Planning rule 23) and assume the client's inputs in section 6 arrive on time.

## 5. Price and payment
- **Contract model:** fixed price per phase / time and materials with a cap / fixed budget, flexible scope ([Planning §4.17](../Planning.md#417-forecasting-and-budgeting-fix-time-and-cost-flex-scope))
- **Price:** <amount and currency>; taxes: <included / extra>
- **Payment schedule:**

| Payment | When | Amount |
|---------|------|--------|
| 1 | On signing | |
| 2 | <milestone accepted> | |
| 3 | Final acceptance | |

- **Not included in the price:** third-party costs (cloud, app store accounts, paid APIs, AI usage, devices) — paid by: <client / us, re-billed>

## 6. What we need from the client
| Input | Needed by | Owner (client side) |
|-------|-----------|---------------------|
| Decision-maker available for Sprint Reviews (every 2 weeks) | ongoing | |
| Feedback on designs and releases within <2> working days | ongoing | |
| Content, brand assets, accounts, API keys, test devices | <date> | |

Late inputs move the dates in section 4; we tell the client in the next delivery note.

## 7. How changes work
- New ideas after signing go into the backlog. The client chooses: a **swap** (same size, no price change) or a **change request** with cost and time ([template](change-request.md), Planning rules 5 and 15).
- No "quick change" is built without one of these, in writing.

## 8. Acceptance
- Each feature is accepted against its acceptance criteria in **UAT** ([template](../../04-Testing/templates/uat-signoff.md)).
- The client has <5> working days to accept or report a defect; no answer by then counts as accepted **for that delivery only** (scope changes are never accepted by silence).
- Defects found in UAT that break an acceptance criterion are fixed at no extra cost.

## 9. Ownership, access and data
- Code, designs and accounts created for the client belong to the client after <full payment / each milestone payment>.
- All accounts (cloud, app stores, domains, device registry) are created in the **client's name** or transferred at hand-over ([takeover audit](../../06-Maintenance/templates/takeover-audit.md), section 1).
- Personal data is handled as agreed in <data processing agreement / privacy section>.

## 10. After go-live
- Warranty: <e.g. 30 days of defect fixes at no cost>
- Support: <none / support agreement with response times and monthly hours>

## 11. Signatures
| For | Name | Role | Signature | Date |
|-----|------|------|-----------|------|
| Client | | | | |
| LumenVenture | | Sponsor | | |
