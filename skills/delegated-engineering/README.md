# Delegated Engineering

Source version **2.4.1** is a compatible optimization patch over **2.4.0**. It retains node-level model/effort selection, client awareness and the existing FAST/FULL, STANDARD/HARDENED workflow, with a smaller shared instruction footprint and less repeated orchestration. Local package checks prove neither installation, host enforcement nor live runtime behavior.

A primary owns routing, scope, authority and synthesis; delegated children execute bounded discovery, planning, implementation, validation or read-only review. Integration and release remain separately authorized responsibilities. Optimize accepted results per total wall-clock time and usage, including retries, rework and repeated context; required safety and completion come first.

## 2.4.1 source release notes

- Consolidates model/effort choices in [SKILL.md](SKILL.md); retains compatible GPT-6/GPT-6.1 user pins, runtime/client limits and requested versus observed settings. Unknown effort alone does not block ordinary completion; no new verification machinery.
- Adds a rare empirical Astra exception beside concrete Sol insufficiency, requiring cited real task-class outcomes. HIGH_RISK/EXTREME never makes Astra the default. Optional `task_class` and standalone `RoutingOutcome` support future comparison without a ledger, benchmarks or invented metrics.
- Schedules independent ready work conservatively: FAST one child, ordinary FULL 1–2 concurrent children; unknown global capacity uses desired parallelism 2. Capacity denial keeps work pending for sequential execution, never raises model/effort.
- Tracks acceptance milestones in memory, changes stalled workflows after two empty cycles and finishes when mandatory gates are satisfied. No speculative phases or progress agent.
- Makes content-complete snapshots identify full content without copying trees. Reuses valid evidence/checks/reviews, preserves control and unknown-write comparisons, bans repository scratch and recursive evidence amplification, and reserves external byte storage for actual WIP/recovery/evidence needs.

Compatibility: 2.4.1 preserves 2.4.0 capabilities and 2.3.1's proportional workflow. The v2.2 compact protocol is not wire-compatible with strict v2.1 parsers; consumers must normalize its renamed/regrouped shapes. v2.4 effort fields and 2.4.1 optional node `task_class` may need acceptance/normalization in strict consumers. `RoutingOutcome` and progress are not mandatory receipt fields. This describes source compatibility, not proof for every client.

## Use the smallest sufficient path

[SKILL.md](SKILL.md) is the canonical route/model/effort policy and owns self-contained FAST projections. Simple exact lookup or deterministic reversible edits can use one Luna child and a focused check without a graph, planner or reviewer. FULL adds only real discovery, design choices, validation and required review; its lazy graph starts only when multiple substantive nodes are needed. Known difficult work starts at appropriate settings without a failed-model ladder.

Before adding an agent, planner, review, snapshot or expensive check, identify the unresolved question and how the result changes acceptance or the next decision. Prefer safe reuse when context overlaps and parallel execution would not shorten the critical path. Reuse requires unchanged scope, ownership, instructions/authority/skills, risk, responsibility, valid evidence and fitting model/effort configuration; required independence still needs a fresh reviewer. Runtime identity matters only to claims that depend on it.

STANDARD binds task-used originals, mandatory rules, scope, acceptance, checks and WIP safeguards. HARDENED always routes FULL for designated instruction/authority changes, skill modification/transfer/install/update, supply-chain paths, sensitive policy or provenance ambiguity. Skill changes bind the complete distributable tree, including `agents/openai.yaml`, under pre-change authority. Changed instructions cannot authorize themselves. Ordinary unchanged Markdown use does not load a package graph.

Every agent independently reads applicable authoritative originals; reading alone proves no compliance. Observable and independent rules need matching evidence. Preserve unrelated WIP. Primary verifies writes and protected repository state; discovery/planning/implementation/validation/review never stage for internal checkpoints. `LOCAL_READY` is local only: push, remote SHA/CI, merge, deployment and live proof each need explicit authority and separate evidence.

## Conditional references

FAST loads no delegated-engineering reference files, but still reads effective/nested `AGENTS.md`, mandatory project skills and task-needed runbooks/references. FULL uses [planning](references/planning.md); [execution](references/execution.md) for mutation/validation/integration/release; [review profiles](references/review-profiles.md) for required review; [evidence contracts](references/evidence-contracts.md) for expanded contracts, runtime identity or provenance (HARDENED loads it). [Reasoning effort](references/reasoning-effort.md) covers client/inheritance/reuse and exceptional settings, without repeating the canonical table.

Typical routes: exact lookup → Luna low → evidence answer; known typo → Luna low → edit → focused check → done; ordinary implementation → Sol medium → focused validation → required review if applicable. An unknown local bug needs focused discovery only if current evidence is insufficient; complex debugging can start Sol high. Astra eligibility is defined only in [SKILL.md](SKILL.md).

## Install, validate, and use

This package is a standalone instruction skill: it contains Markdown instructions, references, UI metadata, and the adjacent license. It has no services, dependencies, custom installer, credential handling, or automatic updater.

Source-checkout only: inspect `SKILL.md` and the references, then place the complete `delegated-engineering` folder in the supported skills directory of the target agent. Preserve and compare an existing copy before replacement. The repository's local package checks are run from the repository root:

```sh
python3 -B scripts/check.py
```

Those checks cover package structure and fixture facts; they do not run an agent, prove host enforcement, or establish review quality. An extracted skill package does not contain `scripts/check.py` or the root `INSTALLATION.md`; read its `SKILL.md`, references, and README, then use the host-supported install flow. Installation and compatibility with every client or operating system require their own evidence. See the repository root's `INSTALLATION.md` for agent-specific discovery details when working from source.

Invoke the installed skill with a focused request, for example:

```text
Use $delegated-engineering to locate the reconnect timeout. Do not change code.
```

```text
Use $delegated-engineering to fix this known documentation typo and run the focused check.
```

## Release references

Published release **2.4.0** references (current source is **2.4.1**, not yet a published archive): [ZIP](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.4.0/delegated-engineering-2.4.0.zip) and [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.4.0/delegated-engineering-2.4.0.zip.sha256). Release links do not prove that a package has been installed or verified live.

To select the fixed 2.4.0 tag with a supported installer:

```text
Use $skill-installer to install only delegated-engineering from https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v2.4.0/skills/delegated-engineering into my personal skills directory. Preserve any existing copy; do not install other skills.
```

Delegated Engineering 1.0.1 also remains available as a fixed release tag for compatibility:

```text
Use $skill-installer to install only delegated-engineering from https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v1.0.1/skills/delegated-engineering into my personal skills directory. Preserve any existing copy; do not install other skills.
```

Original material uses the adjacent [MIT license](LICENSE).
