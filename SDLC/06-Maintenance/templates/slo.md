# SLOs — <Service name>

> Copy to `docs/slo.md` before go-live. Owner: Tech Lead with the Product Owner. Review monthly in the service review.

| SLI (what we measure) | SLO (target) | Window | Error budget | Measured by |
|-----------------------|--------------|--------|--------------|-------------|
| Availability: share of requests without 5xx | 99.9% | 30 days | 0.1% (≈ 43 min full outage) | <metric / dashboard link> |
| Latency: share of requests faster than 200 ms | 95% | 30 days | 5% | |
| <business flow, e.g. "review saved"> | | | | |

## Error budget policy
- **Budget left:** normal feature work.
- **Budget burning fast** (alert): on-call investigates now.
- **Budget used up:** pause risky releases; next sprint prioritizes reliability work until back within SLO.

## SLA (client projects only)
- Contracted level: <e.g. 99.5% monthly> — must be **looser** than the SLO.
- Support hours and response times: <from the support agreement>
