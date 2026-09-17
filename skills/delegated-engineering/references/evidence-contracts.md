# Evidence Contracts

## Task Receipt

Every scout, worker, reviewer, integrator, and release agent returns one compact receipt:

```json
{
  "run_id": "",
  "scope": ["path or responsibility"],
  "source_receipts": [{"path": "", "observed_identity": "", "rule_ids": [""]}],
  "authority_delta": {"allowed": [], "approval_required": [], "forbidden": []},
  "model_decision": {"model": "", "role": "", "risk_rationale": ""},
  "writes": ["path or none"],
  "checks": [{"purpose": "", "state": "read|ran_pass|ran_fail|not_run|manual_required|environment_blocked"}],
  "gaps": [{"kind": "evidence|capability|environment", "detail": ""}],
  "observed": {"head": "", "dirty_paths": []}
}
```

`model_decision` is required for every assignment and records the selected model,
agent role, and one-line rationale based on uncertainty, blast radius,
reversibility, or security/operational risk. A receipt must not use token budget
or file count as its routing rationale. The final report additionally emits one
`routing_summary` object with `assignments`, `escalations`, and
`scout_revalidations` arrays; it is report metadata, not an agent receipt field.

The primary keeps a compact source/skill matrix from receipts and targeted-verifies high-risk claims. Receipts are evidence, not authority. Do not repeat full rules, include secrets, or expose private data.

## Scout JSON

The scout returns exactly one JSON object, with no Markdown or surrounding text:

```json
{
  "state": {"head": "", "branch": "", "dirty_paths": []},
  "behavior": [""],
  "code": [{"path": "", "lines": "", "symbols": [""], "role": ""}],
  "flow": [""],
  "tests": [{"path": "", "covers": "", "command": "", "ran": "read|ran_pass|ran_fail|not_run|manual_required|environment_blocked"}],
  "constraints": [{"source": "", "rule": ""}],
  "risk_surfaces": [{"kind": "", "evidence": "", "review_focus": ""}],
  "manual_validation": [{"environment": "", "purpose": "", "available_to_agent": false}],
  "unknowns": [],
  "receipt": {
    "run_id": "",
    "scope": ["path or responsibility"],
    "source_receipts": [{"path": "", "observed_identity": "", "rule_ids": [""]}],
    "authority_delta": {"allowed": [], "approval_required": [], "forbidden": []},
    "model_decision": {"model": "gpt-5.6-luna", "role": "explorer", "risk_rationale": ""},
    "writes": ["none"],
    "checks": [],
    "gaps": [],
    "observed": {"head": "", "dirty_paths": []}
  }
}
```

Required keys and shown value types are fixed. `code` has at most 10 entries, `tests` at most 6, `risk_surfaces` at most 5, and `unknowns` at most 5. `ran` uses the stated enum. On a format failure, request one correction; a second failure is an evidence gap.

## Findings And Gaps

Separate a code or product finding from an evidence gap and a capability or environment gap. State what was observed, what was not proved, and the next safe action. Repairing a receipt or check description without writing an artifact does not consume a review round.
