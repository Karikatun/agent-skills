# Execution, validation, and release

For FULL mutation/validation/integration/release; apply [core invariants](../SKILL.md), [evidence contracts](evidence-contracts.md) and shared [acceptance/stopping](planning.md#acceptance-and-stopping).

## Mutation lifecycle and WIP

Use needed states only: `ROUTING -> EXECUTING -> INTEGRATING? -> VALIDATING? -> REVIEWING? -> FINALIZING -> LOCAL_READY`. Discovery/planning precede execution only when routed; read-only/plan-only finish at `EVIDENCE_COMPLETE`/`PLAN_COMPLETE`. Truthful stops: `PAUSED_AUTHORITY`, `PAUSED_CAPABILITY`, `PAUSED_ENVIRONMENT`, `BLOCKED_UNRESOLVED`, `BLOCKED_REVIEW_LIMIT`.

Workers own exact writes and smallest meaningful local checks. Validators prove gates without fixing. An authorized integrator owns only assigned conflicts/generated files/staging/commits/integration validation. Before mutation bind intended scope, relevant dirty/WIP and cheap controls; after mutation verify actual writes, affected scope and controls under [scoped evidence](evidence-contracts.md#evidence-levels-and-coverage). Expand only on named risk/anomaly. Recheck relevant dirty paths before assignment and completion. Overlapping pre-existing WIP requires a targeted immutable baseline and three-way or semantic preservation; replacing its exact identity needs explicit authority. No overlap means no WIP evidence structure. Unavailable safe snapshot/comparison means pause, never claimed preservation.

## Checks and first diagnostics

Use the existing runner/tool, not a helper project. Capture `CheckResult` ([contract](evidence-contracts.md#runner-results)) during normal execution; failure output accompanies its result for the next node. No extra collector, wrapper, executor or wrapper reviewer just to see already-returned output. A helper is justified only by a demonstrated output-retention capability gap and scoped engineering authority. Run the exact useful failing check before broad diagnosis; preserve actual failure rather than rerun merely to recollect it. Secret redaction and bounded retention apply to success and failure alike.

## Fix and integration order

Review finding -> primary-authorized fix node -> worker satisfying [safe reuse](planning.md#assignments-and-safe-reuse), otherwise fresh worker -> affected validation -> required fresh re-review. A worker cannot self-close required review. Reuse/invalidations follow [evidence contracts](evidence-contracts.md#efficient-evidence-reuse); avoid extra unchanged preparation/snapshot/check cycles.

Integrate only after compatible scopes/contracts and explicit integration authority; only authorized integration/release roles mutate index/refs, then validate. Never stage for internal checkpoints, snapshots, WIP preservation, handoffs or review preparation. Resolve assigned conflicts only; local gates prove no remote/release/live state.

## Release boundary

Explicit release authority, delegated release responsibility and independently read original runbooks are prerequisites. Preserve their procedural order and stopping conditions; bind each authorized transition and verify its result before a dependent step. Push, remote SHA/CI, merge, deploy and live verification each need separate evidence and authority; `LOCAL_READY` proves none of them. No later release action is implied by an earlier one.
