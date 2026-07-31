# Security Policy — Coherence Energy Labs

This is the organization-wide default policy; it applies to every
Coherence Energy Labs repository that does not carry its own SECURITY.md.

## Reporting a vulnerability

Email **security@coherenceenergylabs.com**. We aim to acknowledge within
72 hours. Please include a reproduction path. Do not open a public issue
for a vulnerability before we have responded — coordinated disclosure
protects users of our live surfaces.

Machine-readable policy: [security.txt](https://coherenceenergylabs.com/.well-known/security.txt) (RFC 9116).

## What counts as a security issue here

Beyond conventional vulnerabilities, we treat **integrity failures as
security issues**: anything that lets a signed artifact be altered after
issuance, a receipt verify for data it does not bind, a publication gate
be bypassed, or a "verified" claim pass without its verification actually
running.

## Scope

All public repositories under
[github.com/coherence-energy-labs](https://github.com/coherence-energy-labs),
the live sites coherenceenergylabs.com, demos.coherenceenergylabs.com, and
hazardpulse.com, and the published verifiers and receipts they reference.
