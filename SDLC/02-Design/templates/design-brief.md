# Design Brief — <Feature or screen set>

> Write this **before** design work starts ([Design §4.9](../Design.md#49-uiux-design-and-prototypes), rules 27–30). It tells the designer what "good" means, so a design is approved or rejected **against written criteria**, not taste. Owner: Product Owner. Copy to `docs/design/briefs/<feature>.md` or the design ticket.

| Field | Value |
|-------|-------|
| Story / epic IDs | `REQ-…` / `EPIC-…` |
| Designer | <name> |
| **Approver (one person)** | <name: the PO; on client projects the client's named decision-maker> |
| Developer contact | <name> (checks every draft for build cost and limits) |
| QA contact | <name> (checks that states and errors are testable) |
| Needed by | <date>, at least **one sprint before** the build sprint (README §6.1) |
| Review turnaround | Approver answers within **2 working days** |

## 1. Problem and users
- Who uses this screen, on which device, and what are they trying to do?
- What happens today (current system or workaround)?

## 2. Acceptance criteria for the design
The approver judges the design **only** against these. Add more if needed.
- [ ] Covers every state: empty, loading, error, success, no permission, offline (mobile and IoT apps)
- [ ] Uses the project's design system components; any new component is named and justified
- [ ] Meets the **visual quality bar** from the project brief (reference apps, brand, "showcase" level or "tool" level)
- [ ] Works at 320 px wide and on desktop; touch targets at least 24 × 24 CSS px; text contrast at least 4.5:1 (WCAG 2.2 AA)
- [ ] Every text, label and error message is final (no "lorem ipsum")
- [ ] <feature-specific criterion>

## 3. Constraints
- Component library and its known limits (from the design-system ADR, Design rule 29)
- Data the back-end or device can actually provide; slow or missing data cases
- Brand assets, fonts, existing screens to stay consistent with

## 4. Review log (written feedback only)

| Round | Date | Approver | Decision | Reason, linked to a criterion above |
|-------|------|----------|----------|-------------------------------------|
| 1 | | | Approved / Changes needed | e.g. "Criterion 1: no error state for failed payment" |
| 2 | | | Approved / Escalated | After round 2, open points go to PO + Delivery Lead (rule 28) |

## 5. Hand-off to development (status: **Ready for dev**)
- [ ] Final design link (frame or page, not the whole file): <link>
- [ ] Assets exported; spacing, colors and fonts use design tokens
- [ ] Interactions and animations described (or a prototype link)
- [ ] Walk-through held with the developer and QA (15–30 min), questions answered in the ticket
- [ ] Linked from the story; the story's Definition of Ready box "design approved" is ticked
