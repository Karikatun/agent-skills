# Agent Skills

Focused, reusable workflows for coding agents. Install only the skills you need; each folder contains its own instructions and supporting resources.

[Русская версия](README.ru.md)

## Available skills

| Skill | Version | Use it for |
| --- | --- | --- |
| [API Performance Review](skills/api-performance-review/README.md) | 1.0.2 | Trace request cost, scaling, retries, caching, and failure behavior; distinguish defects from missing evidence |
| [Learn from Task](skills/learn-from-task/README.md) | 1.0.0 | Extract useful lessons from completed work and propose the smallest durable improvement before writing it |

Both skills are instruction-only, written in English, and answer in the user's language. They require no other skill, package, MCP server, subscription beyond the chosen agent host, or API key. Optional evaluation scripts use Python 3.9+ and its standard library.

## Install one skill

Choose a versioned archive from [Releases](https://github.com/Karikatun/agent-skills/releases), verify its adjacent SHA-256 checksum, and extract it. Copy the single skill folder into your agent's supported skills directory. Keep `SKILL.md`, references, metadata, and the license together.

For local Codex use, the documented personal directory is `$HOME/.agents/skills`; on Windows it is `.agents/skills` inside your user profile. If the destination already exists, compare it with the new version and preserve any local edits before replacing that specific folder. Do not keep backup copies inside a scanned skills directory.

You can also obtain the source with:

```sh
git clone https://github.com/Karikatun/agent-skills.git
```

Copy only the desired folder from `skills/`. For repeatable installations, select a release tag or exact commit rather than following a moving branch. There is no installer or automatic updater.

In Codex, invoke a skill explicitly:

```text
Use $api-performance-review to review GET /orders. Do not change code.
```

```text
Use $learn-from-task to review the completed task and propose useful lessons. Do not write them yet.
```

Restart the client if a newly copied skill is not discovered. The workflow format follows the [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills), checked on 2026-09-10. OpenAI recommends plugins for installable distribution; this initial release provides standalone folders and archives. No plugin-directory listing or installation in every agent host is claimed.

## Scope and evidence

The workflows do not depend on a particular application language or framework. Host behavior is separate: local Codex-format validation and bounded agent evaluations do not prove compatibility with every agent or operating system.

- [API review evidence](evaluations/api-performance-review/VALIDATION.md): synthetic cases, executable fixture checks, and explicit limits. The earlier baseline comparison did not establish an improvement over the baseline.
- [Learning workflow evidence](evaluations/learn-from-task/VALIDATION.md): synthetic proposal, no-lesson, approved-update, and untrusted-input cases.
- [Security boundaries](SECURITY.md): access, source provenance, evaluation scope, and known limits. Skill instructions do not create a sandbox.

To run local package checks and the seven API fixture tests:

```sh
python3 -B scripts/check.py
```

This command checks package structure and the facts built into fixtures; it does not run an agent or prove review quality. Agent evaluation procedures are documented beside each case suite.

## Contribute and maintain

See [CONTRIBUTING.md](CONTRIBUTING.md). Each skill has its own version and release archive. Project-specific commands, policies, paths, and examples belong in the consuming project's configuration, not in a shared runtime dependency on another checkout.

Original material is available under the [MIT license](LICENSE). The API skill retains its original copyright notice. Linked standards and other third-party sources retain their own terms; links do not relicense those sources.
