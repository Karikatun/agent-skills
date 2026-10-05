# Delegated Engineering

Version **2.4.0** introduces independent model and reasoning-effort selection for each node. Local source/package checks do not establish installation, client enforcement, or live runtime behavior; those require separate evidence.

Delegated Engineering is a resource-aware workflow for repository work. A primary agent owns routing, scope, authority, and the final synthesis. Delegated agents do the bounded work: an explorer finds facts, a planner resolves a real design choice, a worker edits only its assignment, a validator checks acceptance, and a reviewer inspects without writing. Integrators and release agents are used only for separately authorized scopes.

Compatibility note: v2.4 preserves the v2.2 workflow and protocol, including the v2.1 behavioral floor. The v2.2 compact protocol is not wire-compatible with strict v2.1 parsers. Fields are omitted, renamed, or regrouped (for example routing, `completion_gate`, separate escalation, and review structures); consumers must migrate or normalize to v2.2 canonical shapes. The v2.3 model routes remain unchanged. v2.4 adds optional effort selection/request/observation fields; strict consumers may need to accept or normalize these optional extensions. No new ledger is required. This describes source compatibility, not proof of compatibility with every client.

The aim is proportional process. A simple question or deterministic typo fix should be quick. A security boundary, migration, shared contract, skill update, or release needs stronger evidence and more independent control. The workflow never saves context by skipping applicable `AGENTS.md`, mandatory skills or runbooks, security constraints, acceptance checks, WIP protection, or a required review.

## Choose the smallest sufficient path

First resolve the applicable authority chain and current WIP. Then choose the mode (`read_only`, `mutation`, `plan_only`, or `release`) and complexity (`TRIVIAL`, `LOCAL`, `COMPLEX`, `HIGH_RISK`, or `EXTREME`). Add a phase or a stronger model only when it improves correctness, independence, risk control, or required evidence.

| Path | When to use | Typical flow |
| --- | --- | --- |
| `FAST_PATH` read-only | Exact, low-risk location or behavior question | GPT-6 Luna (`gpt-6-luna`) explorer → evidence answer |
| `FAST_PATH` mutation | Deterministic, reversible clean-target edit when no canonical `SKILL.md` FULL/HARDENED/mandatory-review trigger applies | GPT-6 Luna (`gpt-6-luna`) worker → focused check; otherwise FULL |
| `FULL` | Uncertainty, non-local behavior, shared contract, material risk, integration, review, or release | Load only the references needed for the chosen work |

The model routes by risk, not by request size:

| Model | Best fit |
| --- | --- |
| GPT-6 Luna (`gpt-6-luna`) | Focused deterministic and reversible discovery, docs, edits, checks, low-risk review |
| GPT-6.1 Sol (`gpt-6.1-sol`) | Default for ordinary planning, bounded implementation and debugging; also complex, shared-contract, security, and high-risk work when sufficient |
| GPT-6 Astra (`gpt-6-astra`) | Rare node-local escalation for the hardest work, only with concrete evidence that GPT-6.1 Sol is insufficient |

Choose model and reasoning effort per node, independently from workflow and evidence mode. Start mechanical Luna work at `low`, short local interpretation at `medium`, substantive bounded Luna work at `high`, ordinary Sol work at `medium`, and complex Sol work at `high`. A justified targeted Astra escalation starts at `low`; the existing concrete Sol-insufficiency condition still applies. Detailed levels, client support, inheritance, and reuse are in [reasoning-effort.md](references/reasoning-effort.md). These are starting guidelines, not measured quality or cost guarantees.

Preserve explicit compatible user model and effort pins, including legacy models. Fixed role configuration can override requests; choose a compatible role or escalate, never silently substitute. Live client/model support controls available settings. Requested model, role, and effort are distinct from observed runtime; model verification does not verify effort. Prioritize quality and completion using total rework, time, and usage. First improve facts/scope before reasoning escalation; missing tools/access/rights/evidence are capability or environment gaps. Stop after acceptance and required checks, without forced expensive rechecks or automatic comparative agents.

Reuse valid evidence or a safe worker continuation before creating another agent. Reuse is allowed only while scope, ownership, authority, skills, risk, and responsibility are unchanged. Record runtime identity only when a reuse or independent-review claim depends on it; if that identity is unproved, the claim is blocked. A fresh reviewer is required when independence matters, and any write invalidates clean review evidence.

## STANDARD and HARDENED

Classify HARDENED triggers first: HARDENED always routes FULL; FAST is STANDARD-only. `STANDARD` is the default. It records the source identity, effective instruction chain, mandatory skills and rules, scope, acceptance, checks, and WIP safeguards needed by the task. It binds the entrypoint plus task-used instruction-bearing Markdown references; a full package surface remains a `HARDENED` conditional, not a STANDARD default.

