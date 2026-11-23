---
title: Lint Gate
created: 2026-11-23T04:50:00Z
modified: 2026-11-23T04:50:00Z
version: 1.0.0
description: Commit gate and size trigger over the reflection convention linter, with a record-length check
---

# Lint gate

Target metric (IMP-20261123-03): new or changed document-concision errors, 5 at
2026-11-23T04:36Z, 0 for the next 10 records. Run from the repository root with
the python3 that runs the linter; the linter is read from `~/dtadpole/reflection`
(`--reflection` or `LINT_GATE_REFLECTION` overrides).

| Command | Does | Exit |
|---|---|---|
| `check --staged` | Judges the commit in about a second; blocks a new or changed document at 500 words or more, a new folder without `INDEX.md`, or a new file in a type folder. | 0 ok, 1 blocked, 2 cannot run |
| `check --base REF` | The same against REF with a full lint (about a minute); for review and CI. | same |
| `install [--dry-run] [--force]` | Sets `core.hooksPath` to `hooks/`, whose pre-commit hook runs `check --staged`. | 0, 1 refused |
| `watch` | Prints counts over 300 and 500 words (legacy versus new, by top folder), the 10 largest documents and any document that grew more than 20 percent since the last run; writes a summary to `_tools_/state/lint-baseline.json`. | 0 |
| `record-check PATH...` | Prints body words; exits 1 at 480 or more so a record is trimmed before it closes a unit. | 0, 1, 2 |

## Rules

- Legacy findings never block: a document already at or over 500 words, a folder already lacking `INDEX.md` and a file already in a type folder are all measured against the base commit.
- `exempt.txt` lists globs the size check skips: today the append-only day indexes.
- `watch` keeps its anchor (the commit whose oversized documents count as legacy) in the baseline; `--anchor REF` resets it. A new error above 0 assigns the owning seat a fix.
- An environment failure exits 2; the hook then warns and allows the commit.
- Rollback: `git config --unset core.hooksPath`. Tests: `python3 -m unittest discover -s _tools_/lint-gate`.
