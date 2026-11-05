---
title: Daily Missions
created: 2026-10-25T18:58:00Z
modified: 2026-11-04T17:40:01Z
level: L1
version: 1.5.0
description: The Mission daily task list and activity chests, one activity folder for mission knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: daily-missions execution record 2026-11-01 1444 queue run
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (missions fix-up expired, attempts 0)
  - source: daily-missions execution record 2026-11-02 0444 queue run
  - source: ticker-0004 daily-missions execution record 2026-11-03 0017 queue run (partial, activity chest claim path unverified, Issue 208)
  - source: ticker-0904 daily-missions execution record 2026-11-04 0914 queue run (partial, 3 gather tasks claimed on one tap, first verified 200-point activity-chest claim, Issues #171 and #208 commented by the ticker pass)
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

## What the 2026-11-03 0017 unit added - first unit of the new reset day, chest claim unverified, partial

- Unit daily-missions-2026-11-02-1900 by ticker-0004,
  session about 00:17 local, status partial.
  Evidence in
  `_records_/2026-11-03/daily-missions/0017-queue-run.md`.
- Entry and state, read live: Mission opened from
  the base bottom-left terminal icon, grounded at
  norm 52,863 in this base view. Daily Tasks tab
  selected. Next Refresh 17:39:57 at entry
  (17:37:59 at close). Activity star reads 160.
  This is the first daily-missions unit of the
  reset day started 2026-11-02 19:00; the completed
  rows seen by the 2026-11-02 0444 unit belonged to
  the previous reset day and do not carry over.
- Chests row: 40, 80, 120, 160 shown as open golden
  chests, 200 shown closed. No completed task row
  with a green Claim button was visible in this
  view: Recruit Heroes 1 Time (0/1), Kill 5 zombies
  on World Map (0/5), Attack a Commander 1 time
  (0/1, PvP, stays undone without the owner
  instruction), Gather Food x 10,000 at resource
  tile (0/10000), all with blue Go buttons, none
  tapped. A further row below the fold was not read.
- Activity chests, claim path unverified: the 40
  chest was tapped at its grounded point (313,256).
  It opened only a contents preview: 5m
  Construction Speed-up x1, Iron Chest (SR) x2,
  Food Chest (SR) x2, Coin Chest (SR) x6, Drone
  Parts x2, Crystal Ore 600. No Claim button was
  found in the preview (visual grounding located
  only the popup chest icon). Tapping that popup
  chest icon (349,270) dismissed the preview.
  Enlarged before/after crops of the chest row show
  no change to the 40 chest icon. Per rule R2 the
  chest-claim method ends inside this unit after
  these two taps with no verified claim. The claim
  state is therefore NOT asserted: the open icons
  may mean already claimed, or claimable with an
  unidentified claim step, and no Congratulations
  or receipt panel was observed. No chest is
  recorded as claimed in this unit.
- Correction of scope, not of a prior claim: this
  chest-preview failure is distinct from Issue 171
  (green task Claim buttons unresponsive,
  2026-11-02 0444). It was filed as GitHub Issue
  208 (play class) from this unit; closure belongs
  to the daily retro with evidence, not to this
  organiser run. No diamonds, no money, no Go
  button tapped, no PvP task attempted. Game left
  on the base screen.


## Open questions

- The full daily task set and its reset time, and the chest
  thresholds above 120 points - 160 and 200 were seen ahead
  at the 1444 close, not yet claimed. (2026-11-03 0017 update: activity 160
  reached on the new reset day, chests 40/80/120/160 shown as
  open golden chests and 200 closed, but the 40 chest tap
  opened only a contents preview with no Claim button, so
  no chest is asserted claimed - see Issue 208.) (2026-11-04 0914 update: the 200-point chest is now claimed and verified - gold bar x1, red gem x50, wrench x1, flower x1, crate x1, Crystal Ore 2.0K, 5m speed-up x4, with the standard "No double reward this time" receipt; the 40/80/120/160 chests showed open golden icons at entry and were not re-tapped, so their claim state is still not asserted. The 0914 evidence supports the already-claimed reading of the 0017 40-chest preview-only case; Issue #208 was commented with this evidence by the ticker pass.)
- The one-tap-two-claims mechanism of the 1444 unit -
  unverified, not a rule to rely on until a later unit
  watches the same behaviour. (2026-11-04 0914 update: second observation - one tap on the Gather Food Claim button removed all three completed gather rows at once, activity 180 to 210, tab badge 3 to 1. Still inference from two observations, not a verified mechanism; the claim-each-task-individually rule stands.)

## What the 2026-11-04 0914 unit added - 3 gather tasks on one tap, first verified 200-point chest claim, partial

- Unit daily-missions-2026-11-03-1900 by ticker-0904, about 09:06 to 09:10 local, status partial. Session cc-441. Evidence in `_records_/2026-11-04/daily-missions/0914-queue-run.md`. No diamonds, no money, no Go button tapped, no PvP task attempted, no paid-purchase row touched.
- Entry and state, read live: Mission opened from the base bottom-left terminal icon, grounded fresh at norm 43,846 in this base view. Daily Tasks tab selected. Next Refresh 08:52:35 at entry (08:50:27 at close). Activity star 180 at entry. Daily Tasks tab badge 3 at entry.
- Claims made in this unit, all verified live: one grounded single tap on the Gather Food Claim button (norm 780,410) removed all three completed gather rows from the list at once: Gather Food x10,000 (1800000/10000), Gather Iron x10,000 (1800000/10000) and Gather Coin x10,000 (432000/10000). Activity star rose 180 to 210 (+30, exactly 3 tasks x 10 points), and the tab badge fell 3 to 1. Whether the game batch-claims completed rows on one tap is inference from that single observation, not a separately verified mechanism; the observed facts are the three rows leaving the list and the +30 star delta. This is the second one-tap-multi-claim observation after the 1444 unit (one tap cleared two rows); the claim-each-task-individually rule stands until the mechanism is verified.
- Counter-evidence to Issue #171, commented there by the ticker pass (no duplicate comment here): this contradicts the standing Issue #171 picture (green Claim buttons unresponsive, 2026-11-02) - the buttons responded in this session (cc-441). Together with the 0847 secrets unit (buttons dead in cc-440 the same morning), Claim responsiveness is session-dependent, not a global dead state. Closure of #171 belongs to the daily retro.
- 200-point activity chest, first verified activity-chest claim in this line: with activity at 210, one grounded tap on the 200 chest (norm 819,249) produced a CONGRATULATIONS receipt popup ("No double reward this time. Good luck next time, Commander!") with rewards: gold bar x1, red gem x50, wrench x1, flower x1, crate x1, Crystal Ore 2.0K, 5m speed-up x4. Popup dismissed by tapping its banner. After dismissal the Daily Tasks tab badge was gone. Commented on Issue #208 by the ticker pass (no duplicate comment here), suggesting its 2026-11-03 40-chest preview-only case was an already-claimed chest. Closure of #208 also belongs to the daily retro.
- Remaining tasks, read live, none actioned: Recruit Heroes 1 Time (0/1), Kill 5 zombie(s) on World Map (3/5), Attack a Commander 1 time (0/1, PvP, stays undone without the owner instruction), Train 100 units of any level (0/100), Upgrade a Building 1 time (0/1), Recruit Survivors 1 time in the Tavern (0/1), Make any paid purchase once (0/1, red-line row, observed only, never to be actioned), Perform Data Training on Drone 1 time (0/1). Go not tapped on any row.
- Outcome: partial. The unit claimed everything claimable at entry, but the regular's task list is not fully done: 8 tasks remain incomplete and belong to other regulars or later ticks, so the tracker is untouched and the next tick re-checks the list. Game left on the base screen.
