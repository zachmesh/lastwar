---
title: Event claims queue run 0340
created: 2026-10-31T10:41:00Z
modified: 2026-11-01T07:00:34Z
version: 1.0.1
description: Events unit events-2026-10-31-0257 by ticker-0334, partial
status: partial
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
---

# 0340 queue run - event claims (partial)

Events unit events-2026-10-31-0257 by ticker-0334,
sessions cc-604 then cc-605 (cc-604 dropped mid-unit,
cc-605 resumed with no state lost), window mode
642x951, no different-device dialog.

- Zombie Invasion was NOT seeded in this pass: the
  chain zombie-2026-10-28 is closed in the activity
  metadata (the event ended at about the 19:00 reset
  on 2026-10-30, unit 066 the last chain unit), and
  the Events hub tab bar shows no Zombie Invasion tab.
- Events hub opened on the Arms Race Base Building
  page (Contest Segment Lv.29-30): score 0, rank 9 at
  #2110 [redacted-character-name], chest thresholds 6,250 /
  12,500 / 30,000, cumulative chest 0/2 at top left,
  about 03:22 left on the stage at entry. No chest
  reached, nothing to claim on this page. No Arms
  Race grinding was done under this unit - the
  separate arms-race unit owns the tier-3 push.
- A tap on the tab bar's right edge opened the Arms
  Race HOW TO GET POINTS schedule popup: current
  stage Base Building at 03:00 local, then 07:00
  Drone Boost, 11:00 Hero Advancement, 15:00 Base
  Building, Day 7 19:00 Drone Boost, 23:00 Hero
  Advancement. Swap attempts today 1/1. The popup
  was dismissed by a later tab-bar tap; its X did
  not respond to background clicks (two taps) and
  the window stayed behind Chrome throughout.
- Tab sweep BLOCKED: repeated taps on the Desert
  Battlefield tab position, a click_element on the
  tab strip, and a click_foreground attempt (stale
  element) all left the hub on the Arms Race page.
  Background tab taps do not switch tabs while
  Chrome is frontmost. Desert Storm, Winter
  Battlefield, Level Swap, Wanted Boss and Community
  tabs were therefore NOT swept in this unit.
- Nothing claimed in this unit. The base-screen
  Events badge (1) was not re-attributed here; the
  2026-10-30 sweep attributed it to the Wanted Boss
  tab dot, which this unit could not re-verify.

Outcome: partial. The next tick re-produces this
regular; the next unit should bring the game window
to the front first, then sweep the remaining tabs.

Tracker NOT marked (partial).
