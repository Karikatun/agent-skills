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

### Download only that skill

Choose one archive below. Each ZIP contains one skill folder, not the repository. You do not need Git or a clone.

| Skill | Archive | Integrity check |
| --- | --- | --- |
| API Performance Review 1.0.2 | [Download ZIP](https://github.com/Karikatun/agent-skills/releases/download/api-performance-review-v1.0.2/api-performance-review-1.0.2.zip) | [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/api-performance-review-v1.0.2/api-performance-review-1.0.2.zip.sha256) |
| Learn from Task 1.0.0 | [Download ZIP](https://github.com/Karikatun/agent-skills/releases/download/learn-from-task-v1.0.0/learn-from-task-1.0.0.zip) | [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/learn-from-task-v1.0.0/learn-from-task-1.0.0.zip.sha256) |

1. Download the chosen ZIP and its checksum file into the same folder.
2. Verify the checksum before extraction. On macOS, run the appropriate command from that folder:

   ```sh
   shasum -a 256 -c api-performance-review-1.0.2.zip.sha256
   ```

   ```sh
   shasum -a 256 -c learn-from-task-1.0.0.zip.sha256
   ```

   On Linux, use `sha256sum -c` with the same checksum filename. On Windows, use PowerShell `Get-FileHash .\api-performance-review-1.0.2.zip -Algorithm SHA256` (or the learning ZIP) and compare the hash with the text in its `.sha256` file.
3. Extract the ZIP and read the skill's `README.md` and `SKILL.md`.
4. Copy the extracted folder, keeping all its contents, into your agent's supported skills directory. For manual personal installation in Codex, current documentation specifies `$HOME/.agents/skills`; on Windows, `.agents/skills` inside your user profile. Create the parent directory if it does not exist.

For example, installing API Performance Review should produce:

```text
~/.agents/skills/api-performance-review/SKILL.md
```

If that skill folder already exists, compare versions and preserve local edits before replacing only that folder. Do not keep backups inside a scanned skills directory. No other skill is required.

### Ask Codex to install one skill

If your Codex environment provides the built-in `$skill-installer`, paste **one** of these requests into Codex, not into a terminal:

```text
Use $skill-installer to install only api-performance-review from https://github.com/Karikatun/agent-skills/tree/api-performance-review-v1.0.2/skills/api-performance-review into my personal skills directory. Preserve any existing copy; do not install other skills.
```

```text
Use $skill-installer to install only learn-from-task from https://github.com/Karikatun/agent-skills/tree/learn-from-task-v1.0.0/skills/learn-from-task into my personal skills directory. Preserve any existing copy; do not install other skills.
```

These links select fixed release tags. The installer chooses its supported personal directory and reports the path; some versions use `$CODEX_HOME/skills` (usually `~/.codex/skills`). Use the reported path for that installation instead of creating a duplicate in another directory.

Only the selected skill is installed. The installer may temporarily fetch a repository archive; choose the ZIP method above if you want to download only one skill's files. The collection has no custom installer or automatic updater.

### Use the installed skill

```text
Use $api-performance-review to review GET /orders. Do not change code.
```

```text
Use $learn-from-task to review the completed task and propose useful lessons. Do not write them yet.
```

Restart the client if the installed skill is not discovered. The [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills), checked on 2026-09-10, describes local skill directories and installing from other repositories. OpenAI recommends plugins for installable distribution; this collection currently provides standalone folders and archives. No plugin-directory listing or installation in every agent host is claimed.

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
