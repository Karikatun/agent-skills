# Review Profiles And Immutable Rounds

Select only profiles supported by active scope: client/server trust; authentication/API; concurrency/async; persistence/transactions/migrations; external I/O/errors; lifecycle/resources; types/contracts; UI/accessibility/responsive/rendered flow; operations/release/data preservation; or agent-skill/supply-chain/install-update. The applicable security skill selects the current OWASP source for the last profile.

## Whole-Scope Review

A review round is one immutable snapshot. A fresh Luna, write-capable worker-role reviewer with `model: gpt-5.6-luna` and `fork_turns: none` reads originals and reviews `base..HEAD`, staged, unstaged, and relevant untracked changes, separating task scope from preserved WIP. Give it the TaskContract, final acceptance, and selected profiles, but no prior review conclusions; then run independent Terra or Sol specialists only when the profile or risk requires them. The quality floor remains model-independent; route specialists by uncertainty, blast radius, reversibility, and security or operational risk.

The round counter increments only when the fresh whole-scope reviewer completes. A failed spawn is not a round. For a read-only review, report findings and finish at `EVIDENCE_COMPLETE`; no reviewer fixes or loop occur.

For an authorized mutation, an in-scope finding is fixed and validated by that same reviewer, then a new immutable snapshot gets a new fresh reviewer. Any write invalidates earlier clean evidence. An out-of-scope finding pauses at `PAUSED_AUTHORITY`; do not edit or route it as implicitly authorized.

## Limits And Replanning

At most five whole-scope rounds run per `run_id`. A clean fifth round may reach `LOCAL_READY`. A fix or unresolved finding in round five reaches `BLOCKED_REVIEW_LIMIT` and remains unreviewed. Replanning continues the same run, budget, history, and counter. Trigger replanning after the same defect class recurs after a claimed fix, or after two rounds without primary-signal improvement.

After `BLOCKED_REVIEW_LIMIT`, restart only on new explicit user instruction, a new `run_id`, and a materially changed plan; preserve earlier history. Unresolved non-authority work reaches `BLOCKED_UNRESOLVED`. A receipt-only repair without artifact writes does not consume a round.
