---
title: Privacy finding and records delivery - 2026-11-22 22:22 PT
created: 2026-11-22T22:22:00-08:00
modified: 2026-11-22T22:24:00-08:00
level: L3
version: 0.1.0
description: Delivering the day's untracked records exposed that the public repository carries the owner account name and alliance tag; redaction before first commit, an owner decision, and prevention in the commit gate
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2222-privacy-finding
trigger: scribe's note that cited records were untracked; privacy scan before committing them
started_at: 2026-11-22T22:15:00-08:00
finished_at:
duration_seconds:
verified: scan patterns held in code, counts and paths only; staged set rescanned to zero after redaction; the two new register files scanned to zero
---

# Privacy finding and records delivery

## Delivery

121 files in one commit, `2481d606`: 56 records, 18 closed units, the planner's 16 staged units, the bridge ledger and the deletions of moved units. They had been untracked for hours; the gate passed with 0 blocking and 7 exempt (the grandfathered records).

## Finding

The account privacy convention keeps the owner account's in-game name and alliance tag out of this public repository (HTTP 200). A scan of the staged set found the alliance tag in 11 lines and the owner name in 3, across 10 files, no emails and no tokens. A scan of tracked files at HEAD then found the owner name in 172 files (375 lines) and the alliance tag in 334 files (810 lines): 276 records, 57 activity files, one log. It predates the team and sits in git history. The first scan also showed that `git grep -E` does not support `\s`; a false zero was caught by re-running with a POSIX class.

## Actions

- Redacted the ten delivered files before their first commit (12 tag and 4 name replacements, neutral markers), then committed. Nothing new entered the history.
- Owner decision `OD-20261123-04` filed in the new register form (article plus entry-page lines): redact the current tree, rewrite history or not, public meanwhile, allies' names.
- Prevention: a local denylist inside `.git` (never pushed); toolsmith `A-20261123-0623` builds a gate check that blocks added lines and file names without ever printing a match, and a counting `watch --privacy` (due 06:55Z). The operator got the writing rule.
- Never again in my own messages: counts and paths only.

## Outcome

Pending the toolsmith and the owner.

## Correction (appended 2026-11-23T06:24Z)

My message to the Steward said 12 commits after its last push (`5173ed7d`). Counted from git: 11, ending at `076ab668`, plus this record's own commit.
