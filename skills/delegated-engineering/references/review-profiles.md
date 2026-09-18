# Adaptive review profiles

Review is conditional risk control. Apply the core invariants in [SKILL.md](../SKILL.md); record review types only through [evidence contracts](evidence-contracts.md).

Select only relevant profiles: trust/auth/API, concurrency/async, persistence/migration, external I/O/errors, lifecycle/resources, types/contracts, UI/accessibility, operations/data preservation, or agent-skill/supply-chain/install/update. The latter uses the applicable security skill.

| Level | When | Flow |
| --- | --- | --- |
| LOW | trivial, deterministic, reversible; no controlling independent-review rule | worker check/validation |
| MEDIUM | bounded behavior risk or controlling independent-review rule | fresh Luna, read-only final-scope review |
| HIGH | trust/security, concurrency, persistence/migration, shared contract, high operational risk | justified specialist read-only review, then fresh whole-scope review |

Do not add duplicate reviewers to vote. A reviewer independently reads applicable originals, receives the immutable final snapshot, scope, acceptance, profiles, and compact receipts—not prior conclusions—and reports findings and compliance. It never writes, fixes, stages, integrates, or delegates.

Finding -> authorized fix node -> same worker continuation only if scope, ownership, authority/skills, and risk are unchanged and independence is unnecessary; otherwise a fresh worker -> validation -> fresh re-review. No reviewer reuses implementation context after a write; any write invalidates clean review evidence. Out-of-scope findings pause for authority.

Count at most five completed whole-scope rounds per run. A clean fifth round may finish; a defect or unresolved issue in it is `BLOCKED_REVIEW_LIMIT`. A required review evidence ref must exactly match its bound rule, stable review ref, immutable digest, profile, and round; use the canonical content-complete digest semantics. Compare reviewer agent only with primary-ledger agent sets and reviewer session only with session sets. `ReviewEvidence.context` is proved only by primary-validated runtime refs; policy read-only remains mandatory. Otherwise record the limitation. Identity is required only for that claim.
