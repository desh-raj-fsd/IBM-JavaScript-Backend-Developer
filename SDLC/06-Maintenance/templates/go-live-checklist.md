# Go-Live Checklist (Gate G5) — <Service name>

> Before the **first** production release with real users (and after major changes). Accountable: Tech Lead. The Product Owner and the support owner must agree.

## Observability
- [ ] Logs, metrics and traces in production; dashboard with rate, errors, duration
- [ ] Error tracking connected
- [ ] SLOs defined (`docs/slo.md`) and measured
- [ ] Alerts are actionable, each with a **runbook**

## Support
- [ ] On-call rotation set; contact and escalation path known
- [ ] Incident process and severity levels known by the team
- [ ] Client projects: support agreement / SLA signed; client contact list ready
- [ ] Status page or communication channel ready

## Resilience
- [ ] Backups configured; **a restore was tested**; RPO/RTO documented
- [ ] Rollback tested on staging
- [ ] Capacity checked (load test vs. expected traffic); autoscaling set
- [ ] TLS certificates auto-renew

## Security and data
- [ ] Threat model mitigations done; scans clean; pen test done if required
- [ ] Access to production reviewed (least privilege)
- [ ] Data retention and deletion process ready (GDPR requests)
- [ ] Audit logging (regulated data projects)

## Business
- [ ] UAT / acceptance signed
- [ ] User docs / release notes ready
- [ ] Cost monitoring and budget alerts set

| Role | Name | Date | Go / No-go |
|------|------|------|------------|
| Tech Lead | | | |
| Product Owner | | | |
| Client (client projects) | | | |
