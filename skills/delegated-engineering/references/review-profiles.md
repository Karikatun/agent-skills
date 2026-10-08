# Adaptive review profiles

For conditional FULL review; core invariants are in [SKILL.md](../SKILL.md), review types/bindings/snapshot/runtime proof in [evidence contracts](evidence-contracts.md).

Select relevant profiles only: trust/auth/API, concurrency/async, persistence/migration, external I/O/errors, lifecycle/resources, types/contracts, UI/accessibility, operations/data preservation, agent-skill/supply-chain/install/update (the latter uses the applicable security skill).

| Level | When | Flow |
| --- | --- | --- |
| LOW | trivial deterministic reversible; no controlling independent-review rule | worker check/validation |
| MEDIUM | bounded behavior risk or controlling independent-review rule | fresh compatible read-only review covering required gates |
| HIGH | trust/security, concurrency, persistence/migration, shared contract, high operational risk | fresh qualified specialist(s) for distinct independent gates; whole-scope only for remaining gates |

Map required acceptance/risk gates to each reviewer before assignment. Review depth follows that responsibility, not the presence of a review abstraction. HIGH requires specialist competence for applicable security/concurrency/persistence/shared-contract risks; never replace independent gates with worker self-checks. A specialist can close all matching gates it covers. Add a fresh whole-scope review only for uncovered cross-cutting gates, a controlling rule, or final integration risk beyond the specialist scope. Multiple reviewers need different independent responsibilities; do not duplicate the same property without a stated reason. Before adding a reviewer name the still-open gate and expected new evidence; none means stop reviewing.

Reviewers independently preflight originals, receive immutable final snapshot/scope/acceptance/profiles/compact receipts without prior conclusions, and report findings/compliance. They never write/fix/stage/integrate/delegate. No duplicate reviewers to vote; the five-round stopping bound below is a rework safeguard, never a reviewer count target.

Fixes follow [execution's ordered fix lifecycle](execution.md#fix-and-integration-order). After a relevant write, no reuse of implementation context for review; obtain required fresh final review after affected validation. Out-of-scope findings pause for authority. Snapshot/control drift and reusable evidence follow the canonical [evidence contract](evidence-contracts.md#efficient-evidence-reuse).

At most five completed whole-scope rounds per run: a clean fifth may finish; defect/unresolved issue in it -> `BLOCKED_REVIEW_LIMIT`. Required review exact-matches its bound rule, stable ref, immutable digest, profile and round. Compare agent with primary-ledger agent sets and session with session sets. Context/freshness/isolation/enforced read-only claims require primary-validated runtime refs; policy read-only remains mandatory. Record limitations without inventing proof; identity is required for a claim that depends on it.
