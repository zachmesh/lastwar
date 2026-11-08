---
title: Queue Run 0444 Daily Missions
created: 2026-11-02T12:44:00Z
modified: 2026-11-02T12:44:00Z
level: L0
version: 1.0.0
description: Daily missions unit partial - green Claim buttons unresponsive, nothing claimed
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 0444 queue run - daily missions (partial)

Unit daily-missions-2026-11-01-1900, executor ticker-0434,
sessions cc-152/cc-153 on the Mac mini, LastWar window
137757, about 04:42 to 04:44 America/Los_Angeles. Status
partial: no task or chest was claimed. No different-device
dialog, no login demand, nothing spent, no Go button
tapped, no paid task attempted.

## Entry and state read live

- From the Events hub, the back arrow at norm [163,947]
  returned to base (a tap at [101,941] first landed on
  the portrait icon overlapping the arrow left edge and
  did nothing - same overlap note as the 1437 scout
  record). The orange Mission terminal at norm [45,865]
  opened MISSION.
- Daily Tasks tab, badge 3, Next Refresh 13:17:28,
  activity 70. Chests 40, 80, 120, 160, 200 shown; the
  40 chest icon appears open/gold in captures, but its
  claimed state was not verified by a tap and is not
  asserted here.
- Completed rows with green Claim buttons, read live:
  Defeat any Doom Elite 1 time(s) (1/1), rewards 10
  activity points, food 5.0K, iron 5.0K; Help Allies 5
  Times (12/5), rewards 10 points, food 5.0K, iron
  5.0K; Dispatch Trade Trucks 3 time(s) (3/3), rewards
  30 points, coin 6.0K. Together 50 points, which
  would take activity 70 to 120 if all three claimed.
- Incomplete rows seen: Recruit Heroes 1 Time(s)
  (0/1, Go button, not tapped); after a list drag,
  Greet Visitors 3 times (0/3), Kill 5 zombie(s) on
  World Map (0/5), Attack a Commander 1 time(s)
  (0/1, PvP, stays undone without the owner
  instruction), Gather Food x 10,000 at resource tile
  (0/10000), Gather Iron x 10,000 at resource tile
  (0/10000, partially visible at the fold). Rows
  between Recruit Heroes and Greet Visitors were not
  re-read in this unit (drag jump), named here
  rather than assumed.

## Claim failure - green Claim buttons, button-specific

- Defeat row Claim: single tap at norm [779,384],
  then double tap at [782,384]; verified by following
  screenshots each time - button stayed green,
  activity stayed 70, tab badge stayed 3.
- Help row Claim: single tap at norm [782,499];
  same verification - no change.
- Per queue rule R2 the Claim method ends inside
  this unit after the two no-change taps on the
  first button; the second button was a pivot to a
  different control, not a repeat, and it failed
  identically.
- This is the same session as the VIP unit, where
  the Daily Freebie Claim button failed twice while
  the VIP login chest tap worked at once. The
  pattern now spans two screens and five failed
  Claim taps against navigation taps, tab taps,
  drags, the Mission terminal tap and the VIP chest
  tap all working. Filed as GitHub Issue #171
  (play class) from this unit, referencing #165
  and #123; closure belongs to the daily retro
  with evidence, not to this executor.
- The small portrait icon overlapping the right
  edge of each Mission Claim button is recorded as
  a candidate cause for the tooling owner to test,
  not as a finding.

## Outcome

- Status: partial. Claimed in this unit: nothing.
  Still pending: the three completed rows above
  (50 activity points) and the activity chests at
  and above the reached thresholds, for the next
  tick or the pre-reset sweep.
- Tracker untouched (partial units do not mark the
  tracker). Game left on the Mission Daily Tasks
  list, scrolled to the lower rows.
- Red lines: nothing spent, no diamonds, no paid
  purchase task attempted.
