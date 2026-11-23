#!/usr/bin/env python3
"""split_doc: a section-aware, verbatim splitter for a Markdown document.

A document too long for the word budget becomes a folder: an INDEX.md of 300 words or fewer (what it is, how to find an
entry, one line per article with its keys and first sentence; catalog pages when the articles outnumber what an index
holds) and articles of at most 450 body words. Each ## or ### section starts its own article, named from its key (an
entry id, a unit key such as run-20261107-1824, a day, else a slug); only consecutive tiny sections share one, and an
oversize section is cut at paragraph, list-item, table-row, line, sentence and word boundaries into -p1, -p2 parts.
Article bodies are exact slices of the original body, so in sequence order they equal it byte for byte. Dry run by
default; --apply writes. It acts only on the files it is given. Standard library only; the word counter is the
convention linter's own, loaded from the reflection checkout. Exit 0 ok, 1 refused or verify failed, 2 cannot run.
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

VERSION = "1.2.0"
ARTICLE_LIMIT, INDEX_LIMIT, CATALOG_BUDGET, HEADROOM = 450, 300, 360, 60
TARGETS = (440, 420, 380, 320, 250)        # packing targets, tried in turn until every real count is within the limit
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+){1,3}$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})[ \t]+(\S.*?)[ \t]*$")
ITEM = re.compile(r"^(?:[-*+]|\d{1,3}[.)])[ \t]|^\|")
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


# --- keys, titles and names --------------------------------------------------------------------------------------
ENTRY = re.compile(r"\b([A-Za-z]{2,6})-(\d{8})-(\d{1,3})\b")
DATE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
TIME_AFTER_DATE = re.compile(r"\s+(\d{2}):?(\d{2})\b")
CLOCK = re.compile(r"(?<![\d:])(\d{1,2}):(\d{2})(?::\d{2})?(?![\d:])")
TINY = 120          # a section this small may share an article with the consecutive tiny sections around it
SPLIT_LEVELS = (2, 3)


def heading_key(text: str) -> str:
    """The key of a heading: an entry id (od-20261123-03), a unit key (run-20261107-1824: date and HHMM), a day key
    (day-20261105), else a 2 to 4 word slug of its first words. Always lower case, words of [a-z0-9]."""
    m = ENTRY.search(text)
    if m:
        return f"{m.group(1).lower()}-{m.group(2)}-{int(m.group(3)):02d}"
    d = DATE.search(text)
    if d:
        ymd = "".join(d.groups())
        t = TIME_AFTER_DATE.match(text[d.end():])
        return f"run-{ymd}-{t.group(1)}{t.group(2)}" if t else f"day-{ymd}"
    words = re.findall(r"[a-z0-9]+", text.lower())[:3] or ["part"]
    return "-".join(words if len(words) > 1 else words + ["section"])


KEY_STOP = {"what", "is", "the", "this", "a", "an", "of", "and", "to", "how", "it", "in", "for", "from", "on", "as", "or",
            "with", "are", "was", "unit", "units", "added", "notes"}


def key_map(texts: list[str]) -> dict[str, str]:
    """Heading text to key. Two different headings with the same key (two dated sections of one day) are told apart by
    the first meaningful word of each; one heading listed twice keeps one key."""
    raw = {t: heading_key(t) for t in texts}
    groups: dict[str, list[str]] = {}
    for t, k in raw.items():
        groups.setdefault(k, []).append(t)
    out = dict(raw)
    for k, members in groups.items():
        if len(members) > 1:
            for t in members:
                word = next((w for w in re.findall(r"[a-z][a-z0-9]*", t.lower()) if w not in KEY_STOP and w not in k), None)
                if word and len(k.split("-")) <= 3:
                    out[t] = f"{k}-{word}"
    return out


def title_text(text: str) -> str:
    """A title: times read HHMM (00:11:00 is 0011), any other colon becomes a dash, markup is dropped."""
    text = CLOCK.sub(lambda m: f"{int(m.group(1)):02d}{m.group(2)}", text)
    return plain(text.replace(":", " -"), 16)


def allocate(base_key: str, part: int | None, taken: set) -> str:
    """A file name of 2 to 4 words from the key, with -pN for a part and -2, -3 when the name is taken."""
    base, suffix, n = base_key.split("-"), ([f"p{part}"] if part else []), 1
    while True:
        extra = suffix + ([str(n)] if n > 1 else [])
        name = "-".join(base[:max(1, 4 - len(extra))] + extra)
        if name not in taken:
            taken.add(name)
            return name
        n += 1


class Article:
    def __init__(self, text="", heading=None, words=0, part=None, parts=1, key=None):
        self.text, self.words, self.part, self.parts = text, words, part, parts
        self.headings = [heading] if heading else []     # the ## and ### headings this article holds
        self.keys = [key] if heading else []
        self.name, self.base = "", ""

    def add(self, text: str, heading: str, words: int, key: str) -> None:
        self.text += text
        self.words += words
        self.headings.append(heading)
        self.keys.append(key)


def make_articles(body: str, counter: Counter, target: int) -> list[Article]:
    """One article per ## or ### section when it fits; consecutive tiny sections share one; an oversize section is cut
    at paragraph or item boundaries into parts. The texts are exact slices of the body, in order."""
    lines = body.splitlines(keepends=True)
    heads = headings(lines)
    texts = {i: HEADING.match(lines[i].rstrip("\r\n")).group(2).rstrip("# ").strip() for v in heads.values() for i in v}
    cuts = sorted({i for lv in SPLIT_LEVELS for i in heads.get(lv, [])})
    kmap = key_map([texts[i] for i in cuts])
    edges = sorted(set([0] + cuts + [len(lines)]))
    arts, pending, carry = [], None, ""
    def flush():
        nonlocal pending
        if pending:
            arts.append(pending)
            pending = None
    for a, b in zip(edges, edges[1:]):
        text, heading = carry + "".join(lines[a:b]), (texts[a] if a in cuts else None)
        carry = ""
        if not text.strip() and heading is None:
            carry = text                       # leading blank lines ride along with the next section
            continue
        words = counter.words(text)
        if heading is None:                    # the preamble: its own article, titled by the document heading
            flush()
            top = next((texts[i] for i in sorted(texts) if i < (cuts[0] if cuts else len(lines)) and i in heads.get(1, [])), None)
            art = Article(text, None, words)
            art.preamble = top or "Preamble"
            arts.append(art)
        elif words > target:
            flush()
            hl = text.splitlines(keepends=True)          # keep the heading line with the start of its first paragraph
            k = 1
            while k < len(hl) and not hl[k].strip():
                k += 1
            head, rest = "".join(hl[:k]), "".join(hl[k:])
            atoms = explode(rest, target, counter)
            room = target - counter.words(head) - 2
            if atoms and counter.words(atoms[0]) > room:
                atoms = explode(atoms[0], room, counter) + atoms[1:]
            parts = pack([head] + atoms, target, counter)
            for n, ptxt in enumerate(parts, 1):
                arts.append(Article(ptxt, heading, counter.words(ptxt), n if len(parts) > 1 else None, len(parts), kmap[heading]))
        elif words <= TINY and pending and pending.words + words <= target:
            pending.add(text, heading, words, kmap[heading])
        elif words <= TINY:
            flush()
            pending = Article(text, heading, words, key=kmap[heading])
        else:
            flush()
            arts.append(Article(text, heading, words, key=kmap[heading]))
    if carry and arts:
        arts[-1].text += carry
    flush()
    return arts


def keyed_articles(body: str, counter: Counter) -> tuple[list[Article], int]:
    arts, target = [], TARGETS[-1]
    for target in TARGETS:
        arts = make_articles(body, counter, target)
        if "".join(a.text for a in arts) != body:
            raise Refused("internal error: the slices do not rebuild the body")
        if all(counter.words(a.text) <= ARTICLE_LIMIT for a in arts):
            break
    taken: set = set()
    for a in arts:
        first = a.headings[0] if a.headings else getattr(a, "preamble", "Preamble")
        a.base = a.keys[0] if a.keys else heading_key(first)
        a.name = allocate(a.base, a.part, taken) + ".md"
    return arts, target


def article_title(a: Article) -> str:
    first = a.headings[0] if a.headings else getattr(a, "preamble", "Preamble")
    title = title_text(first) or "Part"
    if a.part:
        title += f" part {a.part}"
    elif len(a.headings) > 1:
        title += f" and {len(a.headings) - 1} more"
    return title


def heading_keys(body: str) -> list[str]:
    lines = body.splitlines(keepends=True)
    heads = headings(lines)
    cuts = sorted({i for lv in SPLIT_LEVELS for i in heads.get(lv, [])})
    texts = [HEADING.match(lines[i].rstrip("\r\n")).group(2).rstrip("# ").strip() for i in cuts]
    kmap = key_map(texts)
    return [kmap[t] for t in texts]


def findability(plan: "Plan", texts: dict | None = None, entry: str | None = None) -> tuple[int, int, list[str]]:
    """How many ## and ### heading keys are an article title or a key on a catalog or index line, read from the files."""
    keys = heading_keys(plan.body)
    texts = dict(texts if texts is not None else plan.files)
    titles = " ".join((field(split_frontmatter(t)[0], "title") or "").lower() for n, t in texts.items() if n in plan.articles)
    pages = "\n".join(split_frontmatter(t)[1].lower() for n, t in texts.items() if n not in plan.articles)
    if plan.entry:
        pages += "\n" + split_frontmatter(entry if entry is not None else plan.entry[1])[1].lower()
    missing = [k for k in keys if k not in titles and not re.search(rf"(?<![a-z0-9-]){re.escape(k)}(?![a-z0-9-])", pages)]
    return len(keys) - len(missing), len(keys), missing


