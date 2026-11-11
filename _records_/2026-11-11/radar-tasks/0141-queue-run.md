---
title: Radar tasks queue run 0141
created: 2026-11-11T09:41:00Z
modified: 2026-11-11T09:41:00Z
version: 1.0.0
description: Ticker-0135 radar unit, duel day 3 release - 28 claims, 9 Quick Execute, stored cleared to 0/40, pins inventoried not worked, partial on time cap
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 01:35-01:41 PT
---

# Radar tasks queue run 0141 (ticker-0135)

Unit: radar-2026-11-10-2203. Status: partial.
Activity: radar-tasks. Posture: RELEASE (live duel day 3; unit
window label "duel day 3 - radar release" agrees with the live
posture this time, unlike the stale label the 2055 unit carried).

## Entry - first-try success

- The dish was re-grounded fresh from a current screenshot
  (visual grounding on the 642x951 window): centre norm
  (53,707), red badge 1. Move, wait 1 second, click - the
  radar opened on the first attempt. Entry verified by screen:
  Lv.13, radar points 375, stored 28/40, stamina 112/120.
- Note for the next unit: the dish sat at norm (53,707) this
  pass against (86,712) in the 2055 unit - the column shifts
  with the camera. Re-ground fresh every unit, never reuse
  either point blind.

## Release cycle - Claim All and Quick Execute interleaved

- Entry reads: Lv.13, radar points 375, stored 28/40, stamina
  112/120, restore "12 Radar Task(s) will be restored in
  04:03:00" / "Fully restore at 11-10 23:39:11 local time".
  An Achievements toast (8/16 Completed) overlayed the top
  of the screen at entry and faded on its own.
- Bar at entry presented Quick Execute: "complete 3 tasks,
  requires 30 Stamina".
- Quick Execute 1: 3 tasks, stamina 112 to 82 (30 spent, 10
  each). Stored 28/40 to 23/40 (down 5, not 3 - the extra 2
  match the pattern below). Bar flipped to Claim All: 5 task
  rewards pending (3 executed + 2 extra).
- Claim All 1: 5 rewards claimed. Radar points 375 to 380
  (+5, exactly 1 per claim). Stored 23/40 to 18/40 (down 5,
  matches). Rewards: coil x50, Hero EXP 6.6M, blue triangle
  225, item 800, iron 1.7M, food 1.0M, coin 1.0M. Bar flipped
  to Quick Execute: "complete 1 tasks, requires 10 Stamina".
- Quick Execute 2: 1 task, stamina 82 to 72 (10 spent). Bar
  flipped to Claim All: 5 task rewards pending (1 + 4 extra).
- Claim All 2: 5 rewards claimed. Radar points 380 to 385.
  Stored 18/40 to 13/40 (down 5, matches). Rewards: coil x50,
  Hero EXP 8.3M, item 3.2K, iron 3.5M, coin 770.4K, food
  475.2K. Bar flipped to Quick Execute: "complete 2 tasks,
  requires 20 Stamina".
- Quick Execute 3: 2 tasks, stamina 72 to 52 (20 spent). Bar
  flipped to Claim All: 5 task rewards pending (2 + 3 extra).
- Claim All 3: 5 rewards claimed. Radar points 385 to 390.
  Stored 13/40 to 8/40 (down 5, matches). Rewards: coil x50,
  Hero EXP 8.5M, item 2.4K, iron 792.0K, food 3.0M, coin
  831.6K. Bar flipped to Quick Execute: "complete 2 tasks,
  requires 20 Stamina".
- Quick Execute 4: 2 tasks, stamina 52 to 32 (20 spent). Bar
  flipped to Claim All: 5 task rewards pending (2 + 3 extra).
- Claim All 4: 5 rewards claimed. Radar points 390 to 395.
  Stored 8/40 to 3/40 (down 5, matches). Rewards: coil x50,
  Hero EXP 5.0M, blue triangle 408, item 800, iron 1.5M,
  food 664.8K, coin 1.0M. Bar flipped to Quick Execute:
  "complete 1 tasks, requires 10 Stamina".
- Quick Execute 5: 1 task, stamina 32 to 22 (10 spent). Bar
  flipped to Claim All: 5 task rewards pending (1 + 4 extra).
- Claim All 5: 5 rewards claimed. Radar points 395 to 400.
  Stored 3/40 to 0/40 (down 3 to zero). Rewards: coil x50,
  Hero EXP 4.8M, item 1.6K, blue triangle 585, food 1.9M,
  coin 1.2M, Lv.1 chest x2, iron 348.0K. Bar flipped to
  Claim All again: "3 task rewards can be claimed" - rewards
  kept appearing after stored hit 0.
