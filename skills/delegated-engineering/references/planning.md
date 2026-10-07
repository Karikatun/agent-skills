# Planning and routing

This reference is for FULL work. Apply the core invariants and model table in [SKILL.md](../SKILL.md); schemas live only in [evidence contracts](evidence-contracts.md).

## Classify the needed work

Set `mode`: `read_only`, `mutation`, `plan_only`, or `release`. Set `complexity`: `TRIVIAL`, `LOCAL`, `COMPLEX`, `HIGH_RISK`, or `EXTREME`. Judge uncertainty, blast radius, reversibility, security/operational/architecture/contract/persistence/concurrency risk, and unknown behavior—not request size or token budget. Optionally label `task_class` for routing/outcomes: `mechanical`, `local_lookup`, `local_edit`, `local_bug`, `bounded_implementation`, `complex_debugging`, `shared_contract`, `architecture`, `security`, `persistence`, `migration`, `concurrency`, or `release`. It supplements, never replaces risk/complexity.

Use a compact reason code when adding an agent, phase, or model: `unknown_location`, `unknown_behavior`, `deterministic_local_edit`, `bounded_implementation`, `architectural_choice`, `shared_contract`, `security_boundary`, `persistence_change`, `migration`, `concurrency`, `high_blast_radius`, `independent_review_required`, `release_boundary`, `capability_escalation`, or `instruction_requirement`. Add prose only if the code is insufficient.

## Discover and plan only when needed

Before a new agent/discovery/planner/review/snapshot/expensive check, identify the unresolved question and how its result changes a decision or acceptance; skip steps without marginal value. Reuse evidence while relevant inputs/content, baseline/WIP, scope, instructions/authority/skills, contracts, behavior and required independence remain valid; targeted-revalidate only what was invalidated. An explorer is read-only and answers one exact flow/question, including relevant tests, constraints, risks, and unknowns.

Skip discovery when exact location and current behavior evidence are known. Skip a planner when the implementation is obvious and has no architectural choice, dependent node, shared/cross-layer contract, security concern, migration, concurrency, persistence change, high blast radius, or unclear approach. A worker may decide ordinary local details.

Create a lazy `TaskGraph` only after more than one substantive node is necessary; add dependencies only when they become real. Prioritize the critical path: unblock dependencies, test a concrete risky hypothesis cheaply before expensive work, and close mandatory acceptance. No speculative fallback designs, phases or agents.

## Prepare or reuse an assignment

Each assignment has exact scope/ownership, applicable original sources/skills/rules, acceptance, required checks/review, relevant evidence, routing/model/effort/reason code, and `delegation: forbidden`. Select a supported model/effort pair for this node separately from workflow and risk mode. Use [reasoning effort](reasoning-effort.md) when detailed level selection or client configuration affects the assignment. The agent independently preflights originals; a handoff or prior receipt never substitutes. Apply HARDENED bindings only when the router trigger applies.

Before respawn, continue the same worker only if its scope, ownership, authority/skill identities, risk, and responsibility are unchanged, no independence is required, its current model/effort configuration fits the assignment, and its agent/session exactly match the primary-owned runtime ledger. Otherwise use a fresh worker and record the identity limitation. A new agent is required for review, changed responsibility/ownership, material scope/risk change, instruction drift, insufficient model, unreliable evidence, or an independent specialist profile. Identity is required only for a reuse or independence claim; otherwise record its runtime status as unknown rather than inventing proof.

Client-specific inheritance/continuation limits live in [reasoning effort](reasoning-effort.md). If continuation cannot apply the required pair, use a compatible new assignment; prose cannot change settings.

## Schedule ready work conservatively

Parallelism optimizes completion; it is never a gate. Run only independent ready nodes: no dependency, overlapping writes, unresolved shared design decision or conflict risk. Keep simple `pending|running|completed` states, no scheduler agent. FAST uses one child; ordinary FULL prefers 1–2 substantive children concurrently. If global capacity is unknown, desired substantive parallelism is 2; session slots do not establish global availability across chats. Never fill slots merely because they exist or hardcode platform limits.

3+ concurrent children need enough independent ready work, known live capacity and a material critical-path benefit exceeding new-agent context cost. Prefer sequential safe reuse for short/high-context-overlap work. Capacity/rate/temporary spawn denial leaves the node pending: continue existing work and retry after capacity frees, or run sequentially. It is a scheduler constraint, not failure or evidence of model insufficiency; never raise model/effort for it.

After every receipt, compare expected sources/skills/rules/checks with what was read, applied, and evidenced. Update only the affected node after an escalation; do not prebuild contingencies.

## Progress and stopping

Primary keeps compact in-memory `ProgressState` (no ledger/file/agent): `{acceptance_open, blockers, active_hypothesis?, next_decision?, last_material_progress?}`. Before a substantial step, name the open acceptance/blocker it advances. Each cycle produces new task-relevant evidence, a change, acceptance-check result, concrete blocker, resolved cause or closed substantive node. Preparation/context/snapshot/plan refresh alone is no progress.

After two consecutive cycles without material progress, stop repeating that workflow: state known facts, isolate the unresolved assumption and choose a different diagnostic toward the nearest open acceptance. Long work is valid while it closes real work; no arbitrary time cutoff. Fix a noisy infrastructure/root cause before rerunning its symptoms; stronger reasoning helps only a demonstrated reasoning shortfall, never missing capability/environment.

For long tasks, report approximate weighted acceptance milestones: discovery/root cause 1, planning only if needed 1, implementation 2–4, integration if needed 1–2, validation 1, required review 1, final gate 1. These are guides, not a scoring engine; no extra checks to compute a percentage. Update on closed milestones, acceptance/blocker/critical-path or material scope changes, showing completed/current/next verifiable result. Scope expansion may lower progress with a short explanation. Native progress UI only if live capability exists; otherwise compact text. Never count time, calls, messages, files or agents as progress.

When acceptance, authority/WIP, required checks/reviews and all other mandatory gates are satisfied with no concrete blocker, finish. No optional audit, cleanup, polish or repeated preparation after sufficient evidence. Optimize accepted outcome per total wall-clock and usage, not maximum process completeness.
