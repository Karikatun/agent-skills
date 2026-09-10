# Humanize Dev Post

Version 1.0.0. Rewrite a development draft as a readable account for the intended audience, particularly a Russian developer journal or Telegram post. Preserve the facts and the author's supplied voice without inventing experiences.

```text
Use $humanize-dev-post to rewrite these notes for non-specialist readers in Russian. Preserve the factual corrections and return only the post, without a code block or promotional ending.
```

Unlike an editorial audit, this workflow produces the requested narrative. Unlike general microcopy editing, it pays particular attention to the episode, technical explanation, chronology, and attribution. It does not require either `devlog-editor` or `humanize-russian-text` to be installed.

The public package generalizes an existing private workflow. It removes the fixed product CTA, required code block, compulsory humour, and blanket shortening target. Original examples and private drafts are not included. Instructions are English; output follows the user's requested language.

Copy the whole folder into a supported skill directory. Compare an existing copy before replacing it. No executable scripts, runtime dependencies, external services, or automatic updates are included.

## Install with Codex

```text
Use $skill-installer to install only humanize-dev-post from https://github.com/Karikatun/agent-skills/tree/humanize-dev-post-v1.0.0/skills/humanize-dev-post into my personal skills directory. Preserve any existing copy; do not install other skills.
```

See the [validation record](https://github.com/Karikatun/agent-skills/blob/humanize-dev-post-v1.0.0/evaluations/humanize-dev-post/VALIDATION.md) for factual-preservation and format cases. Editorial preference and audience engagement were not measured. Original material uses the adjacent [MIT license](LICENSE).