def what_the_style(arts: list[Article]) -> int:
    """Names built from a heading's first words rather than its key: a what-the prefix, or one base name shared by
    sections whose headings differ (the same heading listed twice, as an entry under Open and Decided, is one key)."""
    by_base = {}
    for a in arts:
        by_base.setdefault(a.base, set()).add(a.headings[0] if a.headings else "")
    shared = sum(1 for a in arts if len(by_base[a.base]) > 1)
    return shared + sum(1 for a in arts if a.name.startswith("what-the-"))


# --- describing the articles -------------------------------------------------------------------------------------
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


def entry_line(file: str, title: str, keys: list, sentence: str, cap: int) -> str:
    t = " ".join(title.split()[:8])
    s = " ".join(sentence.split()[:cap]) if cap else ""
    k = ", ".join(keys)                     # the keys are never shortened: they make each heading section findable
    return f"- [{t}]({file})" + (f" - {k}" if k else "") + (f" - {s}" if s else "") + "\n"


def fit_page(entries: list[tuple], budget: int, counter: Counter, caps=(14, 10, 6)) -> str | None:
    for cap in caps:   # an INDEX is never titles-only: it paginates instead; an entry page may be
        text = "".join(entry_line(f, t, k, s, cap) for f, t, k, s in entries)
        if counter.words(text) <= budget:
            return text
    return None


