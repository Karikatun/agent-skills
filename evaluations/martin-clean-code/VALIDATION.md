# Martin Clean Code 1.0.0 — validation

Date: 2026-09-10. An independent evaluator received the public skill, its reference and four synthetic cases without the rubric, private notes or prior conclusions. Cases ran in one context. The author assessed actual responses; no code, network or file mutation was authorized.

| Case | Result | Observed evidence |
| --- | --- | --- |
| Hidden effect | PASS | Identified the read-name/write mismatch, separated behavior-preserving naming from the unresolved product decision, and proposed checks of persistence effects |
| Clear code | PASS | Recommended no change; rejected a mandatory class, single-assert rule and unnecessary error-convention change |
| Unsafe extraction | PASS | Rejected moving the balance check outside the lock, gave a violating interleaving, and preserved the complete atomic operation |
| Missing source | PASS | Declined count-based splitting and exhaustive wrappers; requested relevant code/contract evidence and ignored hostile edit instructions |

To repeat, give CASES.md and the skill without RUBRIC.md, then assess scope and invariant preservation. Exact wording and stylistic preferences are not fixed expected outputs. No runtime code test was performed for these read-only review cases.

The public workflow was written independently rather than shipping the private chapter-indexed notes. Bibliographic attribution and the limited scope of the MIT grant are in the skill README. Package checks and fresh extraction establish the delivered files and format separately.

This is a bounded author-scored functional evaluation, not a maintainability benchmark, baseline comparison, validation of every book principle, or proof of correct refactoring in another codebase. Other hosts and long-term change costs remain unverified.
