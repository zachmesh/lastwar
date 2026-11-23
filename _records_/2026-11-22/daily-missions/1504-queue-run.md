---
title: Daily missions queue run 1504
created: 2026-11-22T23:20:00Z
modified: 2026-11-22T23:20:00Z
level: L0
version: 1.0.0
description: Daily-missions unit daily-missions-2026-11-21-1800, ticker-1504, six completed rows claimed on one tap, activity 0 to 90, 40 and 80 activity chests claimed, remaining tasks belong to other regulars
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 15:16-15:19 PT
  - source: unit daily-missions-2026-11-21-1800 in _queue_/claimed
  - source: _activities_/daily-missions/INDEX.md, Mission procedure
---

# Daily missions queue run 1504 (ticker-1504)

Unit daily-missions-2026-11-21-1800, regular
daily-missions, segment 3. Executor ticker-1504.
Computer session cc-166 on the owner Mac mini.
Session window about 15:16 to 15:19 PT. Game in
window mode (642x951, window 127196), background
input working. No "active on a different device"
dialog, no login demanded.

## Outcome

Partial - everything claimable at entry was claimed
and verified live, but the regular's task list is
not fully done: the remaining tasks are incomplete
and belong to other regulars or later ticks, so the
tracker is untouched and the next tick re-checks
the list (precedent: the 2026-11-04 0914 and
2026-11-08 1628 units).

## Entry state - read live

- Base screen at entry: power 147,972,269; food
  765.4M, iron 1.1G, coin 109.2M, gold bricks 17.72K (diamonds 4,706 per the seq-18 resolution in the KO 1432 fold),
  cart 6,436; stamina 120; Build: Oil Well [0/1]
  banner; Season II timer 02:44:32.
- Mission opened from the orange terminal on the
  base screen, grounded fresh at norm 45,846 in
  this base view. Panel opened directly on the
  Daily Tasks tab.
- Daily Tasks tab badge 6. Next Refresh 02:43:58
  at entry (02:42:01 at close), pointing at the
  18:00 local reset. Activity star 0. Chests 40 /
  80 / 120 / 160 / 200 all unreached.
- Completed green rows with Claim buttons at entry:
  Daily Login (1/1, star 10 + red gem 10); Donate
  to Alliance Tech 5 times (5/5, star 10 + coin
  6.0K); Help Allies 5 Times (5/5, star 10 + food
  5.0K + iron 5.0K); Greet Visitors 3 times (3/3,
  star 10 + food 5.0K + iron 5.0K); plus a fifth
  green row partly visible at the bottom edge of
  the view. The badge count of 6 means one more
  completed row sat below the fold.

## Claims - verified live

- ONE tap on the Daily Login Claim button (norm
  794,415) claimed every completed row: the list
  reordered at once to unclaimed rows, the tab
  badge fell 6 to gone, and the activity star rose
  0 to 90. Seventh observation of the verified
  one-tap-multi-claim mechanism (see Issues #171
  and #208; no new comment - the mechanism is
  already verified, and this unit adds no new
  evidence about it).
- Star arithmetic, read live: 0 to 90. The four
  named rows account for 40; the remaining +50 is
  NOT fully pinned down in this unit: the fifth
  visible row plus one below-fold row together
  contribute 50, which fits VIP Activated at 40
  plus one 10-point row (the 0229 scout read
  lists VIP Activated at star 40), but neither
  row's identity was read live before the claim -
  the partial row's text was cut off and the
  below-fold row was never seen. The claimed rows
  sit at the bottom of the list with green checks
  per the 1753 correction; this unit scrolled
  partway (Kill 5 zombies, Attack a Commander,
  Gather Food/Iron/Coin, Upgrade a Building all
  0/x with Go buttons) but did not reach the
  bottom, so the six claimed rows are NOT
  individually enumerated here. Rows claimed: 6
  by badge and star delta; 4 named, 2 inferred
  by arithmetic only.
- 40-point activity chest: tapped at norm 311,268
  with activity at 90. CONGRATULATIONS receipt
  popup read live: "Congrats! You've scored
  double rewards 1 times this round!" Contents:
  gear x6, rocket x1, wrench x2, blue crate x10,
  food crate x10, gold coins x6, Crystal Ore
  1.6K, 5m speedup x5. Popup dismissed by
  tapping its banner.
