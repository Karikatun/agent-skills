# Adaptive review profiles

For conditional FULL review; core invariants are in [SKILL.md](../SKILL.md), review types/bindings/snapshot/runtime proof in [evidence contracts](evidence-contracts.md).

Select relevant profiles only: trust/auth/API, concurrency/async, persistence/migration, external I/O/errors, lifecycle/resources, types/contracts, UI/accessibility, operations/data preservation, agent-skill/supply-chain/install/update (the latter uses the applicable security skill).

| Level | When | Flow |
| --- | --- | --- |
| LOW | trivial deterministic reversible; no controlling independent-review rule | worker check/validation |
| MEDIUM | bounded behavior risk or controlling independent-review rule | fresh Luna read-only final-scope review |
| HIGH | trust/security, concurrency, persistence/migration, shared contract, high operational risk | justified specialist read-only review -> fresh whole-scope review |

Reviewers independently preflight originals, receive immutable final snapshot/scope/acceptance/profiles/compact receipts without prior conclusions, and report findings/compliance. They never write/fix/stage/integrate/delegate. No duplicate reviewers to vote.

Fixes follow [execution's ordered fix lifecycle](execution.md#fix-and-integration-order). After a relevant write, no reuse of implementation context for review; obtain required fresh final review after affected validation. Out-of-scope findings pause for authority. Snapshot/control drift and reusable evidence follow the canonical [evidence contract](evidence-contracts.md#efficient-evidence-reuse).

At most five completed whole-scope rounds per run: a clean fifth may finish; defect/unresolved issue in it -> `BLOCKED_REVIEW_LIMIT`. Required review exact-matches its bound rule, stable ref, immutable digest, profile and round. Compare agent with primary-ledger agent sets and session with session sets. Context/freshness/isolation/enforced read-only claims require primary-validated runtime refs; policy read-only remains mandatory. Record limitations without inventing proof; identity is required for a claim that depends on it.
