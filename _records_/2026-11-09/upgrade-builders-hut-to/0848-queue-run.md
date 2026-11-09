---
title: Builders Hut Lv.26 banner quest exploration
created: 2026-11-09T16:52:00Z
modified: 2026-11-09T16:52:00Z
version: 1.0.0
description: Scout discovery exploration of the Upgrade Builders Hut to Lv.26 banner quest - read-only learning
status: done
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-09 08:48-08:53 PT
---

# Builders Hut Lv.26 banner quest - 0848 queue run

Unit scout-scout-discovery-2026-11-09-009, executor ticker-0842.
Session cc-245, LastWar window 489932, no device dialog, no
contention, no login demand.

## What was learned

The banner quest "Upgrade Builder's Hut to Lv.26 (0/1)" sits at the
bottom left of the base screen, above the HEROES button. Tapping
it pans the camera to the Builder's Hut (Lv.25) and selects it -
yellow arrow above the building, paw and green up-arrow buttons.
Tapping the green up-arrow opens the upgrade panel; everything
below was read live on that panel.

- Builder's Hut Lv.25 to Lv.26. Hero EXP 22.0M shown on the
  panel. Power 90,800 to 108,300. Free Construction Speed-up
  Time 00:20:00 to 00:22:00.
- Cost, all prerequisites met (green checks): Lv.26
  Headquarters; Iron 866.8M/170.0M (have 866.8M, need 170.0M);
  Food 542.1M/56.9M (have 542.1M, need 56.9M).
- Original Time 15d 08:05:18. The Upgrade button shows
  7d 07:16:49 (effective time after bonuses, as displayed).
- Finish Now would cost 18,188 diamonds.
- No deadline or countdown was seen on the quest banner or the
  panel. Whether the banner quest itself pays a separate reward
  on completion is untested - it was not checked against the
  daily-missions list in this unit.

## Result

Done - the mechanism, cost, time and rewards are measured. The
action itself is owner-only: starting a building is a red line
(never start buildings on own initiative), so the Upgrade button
was NOT tapped and Finish Now was NOT tapped. Building queue
read 1/4 at the time (Lv.29 Aircraft Center in progress, per
the 0744 unit), so a free builder slot exists, but the 15-day
build is the longest commitment measured so far.

- Follow-up: Issue #517 filed (owner-decision) - start the
  Lv.26 Builders Hut upgrade now, or leave it queued? If
  approved, the building-queues regular (PR #515, Refs #513)
  would own the execution. Candidate stays learn-only until
  the owner decides.
- Token note: token held until 09:00:48 PT; the session ended
  about 08:53, inside the window; no game input ran after
  expiry.

## Stats

- target: explain-builders-hut-lv26-quest-mechanism-cost-time-rewards
- achieved: 1
- resources_gained: none
- costs: about 5 minutes, no items spent, no diamonds spent
- verified: yes (same-unit live reads)
- blocker_category: none
