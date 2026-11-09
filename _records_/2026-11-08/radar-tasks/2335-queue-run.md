---
title: Radar queue run 2335
created: 2026-11-09T07:49:00Z
modified: 2026-11-09T07:49:00Z
level: L0
version: 1.0.0
description: Ticker-2334 radar unit, release posture duel day 1, ordinary-task cycle cleared to 0 of 40, 44 claims, pins left unworked
status: unverified
---

# 2335 queue run - Radar tasks

Executor: ticker-2334. Unit: radar-2026-11-08-2203 (window duel
day 1 - radar release; live duel posture at 23:35 local is duel
day 1, Radar Training, radar_posture release per tools/duel.py).
Session window about 23:35 to 23:50 America/Los_Angeles.

## Performed

- Radar screen entered and verified live: Lv.13, radar points 267,
  stored tasks 39 of 40, stamina 120 (top right), restore line
  "12 Radar Task(s) will be restored in 05:59:54". Bottom bar at
  entry offered Quick Execute for 1 task (10 stamina).
- Release cycle, alternating Quick Execute and Claim All until the
  bar disappeared: executed 16 tasks in 6 batches (1, 5, 3, 2, 3,
  2) for 160 stamina; claimed 44 task rewards in 7 Claim All taps
  (11, 9, 8, 5, 5, 5, 1). Radar points 267 to 311 (+44, one per
  claim, as measured). Stored 39 of 40 to 0 of 40; pending rewards
  0; no bottom action bar at close.
- Free stamina claim taken once in the Regain Stamina panel
  (Remaining Today read 2 of 2 at entry, 75 stamina claimed;
  stamina 11 to 86 at that point). The 100 stamina for 300 rubies
  Buy button was never touched. Stamina items were not used
  (inventory counts read in the panel: 10-stamina x641,
  50-stamina x665). Stamina at close 36.
- Claimed rewards, summed from the seven CONGRATULATIONS popups:
  orange chest x50, radar coil x370, EXP 58.4M, blue triangle
  2,496, blue card 8.0K, 5m speedup x8, 1m speedup x50, iron
  14.0M, food about 11.7M, coin about 9.2M, Lv.1 chest x1.
- HUD cross-check on return to base: power 149,209,253 unchanged;
  food 501.9M to 513.8M (+11.9M), iron 824.0M to 838.3M (+14.3M),
  coin 15.8M to 25.2M (+9.4M) - consistent with the radar claim
  totals above plus march yields shown during Quick Execute
  (floating 660,000 / 1,000,000 / 2,300,000 lines).
- Returned to the base screen afterwards. No diamonds, money,
  speedups or other spending. No alliance diplomacy, no assembly,
  no teleport.

## Entry note - fresh grounding corrected the dish coordinate again

- First tap at norm 59,687 (estimated from the fresh screenshot)
  missed the dish and only showed a transient "Achievements 8/16
  Completed" tooltip; the radar did not open.
- Re-grounded from a magnified crop of the left icon column: the
  satellite dish icon with the red "10" badge sits at pixel about
  24,700 in the 642x951 window, i.e. norm 37,736. The second tap
  at norm 37,736 opened the radar on the first try. The profile
  coordinate (norm 62,727, measured 2026-10-29 in a 763x1050
  window) is stale in this window geometry; the correction is
  recorded here and left for the knowledge organizer to harden
  (tier-2 edit, not swept into this records commit).
- Observation: the dish badge read "10" at entry while stored was
  39 of 40 and only 1 task was Quick Executable - the badge number
  does not equal the stored count. What it counts is not
  established.
- One UI element noted but not touched: the gold icon with a NEW!
  badge at the top of the radar screen (about norm 295,60). Its
  function is still unknown; it is not part of this unit's work.

## Pin inventory (release rule, untapped - see Outcome)

- The radar map panned between reads throughout the unit, so the
  same pins reappeared in different screen positions; the closing
  inventory below is from the final clean screenshot, and earlier
  views showed the same classes.
- At close, 6 pins standing, none tapped: 2 blue arrow pins (one
  with a red dot), 2 orange skull pins (no red dots visible), 1
  portrait pin (a man's portrait in a blue frame, no red dot
  visible), 1 purple arrow pin (red dot not clearly visible).
- The brown circular animal-face pin inventoried on 2026-11-07
  (norm about 85,738) was not seen in this unit's map views; the
  map panned away from the southwest edge and it may be off-screen
  rather than gone.
- The pins were not worked because the unit's 15 minutes were
  spent on the ordinary-task release cycle (44 claims, 16
  executions, stored 39 of 40 to 0 of 40) and the device token
  expired at 23:50:29. They fall to the next radar unit under the
  release handling rule.

## Duel note

- The duel-score delta test (read VS panel, claim one batch, read
  again) is still owed: this unit did not visit the VS panel. If
  the in-game displayed value of 30,000 per task held, 44 claims
  would be about 1.32M duel points - stated here as an inference
  only, not a measurement. The duel-score unit in the inbox
  (duel-score-2026-11-08-2230) reads the VS panel separately.

## Closing reads

- Stored 0 of 40, pending rewards 0, radar points 311, stamina 36,
  restore line at entry 12 tasks in 05:59:54 (closing toast read
  "Fully restore at 11-9 23:39:11 local time", meaning unverified),
  tasks executed 16, tasks claimed 44, pins inventoried 6 untapped,
  free stamina claims taken 1 of 2.

## Outcome

Partial. The ordinary-task release cycle is fully done (stored
0 of 40, pending 0, bar gone, 44 claims, 16 executions) but the
release completion standard also requires every map pin closed,
and 6 pins stand untapped. The next radar unit continues with the
pins; the tracker is left untouched so radar stays due.

## Result stats

- target 1, achieved 0, resources_gained coin about 9.2M plus iron
  14.0M food about 11.7M EXP 58.4M, costs 160 stamina plus 1 free
  claim, verified yes, blocker_category time (unit cap reached with
  pins unworked), stored_tasks 0, tasks_executed 16,
  tasks_claimed 44, pins_inventoried 6, pins_worked 0, stamina 36,
  radar_points 311, restore_in_minutes 360, free_stamina_claims 1,
  device_takeovers 0
