# The 6 Phases of the SDLC — Modern Best Practices

How professional backend teams run **Planning, Design, Development, Testing, Deployment and Maintenance** today.

**Related course note:** [03 — Phases of the SDLC](course-1-introduction-to-software-engineering/module-1-the-software-development-lifecycle/notes/03-phases-of-the-sdlc.md) (the lecture version)

---

## 0. Jargon Translation (Read This First)

| Term | Official Definition | Simple Words | Analogy |
|------|--------------------|--------------|---------|
| **SDLC (Software Development Life Cycle)** | A systematic process to build high-quality software in a predictable time and budget. | The steps a team follows from idea to running software. | A recipe for a big meal. |
| **Waterfall** | A model where each phase is fully finished before the next starts, with no going back. | One straight pass: plan everything, then build everything, then test everything. | Water falling down steps. |
| **Agile** | A way of working in short loops that deliver small, working pieces of software and adapt to feedback. | Build a little, show it, learn, repeat. | Cooking one dish at a time and tasting each before the next. |
| **Sprint / Iteration** | A fixed time-box (usually 1–4 weeks) in which a team delivers a small set of features. | One short loop of work. | One lap of a running track. |
| **DevOps** | A culture and set of practices where development and operations work as one team, with heavy automation. | The people who build the software also release and run it. | A chef who also serves the food and hears what guests think. |
| **Backlog** | An ordered list of work items (features, bugs, tasks), most valuable first. | The team's "to-do list", always kept in order. | A shopping list sorted by "need most". |
| **Epic** | A large feature that is too big for one sprint and is split into user stories. | A big chunk of work. | "Renovate the kitchen". |
| **User story** | A short requirement written from the user's point of view: *"As a [user], I want [goal], so that [reason]."* | One small thing a user needs. | "Fit a new tap". |
| **Acceptance criteria** | Clear yes/no conditions a story must meet to be accepted. | The checklist that says "this story is done". | "Tap does not leak; hot and cold both work". |
| **Definition of Done (DoD)** | A team-wide checklist every item must pass before it counts as finished. | The team's quality rules for "done". | A restaurant's rule: "plate is clean, food is hot, order is correct". |
| **Definition of Ready (DoR)** | A checklist a backlog item must pass before the team can start it in a sprint. | "Is this story clear enough to start?" | Checking you have all ingredients before you start cooking. |
| **Persona** | A short, research-based profile of a typical user. | A pretend "typical user" with a name, goals and problems. | "Asha, 28, reads 3 books a month, wants honest reviews." |
| **Functional requirement** | A statement of what the system must do. | A thing the software does. | "The car must have brakes." |
| **Non-functional requirement** | A statement of how well the system must work (performance, security, availability, usability). | How fast, safe or reliable it must be. | "The car must stop from 100 km/h in under 40 m." |
| **MVP (Minimum Viable Product)** | The smallest version of a product that delivers real value and lets the team learn from real users. | The simplest useful first version. | A food truck before opening a full restaurant. |
| **Feasibility study** | An early check that a project is technically, economically, legally, operationally and time-wise possible. | "Can we, and should we, build this?" | Checking your budget and the land before building a house. |
| **Risk register** | A living list of project risks with likelihood, impact, mitigation and owner. | The team's "what could go wrong" list, with a plan for each. | A ship's list of dangers on the route and how to avoid each one. |
| **Traceability** | The ability to link each requirement to its design, code and tests. | Following one requirement all the way to its test. | A parcel tracking number. |
| **Gherkin** | A plain-language format (Given / When / Then) for writing acceptance criteria that tools can run as tests. | Test steps written like simple sentences. | A recipe card: "Given flour, when you add water, then you get dough." |
| **CI (Continuous Integration)** | Merging code into the main branch often, with an automated build and tests on every change. | A robot checks every change as soon as you push it. | A spell-checker that runs on every sentence you type. |
| **Trunk-based development** | A branching strategy where everyone merges small changes into the main branch at least daily. | Everyone works on one shared line of code, in small steps. | A relay team passing the baton often instead of one runner doing the whole race. |
| **Pull request (PR)** | A request to merge a set of code changes, where teammates review and CI checks them first. | "Please check my change before it goes in." | Handing your essay to a friend to proofread before you submit it. |
| **Code review** | Teammates reading and checking a change for correctness, security and clarity before it is merged. | A second pair of eyes on every change. | A co-pilot checking the pilot's flight plan. |
| **Linter** | A tool that checks code for errors and style problems without running it. | An automatic code checker. | A spell-checker for code. |
| **Conventional Commits** | A standard format for commit messages: `type(scope): summary`. | A fixed pattern for writing commit messages. | A fixed format for writing dates, so everyone reads them the same way. |
| **SemVer (Semantic Versioning)** | A version format `MAJOR.MINOR.PATCH` that tells users if a change is breaking, a new feature, or a fix. | Version numbers that mean something. | A traffic light: red = breaking, yellow = new, green = fix. |
| **Lockfile** | A file (`package-lock.json`) that records the exact version of every installed dependency. | A list that freezes exact package versions. | A recipe that names the exact brand and size of every ingredient. |
| **Parameterized query** | A database query where values are sent separately from the SQL text, so they can never change the query. | The safe way to put user input into SQL. | Filling a form's blanks instead of letting someone rewrite the form. |
| **Supply-chain attack** | An attack that hides malicious code inside a dependency or build tool you trust. | A poisoned package you install without knowing. | A bad ingredient from a supplier that ruins every dish. |
| **SBOM (Software Bill of Materials)** | A complete list of every component and version inside a piece of software. | The ingredient list of your software. | The ingredients label on food packaging. |
| **Event loop** | The single thread in Node.js that runs JavaScript and handles all requests, one task at a time. | Node's one worker that serves everyone. | One very fast waiter serving all tables — if he stops for one table, everyone waits. |
| **Pair programming** | Two developers working together on one task at one computer (or shared screen). | Two people, one keyboard. | A driver and a navigator in a rally car. |
| **CD (Continuous Delivery / Deployment)** | Every change that passes CI is automatically ready to release (Delivery) or released automatically (Deployment). | A robot moves good changes to the servers. | A conveyor belt from kitchen to table. |
| **Pipeline** | The automated chain of steps (build, test, scan, deploy) that every change goes through. | The assembly line for code. | A car factory line. |
| **Shift-left** | Moving testing and security work earlier in the timeline. | Test early, not at the end. | Checking ingredients before cooking, not after serving. |
| **TDD (Test-Driven Development)** | Writing a failing test first, then the code that makes it pass, then cleaning up. | Write the exam question before the answer. | Drawing the target before shooting the arrow. |
| **Verification vs. validation** | Verification: "did we build it right?" (against the spec). Validation: "did we build the right thing?" (against real needs). | Right *way* vs. right *thing*. | Following the recipe exactly vs. the guests actually liking the dish. |
| **Black-box / white-box testing** | Testing without looking at the code (black-box) vs. using knowledge of the code's internals (white-box). | Test from outside vs. from inside. | Test-driving a car vs. inspecting the engine. |
| **Regression test** | A test that checks old features still work after a change. | "Did we break anything that used to work?" | Re-checking all the lights after fixing one switch. |
| **Smoke test** | A quick, basic test that the build starts and the most important features work. | "Does it even turn on?" | Turning on a new appliance to see that it powers up, before testing every button. |
| **Exploratory testing** | Unscripted testing where a tester learns the app and designs tests while using it. | Testing by curious exploring. | A detective looking for clues, not following a checklist. |
| **Load test** | A test that measures speed and errors under expected (or higher) traffic. | "Is it fast enough when many people use it?" | Testing a bridge with many trucks at once. |
| **Test double (mock, stub, fake, spy)** | A replacement for a real dependency, used in a test. | A stand-in for the real thing. | A crash-test dummy instead of a real driver. |
| **Code coverage** | The share of code lines or branches that the tests run. | How much of the code the tests touch. | How many rooms of a house the inspector walked into. |
| **Mutation testing** | Making small deliberate changes to code to check that the tests notice. | Testing the tests. | A teacher adding a wrong answer to see if the student spots it. |
| **Flaky test** | A test that sometimes passes and sometimes fails with no code change. | An unreliable test. | A smoke alarm that goes off at random. |
| **Severity vs. priority** | Severity = technical impact of a bug; priority = how urgently to fix it. | How bad vs. how urgent. | A small stain on a wedding dress: low damage, but very urgent. |
| **Chaos engineering** | Deliberately injecting failures to prove a system can recover. | Breaking things on purpose, safely. | A fire drill. |
| **OpenAPI** | A standard YAML/JSON format that describes a REST (Representational State Transfer) API. | A machine-readable "menu" of your API. | A restaurant menu that both waiters and computers can read. |
| **ADR (Architecture Decision Record)** | A short document that records one architecture decision, its reasons and the options rejected. | A diary entry: "we chose X because Y". | A note in a car's service book explaining why a part was replaced. |
| **Threat modeling** | A structured way to find how a system could be attacked, and plan defenses. | Asking "how could a bad person abuse this?" | A security guard walking the building to find weak doors. |
| **HLD (High-Level Design)** | The big-picture design: main components, how they connect, and technology choices. | The map of the whole system. | A city map showing districts and main roads. |
| **LLD (Low-Level Design)** | The detailed design inside each component: modules, database tables, endpoints, error rules. | The detailed plan for one part. | The floor plan of one building, with every room. |
| **Quality attribute** | A measurable property of a system, such as performance, availability, security or maintainability. | How *well* the system works, not *what* it does. | A car's top speed, safety rating and fuel use. |
| **Modular monolith** | One deployable application split into strict internal modules with clear boundaries. | One app, but well-organized inside. | One big house with separate, lockable rooms. |
| **Microservices** | An architecture of many small services, each owning its data and deployed on its own. | Many small apps that talk over the network. | A street of small specialized shops instead of one supermarket. |
| **Stateless service** | A service that keeps no user data in its own memory between requests. | Any copy of the server can answer any request. | Any cashier can serve you, because your order is on the receipt, not in one cashier's head. |
| **Spike** | A short, time-boxed experiment to answer a technical question before committing to a design. | A quick test to learn something. | Testing one tile on the wall before tiling the whole bathroom. |
| **C4 model** | A way to draw architecture at four zoom levels: Context, Container, Component, Code. | Architecture diagrams that zoom in step by step. | Zooming a map from country → city → street → house. |
| **RFC (Request for Comments) / design doc** | A short document that proposes a design and asks the team for feedback before building. | "Here is my plan — please comment." | Sharing a draft travel plan with your friends before booking. |
| **Least privilege** | Giving every user, service and account only the permissions it needs. | Give only the keys someone really needs. | A cleaner gets the key to the office, not to the safe. |
| **Problem Details (RFC 9457)** | A standard JSON format for HTTP API errors (`type`, `title`, `status`, `detail`). | One standard shape for every error. | A standard accident-report form every insurer understands. |
| **Feature flag** | A setting that turns a feature on or off without deploying new code. | A light switch for a feature. | A shop that is built but has its door closed until opening day. |
| **Canary release** | Sending a small share of users to a new version first, then increasing it if all is well. | Test the new version on a few users first. | Miners took a canary into the mine to detect danger early. |
| **Blue-green deployment** | Running the old (blue) and new (green) versions side by side, then switching traffic. | Two copies; flip a switch to change; flip back if it breaks. | Two stages in a theater: prepare the next scene on the second stage. |
| **Rollback** | Returning production to the last good version. | "Undo" for a release. | Ctrl+Z. |
| **Deploy vs. release** | Deploy: new code is running on servers. Release: users can use the new feature. | Installing it vs. turning it on for users. | A new shop counter is installed overnight (deploy) but opens to customers next week (release). |
| **Progressive delivery** | Releasing changes gradually (canary, feature flags) while watching metrics, with automatic rollback. | Release step by step, watching carefully. | Opening a new road one lane at a time. |
| **Immutable image / digest** | A container image that is never changed after it is built; its digest (`sha256:…`) uniquely identifies its exact content. | A sealed, numbered package that is never repacked. | A sealed parcel with a unique tracking number. |
| **Multi-stage build** | A Dockerfile with several stages, where only the needed files are copied into the final image. | Build in a messy workshop, ship only the finished product. | Cooking in the kitchen but serving only the plate. |
| **Graceful shutdown** | Stopping a server by finishing current requests before exiting. | Finish serving, then close. | A shop that stops letting people in at closing time but serves everyone already inside. |
| **HPA (Horizontal Pod Autoscaler)** | A Kubernetes feature that adds or removes pods automatically based on load. | More copies when busy, fewer when quiet. | A supermarket opening more checkouts when the queue grows. |
| **IaC (Infrastructure as Code)** | Defining servers, networks and config in versioned code files instead of manual setup. | Infrastructure written as code in Git. | A building's blueprint that can rebuild the same building anywhere. |
| **GitOps** | Running deployments by changing a Git repository; a tool makes the cluster match Git automatically. | Git is the single source of truth for production. | A thermostat that keeps the room at the temperature written on the dial. |
| **OIDC federation (in CI)** | Letting a CI job exchange its identity for a short-lived cloud token, instead of storing long-lived keys. | No permanent passwords in the pipeline. | A visitor badge that expires tonight instead of a permanent office key. |
| **Roll-forward** | Fixing a bad release by quickly deploying a new, fixed version instead of going back. | Fix forward instead of undoing. | Patching a flat tire on the road instead of driving back home. |
| **DORA metrics** | Four key measures of software delivery: deployment frequency, lead time, change failure rate, time to restore. | Four numbers that show how well a team delivers. | A car's speed, fuel use, breakdown rate and repair time. |
| **Observability** | The ability to understand what a system is doing from its logs, metrics and traces. | Being able to "see inside" the running app. | A car dashboard plus a black-box recorder. |
| **SLO (Service Level Objective)** | A measurable reliability target, for example "99.9% of requests succeed". | A number that says "good enough" for users. | "The bus arrives on time 99 days out of 100". |
| **Postmortem (blameless)** | A written review after an incident about what happened and how to prevent it, without blaming people. | Learn from the failure, don't punish. | An airline investigating a near-miss to fix the process. |
| **Corrective / adaptive / perfective / preventive maintenance** | The four maintenance types: fix bugs / adapt to a changing environment / improve features / prevent future problems. | Fix it, keep it compatible, make it better, stop problems early. | A car: repair a flat tire, fit winter tires, add a better radio, change the oil. |
| **SLI (Service Level Indicator)** | The actual measurement of a service's behavior, such as the share of fast, successful requests. | The number you measure. | The bus's real on-time record. |
| **SLA (Service Level Agreement)** | A contract that promises customers a service level, often with penalties if it is missed. | The promise in the contract. | A delivery company refunding you if the parcel is late. |
| **Error budget** | The amount of failure an SLO allows (100% − SLO), used to balance speed and reliability. | How much "failing" you are allowed. | A monthly allowance: spend it on risky changes, stop when it is gone. |
| **Golden signals** | Four key metrics for a service: latency, traffic, errors, saturation. | The four numbers to watch first. | A car's speedometer, fuel, warning lights and engine temperature. |
| **On-call** | A rota where an engineer is responsible for responding to production alerts at any time. | The person "on duty" for the system. | The doctor on night duty at a hospital. |
| **Runbook** | A short guide that explains how to check and fix a known problem. | Step-by-step instructions for an alert. | The emergency card in an airplane seat pocket. |
| **MTTR (Mean Time To Restore)** | The average time to recover service after an incident. | How fast we fix outages. | How long the road stays closed after an accident. |
| **RPO / RTO** | RPO: maximum acceptable data loss. RTO: maximum acceptable downtime. | How much data, and how much time, we can lose. | How many pages of your work you could lose, and how long you can wait to get your laptop back. |
| **Hotfix** | An urgent, small fix released to production outside the normal release schedule. | An emergency fix. | A plumber called at night for a burst pipe. |
| **Strangler fig pattern** | Replacing a legacy system piece by piece behind a router until the old system can be removed. | Replace the old system slowly, part by part. | A new road built next to the old one, lane by lane, before the old one is closed. |
| **High cardinality (metrics)** | A metric label with very many possible values, creating huge numbers of time series. | Too many different label values. | Filing every receipt in its own folder instead of by month. |
| **Technical debt** | The future cost of shortcuts taken in code today. | Messy code you must "pay back" later. | Not washing dishes: easy now, harder tomorrow. |

