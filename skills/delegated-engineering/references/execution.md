# Execution, validation, and release

Apply [SKILL.md](../SKILL.md)'s canonical invariants. This reference governs mutation lifecycle only; contracts are defined in [evidence contracts](evidence-contracts.md).

## Mutation lifecycle

Use only needed states: `ROUTING -> EXECUTING -> INTEGRATING? -> VALIDATING? -> REVIEWING? -> FINALIZING -> LOCAL_READY`. Discovery/planning precede execution only when routed; read-only and plan-only end at `EVIDENCE_COMPLETE` or `PLAN_COMPLETE`. Truthful stops include `PAUSED_AUTHORITY`, `PAUSED_CAPABILITY`, `PAUSED_ENVIRONMENT`, `BLOCKED_UNRESOLVED`, and `BLOCKED_REVIEW_LIMIT`.

Workers own exact writes and smallest meaningful local checks. Validators prove acceptance and required gates without fixing defects. An integrator is used only when authorized and owns only assigned conflicts, generated files, staging, commits, and integration validation. Recheck relevant dirty paths before assignment and completion.

If a relevant pre-existing dirty path overlaps a write, bind a targeted immutable baseline and prove three-way or semantic preservation; replacing its exact prior identity needs explicit authority. No overlap means no WIP evidence structure. If the snapshot/comparison cannot be made, pause rather than claiming preservation.

Instruction or required-skill identity drift invalidates affected preflight and evidence. Re-read the controlling originals, then targeted-revalidate or replan according to impact; the changed source does not authorize itself.

## Fixes, validation, integration

After a review finding, the primary creates an authorized fix node. The same worker may continue only under the safe-reuse conditions in [planning](planning.md); otherwise use a fresh worker. Validate the fix, then obtain the required fresh re-review. A worker never self-closes a reviewer requirement.

Integrate only after scopes/contracts are compatible and explicit integration authority exists. Only authorized integrator/release roles may mutate index/refs; validate after. Resolve only assigned conflicts; preserve unrelated WIP. Local checks and validation prove no remote, release, or live state.

## Release boundary

Release work requires explicit authority, a delegated release agent, independently read applicable runbooks, and separate evidence for each requested step: push, remote SHA/CI, merge, deploy, and live verification. Do not infer any later state from `LOCAL_READY`.
