---
title: Daily Missions
created: 2026-10-25T18:58:00Z
modified: 2026-11-02T13:45:00Z
level: L1
version: 1.3.0
description: The Mission daily task list and activity chests, one activity folder for mission knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: daily-missions execution record 2026-11-01 1444 queue run
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (missions fix-up expired, attempts 0)
  - source: daily-missions execution record 2026-11-02 0444 queue run
---


# Daily missions

## What this activity is

Working the Mission daily task list to raise activity points and claim
the activity chests. This folder accumulates mission knowledge - the task
set, point values and chest thresholds. Executions are recorded in
`_records_/<date>/daily-missions/`, one file per execution.

## How it is done

- Open Mission from the orange terminal on the base screen.
- Claim each completed task individually and re-check the list after
  each claim, because the list reorders as tasks are claimed.
- Claim the activity chests when their thresholds are reached.
- Tasks that need PvP, stamina combat or a gathering march are reported
  as not done, not silently skipped.

## What is known from 2026-10-25

- Claimed that day - Daily Login, Complete 1 Radar Task, Help Allies
  5 Times and Recruit Heroes 1 Time, plus Donate to Alliance Tech 5 Times
  after the donations were made.
- Activity reached 100 points. The 40 point and 80 point chests were
  claimed. The 80 point chest held Iron and Food Chests SR times 4 each
  and 5 minute build speedups, among other items.
- Not done that day - Defeat any Doom Elite, Kill 5 zombies, Attack a
  Commander and Gather Food 10,000. Attack a Commander is PvP and stays
  undone without the owner instruction.
- Warning from that round - batch tapping one spot is unsafe here, one
  tap landed on Go after the list reordered and jumped to the world map.

## What is known from 2026-11-01

Claim run by ticker-1434 (unit daily-missions-2026-10-31-1900,
status done). Evidence in
`_records_/2026-11-01/daily-missions/1444-queue-run.md`.

- Entry - Mission opened from the orange terminal icon on
  the base screen, grounded at norm 45,865. Daily Tasks
  tab read live on entry - Next Refresh 03:15:35,
  activity 110, tab badge 2.
- Claimed - Help Allies 5 Times (18/5): green Claim
  tapped once at norm 781,426. Rewards on its row - 10
  activity points, 5.0K food, 5.0K iron. Dispatch Trade
  Trucks 3 time(s) (3/3): its green Claim row (30 points,
  6.0K coin) left the list after that same single Help
  Claim tap, with no second tap made on it. After the
  one tap the activity read 150 (110 plus exactly 10
  plus 30), the tab badge read 1, and neither completed
  row remained in the list. The mechanism is unverified
  - the record does not assert how one tap claimed both
  rows, and a later unit should watch for the same
  behaviour before assuming it. The standing rule above
  is unchanged: claim each task individually and re-read
  the list and the activity total after each claim tap.
  Do not batch-tap - the list reorders after each claim
  and a stale tap can land on Go and jump to the world
  map (standing warning from 2026-10-25).
- 120 point activity chest - tapped at norm 560,247
  after the activity reached 150. CONGRATULATIONS popup
  read "No double reward this time. Good luck next time,
  Commander!" Contents read live - gear component x2,
  red crystal x20, milk jar x1, blueprint stack x6, food
  crate x6, iron 1.2K, 5m speedup x2.
- Closing state, read live - activity 150. Chests 40, 80
  and 120 opened; 160 and 200 still ahead (10 points
  short of 160). Daily Tasks tab badge cleared to none.
  Daily Login (1/1) sits at the list bottom with no
  Claim or Go button - already claimed earlier, not by
  this unit.
- Not done, reported not skipped - Defeat any Doom Elite
  1 (0/1), Recruit Heroes 1 (0/1), Kill 5 zombies on
  World Map (0/5), Gather Food, Iron and Coin 10,000
  each (0/10,000), Train 100 units (0/100), Recruit
  Survivors 1 in the Tavern (0/1), Plunder others
  Secret Task reward 1 (0/1), Perform Data Training on
  Drone 1 (0/1): incomplete, needing combat, gathering
  or other regulars gameplay, none attempted in this
  unit. Attack a Commander 1 (0/1): PvP, stays undone
  without the owner instruction. Make any paid purchase
  once (0/1): red line, never attempted.

## What the 2026-11-01 reset close added

