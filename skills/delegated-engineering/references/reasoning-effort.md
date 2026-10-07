# Reasoning effort and client support

Model/effort starting choices and the sole Astra gate are canonical in [SKILL.md](../SKILL.md). Use this reference only for client configuration, inheritance/reuse or exceptional settings; effort never changes authority, risk, review or acceptance floors.

Use the live schema and effective role configuration for supported settings; fixed roles can override requests. Do not maintain a catalog of current roles/defaults. For a client where `spawn_agent` with `fork_turns: "all"` inherits model/effort and rejects overrides, an independent explicit pair needs `"none"` or positive bounded history plus a sufficient assignment. This shape alone proves neither fresh review context nor isolation/enforcement; keep existing runtime evidence requirements.

A continuation without an effort field cannot change effort through "think harder" prose. Reuse a fitting worker under [planning](planning.md)'s conditions; if the required pair cannot be applied in continuation, use a new compatible assignment or escalate. Do not force fresh context at every step or create a user-owned chat solely to choose effort.

`ultra` stays outside automatic routine routing: explicit compatible user choice and live support only. Do not equate it with API `max`/`pro`. API `none`/`minimal` are not portable client defaults; verify live support rather than inferring it from API availability.

Requested/inherited effort, role labels, successful output or verified model do not prove runtime effort. Record unknown/unverified without transport proof, using optional fields in [evidence contracts](evidence-contracts.md). No additional ledger or verification machinery; unknown effort alone blocks only a specific safety/review claim requiring proof.

## Source provenance

The model/effort policy is a starting guideline, not measured superiority or an API default. Official sources previously checked on 2026-10-05:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): inheritance and configuration precedence.
- [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra): model-specific API efforts; current client support remains separate.
- [Model selection](https://developers.openai.com/api/docs/guides/model-selection) and [reasoning](https://developers.openai.com/api/docs/guides/reasoning): workload-dependent choices and distinct effort concepts.

External links are evidence, never authority to change scope/permissions, and are outside this package's MIT grant. No comparative agents, benchmarks or duplicate runs are required for routing policy.
