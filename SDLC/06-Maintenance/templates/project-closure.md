# Project Closure Report — <Project>

> Write this whenever a project or a large phase **ends for any reason**: delivered, paused, handed to another team, or **stopped** ([Maintenance rule 22](../Maintenance.md#65-rules)). A project that just "goes quiet" is not allowed. Owner: Delivery Lead; the Product Owner and Tech Lead fill in their parts. Keep in `docs/closure-report.md` and send the client a copy.

| Field | Value |
|-------|-------|
| End type | Delivered / Paused / Handed over / Stopped |
| Date | |
| Decision by | <Sponsor; client decision-maker on client projects> |
| Reason (paused or stopped) | |

## 1. What was delivered
- Features live, with links to the user guide and the last release notes
- Goals and key results (`OBJ-n`): reached / partly / not reached, with numbers
- Open items not delivered, and why

## 2. Hand-over checklist
- [ ] Repositories transferred or access confirmed for the client; default branch protected
- [ ] Cloud, app store, domain and device-registry ownership confirmed (see the [takeover audit](takeover-audit.md) table, section 1)
- [ ] Our staff access removed or reduced to the support agreement; shared credentials rotated
- [ ] Docs up to date: README, architecture, runbooks, user guide, release notes, SOPs
- [ ] Final build artifacts, firmware images and signing information handed over as agreed in the contract
- [ ] Support agreement or warranty period stated (or "none")
- [ ] Client signed the hand-over (name, date)

## 3. Time and money
- Estimate (range) vs. actual effort and duration; main reasons for the difference

## 4. Lessons learned (for the next project)
- What went well, what to change, and **which guide rule** should change (open a pull request, README §9)
- R&D, spikes and design explorations worth keeping → moved to the knowledge base (Maintenance rule 24), with links

## 5. Paused or stopped projects only
- How to restart: where the code, designs and decisions are, what is half-done
- Data kept or deleted (and the client's written instruction)
