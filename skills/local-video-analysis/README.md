# Local Video Analysis

Version 1.0.0. Prepare a local transcript and timestamped frame evidence, then let the agent inspect them and answer the requested video question. Local Whisper performs recognition; it does not send audio to a cloud transcription API. Transcript excerpts and images the agent inspects become chat context.

```text
Use $local-video-analysis to analyze this public YouTube video. Read the transcript, inspect its slides, and cite timestamps. State any sampling gaps.
```

```text
Use $local-video-analysis on this local file, only from 20:00 to 21:10. Cross-check technical terms against the frames.
```

This skill includes executable Python helpers. Copy the complete folder into a supported skills directory, inspect the scripts, and follow [Setup](references/setup.md). Python, yt-dlp, FFmpeg, whisper.cpp and the fixed model are separate dependencies; they are not bundled or automatically installed. No companion skill, API key or account is required. Replies follow the user's language.

The public package replaces the original private host paths with configurable absolute data, model and trusted-tool paths. macOS runtime behavior has been checked. Linux is not runtime-verified; native Windows is unsupported. A request forbidding all processing files is incompatible with this helper and must be respected.

## Install with Codex

```text
Use $skill-installer to install only local-video-analysis from https://github.com/Karikatun/agent-skills/tree/local-video-analysis-v1.0.0/skills/local-video-analysis into my personal skills directory. Preserve any existing copy; do not install other skills or runtime dependencies.
```

This installs the skill folder only. Review and authorize dependency setup separately if the tools are absent. The [validation record](https://github.com/Karikatun/agent-skills/blob/local-video-analysis-v1.0.0/evaluations/local-video-analysis/VALIDATION.md) distinguishes parser tests, real media processing and unverified environments. Original helper code and instructions use the adjacent [MIT license](LICENSE). External tools, model and analyzed media retain their own licenses.