def layout(entries: list[tuple], budget: int, counter: Counter, now: str, doc_title: str,
           back: tuple = ("index", "INDEX.md"), top_caps=(14, 10, 6)) -> tuple[str, dict]:
    """The entry lines for INDEX.md within `budget` words and, when they do not fit, the catalog pages below it."""
    text = fit_page(entries, budget, counter, top_caps)
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
            first, last = (g[0][2][0] if g[0][2] else g[0][1]), (g[-1][2][-1] if g[-1][2] else g[-1][1])
            body = (f"\n# {title}\n\n{len(g)} entries of {plain(doc_title)}, from {first} to {last}. "
                    f"Back to the [{back[0]}]({back[1]}).\n\n" + fit_page(g, CATALOG_BUDGET, counter))
            pages[name] = front(title, f"{title} of the split {plain(doc_title)}", now, "1.0.0") + body
            upper.append((name, title, [], f"{first} to {last}"))
        level = upper
        text = fit_page(level, budget, counter, top_caps)
        if text is not None:
            return text, pages
    raise Refused("the document has too many articles for three index levels")


def front(title: str, description: str, now: str, version: str, sequence: int | None = None) -> str:
    seq = f"sequence: {sequence}\n" if sequence else ""
    return (f"---\ntitle: {title_text(title)}\ncreated: {now}\nmodified: {now}\nversion: {version}\n{seq}"
            f"description: {title_text(description)}\n---\n")


