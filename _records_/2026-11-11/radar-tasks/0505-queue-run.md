---
title: Radar tasks queue run 0505
created: 2026-11-11T13:05:00Z
modified: 2026-11-11T13:18:00Z
version: 1.0.0
description: Ticker-0504 radar unit, duel day 3 release - stored already 0/40, no bar offer, one pin visible and unresponsive to three tap variants, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 05:05-05:18 PT
---

# Radar tasks queue run 0505 (ticker-0504)

Unit: radar-2026-11-11-0203. Status: partial.
Activity: radar-tasks. Posture: RELEASE (duel day 3, unit window
label "duel day 3 - radar release" agrees with the live posture).

## Entry - first-try success, with a coordinate lesson

- The game was left on the Alliance Tech screens by the previous
  pass. Closed the tech detail panel and the tech list panel, then
  the Alliance screen, back to base (Total Power 149,118,973).
- The dish was re-grounded fresh from a current screenshot:
  centre norm (53,718). One tap opened the radar on the first
  attempt. Entry verified by screen: Lv.13, radar points 403,
  stored 0/40, stamina 59/120.
- Coordinate lesson, worth keeping: computer.control coordinates
  are NORMALIZED 0-1000 of the window, not pixels. Early clicks
  sent as pixel values (547,147) landed at norm (547,147) and
  missed the X; the grounded norm (844,150) closed the panel.
  The 0141 record's norm (53,707) dish point agrees with this
  unit's (53,718) - the column is stable this morning.

## Release cycle - nothing to claim

- Entry reads: Lv.13, radar points 403 (matches the 0141 close),
  stored 0/40, stamina 59/120, restore "12 Radar Task(s) will be
  restored in 00:30:45" / "Fully restore at 11-12 05:39:11 local
  time". The 0141 unit had already cleared stored to 0/40 and
  claimed 28 tasks; no new tasks had restored yet (next restore
  lands about 05:39 local).
- No bottom bar offer appeared at any point - no Claim All, no
  Quick Execute. Radar points unchanged at 403 at close. There
  was nothing to execute or claim in this unit; the release cycle
  is exhausted until the 05:39 restore.

## Pins - worked first per R7, unresponsive (release rule unmet, hence partial)

- Only ONE pin is visible in this map view: a small round
  brown portrait-like pin at the lower left, norm (129,780).
  The six pins inventoried by the 0141 unit (portrait man, blue
  skull, blue arrow, orange arrow, orange axe, purple skull)
  are NOT visible in this frame - the map view differs from the
  0141 unit's views, and no pan was attempted inside the time
  cap.
- Three tap variants on the visible pin, all no-change: (1) a
  first tap at norm (90,750), mis-aimed off the grounded point;
  (2) a tap at the grounded centre (129,780) with
  snap_to_control false; (3) a tap at the same point with the
  default snap. No bottom card opened, no state change, the pin
  still stands. Per R2 the tap method is ended at this point
  inside the unit; the next radar unit must pivot - re-ground
  the pin fresh, try a long-press, or pan the map to the 0141
  pins before tapping again.
- Whether the pin is a non-interactive map marker or a tap
  that needs a different gesture is NOT settled - not assumed.
  Duel score was NOT read before or after (no VS panel visit),
  so the duel delta test (10,000 vs 30,000 per task) is still
  owed.

## Outcome

Partial. The release cycle is genuinely exhausted (stored 0/40,
no bar offer, points unchanged), but the release-day standard
(every pin completed, claimed, or identified with a reason) is
not met - one pin stands unworked and unresponsive to taps.
The tracker is left untouched, so the next tick re-produces
the radar regular and the work resumes as a fresh unit. No
diamonds or money spent. No priced button tapped. No other
activity's rewards touched.

## Result stats

- target 1, achieved 0, resources_gained none, costs stamina 0
  plus about 13 minutes, verified yes, blocker_category c,
  tasks_claimed 0, tasks_executed 0, pins_inventoried 1,
  pins_worked 0, free_stamina_claims 0, radar_points_before 403,
  radar_points_after 403, stored_before 0, stored_after 0,
  stamina_before 59, stamina_after 59, duel_score_before
  not-read, duel_score_after not-read, entry_attempts 1,
  device_takeovers 0
