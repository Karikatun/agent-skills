# Execution, validation, and release

For FULL mutation/validation/integration/release; apply [core invariants](../SKILL.md), [evidence contracts](evidence-contracts.md) and shared [progress/stopping](planning.md#progress-and-stopping).

## Mutation lifecycle and WIP

Use needed states only: `ROUTING -> EXECUTING -> INTEGRATING? -> VALIDATING? -> REVIEWING? -> FINALIZING -> LOCAL_READY`. Discovery/planning precede execution only when routed; read-only/plan-only finish at `EVIDENCE_COMPLETE`/`PLAN_COMPLETE`. Truthful stops: `PAUSED_AUTHORITY`, `PAUSED_CAPABILITY`, `PAUSED_ENVIRONMENT`, `BLOCKED_UNRESOLVED`, `BLOCKED_REVIEW_LIMIT`.

Workers own exact writes and smallest meaningful local checks. Validators prove gates without fixing. An authorized integrator owns only assigned conflicts/generated files/staging/commits/integration validation. Recheck relevant dirty paths before assignment and completion. Overlapping pre-existing WIP requires a targeted immutable baseline and three-way or semantic preservation; replacing its exact identity needs explicit authority. No overlap means no WIP evidence structure. Unavailable safe snapshot/comparison means pause, never claimed preservation.

## Fix and integration order

Review finding -> primary-authorized fix node -> worker satisfying [safe reuse](planning.md#assignments-and-safe-reuse), otherwise fresh worker -> affected validation -> required fresh re-review. A worker cannot self-close required review. Reuse/invalidations follow [evidence contracts](evidence-contracts.md#efficient-evidence-reuse); avoid extra unchanged preparation/snapshot/check cycles.

Integrate only after compatible scopes/contracts and explicit integration authority; only authorized integration/release roles mutate index/refs, then validate. Never stage for internal checkpoints, snapshots, WIP preservation, handoffs or review preparation. Resolve assigned conflicts only; local gates prove no remote/release/live state.

## Release boundary

Explicit release authority, delegated release responsibility and independently read original runbooks are prerequisites. Preserve their procedural order and stopping conditions; bind each authorized transition and verify its result before a dependent step. Push, remote SHA/CI, merge, deploy and live verification each need separate evidence and authority; `LOCAL_READY` proves none of them. No later release action is implied by an earlier one.
