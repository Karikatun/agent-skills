# Planning and routing

For FULL work; route/model/effort policy is canonical in [SKILL.md](../SKILL.md), types in [evidence contracts](evidence-contracts.md).

## Classification and necessary phases

Set `mode`: `read_only|mutation|plan_only|release`; `complexity`: `TRIVIAL|LOCAL|COMPLEX|HIGH_RISK|EXTREME`. Judge uncertainty, blast radius, reversibility, security/operations/architecture/contracts/persistence/concurrency and unknown behavior, not request size or token budget. Optional `task_class` supplements risk/complexity (for example mechanical, local lookup/edit/bug, bounded implementation, complex debugging, shared contract, architecture, security, persistence, migration, concurrency or release).

Reason codes for an added agent/phase/stronger model: `unknown_location`, `unknown_behavior`, `deterministic_local_edit`, `bounded_implementation`, `architectural_choice`, `shared_contract`, `security_boundary`, `persistence_change`, `migration`, `concurrency`, `high_blast_radius`, `independent_review_required`, `release_boundary`, `capability_escalation`, `instruction_requirement`. Explain only when the code is insufficient.

Before an agent/discovery/planner/review/snapshot/expensive check, identify the unresolved question and how its result changes acceptance or a decision; skip work without marginal value. [Evidence reuse](evidence-contracts.md#efficient-evidence-reuse) determines validity; revalidate only affected inputs. An explorer is read-only, answering one exact flow/question with tests, constraints, risks and unknowns. Skip discovery when location/current behavior are established. Skip a planner when implementation is obvious and has no architectural choice, dependent/shared/cross-layer contract, security, migration, concurrency, persistence, high blast radius or unclear approach; workers decide ordinary local details.

Create a lazy `TaskGraph` only when multiple substantive nodes are necessary, adding real dependencies as they arise. Unblock the critical path, cheaply test a concrete risky hypothesis, and close mandatory acceptance; no speculative fallbacks/phases/agents.

## Assignments and safe reuse

Bind exact scope/ownership/responsibility, original sources/skills/rules, acceptance, checks/review, relevant evidence, model/effort/reason code and `delegation: forbidden`. Children independently preflight originals; receipts/handoffs do not substitute. HARDENED bindings come from the core trigger. Compatibility exceptions use [reasoning effort](reasoning-effort.md), not a second routing table.

Reuse a worker only while scope, ownership, authority/skill identities, risk and responsibility are unchanged, no independence is required, model/effort fits, and agent/session exactly match the primary-owned runtime ledger. Review, changed ownership/responsibility/material scope/risk, instruction drift, insufficient model, unreliable evidence or independent specialist work requires a fresh agent. Record identity limitations; fresh work needs no identity claim, reuse/independence does. Compare each receipt's expected sources/skills/rules/checks with actual read/applied/evidenced results; escalation updates only its affected node.

## Ready work and capacity

Parallelism is an optimization, never a gate or reason to fill slots. Run only independent ready nodes: no dependencies, overlapping writes, unresolved shared design or conflict risk. Use `pending|running|completed`, no scheduler agent. FAST has one child; ordinary FULL prefers 1–2 concurrent substantive children. Unknown global capacity means desired parallelism 2; session slots do not prove availability across chats or justify hardcoded platform limits.

3+ concurrent children require independent ready work, known live capacity and critical-path benefit exceeding new context cost. Prefer sequential safe reuse for short/high-context-overlap work. Capacity/rate/temporary spawn denial keeps the node pending: continue existing work, retry when capacity frees or execute sequentially; never classify it as failure/model insufficiency or raise settings.

## Progress and stopping

For every FULL mode, primary keeps compact in-memory `ProgressState`: `{acceptance_open, blockers, active_hypothesis?, next_decision?, last_material_progress?}`; no file/ledger/agent. Each substantial step advances a named open acceptance/blocker. A cycle must produce task-relevant evidence, change, check result, concrete blocker, resolved cause or closed substantive node; preparation/context/snapshot/plan refresh alone is no progress.

After two consecutive cycles without material progress, stop repeating: state known facts, isolate the unresolved assumption and choose a different diagnostic toward nearest open acceptance. Long work may continue while closing real work; no arbitrary cutoff. Fix noisy infrastructure/root causes before rerunning symptoms. The core model gate distinguishes reasoning shortfall from capability/environment gaps.

For long work, report approximate weighted acceptance milestones: discovery/root cause 1; needed planning 1; implementation 2–4; needed integration 1–2; validation 1; required review 1; final gate 1. These are guides, not a scoring engine or reason for extra checks. On closed milestones or changed acceptance/blocker/critical path/material scope, show completed/current/next verifiable result. Explain any progress reduction after scope expansion. Use native progress UI only with live support, otherwise compact text; never count time/calls/messages/files/agents as progress.

The [core completion gate](../SKILL.md#self-contained-fast-protocol) ends the work when required evidence is sufficient; no optional audit/cleanup/polish or repeated preparation afterward.
