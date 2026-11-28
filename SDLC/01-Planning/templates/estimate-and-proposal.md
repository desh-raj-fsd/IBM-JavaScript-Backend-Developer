# Estimate and Proposal — <Client name> / <Project or phase>

> Use **after** the client PRD is approved and **before** the SOW ([Planning §8.6.2](../Planning.md#862-the-eight-discovery-steps) step 5a, rule 29). Part A is **internal**: how we got the numbers. Part B is the **proposal** we send to the client. When the client accepts Part B, the agreed numbers go into the [SOW](sow.md).
> Owners: Delivery Lead builds the estimate with the team; Tech Lead checks the effort and risks; **Sponsor approves the price**; Product Owner writes the proposal. Keep Part A in `docs/estimate/<phase>.md` (never sent to the client).

| Field | Value |
|-------|-------|
| Client PRD version | <v1.x, approved on <date>> |
| Delivery track(s) | A / B / C / D / E ([README §4.1](../../README.md#41-delivery-tracks-by-service)) |
| Estimate by | <DL>, with <team members> |
| Checked by (Tech Lead) | <name, date> |
| Price approved by (Sponsor) | <name, date> |

---

## Part A — Estimate (internal)

### A1. Effort per epic
Size each epic with the people who will build it. Give **ranges**, never one number (Planning rule 23).

| Epic / PRD feature | Design (days) | Development (days) | QA (days) | Other (DevOps, firmware, AI evals) | Total low – high | Confidence | Main uncertainty |
|--------------------|---------------|--------------------|-----------|------------------------------------|------------------|------------|------------------|
| F-01 <name> | | | | | – | L / M / H | |
| **Project work** (setup and walking skeleton, Sprint Reviews, delivery notes, release, hand-over) | | | | | – | | |
| **Total** | | | | | **– ** | | |

Rules of thumb: project work is not free — count it. Track B adds hardware milestones, a test rig and field tests; track C adds the eval set and AI usage cost.

### A2. Team size and shape
| Role | Person (if known) | Share of time | Sprints needed |
|------|-------------------|---------------|----------------|
| Product Owner / Delivery Lead | | e.g. 30% | |
| Designer | | | |
| Tech Lead | | | |
| Developers (how many) | | | |
| QA Engineer | | | |
| Other (firmware, DevOps, AI) | | | |

- Check the team's **shared sprint capacity** across all projects ([README §6.6](../../README.md#66-working-rhythm-rules) rule 10): can we staff this without going above 100%?
- Duration = total effort ÷ team capacity per sprint. Write it as a date range.

### A3. Cost build-up
| Item | Low | High | Notes |
|------|-----|------|-------|
| People: effort × internal rate per role | | | |
| Contingency for risk (higher when confidence is low; e.g. 10–30%) | | | Based on A4 |
| Third-party costs (cloud, app store accounts, paid APIs, AI usage, devices, licenses) | | | Paid by client or re-billed? |
| **Total cost** | | | |
| **Price to the client** (cost + margin) | | | Approved by the Sponsor |

### A4. Risks and assumptions behind the numbers
| # | Risk or assumption | Effect on the estimate if wrong | In the assumptions log? |
|---|--------------------|---------------------------------|-------------------------|
| 1 | e.g. "Client provides all content by Sprint 2" | +1 sprint | yes |

---

## Part B — Proposal (sent to the client)

> Plain language, outcome first. Readable in 5 minutes by a non-technical decision-maker.

### B1. Your goal
What you told us you want to achieve, and how we will measure success (from the PRD).

### B2. What we will deliver
- The MVP features (Must list from the MVP workshop), in plain words
- What comes later (phase 2 list) and what is **not** included
- Deliverables: working product, source code, user guide, a delivery note every 2 weeks, hand-over at the end

### B3. How we will work
- Track and method (for example "2-week sprints; you see working software every 2 weeks")
- What we need from you: one decision-maker, feedback within <2> working days, content and accounts by <date>

### B4. Team
The roles who will work on your project (and names, if agreed).

### B5. Timeline
| Milestone | Date range |
|-----------|------------|
| Start | |
| First demo | |
| Go-live | |

### B6. Price options
| Option | What it includes | Price | Contract model |
|--------|------------------|-------|----------------|
| 1. MVP (recommended) | Must list | | Fixed price per phase |
| 2. MVP + <extra> | | | |
| 3. Flexible scope | Fixed team for <n> sprints; you choose the order | | Time and materials with a cap |

- Payment schedule; third-party costs not included (list them)
- Prices valid until: <date>

### B7. Why LumenVenture
2–3 sentences tied to **this** client's needs (for example "one team for device, cloud and app"). Only past work the client's NDA allows us to mention.

### B8. Next steps
1. You choose an option.
2. We send the **SOW** for signature (scope, deliverables, timeline, price, change and acceptance rules).
3. Kickoff and Sprint 1 within <n> days of signing.

---

## Acceptance
| Client accepted option | Date | Accepted by | SOW sent on |
|------------------------|------|-------------|-------------|
| | | | |
