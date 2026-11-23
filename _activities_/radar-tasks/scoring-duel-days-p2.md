---
title: Scoring - duel days part 2
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 20
description: Live-dialog contradiction, 2026-11-03 1450, RESOLVED 2026-11-03 by PR 237 (Issue 235, tooling) - the 1450 unit
---
- Live-dialog contradiction, 2026-11-03 1450, RESOLVED
  2026-11-03 by PR 237 (Issue #235, tooling): the 1450 unit
  ran on duel day 2, Base Expansion, radar posture stack -
  not day 3 release. The tool's day-3 reading was a clock
  bug, not a stale schedule: duel.py read a naive UTC
  clock, which had already crossed the 19:00 boundary at
  14:03 PT and rolled to day 3 eight hours early. The
  corrected tool returns day 2 stack for the 1450 instant,
  matching the live TIPS dialog verbatim, and the schedule
  in tools/duel_schedule.json is NOT stale - that
  hypothesis is retired. The unit's window stamp (duel day
  2, radar stack) was right and the live tool reading was
  wrong, reversing the 1532 lesson that the live posture
  governs over the stamp: when tool and stamp disagree,
  check the tool's clock basis and the VS panel before
  trusting either. Tapping Claim All opened
  a TIPS dialog reading verbatim: "Completing Radar Tasks
  today will not grant Alliance Duel points, and you are about
  to claim 10 radar task rewards at once. Continue?" This
  contradicts the tool's gate text that radar claims score
  again today. The unit claimed anyway (resources certain,
  holding the stack risks task expiry, release standard
  governs). That either/or is now settled by PR 237 (see
  the head of this bullet): the schedule was NOT stale,
  the tool's clock was wrong, and the dialog meant what
  it said. The next radar release
  decision needs the settled reading, ideally from the VS
  panel itself. No duel score read was taken in the 1450
  unit, so the delta test is still owed. Verification still
  owed after the merge: the next radar unit that consults
  duel.py must report the PT day. ANSWERED IN PART
  2026-11-03 1913 (first radar unit after the PR 243
  merge): the unit consulted duel.py at entry (day 3,
  Age of Science, release) and NO TIPS dialog appeared
  on any of its three post-rollover Claim All taps, so
  tool, day and dialog agree after the fix - but no VS
  panel read was taken, so no duel-points figure is
  claimed and the delta test is still owed. The 19:00 PT
  boundary in this bullet is superseded by PR 243: the
  boundary is absolute 02:00 UTC, about 18:00 PST now
  (19:00 PDT before the DST end), and day 3 release runs
  from the about-18:00 rollover, not from 19:00 PT.
  Issue #235 closure belongs to the daily retro, not
  to this fold.
