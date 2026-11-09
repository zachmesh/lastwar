---
title: Total Power 149217331 queue run 1149
created: 2026-11-09T19:49:00Z
modified: 2026-11-09T19:49:00Z
version: 1.0.0
description: Ticker-1134 scout discovery unit 015, Total Power HUD figure - verified live twice in this pass, not a candidate task, power-drop question already tracked in Issue 482
status: done
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 11:36 and 11:46 PT (unit 014 session, same pass)
---

# Total Power 149217331 queue run 1149 (ticker-1134)

Unit: scout-scout-discovery-2026-11-09-015. Status: done.
Activity: total-power-149217331 (candidate exploration, read-only learning).
Chain: scout-discovery-2026-11-09, seq 15.

## Live reads

- Total Power read live twice inside this pass's unit 014
  session, on the base screen: 149,217,331 at 11:36 PT on
  entry and 149,217,331 at 11:46 PT on return - unchanged
  across the pass, and identical to the observation file's
  value for this item.
- No game session was opened for this unit itself: the figure
  was already read live twice minutes earlier in the same
  pass, so a fresh session would re-read the same number.

## What was learned

- Total Power is a known HUD figure, not a candidate task:
  it has no entry, mechanism, cost, reward, cycle or scoring
  of its own to learn. The observation item's own
  suggested_unit is none, and its state is info-only.
- Reconciliation: the 2026-10-25 baseline is 149,689,618, so
  the current reading sits 472,287 below baseline. That delta
  does not match Issue #482's 641,100 step-down figure for
  2026-11-08, so the step-down accounting stays open - this
  unit adds a fresh live read to #482 rather than closing
  the question.
- The candidate is rejected as a task (nothing to do, nothing
  to profile) and tracked in Issue #482 with this unit's
  reads.

## What was done

- Verified the figure against two live reads from this pass
  and the observation value, computed the baseline delta,
  and commented Issue #482. No game session opened, nothing
  claimed, nothing spent.

## Red lines

- No diamonds or money spent. No priced button tapped. No
  other unit's work touched.

## Stats

- target: learn-total-power-profile-fields
- achieved: 1
- resources_gained: none
- costs: about-3-minutes-no-game-session
- verified: yes
- blocker_category: none
- points: 0
- surfaces_walked: none-reused-unit-014-live-reads
- items_observed: 1
- red_dots_seen: 0
- red_dots_explained: 0
- unexplained_red_dots: 0
- unknown_items: 0
