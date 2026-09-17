# Compact Evidence Contracts

Receipts are orchestration evidence, never authority. Keep paths, identities, results, and unresolved facts; omit chain-of-thought, secrets, copied rules, and large code excerpts.

## TaskContract and InstructionManifest

```yaml
task_contract:
  run_id: ""
  baseline: {head: "", branch: "", dirty_paths: []}
  active_scope: []
  authority: {allowed: [], approval_required: [], forbidden: []}
  instruction_manifest: instruction_manifest
  original_authoritative_sources: []
  mandatory_skills: []
  acceptance: []
  selected_checks: []
  review_requirements: []
  task_nodes: []

instruction_manifest:
  sources: [{path: "", applies_to: "", observed_identity: "", kind: "agents|runbook|policy"}]
  mandatory_skills: [{name: "", source: "", triggered_by: ""}]
  captured_at: ""

planner_result:
  scope: []
  assumptions: []
  solution: []
  task_graph: []
  acceptance_mapping: []
  validation_plan: []
  review_profiles: []
  risks: []
  unknowns: []
```

## TaskNode and scout evidence

```yaml
task_node:
  id: ""
  kind: "discovery|planning|implementation|integration|validation|review|release"
  depends_on: []
  scope: []
  responsibility: ""
  acceptance: []
  checks: []
  risk: ""
  complexity: "TRIVIAL|LOCAL|COMPLEX|HIGH_RISK|EXTREME"
  instructions: {effective_sources: [], mandatory_skills: [], required_checks: [], required_review_profiles: []}
  routing: {agent_type: "", model: "", reason: ""}
  ownership: []
  delegation: forbidden

scout_evidence:
  state: {head: "", branch: "", dirty_paths: []}
  code: [{path: "", lines: "", symbols: [], role: ""}]
  flow: []
  tests: [{path: "", covers: "", command: "", ran: "read|ran_pass|ran_fail|not_run|manual_required|environment_blocked"}]
  constraints: [{source: "", rule: ""}]
  risk_surfaces: [{kind: "", evidence: "", review_focus: ""}]
  unknowns: []
```

Scout evidence is targeted: at most 10 code entries, 6 tests, 5 risk surfaces, and 5 unknowns. An explorer reads only its exact question, makes no writes/external mutation/delegation, and returns `ESCALATION_REQUIRED` for expanded scope.

## Receipts, routing, and gaps

```yaml
task_receipt:
  run_id: ""
  node: ""
  state: "complete|escalation_required|paused|failed"
  scope: []
  writes: []
  observed: {head: "", dirty_paths: []}
  instruction_preflight:
    sources: [{path: "", observed_identity: ""}]
    mandatory_skills: [{name: "", source: ""}]
    status: "complete|incomplete|paused_capability"
  checks: [{purpose: "", state: "read|ran_pass|ran_fail|not_run|manual_required|environment_blocked"}]
  review: {snapshot: "", profile: [], round: null}
  gaps: [{kind: "evidence|capability|environment|instruction", detail: "", next_safe_action: ""}]
  escalation: {reason: "", evidence: "", requested_node_or_capability: ""}
  model_decision:
    requested_role: ""
    requested_model: ""
    reason: ""
    runtime: {observed_role: "unknown", observed_model: "unknown", verified: false, evidence: ""}
```

`model_decision` is required in EVERY TaskReceipt and is the compact routing/model-decision receipt. It records requested routing separately from observed runtime. If API/runtime identity is not proved, use `unknown` and `verified: false`; assignment prose cannot enforce role, model, no-delegation, or read-only behavior. Unsupported necessary capability is `PAUSED_CAPABILITY`. Compact compliance receipt repair cannot retroactively prove an omitted original read.

The final report may add `routing_summary: {assignments: [], escalations: [], scout_revalidations: []}` and the source/skill matrix. Separate confirmed behavior, static evidence, hypotheses, and unknowns. A gap is not a passing result.
