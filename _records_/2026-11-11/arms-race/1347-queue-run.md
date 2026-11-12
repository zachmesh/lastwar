---
title: Arms race queue run 1347
created: 2026-11-11T21:47:00Z
modified: 2026-11-11T21:57:00Z
version: 1.0.0
description: Ticker-1332 arms-race unit - entry failed, Mall opened instead of Events, phase never read, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 13:47-13:57 PT
---

# Arms race queue run 1347 (ticker-1332)

Unit: arms-race-2026-11-11-1003. Status: partial.
Activity: arms-race. Computer session cc-620.

## What happened

- This unit is the first executed unit of the current phase
  (phases rotate every 4 hours; the Tech Research phase ended
  about 06:00, and this unit's window expires 22:03Z, so the
  live phase ends about 14:00 PT). The phase was NEVER read:
  no phase name, no score, no thresholds, no timer, no scoring
  table was seen in this unit.
- Entry failed at the first step. On the base screen (Iron Mine
  Lv.27 still selected from the training unit), the visually
  grounded "Events icon" box (612-678, 28-95) was tapped at
  (645,62) and opened the MALL / HOT DEALS store page instead
  of the Events hub - "Visit the Last War Store for more
  rewards!", subtabs Official Event / Weekly Deal / Super
  Monthly Pass / Weekly Pass / Diamond, a check-in banner with
  a Go button. The grounded box was the store icon, not
  Events. Nothing on the Mall page was tapped (no Go, no
  subtab, no purchase) except the exit attempts below.
- Exit attempts, all no-change: back arrow at (262,958) twice
  (once snap_to_control=false, once default snap - the second
  tap drew the guidance that background clicks do not reach
  some controls and to use click_element or the keyboard);
  HOT DEALS tab at (340,56) once. A click_element for label
  "HOT DEALS" failed - no enabled control carries that label
  (OCR text is not a control). The banner carousel did advance
  between screenshots (check-in banner to a "1000 POINTS" card),
  which may be auto-rotation rather than a tap effect; no tab
  switch and no exit was observed.
- Exit found, and the exit lesson: the Mall back arrow grounds
  precisely at (316,952) - the two failed taps at (262,958)
  missed the button entirely (its box is x 300-333), they were
  not a focus failure. One tap at (316,952) returned to the
  base screen at once. The (262,958) point is retired as a Mall
  exit; the (326,948) radar-map back arrow from the training
  unit is a different button on a different screen and stands.
- Events icon, correctly located this time: on the base screen
  the golden icon with the red "3" badge and the "Events" label
  sits at (707,146). Two taps there - snap_to_control=false,
  then default snap - both produced no change (the second drew
  the background-click guidance). Per R2 the point method ends
  here; the next unit needs a different entry route (a
  foreground click, or the Events entry from another screen),
  not a third tap on (707,146). The (645,62) point from this
  unit's first attempt opens the Mall and is retired as an
  Events entry.
- The game was left on the base screen. No diamonds or money
  spent, no speedup burned, no pack bought, no chest claimed.
  No different-device dialog, no login or verification
  demanded.

## Not done - stated plainly

- Phase, score, thresholds and timer unread; the R4
  phase-start judgement for this phase was not made in this
  unit. Tier-3 target unknown; no scoring work done; no
  rewards claimed; completion sweep not run.
- The phase ends about 14:00 PT, minutes after this unit
  closes, so the next arms-race unit runs in the NEXT phase
  and reads fresh in any case. The miss for this phase is a
  late-pickup entry failure, not a red-line verdict.
- Next-unit instruction: the Events icon must be re-grounded
  fresh from the base screen - the (645,62) point opens the
  Mall and is retired as an Events entry. The (707,146) point
  is the labelled Events icon but took two no-change taps in
  this unit, so the next unit must change the entry route
  before tapping it again (foreground click or another screen's
  Events entry), per R2. If the Mall opens again, exit with the
  back arrow at (316,952), not (262,958). The 0535 unit's
  (934,160) windowed-mode grounding does not apply.

## Result stats

- target read live phase and score, meet tier-3 target just enough, claim earned rewards
- achieved phase never read, no scoring, no claims
- resources_gained none
- points 0
- costs about 9 minutes
- verified no - no live phase read in this unit
- blocker_category c
- phase unknown, score_before unknown, score_after unknown, device_takeovers 0
