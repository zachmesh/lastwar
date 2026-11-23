---
title: How it is done - dispatching
created: 2026-11-23T07:15:45Z
modified: 2026-11-23T07:15:45Z
version: 0.1.0
sequence: 5
description: Normal dispatch sends one task at a time from Your Tasks.
---
## How it is done - dispatching

- Normal dispatch sends one task at a time from Your Tasks.
- The Mega button at the bottom switches the bottom bar to Mega
  Refresh, Mega Deploy and Normal. Mega Deploy opens the MEGA
  DEPLOY REMINDER panel - every pending task listed with its
  duration and an auto assigned hero team (some tasks get only two
  heroes), a checkbox per task, a UR Only filter that starts on,
  and a Perform Now button that sends everything checked at once.
- CORRECTED 2026-11-22 (Issue #831): Mega Deploy's true centre
  is norm (619,946) in the 642x951 window - the (498,900) point
  recorded from the 2243 unit is the button's top-left edge and
  misses (the button spans about pixel x 320-475, y 870-930).
  A tap at (619,946) responds with the toast "There are
  currently no tasks available for dispatch" when nothing is
  pending. The 2243/0150/0259 conclusions that Mega Deploy is
  dead or unresponsive rest on those edge taps and are WRONG -
  do not repeat them. Mega Refresh centre is about (386,946)
  by the same measurement, NOT yet tap-verified - an estimate
  only, do not rely on it. The Mega Deploy toast is the
  authoritative nothing-pending check: when it reports no
  tasks available for dispatch it covers the whole list
  including below the fold, so no scroll check is needed.
- Unchecking UR Only resets every checkbox to empty - after
  unchecking, re-check each task by hand before Perform Now. The
  panel scrolls for long lists.
- Mega Refresh rerolls the pending task list. Its cost was not
  observed - the evening run did not need it.
- Standing rules, owner taught 2026-10-25. One - for the Secret
  Mobile Squad, use Mega Deploy by default on most days. Two - on
  Alliance Duel days when UR secret tasks count toward the duel
  score, first use Mega Refresh to roll UR tasks, then deploy.
  Three - when dispatching via Mega Deploy, unselect UR Only so
  every squad deploys.

