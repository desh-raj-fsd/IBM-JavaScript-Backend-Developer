# Front-End Checklist — <Project name>

> For every web UI (website, web app, admin screen). Use it **once at project start** (sections 1–2, agree the answers in the design doc or project brief) and **again before each release** (sections 3–6). Owner: Tech Lead. Rules: [Design 4.13](../../02-Design/Design.md#413-front-end-design-decisions), [Development 4.14](../Development.md#414-front-end-code-standards), [Testing 4.16](../../04-Testing/Testing.md#416-front-end-testing), [Maintenance 4.12](../../06-Maintenance/Maintenance.md#412-front-end-monitoring-and-upgrades).

## 1. Decisions (project start)
- [ ] Approach chosen and written as an ADR: plain HTML/CSS/JS, library, or framework; rendering mode (static, server-rendered, single-page app)
- [ ] The ADR names the framework's **support window and end-of-life date**
- [ ] **Browser and device support policy** written (for example `browserslist` plus the list of supported browsers); copied to the versioning policy
- [ ] Accessibility target set: **WCAG (Web Content Accessibility Guidelines) 2.2 level AA** (or the contract's level)
- [ ] Performance targets set at the **75th percentile of real users**: Largest Contentful Paint (LCP) ≤ 2.5 s, Interaction to Next Paint (INP) ≤ 200 ms, Cumulative Layout Shift (CLS) ≤ 0.1
- [ ] One styling approach chosen (plain CSS, CSS Modules, utility CSS or Sass with `@use`)
- [ ] Shared components and design tokens (colors, spacing, fonts) planned if the product has many screens

## 2. Tooling (project start)
- [ ] TypeScript, ESLint (with accessibility rules), Prettier and Stylelint set up and run in CI
- [ ] Tests: unit, component, and a few end-to-end tests in **Chromium, Firefox and WebKit** (Playwright or similar)
- [ ] Automated accessibility check and a bundle-size / lab performance budget in CI
- [ ] Dependency updates automated; end-of-life dates of framework, Node.js and build tools in the calendar

## 3. Every UI change (Definition of Done)
- [ ] Native elements used (`button`, `a href`, `label` + `input`); no clickable `div`
- [ ] Works with the **keyboard only**; the focus outline is visible and not hidden by other content
- [ ] Works at **320 px** width and at desktop width; no sideways scroll; text zoom to 200% works
- [ ] **Same content and features** on phone and desktop
- [ ] Every image has correct `alt` text; form fields have labels and clear error messages
- [ ] Colors: text contrast at least 4.5:1 (large text 3:1); touch targets at least 24×24 CSS px, or enough space around smaller ones
- [ ] API calls check for HTTP errors, have a timeout, and show **loading, empty and error** states

## 4. Security (every release)
- [ ] No secrets in the bundle (search the build output); only public keys
- [ ] No untrusted data inserted as HTML (`innerHTML`, `dangerouslySetInnerHTML`, `v-html`)
- [ ] The server validates and authorizes every request; client checks are for user experience only; cookie sessions have a CSRF token or `Origin` check
- [ ] Session cookies are `HttpOnly`, `Secure` and `SameSite`
- [ ] CSP header sent on public web UIs, or an ADR says why not (tested in Report-Only first); third-party scripts approved; CDN scripts and stylesheets use SRI (`integrity` + `crossorigin="anonymous"`)
- [ ] `npm audit` (or the scanner) shows no unresolved high or critical findings

## 5. Performance and delivery (every release)
- [ ] Lab performance check passes the budget for key pages (Lighthouse or similar)
- [ ] Hashed file names; `Cache-Control: public, max-age=31536000, immutable` for hashed files, `no-cache` for HTML
- [ ] Images sized with `srcset` / `sizes`, with width and height set (no layout shift)
- [ ] Code split so the first page does not load code for other pages

## 6. After release
- [ ] Real-user Core Web Vitals and JavaScript errors visible (source maps uploaded to the error tracker, not served to users)
- [ ] Alert on error spikes after a release; checked in the monthly service review

| Role | Name | Date |
|------|------|------|
| Tech Lead | | |
| QA Engineer | | |
