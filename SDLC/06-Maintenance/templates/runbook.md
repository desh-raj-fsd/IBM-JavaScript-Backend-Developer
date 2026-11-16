# Runbook: <Alert name>

> One runbook per alert, in `docs/runbooks/<alert-name>.md`. Link it from the alert's `runbook_url`.

| Field | Value |
|-------|-------|
| **Service** | |
| **Severity** | page / ticket |
| **Owner** | |
| **Last tested** | |
| **Last reviewed / next review due** | <YYYY-MM-DD> / <+ 6 months> ([README §7.2](../../README.md#72-documentation-rules), rule 7) |

## What this alert means
<In plain words: what is broken and who is affected.>

## Check first (5 minutes)
1. Dashboard: <link> — is the problem still happening?
2. Was there a recent deploy or config change? <how to check>
3. Are dependencies healthy (database, external APIs)? <how to check>

## Mitigate (stop user impact first)
- Recent deploy? → **Roll back:** `<command or link>`
- New feature? → **Turn off the flag:** `<flag name>`
- Overload? → **Scale out:** `<command>`
- Dependency down? → <degradation steps / contact>

## Fix and verify
<Steps to find and fix the cause; how to confirm recovery.>

## Escalate
- After <N> minutes without progress, call: <Tech Lead / vendor / client contact>
- SEV1/SEV2: open an incident channel and name an incident commander.
