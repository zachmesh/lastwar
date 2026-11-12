---
title: Daily Missions
created: 2026-10-25T18:58:00Z
modified: 2026-11-12T01:32:17Z
level: L1
version: 1.13.0
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
  - source: ticker-1734 daily-missions execution record 2026-11-05 1734 queue run (failed, Mac device offline, fifty-sixth consecutive ticker pass with a Mac device-access blocker, seventeenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 10h, unchanged since the 1025 pass; seven invokes, zero responses)
  - source: ticker-1604 daily-missions execution record 2026-11-06 1612 queue run (failed, Mac device offline, eighty-second consecutive ticker pass with a Mac device-access blocker, forty-third in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 32h35m, unchanged since the 1507 and 1534 passes; seven invokes, zero responses)
  - source: ticker-0204 perception-scout execution record 2026-11-08 0229 queue run (partial per R1, daily missions panel walked, full 22-task list read live, 4 completed unclaimed, Next Refresh pointing to about 18:00 local; record commit 6560ff267 on records/2026-11-08)
  - source: ticker-1604 daily-missions execution record 2026-11-08 1628 queue run (partial, 4 completed tasks claimed on one tap, activity 0 to 70, first verified 40-point activity-chest claim with double-rewards receipt, Issues 171 and 208 commented by the ticker pass; record commit d8b700b90 on records/2026-11-08)
  - source: ticker-1724 daily-missions execution record 2026-11-08 1753 queue run (partial, full daily task list re-checked live, nothing newly completed, activity 70, 80-point chest 10 short into the reset, claimed rows sink to the bottom with green checks correcting the 1628 removed-from-list reading, first observed duplicate execution of the same unit id; record commit 5f3a904f4 on records/2026-11-08)
  - source: ticker-1518 daily-missions execution record 2026-11-09 1519 queue run (done, one tap claimed all four completed rows at once and the 40/80/120 chests by cascade, activity 0 to 140, one-tap-multi-claim now verified by before/after reads, slow-drag scroll method measured, activity-star composition open; record commit da249faca3 on records/2026-11-09)
  - source: ticker-1424 daily-missions execution record 2026-11-10 1426 queue run (done, four completed rows claimed, 40/80/120 chests claimed with contents identical to the 1519 read, activity 120, Next Refresh 03:31:56 to the 18:00 reset; record commit edd4659a3 on records/2026-11-10)
  - source: ticker-1634 daily-missions execution record 2026-11-11 1638 queue run (done, two completed rows claimed on one tap, activity 80 to 100, 40/80 chests already claimed with contents previewed, Mission list would not scroll - quick drag, scroll action and slow staged drag all no-change; record commit 1fe3a5e69 on records/2026-11-11)
---


# Daily missions

## What this activity is

Working the Mission daily task list to raise activity points and claim
the activity chests. This folder accumulates mission knowledge - the task
set, point values and chest thresholds. Executions are recorded in
`_records_/<date>/daily-missions/`, one file per execution.

## How it is done

