# Planning State Machine

Create the `run_id` and TaskContract before dispatch. Preserve its baseline HEAD, branch, dirty paths, and unrelated WIP; never reset, stash, or overwrite to manufacture a baseline.

Choose the model from uncertainty, blast radius, reversibility, and security or operational risk. Token budget and file count are not routing criteria, and all models are not run by default. Keep scout evidence reusable only while branch/HEAD, relevant dirty paths, and scope match the captured state; otherwise rediscover or revalidate.

| Start | Action | Terminal or next state |
| --- | --- | --- |
| `NEEDS_DISCOVERY` | Fresh scout discovers an unknown location or behavior | `PLANNED` |
| `PLAN_ONLY` | Scout if discovery is needed, then lead plan | `PLAN_COMPLETE` |
| `READ_ONLY` | Fresh whole-scope reviewer when scope is known | `EVIDENCE_COMPLETE` |
| required delegation unavailable | Record capability gap | `PAUSED_CAPABILITY` |

An already-authorized mutation moves from `PLANNED` to execution without repeated approval. A known authorized mutation may skip the scout. A known read-only request uses a fresh reviewer; it never creates a fix loop or an edit. Every repository lookup or inspection is delegated; the primary only verifies targeted claims and named locations.

## Fresh Scout

When location or behavior is unknown, spawn a fresh Luna scout with `agent_type: explorer`, `model: gpt-5.6-luna`, and `fork_turns: none`. Give its absolute repository path, original request, focused questions, known entry points, original-source paths, and TaskContract. It reads only, makes no edits, tests, builds, browser/UI operations, delegation, or external mutations, and returns the one-object Scout JSON from [evidence-contracts.md](evidence-contracts.md). The primary performs only targeted verification of that receipt and named locations.

Preflight the actual delegation API, role, model, slot, and expected scope. If an API field is incompatible, omit it only when the fresh-agent and required-role properties remain true. Do not use a full-history fork with an explicit model override. If Luna is unavailable, try Terra, then Sol; if Terra is unavailable, try Sol. If Sol is required but unavailable, pause. Never replace an explicit compatible user-selected model without direction.

The primary verifies only the scout's targeted claims, then records observable acceptance, non-overlapping slices, model allocation, selected checks and review profiles, and any approval or evidence gap. A lead plan names source paths and responsibilities, not speculative implementation. Each assignment includes a compact `model_decision` receipt. Escalate on scope expansion, contract ambiguity, failed primary signal, recurring defect, or a newly discovered risk boundary.
