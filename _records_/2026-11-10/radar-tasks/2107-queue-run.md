---
title: Radar tasks queue run 2107
created: 2026-11-11T05:07:00Z
modified: 2026-11-11T05:07:00Z
version: 1.0.0
description: Ticker-2055 radar unit, duel day 3 release - 27 claims, 8 Quick Execute, pins inventoried not worked, partial on time cap
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 20:58-21:07 PT
---

# Radar tasks queue run 2107 (ticker-2055)

Unit: radar-2026-11-10-1803. Status: partial.
Activity: radar-tasks. Posture: RELEASE (live duel day 3, Age of
Science; duel.py radar_posture release at 21:02 PT).

## Posture correction - stale window label

- The unit's window text said "duel day 2 - radar stack", stamped
  at production (06:42 PT) for an 18:03 slot. The duel day
  rolled over at 18:00 PT, so by execution time (20:58) the live
  posture was day 3 release. The live duel.py read governed,
  not the label: the stack was released, not stacked. A unit
  produced before a duel-day rollover carries a stale posture
  label - filed as tooling Issue #603 (see below); the next unit
  must re-read duel.py live before acting, as this one did.
- Duel score was NOT read before or after the claims (no VS
  panel visit - the release itself took the unit's time), so
  the duel delta test (10,000 vs 30,000 per task) is still
  owed.

## Entry - changed method, first-try success (R2)

- The 0318 unit (ticker-0304) failed entry twice at inherited
  points (34,324) and (52,694): both taps delivered as map
  drags. This unit used the changed method the 0318 record
  required: the dish was re-grounded fresh from a current
  screenshot (3x crop of the left icon column), centre
  measured at norm (86,712) in the 642x951 window, then
  move, wait 1 second, click.
- The radar opened on the first attempt. Entry verified by
  screen: Lv.13, radar points 348, stored 35/40, stamina 120.
- Note for the next unit: in this window size the dish sits
  near norm (86,712), but the column shifts with the camera -
  re-ground fresh every unit, never reuse this point blind.
- The dish carried a red badge 11 at entry.

## Release cycle - Claim All and Quick Execute interleaved

- Entry reads: Lv.13, radar points 348, stored 35/40, stamina
  120/120, restore "12 Radar Task(s) will be restored in
  02:35:45" (OCR) / "Fully restore at 11-10 23:39:11 local
  time" (on-screen line).
- Bar at entry presented Claim All (14 task rewards) with no
  Quick Execute offer - the 2026-10-31 trap shape, but on a
  release day Claim All is the correct first action.
- Claim All 1: 14 rewards claimed. Radar points 348 to 362
  (+14, exactly 1 per claim). Stored 35/40 to 26/40 (down 9,
  not 14 - mismatch noted, unexplained; the 5 may be pin-task
  rewards never counted in stored, not assumed). Rewards:
  gold chest x50, coil x130, Hero EXP 21.0M, item 3.8K, 5m
  speedup x4, 1m speedup x25, Lv.2 chest x1, blue triangle
  540, iron 4.2M, food 5.6M, coin 2.6M, Lv.1 chest x2.
  Bar flipped to Quick Execute: "complete 4 tasks, requires
  40 Stamina".
- Quick Execute 1: 4 tasks, stamina 120 to 80 (40 spent, 10
  each). Bar flipped to Claim All: 6 task rewards pending
  (4 executed + 2 extra - the extra 2 are unexplained, same
  pattern as the following cycles; possibly tasks whose
  timers elapsed mid-unit, not assumed).
- Claim All 2: 6 rewards claimed. Radar points 362 to 368.
  Stored 26/40 to 20/40 (down 6, matches). Rewards: coil
  x50, Hero EXP 8.7M, item 800, 5m speedup x6, 1m speedup
  x65, iron 2.7M, coin 966.0K, food 1.9M. Bar flipped to
  Quick Execute: "complete 3 tasks, requires 30 Stamina".
- Quick Execute 2: 3 tasks, stamina 80 to 50 (30 spent). Bar
  flipped to Claim All: 4 task rewards pending (3 + 1 extra).
- Claim All 3: 4 rewards claimed. Radar points 368 to 372.
  Stored 20/40 to 16/40 (down 4, matches). Rewards: coil
  x40, Hero EXP 5.6M, item 800, blue triangle 360, iron
  1.1M, food 1.1M, coin 1.1M, Lv.1 chest x2. Bar flipped to
  Quick Execute: "complete 1 tasks, requires 10 Stamina".
- Quick Execute 3: 1 task, stamina 50 to 40 (10 spent). Bar
  flipped to Claim All: 3 task rewards pending (1 + 2 extra).
- Claim All 4: 3 rewards claimed. Radar points 372 to 375.
  Stored 16/40 to 13/40 (down 3, matches). Rewards: coil
  x30, Hero EXP 4.3M, item 800, blue triangle 225, iron
  1.7M, food 1.1M, coin 686.4K. Bar flipped to Quick
  Execute: "complete 2 tasks, requires 20 Stamina" - the
  cycle continues, but the unit was at its time cap, so it
  stops here with 2 executable tasks left for the next unit.

## Totals (all live reads in this unit)

- Tasks claimed 27 (14 + 6 + 4 + 3). Radar points 348 to 375
  (+27, exactly 1 per claim, consistent across all four
  batches).
- Tasks executed via Quick Execute 8 (4 + 3 + 1). Stamina
  120 to 40 (80 spent, 10 per task).
- Stored 35/40 to 13/40. Restore line at close: 12 tasks in
  02:32:16, full restore 23:39:11 local.
- Resources gained: coin 2.6M + 966.0K + 1.1M + 686.4K =
  5,352,400; iron 4.2M + 2.7M + 1.1M + 1.7M = 9.7M; food
  5.6M + 1.9M + 1.1M + 348.0K = 8,948,000;
  Hero EXP 21.0M + 8.7M + 5.6M + 4.3M = 39.6M; coils 250;
  blue triangles 540 + 360 + 225 = 1,125; 5m speedups 10;
  1m speedups 90; Lv.2 chest 1; Lv.1 chests 4; gold chest 50;
  other item 3.8K + 800 + 800 = 5.4K.
- Free stamina claims 0 - stamina never bound (120 to 40
  via Quick Execute only).

## Pin inventory - inventoried, NOT worked (stack rule does not apply; release rule unmet, hence partial)

- First view (entry): 15 pins, every one carrying a red dot,
  none tapped. Top cluster: portrait [AP3x]Mesut... (red),
  blue signal pin (red), portrait [AP3x]TrapQueen97 (red),
  orange arrow pin (red), purple axe pin (red), teal skull
  pin (red), orange skull pin (red); right: grey skull pin
  (red); middle: portrait [AP3x]Amarky257 (red); left-middle:
  orange fist pin [AP3x]...Landmine (red), portrait
  [AP3x]Cap... (red), orange skull pin (red), portrait (red),
  purple fist pin (red); bottom-left: green skull pin (red).
- Later views (map re-centred after the Quick Execute cycles)
  showed 11 pins in frame: orange skull, blue arrow, orange
  arrow, purple axe, portrait (man), blue skull, orange
  arrow, green skull, orange arrow, portrait [AP3x]SAPPER3006,
  purple skull - the same set re-laid-out, some pins
  off-frame. Red dots were present on most but not all pins
  in the later view (blue arrow, blue skull and two orange
  arrows showed no red dot in frame - possibly angle/lighting,
  not a state change; not assumed).
- No pin was tapped in this unit: the release cycle (4 Claim
  Alls + 3 Quick Executes) filled the unit, and each pin
  needs its own tap-and-read. The release-day standard (every
  pin completed, claimed, or identified with a reason) is
  therefore NOT met - the unit closes partial, and the pins
  plus the 2 remaining Quick Execute tasks fall to the next
  radar unit (radar-2026-11-10-2203 in inbox), which inherits
  this inventory as its checklist.

## Outcome

Partial. The release cycle ran cleanly (27 claims, 8 executes,
all closing figures live reads), but the map pins were not
worked and 2 executable tasks remain, so the release-day
completion standard is not met. The tracker is left
untouched, so the next tick re-produces the radar regular and
the work resumes as a fresh unit. No diamonds or money spent.
No priced button tapped. No other activity's rewards touched.

## Result stats

- target 1, achieved 0, resources_gained coin 5,352,400 plus
  iron 9.7M plus food 8,948,000 plus Hero EXP 39.6M plus
  coils 250 plus blue triangles 1125 plus speedups 5m x10
  plus 1m x90 plus chests Lv.2 x1 plus Lv.1 x4 plus gold
  chest x50, costs stamina 80 plus about 10 minutes,
  verified yes, blocker_category h, tasks_claimed 27,
  tasks_executed 8, pins_inventoried 15, pins_worked 0,
  free_stamina_claims 0, radar_points_before 348,
  radar_points_after 375, stored_before 35, stored_after 13,
  stamina_before 120, stamina_after 40, duel_score_before
  not-read, duel_score_after not-read, entry_attempts 1,
  device_takeovers 0