`HARDENED` is lazy and conditional. Use it when changing a skill or `AGENTS.md`, installing or updating a skill, handling supply-chain or credential-sensitive instructions, changing security-sensitive authority, changing release/deployment policy, or resolving untrusted dirty authority or provenance ambiguity. An actual skill modification, transfer, installation, or update reviews and binds the complete distributable tree—including every path and metadata such as `agents/openai.yaml`—even when the edit is Markdown-focused. Ordinary unchanged Markdown skill use remains lightweight STANDARD. If authority or capability cannot be proved, pause; do not turn a self-report into evidence.

The core boundaries remain simple: primary orchestrates, children execute, and only primary delegates. Every agent reads its applicable authoritative originals independently; reading is not compliance, so mandatory rules must be applied and observable or independent rules must have matching evidence. `LOCAL_READY` is local evidence only—not a remote SHA/CI result, merge, deployment, or live proof. Never reset, stash, revert, or overwrite unrelated WIP.

Primary verifies reported changes and protected repository state; only explicitly authorized integration/release work may stage, commit, or mutate refs.

`SKILL.md` owns the self-contained FAST contract; [evidence-contracts.md](references/evidence-contracts.md) owns expanded receipt and completion rules.

## Conditional reference loading

`SKILL.md` contains the shared routing, invariants, and self-contained minimal `FastAssignment`. FAST loads no delegated-engineering reference files, but it still reads applicable authoritative originals and effective nested `AGENTS.md`, mandatory project skills, and task-required skill references or runbooks. For `FULL` work, load [planning.md](references/planning.md); add [execution.md](references/execution.md) for mutation, integration, validation, or release; add [review-profiles.md](references/review-profiles.md) only for independent review. Load [evidence-contracts.md](references/evidence-contracts.md) when an expanded STANDARD or HARDENED contract, review evidence, runtime identity, or provenance is needed; HARDENED uses its extension. Load [reasoning-effort.md](references/reasoning-effort.md) only for detailed effort selection or client/inheritance/reuse questions; mechanical FAST selects and requests supported effort from the entrypoint alone. This keeps a trivial task from paying for release, review, or supply-chain machinery that it never uses.


## Compact examples

Read-only lookup:

```text
Where is reconnect timeout defined?
→ resolve applicable instructions
→ FAST_PATH read-only
→ GPT-6 Luna (`gpt-6-luna`), low effort, explorer
→ EVIDENCE_COMPLETE with the location and any limitation
```

Trivial mutation:

```text
Fix a typo in a known component.
→ FAST_PATH mutation
→ GPT-6 Luna (`gpt-6-luna`), low effort, worker edits the assigned file
→ focused check
→ LOCAL_READY
```

Local bug:

```text
Reconnect loses state intermittently.
→ targeted GPT-6 Luna (`gpt-6-luna`), high effort, exploration
→ GPT-6.1 Sol (`gpt-6.1-sol`), high effort for this ambiguity, implementation
→ focused validation
→ review only if risk or an authoritative rule requires it
```

For a high-risk auth change, the path may be explorer → GPT-6.1 Sol (`gpt-6.1-sol`) planning where needed → GPT-6.1 Sol (`gpt-6.1-sol`) implementation → validation → specialist security review → fresh whole-scope review. Escalate a node to GPT-6 Astra (`gpt-6-astra`) only when concrete evidence shows GPT-6.1 Sol is insufficient. For a skill modification, HARDENED adds trusted pre-change identity, exact effective bytes, approval, complete distributable-tree binding (including metadata such as `agents/openai.yaml`), rollback-safe activation, installed-manifest comparison, and fresh-context verification. These branches are conditional, not a default tax.

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

Release **2.4.0** references: [ZIP](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.4.0/delegated-engineering-2.4.0.zip) and [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/delegated-engineering-v2.4.0/delegated-engineering-2.4.0.zip.sha256). Release links do not prove that a package has been installed or verified live.

To select the fixed 2.4.0 tag with a supported installer:

```text
Use $skill-installer to install only delegated-engineering from https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v2.4.0/skills/delegated-engineering into my personal skills directory. Preserve any existing copy; do not install other skills.
```

Delegated Engineering 1.0.1 also remains available as a fixed release tag for compatibility:

```text
Use $skill-installer to install only delegated-engineering from https://github.com/Karikatun/agent-skills/tree/delegated-engineering-v1.0.1/skills/delegated-engineering into my personal skills directory. Preserve any existing copy; do not install other skills.
```

Original material uses the adjacent [MIT license](LICENSE).