---

## 1. The Big Idea: Same Six Jobs, Different Rhythm

- The **six phases** are the **six jobs** every software team must do. This is true in **every** model.
- What changed in the industry is **when and how often** the jobs happen.

| | **Waterfall way** (the lecture's model) | **Modern way** (Agile + DevOps) |
|---|---|---|
| **Order** | One pass, in a straight line | Many short loops |
| **Overlap** | None — each phase must finish first | Planned overlap (for example test while coding) |
| **Requirements** | All written up front in one big SRS (Software Requirements Specification) | Broad picture first, details just before building |
| **Testing** | After all coding is complete | During coding, on every push |
| **Release** | Once, at the end | Often — weekly, daily, or on every merge |
| **Who runs production** | A separate operations team | The same team that built it |
| **Feedback from users** | After the whole project | After every small release |
| **Cost of a wrong requirement** | Very high (found late) | Low (found in days) |

![Waterfall line versus the modern loop of the six phases](images/sdlc-modern-waterfall-vs-loop.svg)

```mermaid
flowchart TD
    BL["Backlog - ordered list of features and bugs"] --> P["1. Plan a small slice"]
    P --> D["2. Design the slice"]
    D --> DV["3. Develop - code plus tests together"]
    DV --> T["4. Test - CI runs all tests on every push"]
    T --> DP["5. Deploy - CD pipeline to staging then production"]
    DP --> M["6. Maintain - monitor, fix, learn"]
    M -->|new stories and bugs| BL
```

> **Remember:** the **"what"** (each phase's job) is universal. The **"when"** (strict order, no overlap) is Waterfall. Modern teams keep the "what" and change the "when".

---

## 2. Phase 1 — Planning: "Broad First, Detail Later"

### 2.1 The job (same in every model)

- Find out **what** to build, **for whom**, **why**, and with **what time and money**.
- **Other names:** some organizations call this phase **"requirements"**, **"strategy"** or **"analysis"**. Some split it into two stages (for example **feasibility** + **requirements analysis**).
- **Why it comes first:** every later phase depends on it. A wrong requirement makes everything built on top of it wrong — and the later it is found, the more it costs to fix.
- Consider the **eight planning factors**: users, purpose, data inputs and outputs, legal and regulatory compliance, risks, QA (Quality Assurance) requirements, human and financial resources, and schedule (see [2.3](#23-the-eight-planning-factors-then-and-now)).
- **The four core requirement steps are the same in every model.** Requirements are:
  1. **gathered** (collected from stakeholders),
  2. **analyzed** (checked: are they clear, possible, not conflicting?),
  3. **documented** (written down), and
  4. **prioritized** (ordered by importance: "must have" first).
- **Other core planning tasks from the lecture (also still true):**
  - **Estimate labor and material costs** and weigh them against **time constraints**.
  - **Identify project teams** and **propose the role** of each team member.
  - Build **prototypes** when stakeholders struggle to define requirements. Prototyping can also happen **in any later phase** when requirements need to be clarified again.
  - Combine the requirements into a document (the **SRS**) that **all stakeholders understand and approve**, with **developers involved** early.

### 2.2 The four core steps: Waterfall way vs. modern way

- **What stays the same:** all four steps still happen. They usually follow this order, but in practice they **loop**: analysis often shows a gap, so the team gathers again.
- **What changes:**
  - **Waterfall** does them **once**, for **all** requirements, at the start.
  - **Modern teams** do them **broadly once at the start**, then **again in every sprint**, in more detail for the next few items only.

| Step | Waterfall way (once, up front) | Modern way (start + every sprint) | Modern tools and methods |
|------|-------------------------------|-----------------------------------|--------------------------|
| **1. Gather** | Long interviews and workshops before any work starts | Kick-off workshops at the start, then continuous input: sprint reviews (demos), user feedback, analytics, support tickets | Story mapping workshops, user interviews, product analytics |
| **2. Analyze** | Analysts check the whole list once | Each story is checked in **backlog refinement**: is it clear, possible, testable, not in conflict with others? Developers and testers take part. | **INVEST** checklist (Independent, Negotiable, Valuable, Estimable, Small, Testable), spikes (short research tasks) |
| **3. Document** | One large SRS document, signed off | A **light SRS** or product brief for the big picture, plus **user stories with acceptance criteria** in a tracking tool. The documents change as the project learns. | Jira, GitHub Issues, Azure Boards, Markdown docs in Git |
| **4. Prioritize** | Fixed once in the SRS; changes need a formal change request | **Re-prioritized every sprint** by the product owner, based on value, risk and feedback | **MoSCoW** (Must, Should, Could, Won't), value vs. effort matrix |

**The other planning tasks, then and now:**

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **Estimate costs vs. time** | One detailed estimate for the whole project, fixed at the start | A rough range for the whole project, then **re-estimated every sprint** (story points, T-shirt sizes); the team's measured speed (**velocity**) makes forecasts better over time. Velocity is only for the team's own forecasting — never for comparing teams or people |
| **Identify teams and propose roles** | Roles split by phase (analysts, designers, coders, testers, operations) | **Small cross-functional teams** that own a product end to end; key roles: **product owner** (what and in which order), **Scrum Master** (a coach who helps the team follow Scrum and removes blockers — not a manager), and developers (who also test and run the service) |
| **Prototypes to find requirements** | A mock-up shown to the client during planning | Fast throwaway prototypes in days (Figma, quick demo apps), and real users trying early releases |
| **SRS approved by all, developers involved** | One formal sign-off of the full SRS | Stakeholders agree on the vision and priorities; **developers and testers join refinement** for every story; each story is "approved" when its acceptance criteria are agreed |

```mermaid
flowchart TD
    subgraph START["At project start - broad"]
        direction TB
        margin_1((" "))
        style margin_1 fill:none,stroke:none
        margin_1 ~~~ G1
        G1["Gather: vision, users, main features, constraints"] --> A1["Analyze: feasible, no conflicts"]
        A1 --> D1["Document: light SRS plus epics"]
        D1 --> P1["Prioritize: order the epics"]
    end
    subgraph SPRINT["Every sprint - detailed, only the next few items"]
        direction TB
        margin_2((" "))
        style margin_2 fill:none,stroke:none
        margin_2 ~~~ G2
        G2["Gather: feedback from demos, users, analytics"] --> A2["Analyze: backlog refinement - clear and testable?"]
        A2 --> D2["Document: user stories plus acceptance criteria"]
        D2 --> P2["Prioritize: product owner reorders the backlog"]
    end
    P1 --> G2
    P2 -->|next sprint| G2
```

> **Remember:** the four steps are **timeless**. Waterfall runs them **once, in full detail**. Modern teams run them **broadly at the start, then in detail every sprint**.

### 2.3 The eight planning factors: then and now

The lecture lists eight factors to consider. All eight are still required today. What changed is **how** teams work them out.

| # | Factor | Question it answers | Waterfall way | ✅ Modern way |
|---|--------|---------------------|---------------|---------------|
| 1 | **Users of the solution** | Who will use it? | A list of user types in the SRS | **Personas** (short profiles of typical users) built from **user research**; for APIs, also the **client apps and services** that call it |
| 2 | **Overall purpose** | Why does it exist? | A purpose statement in the SRS | A **product vision** plus **measurable success metrics** (KPIs — Key Performance Indicators, or OKRs — Objectives and Key Results), for example *"500 reviews posted in the first month"* |
| 3 | **Data inputs and outputs** | What data goes in and comes out? | Data tables described in the SRS | A first **data model** and **API contract** sketch; **data classification** (which data is personal or sensitive — PII, Personally Identifiable Information); how long data is kept (**retention**) |
| 4 | **Legal and regulatory compliance** | Which laws or rules apply? | Checked once by the legal team | Checked early **and** for every new feature: privacy laws (**GDPR** — General Data Protection Regulation, **CCPA** — California Consumer Privacy Act), **accessibility** (**WCAG** — Web Content Accessibility Guidelines), **open-source licenses**, and AI rules (for example the **EU AI Act**) if the product uses AI. Under GDPR, high-risk data processing needs a **DPIA** (Data Protection Impact Assessment) |
| 5 | **Risk identification** | What could go wrong? | A risk list written once | A **risk register** that is **reviewed regularly**: each risk has a **likelihood**, an **impact**, a **mitigation** (plan to reduce it) and an **owner**. Security risks are found early with **threat modeling** |
| 6 | **QA requirements** | What quality level is required? | Quality goals written in words | **Non-functional requirements** written as **numbers** (SLOs — Service Level Objectives), a **test strategy**, and a team **Definition of Done** |
| 7 | **Human and financial resources** | Who works on it, and how much money is there? | Staff and budget fixed for the whole project | A **stable cross-functional team**; budget reviewed often; **cloud costs** estimated and watched from the start (**FinOps** — financial operations for the cloud) |
| 8 | **Project scheduling** | When is each part due? | A **Gantt chart** with fixed **milestones** for the whole project | A **roadmap** (goals by month or quarter), a **release plan**, and **sprints**; fixed dates are kept for real deadlines (for example a legal date), and **scope** is what flexes |

#### 2.3.1 Risk register example

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| Spam reviews flood the site | High | Medium | Login required; rate limiting; one review per user per book | Backend lead |
| Personal data leak | Low | Very high | Hash passwords; encrypt data; least-privilege database users; security tests in CI | Security champion |
| Key developer leaves | Medium | High | Code review, shared ownership, written ADRs | Team lead |
| Cloud bill grows too fast | Medium | Medium | Budget alerts; right-size servers; review costs monthly | Product owner |

### 2.4 Often-missed parts of a good plan

These are not named in the lecture, but professional teams treat them as part of planning.

#### 2.4.1 Stakeholder identification

- **List every stakeholder** before gathering requirements: users, customers, product owner, developers, testers, operations, security, legal, support.
- Note what each one **needs** and how much **influence** they have. Missing a stakeholder (for example the legal team) means missing their requirements.

#### 2.4.2 Feasibility study

Before committing, check if the project **can** and **should** be done:

| Type | Question |
|------|----------|
| **Technical** | Can we build it with the technology and skills we have? |
| **Economic** (cost-benefit) | Is the value bigger than the cost? |
| **Legal** | Is it allowed? |
| **Operational** | Will people actually use it, and can we run it? |
| **Schedule** | Can it be done in the time we have? |

#### 2.4.3 Functional vs. non-functional requirements

Every requirements list must contain **both** kinds:

| Kind | What it describes | Examples (Book Review API) |
|------|-------------------|-----------------------------|
| **Functional** | **What** the system does | "A logged-in user can add a review." "Anyone can list reviews for a book." |
| **Non-functional** (quality attributes) | **How well** it does it | **Performance:** 95% of requests in under 200 ms. **Availability:** 99.9%. **Security:** passwords hashed. **Scalability:** handle 10x traffic. **Accessibility:** WCAG 2.2 AA for the website. **Maintainability:** 80% test coverage. |

- Teams often forget the non-functional ones — and these are usually the hardest to add later.

#### 2.4.4 Scope, MVP, assumptions, constraints and dependencies

- **Scope:** write what is **in scope** and also what is **out of scope**. "Out of scope" stops arguments later.
- **MVP (Minimum Viable Product):** the smallest version that delivers real value and lets you learn from real users. Build it first.
- **Assumptions:** things you believe are true but have not proven (for example "users already have an account"). Check them early.
- **Constraints:** fixed limits (budget, deadline, required technology, laws).
- **Dependencies:** things you need from others (a payment provider's API, another team's service).

#### 2.4.5 Definition of Ready and traceability

- **Definition of Ready (DoR):** a checklist a story must pass **before** a sprint can start it — for example "clear acceptance criteria, small enough for one sprint, no open blockers".
- **Traceability:** give each requirement an **ID** (for example `REQ-07`) and link it to its design, code (commits, PRs) and tests. You can then prove every requirement was built and tested. In regulated industries, a **traceability matrix** is required.

#### 2.4.6 Change management

Requirements **will** change. The plan must say **how** changes are handled:

| | Waterfall way | Modern way |
|---|---|---|
| **How a change is requested** | A formal **change request** | A new or edited item in the **backlog** |
| **Who decides** | A **change control board** | The **product owner**, with the team |
| **When it is built** | After re-planning, re-estimating and re-approval | In a coming sprint, based on its priority |

#### 2.4.7 Writing acceptance criteria that can be tested

A common modern format is **Gherkin** (*Given / When / Then*). It is readable by non-developers, and tools (for example Cucumber) can run it as an automated test.

```gherkin
# features/add-review.feature — acceptance criteria for REQ-07
Feature: Add a book review
  As a reader, I want to rate a book from 1 to 5,
  so that other readers can judge it.

  Scenario: Valid rating is saved
    Given I am logged in as "asha"
    When I post a review with rating 4 for book "978-0132350884"
    Then the response status is 201
    And the review is listed for that book

  Scenario: Rating outside 1 to 5 is rejected
    Given I am logged in as "asha"
    When I post a review with rating 6 for book "978-0132350884"
    Then the response status is 400

  Scenario: Guest cannot post
    Given I am not logged in
    When I post a review with rating 4 for book "978-0132350884"
    Then the response status is 401
```

**What happens if... acceptance criteria are vague?**

```gherkin
# ❌ Not testable — "fast" and "good" mean different things to different people
Scenario: Reviews work well
  Then the page loads fast and ratings look good
# ✅ Write numbers and exact results: "responds in under 200 ms", "status is 400".
```

#### 2.4.8 Using AI tools in planning

- AI assistants can help **draft** user stories, find **missing edge cases**, and **summarize** interview notes.
- **A human must check every requirement.** AI can invent needs nobody asked for, or miss legal and business rules it does not know.
- Do **not** paste confidential customer data into AI tools that your company has not approved.

### 2.5 How modern teams do it

- **Know the whole map first, but draw the detailed roads only just before you travel them.**
  - At the start, gather **high-level** requirements: goals, users, main features, constraints, risks. This is a **light SRS** (or a "product brief").
  - Split them into **epics** and place them in a **backlog**.
  - Each sprint, **refine** the top items into detailed **user stories** with **acceptance criteria** (this is called **backlog refinement**).
  - Feedback from each release **adds, changes or removes** backlog items.
- **Why not write every detail on day one?**
  - Many requirements **cannot be known** until users see working software.
  - Detailed requirements **go stale**: what you wrote in month 1 is often wrong by month 6.
- **When a full SRS is still the right choice:** fixed-price contracts, regulated industries (banking, medical, aviation, government), or safety-critical systems. The international standard for writing one is **ISO/IEC/IEEE 29148** (it replaced the older **IEEE 830**).

| Level | When it is written | Detail | Example (Book Review API) |
|-------|-------------------|--------|---------------------------|
| **Vision and scope** | Project start | Low | "Readers can share and read book reviews." |
| **Epics** | Project start (roughly) | Medium | "User accounts", "Reviews", "Search" |
| **User stories** | Just before building | High | "As a reader, I want to rate a book 1–5, so that others can judge it." |
| **Acceptance criteria** | With the story | Very high | "Rating 0 or 6 → HTTP 400. Not logged in → HTTP 401." |

![Requirements funnel: vision, epics, user stories, acceptance criteria](images/sdlc-modern-requirements-funnel.svg)

### 2.6 Modern planning practices checklist

- **Prioritize by value:** methods like **MoSCoW** (Must have, Should have, Could have, Won't have this time).
- **Secure by design:** write security and privacy as real requirements from day one.
  - Example: *"Passwords are hashed with bcrypt or argon2."* *"Personal data follows GDPR (General Data Protection Regulation)."*
  - Use the **OWASP (Open Web Application Security Project) Top 10** to learn the most common web risks, and the **OWASP ASVS (Application Security Verification Standard)** as the detailed checklist to write testable security requirements from.
- **Measurable quality targets (SLOs):** *"99.9% of requests succeed; 95% answer in under 200 ms."* Not *"the API must be fast"*. An **SLA (Service Level Agreement)** is the **contract** version promised to a customer, usually looser than the internal SLO.
- **Cheap prototypes:** clickable mock-ups (for example in Figma) or a quick throwaway demo, to get feedback within days.
- **Estimate in ranges, re-plan often:** use story points or T-shirt sizes (S, M, L), and update the plan every sprint.

```mermaid
flowchart TD
    V["Vision and scope - light SRS"] --> E["Epics in the backlog"]
    E --> R["Backlog refinement each sprint"]
    R --> S["Detailed user stories plus acceptance criteria"]
    S --> B["Build in the sprint"]
    B --> F["Release and get feedback"]
    F -->|add, change, remove items| E
```

### 2.7 Planning is "done enough" when...

- [ ] All **stakeholders** are identified, and they agree on the **vision, scope and success metrics**.
- [ ] The project is **feasible** (technical, economic, legal, operational, schedule).
- [ ] All **eight planning factors** are answered.
- [ ] **Functional and non-functional** requirements exist (non-functional ones written as numbers).
- [ ] **In scope / out of scope**, the **MVP**, assumptions, constraints and dependencies are written down.
- [ ] A **risk register** exists, with owners.
- [ ] **Cost and time** are estimated (as ranges), and the **team and roles** are set.
- [ ] The **backlog** is prioritized, and the first stories meet the **Definition of Ready**, with testable **acceptance criteria**.
- [ ] Requirements have **IDs** for traceability.
- [ ] The **change process** is agreed.
- [ ] (Only where required) the full **SRS** is approved by all stakeholders.

---

## 3. Phase 2 — Design: "Lightweight, Versioned, API-First"

### 3.1 The job

- Decide **how** the system will be built to meet the requirements: its parts, data, APIs, security, how it scales, and how it runs in production.
- **Core tasks from the lecture (still true in every model):**
  1. Use the **requirements** (from the SRS or the stories) as the input.
  2. **Several team members work together** to design the **software architecture**.
  3. The architecture is **reviewed by stakeholders and the team**.
  4. **Prototypes** can be designed — a **preliminary mock-up of the system, or parts of it**, used for **demonstration**.
  5. The result is written down as a **design document**, which developers use in the **development phase** (planners also use it to assign coding tasks).
- **Why design before coding:** a mistake fixed in a diagram costs minutes. The same mistake found in code costs days, and in production it can cost data and customers.
- **Two levels of design** (classic SDLC terms, still used in interviews and in large companies):

  | Level | What it covers | Who mainly does it | Book Review API example |
  |-------|----------------|-------------------|--------------------------|
  | **HLD (High-Level Design)** | The big picture: main components, how they talk, technology choices, where data lives | Architect / senior engineers | "Express API in containers on Kubernetes, PostgreSQL database, Redis cache, JWT login" |
  | **LLD (Low-Level Design)** | The details inside each component: modules, classes or functions, database tables, endpoint contracts, error rules | Developers who will build it | "`reviews` table with unique (user_id, isbn); `POST /books/{isbn}/reviews` returns 201/400/401/409" |

### 3.2 Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way (once, up front) | Modern way (per slice, kept up to date) |
|-----------|-------------------------------|------------------------------------------|
| **Input: requirements** | The complete, signed SRS | The light SRS for the big picture + the user stories (with **non-functional requirements**) for this slice |
| **Team designs the architecture** | Architects design the whole system (HLD and all LLD) before coding | **"Just enough" design up front:** the HLD and the hard-to-change decisions are made early; the **LLD for each feature** is done just before it is built, by the developers who will build it, with an architect's help |
| **Review by stakeholders and team** | Formal review gates (often a **preliminary** and a **critical design review**) | Design docs and ADRs reviewed as **pull requests**; small, frequent reviews; a wider **architecture review** only for big or risky changes |
| **Prototypes** | A mock-up to show the client | Clickable mock-ups, **mock servers generated from OpenAPI**, or a short **spike** (time-boxed experiment) to test a risky idea |
| **Design document** | One large document, rarely updated | Small **versioned** docs in Git: OpenAPI contract, ADRs, **C4 diagrams as code**, short design docs (RFCs) — updated when the system changes |
| **Link to requirements** | A traceability matrix in the design document | Each design doc, ADR or endpoint references the **requirement or story IDs** it serves (for example `REQ-07`) |

### 3.3 How modern teams do it

- **API-first design:** write the API contract in **OpenAPI** **before** writing code.
  - Frontend and backend teams can work **in parallel**.
  - Tools create docs, mock servers, client code and validation tests from the same file.
- **ADRs (Architecture Decision Records) in Git:** one short Markdown file per important decision (*context*, *decision*, *rejected options*, *consequences*). By convention an accepted ADR is **not rewritten**; when the decision changes, a new ADR **supersedes** it, so the history of decisions stays visible.
- **Design docs as pull requests:** the design is reviewed like code, and it **changes with the system** — it is not a one-time document.
- **Threat modeling** for each significant new feature: "How could an attacker abuse this?" (A simple method is **STRIDE**: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.)
- **Design for operations:** plan health checks, logs, metrics, traces, configuration through **environment variables**, and secrets through a **secret manager** — before coding.
- **Start simple:** a well-structured **modular monolith** is often better than many microservices for a new product. Split services only when there is a real need (see [3.4.2](#342-choose-an-architecture-style)).
- **Decide late on things that are easy to change; decide early on things that are hard to change** (for example the database, the public API, the identity provider).

```yaml
# openapi.yaml — design-phase contract written before any Express code
openapi: 3.1.0
info: { title: Book Review API, version: 1.0.0 }
paths:
  /books/{isbn}/reviews:
    post:
      summary: Add a review (REQ-07)
      operationId: addReview
      security: [{ bearerAuth: [] }]          # login required (defined below)
      parameters:
        - { name: isbn, in: path, required: true, schema: { type: string } }
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/NewReview' }
      responses:
        '201': { description: Review created }
        '400': { $ref: '#/components/responses/Problem' }   # invalid input
        '401': { $ref: '#/components/responses/Problem' }   # not logged in
        '409': { $ref: '#/components/responses/Problem' }   # already reviewed this book
components:
  securitySchemes:
    bearerAuth: { type: http, scheme: bearer, bearerFormat: JWT }
  schemas:
    NewReview:
      type: object
      required: [rating]
      additionalProperties: false              # reject unknown fields
      properties:
        rating: { type: integer, minimum: 1, maximum: 5 }
        text:   { type: string, maxLength: 2000 }
    Problem:                                   # RFC 9457 "Problem Details" error format
      type: object
      properties:
        type:   { type: string }
        title:  { type: string }
        status: { type: integer }
        detail: { type: string }
  responses:
    Problem:
      description: Error
      content:
        application/problem+json:
          schema: { $ref: '#/components/schemas/Problem' }
```

**What happens if... you reference a security scheme you never define?**

```yaml
# ❌ "bearerAuth" is used but not declared under components.securitySchemes
security: [{ bearerAuth: [] }]
# Validators (for example Redocly or Spectral) report an error, generated docs show
# no login method, and generated clients cannot send the token.
# ✅ Always declare it: components.securitySchemes.bearerAuth (see above).
```

```markdown
<!-- docs/adr/0003-use-postgresql.md — an ADR (Architecture Decision Record) -->
# ADR 0003: Use PostgreSQL for reviews

**Status:** Accepted (2026-11-10)
**Context:** Users, books and reviews are closely related and are often read together
(joins). Rule REQ-09: one review per user per book. The team knows SQL well.
**Decision:** Use PostgreSQL. Enforce REQ-09 with a UNIQUE constraint on (user_id, isbn).
**Rejected options:**
- MongoDB — would also work (it supports compound unique indexes), but our data is
  relational and most queries join users, books and reviews.
- A separate search engine — not needed for the expected traffic.
**Consequences:** One database to run and back up. Revisit if search traffic grows 10x.
```

```mermaid
flowchart TD
    ST["User stories plus acceptance criteria plus NFRs"] --> HLD["High-level design: components and tech choices"]
    HLD --> LLD["Low-level design: schema, endpoints, modules"]
    ST --> TM["Threat model the feature"]
    LLD --> API["Write OpenAPI contract"]
    TM --> ADR["Record key decisions as ADRs"]
    API --> ADR
    ADR --> PR["Review design as a pull request"]
    PR --> BUILD["Frontend and backend build in parallel from the contract"]
```

### 3.4 The design areas a complete design must cover

The lecture says "develop the software architecture". In practice, a complete backend design answers questions in **all** of these areas.

#### 3.4.1 Non-functional requirements drive the architecture

- **Functional** requirements decide **what** components exist. **Non-functional** requirements (quality attributes) decide **how** they are built.
- Every important design choice should point back to a quality attribute:

| Quality attribute (from planning) | Example target | Typical design choices ("tactics") |
|-----------------------------------|----------------|------------------------------------|
| **Performance** | 95% of requests < 200 ms | Database indexes, caching (Redis), pagination, avoid N+1 queries |
| **Availability** | 99.9% uptime | Several instances behind a load balancer, health checks, no single point of failure, backups |
| **Scalability** | Handle 10x traffic | **Stateless** API servers (no session in memory), horizontal scaling, queues for slow work |
| **Security** | Protect personal data | Authentication + authorization design, encryption, least privilege, input validation, rate limiting |
| **Maintainability** | Easy to change | Clear module boundaries, layers (routes → services → repositories), tests, ADRs |
| **Observability** | Find problems in minutes | Structured logs, metrics, tracing (OpenTelemetry), request IDs |
| **Cost** | Fit the cloud budget | Right-sized resources, autoscaling, managed services vs. self-hosted trade-off |

- **Trade-offs are normal.** For example, a cache improves performance but can show **slightly old data**. Write the trade-off down in an ADR.

#### 3.4.2 Choose an architecture style

| Style | What it is | Good when | Watch out for |
|-------|-----------|-----------|---------------|
| **Monolith** | One application, one deployment | Small team, new product | Can become a "big ball of mud" without clear modules |
| **Modular monolith** | One deployment, but strict internal modules (reviews, users, books) | **Default choice for most new products** | Needs discipline to keep module boundaries |
| **Microservices** | Many small services, each with its own data and deployment | Many teams that must release independently; parts with very different scaling needs | Network failures, distributed data, much more DevOps work |
| **Serverless** | Functions run by the cloud on demand (AWS Lambda, Azure Functions) | Spiky or low traffic, event processing | Cold starts, vendor lock-in, harder local testing |
| **Event-driven** | Services communicate through events on a broker (Kafka, RabbitMQ) | Work that can happen later (emails, notifications, analytics) | Eventual consistency, harder debugging |

- These styles can be **combined** — for example a modular monolith that sends events to a serverless function for emails.

#### 3.4.3 Data design

- **Choose the database by access patterns** — how the data will be read and written — not by habit. (See [7 Database Laws](7-Database-Laws-of-Senior-Backend-Developer.md).)
- Design the **schema**: tables or collections, fields, types, relations.
- **Enforce business rules in the database too** (NOT NULL, UNIQUE, FOREIGN KEY, CHECK), not only in the code.
- Plan **indexes** for the most common queries.
- Plan **migrations**: every schema change is a versioned script, written to be **backward compatible**.
- Plan **data protection**: which fields are personal data, encryption, backups, retention and deletion (GDPR "right to erasure").

```sql
-- migrations/0004_create_reviews.sql — data design for REQ-07 and REQ-09
CREATE TABLE reviews (
  id          BIGSERIAL PRIMARY KEY,
  user_id     BIGINT      NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- delete reviews with the user (GDPR erasure)
  isbn        VARCHAR(17) NOT NULL REFERENCES books(isbn),
  rating      SMALLINT    NOT NULL CHECK (rating BETWEEN 1 AND 5),         -- REQ-07 enforced by the database
  text        VARCHAR(2000),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT one_review_per_user_per_book UNIQUE (user_id, isbn)           -- REQ-09
);

-- Most common query: "list reviews for a book, newest first"
CREATE INDEX idx_reviews_isbn_created ON reviews (isbn, created_at DESC);
```

**What happens if... the "one review per user" rule lives only in the code?**

```javascript
// ❌ Check-then-insert: two requests from the same user at the same moment
const existing = await db.query('SELECT 1 FROM reviews WHERE user_id=$1 AND isbn=$2', [userId, isbn]);
if (existing.rowCount === 0) {
  await db.query('INSERT INTO reviews (user_id, isbn, rating) VALUES ($1,$2,$3)', [userId, isbn, rating]);
}
// Both requests see "no review yet" and BOTH insert → duplicate reviews (a race condition).

// ✅ Let the UNIQUE constraint decide, and turn the error into HTTP 409
try {
  await db.query('INSERT INTO reviews (user_id, isbn, rating) VALUES ($1,$2,$3)', [userId, isbn, rating]);
} catch (err) {
  if (err.code === '23505') {               // PostgreSQL code for "unique_violation"
    return res.status(409).json({ title: 'You already reviewed this book', status: 409 });
  }
  throw err;                                 // any other error goes to the error middleware
}
```

#### 3.4.4 API design

(See [8 API Laws](8-API-Laws-of-Senior-Backend-Developer.md) for details.)

- **Resources, not actions:** `POST /books/{isbn}/reviews`, not `POST /createReview`.
- **Correct HTTP methods and status codes** (201 created, 400 bad input, 401 not logged in, 403 not allowed, 404 not found, 409 conflict).
- **One consistent error format** for every endpoint — the standard is **RFC 9457 "Problem Details"** (`application/problem+json`).
- **Pagination** for every list endpoint (`?limit=20&cursor=...`).
- **Idempotency** for retries: `PUT` and `DELETE` are idempotent by design; for `POST` payments or orders, accept an **`Idempotency-Key`** header.
- **Versioning and evolution plan:** add fields without breaking clients; use a new version (for example `/v2`) only for breaking changes; announce deprecations.

#### 3.4.5 Security design

(See [7 Authentication Concepts](7-Authentication-Concepts-Every-Senior-Developer-Should-Know.md) for details.)

- **Authentication:** how users prove who they are (sessions, JWT, OAuth 2.0 / OpenID Connect).
- **Authorization:** who may do what — check **ownership** on the server for every request (for example only the author can delete a review).
- **Least privilege:** every user, service and database account gets only the permissions it needs.
- **Defense in depth:** several layers of protection (validation, auth, rate limiting, database constraints), so one mistake is not enough for an attack.
- **Secure defaults:** deny by default; HTTPS everywhere; secure cookie flags; no secrets in code.
- **Encryption:** in transit (TLS — Transport Layer Security) and at rest (encrypted disks and backups); passwords **hashed** (bcrypt, argon2), never encrypted or stored as plain text.
- Use the **STRIDE** threat model results and the **OWASP ASVS** requirements as the checklist.

#### 3.4.6 Reliability design

- **Timeouts** on every call to another service or database — never wait forever.
- **Retries with backoff** (wait longer each time) only for safe, idempotent operations.
- **Circuit breakers** to stop calling a service that is failing (see [10 Backend Design Patterns](10-Backend-Design-Pattern-Laws-of-Senior-Engineers-and-Architects.md)).
- **Graceful degradation:** if the "recommended books" service is down, still show the reviews.
- **Queues** for slow or unreliable work (sending emails) so the user does not wait.
- **Backups and a restore test** — a backup you never restored is not a backup.

#### 3.4.7 Integrations and build vs. buy

- List every **external system** (payment provider, email service, identity provider) and design an **adapter** for each, so it can be replaced later.
- **Build vs. buy:** do not build what is not your core business. Login, payments and email are usually **bought** (managed services); your book-review logic is **built**.

#### 3.4.8 Diagrams: the C4 model

The **C4 model** is the most common way to draw software architecture today. It has four zoom levels, like a map:

| Level | Shows | Audience |
|-------|-------|----------|
| **1. Context** | The system as one box, with its users and external systems | Everyone, including non-technical stakeholders |
| **2. Container** | The deployable parts: API, database, cache, frontend | Developers, architects, operations |
| **3. Component** | The main modules inside one container | Developers |
| **4. Code** | Classes or functions (usually generated by tools, rarely drawn) | Developers |

- Keep diagrams **as code** (Mermaid, PlantUML, Structurizr) in Git, so they are reviewed and updated with the system.

![C4 model levels for the Book Review API: context, container, component](images/sdlc-modern-c4-design.svg)

```mermaid
flowchart TD
    subgraph CTX["Level 1 - Context"]
        direction TB
        margin_1((" "))
        style margin_1 fill:none,stroke:none
        margin_1 ~~~ R
        R["Reader"] --> SYS["Book Review System"]
        SYS --> IDP["Identity provider - external"]
        SYS --> MAIL["Email service - external"]
    end
    subgraph CON["Level 2 - Containers"]
        direction TB
        margin_2((" "))
        style margin_2 fill:none,stroke:none
        margin_2 ~~~ WEB
        WEB["Web app - React"] -->|HTTPS JSON| API["API - Node.js and Express"]
        API -->|SQL| DB[("PostgreSQL")]
        API -->|cache| RD[("Redis")]
        API -->|events| Q["Queue"]
    end
    SYS -.->|zoom in| WEB
```

#### 3.4.9 UI/UX design and prototypes

- Even for a backend course, the full SDLC design phase includes the **user experience**: **wireframes** (simple screen sketches), **mock-ups**, and clickable **prototypes** (for example in Figma).
- Use a **design system** (shared components and styles) so all screens look and behave the same.
- Design for **accessibility** (WCAG) from the start — adding it later is expensive.
- The lecture's design-phase **prototype** (a preliminary mock-up for demonstration) fits here: show it to stakeholders before building.

#### 3.4.10 The design document (RFC) template

Many companies write a short design doc, often called an **RFC (Request for Comments)**, for each significant feature:

```markdown
# Design: Book ratings (REQ-07, REQ-09)

## Context and problem        — why are we doing this?
## Goals and non-goals        — what is in, and what is explicitly out
## Proposed design            — HLD diagram, LLD: schema, endpoints, modules
## Alternatives considered    — other options and why they lost
## Security and privacy       — threat model results, personal data
## Reliability and operations — failure cases, monitoring, alerts
## Rollout and migration      — feature flag, migration steps, rollback plan
## Testing plan               — how we will prove it works
## Open questions             — what we still need to decide
```

#### 3.4.11 Using AI tools in design

- AI assistants can **suggest options**, **review a design for missing failure cases**, and **draft diagrams or OpenAPI files**.
- **A human owns every decision.** AI may suggest patterns the system does not need, or tools that do not fit your constraints. Record the final decision and the reasons in an ADR.
- If the product **itself uses an AI model**, design for it explicitly: answers can differ each time (plan **evaluation tests**), model calls are slow and cost money (plan **timeouts, caching and budgets**), and user text can try to trick the model (**prompt injection**) — so **authorization must always be checked by your server, never by the model**.

### 3.5 Design is "done enough" when...

- [ ] The **HLD** is agreed: components, technology choices and an **architecture style**, with a C4 context and container diagram.
- [ ] Important decisions are recorded as **ADRs**, each linked to the **quality attributes** it serves.
- [ ] The **LLD** for the next slice exists: **schema** (with constraints and indexes), **API contract** (OpenAPI, error format, pagination), module boundaries.
- [ ] A **threat model** was done, and the security design covers authentication, authorization, least privilege and encryption.
- [ ] **Reliability** is planned: timeouts, retries, failure behavior, backups.
- [ ] **Operations** are planned: logs, metrics, traces, health checks, configuration and secrets.
- [ ] **Integrations** have adapters; build-vs-buy is decided.
- [ ] A **rollout, migration and rollback** plan exists.
- [ ] The design links back to the **requirement IDs** it serves.
- [ ] The design was **reviewed** by the team (and stakeholders for big changes), and **prototypes** were shown where useful.

---

## 4. Phase 3 — Development: "Small Changes, Automated Rules"

### 4.1 The job

- Turn the design into **working, readable, secure, tested code** that the next developer can change easily.
- **Other names:** the **"building"** phase or the **"implementation"** phase.
- **Core tasks from the lecture (still true in every model):**
  1. Coding starts from a **design** (the design document or the contract for this slice).
  2. **Project planners use the design to determine and assign coding tasks**.
  3. Developers use **programming tools**, **programming languages** and **software stacks**.
  4. Developers follow the organization's **standards and guidelines**.

### 4.2 Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **Start from a design** | Coding starts only when the **whole** design document is complete | Coding starts when the design for **this slice** is ready (for example the OpenAPI contract is agreed) |
| **Determine and assign tasks** | A project manager assigns all tasks at the start | The **team** splits stories into tasks in **sprint planning**; developers **pull** tasks from a board (Scrum or Kanban) |
| **Tools, languages, stacks** | Chosen once for the whole project | Chosen early, recorded in ADRs; the dev setup is **reproducible** for everyone (`.nvmrc`, dev containers, Docker Compose, `package.json` scripts) |
| **Follow standards and guidelines** | A written style guide that people must remember | Standards **enforced automatically**: ESLint, Prettier, type checks, pre-commit hooks, branch protection, required code review |

### 4.3 How modern teams do it

- **Trunk-based development:** short-lived branches, merged into `main` within a day or two.
- **Small pull requests (PRs):** easy to review, easy to test, easy to undo. Many teams aim for a few hundred changed lines at most.
- **Required code review:** at least one teammate approves every PR (see [4.4.3](#443-code-review)).
- **Standards enforced by tools, not memory:**

  | Tool | What it enforces |
  |------|------------------|
  | **ESLint** (v9 uses `eslint.config.js`, the "flat config") | Code rules and common bug patterns |
  | **Prettier** | One code format for everyone |
  | **TypeScript / JSDoc types** | Correct data shapes before the code runs |
  | **Husky + lint-staged** | Run checks before each commit |
  | **Branch protection** | No merge if CI fails or review is missing |
  | **CODEOWNERS** file | The right people are asked to review each part of the code |

- **Secure coding:**
  - **No secrets in code** — use environment variables or a secret manager; commit a `.env.example` with fake values, and add `.env` to `.gitignore`.
  - **Validate all input** at the boundary (for example with `zod` or `express-validator`) — and **reject unknown fields**.
  - **Lock dependencies** with `package-lock.json`; install with `npm ci` in CI.
- **Use an LTS (Long-Term Support) Node.js line that is still supported** (check the release schedule on nodejs.org; pin it in `.nvmrc`, CI and the Dockerfile, and upgrade before it reaches end-of-life) and keep Express up to date (Express 5 passes errors from rejected promises in async handlers to the error middleware automatically).
- **AI coding assistants** (Claude Code, GitHub Copilot): useful for speed, but **the developer stays responsible** (see [4.4.11](#4411-using-ai-coding-assistants-well)).
- **Feature flags:** merge unfinished features safely, hidden behind a flag.

```javascript
// src/routes/reviews.js — validate input at the boundary, errors in one standard format
const express = require('express');
const { z } = require('zod');                         // schema validation library
const reviewService = require('../services/reviewService');

const router = express.Router();

// Schema mirrors the OpenAPI contract from the design phase.
// .strict() REJECTS unknown fields (plain z.object() would silently drop them).
const ReviewInput = z.object({
  rating: z.number().int().min(1).max(5),
  text: z.string().max(2000).optional(),
}).strict();

router.post('/books/:isbn/reviews', async (req, res) => {
  const parsed = ReviewInput.safeParse(req.body);     // never trust client input
  if (!parsed.success) {
    // RFC 9457 Problem Details — the same error shape as every other endpoint
    return res.status(400).type('application/problem+json').json({
      type: 'https://api.example.com/problems/invalid-input',
      title: 'Invalid input',
      status: 400,
      detail: parsed.error.issues.map((i) => `${i.path.join('.')}: ${i.message}`).join('; '),
    });
  }
  // Business rules live in the service layer, not in the route
  const review = await reviewService.addReview(req.user.id, req.params.isbn, parsed.data);
  res.status(201).json(review);
  // In Express 5, if addReview() rejects, the error goes to the error middleware automatically
});

module.exports = router;
```

**What happens if... you hard-code a secret?**

```javascript
// ❌ The password is now in Git history. Deleting the line later does NOT remove it
//    from old commits, forks or clones.
const db = connect('postgres://admin:SuperSecret123@prod-db:5432/app');

// ✅ Read it from the environment; set it in CI/CD or a secret manager
const db2 = connect(process.env.DATABASE_URL);
// If a secret was ever committed: ROTATE it (create a new one, disable the old one) at once.
// Removing it from history is a second step, not a replacement for rotation.
```

### 4.4 Industry practices the lecture does not cover

#### 4.4.1 Branching strategies

| Strategy | How it works | Good for | Watch out for |
|----------|--------------|----------|---------------|
| **Trunk-based development** | Everyone merges small changes into `main` at least daily; unfinished work hidden behind feature flags | Teams with good CI and frequent releases — **the common modern default** | Needs strong automated tests |
| **GitHub Flow** | Short feature branch → PR → review → merge to `main` → deploy | Web apps and APIs with continuous delivery | Branches must stay short-lived |
| **GitFlow** | Long-lived `develop` and `main`, plus feature, release and hotfix branches | Software with planned, versioned releases (installed apps, libraries) | Heavy process; painful merges; slow for web services |

#### 4.4.2 Commits and versioning

- **Small, focused commits** with clear messages. A common standard is **Conventional Commits**: `type(scope): summary`.
- **Semantic Versioning (SemVer)** — `MAJOR.MINOR.PATCH`:
  - **MAJOR:** breaking change (clients must change).
  - **MINOR:** new feature, backward compatible.
  - **PATCH:** bug fix, backward compatible.
- Conventional Commits can **generate the changelog and the next version number automatically** (tools like semantic-release or release-please).

```bash
git commit -m "feat(reviews): add rating 1-5 to book reviews (REQ-07)"
git commit -m "fix(reviews): return 409 when user already reviewed the book"
git commit -m "docs(api): document 409 response in openapi.yaml"
# feat = MINOR bump, fix = PATCH bump, "BREAKING CHANGE:" in the body = MAJOR bump
```

#### 4.4.3 Code review

- **Purpose:** find bugs, share knowledge, keep the code consistent — **not** to argue about style (tools handle style).
- **What reviewers check:**
  - Does it do what the story and acceptance criteria say?
  - Is it **correct** in edge cases and error cases?
  - Is it **secure** (input validation, authorization, no secrets, safe queries)?
  - Is it **tested**, and are the tests meaningful?
  - Is it **readable**, with good names and simple flow?
  - Does it follow the **design** (layers, API contract, ADRs)?
- **Good review habits:** review within hours, not days; comment on the code, never the person; separate "must fix" from "suggestion" (many teams prefix optional comments with `nit:`).

```markdown
<!-- .github/pull_request_template.md — every PR gets this checklist -->
## What and why
Closes #42 (REQ-07). Adds rating 1–5 to reviews.

## How to test
`npm test` · manual: POST /books/{isbn}/reviews with rating 6 → 400

## Checklist
- [ ] Tests added or updated
- [ ] OpenAPI contract updated
- [ ] No secrets, no console.log left behind
- [ ] Database migration is backward compatible
- [ ] Docs / CHANGELOG updated if needed
```

#### 4.4.4 Code structure and coding principles

- **Layered structure** (from the design): **routes/controllers** (HTTP only) → **services** (business rules) → **repositories** (database only). Each layer can be tested and changed alone.
- **Principles every senior developer is expected to know:**

  | Principle | Meaning |
  |-----------|---------|
  | **KISS** (Keep It Simple, Stupid) | The simplest solution that works is usually the best. |
  | **DRY** (Don't Repeat Yourself) | One rule should live in one place. (But a little duplication is better than the wrong shared abstraction.) |
  | **YAGNI** (You Aren't Gonna Need It) | Do not build features "just in case". |
  | **SOLID** | Five object-oriented design rules; the most used is **Single Responsibility**: one module, one reason to change. |
  | **Boy Scout Rule** | Leave the code a little cleaner than you found it. |

- More rules with examples: [7 Coding Laws of Senior Developer](7-Coding-Laws-of-Senior-Developer.md) and [10 Backend Design Patterns](10-Backend-Design-Pattern-Laws-of-Senior-Engineers-and-Architects.md).

```text
src/
├── app.js                  # builds the Express app (no listen) — easy to test
├── server.js               # starts the server: app.listen(...)
├── config.js               # reads and VALIDATES environment variables
├── routes/reviews.js       # HTTP: parse, validate, call service, send response
├── services/reviewService.js   # business rules (one review per user per book)
├── repositories/reviewRepo.js  # SQL only
├── middleware/auth.js      # JWT check
├── middleware/errors.js    # one error handler → Problem Details JSON
└── lib/logger.js           # structured logger
test/
├── unit/
└── integration/
```

#### 4.4.5 Configuration: fail fast at startup

- Follow the **Twelve-Factor App** rule: **config lives in the environment**, not in the code.
- **Validate config when the app starts.** If something is missing, crash **immediately** with a clear message — not hours later on the first request.

```javascript
// src/config.js — validate environment variables once, at startup
const { z } = require('zod');

const Env = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().int().default(3000),       // env vars are strings; coerce to number
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),                    // too-short secrets are rejected
});

const result = Env.safeParse(process.env);
if (!result.success) {
  console.error('Invalid configuration:', result.error.issues.map((i) => i.path.join('.')).join(', '));
  process.exit(1);                                   // fail fast: do not start a broken server
}

module.exports = result.data;
```

#### 4.4.6 Error handling and logging in code

- **One central error middleware** turns every error into the standard error format. Routes do not build error responses by hand for unexpected errors.
- **Structured logs** (JSON) with a fast logger like **pino**, including a **request ID** so one request can be followed through all logs.
- **Never log secrets or personal data** (passwords, tokens, full card numbers).
- **Never send stack traces to the client** in production.

```javascript
// src/middleware/errors.js — register LAST: app.use(errorHandler)
const logger = require('../lib/logger');

function errorHandler(err, req, res, next) {
  const status = err.status || 500;
  logger.error({ err, reqId: req.id, path: req.originalUrl }, 'request failed'); // full details in logs
  res.status(status).type('application/problem+json').json({
    type: 'about:blank',
    title: status === 500 ? 'Internal Server Error' : err.message, // no internals leak to the client
    status,
  });
}

module.exports = errorHandler;
```

#### 4.4.7 Node.js-specific pitfalls

| Pitfall | What goes wrong | Fix |
|---------|-----------------|-----|
| **Blocking the event loop** | One slow sync task (`fs.readFileSync`, big `JSON.parse`, heavy loop, `bcrypt.hashSync`) freezes **every** request | Use async APIs; move CPU-heavy work to **worker threads** or a queue |
| **Unhandled promise rejections** | Since Node 15, an unhandled rejection **crashes the process** | Always `await` inside `try/catch` or let Express 5 / the error middleware handle it |
| **Forgotten `await`** | Code continues before the database write finishes; errors are lost | ESLint rules such as `no-floating-promises` (typescript-eslint) |
| **Memory leaks** | Caches or listeners that grow forever | Limit cache size (LRU — Least Recently Used), remove listeners, watch memory metrics |
| **No graceful shutdown** | Deploys cut off requests in the middle | On `SIGTERM`, stop accepting new requests, finish current ones, close the database pool, then exit |

#### 4.4.8 Dependencies and supply-chain security

- **Choose packages carefully:** active maintenance, many users, small size, a clear license that your company allows (MIT, Apache-2.0, BSD are usually fine; check **copyleft** licenses like GPL with your legal team).
- **Fewer dependencies = smaller attack surface.** Do not add a package for a 3-line function.
- **Lockfile + `npm ci`** so every machine installs the **exact** same versions.
- **Automated updates and scanning:** Dependabot or Renovate, `npm audit`.
- **Supply-chain attacks are real:** typosquatting (a fake package with a similar name) and hijacked maintainer accounts. Check names carefully; prefer packages with **npm provenance**; be careful with packages that run **install scripts**.
- **SBOM (Software Bill of Materials):** a list of every component in your software; required by many enterprise and government customers.

#### 4.4.9 Secure coding checklist (code level)

| Risk | Secure code habit |
|------|-------------------|
| **SQL / NoSQL injection** | Always use **parameterized queries** (`$1`, `?`) or a safe ORM; never build queries with string concatenation |
| **Broken access control** (the #1 OWASP risk) | Check **ownership/permissions on the server** for every request (for example only the author can delete a review) |
| **XSS (Cross-Site Scripting)** | Escape output; set a **Content-Security-Policy**; never put raw user HTML into pages |
| **Weak headers** | Use **helmet** to set secure HTTP headers |
| **Brute force / abuse** | **Rate limiting** on login and write endpoints |
| **CORS (Cross-Origin Resource Sharing) mistakes** | Allow only known origins; never `*` together with credentials |
| **Passwords** | Hash with **bcrypt** or **argon2** (async versions) |
| **Sensitive data in errors and logs** | Generic messages to clients; redact secrets in logs |

```javascript
// ❌ SQL injection: isbn = "1' OR '1'='1" returns every row
db.query(`SELECT * FROM reviews WHERE isbn = '${req.params.isbn}'`);

// ✅ Parameterized query: the driver sends the value separately from the SQL
db.query('SELECT * FROM reviews WHERE isbn = $1', [req.params.isbn]);
```

#### 4.4.10 Local development environment

- **"Works on my machine" must not happen.** Every developer gets the same setup in minutes:
  - `.nvmrc` (Node version), `npm ci`, `.env.example`.
  - **Docker Compose** for the database, cache and other services.
  - **Seed data** and a one-command start (`npm run dev`).
  - Optional **dev containers** for a fully identical editor environment.

```yaml
# compose.yaml — start local dependencies with: docker compose up -d
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app_local_only     # local-only password, never used in production
      POSTGRES_DB: book_reviews
    ports: ["5432:5432"]
  cache:
    image: redis:7
    ports: ["6379:6379"]
```

#### 4.4.11 Using AI coding assistants well

- **Give context:** the story, acceptance criteria, the design and the relevant files.
- **Read every line** of the generated code. Check for invented (non-existent) packages or APIs, missing error handling, and security holes.
- **Tests and review are not optional** for AI code — the same CI, review and security scans apply.
- **Never paste secrets** or confidential customer data into tools your company has not approved.
- Watch for **licensing**: follow your company's policy on AI-generated code.
- Keep AI changes **small**, like any other PR.

#### 4.4.12 Collaboration and documentation

- **Pair programming** (two developers, one task) and **mob/ensemble programming** (the whole team, one task) spread knowledge and catch mistakes early.
- **Docs as code:** a **README** (what it is, how to run it, how to test it), API docs generated from OpenAPI, JSDoc on public functions, ADRs, and a **CHANGELOG** — all in Git and reviewed in PRs.
- **Comments explain *why*, not *what*.** The code shows *what*.

### 4.5 Development is "done" when... (a typical Definition of Done)

- [ ] The code meets the story's **acceptance criteria** and follows the **design** (API contract, layers, ADRs).
- [ ] **Unit and integration tests** are written and pass in CI.
- [ ] **Lint, format and type checks** pass.
- [ ] **Security checks** pass: input validated, authorization checked, no secrets, parameterized queries, dependency scan clean.
- [ ] Errors go through the **central error handler**; logs are structured with no sensitive data.
- [ ] The **PR is small**, has a clear description, and is **approved** by at least one reviewer.
- [ ] **Docs** (README, OpenAPI, CHANGELOG) are updated where needed.
- [ ] Database **migrations** are backward compatible.
- [ ] Unfinished user-facing work is hidden behind a **feature flag**.
- [ ] The change is **merged to `main`** and deployable.

---

## 5. Phase 4 — Testing: "Shift-Left, Automate, Pyramid"

### 5.1 The job

- Prove the software is **stable**, **secure**, and **meets the requirements** — and find problems as **early and cheaply** as possible.
- **Core tasks from the lecture (still true in every model):**
  1. Code is **thoroughly tested**: **stable**, **secure**, and **meets the requirements** (the SRS or the acceptance criteria).
  2. Testing is **manual**, **automated**, or a **hybrid** of both.
  3. Large projects may have **dedicated testing (QA — Quality Assurance) teams**.
  4. **The bug cycle:** bugs are **reported**, **tracked**, **fixed**, and the code is **retested** until it is stable.
  5. Testing happens at several **levels**: **unit**, **integration**, **system**, **acceptance**.
- **Two questions testing must answer** (a classic interview topic):

  | | **Verification** | **Validation** |
  |---|---|---|
  | **Question** | "Did we build the product **right**?" | "Did we build the **right** product?" |
  | **Checks against** | The specification / design / acceptance criteria | The real needs of users and stakeholders |
  | **Examples** | Code review, unit and integration tests, contract tests | Acceptance testing / UAT, usability tests, beta testing |

### 5.2 Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **When testing happens** | After all coding is complete | **During** coding (shift-left), on **every push** in CI, and some checks **in production** (shift-right) |
| **Manual / automated / hybrid** | Mostly manual test scripts | **Hybrid, mostly automated**: automated tests for every rule; manual **exploratory testing** for usability and unexpected cases |
| **Who tests** | A separate QA team at the end | **Developers** write unit and integration tests; **QA engineers** work inside the team: test strategy, end-to-end automation, exploratory testing. Quality is the **whole team's** job |
| **Report → track → fix → retest** | Bug reports in a spreadsheet or tool, fixed in a later round | Bugs tracked in Jira / GitHub Issues with **severity and priority**; each fix comes with a **regression test**; CI **retests everything automatically** |
| **Testing levels** | Run one after another, each as its own stage | **All levels run in the pipeline**, in pyramid proportions; acceptance criteria are often automated |

### 5.3 How modern teams do it

- **Shift-left testing:** testing starts **while** coding, not after.
- **TDD (Test-Driven Development)** cycle:
  1. **Red** — write a test; it fails.
  2. **Green** — write the smallest code that passes.
  3. **Refactor** — clean up; the test proves nothing broke.
- **CI runs every test on every push and PR.** A red build blocks the merge.
- **The test pyramid:** many fast unit tests, fewer integration tests, few end-to-end tests. The lecture's four levels map onto it like this:

  | Level (lecture) | What it tests | Speed | How many | Node.js tools |
  |-----------------|---------------|-------|----------|---------------|
  | **Unit** | One function or module alone | Milliseconds | Many | `node:test`, Jest, Vitest |
  | **Integration** | Parts together (route + service + real database) | Seconds | Some | Supertest, Testcontainers (real database in Docker) |
  | **System** | The **whole** system, end to end — **functional** (E2E user flows) **and non-functional** (performance, security, reliability) | Minutes | Few | Playwright (E2E), k6 (load), OWASP ZAP (security) |
  | **Acceptance** | Does it meet the user's needs? | — | Per story | Automated acceptance criteria (for example Gherkin/Cucumber) + customer/product owner review on staging (UAT) |

- **Pyramid vs. "testing trophy":** some teams (especially in JavaScript) prefer the **testing trophy**, which puts **more weight on integration tests**, because they give high confidence for their cost. Both agree on the main rule: **many fast tests, few slow ones, and no ice-cream cone** (mostly manual and E2E tests — slow and fragile).
- **Contract testing:** checks that a provider and its consumers still agree on the API. Two common forms:
  - **Schema validation:** responses are checked against the **OpenAPI** contract in tests.
  - **Consumer-driven contracts** (for example **Pact**): each client publishes what it expects, and the provider's CI checks it still delivers that — useful between microservices.
- **Automated security testing (DevSecOps):**

  | Check | What it does | Example tools |
  |-------|-------------|---------------|
  | **SAST (Static Application Security Testing)** | Scans source code for unsafe patterns | CodeQL, Semgrep |
  | **Dependency / SCA (Software Composition Analysis)** | Finds npm packages with known vulnerabilities | `npm audit`, Dependabot, Snyk |
  | **Secret scanning** | Finds passwords and keys in commits | GitHub secret scanning, gitleaks |
  | **DAST (Dynamic Application Security Testing)** | Attacks the running app in a test environment | OWASP ZAP |
  | **Container image scanning** | Finds vulnerable OS packages in Docker images | Trivy, Grype |

- **Shift-right testing:** some checks continue **in production** — canary releases, synthetic monitoring, feature flags and chaos experiments (see [5.4.10](#5410-shift-right-testing-in-production)).
- **Regression tests for every bug:** each fixed bug gets a test, so if the bug ever comes back, CI **catches it at once**.

![The test pyramid: many unit tests, some integration tests, few end-to-end tests](images/sdlc-modern-test-pyramid.svg)

```javascript
// test/unit/rating.test.js — TDD: these tests were written BEFORE isValidRating existed
const test = require('node:test');
const assert = require('node:assert');
const { isValidRating } = require('../../src/services/rating');

test('accepts whole numbers 1 to 5', () => {
  for (const r of [1, 2, 3, 4, 5]) assert.strictEqual(isValidRating(r), true);
});

test('rejects edge cases from the acceptance criteria', () => {
  for (const r of [0, 6, 4.5, '5', null]) assert.strictEqual(isValidRating(r), false);
});
```

**What happens if... you only test the happy path?**

```javascript
// ❌ Passes even if the code wrongly accepts rating 99
test('rating works', () => assert.strictEqual(isValidRating(3), true));
// The bug escapes to production and is found by users — the most expensive place.
```

### 5.4 Industry practices the lecture does not cover

#### 5.4.1 Ways to classify tests

| Classification | Meaning | Example |
|----------------|---------|---------|
| **Static testing** | Checking **without running** the code | Code review, linting, type checking, SAST |
| **Dynamic testing** | Checking **by running** the code | Unit, integration, E2E, load tests |
| **Black-box testing** | Testing inputs and outputs **without** looking at the code | QA sends requests to the API and checks responses |
| **White-box testing** | Testing **with knowledge of** the code's internal paths | A developer writes tests to cover every `if` branch |
| **Functional testing** | Does it do the **right thing**? | Rating 6 → HTTP 400 |
| **Non-functional testing** | Does it do it **well enough**? | 95% of requests under 200 ms at 500 users |

#### 5.4.2 Common test types (and when they run)

| Type | Purpose | When |
|------|---------|------|
| **Smoke test** | "Does the build start and do the most basic things work?" | After every build and every deployment |
| **Sanity test** | A quick, narrow check that one specific fix or feature works | After a small fix |
| **Regression test** | Old features still work after a change | Every CI run |
| **Exploratory test** | A tester freely explores the app to find unexpected problems | During each sprint, by humans |
| **Performance / load test** | Speed under expected traffic | Before big releases, and regularly |
| **Stress / spike / soak test** | Behavior beyond normal load / sudden load / load for many hours (finds memory leaks) | Before big events or launches |
| **Security / penetration test** | Experts try to break in | Regularly and before major releases (often required by customers) |
| **Accessibility test** | Can people with disabilities use it (WCAG)? | Automated checks in CI (for example axe) + manual checks |
| **Alpha / beta test** | Real users try a pre-release version (internal = alpha, external = beta) | Before general availability |

#### 5.4.3 Non-functional testing: a load test example

```javascript
// load/reviews.k6.js — run with: k6 run load/reviews.k6.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 200,                         // 200 virtual users at the same time
  duration: '2m',
  thresholds: {
    http_req_duration: ['p(95)<200'], // the SLO from planning: 95% of requests under 200 ms
    http_req_failed: ['rate<0.001'],  // fewer than 0.1% errors (99.9% success)
  },
};

export default function () {
  const res = http.get('https://staging.example.com/books/9780132350884/reviews');
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);                         // each user waits 1 second between requests
}
// If a threshold fails, k6 exits with an error, so the CI pipeline fails too.
```

#### 5.4.4 Writing good tests

- **AAA pattern:** **Arrange** (set up data) → **Act** (do one thing) → **Assert** (check the result).
- **FIRST** principles: tests are **F**ast, **I**ndependent (no order dependence), **R**epeatable (same result every time), **S**elf-validating (pass/fail with no human check), **T**imely (written with or before the code).
- **Test behavior, not implementation:** test what the API returns, not which private function was called. Then refactoring does not break the tests.
- **One reason to fail:** each test checks one behavior, with a name that says what it checks.

```javascript
// test/integration/reviews.test.js — integration test with Supertest (AAA pattern)
const test = require('node:test');
const assert = require('node:assert');
const request = require('supertest');
const app = require('../../src/app');          // the app WITHOUT app.listen()

test('POST /books/:isbn/reviews rejects rating 6 with 400 Problem Details', async () => {
  // Arrange
  const token = await loginAsTestUser();         // helper creates a user and returns a JWT

  // Act
  const res = await request(app)
    .post('/books/9780132350884/reviews')
    .set('Authorization', `Bearer ${token}`)
    .send({ rating: 6 });

  // Assert
  assert.strictEqual(res.status, 400);
  assert.match(res.headers['content-type'], /application\/problem\+json/);
  assert.strictEqual(res.body.status, 400);
});
```

#### 5.4.5 Test doubles: mocks, stubs, fakes, spies

| Double | What it does | Example |
|--------|--------------|---------|
| **Stub** | Returns a fixed answer | `getBook()` always returns one test book |
| **Mock** | Checks that it was called in the expected way | "`sendEmail` was called once with the author's address" |
| **Spy** | Records calls to a real function | Count how many times the logger was called |
| **Fake** | A simple working version | An in-memory repository instead of PostgreSQL |

- **Mock at the boundaries** (email provider, payment API, clock) — not your own business logic.
- **Prefer a real database in integration tests** (Testcontainers) over mocking the database: many bugs live in SQL, constraints and transactions.

```javascript
// test/unit/reviewService.test.js — mock the email adapter (an external boundary)
const test = require('node:test');
const assert = require('node:assert');
const { createReviewService } = require('../../src/services/reviewService');

test('notifies the book author after a new review', async (t) => {
  const email = { send: t.mock.fn(async () => {}) };            // mock: records calls
  const repo = { insert: async (r) => ({ id: 1, ...r }) };       // fake repository
  const service = createReviewService({ repo, email });          // dependencies injected

  await service.addReview(7, '9780132350884', { rating: 5 });

  assert.strictEqual(email.send.mock.callCount(), 1);           // called exactly once
});
```

#### 5.4.6 Test data and environments

- **Never use real production personal data** in tests. Use **synthetic** data (generated, for example with a library like Faker) or properly **anonymized** data.
- **Each test creates its own data** and does not depend on other tests (use factories or fixtures; reset the database between tests or run each test in a transaction that is rolled back).
- **Ephemeral preview environments:** many teams spin up a temporary environment **per pull request**, so reviewers and QA can test the change before merging. It is deleted after the merge.

#### 5.4.7 Code coverage and its limits

- **Coverage** = the share of code lines or branches that tests run. Node.js has it built in: `node --test --experimental-test-coverage` (Jest and Vitest also report it).
- **Branch coverage** (every `if`/`else` path) says more than line coverage.
- **Coverage is a warning light, not a goal.** 100% coverage does not mean the tests check anything useful. Many teams use a minimum (for example 80%) to catch **untested areas**, not to prove quality.
- **Mutation testing** (for example **Stryker**) measures test **quality**: it makes small changes ("mutants") to the code, such as turning `>=` into `>`. If no test fails, the tests are too weak.

#### 5.4.8 Flaky tests

- A **flaky test** sometimes passes and sometimes fails **with no code change**. It destroys trust in CI.
- **Common causes:** depending on time or dates, test order, shared data, real network calls, race conditions, fixed `sleep()` waits.
- **Fixes:** control the clock with fake timers, isolate data, mock external services, wait for **conditions** instead of fixed times. **Quarantine** a flaky test (move it out of the blocking suite) and fix it quickly — never just "re-run until green".

```javascript
// ❌ Flaky: fails when the test runs exactly at midnight, or in another time zone
test('review date is today', () => {
  const review = createReview();
  assert.strictEqual(review.date, new Date().toISOString().slice(0, 10));
});

// ✅ Control time with node:test fake timers (Date mocking needs Node 20.11+)
test('review date uses the current time', (t) => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-11-10T09:00:00Z') });
  const review = createReview();
  assert.strictEqual(review.date, '2026-11-10');
});
```

#### 5.4.9 Bugs: severity, priority and lifecycle

- **Severity** = how bad the **technical impact** is. **Priority** = how **urgently** it must be fixed. They are different:

  | Example | Severity | Priority |
  |---------|----------|----------|
  | Payment page crashes for everyone | Critical | Highest — fix now |
  | Company logo wrong on the home page | Low | High — very visible |
  | Crash in a rarely used admin export | High | Medium |
  | Typo in a help page nobody reads | Low | Low |

- **Bug lifecycle:** New → Triaged → In progress → Fixed → Verified (retested) → Closed. If it appears again → **Reopened**.
- **A good bug report** contains: title, environment and version, **steps to reproduce**, **expected** result, **actual** result, logs/screenshots, severity.

```markdown
**Title:** POST /books/:isbn/reviews returns 500 when text is longer than 2000 chars
**Environment:** staging, api v1.5.0
**Steps:** 1. Log in  2. POST a review with rating 4 and 2,500-character text
**Expected:** 400 Problem Details "text: too long"
**Actual:** 500 Internal Server Error (log reqId 9f2c…)
**Severity:** Medium   **Priority:** High (any user can trigger it)
```

#### 5.4.10 Shift-right: testing in production

- **Synthetic monitoring:** a robot runs key user flows (log in, post review) every few minutes against production.
- **Canary analysis:** compare error rate and latency of the new version against the old one before full rollout.
- **Feature flags:** turn a new feature on for internal users first ("dogfooding").
- **Chaos engineering:** carefully break things on purpose (kill a pod, slow the database) to prove the system recovers — start in staging, with a clear plan and a stop button.

#### 5.4.11 Using AI in testing

- AI tools can **suggest test cases and edge cases**, generate test data, and draft test code.
- **Review generated tests carefully:** AI often writes tests that only repeat what the code already does, so they pass even when the code is wrong. Make sure each test checks a **requirement**.
- If the product **itself uses an AI model**, normal assertions are not enough because answers vary. Teams add **evaluations ("evals")**: a fixed set of example inputs with scoring rules, run on every change to the prompt or model.

### 5.5 Testing is "done enough" when... (exit criteria)

- [ ] Every **acceptance criterion** has a passing test (automated where possible).
- [ ] **Unit, integration and system** tests pass in CI; the suite is **not flaky**.
- [ ] Every fixed bug has a **regression test**.
- [ ] **Non-functional** targets are proven: performance (load test vs. SLOs), security scans clean, accessibility checks pass.
- [ ] **Coverage** is above the team minimum, and important paths (auth, payments, data changes) are well covered.
- [ ] No open **critical or high-severity** bugs (or each has an agreed plan).
- [ ] **Smoke tests** pass on staging; **UAT / product owner acceptance** is done.
- [ ] Test data contains **no real personal data**.

---

## 6. Phase 5 — Deployment: "Automated, Small, Reversible"

### 6.1 The job

- Release the software to users **safely**: no downtime, a small blast radius if something is wrong, and a fast way back.
- **Core tasks from the lecture (still true in every model):**
  1. Release the application into the **production environment** and make it **available to users**.
  2. Release **in stages**: first to a **UAT (User Acceptance Testing) platform**, then to production.
  3. Get **customer sign-off** on the functionality before production.
  4. Deliver to the right **target**: a **website**, a **mobile app store**, or a **software distribution server** on a corporate network.
- **Deploy ≠ release** (a key modern idea, not in the lecture):

  | | **Deploy** | **Release** |
  |---|---|---|
  | **Meaning** | New code is **installed and running** on the servers | Users can **see and use** the new feature |
  | **Controlled by** | The CD pipeline | A **feature flag** or a configuration switch |
  | **Why separate them** | Deploy often, at low risk | Turn features on when the business is ready — and off in seconds if there is a problem |

### 6.2 Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **Release to production** | One big release at the end, often done by hand by an operations team, often at night or on weekends | Many small releases by a **CD pipeline**, started by a merge, during normal working hours |
| **Staged release (UAT, then production)** | A UAT server, deployed by hand | Automatic environments: CI → **staging (UAT)** → production, all using the **same image**; plus **canary** steps inside production |
| **Customer sign-off** | A formal signed document after UAT; in large companies also a **CAB (Change Advisory Board)** meeting | An **approval gate** in the pipeline (Continuous Delivery), or automatic if all checks pass (Continuous Deployment); **feature flags** let the product owner "release" a feature when ready. Many enterprises now use **automated change approval** based on pipeline evidence (tests, scans, reviews) |
| **Targets: website, app store, corporate server** | Each released by hand | **Website / API:** container to Kubernetes, OpenShift, a PaaS (Platform as a Service, for example Azure App Service) or serverless. **App store:** automated build + beta track (TestFlight, Google Play testing) + store review + **staged rollout** to a % of users. **Corporate devices:** device-management tools push updates in waves |

### 6.3 How modern teams do it

- **A CD pipeline** does the release work, not a person typing commands.
- **Environments:** development → CI → **staging (UAT — User Acceptance Testing)** → production. Staging should match production closely (same image, same configuration shape, realistic data volume).
- **Build once, promote everywhere:** build **one** immutable Docker image and move that **same** image through every environment. Identify it by the **git commit SHA** or, even safer, by its **digest** (`sha256:…`), which can never point to different content.
- **Continuous Delivery vs. Continuous Deployment:**

  | | Continuous Delivery | Continuous Deployment |
  |---|---|---|
  | **To staging** | Automatic | Automatic |
  | **To production** | One-click human approval | Automatic if all checks pass |
  | **Good for** | Regulated or customer-approval projects | Fast-moving product teams |

- **Safe release strategies** (together called **progressive delivery**):

  | Strategy | How it works | Benefit | Watch out for |
  |----------|--------------|---------|---------------|
  | **Rolling** | Replace instances one by one | No downtime; built into Kubernetes | Old and new versions run **at the same time** for a while |
  | **Blue-green** | Two full environments; switch all traffic at once | Instant rollback (switch back) | Needs **double** the infrastructure during the switch |
  | **Canary** | 5% of users first, then 25%, 50%, 100%, checking metrics at each step | Problems hit few users | Needs good metrics and traffic splitting (service mesh such as Istio, or Argo Rollouts / Flagger) |
  | **Feature flags** | Code deployed but hidden; turned on per user group | "Deploy" separate from "release" | Remove old flags, or they become technical debt |
  | **Shadow / dark launch** | Copy real traffic to the new version, but ignore its answers | Test with real load, zero user impact | Must not cause side effects (no double emails or payments) |

- **Always have a rollback plan** — return to the last good version in minutes (see [6.4.6](#646-rollback-vs-roll-forward)).
- **Infrastructure as Code (IaC):** servers, Kubernetes manifests and config live in Git (Terraform, Helm, Kustomize). **GitOps** tools (Argo CD, Flux) make the cluster match what is in Git, and every change to production is a reviewed commit.
- **Backward-compatible database migrations** (**expand → migrate → contract**): first add new columns, then move the code, and only later remove old columns, so old and new versions can run at the same time.
- **Health checks:** Kubernetes uses a **readiness probe** to decide if a pod should **receive traffic**, and a **liveness probe** to decide if a pod is stuck and must be **restarted**.

![The modern CI/CD pipeline from git push to production with monitoring and rollback](images/sdlc-modern-cicd-pipeline.svg)

![Release strategies: rolling, blue-green and canary](images/sdlc-modern-release-strategies.svg)

```yaml
# .github/workflows/ci-cd.yml — test, build once, deploy to staging, then production
name: CI-CD
on:
  push: { branches: [main] }
  pull_request:

permissions:
  contents: read

env:
  IMAGE: ghcr.io/acme/book-review-api:${{ github.sha }}   # one immutable tag per commit

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 24, cache: npm }  # a pinned Node.js LTS line (check nodejs.org); cache npm downloads
      - run: npm ci                             # exact versions from package-lock.json
      - run: npm run lint                       # coding standards
      - run: npm test                           # unit + integration tests
      - run: npm audit --audit-level=high       # block known high-risk packages

  build:
    needs: test                                 # only runs if tests pass
    if: github.ref == 'refs/heads/main'         # only for merges to main
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write                           # needed to push to GitHub Container Registry
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3            # log in BEFORE pushing
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }} # short-lived token, no stored password
      - uses: docker/build-push-action@v6
        with: { push: true, tags: "${{ env.IMAGE }}" }

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging                        # staging secrets and URL
    steps:
      - uses: actions/checkout@v4
      - run: ./scripts/deploy.sh staging "$IMAGE"   # e.g. update the GitOps repo or run kubectl
      - run: ./scripts/smoke-test.sh https://staging.example.com

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production                     # set "required reviewers" here = the sign-off gate
    steps:
      - uses: actions/checkout@v4
      - run: ./scripts/deploy.sh production "$IMAGE"  # the SAME image that passed staging
      - run: ./scripts/smoke-test.sh https://api.example.com
```

**What happens if... you push an image without logging in?**

```yaml
# ❌ No docker/login-action and no "packages: write" permission
- run: docker push ghcr.io/acme/book-review-api:${{ github.sha }}
# The job fails with "unauthorized" / "denied", and nothing reaches the registry.
```

```yaml
# deployment.yaml — Kubernetes rolling update with health checks, limits and safe shutdown
apiVersion: apps/v1
kind: Deployment
metadata: { name: book-review-api }
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate: { maxUnavailable: 0, maxSurge: 1 }   # never drop below 3 ready pods
  selector: { matchLabels: { app: book-review-api } }
  template:
    metadata: { labels: { app: book-review-api } }
    spec:
      terminationGracePeriodSeconds: 30                  # time for in-flight requests to finish
      securityContext: { runAsNonRoot: true }            # the container must not run as root
      containers:
        - name: api
          image: ghcr.io/acme/book-review-api:9f2c1e7    # the exact tag (git SHA) tested on staging
          ports: [{ containerPort: 3000 }]
          resources:
            requests: { cpu: 250m, memory: 256Mi }       # what the scheduler reserves
            limits:   { memory: 512Mi }                  # pod is killed if it uses more memory
          readinessProbe: { httpGet: { path: /health/ready, port: 3000 } }  # gets traffic?
          livenessProbe:  { httpGet: { path: /health/live,  port: 3000 } }  # restart if stuck?
          lifecycle:
            preStop: { exec: { command: ["sleep", "5"] } } # let the load balancer stop sending traffic first
          env:
            - name: DATABASE_URL
              valueFrom: { secretKeyRef: { name: api-secrets, key: database-url } }
```

```bash
# Roll back a bad release in one command (if not using GitOps)
kubectl rollout undo deployment/book-review-api
kubectl rollout status deployment/book-review-api   # watch it recover
# With GitOps (Argo CD / Flux): revert the commit in the GitOps repo instead,
# otherwise the tool will "fix" the cluster back to the bad version.
```

### 6.4 Industry practices the lecture does not cover

#### 6.4.1 Building a good container image

- **Multi-stage build:** install and build in one stage, copy only what is needed into a small final image.
- **Small, pinned base image** (for example `node:24-alpine` — an LTS line, pinned — or a "distroless" image) — fewer packages, fewer vulnerabilities.
- **Production dependencies only:** `npm ci --omit=dev`.
- **Run as a non-root user** — set it by **numeric UID** (`USER 1000`); Kubernetes `runAsNonRoot` cannot verify a user given only by name and refuses to start the pod.
- **`.dockerignore`** so `node_modules`, `.git`, `.env` and test files never enter the image.
- **Never bake secrets into the image** — they stay readable in the image layers forever. Inject them at runtime.
- **Start `node` directly**, not through `npm start`, so the process receives shutdown signals (`SIGTERM`) correctly.

```dockerfile
# Dockerfile — multi-stage, small, non-root
FROM node:24-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev                 # exact production dependencies only

FROM node:24-alpine
ENV NODE_ENV=production
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY src ./src
USER 1000                             # the built-in "node" user, as a NUMERIC id so Kubernetes runAsNonRoot can verify it
EXPOSE 3000
CMD ["node", "src/server.js"]         # node is PID 1 and receives SIGTERM directly
```

**What happens if... you use `CMD npm start` and copy everything?**

```dockerfile
# ❌
FROM node:24
COPY . .                  # copies .env (secrets!), .git and local node_modules into the image
RUN npm install           # dev dependencies too; versions may differ from the lockfile
CMD npm start             # shell + npm wrap node; SIGTERM may not reach the app,
                          # so Kubernetes kills it after 30 s and requests are cut off
```

#### 6.4.2 Zero-downtime deploys: graceful shutdown

When Kubernetes replaces a pod it sends **`SIGTERM`**. The app must stop taking new requests, **finish the current ones**, close connections, and exit.

```javascript
// src/server.js — graceful shutdown
const app = require('./app');
const config = require('./config');
const db = require('./db');
const logger = require('./lib/logger');

const server = app.listen(config.PORT, () => logger.info(`listening on ${config.PORT}`));

process.on('SIGTERM', () => {
  logger.info('SIGTERM received, shutting down gracefully');
  server.close(async () => {          // stop accepting new connections; wait for open requests
    await db.end();                   // close the database pool
    process.exit(0);
  });
  setTimeout(() => process.exit(1), 25_000).unref(); // force exit before Kubernetes' 30 s limit
});
```

#### 6.4.3 Configuration and secrets per environment

- The **same image** runs everywhere; only **configuration** changes (environment variables, ConfigMaps).
- **Secrets** come from a secret manager (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault) or Kubernetes Secrets synced by a tool such as External Secrets Operator.
- **Pipelines should not hold long-lived cloud keys.** Use **OIDC (OpenID Connect) federation**: the CI job proves who it is and gets a **short-lived** cloud token.
- **Protect production:** only the pipeline (not people's laptops) deploys; production environments need **required reviewers**; access follows **least privilege**.

#### 6.4.4 Autoscaling and capacity

- **Resource requests and limits** tell Kubernetes how much CPU and memory each pod needs.
- **HPA (Horizontal Pod Autoscaler)** adds or removes pods based on CPU, memory or custom metrics (for example requests per second).
- Autoscaling only works if the app is **stateless** (see Design 3.4.1).

#### 6.4.5 Verify after every deployment

- **Smoke tests** run automatically right after each deploy.
- **Automated canary analysis:** tools such as **Argo Rollouts** or **Flagger** compare the new version's error rate and latency with the old one, and **roll back automatically** if the SLOs are broken.
- **Watch dashboards** for the first minutes after a release; link each deploy to its version in your monitoring tool (a "deploy marker").

#### 6.4.6 Rollback vs. roll-forward

| | **Rollback** | **Roll-forward** |
|---|---|---|
| **What** | Go back to the previous version | Fix the problem and deploy a **new** version quickly |
| **When** | Default choice when a release is bad | When rollback is not possible — for example after a database migration that old code cannot read |
| **Key rule** | Keep migrations backward compatible so rollback **stays possible** | Needs a very fast, reliable pipeline |

- **Database changes are the hardest part to undo.** That is why the **expand → migrate → contract** pattern matters: old code still works on the new schema.

#### 6.4.7 Release management

- **Version and tag** each release (SemVer, git tags), with **release notes** generated from Conventional Commits.
- **Supply-chain evidence:** many teams **sign** images (Sigstore **cosign**) and attach an **SBOM** and **provenance** (who built it, from which commit — see the **SLSA** framework), so production only runs trusted images.
- **Deployment freezes** (for example during peak sales) are still used by some companies — but with small, safe releases, they are needed less.
- **Mobile apps** are different: users may not update, so the backend must support **several app versions at once**, and app-store review adds days. Use feature flags and API versioning.

#### 6.4.8 Measuring delivery: DORA metrics

The **DORA (DevOps Research and Assessment)** research program measures software delivery with these key metrics:

| Metric | Question |
|--------|----------|
| **Deployment frequency** | How often do we deploy to production? |
| **Lead time for changes** | How long from commit to running in production? |
| **Change failure rate** | What share of deployments cause a failure in production? |
| **Time to restore service** | How fast do we recover from a failure? |

- DORA's research found that teams that deploy **more often** usually also have **fewer failures** and **faster recovery** — speed and stability go together when releases are small and automated.
- DORA reports also look at **reliability** (meeting your SLOs) next to these delivery metrics.

#### 6.4.9 Using AI tools in deployment

- AI tools can help **write and review** pipelines, Dockerfiles and Kubernetes manifests, and explain failed deploy logs.
- **Review every generated config** — small mistakes (wrong permissions, missing limits, `latest` tags) cause outages and security holes.
- **Do not give AI agents unrestricted production access.** Changes to production should still go through the reviewed pipeline.

### 6.5 Deployment is "done" when...

- [ ] The change reached production through the **pipeline** (no manual steps), using the **same image** that passed staging.
- [ ] **Smoke tests** passed in staging and production; **sign-off / approval gate** completed where required.
- [ ] The rollout used a **safe strategy** (rolling, canary or blue-green), with **no downtime**.
- [ ] **Metrics are healthy** after release (error rate, latency vs. SLOs); no automatic rollback was triggered.
- [ ] A **rollback (or roll-forward) plan** is known and tested; migrations are backward compatible.
- [ ] **Secrets and config** came from the right environment; no secrets in the image.
- [ ] The image is **scanned** (and signed, where the team requires it); the release is **tagged** with release notes.
- [ ] New user-facing features are controlled by **feature flags** where needed.

---

## 7. Phase 6 — Maintenance: "Observe, Learn, Improve Continuously"

### 7.1 The job

- Keep the software **working, secure, fast and useful** after release, and feed what you learn into the next loop.
- Maintenance is usually the **longest** phase: software often runs and changes for years after its first release.
- **Core tasks from the lecture (still true in every model):**
  1. Find **bugs** that were **missed during testing**.
  2. Identify **UI (User Interface) issues**.
  3. Identify **requirements that were not listed in the SRS**.
  4. Identify **code enhancements**.
  5. **High-priority bugs** are fixed now; **others** are added to the requirements of a **future release**.
  6. **Feedback from stakeholders** feeds into **another development cycle**.

#### 7.1.1 The four types of maintenance (classic SDLC theory, not in the lecture)

The classic four maintenance categories, used by the software maintenance standard **ISO/IEC/IEEE 14764**, are below. **Corrective** and **adaptive** are *reactive* (responding to a failure or a change); **preventive** and **perfective** are *proactive*. The lecture's tasks fit into them:

| Type | Meaning | Lecture task it covers | Example |
|------|---------|------------------------|---------|
| **Corrective** | Fix bugs and failures | "Find bugs missed during testing" | Fix the 500 error on long review text |
| **Adaptive** | Keep working in a **changing environment** | (not in the lecture) | Upgrade to a newer Node.js LTS; move to a new cloud; follow a new law |
| **Perfective** | Improve or add features based on feedback | "UI issues", "missing requirements", "code enhancements" | Add "edit my review"; make search faster |
| **Preventive** | Stop future problems before they happen | (not in the lecture) | Refactor messy code, add missing tests, update dependencies, fix a slow query before traffic grows |

![The four types of maintenance and the feedback loop](images/sdlc-modern-maintenance-types.svg)

### 7.2 Core tasks: Waterfall way vs. modern way

| Core task | Waterfall way | Modern way |
|-----------|---------------|------------|
| **When maintenance starts** | After the project is "finished" and handed to a separate support team | From the **first release**, by the **same team** ("you build it, you run it") |
| **Find missed bugs** | Users report them to a help desk | **Error tracking** and **SLO alerts** often detect bugs **before** users report them |
| **Find UI issues** | User complaints | Product analytics, real-user monitoring, usability tests, user feedback |
| **Find missing requirements and enhancements** | Collected for "version 2" months later | Added to the **backlog** immediately and planned in the next sprints; ideas can be checked with **A/B tests** |
| **High priority → fix now; others → future release** | Emergency patch; everything else waits for the next big version | **Rollback**, **feature flag off** or **hotfix** in minutes for urgent issues; everything else is **prioritized in the backlog** — the "future release" may be next week |
| **Feedback → next cycle** | A new project starts | The loop never stops: feedback becomes stories, and the six phases run again |

### 7.3 How modern teams do it

- **"You build it, you run it":** the team that wrote the service is also **on call** for it.
- **Observability — the three pillars:**

  | Pillar | What it answers | Example tools |
  |--------|-----------------|---------------|
  | **Logs** | "What happened?" (structured JSON events) | Grafana Loki, ELK (Elasticsearch, Logstash, Kibana) |
  | **Metrics** | "How much / how fast?" (rates, errors, latency) | Prometheus + Grafana |
  | **Traces** | "Where did this request spend its time?" | OpenTelemetry, Jaeger, Grafana Tempo |

  **OpenTelemetry** is the vendor-neutral standard for producing all three, so you can change monitoring tools without changing code.
- **What to watch:**
  - **Golden signals** (Google SRE): **latency**, **traffic**, **errors**, **saturation**.
  - **RED** method for each service: **R**ate, **E**rrors, **D**uration.
  - **USE** method for each resource (CPU, memory, disk): **U**tilization, **S**aturation, **E**rrors.
  - **Error tracking** (for example Sentry) groups exceptions with stack traces and the release that caused them.
- **Alert on SLOs**, not on every small warning: alert when users are actually hurt (see [7.4.1](#741-sli-slo-sla-and-error-budgets)).
- **Incident management:**
  1. **Detect** — an alert fires.
  2. **Mitigate** — roll back, turn off a feature flag, or **hotfix**.
  3. **Learn** — write a **blameless postmortem**.
  4. **Prevent** — add the fixes and new tests to the backlog.
- **Continuous security maintenance:** automated dependency updates (Dependabot, Renovate), fast patching of CVEs (Common Vulnerabilities and Exposures), and regular secret rotation.
- **Pay down technical debt:** reserve regular time each sprint (many teams use around 10–20%) for refactoring and upgrades.
- **Product analytics and user feedback** become new stories in the backlog — and the loop starts again.

```mermaid
flowchart TD
    PROD["Software in production"] --> OBS["Logs, metrics, traces, error tracking"]
    OBS --> SLO{"SLO broken?"}
    SLO -->|no| FB["Analytics and user feedback"]
    SLO -->|yes| INC["Incident: rollback, flag off, or hotfix"]
    INC --> PM["Blameless postmortem"]
    PM --> BL["Backlog: fixes, tests, improvements"]
    FB --> BL
    BL --> NEXT["Next planning loop"]
```

```javascript
// src/routes/health.js — endpoints used by Kubernetes probes and monitoring
const express = require('express');
const router = express.Router();

// Liveness: "is the process alive?" — keep it simple, NO dependency checks
router.get('/health/live', (req, res) => res.status(200).json({ status: 'ok' }));

// Readiness: "can THIS pod serve traffic right now?"
router.get('/health/ready', async (req, res) => {
  try {
    // Always use a short timeout — a hanging check is worse than a failed one
    await Promise.race([
      req.app.locals.db.query('SELECT 1'),
      new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 1000)),
    ]);
    res.status(200).json({ status: 'ready' });
  } catch (err) {
    res.status(503).json({ status: 'not ready' });  // Kubernetes stops sending traffic to this pod
  }
});

module.exports = router;
```

- **Design note:** if **every** pod checks the **same shared** database, a database outage makes **all** pods unready at once, and users get the load balancer's generic error instead of your clear error message. Some teams therefore check only what **this pod** controls (its own connection pool, startup finished) in readiness, and report shared dependencies through **metrics and alerts** instead. Choose deliberately and record it in an ADR.

**What happens if... the liveness probe checks the database?**

```javascript
// ❌ If the database is slow for 30 seconds, Kubernetes RESTARTS every API pod.
//    Restarting does not fix the database — it only causes a full outage.
router.get('/health/live', async (req, res) => {
  await req.app.locals.db.query('SELECT 1');
  res.send('ok');
});
// ✅ Liveness = process only. Readiness = what this pod needs to serve traffic.
```

### 7.4 Industry practices the lecture does not cover

#### 7.4.1 SLI, SLO, SLA and error budgets

| Term | Meaning | Example |
|------|---------|---------|
| **SLI (Service Level Indicator)** | The **measurement** | Share of requests that succeed in under 200 ms |
| **SLO (Service Level Objective)** | The **internal target** for the SLI | 99.9% over 30 days |
| **SLA (Service Level Agreement)** | The **contract** with customers, often with money back if missed | 99.5% per month, or a service credit |
| **Error budget** | What the SLO **allows** to fail: 100% − SLO | 0.1% of requests ≈ about 43 minutes of full downtime in 30 days |

- **How teams use the error budget:** while budget is left, ship features fast. When the budget is **used up**, slow down releases and spend time on **reliability** work.
- Keep the **SLA looser than the SLO**, so you get an internal warning before you break the contract.

#### 7.4.2 Metrics in code

```javascript
// src/middleware/metrics.js — RED metrics with prom-client, scraped by Prometheus
const client = require('prom-client');
client.collectDefaultMetrics();                 // CPU, memory, event-loop lag of this Node process

const labelNames = ['method', 'route', 'status'];
const duration = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames,
  buckets: [0.05, 0.1, 0.2, 0.5, 1, 2],         // 0.2 s bucket matches the 200 ms SLO
});
const requests = new client.Counter({ name: 'http_requests_total', help: 'HTTP requests', labelNames });

function metrics(req, res, next) {
  const end = duration.startTimer();
  res.on('finish', () => {
    // Use the route PATTERN (/books/:isbn/reviews), never the real URL
    const labels = { method: req.method, route: req.route?.path || 'unmatched', status: res.statusCode };
    end(labels);
    requests.inc(labels);
  });
  next();
}

async function metricsEndpoint(req, res) {      // app.get('/metrics', metricsEndpoint)
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
}

module.exports = { metrics, metricsEndpoint };
```

**What happens if... you use the real URL as a metric label?**

```javascript
// ❌ route: req.originalUrl  →  "/books/9780132350884/reviews", "/books/9781492052203/reviews", ...
// Every ISBN creates a NEW time series ("high cardinality"). Prometheus memory explodes,
// dashboards become slow, and monitoring can fall over during the incident you need it for.
// ✅ Use the route pattern: "/books/:isbn/reviews".
```

#### 7.4.3 Alerting and on-call

- **Every alert must be actionable.** If nobody needs to do anything, it should be a dashboard or a ticket, not a page.
- **Page vs. ticket:** wake someone up only when users are hurt **now** (for example the SLO burning fast). Slow problems become tickets.
- **Runbooks:** each alert links to a short guide: what it means, how to check, how to fix.
- **On-call rotation:** a fair schedule, a clear escalation path, and time to recover after a hard night.
- **Alert fatigue** (too many noisy alerts) makes people ignore the real ones — delete or fix noisy alerts.

```yaml
# alerts.yaml — Prometheus alert: more than 1% of requests failing for 5 minutes
groups:
  - name: book-review-api
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m]))
            / sum(rate(http_requests_total[5m])) > 0.01
        for: 5m                                  # must last 5 minutes — ignore short blips
        labels: { severity: page }
        annotations:
          summary: "Book Review API: more than 1% of requests are failing"
          runbook_url: "https://wiki.example.com/runbooks/high-error-rate"
```

#### 7.4.4 Incidents in detail

- **Severity levels** (for example SEV1 = full outage … SEV4 = minor issue) decide who is called and how fast.
- **Clear roles** in a big incident: an **incident commander** (coordinates, decides), people who **investigate and fix**, and a **communications lead** (updates the **status page** and stakeholders).
- **Mitigate first, find the root cause later.** Rolling back in 5 minutes is better than debugging for an hour while users suffer.
- **Measure:** **MTTD** (Mean Time To Detect) and **MTTR** (Mean Time To Restore/Recover).
- **Problem management** (an **ITIL** — Information Technology Infrastructure Library — idea, common in enterprises): an *incident* is one outage; a *problem* is the **root cause** behind repeated incidents, tracked until it is removed.

```markdown
# Postmortem: Reviews API errors — 2026-11-10 (SEV2)

**Impact:** 18% of review requests failed for 22 minutes. No data lost.
**Timeline (UTC):** 09:02 deploy v1.6.0 · 09:05 alert HighErrorRate · 09:09 rollback started · 09:24 recovered
**Root cause:** New query had no index on (isbn, created_at); the database CPU reached 100% under normal load.
**What went well:** Alert fired in 3 minutes; rollback was one command.
**What went wrong:** The load test used a database with only 100 rows.
**Action items (owner, due date):**
- Add the missing index via migration (backend lead, 2026-11-12)
- Use production-sized synthetic data in load tests (QA, 2026-11-20)
- Add a slow-query alert (SRE, 2026-11-20)
*Blameless: we fix systems and processes, not people.*
```

#### 7.4.5 The hotfix process

- A hotfix is a **small, urgent fix** to production — but it still goes through the **same pipeline**: a PR, a review (it can be quick), **tests**, and staging.
- **Skipping tests for "just a one-line fix"** is a common cause of a second incident.
- Always add a **regression test** for the bug, and make sure the fix also lands on `main` so the next release does not bring the bug back.

#### 7.4.6 Backups and disaster recovery

| Term | Question | Example target |
|------|----------|----------------|
| **RPO (Recovery Point Objective)** | How much data can we afford to **lose**? | At most 5 minutes (point-in-time recovery) |
| **RTO (Recovery Time Objective)** | How long can we be **down**? | Back online within 1 hour |

- **Test restores regularly** — a backup you have never restored is only a hope.
- Keep backups in a **separate account or region**, and protect them from deletion (ransomware often targets backups first).
- Practice **disaster recovery drills** (for example "the main region is down").

#### 7.4.7 Keeping the platform up to date (adaptive maintenance)

- **Runtime and framework upgrades:** move to a newer Node.js **LTS** line **before** the old one reaches end-of-life; keep Express and major libraries current. Small, regular upgrades are much cheaper than one huge upgrade every few years.
- **Base images:** rebuild Docker images regularly to get OS security fixes, even if your code did not change.
- **Certificates:** automate TLS certificate renewal (for example cert-manager with Let's Encrypt). Expired certificates are a classic, embarrassing outage.
- **Vulnerability management:** fix known vulnerabilities within an agreed time by severity (for example critical within days).
- **Access reviews:** regularly remove access that people or services no longer need.

#### 7.4.8 Data maintenance

- **Retention and deletion:** delete or archive data you no longer need; handle **GDPR requests** (export, correct, delete a user's data) within the legal deadline.
- **Database health:** watch slow queries, add or remove indexes, keep table statistics fresh (in PostgreSQL, **autovacuum** does much of this — monitor it).
- **Capacity and cost:** watch disk growth and cloud costs (**FinOps**); right-size servers.
- **Audit logs:** keep a record of important actions (who deleted what, and when).

#### 7.4.9 Deprecation and end-of-life

- Features and API versions also need a **planned end**:
  1. Announce the deprecation (docs, changelog, emails).
  2. Mark responses with headers such as **`Deprecation`** and **`Sunset`** (the date it will stop working).
  3. Watch usage metrics; contact remaining users.
  4. Remove it after the sunset date.

#### 7.4.10 Legacy systems and modernization

- Old systems that are hard to change are common. A full rewrite is risky.
- The **strangler fig pattern** replaces a legacy system **piece by piece**: put a router in front, move one feature at a time to the new service, and remove the old code when nothing uses it.
- First add **tests and monitoring** around the legacy code, so changes are safe.

#### 7.4.11 Using AI in maintenance

- AI tools can **summarize logs and incidents**, suggest likely causes, draft postmortems, and propose fixes or dependency upgrades. Many monitoring products now include these features (often called **AIOps**).
- **Treat AI suggestions as hypotheses.** Verify with real data, and send every fix through the normal review and tests.
- If the product **itself uses an AI model**, maintenance also includes: monitoring answer **quality** over time (quality can drift as user behavior changes), re-running **evals** before upgrading to a new model version, and watching **cost per request**.

### 7.5 A service is "healthy and well maintained" when...

- [ ] **SLOs** are defined, measured (SLIs), and **met**; the error budget is tracked.
- [ ] **Logs, metrics, traces and error tracking** are in place; dashboards show RED/golden signals.
- [ ] **Alerts** are actionable, link to **runbooks**, and page the **on-call** person only when users are hurt.
- [ ] **Incidents** are handled with clear roles and followed by **blameless postmortems** whose action items are done.
- [ ] **Hotfixes** use the normal pipeline and always add a **regression test**.
- [ ] **Backups** meet RPO/RTO and **restores are tested**.
- [ ] **Dependencies, Node.js LTS, base images and certificates** are kept up to date; vulnerabilities are fixed on time.
- [ ] **Data** retention, deletion requests and database health are managed.
- [ ] **Technical debt** gets regular time; deprecated features and APIs follow a **sunset plan**.
- [ ] **Feedback, analytics and incident learnings** flow into the **backlog**, starting the next loop.

---

## 8. One Feature, All Six Phases (Modern Flow)

**Feature:** "Readers can rate a book from 1 to 5" in the Book Review API.

| Day | Phase | What happens |
|-----|-------|--------------|
| 1 | **Plan** | The story and acceptance criteria are refined from the "Reviews" epic. Security requirement added: "only logged-in users". |
| 1 | **Design** | The OpenAPI contract is updated; the threat model notes "one review per user per book" to stop spam. An ADR records the unique index. |
| 2 | **Develop + Test** | TDD: tests for `isValidRating` first, then the code. Integration test with Testcontainers. Small PR, reviewed, CI green. |
| 2 | **Deploy** | Merged to `main`. The pipeline builds image `1.5.0`, deploys to staging, the product owner checks it, then a canary sends 5% of traffic to it. |
| 3 | **Deploy** | No errors at 5% → rolled out to 100%. |
| 3+ | **Maintain** | A dashboard shows rating requests and errors. Users ask to "edit my rating" → new story in the backlog. |

```mermaid
flowchart TD
    S["Story: rate a book 1 to 5"] --> C["Update OpenAPI contract and ADR"]
    C --> TDD["TDD: test first, then code"]
    TDD --> PR["Small PR plus code review"]
    PR --> CI["CI: lint, tests, security scans"]
    CI --> STG["Deploy image to staging"]
    STG --> CAN["Canary: 5 percent of users"]
    CAN --> FULL["Roll out to 100 percent"]
    FULL --> MON["Monitor dashboards and feedback"]
    MON -->|edit my rating| S
```

---

## 9. Quick Reference: Lecture vs. Modern

| Phase | Lecture (Waterfall view) | ✅ Modern best practice |
|-------|--------------------------|--------------------------|
| **Planning** | Gather all requirements → one approved SRS | Stakeholders + feasibility first; light SRS or vision + backlog of epics; functional **and** non-functional requirements; living risk register; detailed stories with testable acceptance criteria just in time; security and SLOs as requirements |
| **Design** | One design document before coding | HLD early + LLD per slice ("just enough" design); quality attributes drive choices; modular monolith by default; schema with database constraints; API-first (OpenAPI, Problem Details errors); threat modeling + security principles; reliability and operations planned; C4 diagrams as code; ADRs and design docs reviewed as PRs |
| **Development** | Assign tasks from the design doc; follow standards | Trunk-based (or GitHub Flow), small PRs, Conventional Commits + SemVer, real code review, layered code + KISS/DRY/YAGNI/SOLID, config validated at startup, central error handler + structured logs, Node event-loop care, supply-chain security, secure coding checklist, reproducible local setup, AI code reviewed like human code, Definition of Done |
| **Testing** | After coding is complete | Shift-left + shift-right, TDD, pyramid/trophy with all four levels in CI, verification and validation, functional + non-functional (load, security, accessibility) tests, test doubles at boundaries, synthetic test data, coverage + mutation testing, no flaky tests, severity vs. priority, regression test for every bug, exit criteria |
| **Deployment** | UAT sign-off → production | CD pipeline (Delivery or Deployment), deploy ≠ release, build once and promote by SHA/digest, secure multi-stage image, progressive delivery (rolling, canary, blue-green, flags), graceful shutdown, OIDC + secret managers, autoscaling, post-deploy checks with auto-rollback, rollback vs. roll-forward, signed images + SBOM, DORA metrics |
| **Maintenance** | Find bugs, UI issues, missing requirements after release | Four maintenance types (corrective, adaptive, perfective, preventive); observability with OpenTelemetry; RED/golden signals; SLI/SLO/SLA + error budgets; actionable alerts, runbooks, on-call; incident roles + blameless postmortems; hotfixes through the pipeline; tested backups (RPO/RTO); platform, certificate and dependency upgrades; data maintenance; deprecation plans; strangler fig for legacy |

---

## 10. Related Concepts

1. **Agile and Scrum** — Scrum gives the six phases a fixed rhythm: sprint planning (plan), daily work (design, develop, test), sprint review (acceptance), retrospective (improve the process).
2. **DevOps and the DORA metrics** — DORA (DevOps Research and Assessment) measures team performance with four numbers: deployment frequency, lead time for changes, change failure rate, and time to restore service.
3. **Twelve-Factor App** — a set of rules for cloud-ready apps (config in the environment, stateless processes, logs as event streams) that makes the deployment and maintenance phases easier.
4. **OWASP Top 10 and DevSecOps** — the list of the most common web security risks, and the practice of checking for them automatically in every phase.
5. **SRE (Site Reliability Engineering)** — Google's approach to running production with SLOs, error budgets and blameless postmortems; it gives the maintenance phase its modern shape.