- 80-point activity chest: the single 40-chest tap
  claimed it by cascade (precedent 1519). Verified
  by tapping the 80 chest at norm 452,268: it
  opened only a contents preview, not a receipt -
  5m Construction Speed-up x2, Iron Chest (SR)
  x4, Food Chest (SR) x4, Construction Part x1,
  Drone Parts x2, Crystal Ore 1.0K, identical to
  the 1519/1426 80-chest contents. Preview
  dismissed by tapping its chest icon. No second
  receipt exists for the 80 chest, and none is
  claimed.
- Closing state, read live: activity 90, progress
  bar gold through 80, 40 and 80 chest icons open,
  120/160/200 unreached. Daily Tasks tab badge
  gone. Next Refresh 02:42:01.
- Remaining tasks, read live, none actioned:
  Defeat any Doom Elite 1 time(s) (0/1), Complete
  1 Radar Task(s) (0/1), Recruit Heroes 1 Time(s)
  (0/1), Kill 5 zombie(s) on World Map (0/5),
  Attack a Commander 1 time(s) (0/1, PvP, stays
  undone without the owner instruction), Gather
  Food / Iron / Coin x10,000 at resource tile
  (0/10000 each), Upgrade a Building 1 time(s)
  (0/1). Rows below Upgrade a Building were not
  re-read in this unit. Make any paid purchase
  once was not seen in this unit's views; it is a
  red-line row, observed only, never to be
  actioned.
- No diamonds spent, no money spent, no Go button
  tapped, no PvP task attempted, no paid-purchase
  row touched, no research or building started.
  Game left on the base screen.

## Pass notes

- Tool currency: this pass ran queue.py from a fresh
  main worktree (ticker-1504-main, detached HEAD
  7bf9f5b86, main including PR #825) because the
  live tree's tools/queue.py is still stale against
  main's _tools_/queue.py after PR #824 (issue
  #694 guard); the 1440 planner run documented the
  same stale state. Records worktree
  ticker-1504-delivery at the records/2026-11-22
  tip 3875a3ad1.
- Sync: reaped 0, expired 3, due 24, produced 0,
  already queued all 24. Stats: inbox 93, claimed
  0, done 2887; newest finished 22:08:09Z, 64
  minutes old, evidence not stale.
- Zombie seeding: none. No zombie-invasion unit in
  inbox or claimed; the Glacieradon chain
  zombie-2026-11-10 closed 2026-11-14 when the
  event ended (unit 037), and no Zombie Invasion
  tab has been seen since. Zombie Siege 23:15
  today is a different event (open Issue #814).
- Own PRs first: PR #821 (records: 2026-11-22)
  open, mergeable, clean, 0 comments - no question
  addressed to this job. No other open PR names
  this job as Owner.
- Read receipt (issue #737): the newest
  queue-ticker record per the tool is
  _records_/2026-11-19/queue-ticker/2304-queue-run.md
  (device-offline failure record); read and receipt
  recorded before claim. The newest execution
  record, alliance-duel/1415-queue-run.md, was also
  read: star-ceremony unit, partial at ceremony
  step 7 of 13, successor star-ceremony-1430 in
  inbox.

## Result stats

- target: claim all completed daily tasks and every reachable activity chest for the reset day
- achieved: 6 completed rows claimed on one tap, activity 0 to 90, 40 and 80 chests claimed
- resources_gained: 40-chest receipt (gear x6, rocket x1, wrench x2, blue crate x10, food crate x10, gold x6, Crystal Ore 1.6K, 5m speedup x5) plus 80-chest contents by cascade (5m speedup x2, Iron Chest SR x4, Food Chest SR x4, Construction Part x1, Drone Parts x2, Crystal Ore 1.0K); task rewards star 90, red gem 10, coin 6.0K, food 10.0K, iron 10.0K (from the four named rows; the two unidentified rows' rewards not itemised)
- points: 90
- costs: about 5 minutes device time, no spend, no items
- verified: yes (badge, star, chest states and receipt read live in this unit)
- blocker_category: h (by-design partial - task list not fully done, remaining tasks belong to other regulars)
- activity_before: 0
- activity_after: 90
- rows_claimed: 6
- rows_named: Daily Login, Donate to Alliance Tech 5 times, Help Allies 5 Times, Greet Visitors 3 times
- rows_unidentified: 2
- chests_claimed: 40, 80
- chests_unreached: 120, 160, 200
- next_refresh: 02:42:01
