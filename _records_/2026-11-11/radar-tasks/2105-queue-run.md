---
title: Radar queue run 2105
created: 2026-11-12T05:13:00Z
modified: 2026-11-12T05:13:00Z
version: 1.0.0
description: Ticker-2105 radar unit, duel day 4 stack - entry recovered by fresh grounding plus exact-pointer tap, 5 tasks Quick Executed, 7 rewards stacked unclaimed, Claim All blocker named
status: unverified
---

# Radar - ticker-2105, 21:05 to 21:12 PST

Unit radar-2026-11-11-1803, executor ticker-2105. Status
done: the stack posture is complete - the only Quick Execute
offer was run, nothing was claimed, and the closing reads and
pin inventory are recorded. Computer session cc-667, windowed
642x951 play throughout. No device dialog, no login demand,
no Touch ID, no password typed.

## Posture

- tools/duel.py --json at 21:05: duel day 4, theme Train
  Heroes, radar_posture stack. On a stack day radar tasks
  are completed but NOT claimed, and map pins stay untapped.
- The unit file's window text still reads "duel day 3 -
  radar release" - stale against the live day-4 stack
  posture. The live duel.py read governs; a release-day
  claim here would have been wrong. Same staleness as the
  1805 unit noted.

## Entry - changed method per rule R2

- The 1805 unit closed partial on this same blocker: two
  entry attempts at stale coordinates opened Special Forces
  / Tech instead of radar (47,242, then 62,727). This unit
  is the second consecutive partial with that blocker, so
  it arrived with a changed method.
- Changed method: the dish icon was re-grounded from a
  fresh base screenshot (two visual grounding calls - the
  full window screenshot, then the cropped left column),
  landing at norm (55,702), close to the 0141 unit's
  (53,707) - the column shifts with the camera, so fresh
  grounding every unit is confirmed again. The tap was
  sent as an exact-pointer tap (snap_to_control false) so
  no accessibility snap could redirect it onto a neighbour.
- Result: the radar screen opened on the first tap.
  Entry verified: Lv.13, radar points 427, stored 1/40,
  stamina 60/120, restore "12 Radar Task(s) will be
  restored in 02:29:47".
- Lesson for the profile (not edited here - tier 2):
  exact-pointer taps belong in the entry section alongside
  fresh grounding; the default snap may have contributed
  to the 1805 mis-taps.

## Execution - stack posture

- Quick Execute tapped once on the offer "You can complete
  5 tasks, requires 50 Stamina". Stamina 60 to 11 (50
  spent, 5 x 10, plus 1 regen tick). The bar flipped to
  "7 task rewards can be claimed" with Claim All: 5
  executed plus 2 extra, the same +2 pattern the 0141
  release unit recorded.
- Claim All was NOT tapped - stack posture. After a 60
  second wait and re-observation the bar still offered
  Claim All only, no Quick Execute re-offer (the
  2026-10-31 single-offer trap, 7 pending). The free
  stamina claim was NOT taken: stamina is not the
  blocker here, the bar offer is, and the free claim
  (2/day) is not spent on a non-blocker.
- Stored-count puzzle, same as the 1233 unit found:
  stored read 1/40 at entry and still 1/40 after 5 tasks
  executed. The stored counter does not track the
  executed tasks; the bottom bar offer is the authority.
  The 1233 unit cleared stored to 0/40 at its close, so
  the counter also drifted 0 to 1 between units without
  a restore landing (next restore in about 2.5 hours).

## Pins - inventoried, untapped (stack rule)

- Purple skull pin, top centre, norm (506,315).
- Grey skull pin with red dot, top right, norm (826,336).
- Green skull pin with red dot, left, norm (312,573).
- Purple portrait (man) pin, right, norm (763,505).
- Purple bull/horn pin, bottom centre, norm (498,647).
- Small round brown pin seen at entry, norm (86,725),
  not visible in the close view (map drift); same
  description as the 0505 unit's unresponsive pin at
  (129,780) - left for the release-day unit to work.
- Alliance portraits on the map ([AP3x]JerryLog0g3xKaBoom420,
  [AP3x]SkruzBRZ, [AP3x]Shimmer Box, [AP3x]K9LJ) are
  member bases, not task pins.

## Closing reads

- Stored 1/40, pending rewards 7 (unclaimed, stacked for
  the day-5 release), radar points 427 (unchanged - no
  claims, correct for stack), stamina 11/120, restore
  "12 Radar Task(s) will be restored in 02:26:49".
- Exited with the home button. Base HUD re-read on exit:
  food 697.1M, power 149,218,973, task "Build: Oil Well
  [0/1]".

## Result stats

- target: 5 tasks executed per the stack posture
  (complete, do not claim), stored tasks read
- achieved: 5 tasks executed, 0 claimed
- resources_gained: 7 rewards stacked, unclaimed
  (for the day-5 release unit)
- points: 0
- costs: about 7 minutes, no items spent
- verified: yes (all closing figures read live on
  screen inside this unit)
- tasks_executed 5, tasks_claimed 0, pins_inventoried 6,
  pins_worked 0, free_stamina_claims 0,
  radar_points_before 427, radar_points_after 427,
  stored_before 1, stored_after 1, stamina_before 60,
  stamina_after 11, pending_rewards 7
- follow_up: the 7 pending rewards await the day-5
  release unit; the next radar unit opens with the Claim
  All block (7 pending, no Quick Execute offer) as its
  opening read, and works the pins listed above.
