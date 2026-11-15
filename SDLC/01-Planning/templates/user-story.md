# Story: <short title> (<ID, e.g. REQ-07>)

**Epic:** <epic name>
**As a** <user/persona>, **I want** <goal>, **so that** <reason>.

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

## Non-functional notes
- Performance / security / accessibility / privacy points that apply to this story.

## Notes and links
- Design doc / ADR / API contract:
- Dependencies:

## Definition of Ready (all must be ticked before the sprint starts)
- [ ] Clear user value (the "so that" is real)
- [ ] Acceptance criteria are exact and testable (numbers, status codes, messages)
- [ ] Small enough to finish in one sprint (split it if not)
- [ ] Estimated by the team
- [ ] Dependencies and open questions resolved (or a spike planned)
- [ ] Design needs known (does it need a design doc / ADR / threat-model update?)
- [ ] Security and privacy impact considered
