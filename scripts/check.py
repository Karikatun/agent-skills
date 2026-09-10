#!/usr/bin/env python3
"""Bounded package checks plus synthetic fixture tests; Python 3.9+ stdlib only."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".scratch", ".venv", "dist", "__pycache__"}


def check_skill(directory):
    """Check the metadata subset this collection uses, not arbitrary YAML."""
    entry = directory / "SKILL.md"
    text = entry.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    assert len(parts) == 3 and not parts[0].strip(), f"Missing frontmatter: {entry}"
    frontmatter = parts[1]
    name = re.search(r"^name: ([a-z0-9]+(?:-[a-z0-9]+)*)$", frontmatter, re.M)
    assert name and name.group(1) == directory.name, f"Invalid skill name: {entry}"
    assert re.search(r"^description: \S.+$", frontmatter, re.M), f"Missing description: {entry}"
    assert re.search(r'^  version: "\d+\.\d+\.\d+"$', frontmatter, re.M), f"Missing version: {entry}"
    assert (directory / "LICENSE").is_file(), f"Missing license: {directory}"
    assert (directory / "README.md").is_file(), f"Missing usage guide: {directory}"
    for file in directory.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
            if re.match(r"https?://", target) or target.startswith("#"):
                continue
            destination = (file.parent / target.split("#", 1)[0]).resolve()
            assert directory.resolve() in destination.parents, f"Reference leaves skill: {file.name} -> {target}"
            assert destination.is_file(), f"Missing local reference: {target}"


def main():
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    assert skills, "No skills found"
    for directory in skills:
        check_skill(directory)

    private_path = re.compile(r"/(?:Users|home)/[^/\s]+|[A-Z]:\\Users\\", re.I)
    token_prefix = re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{32,})")
    checked = 0
    for file in ROOT.rglob("*"):
        relative = file.relative_to(ROOT)
        if any(part in IGNORED for part in relative.parts):
            continue
        assert not file.is_symlink(), f"Symlink in package: {relative}"
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8")
        assert not private_path.search(text), f"Personal path in {relative}"
        assert not token_prefix.search(text), f"Credential-shaped text in {relative}"
        assert not re.search(r"-----BEGIN [A-Z ]*PRIVATE" + r" KEY-----", text), f"Private key in {relative}"
        assert not any(ord(char) < 32 and char not in "\n\r\t" for char in text), f"Control character in {relative}"
        assert not any(char in text for char in "\u200b\u200c\u200d\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069\ufeff"), f"Invisible or bidi control in {relative}"
        if file.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if re.match(r"https?://", target) or target.startswith("#"):
                    continue
                destination = (file.parent / target.split("#", 1)[0]).resolve()
                assert ROOT in destination.parents and destination.exists(), f"Broken repository link: {relative} -> {target}"
        checked += 1

    print(f"PASS: {len(skills)} skill packages, {checked} text files; local references and bounded content checks", flush=True)
    for test_file in (
        "evaluations/api-performance-review/test_fixtures.py",
        "skills/local-video-analysis/scripts/test_video.py",
    ):
        subprocess.run(
            [sys.executable, "-B", str(ROOT / test_file)],
            check=True, cwd=ROOT, timeout=60,
        )
    print("These checks do not establish agent quality, host isolation, or exhaustive secret detection.")


if __name__ == "__main__":
    main()
