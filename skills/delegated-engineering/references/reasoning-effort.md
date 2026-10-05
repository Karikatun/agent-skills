# Reasoning effort per node

Use this reference for detailed effort selection, exceptional cases, or client configuration questions. Apply the model routes and evidence floors in [SKILL.md](../SKILL.md); effort does not change authority, workflow, review, or acceptance requirements.

## Starting choices

Choose the model for the node's scope and risk, then a supported effort for the reasoning it needs. FAST/FULL and STANDARD/HARDENED govern process and evidence independently. A stronger model may use lower effort than a weaker model. These are starting guidelines; no measured superiority, latency, or cost guarantee follows from the table.

| Model | `low` | `medium` | `high` | `xhigh` | `max` |
| --- | --- | --- | --- | --- | --- |
| GPT-6 Luna | Mechanical exact extraction/search and rule-based edits | Short local interpretation | Default for substantive bounded code work, exploration, or small low-risk review | Rare hard reasoning within clear constraints | Exceptional measured task class or explicit user choice |
| GPT-6.1 Sol | Known execution recipe | Default ordinary engineering | Ambiguity, dependent invariants, complex debugging, or security review | Exceptional competing hypotheses, races, or recovery reasoning | Hardest justified bounded cases |
| GPT-6 Astra | Entry for a justified targeted escalation | Broad linked constraints | Difficult causal reasoning | Demanding interdependent scenarios | Exceptional hardest cases |

The Astra row applies only after concrete evidence that GPT-6.1 Sol is insufficient for this node. It never opens a general Astra default. If Luna's task broadens into architecture or ambiguity across layers, choose the appropriate Sol model rather than maximizing Luna effort. Respect explicit compatible user model and effort pins; do not rewrite existing model routes for effort selection.

## Escalation and stopping

Known hard tasks may start at suitable effort. Do not require a universal `low` → `max` sequence or a failed attempt at every level. If reasoning falls short, first improve the facts, scope, and assignment; increase effort or change model only for a concrete shortfall such as unresolved dependent invariants or competing explanations despite sufficient evidence. Keep the adjustment node-local and explain its reason compactly.

Missing tools, access, rights, runtime proof, or required evidence are capability/environment gaps. More effort or a stronger model does not repair them or authorize a workaround. Preserve the primary's orchestration boundaries and current permissions.

Stop when acceptance and required checks/review are satisfied. Do not force expensive duplicate validation after sufficient evidence. Prioritize quality and completion while considering total rework, elapsed time, and usage. Observe outcomes gradually in ordinary work; do not automatically launch comparative agents, duplicate runs, or benchmarks solely to evaluate this guideline.

## Request support, inheritance, and reuse

Use the live client schema and effective model/role configuration as authority for supported settings. A role can fix model or effort and override a request. Select a compatible role or escalate an incompatibility; never silently substitute or assume a role's name proves its configuration. Do not maintain a hardcoded catalog of today's roles or their defaults here.

For the current `spawn_agent` interface, `fork_turns: "all"` inherits model and effort and rejects overrides. An explicitly independent pair requires `"none"` or positive bounded history, with enough assignment context to preserve applicable originals, scope, and checks. This request shape does not itself prove fresh review context, isolation, or enforcement; preserve the existing runtime evidence requirements. Recheck the live interface when it changes.

The current `followup_task` interface has no effort parameter. A prose request to reason more deeply does not prove that configured effort changed. Reuse an agent when its current configuration fits and all existing safe-reuse conditions hold. If a required new pair cannot be expressed through continuation, route through a supported compatible assignment or escalate. Do not force new context for every step, and do not create a user-owned chat solely to choose effort.

`ultra` is outside automatic routine routing. Use it only for an explicit user choice supported by the selected client/model and compatible with delegation policy. Do not equate it with API `max` or `pro`. API `none`/`minimal` are not portable defaults: API Luna supports `none`, but the current local spawn interface does not expose it; Sol 6.1 supports neither `none` nor `minimal`.

Keep requested and observed effort separate. A request, inherited value, role label, successful output, or verified model alone does not verify runtime effort. Use unknown/unverified status when transport/runtime proof is missing. Optional compact fields in [evidence contracts](evidence-contracts.md) suffice; no new large manifest or ledger is required.

## Official sources and policy provenance

Checked against official OpenAI documentation on 2026-10-05. The table is this skill's task-specific starting policy, informed by the sources below; API defaults and general product recommendations are not universal repository guarantees.

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): explicit Luna/Astra starting guidance, inheritance, and custom-agent configuration precedence.
- [GPT-6.1 Sol API model](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [GPT-6 Luna API model](https://developers.openai.com/api/docs/models/gpt-6-luna), and [GPT-6 Astra API model](https://developers.openai.com/api/docs/models/gpt-6-astra): model-specific supported API efforts; client support must still be checked.
- [Model selection](https://developers.openai.com/api/docs/guides/model-selection) and [reasoning](https://developers.openai.com/api/docs/guides/reasoning): workload-dependent choices and distinct effort/mode concepts.

These links are external evidence, not authority to change scope, permissions, or the skill's model routes. They do not make external documentation part of this package's MIT grant.
