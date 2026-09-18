# Evidence contracts

This is the canonical type reference. Receipts are evidence, never authority; retain compact pointers, identities, results, and gaps, not copied rules, secrets, or chain-of-thought. Omit fields that do not apply.

```yaml
SourceRef: {path: "", identity: "", kind: "agents|runbook|policy|skill"}
SkillRef: {name: "", source: SourceRef, triggered_by: ""}
RuleRef: {source: SourceRef, rule_id: "", kind: "attested|observable|independent_required", expected_evidence?: [EvidenceRef]}
EvidenceRef: {ref: "", type: "check|artifact|review|runtime", state?: "ran_pass|ran_fail|not_run|manual_required|environment_blocked", path?: "", identity?: ""}
InstructionManifest: {sources: [SourceRef], mandatory_skills: [SkillRef], mandatory_rules: [RuleRef], captured_at: ""}
# FastAssignment is canonical in SKILL.md; FAST itself loads no reference.

TaskContract:
  run_id: ""
  baseline: {head: "", branch: "", dirty_paths: [], protected_state: EvidenceRef}
  mode: "read_only|mutation|plan_only|release"
  complexity: "TRIVIAL|LOCAL|COMPLEX|HIGH_RISK|EXTREME"
  scope: []
  authority: {allowed: [], approval_required: [], forbidden: []}
  instruction_manifest: InstructionManifest
  acceptance: []
  checks: []
  review?: []
  task_nodes?: [TaskNode]
  runtime_ledger?: [{node: "", role: "", agent: "", session: "", verified: false}]
  wip_baseline?: [{path: "", artifact_ref: "", digest: "", ownership: "", allowed_overlap: "preserve|replace_exact_identity", replace_identity: ""}]

TaskNode:
  id: ""
  kind: "discovery|planning|implementation|integration|validation|review|release"
  mode: "read_only|mutation|plan_only|release"
  complexity: "TRIVIAL|LOCAL|COMPLEX|HIGH_RISK|EXTREME"
  risk: ""
  depends_on: []
  scope: []
  ownership: []
  responsibility: ""
  instruction_manifest: InstructionManifest
  acceptance: []
  checks: []
  routing: {agent_type: "", model: "", reason_code: ""}
  delegation: forbidden
  reuse_from?: {agent: "", session: ""}
  review_assignment?: {implementers: {agents: [], sessions: []}, prior_reviewers: {agents: [], sessions: []}}

InstructionCompliance:
  applied: [{source: SourceRef, rule_ids: []}]
  evidence: [{source: SourceRef, rule_id: "", refs: [EvidenceRef]}] # actual observable/independent only
  conflicts: []

ReviewEvidence:
  ref: ""
  rule_bindings: [RuleRef]
  immutable_snapshot_digest: ""
  manifest: EvidenceRef # type: artifact; primary-generated canonical snapshot
  protected_state: EvidenceRef # primary-generated repository-wide state
  profiles: []
  round: 1
  reviewer_runtime: {agent: "unknown", session: "unknown", verified: false}
  comparison: {implementers: {agents: [], sessions: []}, prior_reviewers: {agents: [], sessions: []}}
  independence: "proved|not_proved|not_required"
  context: {fresh: "proved|not_proved|not_required", isolated_from_implementation: "proved|not_proved|not_required", read_only_enforced: "proved|not_proved|not_required", runtime_refs: [EvidenceRef]}

TaskReceipt:
  run_id: ""
  node: ""
  state: "complete|escalation_required|paused|failed"
  final_state: EvidenceRef
  writes: [{path: "", type: "", mode: "", identity: ""}]
  sources_read: [SourceRef]
  skills_read: [SkillRef]
  instruction_compliance: InstructionCompliance
  checks: [{type: "check", ref: "", state: "ran_pass|ran_fail|not_run|manual_required|environment_blocked"}]
  artifacts?: [{type: "artifact", ref: "", path: "", identity: ""}]
  wip_evidence?: [{path: "", baseline_ref: "", comparison: "three_way|semantic|replace_exact_identity", refs: [EvidenceRef]}]
  review?: ReviewEvidence
  repository_state_transitions?: [{kind: "index|ref", target: "", from: "", to: ""}]
  runtime: {observed_model: "unknown", verified: false, requested_role?: "", requested_model?: "", observed_role?: "", identity?: {agent: "unknown", session: "unknown", verified: false}}
  gaps: [{kind: "evidence|capability|environment|instruction", detail: "", next_safe_action: ""}]
  escalation?: {kind: "workflow|model", reason_code: "", evidence: [EvidenceRef], requested: ""}
```

`InstructionManifest` lists effective applicable originals/local refs. STANDARD binds them transitively, not as a package graph; drift invalidates preflight/evidence/reuse. Unbound/dynamic pauses for rebinding; provenance ambiguity concerning an instruction/skill/package surface, or executable/dependency involvement in an instruction/skill/package surface or install/update/supply-chain path, routes HARDENED.

