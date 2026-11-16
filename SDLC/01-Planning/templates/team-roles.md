# Team Roles — <Project name>

> Copy to `docs/team-roles.md` at kickoff (README §2, step 1). Owner: Delivery Lead. Update it **the same day** a person joins, leaves or changes hats, and check it at every Sprint Retrospective.
> **One person can wear several hats** (at most 3; Developer work, on-call and backup duty do not count) — roles: [README §3](../../README.md#3-roles-default-for-a-48-person-team), optional and shared roles: [README §3.2](../../README.md#32-optional-and-shared-roles), rules: [README §3.3](../../README.md#33-role-rules).
> **Backup:** the person who takes over the hat when the holder is away for more than 2 working days. Required for **PO** (Product Owner) and **TL** (Tech Lead) from kickoff, and for **on-call** from go-live (Gate G5) when the project has an on-call rotation. Recommended for every hat.

**Last reviewed:** <YYYY-MM-DD> · **Next review due:** <YYYY-MM-DD> (every Sprint Retrospective, at least every 6 months)

## 1. Core roles (every project)

| Role (hat) | Short | Person | Share of their time | Backup | Notes |
|------------|-------|--------|---------------------|--------|-------|
| Sponsor | SP | | | — | Budget and go/no-go at Gates G1 (plan) and G2 (architecture) |
| Product Owner | PO | | | | Decides **what** and in which order — not **how it is built** |
| Delivery Lead (Scrum Master) | DL | | | | Coach; does **not** assign tasks |
| Tech Lead (architect in our team size) | TL | | | | Decides **how it is built**, with the Developers; writes ADRs (Architecture Decision Records) |
| Developers | DEV | | | — | Also test, review and run the service |
| QA (Quality Assurance) Engineer | QA | | | | Leads the test strategy; quality is the whole team's job |
| Security Champion | SEC | | | | Extra hat, usually a developer |
| On-call rotation (from go-live) | — | <names, in order> | <week on / weeks off> | <escalation person> | [Maintenance §4.3](../../06-Maintenance/Maintenance.md#43-alerting-and-on-call) |
| Client contact / decision-maker | CL | | | | Client projects; the same person as in the stakeholder register |

## 2. Optional and shared roles (tick the ones this project uses)

| Used? | Role | Person or team | Days per sprint | If not used, who covers it (write the reason) |
|-------|------|----------------|-----------------|-----------------------------------------------|
| [ ] | UX (User Experience) / product designer | | | PO + developers, using the company design system |
| [ ] | Technical writer | | | Developers + PO (README §7.2 rule 9) |
| [ ] | SRE (Site Reliability Engineering) / platform team (shared) | | | The team runs its own service |
| [ ] | Business analyst | | | PO |
| [ ] | Solution architect | | | TL |

**Line managers** (always outside the team — never the PO or DL of this project): <name per team member, or "LumenVenture engineering manager">

## 3. Checks (tick before Gate G1)

- [ ] Every core hat has a named person; PO and TL have a backup (on-call backup: before go-live).
- [ ] The **author** and the **reviewer** of a change are never the same person; the **PO** is not the only tester ([README §3](../../README.md#3-roles-default-for-a-48-person-team)).
- [ ] People management (line manager) is outside the PO and DL hats, or the exception is written in the project brief §10.
- [ ] Nobody holds more than **3** hats, and nobody's shares add up to more than 100% of their time.
- [ ] The RACI in [README §3.1](../../README.md#31-who-does-what-raci) applies, or the project's changes to it are listed below.

## 4. Changes to the default RACI (if any)

| Activity | Change | Reason |
|----------|--------|--------|
| | | |

---

## Filled example — Book Review API (client project, 6 people)

**1. Core roles**

| Role (hat) | Short | Person | Share | Backup | Notes |
|------------|-------|--------|-------|--------|-------|
| Sponsor | SP | Client's Head of Digital | — | — | Signs G1, G2 |
| Product Owner | PO | Asha | 80% | Ben | Works with the client decision-maker every week |
| Delivery Lead (Scrum Master) | DL | Ben | 50% (also a developer, 50%) | Asha | Runs the events; single contact for the client's project manager on budget and dates |
| Tech Lead + Security Champion | TL, SEC | Chen | 100% | Dina | Writes ADRs, leads the threat model |
| Developers | DEV | Dina, Eli, Ben (50%) | — | — | |
| QA Engineer | QA | Farah | 100% | Eli | Also writes the OpenAPI (API description) examples |
| On-call rotation (from go-live) | — | Dina → Eli → Chen | 1 week each | Escalation: Chen | |
| Client contact / decision-maker | CL | Client's Product Manager | — | Client's Head of Digital | Same as the stakeholder register |

**2. Optional and shared roles**

| Used? | Role | Person or team | Days per sprint | If not used, who covers it |
|-------|------|----------------|-----------------|----------------------------|
| [x] | UX / product designer (shared) | Company design team | 1 | — (prototype test before each new screen) |
| [ ] | Technical writer | — | — | Developers + Farah write the docs; PO owns user docs (no public API, one client audience) |
| [x] | SRE / platform team (shared) | Company platform team | — | Provides the Kubernetes platform and SLO dashboards; the team stays on call |
| [ ] | Business analyst | — | — | PO (business rules are simple) |
| [ ] | Solution architect | — | — | TL (only one client system to integrate) |

**Line managers:** LumenVenture engineering manager (outside the team).

**Checks:** Ben holds 2 hats (DL + DEV — Developer work does not count) plus the PO backup, and never reviews his own pull requests · Chen holds 2 hats (TL + SEC) · Asha (PO) is not a tester; Farah leads testing · line managers are outside the team.
