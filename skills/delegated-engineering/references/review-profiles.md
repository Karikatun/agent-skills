# Adaptive Review Profiles and Immutable Rounds

Review is a risk control, not a universal ceremony. Select only profiles relevant to active scope: client/server trust; authentication/API; concurrency/async; persistence/transactions/migrations; external I/O/errors; lifecycle/resources; types/contracts; UI/accessibility/rendered flow; operations/release/data preservation; or agent-skill/supply-chain/install/update. For agent tooling, use the applicable security skill and its current official-source procedure.

| Level | When | Required flow |
| --- | --- | --- |
| LOW | trivial, deterministic, reversible, no mandatory independent review | worker check/validation is sufficient |
| MEDIUM | bounded behavior/change risk or a controlling rule requires independence | fresh Luna read-only review of final scope |
| HIGH | trust/security, concurrency, persistence, migration, shared contract, or high operational risk | specialist read-only profile review where applicable, then fresh whole-scope review |

Do not run duplicate reviewers to vote. Add a specialist only for a distinct justified profile or capability.

## Immutable review flow

A reviewer is read-only. It independently reads original applicable instructions/skills, receives the final snapshot, acceptance, selected profiles, relevant scope, and compact receipts—not prior review conclusions—and reports findings and instruction compliance. It does not edit code, fix a finding, stage, integrate, or delegate.

For a whole-scope round use a fresh Luna reviewer with `fork_turns: none` where supported; route specialist reviewers to Luna/Terra/Sol by the profile risk, not by file count. Review the immutable assigned snapshot while separating task scope from preserved WIP. Record snapshot identity and increment the whole-scope counter only when the fresh whole-scope review completes.

Finding -> primary creates a separate authorized fix TaskNode -> worker fixes -> validator validates -> fresh reviewer inspects the new snapshot. Any write after a clean review invalidates that clean evidence. An out-of-scope finding is `PAUSED_AUTHORITY`, not an implicit repair.

At most five whole-scope rounds occur per `run_id`. A clean fifth round may reach `LOCAL_READY`; a defect/unresolved finding in round five is `BLOCKED_REVIEW_LIMIT`. Restart only with new explicit user direction, a new `run_id`, and a materially changed plan. Receipt-only repairs do not consume a round. Reviewers treat missing applicable-source reads, missed mandatory skills, required checks, security review, architecture boundaries, or nested `AGENTS.md` as findings; an instruction gap that could affect work invalidates the affected evidence and requires reassign/revalidate/review.
