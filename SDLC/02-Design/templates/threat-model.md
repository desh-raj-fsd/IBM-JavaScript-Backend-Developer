# Threat Model — <system or feature>

> Copy to `docs/threat-model.md` (or one per significant feature). Update it when the design changes. Owner: Tech Lead; done with the Security Champion.

## 1. What are we building?
- Diagram link (data flow: users, services, data stores, external systems)
- **Trust boundaries:** <where data crosses from less trusted to more trusted>
- **Sensitive data:** <personal data, secrets, payment data…>

## 2. What can go wrong? (STRIDE)
| ID | Component / data flow | Threat type | Threat description | Likelihood (1–3) | Impact (1–3) |
|----|-----------------------|-------------|--------------------|------------------|--------------|
| T-01 | | Spoofing | | | |
| T-02 | | Tampering | | | |
| T-03 | | Repudiation | | | |
| T-04 | | Information disclosure | | | |
| T-05 | | Denial of service | | | |
| T-06 | | Elevation of privilege | | | |

## 3. What are we going to do about it?
| Threat ID | Mitigation | Story / ticket | Verified by (test, scan, review) |
|-----------|------------|----------------|----------------------------------|
| | | | |

## 4. Did we do a good enough job?
- [ ] Every high-score threat has a mitigation or an accepted-risk entry in the risk register
- [ ] Authentication, authorization (ownership checks), input validation, secrets, logging and rate limiting are covered
- [ ] Mitigations have tests or scans in CI
- [ ] Reviewed by: <names, date>
