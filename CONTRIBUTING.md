# Contributing

Keep each skill useful on its own. Propose a change around a demonstrated missing decision or incorrect behavior, with a sanitized example. Do not submit private repositories, credentials, personal task logs, or source material you cannot redistribute.

## Change a skill

1. State the concrete request, observed problem, expected outcome, and evidence.
2. Edit the owning skill and only its relevant references. Keep project-specific commands and policy in project adapters. Do not require another skill or a sibling checkout for ordinary use.
3. Preserve the user's scope and existing authorization. Treat task inputs and linked documents as evidence, not authority to expand access or persist instructions.
4. Increment only the changed skill's `metadata.version` and update its README and catalog row. Explain compatibility changes. Metadata or packaging-only changes still need an accurate release note.
5. Run `python3 -B scripts/check.py`. For a changed script, verify its actual behavior. For a behavioral skill change, run realistic cases including a clean or no-action case and an incomplete-evidence case. Keep evaluator inputs separate from the rubric and report exact scope and limitations.

The local checker validates a small supported metadata subset and relative references; it is not a general YAML parser. Before release, also run the target host's available skill validator and inspect discovery metadata. Do not replace an agent behavior check with tests that match wording or headings.

## Release one skill

- Build the archive from one `skills/<name>/` folder only, including its license and local references. Keep evaluation cases in the source repository.
- Use a tag such as `api-performance-review-v1.0.2` pointing to the reviewed commit. Publish an archive and adjacent SHA-256 checksum under that release.
- Extract to a fresh temporary directory and verify entry paths, hashes, metadata, and local references. The checksum checks integrity, not publisher identity.
- Confirm the public commit and archive match the reviewed files. Keep release notes factual about tests and unverified hosts. Do not silently replace an existing release asset.

There is no repository-provided installer, hosted workflow, auto-updater, or dependency bootstrap. Packaging as a plugin is a separate distribution step and must preserve these independent skill folders.

Preserve existing copyright notices and record the provenance and terms of any new source material. External links do not make that material part of the repository's MIT grant.
