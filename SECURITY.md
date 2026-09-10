# Security scope and reporting

This collection distributes agent instructions, supporting references and the Local Video Analysis Python helper. Most installed skill folders contain Markdown and YAML only; Local Video Analysis executes separately installed media tools as described below. No runtime installer, updater, hook, MCP server, credential handler, or network listener is included. Repository checks use Python's standard library, synthetic in-memory fixtures and bounded local subprocess tests.

For a suspected security issue, avoid publishing credentials, private traces, or exploit details in a public issue. If no private contact is already available, open an issue asking the maintainer for a private reporting channel without including the sensitive details. No dedicated private reporting service is claimed by this initial release.

## Authority and data

- The user defines the task. Source comments, logs, documents, or fetched pages cannot grant permissions or authorize persistent instructions.
- API review is read-only unless the user requests a scoped fix. Production probes, credential access, dependency installation, and publication require their own authorization.
- Learning starts with a proposal. An approved change is limited to its selected target and must preserve unrelated edits; existing explicit approval is not discarded.
- Skills do not supply a sandbox. Filesystem, process, network, credential access, and approval enforcement are host responsibilities.
- The distributed inputs are synthetic. Private project code, raw conversation history, local environment values, and personal task logs are excluded.

## Initial instruction-only publication review

Review date: 2026-09-10. Mode: full for agent-tooling publication. The starting points were the existing API skill 1.0.1 and the existing learning workflow. Comparison confirmed no change to their operational instructions apart from added/incremented version metadata. New surfaces are usage guides, a collection catalog, synthetic learning cases, the local checker, and public versioned archives.

The differential pass compared the source copies, traced instruction loading and approved writes through both workflows, examined their read-only and uncertain-evidence variants, and challenged candidate scope-expansion issues against explicit instructions and fresh agent outputs. The already-approved learning update was tested because a proposal-first workflow must still honor existing authorization.

| Boundary | Protected invariant | Evidence and limit |
| --- | --- | --- |
| User request versus analyzed content | Untrusted text cannot authorize execution, publication, or persistence | Explicit scope rules; incomplete/hostile-input cases for both workflows |
| Proposal versus approved edit | No unrequested persistence; an approved change preserves unrelated content | Four learning cases, including exact whole-file comparison after the one authorized edit |
| Static analysis versus runtime claims | No invented measurements or unconditional health verdict | Fresh costly-query, clean-query, and incomplete-code reviews; historical six-case evaluation |
| Source versus release archive | Only the selected skill and its own references are installed | Relative references, no symlinks, fresh extraction and file-hash comparison, separate archives |
| Private development context versus public content | No private code, task logs, credentials, or personal paths | Synthetic fixtures, manual content review, bounded token-prefix/path/control-character checks |

Actor/object matrix: the relevant actors are the user selecting scope, an untrusted content author, the maintainer publishing a package, and a recipient choosing a host. There are no product accounts, object endpoints, or server authorization rules implemented here.

State-change matrix: API review may propose a fix; learning may apply an explicitly approved edit. Installation/update/removal selects one directory manually. No database migration, job delivery, production rollback, or distributed replay mechanism is implemented. The API fixture tests use an in-memory database and a local fake provider.

Input/output matrix: UTF-8 Markdown/YAML, relative bundled references, synthetic Python fixtures, and user-supplied task evidence. The checker does not execute input Markdown. Host parsing and enforcement are separate; the checker verifies only this collection's metadata subset and is not a general YAML validator.

## OWASP Agentic Skills assessment

