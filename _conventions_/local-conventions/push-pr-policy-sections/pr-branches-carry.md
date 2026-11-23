---
title: PR branches carry no log appends
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 11
description: A pull request branch - records or work - never carries appends to the append-only logs
---
## PR branches carry no log appends

A pull request branch - records or work - never carries
appends to the append-only logs under `_logs_` (the input log
and the action log). The evidence is from this repository on
2026-10-31: PR #2 went through two rebase rounds, main
advanced three times inside ten minutes on records commits,
and every conflict sat in the log tails and the day index
those commits keep appending. Log lines race main's
high-frequency records flow by construction; a branch that
carries them is a branch built to conflict.

The record duty does not disappear, it moves:

- During the PR's life, the record is the PR body and the
  commit messages, which already state what the change
  serves, what was validated and what files it touches.
- At merge time, the integrator adds the input-log and
  action-log lines for the merged work as part of the merge
  bookkeeping, or the lines ride the next records branch
  after the merge. Either way they land once, on a branch
  that does not race itself.
- A retro that cannot find a merged change's log lines names
  the gap like any other loop-health gap; the fix is to add
  the lines, never to start carrying them on PR branches
  again.

