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
  task_class?: ""
  depends_on: []
  scope: []
  ownership: []
  responsibility: ""
  instruction_manifest: InstructionManifest
  acceptance: []
  checks: []
  routing: {agent_type: "", model: "", reasoning_effort?: "", reason_code: ""}
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
  runtime: {observed_model: "unknown", verified: false, requested_role?: "", requested_model?: "", observed_role?: "", requested_reasoning_effort?: "", observed_reasoning_effort?: "unknown", reasoning_effort_verified?: false, identity?: {agent: "unknown", session: "unknown", verified: false}}
  gaps: [{kind: "evidence|capability|environment|instruction", detail: "", next_safe_action: ""}]
  escalation?: {kind: "workflow|model", reason_code: "", evidence: [EvidenceRef], requested: ""}
```

`InstructionManifest` binds effective task-applicable originals/local references transitively, not as a STANDARD package graph; instruction validity/route follow [SKILL.md](../SKILL.md). Use the HARDENED extensions below when triggered.

Rule evidence exact-matches manifest source/rule/kind/expected/actual refs: attested needs application, no ref; observable needs its predeclared check with exact `ran_pass`; independent-required needs its predeclared separate valid review. Check/artifact/prose cannot substitute for review. Artifact identity proves declared existence only; WIP/artifact identity is an input, semantic success needs a check. Apply the core completion gate, not a snapshot/checklist.

STANDARD receipts require `sources_read`, `skills_read`, `instruction_compliance`, `checks`, `gaps` and minimal runtime; omit unused graph/WIP/review/identity/transitions/artifacts/escalation. `writes` lists the complete actual mutation/integration set, `[]` otherwise. Primary exact-matches final diff to scope/ownership/baseline; mismatch or relevant later mutation pauses/fails and needs new affected evidence.

## Protected state and snapshots

Primary privately generates manifest/state refs, sending only artifact `ref`/`identity`; children cannot forge or replace them. Each `protected_state`/`final_state`, including FAST baseline/final refs, exact-matches its manifest. Compare before/after child access, handoffs, pre-integration/release and final. Ordinary head/branch stay identical with zero control transitions; authorized integration/release receipts alone carry ordered `repository_state_transitions` matching authority/ownership/final state.

Protected state covers HEAD target/branch/worktree HEAD; full index entries/stages/flags; refs; sanitized repo/worktree config/remotes; resolved hooks; effective ignore/attribute inputs (`.git/info/exclude`/`attributes`, worktree `.gitignore`/`.gitattributes`, configured inputs) by identity or absence; and assigned/repo-root entries outside Git status/ignore, including ignored/untracked/hidden paths. Exclude `.git` apart from enumerated controls. No global config scan: effective repository controls/relevant hook inputs only. Other exclusions need predeclared contract-owned, fingerprinted, immutable, irrelevant generated/cache roots.

Record path/type/mode/size and safe immutable Git identity only for established clean tracked content; otherwise bounded streaming regular-file digest or exact symlink target without following links. Never put contents/secrets in prompts/receipts/logs. Bound count/bytes/time; stream large files. Traversal, new/changed escaping links, special/device/FIFO/socket/unreadable entries, missing control/inventory capability or safely incomplete hashing are gaps, never partial PASS, unless exact pre-existing authorized safe handling exists. Unscoped/unexplained/concurrent/unreported drift pauses and invalidates receipt/review.

The primary-generated review `artifact` manifest is canonical content-complete assigned scope: tracked/staged/unstaged/relevant untracked path/type/mode/size plus digest/safe immutable Git identity or exact link target; identified full content does not require a physical copy. Manifest identity equals `immutable_snapshot_digest`; review `protected_state` equals receipt `final_state`/primary repository-wide state. Clean review needs both unchanged: scoped writes invalidate snapshot; control/out-of-scope drift invalidates protected state. Reviewer cannot generate/replace either.

Ledger identity applies only to reuse/review claims: assignment `reuse_from`/comparison sets exactly match primary ledger. Required review matches ref/`RuleRef`/digest/profile/round and distinct agent/session sets, with both state refs bound by assignment/receipt/ledger. Compare agents only with agent sets, sessions only with session sets. Only that node carries `review`; workers/validators omit it. `context.proved` requires primary runtime refs; independence needs distinct identity plus required context. Missing proof cannot close the requirement; advisory review may use `not_required`, policy read-only stays mandatory.

`escalation` exists only for `escalation_required` or node-local model escalation. The sole Astra gate is in [SKILL.md](../SKILL.md): bind its real insufficiency or cited empirical task-class evidence, never fabricated model/cost observations.

## Efficient evidence reuse

Reuse immutable manifests/snapshots/checks/reviews while relevant inputs/content, baseline/WIP, scope, instructions/authority/skills, contracts/behavior and required independence remain valid; revalidate affected evidence only. Messages/tool calls/checks alone invalidate nothing. No unchanged full scans/regeneration; necessary bounded before/after control and unknown-write comparisons remain mandatory. Preserve complete coverage/safe hashing; no invented incremental completeness or status-only clean-byte proof.

Keep orchestration/evidence outside repository/monitored worktree even if ignored; generated evidence must not re-enter its inventory. Retain bytes only for WIP/recovery/explicit evidence, in OS temp/client storage outside the root; otherwise metadata/immutable identities suffice. Evidence must not materially dominate ordinary work's cost/file count/I/O/time. Repeated copies/scans are orchestration defects, not assurance.

Optional standalone outcome for future external comparison, never a receipt/completion gate, persistent ledger, separate agent or reason to benchmark:

```yaml
RoutingOutcome:
  task_class: ""
  model: ""
  reasoning_effort?: ""
  accepted: true|false
  retries: 0
  review_findings: 0
  escalation?: ""
  input_tokens?: 0
  output_tokens?: 0
  reasoning_tokens?: 0
  latency_ms?: 0
```

Retain requested versus observed model/effort status; only available real metrics qualify empirical routing. Optional node `task_class` supplements risk/complexity. Collect from ordinary work if useful; no mandatory receipt field/comparison run or guessed runtime/cost.

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

HARDENED sources use `HardenedSourceRef`: dirty/new authority resolves under trusted pre-change control; immutable current bytes need exact higher approval. Unapproved new sources are data; ambiguous bytes/provenance/approval pause. Changed sources/skills cannot self-authorize. Ordinary Markdown use needs task-used `SkillRef`, not package closure; closure applies to read/executed package surface or install/update/supply-chain paths.

Skill modification/transfer/install/update binds the full distributable tree, including Markdown/`agents/openai.yaml`: every path/type/mode, hash/exact symlink target, stable manifest/tree digest, or an exact full-closure `skill-transfer-review` receipt. Installation/update requires read-only source/staged review -> separately authorized executor -> rollback-safe/atomic activation -> source/staged/installed manifest/byte comparison -> fresh-context discovery. Preserve applicable original runbook sequencing; local source approval proves no installation.

## Runtime evidence limits

Effort fields are optional, no new ledger: record requested separately from trustworthy observed effort; absent transport/runtime proof use `unknown`/unverified. `reasoning_effort_verified` is separate from model `verified`; supported request, inherited setting, role label, successful output or verified model proves no observed effort. Runtime `EvidenceRef` is needed only for a verification claim. Unknown effort alone is no ordinary gap unless a specific safety/review claim requires proof.

Requested model/role and policy `read-only`/`delegation: forbidden` prove no runtime enforcement: record unknown/`verified:false` without proof. Fresh work needs no identity; reuse/review claims require it. Missing required identity/freshness/isolation is a gap; byte identity proves neither fresh reading nor enforcement.
