---
title: Split Doc
created: 2026-11-23T05:46:29Z
modified: 2026-11-23T05:46:29Z
version: 1.0.0
description: Verbatim, section-aware splitter that turns an oversized Markdown document into an index plus short articles
---

# Split doc

Target metric (IMP-20261123-03): documents over 500 words, split without losing a word.

```
python3 _tools_/split-doc/split_doc.py DOCUMENT.md [--verify] [--list] [--apply]
python3 _tools_/split-doc/split_doc.py --check FOLDER ORIGINAL.md
```

## What it does

A document becomes a folder named like it: `register.md` becomes `register/`. A document already called `INDEX.md`
keeps its folder and gets its articles beside it.

- `INDEX.md` of 300 words or fewer: what it is, how to find an entry, and one line per article with its first
  sentence. When the articles outnumber what one index holds, `catalog-NN.md` pages sit below it.
- Articles of at most 450 body words, numbered `001-first-words.md`, cut at headings first (`##`, then `###` and
  below), then at paragraph, list-item, table-row, line, sentence and word boundaries. Code fences stay whole when
  they fit.
- Article bodies are exact slices, so concatenated in order they equal the original body byte for byte. Each gets
  generated frontmatter at version 0.1.0; the original frontmatter stays on `INDEX.md`, version bumped one minor.

## Safety

- Dry run by default; `--apply` writes into a staging folder, verifies the files from disk, then removes the original.
- `--verify` prints the byte-for-byte proof for a dry run. `--check` re-proves an applied split against a copy of the
  original (for example `git show HEAD:path`).
- It touches only the files named. It refuses directories, symbolic links, non-Markdown files, an existing target
  folder and any file it would overwrite.
- Inbound references to the old path are counted; they need updating after the move.

Word counts come from the convention linter's counter (`--reflection` or `LINT_GATE_REFLECTION`). Exit 0 ok, 1
refused or failed, 2 cannot run. Tests: `python3 -m unittest discover -s _tools_/split-doc`.
