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


# --- audit rows and the git helpers -------------------------------------------------------------------------------

def read_audit(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [f for f in AUDIT_FIELDS if f not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit(f"run_notes_move: the audit CSV lacks columns: {', '.join(missing)}")
        return [{"path": r["path"].strip(), "activity": r["activity"].strip(), "words": int(r["words"] or 0),
                 "record": r["mapped_record_path"].strip(), "share": r["shared_number_share"], "cls": r["class"].strip().lower()}
                for r in reader]


def git(root: Path, *args: str, check: bool = True) -> str:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    proc = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, env=env)
    if check and proc.returncode:
        raise SystemExit(f"run_notes_move: git {args[0]} failed: {proc.stderr.strip()[:200]}")
    return proc.stdout if proc.returncode == 0 else ""


def write_safe(root: Path, rel: str, text: str) -> None:
    """The only writer: a path under _activities_/ or _run_notes_/, so a record, a queue file or a knowledge page can never be
    edited by this tool."""
    if not (rel.startswith("_activities_/") or rel.startswith(f"{TYPE_DIR}/")) or ".." in rel.split("/"):
        raise SystemExit(f"run_notes_move: refusing to write outside _activities_ and {TYPE_DIR}: {rel}")
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".run-notes-", dir=str(path.parent))
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.replace(tmp, path)


def write_page(root: Path, rel: str, text: str, now: datetime) -> bool:
    """Write a generated page unless it already says the same: an unchanged body leaves the file alone (a second run changes
    nothing); a changed one keeps its created, moves modified and version. True when the file was written."""
    path = root / rel
    if path.is_file():
        old = path.read_text(encoding="utf-8")
        f_old, _h, b_old = split_front(old)
        f_new, h_new, b_new = split_front(text)
        if f_old is not None and f_new is not None:
            if b_old == b_new:
                return False
            keys = dict(kv for kv in (key_of(l) for l in f_old) if kv[0])
            lines = []
            for line in f_new:
                k = key_of(line)[0]
                if k == "created" and keys.get("created"):
                    line = f"created: {keys['created']}"
                elif k == "version" and keys.get("version"):
                    line = f"version: {bump_minor(keys['version'])}"
                elif k == "modified":
                    line = f"modified: {now.strftime('%Y-%m-%dT%H:%M:%SZ')}"
                lines.append(line)
            text = "---\n" + "\n".join(lines) + "\n---\n" + b_new
    write_safe(root, rel, text)
    return True


