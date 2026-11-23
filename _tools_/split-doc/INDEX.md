---
title: Split Doc
created: 2026-11-23T05:46:29Z
modified: 2026-11-23T05:58:54Z
version: 1.2.0
description: Verbatim, section-aware splitter that turns an oversized Markdown document into an index plus short articles
---

# Split doc

Target metric (IMP-20261123-03): documents over 500 words split without losing a word, every heading section findable.

```
python3 _tools_/split-doc/split_doc.py DOCUMENT.md [--keep-entry LOGDIR] [--verify] [--list] [--apply]
python3 _tools_/split-doc/split_doc.py --check FOLDER ORIGINAL.md
```

## Two forms

- **Folder form**: `register.md` becomes `register/`; an `INDEX.md` document keeps its folder and gains its articles.
- **Entry form** (`--keep-entry register-log`): the original path stays as a generated entry page of 300 words or fewer, so no reference breaks; the articles go to the sibling folder `register-log/`. Its version bumps one minor.

## Articles

Each `##` and `###` heading section starts its own article of at most 450 words; only consecutive tiny sections (120 words or fewer) share one, and an oversize section is cut at paragraph or item boundaries into `-p1`, `-p2` parts (`-part-N` would break the 4-word name rule). Names come from the heading key: an entry id (`od-20261123-03`), a unit key (`run-20261107-1824`), a day (`day-20261105`), else a slug. Titles read times as HHMM.

Every key sits beside its article link on a catalog or index line; the dry run reports findability and what-the-style names. Bodies are exact slices, so in `sequence` order they equal the original body byte for byte.

## Adding an entry later (entry form)

Add one small article `register-log/<entry-id>.md`, an id starting with letters, such as `od-20261123-04`, with title, created, modified, version and description (no `sequence`). Append one line at the end of the entry page: `- [Title](register-log/<entry-id>.md) one sentence`.

## Safety

Dry run by default; `--apply` stages, verifies from disk, then replaces or removes the original. `--check` re-proves a split against a copy of the original, ignoring later entries. It touches only the named file and never overwrites.
