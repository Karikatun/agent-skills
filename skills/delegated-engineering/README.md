# Delegated Engineering

Version 2.0.0. A resource-aware repository-engineering workflow: the primary orchestrates; explorers discover; planners design only when necessary; workers implement; validators prove; read-only reviewers inspect independently; integrators and release agents act only in separately owned, authorized scopes. Project instructions bind every role.

The workflow minimizes agent count, model cost, and context size without lowering correctness or instruction-compliance. It never trades away applicable `AGENTS.md`, mandatory skills/runbooks, acceptance, security constraints, required validation, or required independent review. The package has instructions, references, and UI metadata only—no scripts, services, dependencies, installers, credential handling, or automatic updates.

Project-local mandatory skills require identity/integrity preflight before use. A skill transfer or update remains a separately authorized, rollback-protected operation: read-only source/staged review, executor activation, installed-manifest comparison, then genuinely fresh-context effective verification; neither source nor changed instructions self-authorize it.

## Adaptive workflow

```text
ROUTING -> DISCOVERING? -> PLANNING? -> EXECUTING -> VALIDATING? -> REVIEWING? -> FINALIZING -> LOCAL_READY
```

The question before each phase is: does it materially improve correctness, independence, risk control, or required evidence? `TRIVIAL` work can be a Luna worker plus a focused check. `LOCAL` work gets current evidence or a targeted explorer, then a Luna/Terra worker and targeted validation. `COMPLEX` and `HIGH_RISK` work add only necessary planning, dependent TaskNodes, validation, and fresh review. `EXTREME` does not mean a bigger request: Astra is a rare, node-local escalation after concrete evidence that Sol is insufficient.

| Model | Use per TaskNode |
| --- | --- |
| Luna | Targeted exploration, deterministic edits, docs, focused validation, low-risk review |
| Terra | Bounded implementation/debugging, ordinary planning |
| Sol | Architecture, high uncertainty, shared contracts, auth/security, concurrency, migration, persistence, high operational risk |
| Astra | Specific Sol-insufficiency escalation only |

Skip discovery only when exact scope and sufficient current behavior evidence are known; otherwise ask a focused explorer, not a repository-wide scout. Reuse evidence only while baseline, branch, relevant dirty paths, scope, contracts, and behavior remain valid. Skip planning when implementation is obvious and has no architectural/shared-contract/security/migration/concurrency/persistence/cross-layer/high-blast-radius decision. Skip independent review for low-risk trivial work unless an authoritative rule requires it; use fresh Luna review for medium risk and specialist plus fresh whole-scope review for high risk.

## Compact complete examples

The primary records a compact `TaskContract` with run id, baseline/branch/WIP, authority ledger, active scope, `InstructionManifest`, original source paths, mandatory skills, acceptance, checks, reviews, and current nodes. The manifest stores authoritative source pointers and observed identities; a component node can receive `/repo/AGENTS.md -> /repo/frontend/AGENTS.md -> /repo/frontend/components/AGENTS.md`, while an unrelated backend node receives only its own complete effective chain. [evidence-contracts.md](references/evidence-contracts.md) remains the schema truth.

```yaml
task_node:
  id: backend-profile
  kind: implementation
  depends_on: [profile-contract]
  scope: [server/profile/**]
  responsibility: persist profile setting
  acceptance: ["setting survives reload"]
  checks: ["unit:profile-service"]
  risk: shared profile contract
  complexity: COMPLEX
  instructions:
    effective_sources: [/repo/AGENTS.md, /repo/server/AGENTS.md]
    mandatory_skills: []
    required_checks: ["unit:profile-service"]
    required_review_profiles: [types/contracts]
  routing:
    agent_type: worker
    model: gpt-5.6-terra
    reason: bounded implementation
  ownership: [server/profile/**]
  delegation: forbidden
```

```yaml
task_receipt:
  run_id: profile-setting-20260917-01
  node: backend-profile
  state: complete
  scope: [server/profile/**]
  writes: [server/profile/service.ts]
  observed: {head: abc1234, dirty_paths: [server/profile/service.ts]}
  instruction_preflight:
    sources: [{path: /repo/AGENTS.md, observed_identity: "sha256:agents-v1"}]
    mandatory_skills: []
    status: complete
  checks: [{purpose: unit, state: ran_pass}]
  review: {snapshot: abc1234, profile: [types/contracts], round: 1}
  gaps: []
  escalation: {reason: "", evidence: "", requested_node_or_capability: ""}
  model_decision:
    requested_role: worker
    requested_model: gpt-5.6-terra
    reason: bounded implementation
    runtime: {observed_role: unknown, observed_model: unknown, verified: false, evidence: ""}
```

Medium example: an intermittent reconnect bug becomes targeted Luna discovery -> Terra worker -> focused validation -> fresh Luna review only if risk justifies it. High-risk password recovery becomes effective instruction/mandatory-security-skill resolution -> targeted explorers -> Sol plan when a security decision exists -> Terra/Sol worker nodes -> validators -> specialist security review -> fresh whole-scope review. If a reviewer finds a defect, a separate worker fixes it, a validator validates it, and a fresh reviewer sees the new immutable snapshot.

## Hard boundaries

- The primary does not discover, design, implement, integrate, validate engineering work, or review code.
- Only the primary delegates; every child has `delegation: forbidden` and escalates scope/risk/capability issues.
- Every agent independently reads original applicable authority; summaries and receipts never substitute.
- Scoped ownership preserves WIP; no reset, stash, revert, overwrite, or conflict resolution outside explicit ownership.
- A reviewer is read-only; every write invalidates prior clean review evidence; whole-scope review has a five-round limit.
- Instruction drift invalidates affected preflight/evidence; an instruction cannot authorize itself.
- `LOCAL_READY` is not remote SHA/CI, merged, deployed, or live verified.

Requested routing is not observed runtime: unsupported APIs and assignment prose cannot prove model identity, role enforcement, no-delegation, or read-only behavior. Report unproved runtime as `unknown`/`verified: false` and pause as `PAUSED_CAPABILITY` when a necessary capability is absent. Installing or editing the skill in the current context does not prove effective fresh-context discovery.

## Prior release

Delegated Engineering 1.0.1 remains available as a fixed release tag and package reference:

```text
Use $skill-installer to install only delegated-engineering from https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v1.0.1/skills/delegated-engineering into my personal skills directory. Preserve any existing copy; do not install other skills.
```

Copy a complete folder, including its references and license, into a supported skills directory; compare any existing copy before replacement. The 1.0.1 release link does not activate or update the current skill automatically.

Current release downloads: [ZIP](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.0.0/delegated-engineering-2.0.0.zip) and [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.0.0/delegated-engineering-2.0.0.zip.sha256). These assets are published separately from this source update.

Original material uses the adjacent [MIT license](LICENSE).
