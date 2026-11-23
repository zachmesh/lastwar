#!/usr/bin/env python3
"""run_notes_move: mark, then move the run articles that duplicate a dated record into `_run_notes_/<activity>/` (OD-20261123-14).

Input: the coach's audit CSV (path, activity, words, mapped_record_path, shared_number_share, class, reason). Scope: class a only.
Commands (nothing is written except by `apply`):

  plan   [--activities a,b] [--reviewed a,b | --reviewed-file F] [--sample N]   dry run: counts per activity, a sample diff
  apply  --activities a,b,c --reviewed a,b,c                                     one block: mark, git mv, catalogs, references
  verify [--base REV]                                                            prove every row of moved-paths.csv

`apply`, per activity and resumable (a second run finds it done and changes nothing):
  1. marks each file: `status: superseded`, `superseded_by` the mapped record path, `version` up one minor, `modified` now, one
     changelog line appended; every other frontmatter line and the whole original body stay byte-for-byte;
  2. `git mv` to `_run_notes_/<activity>/<same name>`;
  3. writes the folder INDEX.md (300 words or fewer) and catalog pages under the word budget (one first sentence per file);
  4. rewrites the markdown links to moved files inside `_activities_` to the new paths (version and modified of the edited
     page move; a changelog line goes in when the page has a Changelog section);
  5. appends `_run_notes_/moved-paths/moved-paths.csv` (old path, new path, record), in an instance folder because the gate
     blocks a loose file in a type folder, and lists the folder in the type INDEX;
  6. proves each moved file equals its original apart from the marked frontmatter and the changelog line.
It REFUSES a file whose class is not a, whose record path is not a file, whose activity has no reviewed digest (`--reviewed`),
that is not directly in `_activities_/<activity>/`, whose source is gone or target differs, that lacks version or modified, or
that would reach 500 body words with the changelog line. It never writes outside `_activities_/` and `_run_notes_/`: a record is
never edited. `apply` takes at most --block-limit (3) activities. Output is counts. Exit 0 ok, 1 refusals or a failed proof,
2 cannot run.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, OrderedDict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TYPE_DIR, MAP_DIR = "_run_notes_", "moved-paths"
MAP_REL = f"{TYPE_DIR}/{MAP_DIR}/moved-paths.csv"
MARKED = ("status", "superseded_by", "version", "modified")
CATALOG_WORDS, INDEX_WORDS, HARD_WORDS = 300, 300, 500
AUDIT_FIELDS = ("path", "activity", "words", "mapped_record_path", "shared_number_share", "class", "reason")
LINK = re.compile(r"\]\(([^)\s#]+\.md)(#[^)\s]*)?\)")


class Refusal(Exception):
    def __init__(self, code, detail=""):
        super().__init__(code)
        self.code, self.detail = code, detail


# --- words ---------------------------------------------------------------------------------------------------------

_COUNTER = []


def body_words(text: str) -> int:
    """Body words as the word-budget checker counts them (the whitespace count after the frontmatter without it)."""
    if not _COUNTER:
        path = Path(os.environ.get("RUN_NOTES_WORD_COUNTER") or "~/dtadpole/reflection/_tools_/document-word-budget/word-budget.py").expanduser()
        try:
            spec = importlib.util.spec_from_file_location("run_notes_word_budget", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            _COUNTER.append(module.check_text)
        except Exception:
            _COUNTER.append(None)
    if _COUNTER[0] is not None:
        try:
            return int(_COUNTER[0](text, "x.md")["body_words"])
        except Exception:
            pass
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    return len(body.split())


# --- frontmatter ---------------------------------------------------------------------------------------------------

def split_front(text: str):
    """(front_lines, head, body): the lines between the --- fences, the text up to and including the closing fence line, and
    everything after it, so head + body is the file byte for byte. (None, None, None) without a frontmatter block."""
    if not text.startswith("---\n"):
        return None, None, None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None, None, None
    head_end = end + len("\n---\n")
    return text[4:end].split("\n"), text[:head_end], text[head_end:]


def key_of(line: str):
    m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s(.*))?$", line)
    return (m.group(1), (m.group(2) or "").strip()) if m else (None, None)


def bump_minor(version: str) -> str:
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", version.strip())
    if not m:
        raise Refusal("frontmatter-incomplete", f"version {version!r} is not X.Y.Z")
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0"


def changelog_line(version: str, day: str, record: str, activity: str) -> str:
    return f"- {version}, {day} - Marked superseded by {record} and moved to {TYPE_DIR}/{activity}/ ({day})."


def is_marked(front_lines, record: str) -> bool:
    keys = dict(kv for kv in (key_of(l) for l in front_lines) if kv[0])
    return keys.get("status") == "superseded" and keys.get("superseded_by") == record


def mark_text(text: str, record: str, activity: str, now: datetime) -> str:
    """The marked version of a run article: status and superseded_by set, version up one minor, modified now, the original body
    untouched with one changelog line appended. Refuses when the frontmatter lacks version or modified."""
    front, head, body = split_front(text)
    if front is None:
        raise Refusal("no-frontmatter")
    keys = [key_of(l)[0] for l in front]
    if "version" not in keys or "modified" not in keys:
        raise Refusal("frontmatter-incomplete", "version or modified missing")
    day, stamp = now.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%dT%H:%M:%SZ")
    version = bump_minor(dict(kv for kv in (key_of(l) for l in front) if kv[0])["version"])
    out, seen = [], set()
    for line in front:
        k, _v = key_of(line)
        if k == "version":
            line = f"version: {version}"
        elif k == "modified":
            line = f"modified: {stamp}"
        elif k == "status":
            line = "status: superseded"
        elif k == "superseded_by":
            line = f"superseded_by: {record}"
        if k:
            seen.add(k)
        out.append(line)
    if "status" not in seen:
        out.append("status: superseded")
    if "superseded_by" not in seen:
        out.append(f"superseded_by: {record}")
    new_head = "---\n" + "\n".join(out) + "\n---\n"
    tail = ("" if body.endswith("\n") else "\n") + f"\n## Changelog\n\n{changelog_line(version, day, record, activity)}\n"
    return new_head + body + tail


def verify_pair(old: str, new: str, record: str, activity: str) -> list[str]:
    """Problems proving `new` is `old` apart from the marked frontmatter: other frontmatter lines identical and in order, the
    original body a byte-exact prefix of the new body, and the rest exactly one changelog block."""
    problems = []
    f_old, _h_old, b_old = split_front(old)
    f_new, _h_new, b_new = split_front(new)
    if f_old is None or f_new is None:
        return ["frontmatter missing"]
    keep_old = [l for l in f_old if key_of(l)[0] not in MARKED]
    keep_new = [l for l in f_new if key_of(l)[0] not in MARKED]
    if keep_old != keep_new:
        problems.append("a frontmatter line other than the marked ones changed")
    new_keys = dict(kv for kv in (key_of(l) for l in f_new) if kv[0])
    old_keys = dict(kv for kv in (key_of(l) for l in f_old) if kv[0])
    if new_keys.get("status") != "superseded" or new_keys.get("superseded_by") != record:
        problems.append("status or superseded_by is not set as marked")
    if new_keys.get("created") != old_keys.get("created"):
        problems.append("created changed")
    try:
        if new_keys.get("version") != bump_minor(old_keys.get("version", "")):
            problems.append("version is not the old one up one minor")
    except Refusal:
        problems.append("version unreadable")
    if not b_new.startswith(b_old):
        problems.append("the original body is not a byte-exact prefix of the new body")
    else:
        rest = b_new[len(b_old):]
        expected = ("" if b_old.endswith("\n") else "\n") + "\n## Changelog\n\n" + changelog_line(
            new_keys.get("version", "?"), (new_keys.get("modified") or "")[:10], record, activity) + "\n"
        if rest != expected:
            problems.append("what follows the original body is not exactly one changelog line")
    return problems


def first_sentence(body: str, max_words: int) -> str:
    """The first sentence of the text after the headings, flattened to one line and cut at max_words; no body is copied."""
    if max_words <= 0:
        return ""
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            if lines:
                break
            continue
        lines.append(re.sub(r"^[-*+]\s+", "", line))
    text = re.sub(r"\s+", " ", " ".join(lines)).replace("|", "/").replace("`", "").replace("*", "")
    text = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    words = text.split()
    return " ".join(words[:max_words]).rstrip(" ,;:-")
