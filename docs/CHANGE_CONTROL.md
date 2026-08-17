# Change Control

Use the lightest process that preserves correctness, evidence, and recovery.

A substantial change should answer six questions before merge:

1. **Need** — why is the change necessary?
2. **Impact** — what behavior, evidence, interface, or public claim can change?
3. **Proof** — what validation supports the candidate?
4. **Boundary** — what does the evidence not establish?
5. **Recovery** — how can the change be reverted, superseded, or revalidated?
6. **Disposition** — merge, hold, rework, or require renewed authorization.

High-impact changes should not be auto-merged merely because CI is green.