# --- the plan ----------------------------------------------------------------------------------------------------
class Plan:
    def __init__(self):
        self.files: list[tuple[str, str]] = []     # (name, full text), INDEX.md last
        self.articles: list[str] = []
        self.body = ""
        self.target = 0
        self.index_words = 0
        self.what_the = 0
        self.entry: tuple[str, str] | None = None   # --keep-entry: (the original file name, the generated entry page)


def build(original: str, stem: str, counter: Counter, now: str, keep: str | None = None, doc_name: str = "",
          example: str = "entry-20261123-01") -> Plan:
    plan = Plan()
    frontmatter, body = split_frontmatter(original)
    plan.body = body
    arts, plan.target = keyed_articles(body, counter)
    plan.what_the = what_the_style(arts)
    entries = []
    for n, art in enumerate(arts, 1):
        title = article_title(art)
        description = first_sentence(art.text, 25) or title
        plan.files.append((art.name, front(title, description, now, "0.1.0", n) + art.text))
        plan.articles.append(art.name)
        entries.append((art.name, title, art.keys, first_sentence(art.text, 14)))
    doc_title = field(frontmatter, "title") or next(
        (plain(HEADING.match(l.rstrip("\r\n")).group(2)) for l in body.splitlines() if HEADING.match(l)), stem)
    full = plain(field(frontmatter, "description") or "")
    summary = " ".join(full.split()[:25]) + ("..." if len(full.split()) > 25 else ".") if full else ""
    version = bump_minor(field(frontmatter, "version"))
    if frontmatter:
        fm = frontmatter
        fm = re.sub(r"(?m)^version:.*$", f"version: {version}", fm, count=1) if field(fm, "version") is not None else \
            fm.replace("\n---", f"\nversion: {version}\n---", 1)
        fm = re.sub(r"(?m)^modified:.*$", f"modified: {now}", fm, count=1) if field(fm, "modified") is not None else fm
    else:
        fm = front(doc_title, summary or f"Split from {stem}", now, "0.1.0")
    if keep:
        howto = (f"## Adding an entry\n\nAdd one small article file `{keep}/<entry-id>.md`, named by an entry id that starts "
                 f"with letters (for example `{example}.md`), with the frontmatter fields title, created, modified, version "
                 f"and description, then add one line for it at the end of this page: `- [Title]({keep}/{example}.md) one "
                 f"sentence`. Never edit an existing article.\n\n")
        intro = (f"\n# {doc_title}\n\n{summary + ' ' if summary else ''}This register stays at this path as an entry page; "
                 f"its text was split verbatim into {len(arts)} articles in [{keep}]({keep}/INDEX.md), unchanged and in "
                 f"reading order.\n\n{howto}## Articles\n\n")
        budget = INDEX_LIMIT - counter.words(intro) - HEADROOM - 8     # headroom: room for the lines added later
        lines, pages = layout(entries, budget, counter, now, doc_title, back=("register page", f"../{doc_name}"),
                              top_caps=(14, 10, 6, 0))
        lines = re.sub(r"\]\(([^)]+\.md)\)", lambda m: f"]({keep}/{m.group(1)})", lines)
        plan.files += list(pages.items())
        plan.entry = (doc_name, fm + intro + lines)
        plan.index_words = counter.file_words(plan.entry[1])
        shown = plain(doc_title)
        plan.files.append(("INDEX.md", front(f"{shown} log", f"Articles of the {shown} register, split verbatim; the register "
                                             f"page lists them", now, "1.0.0") +
                           f"\n# {shown} log\n\nThe articles of [{shown}](../{doc_name}), split verbatim from the "
                           f"original in reading order. The register page lists every article and says how to add one; "
                           f"later entries are single files named by entry id, for example `{example}.md`.\n"))
        return plan
    intro = (f"\n# {doc_title}\n\n{summary + ' ' if summary else ''}This document was split verbatim into {len(arts)} "
             f"articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original "
             f"body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) "
             f"or heading; each line gives the title, the keys the article holds and its first sentence.\n\n")
    budget = INDEX_LIMIT - counter.words(intro) - 8
    lines, pages = layout(entries, budget, counter, now, doc_title)
    plan.files += list(pages.items())
    index = fm + intro + lines
    plan.index_words = counter.file_words(index)
    plan.files.append(("INDEX.md", index))
    return plan