- Open Mission from the orange terminal on the base screen.
- Claim with ONE tap on a completed row's Claim button: the tap claims every completed row in view at once (verified 2026-11-09 1519, fourth observation, before/after reads), then re-check the list - claimed rows sink to the bottom with green checks and the list reorders to unclaimed rows. Do not keep tapping Claim buttons on the reordered list without a fresh read: a tap can land on a Go button after the reorder (2026-10-25 warning).
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
  no chest is asserted claimed - see Issue 208.) (2026-11-04 0914 update: the 200-point chest is now claimed and verified - gold bar x1, red gem x50, wrench x1, flower x1, crate x1, Crystal Ore 2.0K, 5m speed-up x4, with the standard "No double reward this time" receipt; the 40/80/120/160 chests showed open golden icons at entry and were not re-tapped, so their claim state is still not asserted. The 0914 evidence supports the already-claimed reading of the 0017 40-chest preview-only case; Issue #208 was commented with this evidence by the ticker pass.) (2026-11-08 1628 update: the 40-point chest is now claimed and verified - see the 1628 section below. The 0017 preview-only case is confirmed as an already-claimed chest; Issue #208 was commented with this evidence by the ticker pass.) (2026-11-09 1519 update: the 40, 80 and 120 chests are now all claimed and verified - 40 chest contents gear part x10, red gem x40, wrench x1, blue crate x20, food crate x20, gold coins x12, crystal 2.8K, 5m speedup x8 with a double-rewards receipt; 80 chest 5m Construction Speed-up x2, Iron Chest (SR) x4, Food Chest (SR) x4, Construction Part x1, Drone Parts x2, Crystal Ore 1.0K; 120 chest 5m Construction Speed-up x2, Iron Chest (SR) x6, Food Chest (SR) x6, Diamond x20, Drone Parts x2, Crystal Ore 1.2K. The 160 and 200 chests stand unreached at activity 140. The chest cascade matches the row cascade - one tap claims every claimable chest, not just its own; tapping an already-open chest shows its contents list and spends nothing. Issue #208 commented with this evidence by this run; closure belongs to the daily retro.) (2026-11-10 1426 update: the 40, 80 and 120 chests are claimed again with contents identical to the 1519 read (40: gear x10, red gem x40, wrench x1, blue crate x20, food crate x20, gold x12, crystal 2.8K, 5m speedup x8 with the double-rewards receipt; 80 and 120 as in 1519); activity 120 at close, the 160 and 200 chests stand unreached. The chest cascade matches the row cascade - one tap claims every claimable chest. Issue #208 commented with this evidence by this run; closure belongs to the daily retro.) (2026-11-11 1638 update: the 40 and 80 chests were already claimed and each tap opened only a contents preview - 40: 5m Construction Speed-up x1, Iron Chest (SR) x2, Food Chest (SR) x2, Coin Chest (SR) x6, Drone Parts x2, Crystal Ore 600, identical to the 0017 preview read, the second preview confirmation; 80: 5m Construction Speed-up, Iron Chest (SR), Food Chest (SR), Construction Part, Drone Parts, Crystal Ore 1.0K, matching the 1519/1426 claim contents in items with counts partly OCR-garbled. Preview contents and claim-receipt contents differ because receipts carry the double-rewards multiplier - no contradiction. The 160 and 200 chests stand unreached at activity 100.)
- The one-tap-two-claims mechanism of the 1444 unit -
  unverified, not a rule to rely on until a later unit
  watches the same behaviour. (2026-11-04 0914 update: second observation - one tap on the Gather Food Claim button removed all three completed gather rows at once, activity 180 to 210, tab badge 3 to 1. Still inference from two observations, not a verified mechanism; the claim-each-task-individually rule stands.) (2026-11-08 1628 update: third observation - one tap on the Daily Login Claim button removed all four completed rows at once, activity 0 to 70, tab badge 4 to 1. Still inference from three observations, not a verified mechanism; the claim-each-task-individually rule stands.) (2026-11-08 1753 correction: the 1628 "removed" reading is superseded - the full-list re-check read the claimed rows sunk to the bottom of the list with green checkmarks (Daily Login 1/1, Donate to Alliance Tech 5/5 seen checked); the 1628 unit did not scroll to the bottom, so it could not see them there. The one-tap claim itself stands - activity rose 0 to 70 on the single tap - but claimed rows sink, they are not removed. The mechanism stays unverified.) (2026-11-09 1519 update: VERIFIED - the fourth observation, with before/after reads: one tap on the Daily Login Claim button claimed all four completed rows at once (badge 9 to 3, activity star 0 to 140, bar gold through 120) and the 40/80/120 chests by cascade. The claim-each-task-individually rule is superseded by the How-it-is-done update above; Issues #171 and #208 commented with this evidence by this run, closure belongs to the daily retro.) (2026-11-11 1638 update: sixth consistent observation - one tap on the Help Allies Claim button claimed both completed rows, activity 80 to 100; the mechanism stays unverified in this unit alone - possibly one tap claims every completed row, or the list refreshed on claim - and the 1519 verification stands.)

- Activity star composition (2026-11-09 1519): five claimed rows at 10 points each account for 50 of the 140 the star reads; the other 90 are unexplained by this unit's reads. The star read 0 at entry even though the four green rows were already complete, so the header may render stale until a claim refreshes it - or the star counts Main Tasks activity as well. The Main Tasks tab was not opened in this unit. A later unit should read the Main Tasks tab and the star in the same pass to pin this down.

## What the 2026-11-04 0914 unit added - 3 gather tasks on one tap, first verified 200-point chest claim, partial

- Unit daily-missions-2026-11-03-1900 by ticker-0904, about 09:06 to 09:10 local, status partial. Session cc-441. Evidence in `_records_/2026-11-04/daily-missions/0914-queue-run.md`. No diamonds, no money, no Go button tapped, no PvP task attempted, no paid-purchase row touched.
- Entry and state, read live: Mission opened from the base bottom-left terminal icon, grounded fresh at norm 43,846 in this base view. Daily Tasks tab selected. Next Refresh 08:52:35 at entry (08:50:27 at close). Activity star 180 at entry. Daily Tasks tab badge 3 at entry.
- Claims made in this unit, all verified live: one grounded single tap on the Gather Food Claim button (norm 780,410) removed all three completed gather rows from the list at once: Gather Food x10,000 (1800000/10000), Gather Iron x10,000 (1800000/10000) and Gather Coin x10,000 (432000/10000). Activity star rose 180 to 210 (+30, exactly 3 tasks x 10 points), and the tab badge fell 3 to 1. Whether the game batch-claims completed rows on one tap is inference from that single observation, not a separately verified mechanism; the observed facts are the three rows leaving the list and the +30 star delta. This is the second one-tap-multi-claim observation after the 1444 unit (one tap cleared two rows); the claim-each-task-individually rule stands until the mechanism is verified.
- Counter-evidence to Issue #171, commented there by the ticker pass (no duplicate comment here): this contradicts the standing Issue #171 picture (green Claim buttons unresponsive, 2026-11-02) - the buttons responded in this session (cc-441). Together with the 0847 secrets unit (buttons dead in cc-440 the same morning), Claim responsiveness is session-dependent, not a global dead state. Closure of #171 belongs to the daily retro.
- 200-point activity chest, first verified activity-chest claim in this line: with activity at 210, one grounded tap on the 200 chest (norm 819,249) produced a CONGRATULATIONS receipt popup ("No double reward this time. Good luck next time, Commander!") with rewards: gold bar x1, red gem x50, wrench x1, flower x1, crate x1, Crystal Ore 2.0K, 5m speed-up x4. Popup dismissed by tapping its banner. After dismissal the Daily Tasks tab badge was gone. Commented on Issue #208 by the ticker pass (no duplicate comment here), suggesting its 2026-11-03 40-chest preview-only case was an already-claimed chest. Closure of #208 also belongs to the daily retro.
- Remaining tasks, read live, none actioned: Recruit Heroes 1 Time (0/1), Kill 5 zombie(s) on World Map (3/5), Attack a Commander 1 time (0/1, PvP, stays undone without the owner instruction), Train 100 units of any level (0/100), Upgrade a Building 1 time (0/1), Recruit Survivors 1 time in the Tavern (0/1), Make any paid purchase once (0/1, red-line row, observed only, never to be actioned), Perform Data Training on Drone 1 time (0/1). Go not tapped on any row.
- Outcome: partial. The unit claimed everything claimable at entry, but the regular's task list is not fully done: 8 tasks remain incomplete and belong to other regulars or later ticks, so the tracker is untouched and the next tick re-checks the list. Game left on the base screen.

## What the 2026-11-05 1734 unit added - Mac device offline, fifty-sixth consecutive pass, zero-response form

- Unit daily-missions-2026-11-04-1800 by ticker-1734, about 17:38 to 17:42 local, status failed. Evidence in `_records_/2026-11-05/daily-missions/1734-queue-run.md`. No mission list was read, no completed task was claimed, and no activity chest was claimed. This was a stale unit from the 2026-11-04 18:00 slot (planned_for 2026-11-05T02:00:00Z, expires 2026-11-06T02:00:00Z).
- No game screen was ever read and no game input was dispatched. Seven device invokes, zero responses, across two devices and four distinct commands: computer.session start on the Mac mini three times node_offline (device offline, no wake-up path), connection.health on the Mac mini node_offline, connection.repair (target web) on the Mac mini node_offline, connection.repair (target native) on the recovery device node_invoke_timeout after 25 seconds, connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 10 hours at pass time, unchanged since the ticker-1025 pass; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Recurrence, not a new failure class: this is the fifty-sixth consecutive ticker pass with a Mac device-access blocker, seventeenth in the worsened zero-response form after ticker-1704 (fifty-fifth, sixteenth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fifty-sixth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the daily-missions state. It must NOT be read as "no missions claimable" or as an activity-points state - the 0914 close (activity 210, 200-point chest claimed and verified, 8 tasks remaining incomplete) rests on live reads and stands as the last live read; this unit rests on no read at all. The claim-each-task-individually rule stands, and the one-tap-multi-claim observation remains inference from two observations, not a verified mechanism.
- The pass stopped after this one unit: a second unit would hit the same dead channel. Sync at pass start produced 5 new units (passes, secrets, treasures, trucks, events for the 1457 slot); 18 due regulars were already queued. The Zombie Invasion chain stays closed: the event ended 2026-10-30 about 19:00 and no Zombie Invasion tab has been seen in the Events hub since, so no fresh chain was seeded. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-05) is staged in the inbox (units 001 and 002).
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 1604 unit added - Mac device offline, eighty-second consecutive pass, zero-response form

- Unit daily-missions-2026-11-05-1800 by ticker-1604, about 16:04 to 16:12 local, status failed. Evidence in `_records_/2026-11-06/daily-missions/1612-queue-run.md`. No mission list was read, no completed task was claimed, and no activity chest was claimed. This was a stale unit from the 2026-11-05 18:00 slot (planned_for 2026-11-06T02:00:00Z, expires 2026-11-07T02:00:00Z).
- No game screen was ever read and no game input was dispatched. Seven device invokes, zero responses, across two devices and four distinct commands: computer.session start on the Mac mini three times node_offline (device offline, no wake-up path), connection.health on the Mac mini node_offline, connection.repair (target web) on the Mac mini node_offline, connection.repair (target native) on the recovery device node_invoke_timeout after 25 seconds, connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 32 hours 35 minutes at pass time, unchanged since the ticker-1507 and ticker-1534 passes; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Recurrence, not a new failure class: this is the eighty-second consecutive ticker pass with a Mac device-access blocker, forty-third in the worsened zero-response form after ticker-1534 (eighty-first, forty-second). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the eighty-second occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the daily-missions state. It must NOT be read as "no missions claimable" or as an activity-points state - the 0914 close of 2026-11-04 (activity 210, 200-point chest claimed and verified) rests on live reads and stands as the last live read; this unit rests on no read at all.
- The pass stopped after this one unit: a second unit would hit the same dead channel. Sync at pass start reaped 0, expired 1, dropped 1 stale done (donations-2026-11-06-1403), produced 1 new unit (duel-score-2026-11-06-1430); 20 regulars already queued. Queue stats at 00:07Z: inbox 72, claimed 0, done 975, upcoming 53. The Zombie Invasion chain stays closed: the event ended 2026-10-30 about 19:00 and no Zombie Invasion tab has been seen in the Events hub since, so no fresh chain was seeded. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (pending 2), not yet due.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-08 0229 scout read added - full 22-task list read live

- Scout unit scout-midday-scout-mid-2026-11-03-004 by ticker-0204, 02:17 to 02:32 local, status partial per rule R1 (3 red dots unexplained, none of them missions). Evidence in `_records_/2026-11-08/perception-scout/0229-queue-run.md` (commit 6560ff267 on records/2026-11-08) and the appended section of `_records_/2026-11-03/perception-scout/observation.md`. Observe-only; nothing claimed.
- Entry: base bottom-left terminal icon, grounded at norm 52,863 in this base view (per the 2026-11-03 record; the yellow icon at [66, 790] is the build menu, not Missions - do not re-tap it for this panel). Re-ground fresh each unit; the base map scrolls.
- Daily Tasks tab (red badge 4 = the 4 completed tasks). Next Refresh 15:36:16 at entry, 15:32:08 at close (points to about 18:00 local - see the reset note below). Activity star 0 (points count only after claiming). Chest thresholds 40 / 80 / 120 / 160 / 200, all unreached; chest contents not read (no tap).
- Completed (green rows, Claim buttons - observed only, NOT claimed; claims belong to the daily-missions regular): Daily Login (1/1) star 10 + red gem 10; Donate to Alliance Tech 5 times (5/5) star 10 + coin 6.0K; Greet Visitors 3 times (3/3) star 10 + iron 5.0K + food 5.0K; VIP Activated (1/1) star 40 + red gem 10.
- Incomplete (Go buttons, NOT tapped): Defeat any Doom Elite 1 time(s) (0/1) star 10 + iron 5.0K + food 5.0K; Complete 1 Radar Task(s) (0/1) star 10 + iron 5.0K + food 5.0K; Help Allies 5 Times (0/5) star 10 + iron 5.0K + food 5.0K; Recruit Heroes 1 Time(s) (0/1) star 10 + red gem 10; Kill 5 zombie(s) on World Map (0/5) star 10 + iron 5.0K + food 5.0K; Attack a Commander 1 time(s) (0/1) star 10 + red gem 10; Gather Food x 10,000 at resource tile (0/10000) star 10 + iron 5.0K + food 5.0K; Gather Iron x 10,000 at resource tile (0/10000) star 10 + iron 5.0K + food 5.0K; Gather Coin x 10,000 at resource tile (0/10000) star 10 + iron 5.0K + food 5.0K; Train 100 units of any level (0/100) star 10 + iron 5.0K + food 5.0K; Upgrade a Building 1 time(s) (0/1) star 10 + iron 5.0K + food 5.0K; Research a tech 1 time(s) (0/1) star 10 + iron 5.0K + food 5.0K; Obtain 1 Gear at SSR and/or better rarity (0/1) star 10 + iron 5.0K + food 5.0K; Recruit Survivors 1 time(s) in the Tavern (0/1) star 20 + red gem 10; Make any paid purchase once (0/1) star 50 + red gem 50 (paid task - red line, never to be done); Dispatch Trade Trucks 3 time(s) (0/3) star 30 + coin 6.0K; Plunder others' Secret Task reward 1 time(s) (0/1) star 30 + red gem 10; Perform Data Training on Drone 1 time(s) (0/1) star 10 + iron 5.0K + food 5.0K.
- Full list is 22 tasks (4 completed + 18 incomplete); a final drag produced no change, so the list ends at Perform Data Training on Drone. Max activity stars 340 (290 without the paid-purchase task), so all five chests are reachable without paying.
- Season and Main Tasks tabs not opened.
- Reset note: Mission Next Refresh pointing to about 18:00 local today is new evidence for Issue #242 (commented by this run) - a countdown-based pointer from the missions panel, a second surface corroborating the 18:00 reset. Still unverified as a formal arbitration; the standing 19:00 note is not changed here. (2026-11-08 1753 update: the re-check read Next Refresh 00:11:55 falling to 00:08:22 across the unit, again pointing at the 18:00 local reset, and the 18:00 reset then arrived mid-sweep in the same pass's harvest unit - direct reset-time evidence, commented on Issue #242 by this run.)
- Game left safe: game left on the base screen. No claim, no purchase, no dispatch. No Assemble, no teleport.

## What the 2026-11-08 1628 unit added - 4 tasks on one tap, first verified 40-point chest claim, partial

- Unit daily-missions-2026-11-07-1800 by ticker-1604, about 16:23
  to 16:28 local, status partial - everything claimable at entry
  was claimed and verified live, but the regular's task list is
  not fully done: the remaining tasks are incomplete and belong
  to other regulars or later ticks, so the tracker is untouched
  and the next tick re-checks the list. This was a stale unit from
  the 2026-11-07 18:00 slot (planned_for 2026-11-08T02:00:00Z,
  expires 2026-11-09T02:00:00Z); the mission list read is live,
  so it covers the current reset day's missions. Evidence in
  `_records_/2026-11-08/daily-missions/1628-queue-run.md` (commit
  d8b700b90 on records/2026-11-08). Session cc-140 on the owner
  Mac mini. No device-access error, no different-device dialog,
  no login demanded. No screen-capture failure.
- Entry, read live about 16:24 local: Mission opened from the
  orange terminal on the base screen, grounded fresh at norm
  52,863 in this base view. Daily Tasks tab selected, tab badge
  4. Next Refresh 01:35:22 (points to about 18:00 local - another
  missions-panel pointer to the 18:00 reset, after the 0229 scout
  read; new evidence for Issue #242, commented by this run). Activity star 0. Chests 40 / 80 / 120 / 160 / 200
  all unreached. Base state at entry: power 149,850,353; food
  490.8M, iron 813.3M, coin 12.3M; stamina 120; Season II 7d
  01:36:14. Furnace toast read in full: "High-temp Furnace total
  overdrive time (in sec) [22/60]" - recurring, unexplained,
  observed only. Wanted Boss badge 2, timer 00:00:42, observed
  only.
- Completed rows at entry, all with green Claim buttons: Daily
  Login (1/1), star 10 + red gem 10; Donate to Alliance Tech 5
  times (5/5), star 10 + coin 6.0K; Greet Visitors 3 times
  (3/3), star 10 + iron 5.0K + food 5.0K; VIP Activated (1/1),
  star 40 + red gem 10. Together 70 activity points - the same
  four rows the 0229 scout read saw completed and unclaimed, now
  claimed by this unit.
- Claims, verified live: ONE grounded single tap on the Daily
  Login Claim button (norm 754,424) removed all four completed
  rows from the list at once. Activity star rose 0 to 70 (+70,
  exactly 4 tasks: 10 + 10 + 10 + 40), and the tab badge fell 4
  to 1. (2026-11-08 1753 correction: the "removed from the list"
  wording is superseded - the re-check read the four claimed rows
  sunk to the bottom of the list with green checkmarks, not
  removed; this unit did not scroll to the bottom. The one-tap
  claim and the +70 star delta stand as observed.) This is the third one-tap-multi-claim observation after
  the 1444 unit (one tap cleared two rows) and the 0914 unit
  (one tap cleared three gather rows). Whether the game
  batch-claims completed rows on one tap is inference from three
  observations, not a verified mechanism; the observed facts are
  the four rows leaving the list and the +70 star delta. The
  claim-each-task-individually rule stands until the mechanism is
  verified. Counter-evidence to Issue #171, commented there by
  the ticker pass (no duplicate comment here): the green Claim
  button responded at once in this session, like the 1444 and
  0914 sessions - responsiveness is session-dependent, not a
  global dead state. Closure of #171 belongs to the daily retro.
- 40-point activity chest, first verified 40-point chest claim in
  this line: with activity at 70, one grounded tap on the 40
  chest (norm 315,262) produced a CONGRATULATIONS receipt popup:
  "Congrats! You've scored double rewards 1 times this round!"
  Contents read live - gear x4, Iron Chest (SR) x4, Food Chest
  (SR) x4, Coin Chest (SR) x12, Crystal Ore 600, 5m speedup x2.
  Popup dismissed by tapping its banner. This confirms the 0914
  reading of Issue #208: the 0017 40-chest preview-only case was
  an already-claimed chest, and a claimable chest is claimed by
  tapping it for a receipt. Commented on Issue #208 by the ticker
  pass (no duplicate comment here); closure belongs to the daily
  retro.
- Closing state, read live about 16:28 local: activity 70,
  progress bar gold through 40, 40 chest icon open. Daily Tasks
  tab badge GONE. Next Refresh 01:32:58. The 80 chest sits 10
  points short. No completed row remains in view.
- Remaining tasks, read live, none actioned: Defeat any Doom Elite
  1 time(s) (0/1), Complete 1 Radar Task(s) (0/1), Help Allies 5
  Times (2/5), Recruit Heroes 1 Time(s) (0/1), all with blue Go
  buttons, none tapped. Rows below the fold were not re-read in
  this unit; per the 0229 scout full-list read they are Kill 5
  zombies on World Map, Attack a Commander (PvP, stays undone
  without the owner instruction), Gather Food / Iron / Coin
  x10,000, Train 100 units, Upgrade a Building, Research a tech,
  Obtain 1 Gear at SSR or better, Recruit Survivors 1 in the
  Tavern, Make any paid purchase once (red-line row, observed
  only, never to be actioned), Dispatch Trade Trucks 3 times,
  Plunder others' Secret Task reward 1 time, Perform Data
  Training on Drone 1 time.
- Ticker line "President HawksMav appointed Neimallah as
  Secretary of Development!" seen at the top during the chest
  receipt, observed only.
- Back-arrow grounding: the Mission screen back arrow grounds at
  norm (57, 938) in this capture; one tap returned to the base
  screen at once. No back-arrow point is standing across screens;
  re-ground fresh per screen.
- No diamonds spent, no money spent, no Go button tapped, no PvP
  task attempted, no paid-purchase row touched. Game left on the
  base screen.
- Follow-up: the 80-point chest needs 10 more activity points; the
  next tick re-checks the list for newly completed tasks. The
  one-tap-multi-claim mechanism stays unverified (three
  observations, no separate verification).

## What the 2026-11-08 1753 unit added - full-list re-check, claimed rows sink with green checks, 80 chest 10 short into the reset, partial

- Unit daily-missions-2026-11-07-1800 by ticker-1724, about 17:47
  to 17:53 local, status partial - the full daily task list was
  re-checked live top to bottom and nothing is newly completed
  since the 1628 unit, so nothing was claimed; activity stays 70
  and the 80-point chest stays 10 points short into the 18:00
  reset. Evidence in
  `_records_/2026-11-08/daily-missions/1753-queue-run.md` (commit
  5f3a904f4 on records/2026-11-08). Session cc-144 on the owner
  Mac mini (session cc-143, opened for the sweep unit of this
  pass, had closed by the time this unit started; a fresh session
  was opened). No device-access error, no different-device dialog,
  no login demanded. One control call failed first on a missing
  observation_id (stale_observation); retried with the screenshot
  observation_id, no input lost. LastWar was already running and
  selected, verified by list_apps and observe before any input.
- This is the same unit id the 1604 pass ran at 16:28 (partial,
  tracker untouched); sync re-produced it and this unit is its
  re-execution - the first observed duplicate execution of a unit
  already closed on the branch, recorded on Issue #465 by the
  planner-1740 pass. The branch keeps the ticker-1604 result (5
  items claimed including the 40 chest); the done file for this
  unit was NOT overwritten by this re-execution.
- Entry, read live about 17:47 local: base screen, power
  149,209,253 (unchanged from 17:12 and 17:40); food 490.8M, iron
  813.3M, coin 12.3M; diamonds 13.22K; cart 4,417; stamina 120;
  Season II 7d 00:13:44. Mission opened from the orange terminal
  on the base screen, grounded fresh at norm 51,863 in this unit's
  base view (the 1628 read grounded 52,863 - a 1-unit x variance
  between the two fresh groundings, recorded as observed, same
  point within rounding). The panel opened on the Main Tasks tab
  ("All tasks completed", Side Tasks all 0/1 with Go buttons, none
  actioned); the Daily Tasks tab was tapped to reach the daily list.
- Daily Tasks tab, read live about 17:48-17:52 local: Next Refresh
  00:11:55 falling to 00:08:22 across the unit, pointing at the
  18:00 local reset (new evidence for Issue #242, commented by
  this run). Activity star 70, progress bar gold through 40.
  Chests 40 / 80 / 120 / 160 / 200: the 40 chest claimed (open
  icon), 80, 120, 160, 200 unreached. Daily Tasks tab badge gone.
  Signed in as HidingAnt504 (Game Center binding).
- Full list, re-checked top to bottom in four scrolled views, no
  green Claim button anywhere: Defeat any Doom Elite 1 time(s)
  (0/1); Complete 1 Radar Task(s) (0/1); Help Allies 5 Times
  (2/5); Recruit Heroes 1 Time(s) (0/1); Kill 5 zombie(s) on World
  Map (0/5); Attack a Commander 1 time(s) (0/1); Gather Food
  x10,000 at resource tile (0/10000); Gather Iron x10,000 at
  resource tile (0/10000); Gather Coin x10,000 at resource tile
  (0/10000); Train 100 units of any level (0/100); Upgrade a
  Building 1 time(s) (0/1); Research a tech 1 time(s) (0/1);
  Obtain 1 Gear at SSR and/or better rarity (0/1); Recruit
  Survivors 1 time(s) in the Tavern (0/1); Make any paid purchase
  once (0/1); Dispatch Trade Trucks 3 time(s) (0/3); Plunder
  others' Secret Task reward 1 time(s) (0/1); Perform Data
  Training on Drone 1 time(s) (0/1). Every row carries a blue Go
  button, none tapped.
- Correction to the 1628 record, read live: claimed rows sit at
  the bottom of the list with a green checkmark - Daily Login
  (1/1) and Donate to Alliance Tech 5 times (5/5) seen with
  checks. The four rows claimed at 16:24 were not removed from
  the list, they sank to the bottom with a green check; the 1628
  unit did not scroll to the bottom, so it could not see them
  there. Commented on Issue #208 by this run (the chest-claim-path
  issue, which the 1628 evidence bears on); closure belongs to the
  daily retro.
- The 80-point chest needs 10 more activity points. The only
  in-list path before the reset would be Help Allies (2/5, three
  helps short); its owning unit help-2026-11-08-1830 is queued
  with not_before 18:30, after the reset, and helping is the help
  regular's work, not this unit's. The 80 chest expires unclaimed
  at the reset.
- No diamonds spent, no money spent, no Go button tapped, no PvP
  task attempted, no paid-purchase row touched, no research or
  building started. Game left on the base screen.
- Follow-up: the next tick re-checks the list in the new reset day.
  The one-tap-multi-claim mechanism stays unverified (three
  observations, no separate verification); this unit adds the
  checkmark-row observation, which the retro may use when it
  revisits Issues #171 and #208.

## What the 2026-11-09 1519 unit added - one-tap-multi-claim VERIFIED for rows and chests, activity 140, slow-drag scroll measured, partial

- Unit daily-missions-2026-11-08-1800 by ticker-1518, about 15:19 to 15:38 local, status done - the full daily task list was re-checked live top to bottom, every completed row was claimed, and the 40, 80 and 120 activity chests were all claimed. Activity star reads 140 at close; the 160 and 200 chests are unreached. Next Refresh read 02:38:33 at entry falling to 02:24:03 at close, pointing at the 18:00 local reset (another missions-panel pointer to the 18:00 reset, Issue #242). Evidence in `_records_/2026-11-09/daily-missions/1519-queue-run.md` (commit da249faca3 on records/2026-11-09). Session cc-300 then cc-303 on the owner Mac mini (cc-300 closed mid-unit, observe returned observation_unavailable; cc-303 was started, LastWar re-selected, no game state lost). One control call failed first on a missing observation_id (stale_observation); retried with the screenshot observation_id, no input lost.
- Entry, read live about 15:21 local: base screen, power 149,217,331; food 553.9M, iron 879.2M, coin 51.8M; diamonds 6,077. Mission opened from the orange terminal on the base screen, grounded fresh at norm 44,836 in this unit's base view. The panel opened directly on the Daily Tasks tab. At entry the Daily Tasks tab badge read 9 and four rows stood green with Claim buttons: Daily Login (1/1), Defeat any Doom Elite 1 time(s) (1/1), Complete 1 Radar Task(s) (1/1), Donate to Alliance Tech 5 times (5/5). The activity star read 0 and the progress bar was grey through all five chests.
- VERIFICATION of the one-tap-multi-claim mechanism, fourth observation, with before/after reads: one tap on Daily Login's Claim (norm 782,423) claimed all four green rows at once - the list reordered immediately to unclaimed rows, the badge fell 9 to 3, the star jumped to 140 and the bar went gold through 120. This is the fourth observation of the mechanism (see Issues #171 and #208): a single Claim tap claims every completed row in view, not just its own row. It is now verified by this unit's before/after reads, not merely observed. The claim-each-task-individually rule is superseded (see How it is done). The full list, re-checked top to bottom in seven slow-drag scrolled views: completed and claimed (green check at the bottom of the list) are Daily Login (1/1), Defeat any Doom Elite (1/1), Complete 1 Radar Task(s) (1/1), Donate to Alliance Tech 5 times (5/5), Help Allies 5 Times (5/5). Help Allies was not in the entry view; it stands claimed with a green check, either claimed by the same multi-claim tap or by an earlier pass this reset day - not distinguished in this unit.
- Activity chests, verified by a before/after crop of the chest row: at entry all five chests were closed with the star at 0; at close the 40, 80 and 120 chests stand open (lids up) and the 160 and 200 chests closed. The 40 tap produced a CONGRATULATIONS banner: gear part x10, red gem x40, wrench x1, blue crate x20, food crate x20, gold coins x12, crystal 2.8K, 5m speedup x8, with the line "You've scored double rewards 2 times this round!" The 80 tap showed its contents list: 5m Construction Speed-up x2, Iron Chest (SR) x4, Food Chest (SR) x4, Construction Part x1, Drone Parts x2, Crystal Ore 1.0K. The 120 chest already stood open before its tap, so it was claimed by the same cascade; tapping it showed its contents list: 5m Construction Speed-up x2, Iron Chest (SR) x6, Food Chest (SR) x6, Diamond x20, Drone Parts x2, Crystal Ore 1.2K. The chest cascade matches the row cascade - one tap claims every claimable chest, not just its own. Tapping an already-open chest shows its contents list and spends nothing.
- Incomplete, all with blue Go buttons, none tapped: Recruit Heroes 1 Time(s) (0/1); Kill 5 zombie(s) on World Map (0/5); Attack a Commander 1 time(s) (0/1); Gather Food x10,000 at resource tile (0/10000); Gather Iron x10,000 at resource tile (0/10000, seen only as the cut-off row between views); Gather Coin x10,000 at resource tile (0/10000); Train 100 units of any level (0/100); Upgrade a Building 1 time(s) (0/1); Research a tech 1 time(s) (0/1); Obtain 1 Gear at SSR and/or better rarity (0/1); Recruit Survivors 1 time(s) in the Tavern (0/1); Make any paid purchase once (0/1) - never to be tapped, red line; Dispatch Trade Trucks 3 time(s) (not seen in this unit's views - likely skipped between scroll steps, belongs to the trucks regular); Plunder others' Secret Task reward 1 time(s) (0/1); Perform Data Training on Drone 1 time(s) (0/1).
- Scroll method, rule R2 pivot: the scroll action and a fast drag both produced no list movement (two no-change attempts, method ended); the slow drag - mouse down, three stepped moves with 0.5s waits, mouse up - moved the list every time and is now the working scroll method for this panel. Downward drags to return to the top did not move the list; the chest row is fixed at the top of the panel, so chests were tapped from the bottom view.
- Coordinate note: coordinate inputs are normalized 0-1000, not window pixels. The first click at normalized 100,875 missed the back arrow; the grounded point 156,920 worked.
- Power read: 149,217,331 at entry, 149,317,331 at close - plus 100,000 during the unit. The 1609 scout read 149,217,331 again at 16:03 and 16:09, so the value moves both ways by exactly 100,000 within the hour; see the Total Power note in the 1609 scout fold and the comment on Issue #482. No cause is attributed from this unit.
- Follow-up: the next tick re-checks the list in the same reset day; the remaining rows belong to their owning regulars (trucks, help, training, donations, radar) or later ticks, not to this unit. The 160 chest needs 20 more activity points and the 200 chest 60 more; the only in-list paths before the 18:00 reset are Recruit Survivors (20), Plunder (30) and Drone Training (10) plus the gather/train rows, all incomplete and owned elsewhere. The Main Tasks tab plus the activity star in the same pass is the next unit's pin-down for the star-composition open question.
- No diamonds spent, no money spent, no Go button tapped, no PvP task attempted, no paid-purchase row touched, no research or building started. Game left on the base screen, power 149,317,331 at close.

## What the 2026-11-10 1426 unit added - four completed rows and three activity chests claimed, activity 120, fifth one-tap-multi-claim observation, done

- Unit daily-missions-2026-11-09-1800 by ticker-1424, about 14:26 to 14:37 local, status done - every completed row was claimed, the 40, 80 and 120 activity chests were all claimed, and the full daily list was re-checked live top to bottom. Activity star reads 120 at close; the 160 and 200 chests are unreached. Next Refresh read 03:31:56 at entry, pointing at the 18:00 local reset (another missions-panel pointer to the 18:00 reset, Issue #242). Evidence in `_records_/2026-11-10/daily-missions/1426-queue-run.md` (commit edd4659a3 on records/2026-11-10). Computer session cc-469 on the owner Mac mini. One control call failed first on a missing observation_id (stale_observation); retried with the screenshot observation_id, no input lost. One drag failed with "target app exited or restarted" (stale_observation); re-selected with activate and the app was still on the Mission screen, no game state lost. LastWar was already running on the base screen at entry: food 629.2M, iron 952.1M, coin 92.6M, gold 13.22K, power 148,765,978.
- Mission opened with the Daily Tasks badge at 7. Four rows stood completed with Claim buttons: Daily Login (1/1, 10 points plus red gem x10), Donate to Alliance Tech 5 times (5/5, 10 points plus 6.0K coins), Help Allies 5 Times (7/5, 10 points plus 5.0K iron plus 5.0K food), Greet Visitors 3 times (3/3, 10 points plus 5.0K iron plus 5.0K food).
- One Claim tap on Daily Login; on the re-read all four completed rows were gone from the list and the badge read 3, the three reachable chests. The per-row claim taps for the other three rows were not individually observed, so this unit alone does not re-verify the mechanism - possibly one Claim tap claims every completed row, or the list refreshed on claim. The end state is live-verified: no completed row with a Claim button remains anywhere in the list. This is the fifth observation consistent with the one-tap-multi-claim mechanism VERIFIED by the 1519 unit's before/after reads; the 1519 verification stands, this unit adds a consistent observation, not a new verification.
- Activity chests, each claimed with its reward popup read live:
  - 40 points: gear x10, red gem x40, wrench x1, blue crate x20, food crate x20, gold x12, crystal 2.8K, 5m speedup x8. The popup banner read "CONGRATULATIONS! You have scored double rewards 2 times this round!" The contents match the 2026-11-09 unit's 40 chest exactly.
  - 80 points: 5m Construction Speed-up x2, Iron Chest (SR) x4, Food Chest (SR) x4, Construction Part x1, Drone Parts x2, Crystal Ore 1.0K.
  - 120 points: 5m Construction Speed-up x2, Iron Chest (SR) x6, Food Chest (SR) x6, Diamond x20, Drone Parts x2, Crystal Ore 1.2K.
- Full list re-checked by scrolling to the bottom. The remaining tasks are all incomplete with Go buttons and were left undone per the activity metadata: Defeat any Doom Elite 1 time (0/1, stamina combat), Complete 1 Radar Task (0/1, the radar regular's own unit), Recruit Heroes 1 Time (0/1), Kill 5 zombies on World Map (0/5), Attack a Commander 1 time (0/1, PvP, never), Gather Food x10,000 (0/10000), Gather Iron x10,000 (0/10000), Gather Coin x10,000 (0/10000, gathering marches), Upgrade a Building 1 time (0/1, red line - never start buildings).
- Activity star 120 at close. The entry star reading was not cleanly captured (the opening screenshot was ambiguous), so no entry-to-close delta is claimed. The star-composition open question stands: the four claimed rows at 10 points each account for 40 of the 120, the other 80 are unexplained by this unit's reads - earlier claims this reset day, Main Tasks activity, or a stale header render are all still open.
- Returned to the base screen at close; HUD unchanged (food 629.2M, iron 952.1M, coin 92.6M).

## What the 2026-11-11 1638 unit added - two completed rows claimed on one tap, activity 100, list would not scroll, done

- Unit daily-missions-2026-11-10-1800 by ticker-1634, about 16:38 to 16:46 local, status done - every completed row was claimed and the visible list holds no Claim button; the below-fold rows were not re-read (see the scroll failure below), so the unit closes done on the visible list, not on a full-list re-check. Evidence in `_records_/2026-11-11/daily-missions/1638-queue-run.md` (commit 1fe3a5e69 on records/2026-11-11). Computer session cc-639 on the owner Mac mini, LastWar window 676414. No device-access error, no different-device dialog, no login demanded.
- Account verified live at entry: My Profile read Lv.30 [AP3x]Bears Lair, 149.2M power, VIP13, [AP3x]The Apex, Warzone #2110. The VIP screen seen on arrival was left open by an earlier session; no purchase touched.
- Entry, read live: Mission, Daily Tasks tab. Activity star 80, Next Refresh 01:19:37 (points to about 18:00 local - another missions-panel pointer to the 18:00 reset, Issue #242). Chests at 40 and 80 standing.
- Completed rows at entry: Help Allies 5 Times (20/5) with Claim, Kill 5 zombie(s) on World Map (5/5) with Claim. Row rewards shown: 10 activity points plus 5.0K iron plus 5.0K food each.
- One Claim tap on Help Allies 5 Times (normalized 791,414). On the re-read both completed rows were gone from the list and the activity star read 100, a rise of 20 points. The mechanism is unverified - possibly one Claim tap claims every completed row, or the list refreshed on claim. This is the same phenomenon the 2026-11-10 1426 unit recorded (one Claim tap, four completed rows gone). The end state is live-verified for the visible list: no completed row with a Claim button remains. This is the sixth observation consistent with the one-tap-multi-claim mechanism VERIFIED by the 1519 unit's before/after reads; the 1519 verification stands, this unit adds a consistent observation, not a new verification.
- Activity chests: the 40 point chest and the 80 point chest were each tapped and each opened a contents preview only, with no claim action - both were already claimed before this unit. 40 points: 5m Construction Speed-up x1, Iron Chest (SR) x2, Food Chest (SR) x2, Coin Chest (SR) x6, Drone Parts x2, Crystal Ore 600 - identical to the 0017 preview read, the second preview confirmation. 80 points: 5m Construction Speed-up, Iron Chest (SR), Food Chest (SR), Construction Part, Drone Parts, Crystal Ore 1.0K (counts partly OCR-garbled in the preview read) - matching the 1519/1426 claim contents in items. Preview contents and claim-receipt contents differ because receipts carry the double-rewards multiplier; the 1628 receipt (double x1) and the 1519/1426 receipts (double x2) already show receipts varying with the multiplier, so no contradiction is recorded here.
- Remaining tasks are all incomplete and were left undone per the activity metadata: Defeat any Doom Elite 1 time(s) (0/1, stamina combat), Recruit Heroes 1 Time(s) (0/1), Attack a Commander 1 time(s) (0/1, PvP, never), Gather Food x 10,000 at resource tile (0/10000, gathering march).
- List-scroll failure, new failure mode for this panel: below-fold rows were NOT re-read in this unit. The list would not scroll: a quick drag, a scroll action, and a slow staged mouse drag all produced no change (R2 pivot attempted, second variant also no-change). The fifth partially visible row is a Gather task at 0 progress. This contrasts with the 1519 slow-drag method, which moved the list every time - scroll responsiveness is session-dependent (like Claim responsiveness, Issue #171) or window-state dependent (Issue #650, Zoom-to-Fit precondition; this unit did not record the window state). The visible list holds no Claim button, so nothing claimable is known to remain. Next unit: re-ground the window state first (Zoom to Fit per #650), then retry the slow drag before concluding the below-fold rows hold nothing claimable.
- Close: returned to the base screen. HUD unchanged at close: food 689.4M, iron 1.0G, coin 136.7M, power 149,218,973, stamina 67. Claimed this unit: Help Allies 5 Times, Kill 5 zombie(s) on World Map - 20 activity points plus 10.0K iron plus 10.0K food by the row rewards shown; the zombie row's individual claim tap was not observed, only the end state (row gone, points up 20). Activity star 100 at close. The 120 point chest is not yet reached; the remaining incomplete tasks cannot reach it inside this unit's scope.
