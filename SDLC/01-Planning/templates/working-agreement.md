# Working Agreement — <Project name>

> Copy to `docs/working-agreement.md` at kickoff (README §2, step 5a). Written **by the whole team**, not by the lead alone. Owner: Delivery Lead. Review it in a Sprint Retrospective **at least every 3 sprints** (Kanban teams: monthly) and whenever a person joins. Keep it to **one page**; a rule nobody follows is fixed or removed.
> Why: research on team effectiveness (Google re:Work, "Understand team effectiveness") puts **psychological safety** first, then dependability, structure and clarity, meaning and impact. This page makes the first three visible. Rules: [README §6.6](../../README.md#66-working-rhythm-rules), rules 7–9.

**Last reviewed:** <YYYY-MM-DD> · **Next review due:** <YYYY-MM-DD> (every 3 sprints)

## 1. Our goal
- Product Goal / current Sprint Goal: <one sentence everybody can say>

## 2. How we communicate
- Questions and quick talks: <channel>. Answer within: <for example 4 working hours>
- Urgent problems: <on-call route / incident channel>, not the normal channel
- Decisions are written in: <ADR folder / decisions log / ticket>, never only in chat or on a call
- Core hours and time zones: <for example 10:00–15:00 UTC overlap>; outside them, write so that others can answer later (async-first)
- Meetings: <list: daily 15 min, planning, review, retro>; each has an agenda and ends with a summary with owners and dates

## 3. How we work
- Reviews: every pull request gets a reviewer within <1 working day>; nobody approves their own change; owners of risky areas (CODEOWNERS) are always included
- Definition of Done: [definition-of-done.md](../../03-Development/templates/definition-of-done.md)
- Who decides what: PO = what and order; TL and Developers = how; the team = who picks which task
- Disagreement: we write the options and reasons, the person responsible decides, we support the decision ("disagree and commit"), and record it as an ADR if it is hard to undo
- Pairing or mobbing: <when we use it: hard problems, onboarding>; breaks and solo time are fine

## 4. How we treat each other
- Asking for help or admitting a mistake is normal; we do **blameless** reviews of problems (what allowed it, not who)
- We say thanks for good work and share wins in <channel>
- Feedback is specific, kind and about the work
- Everyone can speak: quiet people and other time zones are asked for input in writing first

## 5. How we share knowledge
- At least two people can work on, deploy and operate every important part (bus factor ≥ 2): <list parts with only one expert>
- Demos or tech talks: <rhythm>, recorded for newcomers when the content allows (no production data, secrets, personal or client-confidential content)
- New joiner: a buddy, the onboarding checklist, one small first task within the first week
- Mentoring: <who mentors whom, how often>

## 6. Team health check (every ~3 sprints, 10 minutes in the retrospective)
Score 1–5 **anonymously** (poll tool or paper slips) and discuss the team average and the lowest two. Never trace a score to a person. Based on the five dynamics of effective teams:
| Statement | Score |
|-----------|-------|
| If I make a mistake on our team, it is not held against me (psychological safety) | |
| Teammates reliably finish quality work on time (dependability) | |
| I understand the goals, the plan and what is expected of me (structure and clarity) | |
| The work is personally meaningful to me (meaning) | |
| I understand how our work contributes to the organization's goals (impact) | |

**Changes agreed in the last review:** <date — change — owner>
