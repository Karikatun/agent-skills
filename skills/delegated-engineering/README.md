# Delegated Engineering

Version **2.4.3** reduces repeated reads/scans, unnecessary handoffs and duplicate review. Progress presentation remains removed; acceptance tracking, anti-stall behavior and required evidence/independence remain. The release links below select **2.4.3**. Runtime policy lives in [SKILL.md](SKILL.md) and its conditional references; this README documents the package, history and usage rather than creating another source of rules. Local package checks establish neither installation, host enforcement nor live runtime behavior.

## Changes and compatibility

**2.4.3** separates cheap `CONTROL_BASELINE`, targeted `CHANGE_SCOPE` and risk-triggered `EXPANDED_INVENTORY`. Known clean Git identities and trustworthy changed-path coverage support reuse; basenames, ignore rules and lockfiles cannot manufacture immutability or write coverage. Checks retain existing runner diagnostics without helper projects; one compatible worker executes known procedures at fitting low/medium effort. Gate ownership preserves required independent/specialist review and adds whole-scope review only for uncovered responsibilities. Optional indexed lexical search falls back to exact search/`rg`/Git; no new dependency, service or semantic search is added. Optional observed I/O/workflow counters are diagnostic only. No measured speedup is claimed.

The prior local WIP removed the progress pilot reference, Python helper, HTML template, helper tests and presentation duties. That removal remains: no panel integration, weighted milestones or UI reporting returns. Internal `AcceptanceState`, authority, WIP, anti-stall, required reviews, HARDENED closure and runtime-proof limits remain. Existing local copies must be compared with the release package before replacement; a shared version number does not prove identical bytes or installation.

**2.4.2** keeps the self-contained FAST protocol, responsibility/authority/WIP floor, workflow/risk routes and node-level model/effort selection in the entrypoint. Detailed scheduling/acceptance, evidence/snapshots, review, release and exceptional client settings each have one canonical reference. Repeated procedural scaffolding and policy recaps are shortened; dated source rationale belongs here. No new runtime files, metadata changes or architecture migration are introduced.

**2.4.1** added conservative ready-work scheduling, in-memory acceptance tracking, anti-thrashing and valid evidence reuse without repository scratch or unnecessary tree copies. Its rare empirical Astra exception requires real task-class outcomes; optional `task_class` and standalone `RoutingOutcome` support future comparison without a mandatory ledger or benchmarks. These capabilities remain in 2.4.2.

**2.4.0** introduced separate node-level model/effort selection with live client awareness and requested versus observed settings. Compatible GPT-6/GPT-6.1 user pins remain supported. Effort fields do not create runtime proof or another verification system.

2.4.3 retains 2.3.1's proportional workflow. The v2.2 compact protocol is not wire-compatible with strict v2.1 parsers; consumers must normalize its renamed/regrouped shapes. Strict consumers may also need to accept/normalize v2.4 effort fields and 2.4.1's optional node `task_class`. Optional `gates`, `evidence_coverage` and check `result` are additive; legacy acceptance/check/review fields normalize into gates. State refs now bind explicit controls + declared scope; strict consumers assuming a repository-wide tree must accept that semantic change or request justified expanded coverage. Internal acceptance state, diagnostic stats and `RoutingOutcome` are not mandatory receipt fields. This is source compatibility, not proof for every client.

## Runtime locations and examples

- [SKILL.md](SKILL.md): core authority/responsibility, FAST/FULL/HARDENED routes, self-contained FAST assignment/receipt, model/effort policy and completion floor.
- [Planning](references/planning.md): FULL classification, marginal-value phases, safe agent reuse, scheduling/capacity, acceptance tracking and stopping.
- [Execution](references/execution.md): FULL mutation/WIP and ordered fix/integration/release lifecycle.
- [Evidence contracts](references/evidence-contracts.md): evidence levels/coverage, schemas, snapshots/reuse, runner results, HARDENED provenance and runtime proof; optional observed telemetry.
- [Review profiles](references/review-profiles.md): independent gate responsibilities, conditional review depth and rework round limit.
- [Reasoning effort](references/reasoning-effort.md): actual client/inheritance/continuation compatibility questions and exceptional settings.

For example, an exact timeout lookup or known typo can use one Luna child and a focused answer/check with no DE reference files. An ordinary implementation often uses Sol medium, necessary local validation and required review if applicable; complex debugging can start Sol high. FULL adds only phases needed by the task. Project instructions and task-needed runbooks still apply; these examples illustrate the runtime policy rather than overriding it.

```text
Use $delegated-engineering to locate the reconnect timeout. Do not change code.
```

```text
Use $delegated-engineering to fix this known documentation typo and run the focused check.
```

## Install and validate

This standalone package contains Markdown instructions/references, UI metadata and the adjacent license. It has no services, third-party dependencies, custom installer, credential handling or automatic updater. Its existing metadata allows normal automatic skill discovery.

From a source checkout, inspect the package and place the complete `delegated-engineering` folder in the target agent's supported skills directory, comparing/preserving any existing copy. Source-checkout checks run from the repository root:

```sh
python3 -B scripts/check.py
```

This check covers package structure and configured fixtures, not agent behavior, host enforcement or review quality. Extracted skill archives omit root `scripts/check.py` and `INSTALLATION.md`; use the host-supported installation flow with the enclosed instructions. Source checkouts have agent-specific discovery details in root `INSTALLATION.md`. Installation and client/OS compatibility need their own evidence.

## Release references

Fixed **2.4.3** release references: [ZIP](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.4.3/delegated-engineering-2.4.3.zip), [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.4.3/delegated-engineering-2.4.3.zip.sha256).

To select that fixed tag with a supported installer:

```text
Use $skill-installer to install only delegated-engineering from https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v2.4.3/skills/delegated-engineering into my personal skills directory. Preserve any existing copy; do not install other skills.
```

The fixed [1.0.1 compatibility tag](https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v1.0.1/skills/delegated-engineering) remains available; a release reference never proves live verification.

## Model-policy provenance

The model/effort policy is a starting guideline, not measured superiority or an API default. Official sources previously checked on 2026-10-05:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): inheritance/configuration precedence.
- [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra): model-specific API efforts, distinct from live client support.
- [Model selection](https://developers.openai.com/api/docs/guides/model-selection) and [reasoning](https://developers.openai.com/api/docs/guides/reasoning): workload-dependent choices and distinct effort concepts.

These historical citations are documentation, not authority to alter scope/permissions or proof of current client support. No comparative agents, benchmarks or duplicate runs are required by the routing policy. Original material uses the adjacent [MIT license](LICENSE); external sources retain their own terms.
