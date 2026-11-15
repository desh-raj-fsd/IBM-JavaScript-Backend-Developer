# Product Requirements — <Project name> (version <x.y>)

> **Client-facing PRD (Product Requirements Document).** Copy to `docs/discovery/client-prd.md`. Owner: Product Owner.
> Write it in **plain words** for a non-technical reader: no code, no Gherkin, no jargon. Keep it to **3–6 pages**. Use screens from the prototype.
> It must **match** the internal [project brief](project-brief.md) (scope, MVP, assumptions). The detailed [user stories](user-story.md) are written from this PRD and carry the same feature IDs.

| Field | Value |
|-------|-------|
| **Client decision-maker** | |
| **LumenVenture Product Owner** | |
| **Version / date** | |
| **Status** | Draft / Sent for review / **Approved on <date>** |

## 1. The problem
<Two or three sentences: who has which problem today, and what it costs them.>

## 2. Goal and success
- **Goal:** <one sentence: what the product will do for its users>
- **We will know it works when:** <measurable result, for example "200 bookings per month by <date>">

## 3. Users
| User type | What they want to do | Device |
|-----------|----------------------|--------|
| | | |

## 4. How it works (main user journeys)
Describe each journey as simple steps, with a link or picture from the prototype.
1. **<Journey name, for example "Book an appointment">**
   1. The customer opens the app and chooses a service.
   2. …
   - Screens: <prototype link / image>

## 5. Features in the first version (MVP)
| ID | Feature | What it means for the user | Priority |
|----|---------|----------------------------|----------|
| F-01 | Sign up with email | A new customer can create an account with email and password. | Must |
| F-02 | | | Must / Should / Could |

**Simple examples (how we will check it works):**
- F-01: *If a customer uses an email that already has an account, they see "This email is already registered".*
- F-02: *…*

## 6. Not in this version (out of scope)
| Feature | Why not now | Maybe in |
|---------|-------------|----------|
| | | Phase 2 |

## 7. Quality expectations (in plain words)
| Area | Expectation |
|------|-------------|
| Speed | Pages open in under <2> seconds on a normal phone connection |
| Availability | The service works <99.5%> of the time (about <3.6> hours of downtime per month at most) |
| Security and privacy | Passwords are protected; personal data follows <GDPR / local law>; users can delete their account |
| Accessibility | Usable with screen readers and large text (<WCAG 2.2 AA>) |
| Devices | <for example: latest 2 versions of iOS and Android; Chrome, Safari, Edge> |

## 8. Assumptions (please check carefully)
Things we decided because they were not clear. **If one is wrong, cost or time may change.**
| ID | Assumption |
|----|------------|
| A-01 | |

## 9. What you provide
- <for example: logo and brand colors, texts for the app, test accounts for the payment provider, one person for feedback>

## 10. How we work together
- **Demo** of working software every **<2> weeks**; you give feedback within **<3> working days**.
- **Changes after approval:**
  - **Swap:** a new feature can replace one of the **same size** → price and date stay the same.
  - **Add:** if you want both, we write a **change request** with the extra cost and time, and start only after you approve it.
- **Acceptance:** before go-live you test the product (UAT — User Acceptance Testing) against the examples in section 5.

## 11. Open questions
| ID | Question | Who answers | By when |
|----|----------|-------------|---------|
| Q-01 | | | |

## 12. Approval
By approving, you agree that sections 5–10 describe the first version. Changes after this date follow section 10.

| Role | Name | Date | Decision |
|------|------|------|----------|
| Client decision-maker | | | Approved / Approved with comments / Not approved |
| LumenVenture Product Owner | | | |

## Change history
| Version | Date | What changed | Approved by |
|---------|------|--------------|-------------|
| 0.1 | | First draft | — |
