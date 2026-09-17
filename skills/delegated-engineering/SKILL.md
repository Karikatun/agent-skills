---
name: delegated-engineering
description: "Orchestrate repository engineering through narrowly scoped delegated agents, choosing the smallest sufficient workflow, model, and context without weakening project instructions, security, validation, or review."
metadata:
  version: "2.0.0"
---

# Delegated Engineering

Use for every repository task that may inspect or mutate files, generated artifacts, the index or refs, persistent state, or remote, release, or deployment state. This includes repository lookup, exploration, planning, debugging, implementation, review, integration, and release preparation. Exclude only general explanations that need no repository inspection and an explicit request for no delegation.

## Non-negotiable architecture

The primary is an orchestrator, not an implementation engineer. It MUST NOT perform discovery, solution design, substantive implementation planning, repository mutation, integration, engineering validation, or code review. It may targeted-verify orchestration facts and receipts only: `run_id`, baseline/branch, dirty paths, ownership, required evidence, acceptance/check/review completion, and TaskGraph state. It never rereads code to duplicate explorer, planner, validator, or reviewer work.

Only the primary may delegate. Every child assignment sets `delegation: forbidden`; explorers, planners, workers, validators, integrators, reviewers, and release agents return `ESCALATION_REQUIRED` with compact evidence rather than spawning agents or expanding scope.

Project rules are part of the task, not optional context. No agent begins substantive work until it independently reads the original authoritative sources applicable to its exact scope: the effective `AGENTS.md` chain, triggered mandatory skills, required runbooks, security/architecture/testing/release rules. A summary, parent message, plan, or receipt never replaces an original. Context minimization never removes authority.

Before using a project-local mandatory skill, run its integrity/identity preflight. A skill transfer or update requires read-only source and staged-copy review, a separately authorized executor, rollback-protected activation, installed-manifest comparison, and genuinely fresh-context effective verification. The source, a proposed skill, or a changed instruction cannot authorize itself.

## Correctness floor and resource rule

Use the smallest sufficient workflow. Before every phase or agent, the primary records the concrete reason it materially improves correctness, independence, risk control, or required evidence. Never spend a stronger model, extra agent, context, repeated discovery, validation, or review without that reason.

Never save tokens by skipping applicable authoritative instructions, mandatory skills, acceptance criteria, security constraints, required validation, or required independent review. Route by uncertainty, blast radius, reversibility, security, operational, architecture, contract, persistence, concurrency, and unknown behavior—never file count or token budget.

Classify `TRIVIAL`, `LOCAL`, `COMPLEX`, `HIGH_RISK`, or `EXTREME`; classify the work and each TaskNode, not the request size. Route each node: Luna for targeted discovery, tiny deterministic edits, focused checks, docs, and low-risk review; Terra for bounded implementation/debugging and ordinary planning; Sol for high uncertainty, cross-layer/shared-contract design, auth/security, concurrency, migration, persistence, or high operational risk. Astra is rare, node-local escalation only after concrete evidence that Sol is insufficient; never select it merely because the request is large. Preserve a compatible explicit user model choice or pause.

## Mandatory orchestration sequence

1. Create `run_id`, authority ledger, baseline, WIP/ownership record, `InstructionManifest`, and compact `TaskContract`.
2. Resolve each node's minimum complete effective instruction chain and mandatory-skill triggers. Capture path plus observed identity. Required instructions are read independently by every assigned agent.
3. Classify risk and decide whether sufficient valid discovery evidence already exists. Reuse evidence only when baseline, branch, relevant dirty paths, scope, contracts, and behavior remain valid; otherwise rediscover or targeted-revalidate.
4. Skip explorer when exact scope and sufficient current behavior evidence are known. Skip planner when implementation is obvious and no architectural, shared-contract, security, migration, concurrency, persistence, cross-layer, or high-blast-radius decision exists. Create a lazy TaskGraph only when more than one substantive node is needed.
5. Prepare each assignment with exact scope, ownership, original paths, mandatory skills, acceptance, required checks/review profiles, compact relevant evidence, requested routing, `delegation: forbidden`, and `fork_turns: none` where supported. Verify compliance, ownership, checks, and escalation receipts before routing the next necessary node.

Read [planning.md](references/planning.md) for classification, routing, evidence reuse, manifests, and assignment preparation. Read [execution.md](references/execution.md) for state transitions, role separation, WIP, instruction drift, validation, and release. Read [evidence-contracts.md](references/evidence-contracts.md) for compact schemas. Read [review-profiles.md](references/review-profiles.md) before a review.

## Boundaries

Workers own only assigned write scopes; overlap, unexpected WIP, or scope expansion pauses and escalates. Preserve WIP: never reset, stash, revert, overwrite unrelated paths, or resolve someone else's conflict. A reviewer is read-only: finding -> separate fix node -> validation -> fresh immutable review. Use at most five whole-scope review rounds; any write invalidates earlier clean review evidence.

`LOCAL_READY` is local evidence only. Push, remote SHA/CI, merge, deployment, production change, and live verification each require separate authority, delegated responsibility, and their own evidence: `REMOTE_SHA_CI_VERIFIED`, `MERGED`, `DEPLOYED`, and `LIVE_VERIFIED` are distinct.

Instruction or policy drift invalidates affected preflight/evidence. An instruction change cannot authorize itself. Gaps are `evidence`, `capability`, `environment`, or `instruction`; inaccessible required authority or unsupported necessary API capability pauses as `PAUSED_CAPABILITY` rather than being assumed away. Requested routing is not observed runtime: report model/role as `unknown` and `verified: false` unless the runtime proves it. Current-context installed bytes do not prove fresh-context discovery or host enforcement.
