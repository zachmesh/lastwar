#!/usr/bin/env python3
"""split_doc: a section-aware, verbatim splitter for a Markdown document.

A document too long for the word budget becomes a folder: an INDEX.md of 300 words or fewer (what it is, how to find an
entry, one line per article with its first sentence; catalog pages when the articles outnumber what an index holds) and
articles of at most 450 body words, cut at headings first, then at paragraph, list-item, table-row, line, sentence and
word boundaries. Article bodies are exact slices of the original body, so concatenated in order they equal it byte for
byte. Dry run by default; --apply writes. It acts only on the files it is given. Standard library only; the word
counter is the convention linter's own, loaded from the reflection checkout. Exit 0 ok, 1 refused or verify failed, 2
cannot run.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0.0"
ARTICLE_LIMIT, INDEX_LIMIT, CATALOG_BUDGET = 450, 300, 360
TARGETS = (440, 420, 380, 320, 250)        # packing targets, tried in turn until every real count is within the limit
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+){1,3}$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})[ \t]+(\S.*?)[ \t]*$")
ITEM = re.compile(r"^(?:[-*+]|\d{1,3}[.)])[ \t]|^\|")
ARTICLE_FILE = re.compile(r"^\d+-[a-z0-9-]+\.md$")
PAGE_PREFIXES = ("catalog", "volume", "shelf")


class SplitError(Exception):
    """Cannot run (exit 2)."""


class Refused(Exception):
    """A safety rule refused the operation (exit 1)."""


# --- counting and text helpers -----------------------------------------------------------------------------------
def load_counter(reflection: str | None):
    base = Path(reflection or os.environ.get("LINT_GATE_REFLECTION") or "~/dtadpole/reflection").expanduser()
    path = base / "_tools_/document-word-budget/word-budget.py"
    if not path.is_file():
        raise SplitError(f"word counter not found: {path} (set --reflection or LINT_GATE_REFLECTION)")
    spec = importlib.util.spec_from_file_location("split_doc_word_budget", path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ImportError as exc:
        raise SplitError(f"the word counter needs a module this python lacks ({exc})")
    return module


class Counter:
    def __init__(self, module):
        self.m, self.cache = module, {}

    def words(self, text: str) -> int:
        """Words of a body fragment; an empty frontmatter in front stops a leading `---` rule being read as one."""
        if text not in self.cache:
            self.cache[text] = self.m.count_words("---\n---\n" + text)
        return self.cache[text]

    def file_words(self, text: str) -> int:
        return self.m.count_words(text)


def split_frontmatter(text: str) -> tuple[str, str]:
    """(frontmatter block with its closing line, body); the body is everything after that line."""
    lines = text.splitlines(keepends=True)
    if lines and lines[0].rstrip("\r\n") == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip("\r\n") in ("---", "..."):
                return "".join(lines[:i + 1]), "".join(lines[i + 1:])
    return "", text


def field(front: str, name: str) -> str | None:
    m = re.search(rf"(?m)^{name}:[ \t]*(.*?)[ \t]*$", front)
    return m.group(1).strip("'\"") if m else None


def plain(text: str, cap: int | None = None) -> str:
    """Text made safe as a plain YAML or link value: no colon, quote, bracket or other markup."""
    text = re.sub(r"[^A-Za-z0-9 ,.;()/+_&'-]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^[^A-Za-z0-9]+", "", text)
    if cap:
        parts = text.split()
        text = " ".join(parts[:cap])
    return text


def slug_words(title: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", title.lower())][:3] or ["part"]


def bump_minor(version: str | None) -> str:
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)", version or "")
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0" if m else "0.1.0"


# --- splitting ---------------------------------------------------------------------------------------------------
def headings(lines: list[str]) -> dict[int, list[int]]:
    """Line indices of ATX headings by level, outside fenced code."""
    found, fence = {}, None
    for i, line in enumerate(lines):
        m = FENCE.match(line)
        if m:
            if fence is None:
                fence = m.group(1)[0]
            elif m.group(1)[0] == fence:
                fence = None
            continue
        if fence is None and HEADING.match(line.rstrip("\r\n")):
            found.setdefault(len(HEADING.match(line.rstrip("\r\n")).group(1)), []).append(i)
    return found


def split_paragraphs(text: str) -> list[str]:
    parts, cur, fence, blank = [], [], None, False
    for line in text.splitlines(keepends=True):
        m = FENCE.match(line)
        if blank and line.strip() and fence is None and cur:
            parts.append("".join(cur))
            cur = []
        cur.append(line)
        if m:
            fence = m.group(1)[0] if fence is None else (None if m.group(1)[0] == fence else fence)
        blank = not line.strip()
    if cur:
        parts.append("".join(cur))
    return parts


def split_items(text: str) -> list[str]:
    lines, parts, cur, fence = text.splitlines(keepends=True), [], [], None
    for line in lines:
        m = FENCE.match(line)
        if m:
            fence = m.group(1)[0] if fence is None else (None if m.group(1)[0] == fence else fence)
        if fence is None and not m and ITEM.match(line) and cur:
            parts.append("".join(cur))
            cur = []
        cur.append(line)
    if cur:
        parts.append("".join(cur))
    return parts


SPLITTERS = (
    split_paragraphs, split_items, lambda t: t.splitlines(keepends=True),
    lambda t: re.split(r"(?<=[.!?;])(?=\s)", t), lambda t: re.findall(r"\S+\s*|\s+", t),
)


def explode(text: str, limit: int, counter: Counter, tier: int = 0) -> list[str]:
    """Slices of `text`, in order, each within `limit` words, cut at the coarsest boundary that fits."""
    if counter.words(text) <= limit or tier >= len(SPLITTERS):
        return [text]
    parts = [p for p in SPLITTERS[tier](text) if p]
    if len(parts) <= 1:
        return explode(text, limit, counter, tier + 1)
    out = []
    for p in parts:
        out += explode(p, limit, counter, tier + 1)
    return out


def by_headings(lines: list[str], a: int, b: int, level: int, heads: dict, limit: int, counter: Counter) -> list[str]:
    text = "".join(lines[a:b])
    if counter.words(text) <= limit:
        return [text]
    for lv in range(level, 7):
        cuts = [i for i in heads.get(lv, []) if a < i < b]
        if cuts:
            edges, out = [a] + cuts + [b], []
            for s, e in zip(edges, edges[1:]):
                out += by_headings(lines, s, e, lv + 1, heads, limit, counter)
            return out
    return explode(text, limit, counter)


def pack(atoms: list[str], target: int, counter: Counter) -> list[str]:
    out, cur, total = [], [], 0
    for atom in atoms:
        w = counter.words(atom)
        if cur and total + w > target:
            out.append("".join(cur))
            cur, total = [], 0
        cur.append(atom)
        total += w
    if cur:
        out.append("".join(cur))
    return out


def article_slices(body: str, counter: Counter) -> tuple[list[str], int]:
    lines = body.splitlines(keepends=True)
    heads = headings(lines)
    slices, target = [], TARGETS[-1]
    for target in TARGETS:
        atoms = by_headings(lines, 0, len(lines), 1, heads, target, counter)
        slices = pack(atoms, target, counter)
        if "".join(slices) != body:
            raise Refused("internal error: the slices do not rebuild the body")
        if all(counter.words(s) <= ARTICLE_LIMIT for s in slices):   # the real count of each concatenated slice
            break
    return slices, target


# --- describing the articles -------------------------------------------------------------------------------------
def heading_at(body: str, slices: list[str]) -> list[str]:
    """A title per slice: its first heading when it opens with one, else the preceding heading, continued. Slices may
    start mid-line (a sentence or word cut), so positions are character offsets."""
    lines = body.splitlines(keepends=True)
    starts, pos = [], 0
    for line in lines:
        starts.append(pos)
        pos += len(line)
    texts = {starts[i]: HEADING.match(lines[i].rstrip("\r\n")).group(2).rstrip("# ").strip()
             for v in headings(lines).values() for i in v}
    order = sorted(texts)
    titles, start, last = [], 0, None
    for s in slices:
        end = start + len(s)
        opening = start + len(s) - len(s.lstrip())
        if s.strip() and opening in texts:
            title = texts[opening]
        elif last:
            title = f"{last} continued"
        else:
            title = "Preamble"
        inside = [texts[o] for o in order if start <= o < end]
        last = inside[-1] if inside else last
        titles.append(plain(title) or "Part")
        start = end
    return titles


def first_sentence(text: str, cap: int) -> str:
    gathered, started = [], False
    for line in text.splitlines():
        s = line.strip()
        if not started:
            if not s or s.startswith("#") or FENCE.match(line) or not re.search(r"[A-Za-z0-9]", re.sub(r"[|:\- ]", "", s)):
                continue
            started = True
        elif not s or ITEM.match(s):   # the paragraph ends, or the next list item starts
            break
        s = re.sub(r"^(?:[-*+]|\d{1,3}[.)])\s+", "", s)
        s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
        gathered.append(s)
        if len(" ".join(gathered).split()) >= cap * 3:
            break
    flat = re.sub(r"[`*>|\[\]]", "", " ".join(gathered))
    flat = re.split(r"(?<=[.!?])\s", flat, maxsplit=1)[0]
    words = flat.split()
    return " ".join(words[:cap]) + ("..." if len(words) > cap else "")


def entry_line(file: str, title: str, sentence: str, cap: int) -> str:
    t = " ".join(title.split()[:8])
    s = " ".join(sentence.split()[:cap]) if cap else ""
    return f"- [{t}]({file})" + (f" - {s}" if s else "") + "\n"


def fit_page(entries: list[tuple], budget: int, counter: Counter) -> str | None:
    for cap in (14, 10, 6):   # never a titles-only page: paginate instead
        text = "".join(entry_line(f, t, s, cap) for f, t, s in entries)
        if counter.words(text) <= budget:
            return text
    return None


def layout(entries: list[tuple], budget: int, counter: Counter, now: str, doc_title: str) -> tuple[str, dict]:
    """The entry lines for INDEX.md within `budget` words and, when they do not fit, the catalog pages below it."""
    text = fit_page(entries, budget, counter)
    if text is not None:
        return text, {}
    pages, level = {}, entries
    for prefix in PAGE_PREFIXES:
        groups, cur = [], []
        for e in level:
            if cur and fit_page(cur + [e], CATALOG_BUDGET, counter) is None:
                groups.append(cur)
                cur = []
            cur.append(e)
        groups.append(cur)
        upper = []
        for n, g in enumerate(groups, 1):
            name, title = f"{prefix}-{n:02d}.md", f"{prefix.title()} {n:02d}"
            body = (f"\n# {title}\n\n{len(g)} entries of {plain(doc_title)}, from {g[0][1]} to {g[-1][1]}. "
                    f"Back to the [index](INDEX.md).\n\n" + fit_page(g, CATALOG_BUDGET, counter))
            pages[name] = front(title, f"{title} of the split {plain(doc_title)}", now, "1.0.0") + body
            upper.append((name, title, f"{g[0][1]} to {g[-1][1]}"))
        level = upper
        text = fit_page(level, budget, counter)
        if text is not None:
            return text, pages
    raise Refused("the document has too many articles for three index levels")


def front(title: str, description: str, now: str, version: str) -> str:
    return (f"---\ntitle: {plain(title)}\ncreated: {now}\nmodified: {now}\nversion: {version}\n"
            f"description: {plain(description, 30)}\n---\n")


# --- the plan ----------------------------------------------------------------------------------------------------
class Plan:
    def __init__(self):
        self.files: list[tuple[str, str]] = []     # (name, full text), INDEX.md last
        self.articles: list[str] = []
        self.body = ""
        self.target = 0
        self.index_words = 0


def build(original: str, stem: str, counter: Counter, now: str) -> Plan:
    plan = Plan()
    frontmatter, body = split_frontmatter(original)
    plan.body = body
    slices, plan.target = article_slices(body, counter)
    titles = heading_at(body, slices)
    width = max(3, len(str(len(slices))))
    entries = []
    for n, (text, title) in enumerate(zip(slices, titles), 1):
        name = f"{n:0{width}d}-{'-'.join(slug_words(title))}.md"
        description = first_sentence(text, 25) or title
        plan.files.append((name, front(title, description, now, "0.1.0") + text))
        plan.articles.append(name)
        entries.append((name, title, first_sentence(text, 14)))
    doc_title = field(frontmatter, "title") or next(
        (plain(HEADING.match(l.rstrip("\r\n")).group(2)) for l in body.splitlines() if HEADING.match(l)), stem)
    full = plain(field(frontmatter, "description") or "")
    summary = " ".join(full.split()[:25]) + ("..." if len(full.split()) > 25 else ".") if full else ""
    intro = (f"\n# {doc_title}\n\n{summary + ' ' if summary else ''}This document was split verbatim into {len(slices)} "
             f"articles in reading order, numbered from 001; nothing was rewritten, and `split_doc.py --check` "
             f"rebuilds the original body from them. Find an entry by its heading; each line gives the heading and "
             f"its first sentence.\n\n")
    budget = INDEX_LIMIT - counter.words(intro) - 8
    lines, pages = layout(entries, budget, counter, now, doc_title)
    plan.files += list(pages.items())
    version = bump_minor(field(frontmatter, "version"))
    if frontmatter:
        fm = frontmatter
        fm = re.sub(r"(?m)^version:.*$", f"version: {version}", fm, count=1) if field(fm, "version") is not None else \
            fm.replace("\n---", f"\nversion: {version}\n---", 1)
        fm = re.sub(r"(?m)^modified:.*$", f"modified: {now}", fm, count=1) if field(fm, "modified") is not None else fm
    else:
        fm = front(doc_title, summary or f"Split from {stem}", now, "0.1.0")
    index = fm + intro + lines
    plan.index_words = counter.file_words(index)
    plan.files.append(("INDEX.md", index))
    return plan


def verify(plan: Plan, counter: Counter, written: dict[str, str] | None = None) -> list[str]:
    """Problems found re-reading the files (as rendered, or as written): empty when the proof holds."""
    texts = dict(written if written is not None else plan.files)
    problems, joined = [], ""
    for name in plan.articles:
        joined += split_frontmatter(texts[name])[1]
    if joined != plan.body:
        problems.append("the article bodies do not concatenate to the original body")
    for name, text in texts.items():
        if name != "INDEX.md" and not NAME.match(name[:-3]):
            problems.append(f"{name}: name does not match the kebab-case rule")
        limit = INDEX_LIMIT if name == "INDEX.md" else ARTICLE_LIMIT
        words = counter.file_words(text)
        if words > limit:
            problems.append(f"{name}: {words} words, limit {limit}")
    if len(texts) != len(plan.files):
        problems.append("file count differs from the plan")
    return problems


# --- running -----------------------------------------------------------------------------------------------------
def inbound_references(top: Path | None, path: Path) -> list[str]:
    if top is None or path.name == "INDEX.md":
        return []
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    needle = f"{path.parent.name}/{path.name}"      # parent folder and name: the bare name matches too much
    out = subprocess.run(["git", "-C", str(top), "grep", "-l", "-F", "--", needle], capture_output=True, text=True, env=env).stdout
    here = path.resolve().relative_to(top).as_posix()
    return [p for p in out.splitlines() if p != here and not p.startswith(here[:-3] + "/")]


def repo_top(path: Path) -> Path | None:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    out = subprocess.run(["git", "-C", str(path.parent), "rev-parse", "--show-toplevel"], capture_output=True, text=True, env=env)
    return Path(out.stdout.strip()).resolve() if out.returncode == 0 and out.stdout.strip() else None


def check_input(path: Path) -> None:
    if path.is_symlink():
        raise Refused(f"{path}: a symbolic link is not split")
    if path.is_dir():
        raise Refused(f"{path}: a directory is not accepted; name the document itself")
    if not path.is_file() or path.suffix != ".md":
        raise Refused(f"{path}: not a Markdown file")


def process(path: Path, args, counter: Counter) -> int:
    check_input(path)
    original = path.read_bytes().decode("utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    is_index = path.name == "INDEX.md"
    folder = path.parent if is_index else path.with_suffix("")
    stem = path.parent.name if is_index else path.stem
    plan = build(original, stem, counter, now)
    problems = verify(plan, counter) if (args.verify or args.apply) else []
    sizes = [counter.file_words(t) for n, t in plan.files if n in plan.articles]
    original_words = counter.m.count_words(original)
    pages = len(plan.files) - len(plan.articles) - 1
    verdict = "not run (pass --verify)" if not (args.verify or args.apply) else ("FAIL: " + "; ".join(problems) if problems else
              f"PASS, article bodies rebuild the original body byte for byte (sha256 {hashlib.sha256(plan.body.encode()).hexdigest()[:12]})")
    print(f"{path}: {original_words:,} body words -> {len(plan.articles)} articles (max {max(sizes)} words, packed to {plan.target}), "
          f"INDEX.md {plan.index_words} words, {pages} catalog page(s); target folder {folder}")
    print(f"  verify: {verdict}")
    refs = inbound_references(repo_top(path), path)
    if refs:
        print(f"  inbound references to {path.parent.name}/{path.name} in {len(refs)} file(s), first {refs[:5]}; they need updating after the move")
    if is_index:
        print("  INDEX.md keeps its path; links to headings inside it may break")
    if args.list:
        for name, text in plan.files:
            print(f"    {counter.file_words(text):4d}  {name}")
    if problems:
        return 1
    if not args.apply:
        print("  dry run; pass --apply to write")
        return 0
    return apply(path, folder, is_index, plan, counter)


def apply(path: Path, folder: Path, is_index: bool, plan: Plan, counter: Counter) -> int:
    if not is_index and folder.exists() and any(folder.iterdir()):
        raise Refused(f"{folder} already exists and is not empty; nothing written")
    if is_index:
        clash = [n for n, _ in plan.files if n != "INDEX.md" and (folder / n).exists()]
        if clash:
            raise Refused(f"{folder}: would overwrite {clash[0]}; nothing written")
    staging = Path(tempfile.mkdtemp(prefix=".split-doc-", dir=path.parent))
    os.chmod(staging, 0o755)
    try:
        for name, text in plan.files:
            (staging / name).write_bytes(text.encode("utf-8"))
        written = {n: (staging / n).read_bytes().decode("utf-8") for n, _ in plan.files}
        problems = verify(plan, counter, written)
        if problems:
            print("  verify after writing: FAIL: " + "; ".join(problems))
            return 1
        if is_index:
            for name, _ in plan.files:
                if name != "INDEX.md":
                    os.rename(staging / name, folder / name)
            os.replace(staging / "INDEX.md", path)
        else:
            os.rename(staging, folder)
            staging = None
            os.remove(path)
    finally:
        if staging is not None:
            shutil.rmtree(staging, ignore_errors=True)
    print(f"  applied: {len(plan.files)} files in {folder}; verified from disk; original {'replaced' if is_index else 'removed'}")
    return 0


def check_folder(folder: Path, against: Path, counter: Counter) -> int:
    if not folder.is_dir() or not against.is_file():
        raise SplitError("--check needs a split folder and the original file (for example from git show)")
    joined = "".join(split_frontmatter((folder / n).read_bytes().decode("utf-8"))[1]
                     for n in sorted(os.listdir(folder)) if ARTICLE_FILE.match(n))
    original = split_frontmatter(against.read_bytes().decode("utf-8"))[1]
    same = joined == original
    print(f"check {folder}: article bodies {'EQUAL' if same else 'DIFFER FROM'} the original body ({len(joined)} and {len(original)} characters)")
    return 0 if same else 1


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="split_doc.py", description=__doc__.split("\n\n")[0])
    p.add_argument("paths", nargs="*", metavar="DOCUMENT.md", help="the Markdown files to split; only these are touched")
    p.add_argument("--apply", action="store_true", help="write the folder and remove the original (default: dry run)")
    p.add_argument("--verify", action="store_true", help="prove the planned bodies rebuild the original byte for byte")
    p.add_argument("--list", action="store_true", help="list every planned file with its word count")
    p.add_argument("--check", nargs=2, metavar=("FOLDER", "ORIGINAL"), help="verify an applied split against a copy of the original")
    p.add_argument("--reflection", help="the reflection checkout (default ~/dtadpole/reflection or LINT_GATE_REFLECTION)")
    args = p.parse_args(argv)
    try:
        counter = Counter(load_counter(args.reflection))
        if args.check:
            return check_folder(Path(args.check[0]), Path(args.check[1]), counter)
        if not args.paths:
            p.error("name at least one document")
        worst = 0
        for name in args.paths:
            try:
                worst = max(worst, process(Path(name), args, counter))
            except Refused as exc:
                print(f"split_doc: refused: {exc}", file=sys.stderr)
                worst = max(worst, 1)
        return worst
    except SplitError as exc:
        print(f"split_doc: cannot run: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
