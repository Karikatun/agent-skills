# Resource-Aware Planning

The primary orchestrates only. It creates the run record, resolves authority and instruction scope, classifies risk, selects the next necessary role, and structurally checks receipts. It does not discover code, choose a technical solution, create a substantive implementation plan, or review engineering work.

## Classification and shortest sufficient flow

Classify from uncertainty, blast radius, reversibility, security/operational/architecture/contract/persistence/concurrency risk, and unknown behavior—not file count or token budget.

| Class | Sufficient default | Add only with a recorded reason |
| --- | --- | --- |
| `TRIVIAL` | Luna worker -> smallest meaningful check | Discovery, planner, validator, or reviewer only if authority/risk requires it |
| `LOCAL` | valid evidence or Luna explorer -> Luna/Terra worker -> targeted validation | Fresh review when risk or project rules justify it |
| `COMPLEX` | targeted explorers -> Terra/Sol planner -> Terra workers -> validation -> fresh Luna review | Specialists only for a distinct profile |
| `HIGH_RISK` | targeted Luna/Terra explorers -> Sol planner -> Terra/Sol nodes -> validators -> specialist review -> fresh whole-scope review | Parallel work only after contracts and scopes are independent |
| `EXTREME` | the smallest high-risk graph that resolves the node | Astra only for a specific node after concrete Sol-insufficiency evidence |

Luna is the default for focused discovery, deterministic edits, documentation, focused tests/validation, and low-risk review. Terra handles bounded implementation/debugging and ordinary planning. Sol handles high uncertainty, architecture, shared contracts, auth/security, concurrency, migration, persistence, or high operational risk. Astra is never selected for request size, number of files, or large context. Escalate only an affected node from Luna -> Terra -> Sol -> Astra with evidence of insufficiency or risk; do not promote the whole run.

For discovery use the built-in `agent_type: explorer`, preferably `model: gpt-5.6-luna` and `fork_turns: none`; its question names exact flow, producer/consumer boundaries, tests, constraints, risk surfaces, and unknowns. It is read-only, does not implement, and does not delegate.

## Decision flow and skip rules

```text
ROUTING
  -> resolve authority + InstructionManifest + baseline
  -> one cheap worker safely sufficient? yes: assign
  -> otherwise valid exact discovery evidence? yes: reuse
  -> otherwise targeted explorer
  -> separate planning needed? no: worker; yes: Terra/Sol planner
  -> create only needed TaskNodes -> validate as required -> review only if required
```

Skip an explorer only when location/scope and enough current behavior evidence are known. Before launching one ask: "Do we already have valid evidence for this exact question?" Reuse only if HEAD, branch, relevant dirty paths, scope, relevant contracts, and behavior still match; change invalidates it and requires targeted revalidation or discovery.

Skip a planner when the implementation is obvious and there is no architectural choice, dependent nodes, cross-layer behavior, shared contract, security-sensitive work, migration, concurrency, persistence change, high blast radius, or unclear approach. A worker may resolve ordinary local implementation details. Do not create agents for voting or ceremony.

## InstructionManifest and effective chain

Before substantive work create an `InstructionManifest` from original controlling sources. It records pointers/identities, not copied rules. Derive the minimum complete effective chain per TaskNode: `/repo/AGENTS.md -> /repo/frontend/AGENTS.md -> /repo/frontend/components/AGENTS.md` for a component node; a backend node receives only its applicable chain. Resolve and include mandatory skill triggers, required runbooks, checks, and profiles. Every agent independently reads its originals; a compact handoff never substitutes.

An identity change in `AGENTS.md`, a mandatory skill, runbook, validation/security policy, or other authority source invalidates affected instruction preflight. Reload then targeted-revalidate or replan according to impact. The changed source cannot grant authority to itself.

## Lazy TaskGraph and parallelism

Create a TaskGraph only when more than one substantive TaskNode is needed; add nodes as dependencies become real. Each node has exact scope and exclusive ownership. Parallelism needs demonstrated independent scope and already-defined shared contracts: independent explorers for different questions, or backend/frontend/docs workers for non-overlapping writes. Never parallelize planner with dependent implementation or allow writers in overlapping scope. No consensus voting among duplicate planners/reviewers.

## Assignment preparation and escalation

Before every child assignment:

1. Fix exact TaskNode scope and ownership.
2. Resolve controlling authority and effective `AGENTS.md` chain.
3. Resolve mandatory skills, runbooks, checks, and review profiles.
4. Decide evidence reuse or targeted discovery.
5. Choose the cheapest sufficient model and explain why.
6. Send only necessary context plus original authority paths and acceptance.
7. Set `delegation: forbidden`, request instruction preflight, and use `fork_turns: none` where supported.

After return, compare expected sources/skills/checks to the receipt, check ownership and evidence freshness, and route only the next necessary node. A child returns `ESCALATION_REQUIRED` for scope expansion, unknown dependency/component, ownership conflict, new risk boundary, contract/API/persistence ambiguity, recurring defect, failed primary signal, unavailable capability, or insufficient model. The primary updates only the affected graph/node and may rediscover, plan, or escalate its model.
