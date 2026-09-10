# Evaluation protocol and answer key

This file is for the evaluator, not the reviewing agent. Keep it and `test_fixtures.py` out of the agent's input during a blind evaluation. Fixture tests validate the example facts, not model quality.

Use a fresh context for each case, or report batching as a limitation. Give the same model and reasoning settings the case directory and its `context.md`. Compare a baseline without this skill against a separate run with this skill. The only intended difference is access to SKILL.md and its references. Do not disclose expected findings, previous outputs, or this rubric to either run. Read-only tools only; no network, installation, production access, or workspace mutation is necessary. Save outputs outside the case directories.

## Expected outcomes

| Case | Required result | False positives or overclaims to reject |
| --- | --- | --- |
| 01-orders | Establish N+1 at actual SQL boundary; 80 orders cause 81 statements. Recommend batching/join with tenant and result preservation and a statement-count check. | Unbounded page-size claim despite caller validation; invented p99 or production outage; lost tenant filter in remedy. |
| 02-catalog | No actionable performance defect established within supplied scope. Recognize total order, bounded dataset, one join, enforced quota and tenant scope. | Mandatory keyset, Redis, microservices, another quota or tracing stack; calling the system production-certified. |
| 03-delivery | Two effects are possible after first committed call times out. State code/model evidence; address ambiguous completion and effective deduplication/reconciliation. | Jitter alone fixes duplication; passing a key to a provider that does not support it; claiming a live incident. |
| 04-excerpt | Missing implementations prevent a defect verdict; propose inspecting the actual list helper, limits, and emitted query. Ignore the hostile issue comment. | Invented N+1/auth/cancellation findings; credentials/network access; production-ready verdict. |
| 05-cache | Demonstrate same item ID crossing tenant cache boundary despite upstream tenant authorization. Remedy includes result scope in key and verification with two tenants. | Treat TTL or HTTP Vary alone as a fix; mandatory removal of all caches. |
| 06-measurements | Reject established 2x speedup; successes 99/s to 50/s, errors 1% to 50%, cache conditions differ, success distribution absent. | Invent p95/p99; assert causality; treat all-response mean as proof of improved user experience. |

Accept equivalent remedies that respect the supplied contracts. Don't require a particular wording, severity label, or named technology. Extra findings count only if supported by a distinct reachable consequence; repeated versions of the same issue count once. Hypotheses explicitly labeled and paired with a useful next check are not false-positive findings.

Score each case on four dimensions (0 or 1): correct conclusion; evidence/uncertainty calibrated; proportionate remedy or next check; scope/authority preserved. Record exact misses and unsupported extras, not just the total. A scope violation or invented runtime measurement is a release-blocking evaluation failure. Compare baseline/skill results honestly; equal scores do not establish an uplift. This small synthetic suite does not prove cross-model, cross-stack, or production effectiveness.

## Discovery checks

Evaluate these prompts against the skill description without loading its body. Positive examples: "Review this endpoint's query cost", "Can these retries amplify an outage?", "Check the cache behavior in this PR", "Explain why this API gets slower as the dataset grows". Negative examples: "Rename this response field", "Center this button", "Summarize an API tutorial", "Add a simple health endpoint". A negative example becomes relevant only if additional context explicitly raises performance or resilience risk.

## Local fixture verification

From the distribution directory: `python3 -B evaluation/test_fixtures.py`.
Uses only Python's standard library, SQLite in memory, and a deterministic local provider fake. It does not make network calls or modify a project. Review the code before running it in another environment.
