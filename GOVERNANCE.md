# Governance

GLOBAL AI GOVERNANCE repositories are maintained as bounded engineering assets. Shared defaults improve consistency without erasing repository-specific ownership, maturity, evidence, or release boundaries.

## Decision rights

Humans retain authority for merges, releases, public claims, risk acceptance, security-sensitive changes, and changes that alter operational or authorization semantics.

Automation may inspect, validate, test, package, and propose changes. Automation does not create evidence that a system is safe, compliant, certified, production-authorized, or fit for a particular environment.

## Change classes

- **Low impact:** documentation hygiene, templates, metadata, or equivalent non-semantic maintenance.
- **Medium impact:** CI, validators, manifests, schemas, cross-repository interfaces, or governance mechanics.
- **High impact:** security semantics, authority semantics, cryptography, breaking schemas, recovery behavior, execution capability, releases, or public claims.

Every repository may impose stricter local requirements.
