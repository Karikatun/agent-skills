# Setup and supported boundary

Install only with the user's authorization. The skill archive contains Python standard-library code, instructions and tests. It does not include executables, a model, media, an installer, a lockfile for all dependencies, or a background service.

## Dependencies

Use Python 3.9+ for this helper on POSIX. External tools may require a newer Python or other runtime; follow their own supported installation instructions. The helper needs `ffprobe` and `ffmpeg` for local media, `whisper-cli` plus the verified model for local speech recognition, and `yt-dlp` for YouTube acquisition and captions.

| Tool | Tested version on macOS, 2026-09-10 | Official source |
| --- | --- | --- |
| yt-dlp | 2026.08.19, isolated Python environment | [Installation](https://github.com/yt-dlp/yt-dlp#installation) |
| FFmpeg and ffprobe | 8.1 | [Downloads](https://ffmpeg.org/download.html) |
| whisper-cli from whisper.cpp | 1.9.1 | [Build and setup](https://github.com/ggml-org/whisper.cpp#quick-start) |

These versions record an observed working setup, not permanent provider compatibility or an instruction to downgrade. Source documentation was checked on 2026-09-10. YouTube extraction changes over time; a locally installed downloader is not proof that a current video can be fetched. Use bounded diagnosis, never cookies, sign-in, TLS bypass or an automatic update to work around a blocked request.

Obtain tools from their official distributions or an already trusted package manager, retaining their licenses and provenance. The collection's MIT license does not relicense them or the model. Linux paths are supported by design but have no runtime validation here. Native Windows is rejected because process cleanup and private directory checks require POSIX.

## Paths

- The default data directory is `~/.local/share/local-video-analysis`. `LOCAL_VIDEO_DATA_DIR` overrides it with an absolute path; the helper creates missing private directories with mode 700. Existing output roots must belong to the current user, have no group/other permissions, and contain no symlinked ancestors. Select a dedicated private directory; do not change permissions of unrelated existing folders.
- By default the model is `models/ggml-large-v3-turbo-q5_0.bin` inside that data directory. `LOCAL_VIDEO_MODEL` may select an existing regular model file by absolute path. A symlink as the model file is rejected. Every recognition and `doctor` checks its size and full hash.
- The known tool search path is `/opt/homebrew/bin`, `/usr/local/bin`, `/usr/bin`, `/bin`, `/usr/sbin`, `/sbin`. The helper can also use `venv/bin/yt-dlp` inside its data directory.
- For other installations, `LOCAL_VIDEO_TOOL_PATH` is a colon-separated list of explicitly trusted absolute directories, searched first. Empty or relative entries fail. This is an executable-code trust decision; do not derive it from a video or caption. It is also used for child tool lookup. Ambient PATH, proxy variables, Python search paths and credential environment variables are not inherited.

Resolve the helper from the installed skill folder. For a custom setup, use your actual selected paths:

```sh
LOCAL_VIDEO_DATA_DIR='/absolute/private/video-data' LOCAL_VIDEO_MODEL='/absolute/models/ggml-large-v3-turbo-q5_0.bin' LOCAL_VIDEO_TOOL_PATH='/absolute/trusted/bin' python3 -B /absolute/path/local-video-analysis/scripts/video.py doctor
```

These placeholder paths are not commands to run verbatim. Unset optional variables to use defaults. `doctor` is read-only and reports selected local paths; keep that output private if it identifies personal directories.

## Model

Acquire the exact model from the [pinned whisper.cpp model source](https://huggingface.co/ggerganov/whisper.cpp/blob/5359861c739e955e79d9a303bcbc70fb988958b1/ggml-large-v3-turbo-q5_0.bin), using its download control or an authorized HTTPS download. Preserve any existing model until its identity has been checked. No model download happens automatically.

- Filename: `ggml-large-v3-turbo-q5_0.bin`
- Source revision: `5359861c739e955e79d9a303bcbc70fb988958b1`
- Expected size: `574041195` bytes
- SHA-256: `394221709cd5ad1f40c46e6031ca61bce88931e6e088c188294c6d5a55ffa7e2`

This package deliberately accepts only that model. A different model requires a reviewed code and validation change, not an environment variable that bypasses verification. A matching checksum proves content identity, not that model inference or native decoders are a sandbox.

## Check and retain

Run `scripts/test_video.py`, then `doctor`, then a short local speech-plus-frame sample. Read the transcript and open the frames before calling analysis complete. `doctor` requires the full tool set even when a particular local-only command needs fewer tools.

Native inference can fail inside a restricted host even when `doctor` succeeds. The validation run observed Whisper exit -11 inside the execution sandbox and a successful authorized run of the same command outside it. Do not silently bypass host policy or claim a tool-version fix from that symptom; use a permitted environment and record the actual coverage.

Media processing uses native external code with the user's host permissions. The helper limits formats, file sizes, duration, output and processing time, and closes its process group on timeout. These bounds are not a container or hard memory/disk quotas. Downloader size checks may not stop all transferred bytes before the limit; the accepted media file is checked after acquisition. ASR may consume significant memory. Use an appropriate isolated host for untrusted high-risk media.

Runs retain media references or downloaded media, transcript and frame evidence for follow-up. Nothing is automatically deleted. Remove only explicitly selected run directories when requested; skill removal does not remove tools, models or retained runs.