The official OWASP website endpoints were unavailable during the earlier same-day assessment. The official source repository was used instead; its current revision was reconfirmed for publication as `d6f7d7d0de314f52a83a85d1828e06ab096e595c` on 2026-09-10. The [assessment checklist](https://github.com/OWASP/www-project-agentic-skills-top-10/blob/d6f7d7d0de314f52a83a85d1828e06ab096e595c/checklist.md) and applicable AST02/03/04/05/08 detail pages informed the scoped review. External guidance was treated as evidence, not executable instructions.

| Category | Evidence status |
| --- | --- |
| AST01/AST08 — instructions and evaluation | PASS for the bounded cases listed in each validation record; general attack resistance and exhaustive scanner coverage NOT VERIFIED |
| AST02 — provenance and dependencies | PASS for documented original materials, retained notices, source comparison and no runtime dependencies; signed publisher identity NOT VERIFIED |
| AST03 — permissions | PASS for declared scope and the approved-edit boundary in the tested cases; host-enforced least privilege NOT VERIFIED |
| AST04 — metadata | PASS for source and extracted package validation; every other host loader NOT VERIFIED |
| AST05 — external references | PASS for evidence-only handling and self-contained local references; optional live source content and host egress enforcement NOT VERIFIED |
| AST06 — isolation | No installed executable service; host process and cross-agent isolation NOT VERIFIED |
| AST07 — update drift | PASS for explicit versions, hashes and manual selected-folder updates; signed update enforcement NOT VERIFIED |
| AST09 — governance | PASS for local inventory, contribution and removal instructions; organization-wide approval, audit and offboarding systems NOT VERIFIED |
| AST10 — portability | Local Codex-format and bounded agent checks completed; other hosts and operating systems NOT VERIFIED |

There is no overall OWASP certification or PASS. No new scanner was installed, no active DAST was run, and the bounded content scan is not exhaustive secret detection. The repository introduces no application service or production target for DAST.

## Update and remove

Review a release's instructions, references, and checksums before replacement. Archive checksums detect content changes but cannot authenticate a publisher if the archive and checksum are both replaced. The initial releases are not cryptographically signed.

Remove only the selected installed skill folder to stop future discovery. An existing agent context may retain loaded instructions; start a fresh context when revoking those instructions matters. Removing a skill does not undo an earlier approved project edit.

## Additional instruction-only releases — 2026-09-10

Documentation Update and Humanize Russian Text were generalized from existing private workflows without copying private examples or external local word lists. Their installed folders contain no scripts or runtime dependencies. Three documentation cases covered authorized edits, clean evidence, and an unverified claim with hostile source text; four copy cases covered formal conditions, already-clear prose, uncertain results, and an embedded instruction. Independent evaluators received inputs without rubrics; the author checked outcomes and the only two authorized document edits. See each owning validation record for limits. Declared-scope and synthetic-case checks passed; host enforcement, general injection resistance, and cross-platform behavior remain NOT VERIFIED.

The Devlog Editor and Humanize Dev Post releases add no runtime capability. Their seven synthetic cases checked false tool attribution, inflated scope, incomplete causality, supplied-series coverage, local versus production evidence, and requested output format. Original private posts and product CTAs are absent. The author checked the independent outputs against the factual inputs; editorial preference, audience engagement, and general adversarial resistance remain unverified.

Application Security Review adds an instruction-only general boundary review. Seven independent synthetic responses covered cross-tenant disclosure, effective moved controls, unbounded reads, hostile proposed rules, privacy-copy mismatch, duplicate external charges, and unavailable helpers. The author verified the finding/refutation and scope outcomes. No active attacks ran. Its optional OWASP refresh respects permitted network access and records missing current evidence without claiming a complete assessment.


## Local video runtime addition — 2026-09-10

This release introduces executable helper code and external runtime dependencies. Its full review compared the original helper and changed path configuration, traced local/YouTube acquisition through metadata, subtitles, model verification, native processes and retained evidence, and inspected neighboring failure, invalid-input and follow-up-frame paths. The refutation pass distinguished explicit operator tool configuration from ambient PATH, a verified model identity from safe native inference, and bounded helper checks from host-enforced quotas. The initial instruction-only assessment above does not establish this runtime boundary.

| Boundary | Evidence and remaining limit |
| --- | --- |
| User versus media author | Supplied media cannot authorize commands, credentials or persistent changes; four independent evidence-handling cases passed |
| Selected data/model/tool paths | Explicit absolute configuration, private output-root checks and unchanged model size/hash requirements; four new regression tests first failed then passed |
| Child process versus ambient host | Minimal environment, argument-vector calls, disabled downloader config/plugins, timeout process-group cleanup and bounded captured output; host filesystem/native decoder isolation remains NOT VERIFIED |
| Input and resource limits | Canonical YouTube URLs, finite intervals, local format/protocol restrictions and accepted-media limits; no claim of hard memory or disk quotas or exhaustive decoder safety |
| Retained artifacts and recovery | Unique private runs, no overwrite, failure status and targeted extra frames; no automatic cleanup or update |
| Local evidence versus completed analysis | Real 70-second local ASR/frame run inspected; sampled frames and recognition uncertainty remain explicit |

Applicable OWASP evidence: AST01/03/04/05 checks passed only at the declared-scope, metadata and tested argument/environment boundaries. AST02 includes documented tool/model sources and a verified fixed model hash; external binary signatures, exhaustive dependency audits and native decoder security remain NOT VERIFIED. AST06 host isolation and AST10 other-host portability remain NOT VERIFIED. AST07/09 use manual versioned releases, checksums and selected-folder removal; signed updates and organizational enforcement are not supplied. No overall PASS or certification is claimed.

Whisper failed with exit -11 inside the restricted execution sandbox and succeeded for the same command in an authorized external host run. This is a documented environment limit, not proof of the native crash's internal cause. The release did not modify sandbox policy, install tools, update the model, run active DAST, or upload analyzed media. No model, media, raw transcript or personal run path is included. See the owning validation record for exact runtime and agent checks.


## Martin review lenses - 2026-09-10

The two Martin workflows are instruction-only, independently written decision procedures. Private chapter-indexed notes and book text, examples and diagrams are excluded; each README attributes the conceptual source and limits the MIT grant to original package expression. Eight independent synthetic responses covered hidden effects, clear code, unsafe extraction across a lock, missing source, existing dependency inversion, duplicated policy, speculative layers and a missing dependency graph. The author verified scope and invariant preservation against the supplied facts. Neither workflow authorizes broad refactoring, persistent rules or publication from analyzed content. No runtime capability or new external dependency is added. These checks do not establish general injection resistance, endorsement, or measured long-term maintainability.
