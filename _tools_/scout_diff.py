#!/usr/bin/env python3
"""Scout diff - the diff of the perception layer as a program.

Implements the Phase 2 tool design of the perception-driven queue
(_conventions_/local-conventions/perception-driven-queue.md,
sections 5, 6 and 9). A scout pass observes the game and writes
its observed items into the day observation file; this tool reads
that observation, diffs it against the modelled work - the
regulars profile library, the _activities_ roster with its
candidate register, and the pool itself - and produces four
outputs in an output directory:

  1. the enqueue plan (JSONL, one queue.py enqueue argument set
     per line) for the triggered execution units and for the
     exploration units of new candidates;
  2. the candidate filings - one provisional _activities_ profile
     draft per unknown item or unmatched label not already in the
     register;
  3. the coverage report - items observed, actionable, queued,
     already satisfied, not actionable with reasons, candidates,
     unexplained red dots, and the day unmatched_labels printed
     in full (an empty list is printed as empty, never omitted);
     plus the observation frontmatter day counters (passes
     completed, items observed, red dots seen, explained and
     unexplained), reported separately from the classified
     counts, and the per-pass red-dot accounting sections of
     a narrative observation, reconciled section total
     against frontmatter counter. When no structured item
     was parsed at all, the headline items and unexplained
     figures fall back to those
     frontmatter counts (basis recorded as frontmatter-fallback,
     classified counts kept alongside), so a narrative-only
     observation never reads as zero unexplained when its own
     frontmatter says otherwise; when the frontmatter carries
     no unexplained counter either, the headline unexplained
     figure falls back one more tier to the sum of the
     narrative accounting sections stating a count (basis
     recorded as narrative-fallback, with the caveat that
     chained passes may re-state the same dot, so the sum is
     a section total, not a distinct-dot count - the report
     also carries the distinct named dots parsed from the
     counted unexplained lines, with sections stating no
     countable names counted separately, so the distinct
     figure is a floor); a structured
     observation is never overridden, and the narrative seen
     total is never used as items observed, because seen
     counts red-dot signals, not observed items;
  4. the promotion proposals - one entry per registered
     candidate with a completed exploration unit in the pool,
     naming the exploration evidence and the decision owed
     (promote, reject, or keep exploring). A proposal never
     applies itself: promotion or rejection is a metadata edit
     made by the knowledge organizer or the owner, never by
     this tool, and the proposal never blocks the next
     exploration unit the plan enqueues;
  5. the round-summary section - the perception coverage
     scoreboard as one short section, written to be pasted
     verbatim into the day round summary (roadmap Phase 3).
     It carries no new numbers: every figure is copied from
     the coverage counts computed above, including the
     frontmatter day counters when the observation carries
     them, and when the pool was not read (--root absent) it
     says the promotion proposals were not checked instead
     of reporting zero as a finding.

Without --apply the tool is a dry run: it writes its outputs and
changes nothing in any pool. With --apply it feeds the plan's
enqueue entries to _tools_/queue.py enqueue, one call per unit, so
every unit it creates passes the same validation as a manual
enqueue - and --apply refuses to run unless the pool root is
given explicitly with --root. --root accepts a pool directory or
a repository root, resolved to its _queue_ folder (issue #510);
--apply refuses a root holding no pool state directory, so a
wrong root fails loudly instead of writing units into a fresh
empty directory nobody reads. A dry run against a root holding
no pool state directory prints the same pool_root_warning
queue.py prints, so its counts never silently describe an
empty pool (issue #537).

Idempotency: produced units dedupe on (regular, planned_for)
exactly as sync and plan do, and dynamic units carry their
source observation item (date, surface, label) in their window
text, which the tool checks before enqueueing. The dedupe also
consults today's delivered records branch (issue #466): a unit
already closed on the branch whose inbox copy the plan already
dropped is reported already-queued instead of re-enqueued, and
an exploration already closed on the branch today is not staged
again. The dedupe also reads the shared main-checkout pool's
done/ records (issue #533): a slot the ticker already closed in
the live pool - whose delivery has not landed on the records
branch yet - is reported already-queued instead of re-enqueued,
so a stale observation cannot re-enqueue a reward claimed after
it was read. A second run over the same observation reports every
entry as already queued and applies zero new units.

Priority: the formula of section 5 of the perception design -
deadline pressure times value over expected duration - mapped
onto the queue priority classes 1 to 4. Deadline pressure is 1
with no deadline and rises to 8 as the time left approaches the
band of one unit duration plus one retry; inside that band the
unit is priority 1, expiry-critical. Value is the base 10 log of
the largest figure the observation shows for the item, or a
state default when it shows none. Exploration units are fixed
at priority 2 under the design.

Usage:
  scout_diff.py --observation FILE [--date YYYY-MM-DD]
                [--out DIR] [--root POOL] [--repo DIR]
                [--regulars FILE] [--ledger FILE]
                [--now ISO] [--apply] [--format text|json]

Pool reads (the dedupe checks and the learned estimates) happen
only when --root names a pool or a repository root resolved to
its _queue_ folder; without it the diff runs against
an empty pool view. The observation, regulars, activities roster
and ledger default to the repository this tool lives in
(override with --repo).
"""

import argparse
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))


def _load_queue():
    spec = importlib.util.spec_from_file_location(
        "lastwar_queue", os.path.join(TOOLS_DIR, "queue.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q = _load_queue()
parse_iso = Q.parse_iso
iso = Q.iso
LOCAL_TZ = Q.LOCAL_TZ

ACTIONABLE_STATES = ("claimable", "doable")
KNOWN_STATES = ACTIONABLE_STATES + ("in-progress", "locked",
                                    "info-only")
VALUE_DEFAULTS = {"claimable": 2.0, "doable": 1.5,
                  "in-progress": 1.0, "locked": 1.0, "info-only": 0.5}


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0)


# ---------------------------------------------------------------------
# Observation parsing
# ---------------------------------------------------------------------

def _clean_value(text):
    text = text.strip()
    if len(text) >= 2 and text.startswith('"') and \
            text.endswith('"'):
        return text[1:-1]
    return text


def _parse_items_block(lines, start):
    """Parse one observed_items block sequence starting just after
    its key line. Returns (items, next_index)."""
    items = []
    current = None
    i = start
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"^(\s*)- (.*)$", line)
        if m:
            current = {}
            items.append(current)
            rest = m.group(2)
            fm = re.match(r"^([a-z_]+): (.*)$", rest)
            if fm:
                current[fm.group(1)] = _clean_value(fm.group(2))
            i += 1
            continue
        fm = re.match(r"^\s+([a-z_]+): (.*)$", line)
        if fm and current is not None:
            current[fm.group(1)] = _clean_value(fm.group(2))
            i += 1
            continue
        break
    return items, i


def _strip_inline_comment(text):
    """Drop a trailing ``# ...`` YAML comment (issue #527).

    A comment starts at a ``#`` preceded by whitespace; a ``#``
    glued to a word is part of the value.
    """
    return re.split(r"\s+#", text, maxsplit=1)[0].strip()


def _is_empty_list_marker(text):
    """True when a label line is the prose form of an empty list.

    Day observations write an empty unmatched list as a bare
    ``unmatched_labels: none`` or as a block line ``- none (...)``
    with a parenthetical explanation (issue #527). Either form means
    no label, so it must not reach the candidate classifier as a
    slug like ``none-builders-hut-quest``. ``empty`` is the same
    marker. A real label such as ``nonexistent-thing`` does not
    match: the marker word must end the text or be followed by a
    space, an opening parenthesis, or sentence punctuation
    (``none.``, ``empty:`` - issue #536).
    """
    lowered = _strip_inline_comment(text).lower()
    if lowered in ("none", "empty"):
        return True
    return bool(re.match(r"^(none|empty)([\s(]|[.,;:!?])", lowered))


def _parse_labels_block(lines, start):
    """Parse one unmatched_labels value - an inline flow list, a
    plain scalar, or a block list of scalars."""
    labels = []
    i = start
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^\s*- (.+)$", line)
        if m and not line.lstrip().startswith("- surface"):
            text = m.group(1).strip()
            if not _is_empty_list_marker(text):
                labels.append(text)
            i += 1
            continue
        break
    return labels, i


def parse_observation_text(text):
    """Collect every observed_items block and unmatched_labels list
    in a Markdown or YAML text - frontmatter, fenced blocks and
    body blocks all count, because a day observation file is
    appended to by every pass of the day."""
    items, labels = [], []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("observed_items:"):
            found, i = _parse_items_block(lines, i + 1)
            items.extend(found)
            continue
        if stripped.startswith("unmatched_labels:"):
            rest = stripped.split(":", 1)[1].strip()
            if rest.startswith("["):
                inner = rest.strip("[]").strip()
                if inner:
                    labels.extend(x.strip() for x in
                                  inner.split(",") if x.strip() and
                                  not _is_empty_list_marker(x))
                i += 1
                continue
            if rest:
                rest = _strip_inline_comment(rest)
                if not _is_empty_list_marker(rest):
                    labels.append(rest)
                i += 1
                continue
            found, i = _parse_labels_block(lines, i + 1)
            labels.extend(found)
            continue
        i += 1
    seen = set()
    unique = []
    for item in items:
        key = (item.get("surface", ""), item.get("label", ""),
               item.get("state", ""))
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique, sorted(set(labels))


def parse_observation_json(doc):
    items, labels = [], []

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "observed_items" and \
                        isinstance(value, list):
                    items.extend(v for v in value
                                 if isinstance(v, dict))
                elif key == "unmatched_labels" and \
                        isinstance(value, list):
                    labels.extend(str(v) for v in value
                                  if not _is_empty_list_marker(str(v)))
                else:
                    walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(doc)
    return items, sorted(set(labels))


