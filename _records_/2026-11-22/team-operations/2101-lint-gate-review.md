---
title: Lint gate go-live review - 2026-11-22 21:01 PT
created: 2026-11-22T21:01:00-08:00
modified: 2026-11-22T21:03:00-08:00
level: L3
version: 0.1.0
description: Review and merge of the lint-gate go-live branch, the two decisions the toolsmith asked for, and the assignment that must land before the commit hook is installed
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2101-lint-gate-review
trigger: toolsmith reply on A-20261123-0455
started_at: 2026-11-22T21:00:00-08:00
finished_at: 2026-11-22T21:03:00-08:00
duration_seconds: 180
verified: diff scope checked, 27 tests re-run in a separate worktree, file names and tool rows compared before and after the index split
---

# Lint gate go-live review

## Review

- Branch `work/lint-gate-golive` (`fe8cf5a4`): 18 files, all under `_tools_/`. Tests: 27 pass when re-run by the coordinator.
- `_tools_/INDEX.md` went from 3,796 words to 195 body words plus 13 articles under 500 each. No file name was lost and the 25 table rows remain. Merged to main as `f9d3cd01`.
- Gate counts reported by the toolsmith: new errors 11 before, 4 after (concision 0, entry-points 3, type-instance-trees 1); 7 operator records are exempt by exact path.
- The hook is not installed: `core.hooksPath` is unset.

## Decisions

1. New records folders without an INDEX.md: no blanket exemption. A `stub-index` subcommand creates a static stub of under 60 words, current day only, dry run by default. The operator runs `stub-index --apply` after the first record in a new folder. Older records folders stay as legacy warnings.
2. `board_check.py`: go. It moves to `_tools_/board-check/` with its own index and tests. The token comes only from the caller's environment and is never read from the keychain or printed. The Steward runs it; the coordinator holds no token.

## Assignment

`A-20261123-0501-toolsmith`, due 05:35Z: `stub-index`, then `board-check`. I install the hook after reviewing it. The operator is told to run `stub-index --apply` once the subcommand lands.

## Remaining blockers to install

Type-instance-trees 1 and entry-points 3 must reach zero for a clean records commit; the operator's three new activity folders need their stubs.
