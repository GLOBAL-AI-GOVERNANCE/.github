# Claims Integrity Convention

Claims Integrity keeps public language aligned with the evidence, implementation, maturity, and released state that actually exist.

## Two independent states

- Delivery: `PROPOSED` → `DEFINED` → `SHIPPED`.
- Evidence: `NOT_YET_ESTABLISHED` → `VERIFIED`.

`DEFINED` means requirements, implementation, or acceptance criteria exist within the repository's stated scope. `SHIPPED` requires the repository's authorized public release action. A merge, local commit, passing test, or generated artifact does not silently create a release.

`VERIFIED` must name the exact bounded statement, method, evidence reference, verification date, and limitations. It does not mean universally true, certified, compliant, safe, production-ready, or approved.

## Change review

For any public capability, maturity, assurance, release, validation, or partnership claim, record:

1. The exact wording that changes.
2. Repository-controlled evidence supporting it.
3. The boundary the evidence does not establish.
4. The published release or unreleased development state.

The shared pull-request checklist makes these questions visible. Repositories may adopt stricter claim registers, schemas, phrase scans, or release gates. Repository-specific controls remain authoritative.

## Organizational maturity claims

Repository maturity is not organizational AI maturity. A repository label describes the development, release, or evidence state of a repository. An organizational maturity claim describes an organization's position under a named framework and version.

For a public organizational-maturity claim, review:

- exact framework identity and version;
- assessment scope;
- partial coverage versus full-framework coverage;
- claimed maturity level;
- accountable human-determined level, when present;
- evidence-supported level, only if the evidence gate carries that human determination;
- evidence references;
- freshness;
- representativeness;
- contradictions;
- material-change and reassessment state;
- limitations;
- attribution and framework-license boundary;
- delivery and release state.

An evidence-supported level is not an autonomous machine determination of organizational maturity. `VERIFIED` does not mean certified, compliant, safe, legally approved, or deployment-authorized. Automated output does not transfer authority. `SHIPPED` still requires the repository's authorized release action.

## Automation boundary

The machine-readable convention and validator in this repository verify only the shared control files. They do not scan or govern every account repository automatically. Adoption and enforcement remain explicit per repository, and humans retain authority for claim and release promotion.
