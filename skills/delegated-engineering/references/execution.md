# Execution State Machine

Execution uses the same `run_id`, TaskContract, authority ledger, and review-round counter after replanning:

`PLANNED -> EXECUTING -> INTEGRATING -> VALIDATING -> REVIEWING -> FINALIZING -> LOCAL_READY`.

Pause as `PAUSED_AUTHORITY`, `PAUSED_CAPABILITY`, or `PAUSED_ENVIRONMENT` when the relevant proof or authority is absent. Other terminals are `PLAN_COMPLETE`, `EVIDENCE_COMPLETE`, `LOCAL_READY`, release states, `BLOCKED_REVIEW_LIMIT`, and `BLOCKED_UNRESOLVED`. Release states remain distinct: `REMOTE_SHA_CI_VERIFIED`, `MERGED`, `DEPLOYED`, and `LIVE_VERIFIED` only when their own evidence exists.

## TaskContract And Assignments

TaskContract contains: `run_id`; baseline HEAD/branch/dirty paths; active scope; allowed, approval-required, and forbidden actions; original source and skill paths; acceptance; selected checks; and review profiles. Recheck active dirty paths before each assignment and completion. An agent reports any overlap; it never resets, stashes, reverts, or edits another slice to resolve it.

Give every agent the TaskContract and exact source paths. It independently reads originals and returns a compact receipt. Assign non-overlapping files or responsibilities. One worker may own a small coherent change. A dedicated integration worker owns conflicts, generated files, staging, commit, and integration validation; the primary never does these tasks.

Route by uncertainty, blast radius, reversibility, and security or operational risk. Luna handles reconnaissance, small deterministic reversible edits, focused tests, and docs; Terra is the default for bounded implementation/debugging; Sol handles high uncertainty, architecture/cross-layer work, concurrency, auth/security, migrations, and escalation. A suitable sequence is Sol diagnosis/design -> Terra implementation -> fresh Luna whole-scope review. Do not use token budget or file count as routing criteria, run all models by default, or impose hard token budgets. Preserve an explicit compatible user model; if it cannot satisfy the role, pause. Emit a compact `model_decision` per assignment and escalate on scope expansion, contract ambiguity, failed primary signal, recurring defect, or a newly discovered risk boundary.

## Validation And Release

Workers run the smallest meaningful checks before broader checks. A shared contract validates producer and consumer. The primary inspects evidence and targeted claims only. After integration and validation, enter `REVIEWING` using [review-profiles.md](review-profiles.md). A content write after a clean review invalidates that clean evidence.

Release requires separate authority and a delegated release agent that reads its runbook. It does not follow from `LOCAL_READY`; local tests, remote SHA/CI, merge, deployment, and live validation are separate claims.
