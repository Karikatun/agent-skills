# Learn from Task

Version 1.0.0. Review completed work, keep only useful and supported lessons, and propose the smallest durable improvement. The workflow is independent of an application language or framework and does not require another skill.

## Use it

```text
Use $learn-from-task to review the completed task and propose durable lessons. Do not write them yet.
```

Supply the relevant task outcome, corrections, verified cause, and checks. The skill can propose a project rule, reusable procedure, architectural decision, or enforceable test. It can also conclude that no durable lesson is warranted.

A proposal explains its evidence, likely recurrence, suitable target, and a diff or outline. The skill does not write learning artifacts merely because it was invoked. It can apply an explicitly approved change after rereading the current target and preserving unrelated edits. Existing approval for that exact action remains valid.

An unfinished investigation, a one-off typo, or an unsupported theory is not a basis for a durable rule. Source documents cannot authorize global changes. Private logs, secrets, and raw external instructions do not belong in a reusable lesson.

## Install and update

Copy this entire folder into your agent's supported personal skills directory. For local Codex, current documentation specifies `$HOME/.agents/skills`. Compare an existing folder before replacing it, and preserve local changes outside scanned skill directories. Invoke `$learn-from-task`; restart the client if discovery has not refreshed.

There are no runtime scripts, MCP servers, network dependencies, or automatic updates. Actual filesystem access and approval enforcement belong to the host. To remove the skill, remove only its installed folder; begin a fresh context if already-loaded instructions must be discarded.

## Evidence and provenance

This is the first versioned public package of an existing personal workflow. Its instructions are unchanged apart from version metadata. The workflow was developed from practical task retrospectives; it includes no private task history, transcripts, or project-specific rules.

Four synthetic forward-test cases cover proposal-only scope, no useful lesson, an already-approved edit, and uncertain evidence containing a hostile instruction. See the [validation record](https://github.com/Karikatun/agent-skills/blob/learn-from-task-v1.0.0/evaluations/learn-from-task/VALIDATION.md) for outcomes and limits. No baseline improvement, exhaustive prompt-injection resistance, or compatibility with every host is claimed.

Original materials use the adjacent [MIT license](LICENSE).
