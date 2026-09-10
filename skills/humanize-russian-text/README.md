# Humanize Russian Text

Version 1.0.0. Edit Russian copy for clear, natural language while preserving facts, uncertainty, conditions, and the user's requested register.

```text
Use $humanize-russian-text to rewrite this notice in neutral Russian. Preserve formal address, all dates, and the conditions. Return only the revised text.
```

Useful for interface messages, emails, explanations, and an explicit request to remove bureaucratic or repetitive phrasing. It does not impose slang, informal address, a fixed shortening percentage, or a personality. A factual three-item requirement stays intact. A correct short sentence may need no change.

The instructions are English; editing examples and output for Russian-copy tasks are Russian. The skill does not depend on a project, another skill, external word list, or runtime tool. It cannot determine authorship or guarantee that prose will pass an AI detector.

Copy the entire folder into your agent's supported personal skills directory, or ask Codex's `$skill-installer` to install only `skills/humanize-russian-text` from tag `humanize-russian-text-v1.0.0` of `Karikatun/agent-skills`. Compare and preserve local edits before replacing an existing folder.

This package independently rewrites an existing personal editing workflow. Its project-specific triggers and links to an external local word-list installation were removed; those external reference files are not redistributed. The examples in this package are newly written. Original materials use the adjacent [MIT license](LICENSE).

See the [validation record](https://github.com/Karikatun/agent-skills/blob/humanize-russian-text-v1.0.0/evaluations/humanize-russian-text/VALIDATION.md) for the exact synthetic checks. Editorial quality is audience-dependent; the evaluation does not establish a universal preference or compatibility with every agent.

## Install with Codex

Paste this into Codex when its built-in skill installer is available:

```text
Use $skill-installer to install only humanize-russian-text from https://github.com/Karikatun/agent-skills/tree/humanize-russian-text-v1.0.0/skills/humanize-russian-text into my personal skills directory. Preserve any existing copy; do not install other skills.
```
