# Documentation Update

Version 1.0.0. Audit or update project documentation against implementation evidence. Useful for changed configuration, workflows, integration failures, architecture, and guarantees stated more strongly than the code enforces.

```text
Use $documentation-update to update the README and operations guide for this diff. Do not change application code.
```

```text
Use $documentation-update to audit these documentation claims against the supplied code. Report findings only.
```

The workflow is independent of language, framework, and documentation generator. It follows the project's own conventions. A specification, a prompt instruction, a UI warning, a backend check, and a runtime observation are distinct evidence; the report preserves those distinctions. Missing implementation may prevent a conclusion.

Copy this entire folder into a supported personal skills directory, or ask Codex's `$skill-installer` to install only `skills/documentation-update` from the `documentation-update-v1.0.0` tag of `Karikatun/agent-skills`. Compare an existing installation before replacing it. No other skill, runtime script, or dependency is required. Host permissions remain in force.

This public workflow generalizes an existing project documentation practice. Product names, local paths, integration-specific source locations, and private examples were removed. The original project skill remains independently maintained. No private project material is included.

See the [validation record](https://github.com/Karikatun/agent-skills/blob/documentation-update-v1.0.0/evaluations/documentation-update/VALIDATION.md) for synthetic cases and limits. Local checks and scoped agent evaluation do not prove documentation correctness in arbitrary repositories. Original material uses the adjacent [MIT license](LICENSE).

## Install with Codex

Paste this into Codex when its built-in skill installer is available:

```text
Use $skill-installer to install only documentation-update from https://github.com/Karikatun/agent-skills/tree/documentation-update-v1.0.0/skills/documentation-update into my personal skills directory. Preserve any existing copy; do not install other skills.
```
