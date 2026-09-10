# API Performance Review

Version 1.0.2. Review API cost, scaling, and failure behavior using actual code and available runtime evidence. The workflow is independent of application language and framework; it does not require a particular database, cache, transport, or architecture.

## Use it

```text
Use $api-performance-review to review GET /orders. Do not change code.
```

Other useful requests include reviewing a diff for query growth, tracing work that survives a timeout, checking tenant-sensitive caching, and interpreting a supplied query plan or load-test result.

For each finding, expect a concrete trigger, owning code location, evidence level, consequence, narrow remedy, and verification step. A review may establish no actionable findings. Static evidence is not a measured latency result.

Ordinary API edits, cosmetic changes, and the mere absence of a particular technology do not require this workflow. A review-only request leaves code unchanged; a separately requested fix follows the user's scope and host permissions.

## Install and update

Copy this entire folder into your agent's supported personal skills directory. For local Codex, current documentation specifies `$HOME/.agents/skills`. Do not overwrite an existing folder until you have compared versions and preserved local edits. Invoke `$api-performance-review`; restart the client if discovery has not refreshed.

No other skill or runtime dependency is required. The folder contains Markdown and YAML only. Installation does not configure tools, grant permissions, or create an OS sandbox. Removing this specific installed folder disables future discovery; a fresh agent context may be needed to discard already-loaded instructions.

## Evidence and sources

Version 1.0.2 prepares the existing 1.0.1 workflow for a public collection: adds this README and increments metadata. The review instructions are otherwise unchanged. A fresh scoped forward-test covers a costly query, a clean bounded query, and incomplete evidence; earlier synthetic evaluation and seven executable fixture checks are preserved.

See the [validation record](https://github.com/Karikatun/agent-skills/blob/api-performance-review-v1.0.2/evaluations/api-performance-review/VALIDATION.md) for exact results and limits. The earlier baseline matched the skill's score; no measured quality advantage is claimed. Other hosts and operating systems remain unverified.

[Sources](references/sources.md) distinguish introductory inspiration from protocol standards and engineering guidance. Original package materials use the adjacent [MIT license](LICENSE). No endorsement by source authors or agent vendors is claimed.