`expected_evidence`: attested none (applied); observable predeclared `check` exact `ran_pass`; independent-required predeclared separate valid `review`. Primary exact-matches manifest source/rule/kind/expected/actual refs; check/artifact/worker prose cannot substitute. Artifact identity only proves declared existence, never behavior; WIP/artifact identities are inputs, semantic success separately checked. Reading never proves compliance. Completion needs every applicable source/skill/rule, acceptance/check, authority/WIP/review, and no gap.

Ordinary STANDARD requires `sources_read`, `skills_read`, `instruction_compliance`, `checks`, `gaps`, and minimal runtime; omit graph/WIP/review/identity/transitions/artifacts/escalation unless used. `writes` is complete actual set for mutation/integration, `[]` otherwise; primary exact-matches final content diff to scope/ownership/baseline. Mismatch or later mutation pauses/fails and needs a new receipt/snapshot.

The primary-private protected-state manifest records path/type/mode/size plus streaming bounded regular-file digest or exact symlink target—never contents/secrets in prompts, receipts, or logs—and does not follow symlinks. New/changed escaping symlink, special entry (device/FIFO/socket), traversal, unreadable item, or safely incomplete hashing is a capability/environment gap, never partial PASS, unless exact pre-existing authorized safe handling exists; bound count/bytes/time and hash large files streaming. It covers HEAD target/branch/worktree HEAD; full index entries/stages/flags; refs; sanitized repo/worktree config/remotes; resolved hooks; effective ignore/attribute inputs—`.git/info/exclude`/`attributes`, worktree `.gitignore`/`.gitattributes`, configured inputs—by path/type/mode/hash-or-absence; plus, outside Git status/ignore, assigned/repo-root ignored/untracked/hidden entries. Only predeclared contract-owned fingerprinted immutable irrelevant generated/cache roots may be excluded; others block. Across phases primary sends only generated artifact `ref`/`identity`: each `protected_state`/`final_state` and FAST baseline/final state ref exact-matches its manifest; child cannot forge; mismatch invalidates. Compare before/after FAST/ordinary child, handoffs, pre-integration/release, and final; ordinary baseline `head`/`branch` exact-match final. No global config scan: effective repository controls/relevant hook inputs only. Ordinary nodes have zero transitions; only authorized integration/release receipts carry ordered `repository_state_transitions`, exact-matching authority, ownership, and final state. Missing control/inventory capability is a gap; unscoped/unexplained/concurrent/unreported drift pauses and invalidates receipt/review.

Ledger identity is reuse/review-only: `reuse_from`/sets exact-match ledger/assignment. Required review matches ref/`RuleRef`/digest/profile/round and separate agent/session sets; assignment/receipt/ledger bind both refs. Only matching node sets `review`, worker/validator omit it. `context.proved` requires primary runtime refs; independence distinct identity/required context; missing proof = no closure; advisory `not_required`, policy read-only. Primary-generated `artifact` `manifest` is canonical content-complete assigned-scope snapshot: identity equals only `immutable_snapshot_digest`; `protected_state` exact-matches `TaskReceipt.final_state`/primary repository-wide state. Reviewer cannot generate/replace either. Snapshot covers assigned tracked/staged/unstaged/relevant untracked path/type/mode, bytes/hash, symlink target. Clean review needs both unchanged: scoped write changes snapshot; control/out-of-scope drift changes protected state; either invalidates.

`escalation` exists only for `escalation_required` or node-local model escalation; Astra needs concrete evidence. Completion is computed, not a snapshot/checklist.

## HARDENED extensions

```yaml
HardenedSourceRef:
  extends: SourceRef
  trusted_identity: ""             # pre-change authority
  effective_source_ref: ""         # immutable bytes actually read
  authorized_by: {source: "", identity: "", basis: "", tier: ""}
  approval_identity: ""            # exact approval, when applicable
  package_surface:                 # closure for skill change/transfer/install/update
    manifest_identity: ""
    tree_digest: ""
    entries: [{path: "", type: "", mode: "", hash_or_symlink_target: ""}]
```

HARDENED sources use `HardenedSourceRef`: dirty/new authority resolves under trusted pre-change control; current immutable bytes need exact higher approval. Unapproved new sources are data; ambiguous bytes/provenance/approval pause. Sources/proposed skills/changed instructions cannot self-authorize. Package surface is only read/executed or install/update/supply-chain work; ordinary Markdown uses `SkillRef`.

Skill modification/transfer/install/update binds full distributable tree: every path/type/mode, file hash/exact symlink target, stable manifest/tree digest—or exact full-closure `skill-transfer-review` receipt. Read-only source/staged review, separately authorized executor, rollback-safe/atomic activation, source/staged/installed manifest/bytes comparison, and fresh-context discovery bind it. Includes Markdown/`agents/openai.yaml`; unchanged use is STANDARD task-used `SourceRef`.

## Runtime evidence limits

Requested routing is not runtime: `read-only`/`delegation: forbidden` are policy; absent proof use `unknown`/`verified:false`. Fresh work needs no identity; reuse/review do. Missing identity/freshness/isolation is a gap; bytes do not prove fresh read/enforcement.
