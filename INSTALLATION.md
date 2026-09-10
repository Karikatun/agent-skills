# Install Agent Skills

[Русская версия](INSTALLATION.ru.md) · [Skill catalog and downloads](README.md)

Install one skill in any of the 12 agent families below. Paths and commands were checked against official documentation on September 10, 2026. Installation and execution of this collection have not been tested in all 12 clients.

## Install one skill

1. Choose a skill in the [download table](README.md#download-only-that-skill) and download its ZIP and matching `.sha256` file into the same folder. No repository clone is needed.
2. Verify the checksum before extraction. For API Performance Review 1.0.2, run `shasum -a 256 -c api-performance-review-1.0.2.zip.sha256` on macOS or `sha256sum -c api-performance-review-1.0.2.zip.sha256` on Linux. In PowerShell, run `Get-FileHash .\api-performance-review-1.0.2.zip -Algorithm SHA256` and compare the result with the downloaded `.sha256` file. This checks integrity, not publisher identity.
3. Extract into a separate folder and read its `README.md`, `SKILL.md`, and any included scripts.
4. Choose a personal installation for your projects or a project installation for one repository. Copy the **entire skill folder**, keeping its name and all included resources, into one directory from the table below. Create the parent directory if needed. Avoid an extra nesting level.
5. If a folder with the same name already exists, compare versions and preserve local edits outside discovery directories before replacing it. Do not automatically merge old and new versions. If the client already discovers the skill through a compatible directory, keep a single copy.
6. Refresh discovery or start a new session, then check loading as described for your agent.

The resulting path is `<skills-directory>/api-performance-review/SKILL.md`. The table lists directories **without** the skill name. `~` means your home directory; on a supported Windows client, use the corresponding path inside your user profile. Check the client's operating-system availability separately.

## Agent directories

Agent names link to official documentation. Each row selects one documented path; the sections below mention compatible alternatives where they help avoid duplicates.

| Agent | Personal installation | At the project root |
| --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills/` | `.agents/skills/` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` |
| [Cursor](https://cursor.com/docs/skills) | `~/.cursor/skills/` | `.cursor/skills/` |
| [GitHub Copilot](https://code.visualstudio.com/docs/agent-customization/agent-skills) | `~/.copilot/skills/` | `.github/skills/` |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | `~/.gemini/skills/` | `.gemini/skills/` |
| [Devin Desktop / Windsurf: Cascade](https://docs.devin.ai/desktop/cascade/skills) | `~/.codeium/windsurf/skills/` | `.windsurf/skills/` |
| [Cline](https://docs.cline.bot/customization/skills) | `~/.cline/skills/` | `.cline/skills/` |
| [OpenCode](https://opencode.ai/docs/skills/) | `~/.config/opencode/skills/` | `.opencode/skills/` |
| [Amp](https://ampcode.com/docs/customize/skills) | `~/.config/agents/skills/` | `.agents/skills/` |
| [Kiro](https://kiro.dev/docs/skills/) | `~/.kiro/skills/` | `.kiro/skills/` |
| [Google Antigravity](https://antigravity.google/docs/skills) | `~/.gemini/config/skills/` | `.agents/skills/` |
| [Kilo Code](https://kilo.ai/docs/customize/skills) | `~/.kilo/skills/` | `.kilo/skills/` |

### Codex: app, CLI, and IDE extension

Use a directory from the table and start a new session if discovery has not refreshed. Select the skill using the available picker or ask to use it by name. Each skill README also has a version-tagged `$skill-installer` request. If the built-in installer reports a different supported directory, use that result and avoid a second manual copy. Local discovery does not establish installation in a cloud environment.

### Claude Code

Copy the folder into one Claude Code directory. In a new session, invoke `/api-performance-review` with your task. A personal folder on your computer is not automatically available in Cowork or cloud sessions; those have separate documented sources. This guide covers local installation.

### Cursor

After copying, open `Customize → Skills` and find the skill. Start a new session if discovery has not refreshed. Cursor also reads `.agents/skills` and compatible Claude/Codex directories, so check for duplicates. Synchronizing personal `~/.cursor/skills` with Cloud Agents is a separate action; `~/.agents/skills` is not automatically copied there.

### GitHub Copilot: VS Code and CLI

In VS Code, open `/skills` or `Chat: Open Customizations` and check Skills. Invoke `/api-performance-review` explicitly when needed.

In [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), run `/skills reload` in chat, then `/skills info api-performance-review`. These are CLI chat commands, not shell commands. Cloud agents need the skill in their own repository or environment; a personal laptop folder is not transferred automatically. Other Copilot integrations need their own discovery check.

### Gemini CLI

After copying, run `/skills reload` and `/skills list` in chat. You can also run `gemini skills list --all` in a terminal. Built-in installation from Git or a local folder is available; this guide uses the individual ZIP method. If the skill is already in `.agents/skills`, do not duplicate it: that compatible path takes precedence within the same installation scope.

### Devin Desktop / Windsurf: Cascade

The official Windsurf documentation redirects to Devin Desktop. For **Cascade**, it retains the directories in the table. Open the Cascade customization menu, check Skills, and invoke `@api-performance-review` explicitly. Devin Local Agent uses a separate Devin CLI mechanism; the Cascade paths do not establish its installation procedure.

### Cline

Open the rules/settings menu beside the model selector and choose Skills. Check that the skill is found and enabled; discovered skills are enabled by default. Invoke `/api-performance-review` through chat suggestions. When personal and project copies share a name, Cline prioritizes the personal copy, so check for an older version there.

### OpenCode

Start a new session after copying. Ask to apply the skill by name and check the `skill` tool call for that name. OpenCode also reads `.agents/skills` and `.claude/skills`. If discovery fails, inspect existing permissions: `deny` hides a skill, and disabling the `skill` tool makes skills unavailable. Do not automatically change permissions to make this check pass.

### Amp

For installation on the current machine, use `~/.config/agents/skills`. Check with `amp skills list` in a terminal or ask Amp to reload skills. For a project, use `.agents/skills`. Personal or team Amp repositories are separate distribution destinations; this local copy does not upload files to them.

### Kiro

Copy the folder as shown in the table, or open `Agent Steering & Skills → + → Import a skill → Local folder` and choose the extracted folder of one skill. Check the list and invoke `/api-performance-review`. For a custom CLI agent, ensure its `resources` include the required `skill://` paths. Local IDE/CLI directories do not establish installation for Web/Mobile.

### Google Antigravity

Copy the folder into `~/.gemini/config/skills` or the project's `.agents/skills` and start a new conversation. Ask to use the skill by name; check that the agent reads that `SKILL.md` and required references. Do not substitute the Gemini CLI directory: these products have different personal paths. This is the editor procedure from its Skills page; check CLI-specific behavior separately.

### Kilo Code

Use `.kilo/skills` for the current platform. After copying, run `/reload` in chat or start a new session. Check the `skill` tool call. These instructions cover the current CLI/extension; older extension versions may have a different directory structure.

## Verify installation

A folder on disk is the first step. Check that the client discovers the name, then that a real task loads this `SKILL.md` and can open its included references. An agent saying “installed” without a discovery listing, loading record, or source inspection is not a complete check.

For a first trial, use `api-performance-review` and ask for a review of a small provided handler without editing code. Installing a skill does not grant missing repository, network, or tool access, or override the host's approval rules.

## Local Video Analysis requirements

Copy this skill in the same way. Running its Python code separately requires Python, FFmpeg/ffprobe, whisper.cpp, the pinned model, and yt-dlp for YouTube. Follow the [versioned setup guide](https://github.com/Karikatun/agent-skills/blob/local-video-analysis-v1.0.0/skills/local-video-analysis/references/setup.md). No dependency or model is installed by these instructions alone.

The current version was tested on macOS in an environment that permits native tools. Linux is unverified; native Windows is unsupported. A remote agent needs tools, the model, and media accessible **in that environment**. Support for reading `SKILL.md` alone does not prove video execution or extracted-frame inspection.

## Update or remove

Update only the selected skill after comparing its version, contents, and checksum; keep local edits outside scanned directories. To remove it, remove only that skill folder and start a new session. External tools, models, generated outputs, and prior project edits remain.

## Coverage

This is a practical set of 12 agent families with documented `SKILL.md` support, not a market-share ranking. Roo Code is excluded from the current list: its [official repository](https://github.com/RooCodeInc/Roo-Code) was archived on May 15, 2026 and announces the extension shutdown.

Web chat ZIP uploads, other IDE integrations, plugin catalogs, and format adapters are outside this guide. The collection provides individual folders and release archives; it has no universal installer. Documented paths and commands were checked; live discovery and execution in all 12 clients remain unverified.
