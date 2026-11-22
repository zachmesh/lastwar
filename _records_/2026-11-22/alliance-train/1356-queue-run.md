---
title: Alliance train queue run 1356
created: 2026-11-22T21:56:00Z
modified: 2026-11-22T21:56:00Z
level: L0
version: 1.0.0
description: Train unit train-2026-11-22-1030, ticker-1352, no train preparing at check time - both preparation signals absent on a clean base view, unit closed partial without panning
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 13:52-13:54 PT
  - source: unit train-2026-11-22-1030 in _queue_/claimed
  - source: _activities_/alliance-train/INDEX.md, preparation-only surface rule
---

# Alliance train queue run 1356 (ticker-1352)

Unit train-2026-11-22-1030, regular train, segment 2.
Executor ticker-1352. Computer session cc-155. Session
window about 13:52 to 13:54 PT. Game in window mode
(642x951, window 127196), background input working. No
"active on a different device" dialog. A second LastWar
window (127250, 642x919, untitled) sits unbound beside
it - the duplicate-window class of issue #822; input
stayed on 127196 and the duplicate was not touched.

## Outcome

Partial - no train is preparing at check time, so there
is nothing to board. Both preparation signals are absent
on a clean base view: no "Boarding closes in" banner
under the resource bar, and no train icon in the left
icon column. Per the activity metadata (preparation-only
surface), the unit closes here without panning the base
edge, and re-checks only when a train is preparing. No
Trade Contracts spent, no seat taken, no dialog opened.
Tracker untouched; the next train unit
(train-2026-11-22-1430) is already in the inbox for its
slot.

Note: this unit's slot was 10:30 PT and its expires_at
14:30 PT; it was picked at about 13:53 PT and finished
inside its window. The preparation window is short
(the banner showed 00:02:57 on first sight), so a
10:30-slot train may already have departed - or none
was scheduled for this slot.

## Post state at entry - read live about 13:53

- Base screen, clean view. Coins 109.2M, food 765.4M,
  iron 1.1G, total power 147,972,269 (HUD reads).
- Left icon column: hammer 1/4, test tubes 2/2, blue
  icon with red badge 3, truck, radar with badge 11,
  wrench - no train icon anywhere in the column.
- Breaking News bar reads "Alliance War!" (chat line,
  not a train banner). Events carries a red badge 1;
  VS shows a 04:06:15 countdown.
- A second computer.observe (fresh observation) after
  the screenshot confirms the same screen with no
  change - no train signal appeared.

## Result stats

- target: board carriage 2 of a preparing train with 3 Trade Contracts
- achieved: no train preparing at check time, nothing boarded
- resources_gained: none
- points: 0
- costs: about 3 minutes device time, no spend, no items
- verified: yes (both preparation signals read live on a clean base view in this unit)
- blocker_category: f (missing precondition - no train in preparation)
