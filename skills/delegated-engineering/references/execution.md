# Adaptive Execution

## State machine

Use only the states the selected workflow needs:

```text
ROUTING -> DISCOVERING? -> DISCOVERED? -> PLANNING? -> PLAN_READY?
        -> EXECUTING -> INTEGRATING? -> VALIDATING? -> REVIEWING? -> FINALIZING -> LOCAL_READY
```

Trivial work may be `ROUTING -> EXECUTING -> FINALIZING -> LOCAL_READY`; a local bug may be `ROUTING -> DISCOVERING -> EXECUTING -> VALIDATING -> FINALIZING`. Plan-only/read-only work terminates at `PLAN_COMPLETE`/`EVIDENCE_COMPLETE`. Pause or block truthfully at `PAUSED_AUTHORITY`, `PAUSED_CAPABILITY`, `PAUSED_ENVIRONMENT`, `BLOCKED_UNRESOLVED`, or `BLOCKED_REVIEW_LIMIT`. Release facts are never collapsed: `LOCAL_READY`, `REMOTE_SHA_CI_VERIFIED`, `MERGED`, `DEPLOYED`, and `LIVE_VERIFIED` require separate evidence.

## TaskContract and roles

The compact TaskContract contains `run_id`, baseline HEAD/branch/dirty paths, active scope, allowed/approval-required/forbidden actions, authority ledger, InstructionManifest and original paths, mandatory skills, acceptance, selected checks, review requirements, and current TaskGraph/nodes. Recheck relevant dirty paths before assignment and completion. Do not reset, stash, revert, or overwrite unrelated WIP.

Roles are separate when risk needs independence:

- Explorer: read-only targeted behavior/code/test evidence; no implementation or delegation.
- Planner: produces a compact solution/TaskGraph only when required; no implementation or delegation.
- Worker: owns exact writes and smallest meaningful local checks.
- Validator: proves acceptance and required gates; it does not fix defects without a new node.
- Reviewer: read-only snapshot/instruction-compliance review; it never writes.
- Integrator: only when explicitly authorized, owns assigned conflicts, generated files, staging, commits, and integration validation; the primary never stages or commits.
- Release agent: acts only with explicit release authority and independently read runbook.

For trivial low-risk work a worker check can suffice. For nontrivial work separate worker, validation, and review according to risk and controlling rules. A shared contract validates both producer and consumer.

## Instruction preflight, matrix, and drift

Every assigned agent independently reads each original source in its effective chain plus triggered skills/runbooks before substantive work, then returns a preflight receipt. Primary maintains a compact matrix:

```text
TaskNode -> expected sources/skills/checks/reviews -> confirmed sources/skills/checks -> status
```

Require `expected_sources == sources_read`, `expected_skills == skills_read`, and required checks/reviews to be complete. Missing or inaccessible authority is an `instruction`/`capability` gap; it invalidates affected work rather than being backfilled in prose. If an instruction identity changes, invalidate affected preflight and evidence, reload originals, then revalidate or replan as impact requires. Existing authority controls whether a changed instruction applies; it cannot self-authorize.

## Validation, review, and release

Workers perform the smallest meaningful checks; validators run required project gates and explicit acceptance tests. The primary inspects receipts/targeted orchestration claims, never performs engineering validation itself. Choose review adaptively: LOW = worker validation sufficient; MEDIUM = fresh Luna review; HIGH = specialist review where applicable then fresh whole-scope review. Follow [review-profiles.md](review-profiles.md).

After a reviewer finding, primary creates a separate fix TaskNode -> worker -> validator -> new immutable review snapshot. Any write invalidates clean review evidence. At most five whole-scope rounds run per `run_id`; a defect or unresolved issue on round five becomes `BLOCKED_REVIEW_LIMIT`. Out-of-scope findings require authority and pause; no role self-authorizes a fix.

Release never follows from local readiness. Push, remote CI/SHA confirmation, merge, deployment, production change, publication, and live proof require explicit authority and a delegated release agent that reads the applicable original runbook and returns a separate receipt.