def verify(plan: Plan, counter: Counter, written: dict[str, str] | None = None, written_entry: str | None = None) -> list[str]:
    """Problems found re-reading the files (as rendered, or as written): empty when the proof holds."""
    texts = dict(written if written is not None else plan.files)
    problems, joined = [], ""
    for name in plan.articles:
        joined += split_frontmatter(texts[name])[1]
    if joined != plan.body:
        problems.append("the article bodies do not concatenate to the original body")
    names = [n for n, _ in plan.files]
    if len(set(names)) != len(names):
        problems.append("two files share a name")
    for i, name in enumerate(plan.articles, 1):
        if field(split_frontmatter(texts[name])[0], "sequence") != str(i):
            problems.append(f"{name}: sequence is not {i}")
    found, total, missing = findability(plan, texts, written_entry)
    if missing:
        problems.append(f"{len(missing)} heading key(s) not findable, first {missing[:3]}")
    for name, text in texts.items():
        if name != "INDEX.md" and not NAME.match(name[:-3]):
            problems.append(f"{name}: name does not match the kebab-case rule")
        limit = INDEX_LIMIT if name == "INDEX.md" else ARTICLE_LIMIT
        words = counter.file_words(text)
        if words > limit:
            problems.append(f"{name}: {words} words, limit {limit}")
    if len(texts) != len(plan.files):
        problems.append("file count differs from the plan")
    if plan.entry:
        entry = written_entry if written_entry is not None else plan.entry[1]
        words = counter.file_words(entry)
        if words > INDEX_LIMIT:
            problems.append(f"entry page {plan.entry[0]}: {words} words, limit {INDEX_LIMIT}")
        prose = re.sub(r"`[^`]*`", "", split_frontmatter(entry)[1])      # an example link in code is no link
        for target in re.findall(r"\]\(([^)#]+)\)", prose):
            if "/" in target and target.split("/", 1)[1] not in texts:
                problems.append(f"entry page links to a missing file: {target}")
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
    keep = args.keep_entry
    if keep:
        if is_index:
            raise Refused(f"{path}: --keep-entry applies to a single-file document, not INDEX.md")
        if not NAME.match(keep) or keep == path.stem:
            raise Refused(f"--keep-entry {keep!r}: a kebab-case name of 2 to 4 words, different from {path.stem!r}")
    folder = (path.parent / keep) if keep else (path.parent if is_index else path.with_suffix(""))
    stem = path.parent.name if is_index else path.stem
    plan = build(original, stem, counter, now, keep, path.name, args.entry_example)
    problems = verify(plan, counter) if (args.verify or args.apply) else []
    sizes = [counter.file_words(t) for n, t in plan.files if n in plan.articles]
    original_words = counter.m.count_words(original)
    pages = len(plan.files) - len(plan.articles) - 1
    label = f"entry page {path.name}" if keep else "INDEX.md"
    verdict = "not run (pass --verify)" if not (args.verify or args.apply) else ("FAIL: " + "; ".join(problems) if problems else
              f"PASS, article bodies rebuild the original body byte for byte (sha256 {hashlib.sha256(plan.body.encode()).hexdigest()[:12]})")
    print(f"{path}: {original_words:,} body words -> {len(plan.articles)} articles (max {max(sizes)} words, packed to {plan.target}), "
          f"{label} {plan.index_words} words, {pages} catalog page(s); target folder {folder}")
    print(f"  verify: {verdict}")
    found, total, _ = findability(plan)
    print(f"  findability: {found}/{total} ## and ### heading keys are an article title or a catalog line key "
          f"({100 * found / total if total else 100:.0f} percent); what-the-style names: {plan.what_the}; "
          f"distinct names {len(set(plan.articles))}/{len(plan.articles)}")
    refs = inbound_references(repo_top(path), path)
    if keep:
        print(f"  --keep-entry: {path.name} stays as the entry page, so the {len(refs)} file(s) citing it keep working")
    elif refs:
        print(f"  inbound references to {path.parent.name}/{path.name} in {len(refs)} file(s), first {refs[:5]}; they need updating after the move")
    if is_index:
        print("  INDEX.md keeps its path; links to headings inside it may break")
    if args.list:
        if plan.entry:
            print(f"    {counter.file_words(plan.entry[1]):4d}  {plan.entry[0]} (entry page)")
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
    entry_tmp = path.with_name(f".{path.name}.split-doc-new") if plan.entry else None
    try:
        for name, text in plan.files:
            (staging / name).write_bytes(text.encode("utf-8"))
        written = {n: (staging / n).read_bytes().decode("utf-8") for n, _ in plan.files}
        written_entry = None
        if entry_tmp:
            entry_tmp.write_bytes(plan.entry[1].encode("utf-8"))
            written_entry = entry_tmp.read_bytes().decode("utf-8")
        problems = verify(plan, counter, written, written_entry)
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
            if entry_tmp:
                os.replace(entry_tmp, path)     # the original path becomes the generated entry page
                entry_tmp = None
            else:
                os.remove(path)
    finally:
        if staging is not None:
            shutil.rmtree(staging, ignore_errors=True)
        if entry_tmp is not None and entry_tmp.exists():
            entry_tmp.unlink()
    what = "kept as the entry page" if plan.entry else ("replaced" if is_index else "removed")
    print(f"  applied: {len(plan.files)} files in {folder}; verified from disk; original {what}")
    return 0


