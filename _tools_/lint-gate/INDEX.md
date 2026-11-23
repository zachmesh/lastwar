---
title: Lint Gate
created: 2026-11-23T04:50:00Z
modified: 2026-11-23T08:35:35Z
version: 1.10.0
description: Commit gate for size, structure and account privacy over the reflection convention linter, with a record-length check
---

# Lint gate

Targets: document-concision errors (IMP-20261123-03); owner account identifiers (OD-20261123-04). Linter:
`~/dtadpole/reflection`.

| Command | Does | Exit |
|---|---|---|
| `check --staged` | Blocks a document at 500 words, a new folder without `INDEX.md`, a new file in a type folder, an exempt entry added, or a privacy denylist hit in added lines or a file name. | 0 ok, 1 blocked, 2 cannot run |
| `check --base REF` | The same against REF. | same |
| `install [--dry-run] [--force]` | Sets `core.hooksPath` to `hooks/`: both hooks (`pre-commit`, `pre-merge-commit`) run `check --staged`. | 0, 1 refused |
| `watch` | Documents over 300 and 500 words by folder. | 0 |
| `watch --privacy [--worktree] [--accept]` | Files and lines per folder per pattern at HEAD; counts only. | 0, 1, 2 |
| `redact PATH... [--apply] [--verify] [--report-all] [--allow-outside]` | Replaces each match with its `# marker:` text in whole files; counts per file, pattern, profile; refuses records, `.git/`, binaries, unmarked patterns. | 0, 1, 2 |
| `redact --verify-diff [--base REV]` | Proves each changed file is a pure substitution. | 0, 1 |
| `record-check PATH...` | Body words; exit 1 at 480. | 0, 1, 2 |
| `stub-index [--apply]` | `INDEX.md` stubs for today's records folders. | 0 |
| `exempt-prune [--apply]` | Lists or removes exempt entries that exempt nothing. | 0 |

## Rules

- `exempt.txt` only shrinks: an entry added or reworded blocks; `_activities_` has none.
- Privacy: the untracked `.git/privacy-denylist.txt` holds one case-insensitive regular expression per line, matching across line wraps, with annotation lines before it: `# expect-min N` (fresh clones), `# marker: TEXT` (for `redact`). `watch --privacy` records `.git/privacy-census.json`: then counts may fall; only a drop to zero from over 10 files fails (`--accept`). No output shows a match.
- Redaction-only exemption: a staged file that `--verify-diff` proves is only the substitution (bar `version:` and `modified:` outside records) is exempt from the size rule, per file; other changes are judged normally.
- Exit 2: hooks warn and allow. Rollback: `git config --unset core.hooksPath`. Tests: `python3 -m unittest discover -s _tools_/lint-gate`.
