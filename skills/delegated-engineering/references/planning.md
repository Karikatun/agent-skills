# Planning and routing

This reference is for FULL work. Apply the core invariants and model table in [SKILL.md](../SKILL.md); schemas live only in [evidence contracts](evidence-contracts.md).

## Classify the needed work

Set `mode`: `read_only`, `mutation`, `plan_only`, or `release`. Set `complexity`: `TRIVIAL`, `LOCAL`, `COMPLEX`, `HIGH_RISK`, or `EXTREME`. Judge uncertainty, blast radius, reversibility, security/operational/architecture/contract/persistence/concurrency risk, and unknown behavior—not request size or token budget.

Use a compact reason code when adding an agent, phase, or model: `unknown_location`, `unknown_behavior`, `deterministic_local_edit`, `bounded_implementation`, `architectural_choice`, `shared_contract`, `security_boundary`, `persistence_change`, `migration`, `concurrency`, `high_blast_radius`, `independent_review_required`, `release_boundary`, `capability_escalation`, or `instruction_requirement`. Add prose only if the code is insufficient.

## Discover and plan only when needed

Reuse evidence before discovery only while its baseline, relevant WIP, scope, authority/skill identities, contracts, and behavior remain valid; otherwise targeted-revalidate or rediscover. An explorer is read-only and answers one exact flow/question, including relevant tests, constraints, risks, and unknowns.

Skip discovery when exact location and current behavior evidence are known. Skip a planner when the implementation is obvious and has no architectural choice, dependent node, shared/cross-layer contract, security concern, migration, concurrency, persistence change, high blast radius, or unclear approach. A worker may decide ordinary local details.

Create a lazy `TaskGraph` only after more than one substantive node is necessary; add dependencies only when they become real. Parallelize only independently owned scopes with already-set shared contracts. Never run dependent planning/implementation together or overlapping writers.

## Prepare or reuse an assignment

Each assignment has exact scope/ownership, applicable original sources/skills/rules, acceptance, required checks/review, relevant evidence, routing/model/reason code, and `delegation: forbidden`. The agent independently preflights originals; a handoff or prior receipt never substitutes. Apply HARDENED bindings only when the router trigger applies.

Before respawn, continue the same worker only if its scope, ownership, authority/skill identities, risk, and responsibility are unchanged, no independence is required, and its agent/session exactly match the primary-owned runtime ledger. Otherwise use a fresh worker and record the identity limitation. A new agent is required for review, changed responsibility/ownership, material scope/risk change, instruction drift, insufficient model, unreliable evidence, or an independent specialist profile. Identity is required only for a reuse or independence claim; otherwise record its runtime status as unknown rather than inventing proof.

After every receipt, compare expected sources/skills/rules/checks with what was read, applied, and evidenced. Update only the affected node after an escalation; do not prebuild contingencies.
