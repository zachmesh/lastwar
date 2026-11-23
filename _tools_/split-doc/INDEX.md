---
title: Split Doc
created: 2026-11-23T05:46:29Z
modified: 2026-11-23T05:51:21Z
version: 1.1.0
description: Verbatim, section-aware splitter that turns an oversized Markdown document into an index plus short articles
---

# Split doc

Target metric (IMP-20261123-03): documents over 500 words, split without losing a word.

```
python3 _tools_/split-doc/split_doc.py DOCUMENT.md [--keep-entry LOGDIR] [--verify] [--list] [--apply]
python3 _tools_/split-doc/split_doc.py --check FOLDER ORIGINAL.md
```

## Two forms

- **Folder form** (default): `register.md` becomes `register/`; an `INDEX.md` document keeps its folder and gains its articles beside it.
- **Entry form** (`--keep-entry register-log`): the original path stays as a generated entry page of 300 words or fewer, so no reference breaks. The articles go to the sibling folder `register-log/` (kebab-case, 2 to 4 words, not the document's own name). The entry page's version bumps one minor.

## What it writes

- An index or entry page, with catalog pages when the articles outnumber what it holds. The entry page keeps 60 words of headroom.
- Articles of at most 450 body words, `001-first-words.md`, cut at headings, then at paragraph, item, row, line, sentence and word boundaries. Bodies are exact slices, so in order they equal the original body byte for byte; each gets generated frontmatter.

## Adding an entry later (entry form)

Add one small article `register-log/<entry-id>.md`, an id that starts with letters such as `od-20261123-04`, with title, created, modified, version and description. Append one line at the end of the entry page: `- [Title](register-log/<entry-id>.md) one sentence`. Never edit an existing article.

## Safety

Dry run by default. `--apply` stages, verifies from disk, then replaces or removes the original. `--verify` proves a dry run; `--check` re-proves a split against a copy of the original (`git show HEAD:path`), ignoring later entries. It touches only the named file, and refuses directories, symlinks, existing folders and any overwrite.

Counts use the linter's counter (`--reflection`). Exit 0 ok, 1 refused, 2 cannot run.
