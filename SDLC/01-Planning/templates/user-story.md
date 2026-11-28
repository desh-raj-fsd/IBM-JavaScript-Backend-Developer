# Story: <short title> (<ID, e.g. REQ-07>)

| Field | Value |
|-------|-------|
| **Epic** | <epic name> |
| **Type** | Functional / External interface / Non-functional |
| **Priority** | Must / Should / Could / Won't (this time) |
| **Objective** | <OBJ-n — the key result this story helps move; or the source law / ASVS level / SLO for legal, security and operational needs> |
| **Source** | <who asked, how and when — e.g. "Moderator workshop, 2026-11-04"> |
| **Client PRD feature** (client projects) | <F-nn> |

**As a** <user/persona>, **I want** <goal>, **so that** <reason>.

## Description
- **Context:** why this story exists, what happens today (current screen, workflow or workaround), and who is affected.
- **What changes:** in plain words, what the user will be able to do after this story.
- **Out of scope for this story:** what it does **not** include (split it into another story if needed).
- Screenshots or examples of today's behavior (no real personal data).

## Design and technical links
| Link | Value |
|------|-------|
| **Approved design** (stories with screens) | <link to the frame or page, not the whole file> · Design brief: `docs/design/briefs/<feature>.md` · Status: **Ready for dev** (Design rule 30) |
| **Tech note** (over about 2 days, or new library / device / service) | <link or short note: approach, risks, what to spike> · Checked by Tech Lead: <name, date> |
| Design doc / ADR / API contract | <links, if any> |

## Acceptance criteria
```gherkin
Scenario: <happy path>
  Given <starting state>
  When <action>
  Then <exact, testable result>

Scenario: <error / edge case>
  Given <starting state>
  When <action>
  Then <exact, testable result>
```

## System rules (EARS — optional, for system behavior)
- When <trigger>, the <system> shall <response>.
- If <unwanted condition>, then the <system> shall <response>.

## Non-functional notes
- Performance / security / accessibility / privacy points that apply to this story — as **numbers**, not words like "fast" or "secure".

## Notes and links
- Dependencies:
- Assumptions (each with an owner and a date to confirm):

## Definition of Ready (all must be ticked before the sprint starts)
- [ ] Clear user value (the "so that" is real) and a linked **objective or source**
- [ ] Acceptance criteria are exact and testable (numbers, status codes, messages) — no vague words
- [ ] Passes the quality check: necessary, unambiguous, singular, feasible, verifiable, consistent ([Planning §4.13](../Planning.md#413-checking-and-confirming-requirements))
- [ ] Checked by a developer ("can I build it?") and a tester ("can I test it?")
- [ ] Small enough to finish in one sprint (split it if not)
- [ ] Estimated by the team
- [ ] Dependencies and open questions resolved (or a spike planned)
- [ ] Design needs known (does it need a design doc / ADR / threat-model update?)
- [ ] Security and privacy impact considered
- [ ] **Screens:** design is **Approved** in its design brief and linked in "Design and technical links" — never "we'll guess and fix later" (Planning rule 25, Design rule 30)
- [ ] **Over about 2 days, or new library / device / service:** tech note written, linked in "Design and technical links" and checked by the Tech Lead
- [ ] **QA reviewed** the acceptance criteria (refinement with product, development and QA)
- [ ] Inputs available: API keys, client content, test devices or hardware, accounts