- The sweep's missions fix-up daily-missions-2026-11-02-0151
  (priority 1, expires at the 19:00 reset) expired with
  attempts 0 in the ticker-1904 sync reap (result finished
  2026-11-02T03:04:31Z). No missions execution record after
  the 1444 unit exists for the ended trade day, so the day
  closed at activity 150 with the 160 and 200 chests
  unclaimed.
- The 1444 close stands as the day's last live missions
  read (activity 150, chests 40, 80 and 120 opened). The
  one-tap-two-claims mechanism stays unverified, and the
  160 and 200 thresholds are not carried as progress into
  the new trade day.



## What the 2026-11-02 0444 unit found

- Unit daily-missions-2026-11-01-1900 by ticker-0434, about 04:42
  to 04:44, status partial, nothing claimed. Evidence in
  `_records_/2026-11-02/daily-missions/0444-queue-run.md`.
- Entry - from the Events hub, back arrow at norm 163,947
  returned to base; a tap at 101,941 first landed on the portrait
  icon overlapping the arrow left edge and did nothing, the same
  overlap note as the 1437 scout record. The orange Mission
  terminal at norm 45,865 opened MISSION, confirming the 1444
  grounding. Back arrows differ per screen: the Mission screen
  back-arrow centre is re-grounded at norm 62,941 in the
  crystal-shop 0446 unit, where taps at 101,941 and 163,947 both
  missed on that screen. Do not inherit one screen grounding
  onto another.
- State read live - Daily Tasks tab badge 3, Next Refresh
  13:17:28, activity 70. Chests 40, 80, 120, 160, 200 shown; the
  40 chest icon appears open/gold in captures, but its claimed
  state was not verified by a tap and is not asserted here.
- Completed rows with green Claim buttons, all still pending -
  Defeat any Doom Elite 1 time(s) (1/1), rewards 10 activity
  points, food 5.0K, iron 5.0K; Help Allies 5 Times (12/5),
  rewards 10 points, food 5.0K, iron 5.0K; Dispatch Trade Trucks
  3 time(s) (3/3), rewards 30 points, coin 6.0K. Together 50
  points, which would take activity 70 to 120 if all three
  claimed. They stay pending for the next tick or the pre-reset
  sweep.
- Claim failure, button-specific - Defeat row Claim: single tap
  at norm 779,384, then double tap at 782,384, verified by
  following screenshots each time: button stayed green,
  activity stayed 70, tab badge stayed 3. Help row Claim:
  single tap at norm 782,499, same verification, no change.
  Per queue rule R2 the Claim method ends inside this unit
  after the two no-change taps on the first button; the second
  button was a pivot to a different control, not a repeat, and
  it failed identically.
- This does not supersede the 1444 unit, where a green Claim tap
  worked (and one tap cleared two rows). Claim responsiveness
  is intermittent across units, not a permanent state: the 1444
  success and the 0444 failure both stand. The pattern now
  spans two screens in the same morning session - the VIP 0438
  Daily Freebie Claim failed twice while the VIP login chest
  tap worked at once - five failed Claim taps against
  navigation taps, tab taps, drags, the Mission terminal tap
  and the VIP chest tap all working. Filed as GitHub Issue 171
  (play class) from this unit, referencing Issues 165 and 123;
  closure belongs to the daily retro with evidence, not to
  this organiser run. The small portrait icon overlapping the
  right edge of each Mission Claim button is recorded as a
  candidate cause for the tooling owner to test, not as a
  finding.
- Incomplete rows seen - Recruit Heroes 1 Time(s) (0/1, Go
  button, not tapped); after a list drag, Greet Visitors 3
  times (0/3), Kill 5 zombie(s) on World Map (0/5), Attack a
  Commander 1 time(s) (0/1, PvP, stays undone without the owner
  instruction), Gather Food x 10,000 at resource tile
  (0/10000), Gather Iron x 10,000 at resource tile (0/10000,
  partially visible at the fold). Rows between Recruit Heroes
  and Greet Visitors were not re-read in this unit (drag jump),
  named here rather than assumed.

## Open questions

- The full daily task set and its reset time, and the chest
  thresholds above 120 points - 160 and 200 were seen ahead
  at the 1444 close, not yet claimed.
- The one-tap-two-claims mechanism of the 1444 unit -
  unverified, not a rule to rely on until a later unit
  watches the same behaviour.
