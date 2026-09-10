import importlib.util
import json
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("video", Path(__file__).with_name("video.py"))
video = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(video)


class InputTests(unittest.TestCase):
    def test_default_data_directory_is_host_independent(self):
        self.assertEqual(video.DATA_ROOT, Path.home() / ".local" / "share" / "local-video-analysis")

    def test_configured_paths_require_absolute_explicit_locations(self):
        with patch.dict("os.environ", {"LOCAL_VIDEO_DATA_DIR": "relative/state"}):
            with self.assertRaises(video.VideoError):
                video.configured_path("LOCAL_VIDEO_DATA_DIR", Path("/default"))
        with patch.dict("os.environ", {"LOCAL_VIDEO_DATA_DIR": "/chosen/private-state"}):
            self.assertEqual(video.configured_path("LOCAL_VIDEO_DATA_DIR", Path("/default")), Path("/chosen/private-state"))

    def test_explicit_tool_directory_does_not_import_ambient_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp).resolve()
            tool = folder / "ffmpeg"
            tool.write_text("synthetic executable placeholder")
            tool.chmod(0o700)
            with patch.dict("os.environ", {"LOCAL_VIDEO_TOOL_PATH": str(folder), "PATH": "/untrusted"}):
                self.assertEqual(video.binary("ffmpeg"), str(tool))
                self.assertNotIn("/untrusted", video.child_env()["PATH"])
                self.assertIn(str(folder), video.child_env()["PATH"])
        for value in ["relative/bin", ":/usr/bin", "/usr/bin:"]:
            with patch.dict("os.environ", {"LOCAL_VIDEO_TOOL_PATH": value}), self.assertRaises(video.VideoError):
                video.binary("ffmpeg")

    def test_explicit_model_still_requires_size_hash_and_regular_file(self):
        import hashlib
        with tempfile.TemporaryDirectory() as tmp:
            model = Path(tmp).resolve() / "model.bin"
            model.write_bytes(b"synthetic model")
            with patch.dict("os.environ", {"LOCAL_VIDEO_MODEL": str(model)}), patch.object(video, "MODEL_BYTES", 15), patch.object(video, "MODEL_SHA256", hashlib.sha256(b"synthetic model").hexdigest()):
                self.assertEqual(video.check_model(), model)
                model.write_bytes(b"tampered model!")
                with self.assertRaises(video.VideoError):
                    video.check_model()
                model.unlink()
                model.symlink_to(Path(tmp) / "missing")
                with self.assertRaises(video.VideoError):
                    video.check_model()

    def test_youtube_canonicalization_drops_tracking_and_seek(self):
        expected = "https://www.youtube.com/watch?v=azdEfAO6PXc"
        for source in [expected + "&t=1225s&list=PL123", "https://youtu.be/azdEfAO6PXc?t=5", "https://m.youtube.com/watch?v=azdEfAO6PXc"]:
            self.assertEqual(video.youtube_url(source), expected)

    def test_external_hosts_credentials_and_injection_rejected(self):
        for source in ["https://youtube.com.evil.test/watch?v=azdEfAO6PXc", "https://youtube.com@evil.test/watch?v=azdEfAO6PXc", "https://user:secret@youtube.com/watch?v=azdEfAO6PXc", "http://127.0.0.1", "file:///etc/passwd", "--exec=touch /tmp/owned", "https://youtube.com/watch?v=x;touch /tmp/owned", "https://youtube.com:8443/watch?v=azdEfAO6PXc"]:
            with self.subTest(source=source), self.assertRaises(video.VideoError):
                video.youtube_url(source)

    def test_interval_validation(self):
        self.assertEqual(video.interval(1200, 1245, 1946), (1200, 1245))
        for start, end, duration in [(10, 5, 100), (-1, 20, 100), (0, float("nan"), 100), (0, 110, 100), (0, None, 9000)]:
            with self.assertRaises(video.VideoError):
                video.interval(start, end, duration)

    def test_child_environment_does_not_pass_credentials_or_project_path(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": "secret", "AWS_SECRET_ACCESS_KEY": "secret", "PYTHONPATH": "/untrusted", "PATH": "/untrusted/bin", "HTTP_PROXY": "http://secret"}):
            env = video.child_env()
        for name in ("OPENAI_API_KEY", "AWS_SECRET_ACCESS_KEY", "PYTHONPATH", "HTTP_PROXY"):
            self.assertNotIn(name, env)
        self.assertNotIn("/untrusted", env["PATH"])

    def test_provider_errors_are_classified_without_leaking_urls(self):
        command = [sys.executable, "-c", "import sys; print('HTTP Error 403 https://cdn.example/video?token=private', file=sys.stderr); sys.exit(1)"]
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(video.VideoError) as raised:
            video.run_tool(command, Path(tmp))
        self.assertIn("HTTP 403", str(raised.exception))
        self.assertNotIn("private", str(raised.exception))
        self.assertNotIn("cdn.example", str(raised.exception))

    def test_subprocess_receives_no_ambient_credentials(self):
        command = [sys.executable, "-c", "import os,json; print(json.dumps(sorted(os.environ)))"]
        with tempfile.TemporaryDirectory() as tmp, patch.dict("os.environ", {"PRIVATE_SENTINEL": "not-for-child"}):
            output, _ = video.run_tool(command, Path(tmp))
        self.assertNotIn("PRIVATE_SENTINEL", json.loads(output))

    def test_subprocess_timeout_stops_owned_process(self):
        import os
        with tempfile.TemporaryDirectory() as tmp:
            pid = Path(tmp) / "pid"
            command = [sys.executable, "-c", "import os,pathlib,time; pathlib.Path('pid').write_text(str(os.getpid())); time.sleep(5)"]
            with self.assertRaisesRegex(video.VideoError, "timed out"):
                video.run_tool(command, Path(tmp), timeout=0.5)
            self.assertTrue(pid.is_file())
            with self.assertRaises(ProcessLookupError):
                os.kill(int(pid.read_text()), 0)

    def test_subprocess_output_limit_is_not_success(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaisesRegex(video.VideoError, "output limit"):
            video.run_tool([sys.executable, "-c", "print('x' * 2000)"], Path(tmp), max_output=100)

    def test_invalid_url_does_not_create_artifacts(self):
        from argparse import Namespace
        with tempfile.TemporaryDirectory() as tmp, patch.object(video, "DATA_ROOT", Path(tmp).resolve() / "state"):
            with self.assertRaises(video.VideoError):
                video.prepare(Namespace(source="https://127.0.0.1/private", language="auto", start=0, end=None, every=30, max_frames=72))
            self.assertFalse(video.DATA_ROOT.exists())


class TranscriptTests(unittest.TestCase):
    def test_json3_rollup_duplicates_and_timing(self):
        data = {"events": [
            {"tStartMs": 1000, "dDurationMs": 1000, "segs": [{"utf8": "Hello "}, {"utf8": "world"}]},
            {"tStartMs": 2000, "dDurationMs": 1000, "segs": [{"utf8": "Hello world"}]},
            {"tStartMs": 3000, "dDurationMs": 1000, "segs": [{"utf8": "Next."}]},
            {"tStartMs": 3500, "dDurationMs": 10, "segs": [{"utf8": "\n"}]},
        ]}
        result = video.parse_json3(data, 0, 10)
        self.assertEqual([s["text"] for s in result], ["Hello world", "Next."])
        self.assertEqual(result[0]["end"], 3.0)

    def test_clipped_captions_keep_absolute_video_timestamps(self):
        data = {"events": [{"tStartMs": 1200000, "dDurationMs": 3000, "segs": [{"utf8": "Cache"}]}]}
        self.assertEqual(video.parse_json3(data, 1201, 1202), [{"start": 1201, "end": 1202, "text": "Cache"}])

    def test_whisper_clip_offsets_and_empty_text(self):
        data = {"transcription": [{"offsets": {"from": 500, "to": 2500}, "text": " Кэш "}, {"offsets": {"from": 2500, "to": 3000}, "text": " "}]}
        self.assertEqual(video.parse_whisper(data, 1200, 1245), [{"start": 1200.5, "end": 1202.5, "text": "Кэш"}])

    def test_invalid_provider_payload_does_not_claim_success(self):
        with self.assertRaises(video.VideoError):
            video.parse_json3({"events": "wrong"}, 0, 10)
        with self.assertRaises(video.VideoError):
            video.parse_whisper({"transcription": []}, 0, 10)


class ArtifactTests(unittest.TestCase):
    def test_sampling_covers_entire_clip_and_bounds_count(self):
        result = video.frame_times(100, 2000, [120, 121, 900, 1700], every=30, limit=12)
        self.assertLessEqual(len(result), 12)
        self.assertEqual(result[0], 100)
        self.assertGreater(result[-1], 1998)
        self.assertTrue(all(100 <= t < 2000 for t in result))
        self.assertGreater(len([t for t in result if t > 1000]), 2)

    def test_outputs_are_private_unique_and_outside_working_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(video, "DATA_ROOT", Path(tmp).resolve() / "state"):
                a, b = video.create_run(), video.create_run()
            self.assertNotEqual(a, b)
            self.assertEqual(a.stat().st_mode & 0o777, 0o700)
            self.assertTrue(a.is_relative_to(Path(tmp).resolve() / "state"))

    def test_symlink_output_root_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            (root / "other").mkdir()
            (root / "state").symlink_to(root / "other", target_is_directory=True)
            with patch.object(video, "DATA_ROOT", root / "state"), self.assertRaises(video.VideoError):
                video.create_run()

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "transcript.json"
            video.write_new_json(p, {"original": True})
            with self.assertRaises(FileExistsError):
                video.write_new_json(p, {"replacement": True})
            self.assertEqual(json.loads(p.read_text()), {"original": True})


if __name__ == "__main__":
    unittest.main()
