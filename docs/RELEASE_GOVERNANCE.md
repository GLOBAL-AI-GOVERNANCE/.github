# Release Governance Convention

This convention sets the minimum for a public release in a GLOBAL AI GOVERNANCE repository. Adoption is explicit and per repository. A repository adopts it by linking this file from its own release policy or release record. A repository that has not adopted it is not governed by it.

Repository-local release policy is authoritative. Where a local rule is stricter or more specific, the local rule controls. This convention never relaxes a local requirement.

## Principles

- **Releases are repository-specific.** Each repository releases on its own evidence. There is no synchronized portfolio release, and one repository's release is not a prerequisite for another unless a causal dependency is documented.
- **Human authority is required.** A named human with release authority for the repository approves the tag, the release, and any change to published maturity or claim status.
- **Evidence precedes release.** Required evidence exists and is recorded before the tag is created.
- **CI alone is insufficient.** Passing checks are necessary evidence, not a release decision.
- **Merged is not released.** A merge, passing test, or generated artifact does not create a release or promote a claim.
- **Automation cannot promote release truth.** Tooling may verify a recorded decision. It may not create one.
- **Missing required evidence is NOT VERIFIED.** A required item without evidence is reported as `NOT VERIFIED`. It is not inferred, waived by silence, or carried over from another repository, client, or release.

## Minimum release record

Before a tag is created, the repository's release record states:

1. **Release authority.** The human who approves the release, and the date.
2. **Candidate.** The exact commit SHA to be tagged. The tag must point to that commit.
3. **Current CI.** Required checks passing on that exact commit.
4. **Claim review.** The public claims the release changes, the evidence for each, and what the evidence does not establish.
5. **Metadata consistency.** Version, changelog, citation, and README identify the same release.
6. **Maturity.** An explicit maturity statement, such as prerelease, release candidate, or stable.
7. **Limitations.** Known limitations and unsupported environments.
8. **Repository-specific gates.** Each local gate, with its evidence or its `NOT VERIFIED` status. A release does not proceed while a local blocking gate is `NOT VERIFIED`.
9. **Provenance, checksums, and SBOM.** Only where the repository's own policy requires them, and then as that policy specifies.

## After release

Confirm that the published tag, release, and public surfaces name the approved commit and the stated maturity. Record any discrepancy, and correct it without moving or reusing the published tag.

## Boundary

This convention is a process minimum. It does not certify a release, establish compliance or safety, or authorize production use.