def read(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def new_path(row: dict) -> str:
    return f"{TYPE_DIR}/{row['activity']}/{os.path.basename(row['path'])}"


# --- per-file evaluation -------------------------------------------------------------------------------------------

def evaluate_row(root: Path, row: dict, now: datetime, reviewed: set | None) -> dict:
    """What would happen to one audit row: state move, done or refuse, with a reason and, for a move, the marked text.
    `reviewed` None skips the digest check (the dry run counts as if reviewed and reports the digest separately)."""
    entry = {"row": row, "state": "refuse", "reason": "", "marked": None, "original": None}
    name = os.path.basename(row["path"])
    if row["cls"] != "a":
        entry["reason"] = "class"
    elif row["path"] != f"_activities_/{row['activity']}/{name}" or not name.endswith(".md"):
        entry["reason"] = "outside-activity-folder"
    elif not row["record"].startswith("_records_/") or not (root / row["record"]).is_file():
        entry["reason"] = "record-missing"
    elif reviewed is not None and (row["activity"] not in reviewed or not (root / "_activities_" / row["activity"] / "rule-digest.md").is_file()):
        entry["reason"] = "digest-unreviewed"
    else:
        src, dst = root / row["path"], root / new_path(row)
        if src.is_file() and not dst.exists():
            text = src.read_text(encoding="utf-8")
            front, _head, _body = split_front(text)
            try:
                if front is not None and is_marked(front, row["record"]):
                    marked = text                                            # a resumed run: marked but not yet moved
                    head = git(root, "show", f"HEAD:{row['path']}", check=False)
                    hf, _h, _b = split_front(head) if head else (None, None, None)
                    text = head if head and not (hf is not None and is_marked(hf, row["record"])) else None
                else:
                    marked = mark_text(text, row["record"], row["activity"], now)
                if body_words(marked) >= HARD_WORDS:
                    raise Refusal("word-budget")
            except Refusal as refusal:
                entry["reason"] = refusal.code
            else:
                entry.update(state="move", marked=marked, original=text)         # original None: a resumed file with no unmarked copy at HEAD
        elif dst.is_file() and not src.exists():
            front, _h, _b = split_front(dst.read_text(encoding="utf-8"))
            if front is not None and is_marked(front, row["record"]):
                entry["state"] = "done"
            else:
                entry["reason"] = "target-conflict"
        elif src.exists() and dst.exists():
            entry["reason"] = "target-conflict"
        else:
            entry["reason"] = "source-missing"
    return entry


# --- catalogs, indexes ---------------------------------------------------------------------------------------------

def title_of(activity: str) -> str:
    return " ".join(w.capitalize() for w in activity.split("-"))


def front_block(title: str, description: str, now: datetime) -> str:
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"---\ntitle: {title}\ncreated: {stamp}\nmodified: {stamp}\nversion: 1.0.0\ndescription: {description}\n---\n\n"


def build_pages(activity: str, entries: list[tuple[str, str]], now: datetime) -> dict[str, str]:
    """INDEX.md and catalog pages for one activity folder. entries are (file name, first sentence), sorted by name. Each catalog
    page stays at CATALOG_WORDS body words or fewer; the INDEX names every page in one line."""
    pages: list[list[tuple[str, str]]] = []
    current: list[tuple[str, str]] = []

    def render(n: int, chunk) -> str:
        first, last = chunk[0][0][:-3], chunk[-1][0][:-3]
        lines = [f"- [{name[:-3]}]({name})" + (f" - {sentence}" if sentence else "") for name, sentence in chunk]
        return (front_block(f"{title_of(activity)} run notes catalog {n:02d}", f"Catalog {n:02d} of the superseded {activity} run notes", now)
                + f"# Catalog {n:02d}\n\n{len(chunk)} run notes, from {first} to {last}. Back to the [index](INDEX.md).\n\n" + "\n".join(lines) + "\n")

    for item in entries:
        if current and body_words(render(len(pages) + 1, current + [item])) > CATALOG_WORDS:
            pages.append(current)
            current = []
        current.append(item)
    if current:
        pages.append(current)
    out = {}
    index_lines = []
    for n, chunk in enumerate(pages, 1):
        out[f"catalog-{n:02d}.md"] = render(n, chunk)
        index_lines.append(f"- [Catalog {n:02d}](catalog-{n:02d}.md) - {chunk[0][0][:-3]} to {chunk[-1][0][:-3]}, {len(chunk)} notes")
    title = title_of(activity)
    body = (f"# {title} run notes\n\n{len(entries)} run articles of [{activity}](../../_activities_/{activity}/INDEX.md) that duplicate a dated "
            f"record. Each is marked `status: superseded` with a `superseded_by` pointer to its record and moved here with its text "
            f"unchanged; nothing was deleted. The standing rules are in the [rule digest](../../_activities_/{activity}/rule-digest.md). "
            f"Old paths resolve through the [moved paths table](../moved-paths/INDEX.md).\n\n## Catalogs\n\n" + "\n".join(index_lines) + "\n")
    out["INDEX.md"] = front_block(f"{title} Run Notes", f"Superseded run articles of {activity}, catalogued", now) + body
    return out


def folder_entries(root: Path, activity: str, sentence_words: int) -> list[tuple[str, str]]:
    folder = root / TYPE_DIR / activity
    out = []
    for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
        if path.name == "INDEX.md" or re.match(r"^catalog-\d+\.md$", path.name):
            continue
        _f, _h, body = split_front(path.read_text(encoding="utf-8"))
        out.append((path.name, first_sentence(body or "", sentence_words)))
    return out


def planned_entries(root: Path, activity: str, moves: list[dict], sentence_words: int) -> list[tuple[str, str]]:
    """The catalog entries after the moves: what the folder holds plus the files about to move (read from their source)."""
    have = dict(folder_entries(root, activity, sentence_words))
    for e in moves:
        _f, _h, body = split_front(e["original"])
        have[os.path.basename(e["row"]["path"])] = first_sentence(body or "", sentence_words)
    return sorted(have.items())


def type_index(existing: str | None, activities: list[str], now: datetime) -> str:
    wanted = [f"- [{a}]({a}/INDEX.md)" for a in activities] + [f"- [{MAP_DIR}]({MAP_DIR}/INDEX.md)"]
    if existing is None:
        return (front_block("Run Notes", "Run articles superseded by a dated record, one folder per activity", now) + "# Run notes\n\n"
                "Run articles that duplicate a dated record: each is marked superseded, then moved here from `_activities_/<activity>/`, "
                "unchanged apart from the mark. One folder per activity; the old paths resolve through the moved paths table.\n\n"
                + "\n".join(wanted) + "\n")
    add = [line for line in wanted if line not in existing]
    if not add:
        return existing
    text = existing.rstrip("\n") + "\n" + "\n".join(add) + "\n"
    return touch_doc(text, now)


def touch_doc(text: str, now: datetime, changelog: str | None = None) -> str:
    """modified now and version up one minor in a page's frontmatter; a changelog line when the page ends in a Changelog section."""
    front, head, body = split_front(text)
    if front is None:
        return text
    keys = dict(kv for kv in (key_of(l) for l in front) if kv[0])
    if "version" not in keys or "modified" not in keys:
        return text
    try:
        version = bump_minor(keys["version"])
    except Refusal:
        return text
    out = [f"version: {version}" if key_of(l)[0] == "version" else
           f"modified: {now.strftime('%Y-%m-%dT%H:%M:%SZ')}" if key_of(l)[0] == "modified" else l for l in front]
    text = "---\n" + "\n".join(out) + "\n---\n" + body
    headings = [l for l in body.splitlines() if l.startswith("## ")]
    if changelog and headings and headings[-1].strip() == "## Changelog":
        text = text.rstrip("\n") + "\n" + changelog.format(version=version, day=now.strftime("%Y-%m-%d")) + "\n"
    return text


# --- references ----------------------------------------------------------------------------------------------------

def rewrite_links(text: str, file_rel: str, moved: dict[str, str]):
    """(new_text, count): markdown links that resolve to a moved file now point at its new path."""
    import posixpath
    count = 0

    def sub(m):
        nonlocal count
        target = posixpath.normpath(posixpath.join(posixpath.dirname(file_rel), m.group(1)))
        if target not in moved:
            return m.group(0)
        count += 1
        return "](" + posixpath.relpath(moved[target], posixpath.dirname(file_rel)) + (m.group(2) or "") + ")"
    return LINK.sub(sub, text), count


def scan_references(root: Path, moved: dict[str, str]):
    """[(rel, new_text, links)] for each _activities_ page whose links to moved files need rewriting."""
    out = []
    for path in sorted((root / "_activities_").rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel in moved:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        new, count = rewrite_links(text, rel, moved)
        if count:
            out.append((rel, new, count))
    return out


def dangling_links(root: Path) -> int:
    import posixpath
    bad = 0
    for path in (root / "_activities_").rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        for m in LINK.finditer(path.read_text(encoding="utf-8", errors="replace")):
            if not (root / posixpath.normpath(posixpath.join(posixpath.dirname(rel), m.group(1)))).exists():
                bad += 1
    return bad


def outside_references(root: Path, moved_old: set[str]):
    """Counts of files outside _activities_ and _run_notes_ that name an old path (left untouched: moved-paths.csv resolves them)."""
    out = Counter()
    pattern = r"_activities_/[a-z0-9-]+/run-[0-9]{8}-[0-9]{4}[A-Za-z0-9._-]*\.md"
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    proc = subprocess.run(["git", "-C", str(root), "grep", "-I", "-l", "-E", pattern, "--", ".", ":(exclude)_activities_", f":(exclude){TYPE_DIR}"],
                          capture_output=True, text=True, env=env)
    if proc.returncode not in (0, 1):                      # 1 is "no match"; anything else must not read as none
        raise SystemExit(f"run_notes_move: git grep failed: {proc.stderr.strip()[:200]}")
    names = proc.stdout.splitlines()
    for name in names:
        text = (root / name).read_text(encoding="utf-8", errors="replace")
        if any(old in text for old in moved_old):
            out[name.split("/", 1)[0] if "/" in name else "(root)"] += 1
    return out


# --- the moved-paths table -----------------------------------------------------------------------------------------

def read_map(root: Path) -> "OrderedDict[str, tuple[str, str]]":
    path = root / MAP_REL
    rows = OrderedDict()
    if path.is_file():
        with open(path, newline="", encoding="utf-8") as handle:
            for r in csv.DictReader(handle):
                rows[r["old_path"]] = (r["new_path"], r["record"])
    return rows


def write_map(root: Path, rows: dict, now: datetime) -> None:
    import io
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(["old_path", "new_path", "record"])
    for old in sorted(rows):
        writer.writerow([old, *rows[old]])
    if not (root / MAP_REL).is_file() or read(root, MAP_REL) != buf.getvalue():
        write_safe(root, MAP_REL, buf.getvalue())
    index_rel = f"{TYPE_DIR}/{MAP_DIR}/INDEX.md"
    body = (f"# Moved paths\n\n[moved-paths.csv](moved-paths.csv) maps the old path of each run article that moved from "
            f"`_activities_/<activity>/` to `{TYPE_DIR}/<activity>/` to its new path and to the dated record it duplicates: {len(rows)} rows "
            f"(old_path, new_path, record). Records and other pages that cite an old path are never edited; resolve the path here. "
            f"Back to the [run notes](../INDEX.md).\n")
    write_page(root, index_rel, front_block("Moved Paths", "The table that resolves the old paths of the moved run articles", now) + body, now)


# --- plan, apply, verify -------------------------------------------------------------------------------------------

def parse_now(value: str) -> datetime:
    if not value:
        return datetime.now(timezone.utc).replace(microsecond=0)
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def reviewed_set(a) -> set:
    names = set(filter(None, (a.reviewed or "").split(",")))
    if getattr(a, "reviewed_file", None):
        names |= {ln.strip() for ln in Path(a.reviewed_file).read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")}
    return names


def activities_of(rows: list[dict], wanted: str) -> list[str]:
    present = sorted({r["activity"] for r in rows if r["cls"] == "a"})
    if not wanted or wanted == "all":
        return present
    asked = [x for x in wanted.split(",") if x]
    unknown = [x for x in asked if x not in present]
    if unknown:
        raise SystemExit(f"run_notes_move: no class a rows for: {', '.join(unknown)}")
    return asked


def evaluate_activity(root, rows, activity, now, reviewed, sentence_words):
    mine = [r for r in rows if r["activity"] == activity and r["cls"] == "a"]
    entries = [evaluate_row(root, r, now, reviewed) for r in mine]
    moves = [e for e in entries if e["state"] == "move"]
    done = [e for e in entries if e["state"] == "done"]
    refused = Counter(e["reason"] for e in entries if e["state"] == "refuse")
    moved_map = {e["row"]["path"]: new_path(e["row"]) for e in moves + done}
    refs = scan_references(root, moved_map)
    over = sum(1 for rel, _t, _c in refs if body_words(read(root, rel)) >= HARD_WORDS)
    pages = build_pages(activity, planned_entries(root, activity, moves, sentence_words), now) if (moves or done) else {}
    return {"activity": activity, "files": len(mine), "words": sum(r["words"] for r in mine), "to_move": len(moves), "done": len(done),
            "refused": dict(refused), "catalog_pages": sum(1 for k in pages if k != "INDEX.md"),
            "index_words": body_words(pages["INDEX.md"]) if pages else 0,
            "max_catalog_words": max([body_words(v) for k, v in pages.items() if k != "INDEX.md"] or [0]),
            "reference_links": sum(c for _r, _t, c in refs), "reference_files": len(refs), "referencing_files_over_500_words": over,
            "digest_reviewed": activity in reviewed if reviewed is not None else None,
            "_entries": entries, "_moves": moves, "_moved_map": moved_map}


def public(report: dict) -> dict:
    return {k: v for k, v in report.items() if not k.startswith("_")}


def sample_diff(root: Path, entry: dict) -> list[str]:
    """The frontmatter and the appended changelog of one planned move as a unified diff with no context: only the marked lines
    appear, never the body of the article."""
    f_old, _h, b_old = split_front(entry["original"])
    f_new, _h2, b_new = split_front(entry["marked"])
    lines = list(difflib.unified_diff(f_old, f_new, f"{entry['row']['path']} (frontmatter)", f"{new_path(entry['row'])} (frontmatter)", n=0, lineterm=""))
    lines.append(f"@@ body: the original {len(b_old)} bytes are unchanged; appended after them:")
    lines += ["+" + ln for ln in b_new[len(b_old):].splitlines()]
    return lines


def cmd_plan(a, root: Path, rows):
    now, reviewed = parse_now(a.now), reviewed_set(a)
    reports = [evaluate_activity(root, rows, act, now, None, a.sentence_words) for act in activities_of(rows, a.activities)]
    for r in reports:
        r["digest_reviewed"] = r["activity"] in reviewed
    total = Counter()
    for r in reports:
        for k in ("files", "words", "to_move", "done", "catalog_pages", "reference_links", "reference_files", "referencing_files_over_500_words"):
            total[k] += r[k]
        for k, v in r["refused"].items():
            total["refused:" + k] += v
    outside = outside_references(root, {r["path"] for r in rows if r["cls"] == "a"})
    sample = []
    if a.sample:
        for r in reports:
            for e in r["_moves"][:1]:
                if len(sample) < a.sample:
                    sample.append({"activity": r["activity"], "diff": sample_diff(root, e)})
    result = {"dry_run": True, "audit_rows": len(rows), "activities": [public(r) for r in reports], "total": dict(total),
              "outside_activities_references": dict(outside), "sample": sample,
              "digests_reviewed": sum(1 for r in reports if r["digest_reviewed"])}
    if a.format == "json":
        print(json.dumps(result, indent=1, sort_keys=True))
        return 0
    print(f"run-notes-move PLAN (dry run, nothing written): class a rows {total['files']} ({total['words']} words), "
          f"{len(reports)} activities; the digest check is reported, not applied, in a plan")
    print(f"{'activity':<28}{'files':>6}{'words':>8}{'move':>6}{'done':>5}{'refused':>8}{'pages':>6}{'idx w':>6}{'links':>7}{'in':>4}{'over':>5}  digest")
    for r in reports:
        refused = sum(r["refused"].values())
        print(f"{r['activity']:<28}{r['files']:>6}{r['words']:>8}{r['to_move']:>6}{r['done']:>5}{refused:>8}{r['catalog_pages']:>6}"
              f"{r['index_words']:>6}{r['reference_links']:>7}{r['reference_files']:>4}{r['referencing_files_over_500_words']:>5}  "
              f"{'reviewed' if r['digest_reviewed'] else 'UNREVIEWED'}")
    print(f"{'TOTAL':<28}{total['files']:>6}{total['words']:>8}{total['to_move']:>6}{total['done']:>5}"
          f"{sum(v for k, v in total.items() if k.startswith('refused:')):>8}{total['catalog_pages']:>6}{'':>6}{total['reference_links']:>7}"
          f"{total['reference_files']:>4}{total['referencing_files_over_500_words']:>5}")
    refused_total = {k[8:]: v for k, v in total.items() if k.startswith("refused:")}
    print("refused by reason: " + (", ".join(f"{k} {v}" for k, v in sorted(refused_total.items())) or "none"))
    print("references outside _activities_, left untouched (moved-paths.csv resolves them): "
          + (", ".join(f"{k} {v}" for k, v in sorted(outside.items())) or "none") + f"; dangling links in _activities_ now: {dangling_links(root)}")
    for s in sample:
        print(f"--- sample diff ({s['activity']}) ---")
        print("\n".join(s["diff"]))
    return 0


def apply_activity(a, root: Path, rows, activity: str, now: datetime, reviewed: set) -> dict:
    report = evaluate_activity(root, rows, activity, now, reviewed, a.sentence_words)
    out = public(report)
    out.update(moved=0, proof_failures=0, rewritten_links=0, rewritten_files=0, written=[])
    if activity not in reviewed or not (root / "_activities_" / activity / "rule-digest.md").is_file():
        return out                                                       # refused whole: nothing is written for this activity
    moves = report["_moves"]
    proof_failures = 0
    for e in moves:                                                      # 1 and 2, and 6 for each file moved now
        row, src, dst = e["row"], row_path(root, e["row"]["path"]), root / new_path(e["row"])
        if e["original"] is not None and e["marked"] != e["original"]:
            write_safe(root, row["path"], e["marked"])
        problems = verify_pair(e["original"], e["marked"], row["record"], activity) if e["original"] is not None else []
        if problems:
            proof_failures += 1
            if e["original"] is not None and e["marked"] != e["original"]:
                write_safe(root, row["path"], e["original"])             # put it back: a file that fails its proof does not move
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        tracked = subprocess.run(["git", "-C", str(root), "ls-files", "--error-unmatch", "--", row["path"]], capture_output=True).returncode == 0
        if tracked:
            git(root, "mv", row["path"], new_path(row))
        else:                                                              # not committed yet: a plain move, then the same add
            os.replace(src, dst)
        git(root, "add", "--", new_path(row))                            # the rename and the mark are staged together
        out["moved"] += 1
    out["proof_failures"] = proof_failures
    # 3 catalogs and INDEX from what the folder now holds
    pages = build_pages(activity, folder_entries(root, activity, a.sentence_words), now)
    folder = root / TYPE_DIR / activity
    for stale in sorted(folder.glob("catalog-*.md")):
        if stale.name not in pages:
            stale.unlink()
    for name, text in pages.items():
        if write_page(root, f"{TYPE_DIR}/{activity}/{name}", text, now):
            out["written"].append(name)
    # 4 references, for every file now in the folder (this block and earlier ones)
    moved_map = {}
    for r in (r for r in rows if r["activity"] == activity and r["cls"] == "a"):
        if (root / new_path(r)).is_file() and not (root / r["path"]).exists():
            moved_map[r["path"]] = new_path(r)
    for rel, new_text, count in scan_references(root, moved_map):
        write_safe(root, rel, touch_doc(new_text, now, "- {version}, {day} - Links to run notes that moved to " + f"{TYPE_DIR}/{activity}/" + " now point there."))
        out["rewritten_links"] += count
        out["rewritten_files"] += 1
    # 5 the table rows of this activity; the block writes the table and the type index once
    out["table_add"] = {r["path"]: (new_path(r), r["record"]) for r in rows
                        if r["activity"] == activity and r["cls"] == "a" and r["path"] in moved_map}
    out["dangling_links_in_activities"] = dangling_links(root)
    return out


def row_path(root, rel):
    return root / rel


def cmd_apply(a, root: Path, rows):
    now, reviewed = parse_now(a.now), reviewed_set(a)
    acts = activities_of(rows, a.activities)
    if not a.activities or a.activities == "all":
        raise SystemExit("run_notes_move: apply needs --activities a,b,c (a block, never everything at once)")
    if len(acts) > a.block_limit:
        raise SystemExit(f"run_notes_move: {len(acts)} activities in one block; the limit is {a.block_limit} (--block-limit)")
    results = [apply_activity(a, root, rows, act, now, reviewed) for act in acts]
    table = read_map(root)
    for r in results:
        for old, entry in r.pop("table_add", {}).items():
            if table.get(old, entry) != entry:
                raise SystemExit(f"run_notes_move: moved-paths.csv already maps {old} differently")
            table[old] = entry
    if any(r["moved"] or r["done"] for r in results):
        write_map(root, table, now)
        present = sorted(p.name for p in (root / TYPE_DIR).iterdir() if p.is_dir() and p.name != MAP_DIR)
        idx_rel = f"{TYPE_DIR}/INDEX.md"
        new_index = type_index(read(root, idx_rel) if (root / idx_rel).is_file() else None, present, now)
        if not (root / idx_rel).is_file() or new_index != read(root, idx_rel):
            write_safe(root, idx_rel, new_index)
    bad = 0
    for r in results:
        refused = sum(r["refused"].values())
        bad += refused + r["proof_failures"]
        print(f"{r['activity']}: moved {r['moved']}, already done {r['done']}, refused {refused} {r['refused'] or ''}, proof failures "
              f"{r['proof_failures']}, catalog pages {r['catalog_pages']}, links rewritten {r['rewritten_links']} in {r['rewritten_files']} files"
              + (f", dangling links in _activities_ {r.get('dangling_links_in_activities')}" if r["moved"] or r["done"] else ", NOT APPLIED"))
    return 1 if bad else 0


def cmd_verify(a, root: Path, rows):
    base = a.base
    table = read_map(root)
    selected = set(a.activities.split(",")) if a.activities and a.activities != "all" else None
    ok = missing = bad = 0
    for old, (new, record) in sorted(table.items()):
        activity = new.split("/")[1]
        if selected and activity not in selected:
            continue
        original = git(root, "show", f"{base}:{old}", check=False)
        if not original or not (root / new).is_file() or (root / old).exists():
            missing += 1
            continue
        if verify_pair(original, read(root, new), record, activity):
            bad += 1
        else:
            ok += 1
    print(f"verify against {base}: {ok} files equal their original apart from the marked frontmatter and the changelog line, "
          f"{bad} differ, {missing} could not be compared (original not at {base}, new file missing, or old path still there)")
    return 0 if bad == 0 and missing == 0 else 1


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(HERE.parent.parent), help="the repository (default: the one holding this tool)")
    p.add_argument("--audit", default="_records_/2026-11-22/coach/run-articles-audit.csv", help="the coach's audit CSV, relative to --root")
    p.add_argument("--now", default="", help="the instant to stamp, ISO 8601 UTC (default: now)")
    p.add_argument("--sentence-words", type=int, default=12, help="words of each file's first sentence in a catalog line (0 for none)")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("plan", "apply"):
        s = sub.add_parser(name)
        s.add_argument("--activities", default="", help="a,b,c (apply needs it; plan defaults to all)")
        s.add_argument("--reviewed", default="", help="activities whose rule digest was reviewed against the new paths")
        s.add_argument("--reviewed-file", help="the same, one activity per line")
        if name == "plan":
            s.add_argument("--sample", type=int, default=0, help="print the diff of this many planned moves (frontmatter and changelog only)")
            s.add_argument("--format", choices=("text", "json"), default="text")
        else:
            s.add_argument("--block-limit", type=int, default=3)
    v = sub.add_parser("verify")
    v.add_argument("--base", default="HEAD", help="the revision holding the originals (HEAD before the commit, origin/main after)")
    v.add_argument("--activities", default="")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()
    audit = Path(a.audit) if os.path.isabs(a.audit) else root / a.audit
    if not audit.is_file():
        print(f"run_notes_move: no audit CSV at {audit}", file=sys.stderr)
        return 2
    rows = read_audit(audit)
    return {"plan": cmd_plan, "apply": cmd_apply, "verify": cmd_verify}[a.cmd](a, root, rows)


if __name__ == "__main__":
    sys.exit(main())
