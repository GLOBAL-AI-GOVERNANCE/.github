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

## Automation boundary

The machine-readable convention and validator in this repository verify only the shared control files. They do not scan or govern every organization repository automatically. Adoption and enforcement remain explicit per repository, and humans retain authority for claim and release promotion.