def load_observation(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if path.endswith(".json"):
        return parse_observation_json(json.loads(text))
    try:
        doc = json.loads(text)
        if isinstance(doc, dict):
            return parse_observation_json(doc)
    except ValueError:
        pass
    return parse_observation_text(text)


# ---------------------------------------------------------------------
# Observation day counters - the observation's own accounting
# ---------------------------------------------------------------------

DAY_COUNTER_KEYS = ("passes_completed", "items_observed",
                    "red_dots_seen", "red_dots_explained",
                    "unexplained_red_dots")


def _counter_value(value):
    """A day counter is a non-negative int, or None when absent.

    Absent or malformed values read as None, never as zero: an
    absent counter is unknown, not a finding.
    """
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value >= 0:
        return value
    if isinstance(value, float) and value.is_integer() \
            and value >= 0:
        return int(value)
    if isinstance(value, str) and value.strip().isdigit():
        return int(value.strip())
    return None


def day_counters_from_fields(fields):
    return {key: _counter_value(fields.get(key))
            for key in DAY_COUNTER_KEYS}


def load_day_counters(path):
    """Read the observation's own day counters, if it carries any.

    Text observations carry them in the leading frontmatter
    block (the design's day counters); JSON observations carry
    them as top-level keys. This reads only the observation's
    own accounting - it classifies nothing, enqueues nothing
    and files nothing, so a narrative-only observation keeps
    its dots visible instead of collapsing to a classified
    zero.
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    try:
        doc = json.loads(text)
    except ValueError:
        doc = None
    if isinstance(doc, dict):
        return day_counters_from_fields(doc)
    fields, _ = Q.parse_frontmatter(text)
    return day_counters_from_fields(fields)


# ---------------------------------------------------------------------
# Narrative red-dot accounting - the per-pass accounting sections
# ---------------------------------------------------------------------

ACCOUNTING_KEYS = ("seen", "explained", "unexplained")
ACCOUNTING_FRONTMATTER = {
    "seen": "red_dots_seen",
    "explained": "red_dots_explained",
    "unexplained": "unexplained_red_dots",
}
# Words a scope qualifier may carry between the accounting
# keyword and the count. A qualifier states where the count
# applies ("within the base group alone"), never a dot or a
# counter: a dot word (badge, dot, icon, toast, chest) or a
# counter word would make the following number an identifier
# ("the badge 2"), not a count, so such a word ends the
# qualifier and the line reads as nameless instead of
# inventing a count. At most six qualifier words: the
# attested form carries five.
_ACCOUNTING_QUALIFIER_WORD = (
    r"(?!badge|badges|dot|dots|icon|icons|toast|toasts|"
    r"counter|counters|chest|chests\b)[a-z]+")
_ACCOUNTING_LINE = re.compile(
    r"^-\s*(seen|explained|unexplained)"
    r"(?:\s+red\s+dots?)?"
    r"(?P<qualifier>(?:\s+" + _ACCOUNTING_QUALIFIER_WORD + r"){0,6}?)"
    r"\s*:?\s*(?P<count>\d+)\b",
    re.IGNORECASE)

# A heading may carry a pass's whole accounting in itself
# ("Red dots - 8 seen, 6 explained, 2 unexplained", attested
# 2026-11-10): the counts live in the heading and the bullets
# below it list the items, so the heading starts the section
# with its counts already stated. The hyphen form is the only
# attested one; an em-dash or a bare "Red dots 8 seen" heading
# does not match, and reads as no section rather than a guess.
_HEADING_COUNTS = re.compile(
    r"^#{1,6}\s*red\s+dots?\s*-\s*(?P<seen>\d+)\s+seen\s*,"
    r"\s*(?P<explained>\d+)\s+explained\s*,"
    r"\s*(?P<unexplained>\d+)\s+unexplained\b",
    re.IGNORECASE)


def parse_narrative_accounting(text):
    """Per-pass red-dot accounting sections of a narrative
    observation, in file order. A section starts at a heading
    naming red dot accounting and ends at the next heading;
    its Seen, Explained and Unexplained lines carry that
    pass's own counts, in either the bare form ("Seen 3:")
    or the spelled-out form ("Unexplained red dots: 0.").
    A count may also carry a scope qualifier between the
    keyword and the number ("Unexplained within the base
    group alone 2:"), of at most six digit-free words that
    name no dot and no counter; the qualifier is why the
    2026-11-04 observation's two base-group lines read at
    all. A qualifier followed by digits and then a colon
    and another bare number ("in group 2: 3 dots") is not
    a count: the digits were a scope identifier, so the
    line reads as nameless. Names are taken from a counted
    line under the same qualifier rule as its count (a
    compound "X badges A and B" item splits into two
    names), so a qualified line can name its dots too;
    a line whose names still cannot be counted stays
    unnamed, and the distinct figure stays a floor.
    A heading may instead carry the whole accounting
    ("Red dots - 8 seen, 6 explained, 2 unexplained",
    attested 2026-11-10): the heading starts the section
    with its counts already stated, and the "- Unexplained:"
    bullet below it names the dots against the heading's
    count. Bullet lines never overwrite heading counts -
    an "- Explained: hammer 1/4 ..." bullet is a queue
    indicator, not a count - and the names are taken from
    the bullet's item list with its parentheticals stripped
    before splitting, so a comma inside a parenthesis
    ("(carried from 2026-11-09, badge moved 13 to 1)")
    never splits an item in two.
    A count a section does not state reads as None, never
    as zero - a line naming a dot without a number (for
    example "Unexplained: the Alliance Wars dot") states
    no count and invents none, so the same dot re-stated
    by a later pass is never counted twice by inference -
    and a carried-forward line (for example "Carried
    unexplained from ...") is not a count line, so carried
    dots are never double-counted. Structured items are
    untouched: this reads the narrative's own accounting
    only, so the coverage report can reconcile it against
    the frontmatter day counters instead of presenting
    either figure unexamined."""
    sections = []
    current = None
    unexplained_text = None

    def _finalize(section, bullet_text):
        if section is None or "unexplained_names" in section:
            return
        section["unexplained_text_present"] = \
            bullet_text is not None
        if section.get("heading_counted"):
            section["unexplained_names"] = (
                _heading_counted_unexplained_names(
                    bullet_text, section.get("unexplained"))
                if bullet_text else [])
        else:
            section["unexplained_names"] = (
                _counted_unexplained_names(bullet_text)
                if bullet_text else [])

    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped.startswith("#"):
            _finalize(current, unexplained_text)
            unexplained_text = None
            if "red dot accounting" in stripped.lower():
                current = {key: None for key in ACCOUNTING_KEYS}
                sections.append(current)
            else:
                heading = _HEADING_COUNTS.match(stripped)
                if heading:
                    current = {
                        key: int(heading.group(key))
                        for key in ACCOUNTING_KEYS}
                    current["heading_counted"] = True
                    sections.append(current)
                else:
                    current = None
            continue
        if current is None:
            continue
        if unexplained_text is not None:
            if raw[:1].isspace() and stripped and \
                    not stripped.startswith("-"):
                unexplained_text += " " + stripped
                continue
            _finalize(current, unexplained_text)
            unexplained_text = None
        m = None
        if not current.get("heading_counted"):
            # Heading-counted sections already carry their
            # counts: a bullet must never overwrite them -
            # "- Explained: hammer 1/4 ..." would otherwise
            # read its queue indicator as explained 1.
            m = _ACCOUNTING_LINE.match(stripped)
            if m:
                qualifier = (m.group("qualifier") or "").strip()
                rest = stripped[m.end():]
                if qualifier and re.match(r"\s*:\s*\d", rest):
                    # The digits were a scope identifier, not the
                    # count ("Unexplained in group 2: 3 dots"):
                    # the real count follows the colon. Inventing
                    # the identifier as the count would be worse
                    # than stating none, so the line reads as
                    # nameless.
                    m = None
        if m:
            current[m.group(1).lower()] = int(m.group("count"))
            if m.group(1).lower() == "unexplained":
                unexplained_text = stripped
        elif re.match(r"-\s*unexplained\b", stripped,
                      re.IGNORECASE):
            # A nameless unexplained line states no count and
            # names nothing, but it is still a signal: the
            # section counts as unnamed, never as absent.
            unexplained_text = stripped
    _finalize(current, unexplained_text)
    return sections


_DOT_NAME_EXCLUDE = re.compile(
    r"(no owning|filed as|issue #|maps? to|plus counters?"
    r"|\bcounter\b|unlocated|unwalked|carried|belonging to)",
    re.IGNORECASE)


def _normalize_dot_name(item):
    """One dot name, spelling-normalised, never merged by sense.

    Parentheticals and a trailing explanation clause are cut,
    a leading "the" and a trailing dot/badge word are stripped,
    and case and spacing are flattened - so "Alliance dot"
    and "Alliance red dot" both read "alliance", while
    "Alliance Wars dot" stays a different name. Near-duplicate
    spellings the normaliser does not merge stay separate and
    are shown in the name list, so a reader can merge by eye
    instead of the tool inventing an identity.
    """
    item = re.sub(r"\([^)]*\)", "", item)
    item = item.split(" - ")[0]
    item = item.strip().strip(".").strip()
    if item.lower().startswith("the "):
        item = item[4:].strip()
    lowered = item.lower()
    for suffix in (" red dot", " dot", " badges", " badge"):
        if lowered.endswith(suffix):
            item = item[: -len(suffix)].strip()
            break
    return " ".join(item.lower().split())


# A compound dot item: one shared base naming two dots by
# number ("left-column badges 2 and 1", attested 2026-11-04).
# The base word is singularised so the two names differ only
# in their number; a pair is the only attested form, so three
# or more numbers name nothing rather than guessing.
_COMPOUND_DOTS = re.compile(
    r"^(?P<base>.+?)\s+(?P<word>badges?|dots?|icons?)\s+"
    r"(?P<n1>\d+)\s+and\s+(?P<n2>\d+)$",
    re.IGNORECASE)


def _compound_dot_names(raw_item):
    """Two names from one compound dot item, or None.

    The item is the raw comma-piece before normalising, so the
    shared base and both numbers are still visible; each half
    is normalised on its own, so the usual exclusions and the
    word cap still apply to each name.
    """
    m = _COMPOUND_DOTS.match(raw_item.strip().strip(".").strip())
    if not m:
        return None
    word = m.group("word").lower()
    if word.endswith("s"):
        word = word[:-1]
    names = []
    for num in (m.group("n1"), m.group("n2")):
        item = _normalize_dot_name(
            "%s %s %s" % (m.group("base"), word, num))
        if not item or _DOT_NAME_EXCLUDE.search(item):
            return None
        if len(item.split()) > 6:
            return None
        names.append(item)
    return names


def _counted_unexplained_names(bullet_text):
    """Names from one counted unexplained line, or [].

    Only a line stating a count and a colon list names dots,
    and only when the kept items equal the stated count:
    a trailing explanation clause ("no owning regular",
    "belonging to groups the successor walks"), a filing
    note ("filed as Issue #212") or a counters tail
    ("plus 2 counters ...") would otherwise invent a dot,
    so a line whose items do not add up to its count names
    nothing. The count accepts the same scope qualifier as
    the accounting parser ("Unexplained within the base
    group alone 2:"), with the same guard: when the digits
    follow a qualifier and a colon plus another number
    ("in group 2: 3 dots"), the digits were a scope
    identifier, not the count, so the line names nothing.
    A compound item ("left-column badges 2 and 1") splits
    into two names, each counted. A nameless line names
    nothing by the same rule - its prose is not parsed for
    names - and a zero count is a definite statement, not
    an unnamed section.
    """
    m = re.search(
        r"unexplained(?:\s+red\s+dots?)?"
        r"(?P<qualifier>(?:\s+" + _ACCOUNTING_QUALIFIER_WORD +
        r"){0,6}?)\s*:?\s*(?P<count>\d+)\b",
        bullet_text, re.IGNORECASE)
    if not m:
        return []
    count = int(m.group("count"))
    if count == 0:
        return []
    rest = bullet_text[m.end():]
    qualifier = (m.group("qualifier") or "").strip()
    if qualifier and re.match(r"\s*:\s*\d", rest):
        # The digits were a scope identifier, not the count.
        return []
    rest = rest.lstrip(": ").strip()
    rest = re.sub(r"\bplus\b[^,;]*counters?\b.*$", "", rest,
                  flags=re.IGNORECASE)
    kept = []
    for raw_item in re.split(r"[,;]", rest):
        compound = _compound_dot_names(raw_item)
        if compound is not None:
            kept.extend(compound)
            continue
        item = _normalize_dot_name(raw_item)
        if not item or _DOT_NAME_EXCLUDE.search(item):
            continue
        if len(item.split()) > 6:
            continue
        kept.append(item)
    return kept if len(kept) == count else []


def _heading_counted_unexplained_names(bullet_text, count):
    """Names from a heading-counted unexplained bullet, or [].

    The heading already stated the count ("Red dots - 8 seen,
    6 explained, 3 unexplained"), so this bullet only has to
    name that many dots: its items are split on commas and
    semicolons after the parentheticals are stripped, because
    a parenthetical may itself carry a comma ("(carried from
    2026-11-09, badge moved 13 to 1)") that is not an item
    separator. A trailing countdown tail ("with 00:00:47
    countdown") and the base-screen location tail ("on the
    base screen") name the sighting, not the dot, so they are
    cut before normalising; an empty-list marker ("none",
    "empty") names nothing. The usual exclusions and the
    six-word cap still apply to each name, and a list whose
    kept items do not equal the heading count names nothing,
    exactly like the counted-line rule.
    """
    if not bullet_text or count is None or count == 0:
        return []
    _lead, _sep, rest = bullet_text.partition(":")
    rest = rest.strip()
    if not rest:
        return []
    rest = re.sub(r"\([^)]*\)", "", rest)
    kept = []
    for raw_item in re.split(r"[,;]", rest):
        item = raw_item.strip().strip(".").strip()
        item = re.sub(
            r"\s+with\s+\d{1,2}:\d{2}(?::\d{2})?\s+countdown\s*$",
            "", item, flags=re.IGNORECASE)
        item = re.sub(
            r"\s+on\s+the\s+base\s+screen\s*$",
            "", item, flags=re.IGNORECASE)
        compound = _compound_dot_names(item)
        if compound is not None:
            kept.extend(compound)
            continue
        name = _normalize_dot_name(item)
        if not name or name in ("none", "empty"):
            continue
        if _DOT_NAME_EXCLUDE.search(name):
            continue
        if len(name.split()) > 6:
            continue
        kept.append(name)
    return kept if len(kept) == count else []


def distinct_unexplained_dots(sections):
    """Distinct named unexplained dots across sections.

    Returns None when no section states an unexplained count
    or carries an unexplained bullet at all - no signal, not
    a zero. Otherwise the union of the counted lines' names,
    so a dot re-stated by a chained pass counts once, plus
    the sections that stated unexplained dots without
    countable names: the distinct figure is a floor, and
    the unnamed count says how far below a total it may sit.
    """
    signal = [s for s in sections
              if s.get("unexplained") is not None
              or s.get("unexplained_text_present")]
    if not signal:
        return None
    names = set()
    for section in signal:
        names.update(section.get("unexplained_names", []))
    unnamed = sum(
        1 for s in signal
        if not s.get("unexplained_names")
        and s.get("unexplained") != 0)
    return {"distinct": len(names), "names": sorted(names),
            "unnamed_sections": unnamed,
            "signal_sections": len(signal)}


def narrative_accounting_summary(sections, day_counters):
    """Totals and frontmatter reconciliation for parsed
    accounting sections. A total is the sum over the sections
    that state that count, or None when no section states
    it; reconciliation per count is matches when the total
    equals the frontmatter counter, differs by N when both
    are stated and unequal, and not comparable otherwise."""
    totals = {}
    for key in ACCOUNTING_KEYS:
        stated = [s[key] for s in sections if s[key] is not None]
        totals[key] = sum(stated) if stated else None
    reconciliation = {}
    for key in ACCOUNTING_KEYS:
        front = day_counters.get(ACCOUNTING_FRONTMATTER[key])
        total = totals[key]
        if front is None or total is None:
            reconciliation[key] = "not comparable"
        elif total == front:
            reconciliation[key] = "matches"
        else:
            reconciliation[key] = f"differs by {total - front:+d}"
    return {"sections": sections, "totals": totals,
            "reconciliation": reconciliation}


def load_narrative_accounting(path):
    """Narrative accounting summary for one observation file.
    JSON observations carry no markdown accounting sections,
    so they read as an empty summary, never as an error."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    try:
        doc = json.loads(text)
    except ValueError:
        doc = None
    if isinstance(doc, dict):
        return narrative_accounting_summary([], {})
    return narrative_accounting_summary(
        parse_narrative_accounting(text),
        load_day_counters(path))


# ---------------------------------------------------------------------
# Roster - regulars, activities with their states, the ledger
# ---------------------------------------------------------------------

def normalize(text):
    text = re.sub(r"[^a-z0-9]+", "-", str(text).lower())
    return re.sub(r"-+", "-", text).strip("-")


def slugify(label):
    """A provisional folder name for a candidate label - 2 to 4
    kebab words, the repository instance naming rule."""
    words = [w for w in normalize(label).split("-") if w][:4]
    if not words:
        return "unknown-candidate"
    if len(words) == 1:
        words.append("task")
    return "-".join(words)


def load_regulars(path):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    return {r["id"]: r for r in doc.get("regulars", [])}


def load_roster(repo):
    """The _activities_ roster - folder name to its frontmatter
    title and status. The candidate register lives here: a folder
    whose status is candidate or exploring is a filed candidate,
    rejected is kept against rediscovery."""
    roster = {}
    base = os.path.join(repo, "_activities_")
    if not os.path.isdir(base):
        return roster
    for name in sorted(os.listdir(base)):
        index = os.path.join(base, name, "INDEX.md")
        if not os.path.isfile(index):
            continue
        with open(index, encoding="utf-8") as fh:
            fields, _ = Q.parse_frontmatter(fh.read())
        roster[name] = {"title": fields.get("title", name),
                        "status": fields.get("status", "")}
    return roster


def load_ledger_regulars(path, regular_ids):
    """The regulars the daily collection ledger names as producing
    units - read from its numbered lines, best effort."""
    if not path or not os.path.isfile(path):
        return set()
    found = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if re.match(r"^\d+\. ", line):
                for rid in regular_ids:
                    if re.search(r"\b" + re.escape(rid) + r"\b",
                                 line):
                        found.add(rid)
    return found


# ---------------------------------------------------------------------
# Classification and priority
# ---------------------------------------------------------------------

def extract_value(item):
    text = str(item.get("est_value_or_score", ""))
    numbers = []
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        try:
            numbers.append(float(m.group(0).replace(",", "")))
        except ValueError:
            pass
    if numbers:
        biggest = max(numbers)
        if biggest > 0:
            return math.log10(biggest)
    return VALUE_DEFAULTS.get(item.get("state", ""), 1.0)


def compute_priority(item, est_minutes, stamp):
    """The priority formula of the perception design, section 5,
    mapped onto the queue classes. Returns (priority, score)."""
    deadline = parse_iso(item.get("deadline", ""))
    pressure = 1.0
    if deadline:
        time_left = max(1.0, (deadline - stamp).total_seconds()
                        / 60.0)
        band = 2.0 * est_minutes        # one unit plus one retry
        if time_left <= band:
            return 1, float("inf")
        pressure = min(8.0, max(1.0, (8.0 * band) / time_left))
    score = pressure * extract_value(item) / max(1, est_minutes)
    if score >= 1.0:
        return 2, score
    if score >= 0.25:
        return 3, score
    return 4, score


def redline_blocked(item):
    text = str(item.get("redline_check", "")).lower()
    return text.startswith("blocked") or "owner-needed" in text \
        or "owner needed" in text


def classify(item, regulars, roster, reg_by_activity):
    """One observed item into exactly one class. Returns a dict
    with the class and the reason or owner where it applies."""
    label = str(item.get("label", "")).strip()
    state = str(item.get("state", "")).strip()
    suggested = str(item.get("suggested_unit", "")).strip()
    if not label or state not in KNOWN_STATES:
        return {"class": "unexplained",
                "reason": "missing label or unknown state"}
    if _is_empty_list_marker(label):
        return {"class": "not-actionable", "owner": "",
                "reason": "empty-list marker, not a label "
                          "(issue #536)"}
    if suggested and suggested != "new" and suggested in regulars:
        owner = suggested
    elif suggested and suggested != "new" and \
            suggested in reg_by_activity:
        owner = reg_by_activity[suggested]
    else:
        slug = slugify(label)
        if slug in roster:
            entry = roster[slug]
            if entry["status"] == "rejected":
                return {"class": "not-actionable", "owner": "",
                        "reason": "candidate previously rejected, "
                                  "kept against rediscovery"}
            if entry["status"] in ("candidate", "exploring"):
                return {"class": "candidate", "slug": slug,
                        "known_candidate": True}
            owner = reg_by_activity.get(slug, "")
            if not owner:
                return {"class": "not-actionable", "owner": "",
                        "reason": "profiled in the roster with no "
                                  "producing regular"}
        else:
            # Issue #505: an unknown slug is a discovery candidate
            # only when the item is something to do - a claimable or
            # doable task with no owning regular. A read-only item
            # (info-only, in-progress, locked) or a red-line-blocked
            # item is day evidence, not an unknown task: filing it
            # as a candidate mints exploration units for Total Power
            # totals, building-queue counts and absence notes, and
            # duplicates genuine discoveries under a second slug
            # (survey-center-tab beside survey-center).
            if state not in ACTIONABLE_STATES:
                reason = {"in-progress": "already under way",
                          "locked": "locked or not yet open - " +
                                    str(item.get("redline_check", "")),
                          "info-only": "read for the record, day "
                                       "evidence"}[state]
                return {"class": "not-actionable", "owner": "",
                        "reason": reason}
            if redline_blocked(item):
                return {"class": "not-actionable", "owner": "",
                        "reason": "red line - " +
                                  str(item.get("redline_check", ""))}
            return {"class": "candidate", "slug": slug,
                    "known_candidate": False}
    if redline_blocked(item):
        return {"class": "not-actionable", "owner": owner,
                "reason": "red line - " +
                          str(item.get("redline_check", ""))}
    if state in ACTIONABLE_STATES:
        return {"class": "actionable", "owner": owner}
    reason = {"in-progress": "already under way",
              "locked": "locked or not yet open - " +
                        str(item.get("redline_check", "")),
              "info-only": "read for the record, day evidence"
              }[state]
    return {"class": "not-actionable", "owner": owner,
            "reason": reason}


# ---------------------------------------------------------------------
# Pool reads - dedupe exactly as sync and plan do
# ---------------------------------------------------------------------

def pool_units(root):
    units = []
    if not root:
        return units
    for state in Q.STATES:
        units.extend(Q.list_units(root, state))
    return units


def marker_for(date, item):
    return (f"scout {date} - {item.get('surface', '')} - "
            f"{item.get('label', '')}")


def find_existing(units, regular, planned_iso, marker):
    """An existing unit covering this entry - by the (regular,
    planned_for) invariant, or by the dynamic source marker in
    its window text (same date, surface and label)."""
    for f in units:
        window = str(f.get("window", ""))
        if marker and marker in window:
            return f
        if planned_iso and f.get("regular") == regular and \
                f.get("planned_for") == planned_iso:
            return f
    return None


# ---------------------------------------------------------------------
# Candidate filing draft
# ---------------------------------------------------------------------

def candidate_draft(slug, label, surface, clues, stamp, date):
    title = " ".join(w.capitalize() for w in slug.split("-"))
    lines = ["---",
             f"title: {title}",
             f"created: {iso(stamp)}",
             f"modified: {iso(stamp)}",
             "level: L1",
             "version: 0.1.0",
             "description: Provisional candidate profile filed by "
             "the scout diff - mechanism not yet learned",
             "status: candidate",
             "grounded_in:",
             f"  - source: scout observation of {date}, surface "
             f"{surface}",
             "---",
             "",
             f"# {title}",
             "",
             "## What is known",
             "",
             f"- On-screen text transcribed - {label}",
             f"- Surface - {surface}",
             ]
    for clue in clues:
        lines.append(f"- Clue in hand - {clue}")
    lines += ["",
              "## Learning checklist",
              "",
              "The exploration unit fills these in from the "
              "task's own screens and the cross-checked sources "
              "of the learning protocol, marking each value "
              "measured or untested - entry point, mechanism, "
              "rewards, cost, cycle and deadline shape, whether "
              "it scores anywhere, and the live read that "
              "verifies it.",
              "",
              "## Red lines for exploration",
              "",
              "Exploration is read-only learning. Nothing priced "
              "is pressed, no diamonds are spent, and any rule "
              "that stays unclear keeps the candidate learn-only "
              "and named to the owner in the round summary.",
              "",
              "## Promotion path",
              "",
              "candidate, then exploring, then active once the "
              "mechanism is clear and inside the free and safe "
              "envelope, or rejected with the reason kept - the "
              "discovery protocol of the perception-driven queue "
              "design, section 6.",
              ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------
# Promotion proposals (Phase 3 slice)
# ---------------------------------------------------------------------

def exploration_done_units(units, slug):
    """Completed exploration units for one candidate slug, from
    any date. Exploration units carry their source in their
    window text - "scout <date> - exploration - <slug> - ..." -
    so the window marker, not the run date, is the match; a
    candidate explored on an earlier day is found by a later
    run instead of aging in silence."""
    needle = f"exploration - {slug} -"
    done = [f for f in units
            if f.get("_state") == "done"
            and needle in str(f.get("window", ""))]
    return sorted(done, key=lambda f: str(f.get("_file", "")))


def branch_exploration_slugs(root, branch, date):
    """Candidate slugs whose exploration already closed on the
    delivered records branch on this date (issue #466).

    The branch done set from queue.py names unit ids only, and an
    exploration unit id carries no slug - so the slug comes from
    the done unit's window text, which the diff itself wrote as
    "scout <date> - exploration - <slug> - ...". One git grep over
    the private ref the branch fetch already populated (queue.py
    records_branch_done_units) lists the window lines; only this
    date's slugs count, so a candidate explored on an earlier day
    still gets its next exploration unit. Returns (slugs, warning):
    warning is None on success, else a short reason - the caller
    warns and the run continues on local state only, as with the
    branch done set itself.
    """
    ref = "%s/%s" % (Q.BRANCH_RECONCILE_REF,
                     branch.replace("/", "-"))
    # The pathspec is relative to the pool dir this tool runs in -
    # the pool IS the _queue_ folder, so "done/" is _queue_/done/.
    # git grep has no ":/" top magic (it fails with "Unimplemented
    # pathspec magic"), so the repo-root-relative form cannot be
    # used here; scoping to done/ matters because the branch also
    # carries _records_ files that quote exploration windows of
    # units that were only planned, never closed.
    try:
        out = subprocess.run(
            ["git", "-C", root, "grep", "-h", "-F", "-e",
             "exploration - ", ref, "--", "done/"],
            capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return set(), ("branch exploration grep failed, "
                       "branch check skipped")
    if out.returncode not in (0, 1):
        return set(), ("branch exploration grep failed, "
                       "branch check skipped")
    slugs = set()
    needle = re.compile(
        r"scout (\d{4}-\d{2}-\d{2}) - exploration - "
        r"([a-z0-9-]+) -")
    for line in (out.stdout or "").splitlines():
        match = needle.search(line)
        if match and match.group(1) == date:
            slugs.add(match.group(2))
    return slugs, None


def shared_pool_done_units(root):
    """Unit ids closed in the shared main-checkout pool (issue #533).

    The worktree pool this diff runs against is a snapshot: a unit
    the ticker closed in the live pool lands in the worktree's
    done/ only when the next pool sync copies it, and on the
    delivered records branch only when its delivery lands - the
    1540 planner pass re-enqueued the VIP reward ticker-1518 had
    claimed seven minutes earlier because neither copy had
    arrived yet. The live pool itself is the main checkout's
    _queue_, reachable from any worktree through the same shared
    home queue.py uses for completion markers
    (Q.completion_home), so its done/ records are the ticker
    result the diff was missing. A file counts when it names its
    unit and carries a result status, mirroring
    Q._has_done_record: any result status (done, partial, failed,
    skipped-needs-owner, expired) means the unit already closed.
    Returns (ids, warning): warning is None on success; a shared
    home with no done/ directory simply holds no live
    completions, and an unreadable file is skipped, never fatal.
    """
    home = Q.completion_home(root)
    folder = os.path.join(home, "done")
    if not os.path.isdir(folder):
        return set(), None
    ids = set()
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        try:
            fields, _ = Q.read_unit(os.path.join(folder, name))
        except (OSError, ValueError, UnicodeDecodeError):
            continue
        unit = fields.get("unit")
        if not unit:
            continue
        result = fields.get("result", {})
        if isinstance(result, dict) and result.get("status"):
            ids.add(unit)
    return ids, None


def _result_text(result, key):
    if not isinstance(result, dict):
        return ""
    value = result.get(key, "")
    return "" if value is None else str(value)


def promotion_proposals(units, roster, candidates):
    """One proposal per registered candidate with a completed
    exploration unit. The proposal aggregates the exploration
    record - it never judges mechanism clarity itself, because
    the pool carries the exploration result, not the judgment:
    the decision owed is promote once the mechanism is clear
    and inside the free and safe envelope, reject with the
    reason kept if priced, red-lined, owner-only or not a task
    at all, and keep exploring otherwise. Candidates with no
    completed exploration unit get no proposal, and a proposal
    changes nothing in the pool or the roster."""
    slugs = set(candidates)
    for name, entry in roster.items():
        if entry.get("status") in ("candidate", "exploring"):
            slugs.add(name)
    proposals = []
    for slug in sorted(slugs):
        done = exploration_done_units(units, slug)
        if not done:
            continue
        rec = candidates.get(slug, {})
        entry = roster.get(slug, {})
        explorations = []
        for f in done:
            result = f.get("result", {})
            stats = result.get("stats", {}) \
                if isinstance(result, dict) else {}
            if not isinstance(stats, dict):
                stats = {}
            explorations.append({
                "file": f.get("_file", ""),
                "status": _result_text(result, "status"),
                "finished_at": _result_text(result,
                                            "finished_at"),
                "duration_seconds": _result_text(
                    result, "duration_seconds"),
                "summary": _result_text(result, "summary"),
                "evidence": _result_text(result, "evidence"),
                "follow_up": _result_text(result, "follow_up"),
                "stats": {str(k): str(v)
                          for k, v in stats.items()}})
        proposals.append({
            "slug": slug,
            "label": rec.get("label", "") or
                     entry.get("title", slug),
            "surface": rec.get("surface", "") or
                       "not observed in this pass",
            "register_status": entry.get("status", "") or
                               rec.get("status", ""),
            "observed_today": slug in candidates,
            "explorations": explorations})
    return proposals


# ---------------------------------------------------------------------
# Main diff
# ---------------------------------------------------------------------

def run(args):
    stamp = parse_iso(args.now) if args.now else now_utc()
    date = args.date
    if not date:
        m = re.search(r"(20\d\d-\d\d-\d\d)", args.observation)
        date = m.group(1) if m else stamp.astimezone(
            LOCAL_TZ).strftime("%Y-%m-%d")
    repo = os.path.abspath(args.repo)
    regulars_path = args.regulars or os.path.join(
        repo, "_tools_", "regulars.json")
    regulars = load_regulars(regulars_path)
    roster = load_roster(repo)
    reg_by_activity = {}
    for rid, item in regulars.items():
        if item.get("activity"):
            reg_by_activity[item["activity"]] = rid
    ledger_path = args.ledger
    if ledger_path is None:
        default_ledger = os.path.join(
            repo, "_conventions_", "local-conventions",
            "daily-collection-ledger.md")
        ledger_path = default_ledger if os.path.isfile(
            default_ledger) else ""
    ledger_regulars = load_ledger_regulars(ledger_path,
                                           set(regulars))
    items, unmatched = load_observation(args.observation)
    day_counters = load_day_counters(args.observation)
    narrative_accounting = load_narrative_accounting(
        args.observation)
    units = pool_units(args.root)
    now_local = stamp.astimezone(LOCAL_TZ)

    # Branch-closed consultation (issue #466): a unit closed on
    # today's delivered records branch whose inbox copy the plan
    # already dropped looks unqueued to this diff, so without this
    # the diff re-enqueues it - the planner 0840 run did exactly
    # that to six exploration units closed on the branch. The
    # closed set mirrors queue.py sync/plan: branch done ids plus
    # live completion markers. A branch that cannot be read warns
    # and the run continues on local state only.
    branch = ""
    branch_warning = None
    closed = set()
    branch_closed_ids = set()
    shared_done = set()
    branch_explored = set()
    branch_closed = []
    shared_closed = []
    if args.root:
        branch = "records/%s" % now_local.date().isoformat()
        branch_done, branch_warning = Q.records_branch_done_units(
            args.root, branch)
        if branch_warning is None:
            branch_explored, branch_warning = \
                branch_exploration_slugs(args.root, branch, date)
        if branch_warning:
            print(f"warning: {branch_warning} (issue #466)",
                  file=sys.stderr)
        closed = set(branch_done)
        for unit in Q.completion_marker_units(args.root):
            closed.add(unit)
        branch_closed_ids = set(closed)
        # Shared-pool done consultation (issue #533): the live
        # pool's done/ records close slots the delivered branch
        # has not seen yet - the 1540 pass re-enqueued the VIP
        # reward on exactly that gap. The worktree pool already
        # contributes its own done/ through pool_units, so only
        # the shared home adds anything here.
        shared_done, _ = shared_pool_done_units(args.root)
        closed |= shared_done

    actionable = {}          # (regular, planned_iso) -> entry
    candidates = {}          # slug -> candidate record
    not_actionable = []
    unexplained = []
    counts = {"info_satisfied": 0}

    def file_candidate(slug, label, surface, clues, from_item):
        # Issue #536: a slug in the empty-list family (none-*,
        # empty-*) is prose for "no unmatched labels", never a
        # discovery - a marker form the parser did not recognise
        # must not reach the register here either. A real label
        # survives: slugify("nonexistent-thing") is
        # "nonexistent-thing", not "none-*".
        if slug.startswith(("none-", "empty-")):
            return
        if slug in candidates:
            rec = candidates[slug]
            for clue in clues:
                if clue not in rec["clues"]:
                    rec["clues"].append(clue)
            return
        entry = roster.get(slug)
        candidates[slug] = {
            "slug": slug, "label": label, "surface": surface,
            "clues": list(clues),
            "registered": bool(entry),
            "status": entry["status"] if entry else "",
            "from_item": from_item}

    for item in items:
        verdict = classify(item, regulars, roster, reg_by_activity)
        cls = verdict["class"]
        if cls == "actionable":
            regular = verdict["owner"]
            profile = regulars[regular]
            est = Q.typical_minutes(args.root, regular)[0] \
                if args.root else Q.SYNC_EST_MINUTES.get(
                    regular, Q.DEFAULT_EST_MINUTES)
            priority, score = compute_priority(item, est, stamp)
            planned_local = Q.cycle_start_local(profile, now_local)
            planned_iso = iso(planned_local.astimezone(
                timezone.utc))
            key = (regular, planned_iso)
            entry = actionable.setdefault(key, {
                "regular": regular,
                "activity": profile.get("activity", ""),
                "segment": profile.get("segment", ""),
                "priority": priority, "score": score,
                "est_minutes": est, "planned_for": planned_iso,
                "expires_at": "", "items": []})
            entry["priority"] = min(entry["priority"], priority)
            entry["score"] = max(entry["score"], score)
            deadline = str(item.get("deadline", ""))
            if deadline and (not entry["expires_at"] or
                             deadline < entry["expires_at"]):
                entry["expires_at"] = deadline
            entry["items"].append(item)
        elif cls == "candidate":
            clues = []
            if item.get("deadline"):
                clues.append("visible deadline " +
                             str(item["deadline"]))
            if item.get("est_value_or_score"):
                clues.append("on-screen value " +
                             str(item["est_value_or_score"]))
            if item.get("redline_check"):
                clues.append("redline note " +
                             str(item["redline_check"]))
            file_candidate(verdict["slug"],
                           str(item.get("label", "")),
                           str(item.get("surface", "")), clues,
                           True)
        elif cls == "not-actionable":
            if str(item.get("state", "")) == "info-only":
                counts["info_satisfied"] += 1
            not_actionable.append({"item": item,
                                   "reason": verdict["reason"]})
        else:
            unexplained.append({"item": item,
                                "reason": verdict["reason"]})

    for label in unmatched:
        slug = slugify(label)
        entry = roster.get(slug)
        if entry and entry["status"] == "rejected":
            not_actionable.append({
                "item": {"label": label, "surface": "",
                         "state": "info-only"},
                "reason": "unmatched label previously rejected, "
                          "kept against rediscovery"})
            continue
        if slug in roster and roster[slug]["status"] not in (
                "candidate", "exploring"):
            continue            # already an owned profile
        file_candidate(slug, label, "unmatched label",
                       ["named on the unmatched labels list of " +
                        date], False)

    # Build the enqueue plan - execution entries first, then the
    # exploration entries under the discovery chain.
    plan = []
    for key in sorted(actionable,
                      key=lambda k: (actionable[k]["priority"], k)):
        entry = actionable[key]
        markers = [marker_for(date, it) for it in entry["items"]]
        existing = None
        for marker in markers:
            existing = find_existing(units, entry["regular"],
                                     entry["planned_for"], marker)
            if existing:
                break
        action = "enqueue"
        if existing:
            try:
                have = int(existing.get("priority", 3))
            except (TypeError, ValueError):
                have = 3
            action = "raise" if entry["priority"] < have \
                else "already-queued"
        elif closed:
            slot_unit = Q._unit_id_for_window(
                regulars[entry["regular"]],
                parse_iso(entry["planned_for"]).astimezone(
                    LOCAL_TZ))
            if slot_unit in closed:
                # The slot already closed on the delivered branch
                # (or by a live completion marker) - the live pool
                # holds no trace of it, but minting a fresh unit
                # would re-execute the slot (issue #466). A slot
                # closed only in the shared pool's done/ records
                # is the same suppression through the live pool
                # (issue #533). The two lists partition the
                # suppressions: branch_closed_ids (branch plus
                # markers) counts under branch_closed, a slot the
                # shared pool alone knew counts under
                # shared_closed, so the retro can see which input
                # saved each re-enqueue.
                action = "already-queued"
                if slot_unit in branch_closed_ids:
                    branch_closed.append(slot_unit)
                elif slot_unit in shared_done:
                    shared_closed.append(slot_unit)
        trigger = "claimable now"
        if entry["priority"] == 1:
            trigger = "deadline approaching, expiry band"
        window = "; ".join(markers)
        plan.append({
            "action": action, "kind": "execution",
            "regular": entry["regular"],
            "activity": entry["activity"],
            "segment": entry["segment"],
            "priority": entry["priority"],
            "expires_at": entry["expires_at"],
            "not_before": "", "planned_for": entry["planned_for"],
            "est_minutes": entry["est_minutes"],
            "window": f"{trigger} - {window}",
            "chain_id": "",
            "source_items": [
                {"surface": it.get("surface", ""),
                 "label": it.get("label", "")}
                for it in entry["items"]]})

    est_scout = Q.typical_minutes(args.root, "scout")[0] \
        if args.root else Q.SYNC_EST_MINUTES.get("scout", 10)
    for slug in sorted(candidates):
        rec = candidates[slug]
        label = rec["label"] or slug
        marker = f"scout {date} - exploration - {slug} - {label}"
        existing = find_existing(units, "scout", "", marker)
        action = "already-queued" if existing else "enqueue"
        if not existing and slug in branch_explored:
            # This candidate's exploration already closed on the
            # delivered branch today - the live pool holds no trace
            # of it, but staging a fresh exploration would repeat
            # the 0840 run's re-enqueue of the same six units
            # (issue #466).
            action = "already-queued"
            branch_closed.append(slug)
        plan.append({
            "action": action, "kind": "exploration", "regular": "scout",
            "activity": slug,
            "segment": regulars.get("scout", {}).get("segment",
                                                     ""),
            "priority": 2, "expires_at": "", "not_before": "",
            "planned_for": "",
            "est_minutes": est_scout,
            "window": marker + " - read-only learning, "
                              "red lines learn-only",
            "chain_id": f"scout-discovery-{date}",
            "source_items": [{"surface": rec["surface"],
                              "label": label}]})

    # Apply - one queue.py enqueue call per enqueue entry, only
    # against the explicitly given pool root.
    applied, apply_failures = [], []
    if args.apply:
        queue_py = os.path.join(TOOLS_DIR, "queue.py")
        for entry in plan:
            if entry["action"] != "enqueue":
                continue
            cmd = [sys.executable, queue_py, "--root", args.root,
                   "enqueue", "--regular", entry["regular"],
                   "--activity", entry["activity"] or "",
                   "--priority", str(entry["priority"]),
                   "--est-minutes", str(entry["est_minutes"]),
                   "--window", entry["window"]]
            if entry["segment"] != "":
                cmd += ["--segment", str(entry["segment"])]
            if entry["expires_at"]:
                cmd += ["--expires-at", entry["expires_at"]]
            if entry["not_before"]:
                cmd += ["--not-before", entry["not_before"]]
            if entry["chain_id"]:
                cmd += ["--chain-id", entry["chain_id"]]
            out = subprocess.run(cmd, capture_output=True,
                                 text=True)
            text = (out.stdout or "").strip()
            if out.returncode == 0 and text.startswith("queued"):
                applied.append(text.split(" ", 1)[1])
            elif "already queued" in text:
                entry["action"] = "already-queued"
            else:
                apply_failures.append(
                    {"entry": entry["regular"],
                     "output": text or out.stderr.strip()})

    # Promotion proposals - read-only aggregation over the pool
    # units already loaded above; without --root the pool is
    # unread, so no proposal can be grounded and none is made.
    proposals = promotion_proposals(units, roster, candidates) \
        if args.root else []

    # Outputs.
    out_dir = args.out or os.path.join(
        os.path.dirname(os.path.abspath(args.observation)),
        "scout-diff-output")
    os.makedirs(out_dir, exist_ok=True)
    plan_path = os.path.join(
        out_dir, f"scout-enqueue-plan-{date}.jsonl")
    with open(plan_path, "w", encoding="utf-8") as fh:
        for entry in plan:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

    cand_path = os.path.join(
        out_dir, f"scout-candidates-{date}.md")
    cand_lines = ["---",
                  f"title: Scout Candidate Filings {date}",
                  f"created: {iso(stamp)}",
                  "description: Provisional candidate profiles "
                  "the scout diff files for this date",
                  "---", "",
                  f"# Candidate filings - {date}", ""]
    if not candidates:
        cand_lines.append("No candidates filed for this date.")
    for slug in sorted(candidates):
        rec = candidates[slug]
        cand_lines.append(f"## {slug}")
        cand_lines.append("")
        if rec["registered"]:
            cand_lines.append(
                f"Already in the register with status "
                f"{rec['status']} - no new filing; the exploration "
                f"entry in the enqueue plan is its next unit.")
            cand_lines.append("")
            continue
        cand_lines.append(
            "Provisional profile draft - file as "
            f"`_activities_/{slug}/INDEX.md` -")
        cand_lines.append("")
        cand_lines.append("```markdown")
        cand_lines.append(candidate_draft(
            slug, rec["label"], rec["surface"], rec["clues"],
            stamp, date))
        cand_lines.append("```")
        cand_lines.append("")
    with open(cand_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(cand_lines))

    prom_path = os.path.join(
        out_dir, f"scout-promotions-{date}.md")
    prom_lines = ["---",
                  f"title: Scout Promotion Proposals {date}",
                  f"created: {iso(stamp)}",
                  "description: Promotion or rejection proposals "
                  "for candidates whose exploration completed - "
                  "proposals only, never applied by this tool",
                  "---", "",
                  f"# Promotion proposals - {date}", ""]
    if not args.root:
        prom_lines.append(
            "Pool not read (no --root), so completed "
            "explorations could not be checked and no proposal "
            "is grounded in this run.")
    elif not proposals:
        prom_lines.append(
            "No registered candidate has a completed "
            "exploration unit in the pool - no promotion "
            "decision is owed by this run.")
    for prop in proposals:
        prom_lines.append(f"## {prop['slug']}")
        prom_lines.append("")
        prom_lines.append(
            f"Label - {prop['label']}; surface - "
            f"{prop['surface']}; register status - "
            f"{prop['register_status']}; observed in this "
            f"pass - {'yes' if prop['observed_today'] else 'no'}.")
        prom_lines.append("")
        prom_lines.append(
            "Decision owed - promote to active once the "
            "mechanism is clear and inside the free and safe "
            "envelope, reject with the reason kept if priced, "
            "red-lined, owner-only or not a task at all, "
            "otherwise keep exploring. This proposal changes "
            "nothing: promotion or rejection is a metadata "
            "edit made by the knowledge organizer or the "
            "owner."
            + (" The next exploration unit in the enqueue "
               "plan is still enqueued, so a keep-exploring "
               "decision keeps its unit."
               if prop["observed_today"] else
               " No exploration unit is enqueued for it by "
               "this pass, since it was not observed today - "
               "a keep-exploring decision needs its next "
               "unit staged by the planner."))
        prom_lines.append("")
        for ex in prop["explorations"]:
            prom_lines.append(
                f"- exploration unit {ex['file']} - result "
                f"{ex['status'] or 'unrecorded'}"
                + (f", finished {ex['finished_at']}"
                   if ex["finished_at"] else "")
                + (f", {ex['duration_seconds']}s"
                   if ex["duration_seconds"] else ""))
            if ex["summary"]:
                prom_lines.append(f"  summary - {ex['summary']}")
            if ex["evidence"]:
                prom_lines.append(
                    f"  evidence - {ex['evidence']}")
            if ex["follow_up"]:
                prom_lines.append(
                    f"  follow-up - {ex['follow_up']}")
            if ex["stats"]:
                prom_lines.append(
                    "  stats - " + ", ".join(
                        f"{k}={v}"
                        for k, v in sorted(ex["stats"].items())))
        prom_lines.append("")
    with open(prom_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(prom_lines))

    to_enqueue = [e for e in plan if e["action"] == "enqueue"]
    already = [e for e in plan if e["action"] == "already-queued"]
    raises = [e for e in plan if e["action"] == "raise"]
    surfaces = {}
    for item in items:
        surfaces[item.get("surface", "")] = surfaces.get(
            item.get("surface", ""), 0) + 1
    unexplained_count = len(unexplained) + len(
        [lbl for lbl in unmatched
         if slugify(lbl) not in candidates
         and slugify(lbl) not in roster])
    # Coverage headline fallback (issue 149): with no structured
    # item parsed, the classified counts are 0 by construction,
    # not a finding, and the evaluation metric reads the
    # headline - so a narrative-only day would report 0 items
    # and 0 unexplained dots against its own accounting.
    # The headline then reports the observation's own
    # frontmatter counts first; when the frontmatter carries
    # no unexplained counter, the unexplained headline falls
    # back one more tier to the narrative accounting section
    # total (issue 149, 2026-11-03 shape: narrative sections
    # with no frontmatter counters at all). The narrative
    # seen total is never used as items observed: seen counts
    # red-dot signals, not observed items, so the items
    # headline stays the classified count on that tier. The
    # classified counts are kept alongside so the basis stays
    # auditable. A structured observation (at least one parsed
    # item) is never overridden, and an observation with
    # neither parsed items, frontmatter counters nor a stated
    # narrative unexplained total stays honestly empty.
    classified_items = len(items)
    classified_unexplained = unexplained_count
    headline_items = classified_items
    headline_unexplained = classified_unexplained
    frontmatter_used = False
    narrative_used = False
    if classified_items == 0:
        if day_counters["items_observed"] is not None:
            headline_items = day_counters["items_observed"]
            frontmatter_used = True
        if day_counters["unexplained_red_dots"] is not None:
            headline_unexplained = \
                day_counters["unexplained_red_dots"]
            frontmatter_used = True
        elif narrative_accounting["totals"]["unexplained"] \
                is not None:
            headline_unexplained = \
                narrative_accounting["totals"]["unexplained"]
            narrative_used = True
    if classified_items > 0:
        coverage_basis = "classified"
    elif frontmatter_used and narrative_used:
        coverage_basis = "frontmatter+narrative-fallback"
    elif frontmatter_used:
        coverage_basis = "frontmatter-fallback"
    elif narrative_used:
        coverage_basis = "narrative-fallback"
    else:
        coverage_basis = "empty"
    distinct = distinct_unexplained_dots(
        narrative_accounting["sections"])
    coverage = {
        "date": date, "observation": args.observation,
        "items_observed": headline_items,
        "items_observed_classified": classified_items,
        "coverage_basis": coverage_basis,
        "actionable_items": sum(len(e["items"]) for e in
                                actionable.values()),
        "queued_entries": len(plan),
        "to_enqueue": len(to_enqueue),
        "already_queued": len(already),
        "already_queued_branch_done": len(branch_closed),
        "branch_closed": sorted(branch_closed),
        "already_queued_shared_pool_done": len(shared_closed),
        "shared_pool_closed": sorted(shared_closed),
        "branch_done_reconcile_warning": branch_warning,
        "raises": len(raises),
        "applied": len(applied),
        "already_satisfied": counts["info_satisfied"],
        "not_actionable": len(not_actionable),
        "unknown_items": len([c for c in candidates.values()
                              if c["from_item"]]),
        "candidates_filed": len([c for c in candidates.values()
                                 if not c["registered"]]),
        "candidates_registered": len([c for c in
                                      candidates.values()
                                      if c["registered"]]),
        "unexplained_red_dots": headline_unexplained,
        "unexplained_red_dots_classified": classified_unexplained,
        "unexplained_distinct_dots": (
            distinct["distinct"] if distinct else None),
        "unexplained_distinct_names": (
            distinct["names"] if distinct else []),
        "unexplained_unnamed_sections": (
            distinct["unnamed_sections"] if distinct else 0),
        "observation_day_counters": day_counters,
        "narrative_accounting": narrative_accounting,
        "unmatched_labels": unmatched,
        "promotion_proposals": len(proposals),
        "outputs": {"enqueue_plan": plan_path,
                    "candidates": cand_path,
                    "promotions": prom_path},
    }
    cov_path = os.path.join(
        out_dir, f"scout-coverage-{date}.md")
    narrative_seen = narrative_accounting["totals"]["seen"]
    narrative_unexplained = \
        narrative_accounting["totals"]["unexplained"]
    if coverage_basis == "frontmatter-fallback":
        basis_note = (" (no structured observed_items parsed; "
                      "the items and unexplained figures above "
                      "are the observation frontmatter counts, "
                      f"classified items {classified_items}, "
                      "classified unexplained "
                      f"{classified_unexplained})")
    elif coverage_basis == "narrative-fallback":
        basis_note = (" (no structured observed_items parsed "
                      "and no frontmatter counters stated; "
                      "the unexplained figure above is the sum "
                      "of the narrative accounting sections "
                      "stating a count, so chained passes may "
                      "re-state the same dot and the sum is a "
                      "section total, not a distinct-dot "
                      "count; the items figure above is the "
                      "classified count, not a day total - "
                      "the narrative seen total is "
                      f"{narrative_seen} red-dot signals, not "
                      "observed items)")
    elif coverage_basis == "frontmatter+narrative-fallback":
        basis_note = (" (no structured observed_items parsed; "
                      "the items figure above is the "
                      "observation frontmatter count, the "
                      "unexplained figure above is the sum of "
                      "the narrative accounting sections "
                      "stating a count, so chained passes may "
                      "re-state the same dot and the sum is a "
                      "section total, not a distinct-dot "
                      "count)")
    elif coverage_basis == "empty":
        basis_note = (" (no structured items parsed and no "
                      "frontmatter counters stated; the zeros "
                      "above are an absence of signal, not a "
                      "finding)")
    else:
        basis_note = " (classified structured items)"
    if branch_warning:
        branch_line = (f"- branch done check unavailable - "
                       f"{branch_warning}; the diff ran on local "
                       f"state only")
    elif branch:
        branch_line = (
            f"- already closed on the delivered branch "
            f"{branch} - {len(branch_closed)} "
            f"entr{'y' if len(branch_closed) == 1 else 'ies'} "
            f"not re-enqueued")
    else:
        branch_line = ("- branch done check - not run: the pool "
                       "was not read (no --root), so a unit closed "
                       "on the branch could not be checked")
    if args.root:
        shared_line = (
            f"- already closed in the shared live pool's done/ "
            f"records - {len(shared_closed)} "
            f"entr{'y' if len(shared_closed) == 1 else 'ies'} "
            f"not re-enqueued (issue #533)")
    else:
        shared_line = ("- shared-pool done check - not run: the "
                       "pool was not read (no --root), so a unit "
                       "closed in the live pool could not be "
                       "checked")
    cov = ["---",
           f"title: Scout Coverage {date}",
           f"created: {iso(stamp)}",
           "description: Coverage report of the scout diff for "
           "this date",
           "---", "",
           f"# Scout coverage - {date}", "",
           f"Observation - {args.observation}", "",
           f"- items observed - {coverage['items_observed']}",
           f"- actionable items - {coverage['actionable_items']}",
           f"- queue entries produced - "
           f"{coverage['queued_entries']} (to enqueue "
           f"{coverage['to_enqueue']}, already queued "
           f"{coverage['already_queued']}, priority raises "
           f"{coverage['raises']}, applied this run "
           f"{coverage['applied']})",
           branch_line,
           shared_line,
           f"- already satisfied, read as day evidence - "
           f"{coverage['already_satisfied']}",
           f"- known, not actionable - "
           f"{coverage['not_actionable']}",
           f"- unknown items filed as candidates - "
           f"{coverage['unknown_items']} (new filings "
           f"{coverage['candidates_filed']}, already registered "
           f"{coverage['candidates_registered']})",
           f"- unexplained red dots - "
           f"{coverage['unexplained_red_dots']}",
           (f"- distinct unexplained dots (named, across "
            f"narrative sections; a floor when sections "
            f"below state no countable names) - "
            f"{coverage['unexplained_distinct_dots']}"
            + (f": {", ".join(
                coverage['unexplained_distinct_names'])}"
               if coverage['unexplained_distinct_names']
               else "")
            + (f" ({coverage['unexplained_unnamed_sections']} "
               f"section(s) without countable names)"
              if coverage['unexplained_unnamed_sections']
              else "")
            if coverage['unexplained_distinct_dots'] is not None
            else "- distinct unexplained dots - not stated "
                 "(no narrative unexplained section)"),
           f"- coverage basis - {coverage_basis}{basis_note}",
           f"- promotion proposals - "
           f"{coverage['promotion_proposals']} (registered "
           f"candidates with a completed exploration unit, "
           f"decision owed)"]
    cov += ["", "## Observation day counters", ""]
    if all(v is None for v in day_counters.values()):
        if narrative_used:
            cov.append("The observation carries no day counters "
                       "in its frontmatter - the unexplained "
                       "headline above is the narrative "
                       "accounting section total in the next "
                       "section, and the items figure is the "
                       "classified count only.")
        else:
            cov.append("The observation carries no day counters "
                       "in its frontmatter - the classified "
                       "counts above are the only signal, and "
                       "no day total is claimed.")
    else:
        for key in DAY_COUNTER_KEYS:
            value = day_counters[key]
            cov.append(f"- {key} - "
                       f"{value if value is not None else 'not stated'}")
        front_unexplained = day_counters["unexplained_red_dots"]
        if front_unexplained is not None:
            if coverage_basis == "frontmatter-fallback":
                cov.append(
                    "Headline fallback - the items and "
                    "unexplained figures above are these "
                    "frontmatter counts, because no structured "
                    "items were parsed; the classified counts "
                    f"are items {classified_items}, unexplained "
                    f"{classified_unexplained}.")
            elif front_unexplained == unexplained_count:
                cov.append("The frontmatter unexplained count "
                           "matches the classified count above.")
            else:
                cov.append(
                    f"Mismatch - the frontmatter reports "
                    f"{front_unexplained} unexplained red dots "
                    f"while {unexplained_count} were classified "
                    f"from structured items. The difference is "
                    f"narrative-only dots not yet filed as "
                    f"observed items: this run neither enqueues "
                    f"nor files them, and the classified count "
                    f"above is not the day total.")
    cov += ["", "## Narrative red-dot accounting", ""]
    if not narrative_accounting["sections"]:
        cov.append("No red-dot accounting section was found in "
                   "the observation narrative - the passes wrote "
                   "no per-pass Seen, Explained and Unexplained "
                   "counts to reconcile against the frontmatter.")
    else:
        for idx, section in enumerate(
                narrative_accounting["sections"], 1):
            parts = ", ".join(
                f"{key} "
                f"{section[key] if section[key] is not None else 'not stated'}"
                for key in ACCOUNTING_KEYS)
            cov.append(f"- pass section {idx} - {parts}")
        totals = narrative_accounting["totals"]
        cov.append("- totals over the sections stating each "
                   "count - " + ", ".join(
                       f"{key} "
                       f"{totals[key] if totals[key] is not None else 'not stated'}"
                       for key in ACCOUNTING_KEYS))
        for key in ACCOUNTING_KEYS:
            front = day_counters[ACCOUNTING_FRONTMATTER[key]]
            recon = narrative_accounting["reconciliation"][key]
            if recon == "matches":
                cov.append(f"- frontmatter {key} reconciles - "
                           f"the section total {totals[key]} "
                           f"equals the frontmatter count.")
            elif recon.startswith("differs"):
                cov.append(f"- frontmatter {key} mismatch - "
                           f"the section total {totals[key]} "
                           f"{recon} against the frontmatter "
                           f"count {front}; one of the two "
                           f"accountings is stale.")
            else:
                cov.append(f"- frontmatter {key} not comparable "
                           f"- the section total or the "
                           f"frontmatter count is unstated.")
    cov += ["", "## Promotion proposals", ""]
    if not args.root:
        cov.append("Pool not read (no --root) - completed "
                   "explorations could not be checked.")
    elif not proposals:
        cov.append("None.")
    for prop in proposals:
        cov.append(f"- {prop['slug']} - "
                   f"{len(prop['explorations'])} completed "
                   f"exploration unit(s), register status "
                   f"{prop['register_status']} - decision owed: "
                   f"promote, reject, or keep exploring.")
    cov += ["", "## By surface", ""]
    for surface in sorted(surfaces):
        cov.append(f"- {surface} - {surfaces[surface]}")
    cov += ["", "## Not actionable, with reasons", ""]
    if not not_actionable:
        cov.append("None.")
    for rec in not_actionable:
        cov.append(f"- {rec['item'].get('label', '')} - "
                   f"{rec['reason']}")
    cov += ["", "## Unexplained", ""]
    if not unexplained:
        cov.append("None.")
    for rec in unexplained:
        cov.append(f"- {rec['item'].get('label', '')} - "
                   f"{rec['reason']}")
    cov += ["", "## Unmatched labels", ""]
    if unmatched:
        for lbl in unmatched:
            cov.append(f"- {lbl}")
    else:
        cov.append("The unmatched labels list is empty - the "
                   "passes looked and found nothing outside the "
                   "roster.")
    ledger_unseen = sorted(ledger_regulars - {
        e["regular"] for e in plan} - {
        str(it.get("suggested_unit", "")) for it in items})
    cov += ["", "## Ledger cross-check", "",
            "Ledger producing regulars neither observed nor "
            "queued in this pass (informational - the floor "
            "cadence still covers them) - " +
            (", ".join(ledger_unseen) if ledger_unseen else
             "none")]
    cov.append("")
    with open(cov_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(cov))
    coverage["outputs"]["coverage"] = cov_path

    # Round-summary section - the Phase 3 standing section of
    # the day round summary, paste-ready. It derives every
    # figure from the coverage counts above and adds none of
    # its own, so it can never drift from the coverage report
    # it summarises. An empty observation is reported as no
    # observation, never as a coverage claim.
    exec_entries = [e for e in plan if e["kind"] == "execution"]
    expl_entries = [e for e in plan if e["kind"] == "exploration"]
    new_filings = [c for c in candidates.values()
                   if not c["registered"]]
    rs = ["---",
          f"title: Scout Round Summary Section {date}",
          f"created: {iso(stamp)}",
          "description: Perception coverage section, ready to "
          "paste verbatim into the day round summary - every "
          "figure copied from the coverage report of the same "
          "run, no new numbers",
          "---", "",
          f"## Perception coverage - {date}", ""]
    day_unexplained = day_counters["unexplained_red_dots"]
    narrative_total_unexplained = \
        narrative_accounting["totals"]["unexplained"]
    if coverage["items_observed"] == 0:
        if narrative_used:
            rs.append(
                f"No structured items were parsed, but the "
                f"narrative accounting sections total "
                f"{narrative_total_unexplained} unexplained "
                f"red dot(s) (sum of the sections stating a "
                f"count; chained passes may re-state the same "
                f"dot) - not zero.")
        elif day_unexplained is None and \
                day_counters["items_observed"] is None:
            rs.append("No items were observed in this pass, so "
                      "this section carries no coverage claim - "
                      "the passes, not the summary, are the gap "
                      "to check.")
        else:
            day_items_txt = str(day_counters["items_observed"]) \
                if day_counters["items_observed"] is not None \
                else "an unstated number of"
            day_unexp_txt = str(day_unexplained) \
                if day_unexplained is not None \
                else "an unstated number of"
            rs.append(
                f"No structured items were parsed, but the "
                f"observation frontmatter reports "
                f"{day_items_txt} items observed and "
                f"{day_unexp_txt} unexplained red dot(s) - "
                f"the pass is narrative-only and those dots "
                f"are unclassified, not zero.")
    elif coverage["unexplained_red_dots"] == 0:
        rs.append("Zero unexplained red dots.")
    else:
        rs.append(f"{coverage['unexplained_red_dots']} "
                  f"unexplained red dot(s) - the pass is "
                  f"partial until each is named below.")
    rs.append("")
    rs.append(f"- observed {coverage['items_observed']} items; "
              f"queue entries {coverage['queued_entries']} "
              f"({len(exec_entries)} execution, "
              f"{len(expl_entries)} exploration; to enqueue "
              f"{coverage['to_enqueue']}, already queued "
              f"{coverage['already_queued']}, priority raises "
              f"{coverage['raises']}, applied this run "
              f"{coverage['applied']}"
              + (f", branch-closed {len(branch_closed)}"
                 if branch_closed else "")
              + (f", shared-pool-closed {len(shared_closed)}"
                 if shared_closed else "")
              + f"); already satisfied "
              f"{coverage['already_satisfied']}, known not "
              f"actionable {coverage['not_actionable']}.")
    if coverage_basis == "frontmatter-fallback":
        rs.append("- coverage basis - frontmatter fallback: "
                  "no structured items were parsed, so the "
                  "observed and unexplained figures above are "
                  "the observation frontmatter counts, not "
                  "classified items.")
    elif coverage_basis == "narrative-fallback":
        rs.append("- coverage basis - narrative fallback: "
                  "no structured items were parsed and no "
                  "frontmatter counters stated, so the "
                  "unexplained figure above is the sum of the "
                  "narrative accounting sections stating a "
                  "count, not classified items; the observed "
                  "figure is the classified count.")
    elif coverage_basis == "frontmatter+narrative-fallback":
        rs.append("- coverage basis - frontmatter+narrative "
                  "fallback: no structured items were parsed; "
                  "the observed figure above is the "
                  "frontmatter count and the unexplained "
                  "figure above is the sum of the narrative "
                  "accounting sections stating a count.")
    elif coverage_basis == "empty":
        rs.append("- coverage basis - empty: no structured "
                  "items parsed and no frontmatter counters "
                  "stated, so the zeros above are an absence "
                  "of signal, not a finding.")
    if any(v is not None for v in day_counters.values()):
        parts = ", ".join(
            f"{key} {day_counters[key]}"
            for key in DAY_COUNTER_KEYS
            if day_counters[key] is not None)
        rs.append(f"- observation day counters (frontmatter, "
                  f"not classified items) - {parts}.")
        if day_unexplained is not None and \
                day_unexplained != coverage["unexplained_red_dots"]:
            rs.append(f"  - mismatch - frontmatter unexplained "
                      f"{day_unexplained} against classified "
                      f"{coverage['unexplained_red_dots']}: the "
                      f"difference is narrative-only dots not "
                      f"yet filed as observed items.")
    if narrative_accounting["sections"]:
        totals = narrative_accounting["totals"]
        recon = narrative_accounting["reconciliation"]
        rs.append("- narrative red-dot accounting - "
                  f"{len(narrative_accounting['sections'])} "
                  "pass section(s), totals " + ", ".join(
                      f"{key} "
                      f"{totals[key] if totals[key] is not None else 'not stated'}"
                      for key in ACCOUNTING_KEYS) + "; "
                  "frontmatter reconciliation - " + ", ".join(
                      f"{key} {recon[key]}"
                      for key in ACCOUNTING_KEYS) + ".")
    if distinct is not None:
        rs.append(
            f"- distinct unexplained dots named in narrative "
            f"sections - {distinct['distinct']}"
            + (f" ({", ".join(distinct['names'])})"
               if distinct["names"] else " (none named)")
            + (f"; {distinct['unnamed_sections']} section(s) "
               f"stated unexplained dots without countable "
               f"names, so this is a floor, not a total."
              if distinct["unnamed_sections"] else "."))
    rs.append(f"- unknown items - "
              f"{coverage['unknown_items']} filed as "
              f"candidates ({coverage['candidates_filed']} "
              f"new filings, "
              f"{coverage['candidates_registered']} already "
              f"registered).")
    for rec in sorted(new_filings, key=lambda c: c["slug"]):
        rs.append(f"  - new candidate {rec['slug']} - "
                  f"{rec['label'] or rec['slug']} "
                  f"({rec['surface']}).")
    if unmatched:
        rs.append("- unmatched labels - every label the "
                  "passes met that no roster entry owns:")
        for lbl in unmatched:
            rs.append(f"  - {lbl}")
    else:
        rs.append("- unmatched labels - none: the passes "
                  "looked and found nothing outside the "
                  "roster.")
    if not args.root:
        rs.append("- promotion proposals - not checked: the "
                  "pool was not read (no --root), so a zero "
                  "here would be an unread pool, not a "
                  "finding.")
    elif not proposals:
        rs.append("- promotion proposals - none owed: no "
                  "registered candidate has a completed "
                  "exploration unit in the pool.")
    else:
        rs.append("- promotion proposals - decision owed:")
        for prop in proposals:
            rs.append(f"  - {prop['slug']} - "
                      f"{len(prop['explorations'])} completed "
                      f"exploration unit(s), register status "
                      f"{prop['register_status']} - promote, "
                      f"reject, or keep exploring.")
    rs.append("")
    rs.append("Source - the coverage report and the "
              "promotion proposals file in the same output "
              "directory; this section adds no new numbers.")
    rs.append("")
    rs_path = os.path.join(
        out_dir, f"scout-round-summary-{date}.md")
    with open(rs_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(rs))
    coverage["outputs"]["round_summary"] = rs_path
    coverage["apply_failures"] = apply_failures
    coverage["applied_units"] = applied

    if args.format == "json":
        print(json.dumps(coverage, indent=2, ensure_ascii=False))
    else:
        print(f"scout diff for {date} - "
              f"observed {coverage['items_observed']}, "
              f"actionable {coverage['actionable_items']}, "
              f"to enqueue {coverage['to_enqueue']}, "
              f"already queued {coverage['already_queued']}, "
              f"raises {coverage['raises']}, "
              f"candidates {len(candidates)}, "
              f"unexplained red dots "
              f"{coverage['unexplained_red_dots']}, "
              f"promotion proposals "
              f"{coverage['promotion_proposals']}")
        print(f"outputs in {out_dir}")
        if branch_closed:
            print(f"branch-closed, not re-enqueued - "
                  f"{', '.join(sorted(branch_closed))}")
        if shared_closed:
            print(f"shared-pool-closed, not re-enqueued - "
                  f"{', '.join(sorted(shared_closed))} (issue #533)")
        if applied:
            print(f"applied {len(applied)} - "
                  f"{', '.join(applied)}")
        for failure in apply_failures:
            print(f"apply failed for {failure['entry']} - "
                  f"{failure['output']}")
    return 1 if apply_failures else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observation", required=True)
    parser.add_argument("--date", default="")
    parser.add_argument("--out", default="")
    parser.add_argument("--root", default="")
    parser.add_argument("--repo", default=os.path.join(
        TOOLS_DIR, ".."))
    parser.add_argument("--regulars", default="")
    parser.add_argument("--ledger", default=None)
    parser.add_argument("--now", default="")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--format", choices=["text", "json"],
                        default="text")
    args = parser.parse_args(argv)
    if args.apply and not args.root:
        parser.error("--apply requires --root naming the pool "
                     "explicitly")
    if args.root:
        args.root = os.path.abspath(args.root)
        args.root = Q.resolve_pool_root(args.root)
    if args.root:
        # A dry run against a wrong root used to report its counts
        # against an empty pool with nothing to show it never saw
        # the pool (issue #537): the 1640 planner pass read an
        # empty pool and filed phantom units before --apply refused.
        # Warn through the same pool_root_warning queue.py prints,
        # so the read path fails loudly too. --apply keeps its own
        # refusal below. The warning also fires on --apply: a
        # stray pool beside the resolved _queue_ pool (issue #539)
        # must be named on the write path too, so it gets removed
        # instead of silently ignored.
        warning = Q.pool_root_warning(args.root)
        if warning:
            print(warning, file=sys.stderr)
    if args.apply and not any(
            os.path.isdir(Q.state_dir(args.root, s))
            for s in Q.STATES):
        parser.error(f"--apply root {args.root} holds no inbox, "
                     "claimed or done directory - the pool was "
                     "not found, nothing applied (issue #510)")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