- Claim All 6: 3 rewards claimed. Radar points 400 to 403.
  Stored 0/40 unchanged. Rewards: coil x30, blue triangle
  408, Hero EXP 2.0M, item 800, coin 702.0K, food 1.0M.
  After dismissal the bar showed NO offer - no Quick Execute,
  no Claim All. The release cycle is exhausted.

## The extra-rewards pattern - open question, strengthened

- Every Claim All paid more rewards than the tasks just
  executed: 5 pending after 3 executed, 5 after 1, 5 after 2,
  5 after 2, 5 after 1, and 3 after stored was already 0.
  Totals: 28 claimed against 9 executed - 19 extra rewards
  with no executed task behind them. The 2055 unit saw the
  same shape (27 claimed, 8 executed). Candidate sources:
  finished-task pins paying through the bar, tasks whose
  timers elapsed mid-unit, or pin-task rewards. Not assumed.
  The next release unit should watch whether the pending
  count drops when a pin is tapped - if pins feed the bar,
  working pins first changes the cycle.

## Totals (all live reads in this unit)

- Tasks claimed 28 (5 + 5 + 5 + 5 + 5 + 3). Radar points 375
  to 403 (+28, exactly 1 per claim, consistent across all
  six batches).
- Tasks executed via Quick Execute 9 (3 + 1 + 2 + 2 + 1).
  Stamina 112 to 22 at the last claim, 23 at close after 1
  point regenerated (90 spent, 10 per task).
- Stored 28/40 to 0/40. Restore line at close: 12 tasks in
  03:58:39, full restore 11-11 23:39:11 local.
- Resources gained: coin 1.0M + 770.4K + 831.6K + 1.0M +
  1.2M + 702.0K = 5,504,000; iron 1.7M + 3.5M + 792.0K +
  1.5M + 348.0K = 7,840,000; food 1.0M + 475.2K + 3.0M +
  664.8K + 1.9M + 1.0M = 8,040,000; Hero EXP 6.6M + 8.3M +
  8.5M + 5.0M + 4.8M + 2.0M = 35.2M; coils 50 x5 + 30 = 280;
  blue triangles 225 + 408 + 585 + 408 = 1,626; other item
  800 + 3.2K + 2.4K + 800 + 1.6K + 800 = 9.6K; Lv.1 chests 2.
- Free stamina claims 0 - stamina never bound (112 to 22
  via Quick Execute only).

## Pin inventory - inventoried, NOT worked (release rule unmet, hence partial)

- Pins seen across the unit's map views (about 10 distinct):
  portraits (ally, incl. [AP3x]TrapQueen97, [AP3x]Comandante,
  [AP3x]S...), blue arrow, orange arrow, orange axe, purple
  axe, purple skull, blue skull, green skull (x3 across
  views), grey skull. Red dots were present on most pins in
  the mid-unit views; the closing view showed 6 pins (portrait
  man, blue skull, blue arrow, orange arrow, orange axe,
  purple skull) with no red dot clearly visible on any of
  them in that frame - possibly angle/lighting, not a state
  change; not assumed.
- No pin was tapped in this unit: the release cycle (5 Quick
  Executes + 6 Claim Alls) filled the unit's time, and each
  pin needs its own tap-and-read. The release-day standard
  (every pin completed, claimed, or identified with a reason)
  is therefore NOT met - the unit closes partial, and the
  pins fall to the next radar unit.
- Per R7 the pins were deferred twice in one day inside
  their unit (2055, then this unit): the next radar unit
  (radar-2026-11-11-0203, not_before 02:03) must work pins
  FIRST, before any further Claim All / Quick Execute cycle.
  Duel score was NOT read before or after the claims (no VS
  panel visit), so the duel delta test (10,000 vs 30,000
  per task) is still owed.

## Outcome

Partial. The ordinary-task release ran cleanly (28 claims, 9
executes, stored cleared to 0/40, all closing figures live
reads), but the map pins were not worked, so the release-day
completion standard is not met. The tracker is left
untouched, so the next tick re-produces the radar regular and
the work resumes as a fresh unit. No diamonds or money spent.
No priced button tapped. No other activity's rewards touched.

## Result stats

- target 1, achieved 0, resources_gained coin 5,504,000 plus
  iron 7,840,000 plus food 8,040,000 plus Hero EXP 35.2M
  plus coils 280 plus blue triangles 1626 plus other item
  9.6K plus Lv.1 chests x2, costs stamina 90 plus about 7
  minutes, verified yes, blocker_category h, tasks_claimed
  28, tasks_executed 9, pins_inventoried 10, pins_worked 0,
  free_stamina_claims 0, radar_points_before 375,
  radar_points_after 403, stored_before 28, stored_after 0,
  stamina_before 112, stamina_after 23, duel_score_before
  not-read, duel_score_after not-read, entry_attempts 1,
  device_takeovers 0
