# Assumptions and Decisions Log — <Project name>

> Copy to `docs/discovery/assumptions-and-decisions-log.md`. Owner: Product Owner. **Living document** — update it after every client meeting, demo and change request.
> **Why:** most client disagreements come from **hidden assumptions** and **forgotten decisions**. This log makes them visible and gives each one an ID that can be quoted in the PRD, stories and change requests.

## Assumptions
An **assumption** is something we believe is true but the client has **not yet confirmed**.

| ID | Assumption | Made by / date | Impact if wrong (cost, time, risk) | Status | Confirmed by / date |
|----|------------|----------------|-------------------------------------|--------|---------------------|
| A-01 | Users log in with email and password only | PO, <date> | Social login adds ~<N> days | Open / Confirmed / Rejected | |
| A-02 | | | | | |

**Rules**
- Every assumption that changes **cost or time** must be **confirmed in writing** before the client PRD is approved.
- A **rejected** assumption becomes either a new requirement (before approval) or a **change request** (after approval).

## Decisions
A **decision** is something the client (or LumenVenture) has **agreed**.

| ID | Decision | Decided by | Date | Where recorded (meeting summary, email, demo) | Replaces |
|----|----------|------------|------|-----------------------------------------------|----------|
| D-01 | First version is mobile only (Android + iPhone) | <client name> | | Meeting summary <date> | — |
| D-02 | | | | | |

**Rules**
- Only the **named client decision-maker** can make scope decisions for the client.
- Never delete a decision. If it changes, add a new one and write the old ID in **Replaces**.
- Technical decisions (database, framework) go into an **ADR** (Architecture Decision Record), not this log.
