---
title: Lint Gate
created: 2026-11-23T04:50:00Z
modified: 2026-11-25T22:14:42Z
version: 1.14.0
description: Commit gate for size, structure and account privacy over the reflection convention linter, with a record-length check
---

# Lint gate

Targets: document-concision (IMP-20261123-03), owner account identifiers (OD-20261123-04), playbook cards. Linter: `~/dtadpole/reflection`.

| Command | Does | Exit |
|---|---|---|
| `check --staged` | Blocks a document at 500 words, a new folder without `INDEX.md`, a new file in a type folder, an added exempt entry, a privacy hit, a broken playbook card. | 0 ok, 1 blocked, 2 cannot run |
| `check --base REF [--landing] [--list-ignored]` | Against REF. `--landing` (the Integrator): exit 2, never 0, if REF is unreadable, the denylist is missing or a rule crashes. `--list-ignored`: each ignored finding's path and rule. | same |
| `install [--dry-run] [--force]` | Sets `core.hooksPath`; both hooks run `check --staged`. | 0, 1 refused |
| `watch [--list]` | Counts, new and exempt paths. | 0 |
| `watch --privacy [--worktree] [--accept]` | Counts per folder and pattern at HEAD. | 0, 1, 2 |
| `redact PATH... [--apply] [--verify] [--report-all] [--allow-outside]` | Replaces matches with their `# marker:` text; counts only; refuses records, binaries, unmarked patterns. | 0, 1, 2 |
| `redact --verify-diff [--base REV]` | Proves each changed file is only a substitution. | 0, 1 |
| `record-check PATH...` | Body words; 1 at 480. | 0, 1, 2 |
| `stub-index [--apply]` | Stubs for today's records. | 0 |
| `exempt-prune [--apply]` | Drops entries that exempt nothing. | 0 |

## Rules

- `exempt.txt` only shrinks: an entry added or reworded blocks; `_activities_` has none.
- Paths git ignores (the queue's `completed/`) leave findings and counts.
- Privacy: the untracked `.git/privacy-denylist.txt` holds one case-insensitive regex per line, matching across line wraps; annotations `# expect-min N`, `# marker: TEXT`. `watch --privacy` records `.git/privacy-census.json`; a drop to zero from over 10 files fails (`--accept`). No output shows a match.
- Playbook cards: `playbook_check.py changed` checks changed `_activities_/<activity>/INDEX.md`; a lost shape or over 300 words blocks.
- A staged file `--verify-diff` proves is only a redaction (bar `version:`, `modified:` outside records) is exempt from the size rule.
- Exit 2: hooks warn and allow (`--landing` refuses). Rollback: `git config --unset core.hooksPath`. Tests: `python3 -m unittest discover -s _tools_/lint-gate`.
