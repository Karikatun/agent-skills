#!/usr/bin/env python3
"""Prepare local transcript + sampled frames. No cloud inference or project writes."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import time
from urllib.parse import parse_qs, urlsplit


DATA_ROOT = Path.home() / ".local" / "share" / "local-video-analysis"
MODEL_NAME = "ggml-large-v3-turbo-q5_0.bin"
MODEL_SHA256 = "394221709cd5ad1f40c46e6031ca61bce88931e6e088c188294c6d5a55ffa7e2"
MODEL_BYTES = 574041195
MAX_DURATION = 7200
MAX_MEDIA_BYTES = 2 * 1024 ** 3
MAX_JSON_BYTES = 16 * 1024 ** 2
FORMATS = "mov,matroska,webm,avi,wav,mp3,ogg,flac,aac,mpeg,mpegts"
MEDIA_EXTENSIONS = {".mp4", ".mkv", ".webm", ".mov", ".m4v", ".avi", ".wav", ".mp3", ".m4a", ".flac", ".ogg", ".aac", ".mpeg", ".mpg", ".ts"}
SAFE_PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"


class VideoError(Exception):
    pass


def configured_path(name, default):
    value = os.environ.get(name)
    path = Path(value).expanduser() if value else default
    if value == "" or not path.is_absolute():
        raise VideoError(name + " must be an absolute path")
    return path


def tool_path():
    value = os.environ.get("LOCAL_VIDEO_TOOL_PATH")
    if value is None:
        return SAFE_PATH
    directories = value.split(os.pathsep)
    if any(not part or not Path(part).is_absolute() for part in directories):
        raise VideoError("LOCAL_VIDEO_TOOL_PATH must contain only absolute trusted directories")
    return os.pathsep.join(directories + [SAFE_PATH])


def now():
    return datetime.now(timezone.utc).isoformat()


def clean_text(text, limit=1000000):
    if not isinstance(text, str) or len(text) > limit:
        raise VideoError("Invalid or oversized text in media metadata")
    return "".join(c for c in text if c in "\n\t" or ord(c) >= 32).strip()


def youtube_url(source):
    try:
        u = urlsplit(source)
        if u.scheme != "https" or u.username or u.password or u.port not in (None, 443):
            raise ValueError()
        if u.hostname in ("youtube.com", "www.youtube.com", "m.youtube.com"):
            if u.path == "/watch":
                values = parse_qs(u.query).get("v", [])
                video_id = values[0] if len(values) == 1 else ""
            elif re.fullmatch(r"/(shorts|live)/[A-Za-z0-9_-]{11}", u.path):
                video_id = u.path.rsplit("/", 1)[1]
            else:
                raise ValueError()
        elif u.hostname == "youtu.be":
            video_id = u.path.lstrip("/")
        else:
            raise ValueError()
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            raise ValueError()
        return "https://www.youtube.com/watch?v=" + video_id
    except (ValueError, TypeError):
        raise VideoError("Provide one public HTTPS YouTube video URL; arbitrary hosts and credentials are not accepted") from None


def number(value):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
        raise VideoError("Invalid numeric value")
    return float(value)


def interval(start, end, duration):
    duration, start = number(duration), number(start)
    end = duration if end is None else number(end)
    if not 0 < duration <= MAX_DURATION or not 0 <= start < end <= duration + 0.05:
        raise VideoError("Invalid interval or media longer than the 2-hour processing limit")
    return start, min(end, duration)


def child_env():
    # Do not inherit keys, proxies, Python search paths, or project configuration.
    return {"HOME": str(Path.home()), "PATH": tool_path(), "LANG": "C", "LC_ALL": "C", "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1", "NO_COLOR": "1"}


def binary(name):
    search_path = tool_path().split(os.pathsep)
    # Explicit trusted directories take precedence over the optional local venv.
    explicit_count = len(os.environ.get("LOCAL_VIDEO_TOOL_PATH", "").split(os.pathsep)) if "LOCAL_VIDEO_TOOL_PATH" in os.environ else 0
    if name == "yt-dlp":
        isolated = DATA_ROOT / "venv" / "bin" / "yt-dlp"
        if isolated.is_file() and os.access(isolated, os.X_OK):
            search_path.insert(explicit_count, str(isolated.parent))
    for prefix in search_path:
        p = Path(prefix) / name
        if p.is_file() and os.access(p, os.X_OK):
            return str(p)
    raise VideoError("Missing required executable: " + name)


def run_tool(args, cwd, timeout=120, max_output=MAX_JSON_BYTES):
    """Capture output privately; never expose raw signed URLs or credential-bearing errors."""
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        process = subprocess.Popen(args, cwd=cwd, env=child_env(), stdin=subprocess.DEVNULL,
                                   stdout=stdout, stderr=stderr, start_new_session=True)
        deadline = time.monotonic() + timeout
        try:
            while process.poll() is None:
                if time.monotonic() > deadline:
                    raise VideoError(Path(args[0]).name + " timed out; no automatic retry")
                if os.fstat(stdout.fileno()).st_size + os.fstat(stderr.fileno()).st_size > max_output:
                    raise VideoError("Subprocess output limit exceeded")
                time.sleep(0.1)
        except BaseException:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            raise
        if process.returncode:
            stderr.seek(0)
            diagnostic = stderr.read(min(max_output, 1024 * 1024)).decode("utf-8", "replace")
            reason = ""
            for marker, label in [("HTTP Error 403", "provider refused media access (HTTP 403)"),
                                  ("HTTP Error 429", "provider rate limit (HTTP 429)"),
                                  ("Requested format is not available", "requested media format unavailable"),
                                  ("Sign in to confirm", "provider requires sign-in"),
                                  ("CERTIFICATE_VERIFY_FAILED", "TLS certificate verification failed"),
                                  ("Unknown input format", "unsupported local media container")]:
                if marker in diagnostic:
                    reason = ": " + label
                    break
            raise VideoError(Path(args[0]).name + " failed (exit " + str(process.returncode) + ")" + reason + "; raw diagnostics omitted")
        if os.fstat(stdout.fileno()).st_size + os.fstat(stderr.fileno()).st_size > max_output:
            raise VideoError("Subprocess output limit exceeded")
        stdout.seek(0)
        stderr.seek(0)
        return stdout.read(max_output + 1).decode("utf-8", "replace"), stderr.read(max_output + 1).decode("utf-8", "replace")


def ensure_private_dir(path):
    # Refuse symlinked output roots, including symlinked ancestors.
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise VideoError("Refusing a symlink in the output directory path")
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.stat().st_uid != os.getuid() or path.stat().st_mode & 0o077:
        raise VideoError("Output directory must be owned by this user with mode 700")


def create_run():
    ensure_private_dir(DATA_ROOT)
    ensure_private_dir(DATA_ROOT / "runs")
    return Path(tempfile.mkdtemp(prefix=datetime.now().strftime("%Y%m%d-%H%M%S-"), dir=DATA_ROOT / "runs"))


def write_new_json(path, data):
    with path.open("x", encoding="utf-8") as f:
        os.chmod(path, 0o600)
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write("\n")


def load_json(path):
    if path.is_symlink() or path.stat().st_size > MAX_JSON_BYTES:
        raise VideoError("Invalid or oversized JSON artifact")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError):
        raise VideoError("Invalid JSON artifact") from None


def write_state(run, state):
    # Only replaces the manifest belonging to this newly allocated run.
    tmp = run / "run.json.new"
    write_new_json(tmp, state)
    tmp.replace(run / "run.json")


def check_model():
    path = configured_path("LOCAL_VIDEO_MODEL", DATA_ROOT / "models" / MODEL_NAME)
    if not path.is_file() or path.is_symlink() or path.stat().st_size != MODEL_BYTES:
        raise VideoError("Verified Whisper model is missing; run doctor and inspect the installation")
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(4 * 1024 ** 2), b""):
            h.update(block)
    if h.hexdigest() != MODEL_SHA256:
        raise VideoError("Whisper model checksum mismatch; refusing to load it")
    return path


def yt_args():
    return [binary("yt-dlp"), "--ignore-config", "--no-plugin-dirs", "--no-cache-dir",
            "--no-playlist", "--no-progress", "--no-warnings", "--no-update",
            "--socket-timeout", "20", "--retries", "1", "--extractor-retries", "1",
            "--fragment-retries", "1", "--abort-on-error", "--no-overwrites",
            "--ffmpeg-location", str(Path(binary("ffmpeg")).parent)]


def youtube_info(url, run):
    text, _ = run_tool(yt_args() + ["--skip-download", "--dump-single-json", "--", url], run, timeout=150)
    try:
        info = json.loads(text)
        if not isinstance(info, dict) or info.get("id") != parse_qs(urlsplit(url).query)["v"][0]:
            raise ValueError()
        if info.get("is_live") or info.get("live_status") in ("is_live", "is_upcoming"):
            raise VideoError("Live and upcoming streams are not supported")
        interval(0, None, info.get("duration"))
        return info
    except (ValueError, TypeError):
        raise VideoError("Invalid video metadata") from None


def download_video(url, run):
    run_tool(yt_args() + ["--max-filesize", "1G", "--match-filter", "duration <= 7200 & !is_live",
                          "-f", "bv*[height<=720]+ba/b[height<=720]", "--merge-output-format", "mkv",
                          "-o", str(run / "media.%(ext)s"), "--", url], run, timeout=1200)
    files = [p for p in run.glob("media.*") if p.suffix.lower() in MEDIA_EXTENSIONS]
    if len(files) != 1:
        raise VideoError("Expected one downloaded media file; download may have been skipped")
    return validate_media_file(files[0])


def validate_media_file(path):
    path = path.expanduser().resolve(strict=True)
    if not path.is_file() or path.suffix.lower() not in MEDIA_EXTENSIONS:
        raise VideoError("Provide a regular audio/video file, not a playlist or arbitrary data file")
    if not 0 < path.stat().st_size <= MAX_MEDIA_BYTES:
        raise VideoError("Media file is empty or exceeds the 2 GiB limit")
    return path


def probe(media, run):
    text, _ = run_tool([binary("ffprobe"), "-v", "error", "-protocol_whitelist", "file,pipe",
                        "-format_whitelist", FORMATS, "-show_entries", "format=duration:stream=codec_type,width,height",
                        "-of", "json", str(media)], run, timeout=60)
    try:
        data = json.loads(text)
        duration = float(data["format"]["duration"])
        interval(0, None, duration)
        streams = data["streams"]
        for stream in streams:
            if stream.get("codec_type") == "video" and (stream.get("width", 0) > 8192 or stream.get("height", 0) > 8192):
                raise VideoError("Media resolution exceeds the 8K limit")
        return {"duration": duration, "audio": any(x.get("codec_type") == "audio" for x in streams),
                "video": any(x.get("codec_type") == "video" for x in streams)}
    except (ValueError, TypeError, KeyError):
        raise VideoError("Media has no valid finite duration/stream metadata") from None


def parse_json3(data, start, end):
    if not isinstance(data, dict) or not isinstance(data.get("events"), list) or len(data["events"]) > 100000:
        raise VideoError("Invalid subtitle event list")
    segments = []
    for event in data["events"]:
        if not isinstance(event, dict):
            raise VideoError("Invalid subtitle event")
        chunks = event.get("segs", [])
        if not isinstance(chunks, list) or len(chunks) > 10000:
            raise VideoError("Invalid subtitle segments")
        if any(not isinstance(s, dict) or not isinstance(s.get("utf8", ""), str) for s in chunks):
            raise VideoError("Invalid subtitle text")
        text = clean_text("".join(s.get("utf8", "") for s in chunks))
        if not text:
            continue
        a = number(event.get("tStartMs", 0)) / 1000
        b = a + number(event.get("dDurationMs", 0)) / 1000
        if a < 0 or b <= a:
            continue
        if b <= start or a >= end:
            continue
        a, b = max(start, a), min(end, b)
        if segments and segments[-1]["text"] == text and a <= segments[-1]["end"] + 0.2:
            segments[-1]["end"] = max(segments[-1]["end"], b)
        else:
            segments.append({"start": a, "end": b, "text": text})
    if not segments:
        raise VideoError("No subtitle text found in the requested interval")
    return segments


def captions(url, info, language, run, start, end):
    original = info.get("language", "")
    preferred = [language] if language != "auto" else ([original] if isinstance(original, str) and re.fullmatch(r"[a-z]{2,3}", original) else ["ru", "en"])
    for field, option, method in [("subtitles", "--write-subs", "youtube_manual"), ("automatic_captions", "--write-auto-subs", "youtube_automatic")]:
        available = info.get(field) or {}
        if not isinstance(available, dict):
            continue
        candidates = preferred + [x + "-orig" for x in preferred]
        for lang in candidates:
            if lang not in available:
                continue
            run_tool(yt_args() + ["--skip-download", option, "--sub-langs", lang, "--sub-format", "json3",
                                  "-o", str(run / "captions.%(ext)s"), "--", url], run, timeout=150)
            files = list(run.glob("captions.*.json3"))
            if len(files) != 1:
                raise VideoError("No usable JSON3 subtitles downloaded")
            return parse_json3(load_json(files[0]), start, end), method, lang
    raise VideoError("No matching subtitles available")


def ffmpeg_input(media, start):
    return [binary("ffmpeg"), "-nostdin", "-hide_banner", "-loglevel", "error", "-n",
            "-threads", "4", "-ss", str(start), "-protocol_whitelist", "file,pipe",
            "-format_whitelist", FORMATS, "-i", str(media)]


def parse_whisper(data, start, end):
    if not isinstance(data, dict) or not isinstance(data.get("transcription"), list) or len(data["transcription"]) > 100000:
        raise VideoError("Invalid Whisper transcription")
    segments = []
    try:
        for item in data["transcription"]:
            text = clean_text(item["text"])
            if not text:
                continue
            a = start + number(item["offsets"]["from"]) / 1000
            b = min(end, start + number(item["offsets"]["to"]) / 1000)
            if start <= a < b:
                segments.append({"start": a, "end": b, "text": text})
    except (KeyError, TypeError):
        raise VideoError("Invalid Whisper segment") from None
    if not segments:
        raise VideoError("Whisper produced no speech in this interval")
    return segments


def transcribe(media, run, start, end, language):
    model = check_model()
    wav = run / "audio.wav"
    run_tool(ffmpeg_input(media, start) + ["-t", str(end - start), "-vn", "-ac", "1", "-ar", "16000",
                                          "-c:a", "pcm_s16le", str(wav)], run, timeout=300)
    prefix = run / "whisper"
    run_tool([binary("whisper-cli"), "--model", str(model), "--file", str(wav), "--language", language,
              "--threads", "4", "--output-json", "--output-file", str(prefix), "--no-prints"],
             run, timeout=min(7200, max(300, (end - start) * 2)))
    data = load_json(prefix.with_suffix(".json"))
    return parse_whisper(data, start, end)


def scene_times(media, run, start, end):
    args = ffmpeg_input(media, start)
    args[args.index("error")] = "info"
    _, diagnostics = run_tool(args + ["-t", str(end - start), "-an", "-vf",
                                      "fps=2,scale=320:-2,select='gt(scene,0.3)',showinfo", "-f", "null", "-"],
                             run, timeout=max(120, (end - start) / 2), max_output=8 * 1024 ** 2)
    times = [start + float(value) for value in re.findall(r"pts_time:([0-9.]+)", diagnostics)]
    return [x for x in times if start <= x < end]


def evenly(items, limit):
    if len(items) <= limit:
        return list(items)
    if limit == 1:
        return [items[len(items) // 2]]
    return [items[round(i * (len(items) - 1) / (limit - 1))] for i in range(limit)]


def frame_times(start, end, scenes, every=30, limit=72):
    if not 1 <= every <= 600 or not 2 <= limit <= 120:
        raise VideoError("Frame interval must be 1–600 seconds; frame count must be 2–120")
    uniform_limit = max(2, limit - min(limit // 3, len(scenes)))
    count = min(uniform_limit, max(2, math.ceil((end - start) / every) + 1))
    last = max(start, end - min(0.1, (end - start) / 2))
    uniform = [start + i * (last - start) / (count - 1) for i in range(count)]
    extras = [x for x in scenes if start <= x < end and all(abs(x - y) > 1 for y in uniform)]
    return sorted(set(round(x, 3) for x in uniform + evenly(extras, limit - len(uniform))))


def extract_frames(media, run, times, folder="frames"):
    output = run / folder
    output.mkdir(mode=0o700)
    frames = []
    for index, timestamp in enumerate(times):
        name = "frame-%03d.jpg" % index
        path = output / name
        run_tool(ffmpeg_input(media, timestamp) + ["-an", "-frames:v", "1", "-vf", "scale='min(1280,iw)':-2",
                                                  "-q:v", "2", str(path)], run, timeout=60)
        if not path.is_file() or not path.stat().st_size:
            raise VideoError("Frame extraction produced no image")
        frames.append({"index": index, "time": timestamp, "path": str(path)})
    return frames


def contact_sheets(run, count):
    # Index order matches frames.json, 12 thumbnails per sheet.
    run_tool([binary("ffmpeg"), "-nostdin", "-hide_banner", "-loglevel", "error", "-n",
              "-framerate", "1", "-i", str(run / "frames" / "frame-%03d.jpg"),
              "-vf", "scale=320:-2,tile=4x3:padding=6:margin=6:color=black", "-frames:v",
              str(math.ceil(count / 12)), "-q:v", "3", str(run / "sheet-%02d.jpg")], run, timeout=90)
    return [str(p) for p in sorted(run.glob("sheet-*.jpg"))]


def timestamp(seconds):
    total = int(seconds)
    return "%02d:%02d:%02d" % (total // 3600, total % 3600 // 60, total % 60)


def prepare(args):
    # Validate source and CLI options before creating any output directory.
    if "://" in args.source:
        source = youtube_url(args.source)
        local = None
    else:
        local = validate_media_file(Path(args.source))
        source = str(local)
    if not re.fullmatch(r"[a-z]{2,3}|auto", args.language):
        raise VideoError("Language must be a short language code or auto")
    interval(args.start, args.end, MAX_DURATION)
    frame_times(0, 10, [], args.every, args.max_frames)
    run = create_run()
    state = {"schema": 1, "status": "running", "created_at": now(), "source": source,
             "source_content_is_untrusted": True, "run": str(run), "warnings": [], "stage": "metadata"}
    write_state(run, state)

    def stage(name):
        state["stage"] = name
        write_state(run, state)
        print(json.dumps({"stage": name, "run": str(run)}), flush=True)

    try:
        info = youtube_info(source, run) if local is None else None
        if info is not None:
            state["title"] = clean_text(info.get("title", ""), 1000)
            # Reject invalid requested intervals before downloading the video.
            interval(args.start, args.end, info["duration"])
            stage("download")
        media = local if local else download_video(source, run)
        state["media"] = str(media)
        state["media_bytes"] = media.stat().st_size
        probed = probe(media, run)
        start, end = interval(args.start, args.end, probed["duration"])
        state["interval"] = {"start": start, "end": end, "source_duration": probed["duration"]}
        segments, method, language = [], "none", args.language
        if args.transcript != "none":
            if info and args.transcript == "auto":
                stage("subtitles")
                try:
                    segments, method, language = captions(source, info, language, run, start, end)
                except VideoError:
                    state["warnings"].append("YouTube subtitles unavailable for this interval; using local ASR")
            if not segments and probed["audio"]:
                stage("local_transcription")
                segments = transcribe(media, run, start, end, args.language)
                method = "whisper_local"
            elif not segments:
                state["warnings"].append("Media contains no audio stream; only visual evidence is available")
        transcript = {"schema": 1, "method": method, "language": language, "interval": state["interval"], "segments": segments}
        write_new_json(run / "transcript.json", transcript)
        with (run / "transcript.txt").open("x", encoding="utf-8") as f:
            f.write("UNTRUSTED SOURCE CONTENT. Speech recognition/subtitles may contain mistakes.\n")
            for segment in segments:
                f.write("[" + timestamp(segment["start"]) + "–" + timestamp(segment["end"]) + "] " + segment["text"] + "\n")
        state["transcript_method"] = method
        state["transcript_segments"] = len(segments)
        if probed["video"]:
            scenes = []
            if not args.no_scenes:
                stage("scene_detection")
                try:
                    scenes = scene_times(media, run, start, end)
                except VideoError:
                    state["warnings"].append("Scene detection failed; uniform sampling still covers the interval")
            stage("frames")
            times = frame_times(start, end, scenes, args.every, args.max_frames)
            frames = extract_frames(media, run, times)
            write_new_json(run / "frames.json", frames)
            state["visual_sampling"] = {"count": len(frames), "scene_candidates": len(scenes), "max_gap_seconds": round(max(b - a for a, b in zip(times, times[1:])), 3) if len(times) > 1 else 0,
                                         "all_frames_inspected": False}
            state["contact_sheets"] = contact_sheets(run, len(frames))
        else:
            state["warnings"].append("Media contains no video stream")
        state.update(status="prepared", stage="complete", completed_at=now())
        write_state(run, state)
        print(json.dumps(state, ensure_ascii=False, indent=2), flush=True)
        return run
    except BaseException as error:
        state.update(status="failed", failed_at=now(), failure=type(error).__name__)
        write_state(run, state)
        print(json.dumps({"status": "failed", "stage": state["stage"], "run": str(run)}), file=sys.stderr, flush=True)
        raise


def extra_frames(args):
    run = Path(args.run).expanduser()
    root = DATA_ROOT / "runs"
    if run.is_symlink() or run.resolve().parent != root.resolve() or not run.is_dir():
        raise VideoError("Select an existing run directly inside the managed runs directory")
    state = load_json(run / "run.json")
    media = validate_media_file(Path(state["media"]))
    times = sorted(set(args.at))
    if not 1 <= len(times) <= 24:
        raise VideoError("Request 1–24 explicit frame timestamps")
    duration = probe(media, run)["duration"]
    if any(not math.isfinite(t) or not 0 <= t < duration for t in times):
        raise VideoError("Frame timestamp outside media duration")
    folder = "detail-" + str(time.time_ns())
    result = extract_frames(media, run, times, folder)
    write_new_json(run / folder / "frames.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def doctor(args):
    versions = {}
    for name, flag in (("yt-dlp", "--version"), ("ffmpeg", "-version"), ("ffprobe", "-version"), ("whisper-cli", "--version")):
        try:
            path = binary(name)
            out, err = run_tool([path, flag], Path.home(), timeout=30)
            versions[name] = {"path": path, "version": (out or err).strip().splitlines()[0]}
        except VideoError as e:
            versions[name] = {"error": str(e)}
    try:
        model = {"path": str(check_model()), "sha256": MODEL_SHA256, "verified": True}
    except VideoError as e:
        model = {"verified": False, "error": str(e)}
    result = {"tools": versions, "model": model, "data_root": str(DATA_ROOT)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not model["verified"] or any("error" in x for x in versions.values()):
        raise VideoError("Local video installation is incomplete")


def main():
    global DATA_ROOT
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    d = commands.add_parser("doctor", help="Check dependencies and model checksum")
    d.set_defaults(func=doctor)
    p = commands.add_parser("prepare", help="Prepare a YouTube video or local media file outside the project")
    p.add_argument("source")
    p.add_argument("--start", type=float, default=0)
    p.add_argument("--end", type=float)
    p.add_argument("--language", default="auto")
    p.add_argument("--transcript", choices=("auto", "asr", "none"), default="auto")
    p.add_argument("--every", type=float, default=30)
    p.add_argument("--max-frames", type=int, default=72)
    p.add_argument("--no-scenes", action="store_true")
    p.set_defaults(func=prepare)
    f = commands.add_parser("frames", help="Extract additional frames at absolute video timestamps")
    f.add_argument("run")
    f.add_argument("--at", nargs="+", type=float, required=True)
    f.set_defaults(func=extra_frames)
    args = parser.parse_args()
    try:
        if os.name != "posix":
            raise VideoError("This helper requires a POSIX host; native Windows is not supported")
        DATA_ROOT = configured_path("LOCAL_VIDEO_DATA_DIR", DATA_ROOT)
        tool_path()
        args.func(args)
    except (VideoError, OSError, ValueError, KeyError, TypeError) as e:
        # OSError text can include private paths; only domain errors are printable.
        print(str(e) if isinstance(e, VideoError) else "Local processing failed: " + type(e).__name__, file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Interrupted; owned run artifacts retained for inspection", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
