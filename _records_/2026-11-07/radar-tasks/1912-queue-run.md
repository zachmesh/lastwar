---
title: Radar queue run 1912
created: 2026-11-08T03:12:00Z
modified: 2026-11-08T03:12:00Z
level: L0
version: 1.0.0
description: Ticker-1904 radar unit, stack posture, stack empty at 0 of 40, one pin inventoried untapped
status: unverified
---

# 1912 queue run - Radar tasks

Executor: ticker-1904. Unit: radar-2026-11-07-1803 (window duel
day 6 - radar stack; live duel posture at 19:06 local is duel day
7, off day settlement, radar_posture stack per tools/duel.py).
Session window about 19:07 to 19:12 America/Los_Angeles.

## Performed

- Radar screen entered and verified live: Lv.13, radar points 267,
  stored tasks 0 of 40, stamina 99 (top right), restore line "12
  Radar Task(s) will be restored in 03:22:08". No bottom action
  bar is shown - no Quick Execute offer and no Claim All offer,
  consistent with zero stored and zero pending rewards.
- Stack posture held throughout: nothing executed, nothing
  claimed, no pin tapped. The stack is empty - there were zero
  executable ordinary tasks, so the execute step is vacuously
  complete and no stamina was spent.
- Pin inventory (stack rule, untapped): one pin standing on the
  radar map, southwest near the map edge at about norm 85,738 -
  a brown circular pin showing what looks like an animal face,
  no red dot visible, class unknown. No other pins are visible
  on the map. Left for the next release-day unit to identify
  under the release handling rule.
- Returned to the base screen afterwards (power 149,850,353).
  No diamonds, money, speedups or other spending. No alliance
  diplomacy, no assembly, no teleport.

## Entry note - fresh grounding corrected the dish coordinate

- First tap at norm 50,690 (estimated from the fresh
  screenshot) missed the dish and opened a base visitor
  dialog, "POLAR GUEST - Amazing! This place feels just like
  home." / "Can I stay here forever?" - advanced twice with
  dialog taps only and the dialog closed by itself. No reward
  was offered or claimed; no radar-unrelated work was done.
- Re-grounded from a magnified crop of the left icon column:
  the satellite dish icon sits at pixel about 38,757 in the
  763x1050 window, i.e. norm 52,721 - slightly left of the
  2026-10-29 measured norm 62,727 recorded in the radar
  profile. The second tap at norm 52,721 opened the radar on
  the first try. The profile coordinate is stale by about 10
  norm points in x; the correction is recorded here and left
  for the knowledge organizer to harden (tier-2 edit, not
  swept into this records commit).
- One UI element noted but not touched: a gold icon with a
  NEW! badge at the top of the radar screen (about norm
  295,60). Its function is unknown; it is not part of this
  unit's stack work.

## Capture channel recovered

- The device channel that failed the last twelve-plus passes
  (Issue 282, screen-capture failure, Last War window
  off-Space) is working again in this pass: the Last War
  window is on-screen at 763x1050, global (73,30), and
  screenshots and OCR read normally. This is the first
  successful live game read after the access-failed streak
  recorded through ticker-1608. Recovery noted here and
  commented on Issue 282 by this pass.

## Closing reads

- Stored 0 of 40, pending rewards 0, radar points 267,
  stamina 99, restore 12 tasks in 03:22:08, pins 1 inventoried
  untapped, tasks executed 0, tasks claimed 0.

## Outcome

Done. Stack-day radar check complete: screen verified, zero
executable tasks, stack empty, one pin inventoried for the
release day. The next radar restore lands in about 3 hours
22 minutes (12 tasks); the next radar unit will have work
again then.

## Result stats

- target 1, achieved 1, resources_gained none,
  costs 5m_wall_no_stamina, verified yes, blocker_category none,
  stored_tasks 0, tasks_executed 0, tasks_claimed 0,
  pins_inventoried 1, stamina 99, radar_points 267,
  restore_in_minutes 202, device_takeovers 0