def check_folder(folder: Path, against: Path, counter: Counter) -> int:
    if not folder.is_dir() or not against.is_file():
        raise SplitError("--check needs a split folder and the original file (for example from git show)")
    parts = []
    for n in os.listdir(folder):
        if n.endswith(".md"):
            front, body = split_frontmatter((folder / n).read_bytes().decode("utf-8"))
            seq = field(front, "sequence")
            if seq and seq.isdigit():          # later entries carry no sequence: they are not original text
                parts.append((int(seq), body))
    joined = "".join(body for _, body in sorted(parts))
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
    p.add_argument("--keep-entry", metavar="LOGDIR", help="keep the original path as a small entry page and put the articles in "
                   "the sibling folder LOGDIR (kebab-case, 2 to 4 words), so no reference to the path breaks")
    p.add_argument("--entry-example", default="entry-20261123-01", help="an example entry id shown in the entry page (default %(default)s)")
    p.add_argument("--check", nargs=2, metavar=("FOLDER", "ORIGINAL"), help="verify an applied split against a copy of the original")
    p.add_argument("--reflection", help="the reflection checkout (default ~/dtadpole/reflection or LINT_GATE_REFLECTION)")
    args = p.parse_args(argv)
    try:
        counter = Counter(load_counter(args.reflection))
        if args.check:
            return check_folder(Path(args.check[0]), Path(args.check[1]), counter)
        if not args.paths:
            p.error("name at least one document")
        if args.keep_entry and len(args.paths) != 1:
            p.error("--keep-entry takes exactly one document")
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
