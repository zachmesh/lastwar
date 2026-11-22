---
title: Perception scout queue run 1604
created: 2026-11-22T00:12:00Z
modified: 2026-11-22T00:12:00Z
version: 1.0.0
description: Queue unit scout-2026-11-20-1800, ticker-1604 - post-reset scout chain head, base and Events hub walked live, Bingo Task 9/15 with unclaimed chests, Black Market and Desert Battlefield badges unexplained, full pass unfinished at the unit cap
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 16:07-16:22 PT
  - source: unit scout-2026-11-20-1800 in _queue_/done
---

# Perception scout queue run 1604 (ticker-1604)

Unit scout-2026-11-20-1800, regular scout, activity
perception-scout, priority 2, est 8 minutes, expires
2026-11-22T02:00:00Z (18:00 PT reset). Executor ticker-1604.
Session window about 16:07 to 16:12 PT. Token acquired 16:07
PT; unit claimed 16:07 PT, lease to 16:27 PT. Chain head of
the post-reset pass; chain scout-2026-11-20, successor
enqueued for the unwalked surfaces.

## Outcome

Partial - the base screen and the Events hub were walked
live, 24 observed items recorded, but the full pass did not
finish inside the unit: the Arms Race tab, Black Market,
Desert Battlefield, Wanted Boss and the fourth Events tab
were not opened, and the store, alliance, mail, VIP, passes,
daily missions and world map surfaces were not walked. Two
Events-tab badges stay unexplained (Black Market "!" and
Desert Battlefield "New"). No claim, fight, dispatch,
donation or purchase was made - scout observes only. No
diamonds or money spent. The tracker is untouched (partial
re-produces next tick); the successor chain unit continues
the same pass.

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-19.
- LastWar window 105986 (pid 5136, 788x1083) raised to the
  front with activate raise=true on the first attempt - the
  Issue #648 window precondition that blocked seven
  consecutive units earlier today stays cleared (ticker-1434
  cleared it at 14:34 PT; ticker-1504 played 15:15-15:30 PT).
- No different-device dialog, no login demanded, no Touch
  ID, no password typed. The game canvas exposes no
  Accessibility controls; all reads are screenshots plus OCR.

## Observed items

### Base screen (walked 16:08 PT)

- HUD: food 730.5M, iron 1.1G, coin 88.2M, diamonds 5,236,
  gold bars 17.72K, power 149,653,371. Unchanged from the
  ticker-1504 exit read.
- Events icon, red badge "1" - explained: the Bingo Task tab
  badge (see below).
- VS icon, red dot, countdown 01:51:51 - duel day in
  progress; owning regular duel-score, unit in inbox.
- Alliance icon, red dot - routed to the alliance units in
  inbox (donations/train), not opened this unit.
- Mail icon, red dot - routed to the mail unit in inbox
  (mail-2026-11-21-1430), not opened this unit.
- Inventory icon, red dot - routed to the owning regulars;
  not opened this unit.
- HEROES button, red dot - routed to the owning regulars;
  not opened this unit.
- WORLD button, badge "99+" - routed to the world-map
  surfaces; not opened this unit.
- Construction hammer, 1/4 with red dot - routed to the
  owning regulars; not opened this unit.
- Research flask, 2/2, no dot.
- Trucks icon, red badge "3" - routed to the trucks unit in
  inbox; not opened this unit.
- Hero icon (red-haired hero, left edge), red badge "1" -
  routed to the owning regulars; not opened this unit.
- Megaphone icon labelled "NEW" (bottom centre-right) -
  UNKNOWN item: announcement/news entry point, label and
  content not read; successor to open it.
- "Build: Oil Well (0/1)" banner at the bottom.
- Chat ticker: "Breaking News: Alliance War!
  DieRotenTeufel: [SNGw]Nakie22 ... PandaVoid:
  [SNGw]Jiqullsz (Warzo..." - alliance war news, content
  truncated on screen.

### Events hub (walked 16:09-16:11 PT)

- Tabs (left to right, scrollable): "The Age of Oil"
  (chest icon), "Arms Race", "Bingo Task" (red badge "1"),
  "Black Market" (red "!" badge), "Desert Battlefield"
  (red "New" badge), "Wanted Boss", plus a fourth tab cut
  off at the right edge reading "Cor..." - label unread,
  UNKNOWN item.
- "The Age of Oil" tab: stage track 1-2-3-4, currently at
  stage 2. Two warzone-goal cards, both 1d 01:51:21
  remaining: "Unlock Radar Task: Dripper" - complete 5000
  Radar Tasks in this Warzone, 314811/5000 (goal exceeded
  about 63x); "Unlock Secret Task: Capture the Oil Depot" -
  complete 1000 Secret tasks in this Warzone, 55487/1000
  (goal exceeded about 55x). Both goals are far past their
  targets; whether their rewards are already claimed or
  still claimable was not probed (scout observes only).
- "Bingo Task" tab: "The Age of Oil" event, 1d 01:50:29
  remaining. "Complete tasks to win Black Market Cash and
  various rewards." 3x4 bingo grid, 9/15 tasks complete.
  Row rewards (right side): 5 chests, 2 claimed (green
  check), 3 unclaimed. Column rewards (below): 3 blue
  chests unclaimed, 1 gold chest unclaimed. Final reward:
  "Collect after completing all tasks", 9/15 - Black
  Market Cash 1.5K, Oil 30.0K x12, chest x1, red crystal
  10K x1. The tab badge "1" is explained by these
  unclaimed bingo chests; the owning regular is events
  (unit events-2026-11-21-1857 in inbox).
- "Arms Race" tab: NOT opened this unit - successor.
- "Black Market" tab: NOT opened; red "!" badge
  UNEXPLAINED - successor.
- "Desert Battlefield" tab: NOT opened; red "New" badge
  UNEXPLAINED - successor.
- "Wanted Boss" tab: NOT opened - successor.
- Fourth tab ("Cor..."): NOT opened, label unread -
  UNKNOWN item, successor to identify.
- No Zombie Invasion tab in the tab strip (consistent with
  the event having ended, verified 2026-11-14).

## Result stats

- target: walk the full post-reset pass (base, events,
  store, alliance, mail, duel/radar, world map, VIP,
  passes, daily missions) and record every available item
- achieved: base + Events hub (2 of 4 tabs read) walked;
  24 items observed
- resources_gained: none (scout observes only)
- costs: about 5 minutes device time, no stamina or items
- verified: yes (all items read live from screenshots)
- blocker_category: h (by-design partial - unit cap
  reached mid-traversal)
- surfaces_walked: base, events-partial
- items_observed: 24
- red_dots_seen: 13
- red_dots_explained: 11
- unexplained_red_dots: 2
- unknown_items: 2

## Open for the successor (chain scout-2026-11-20, seq 2)

- Open the Arms Race tab and record the live phase, score
  and tier progress.
- Open Black Market ("!" badge), Desert Battlefield
  ("New" badge), Wanted Boss and the fourth "Cor..." tab;
  identify the fourth tab's label and record each tab's
  state, deadline and claimables.
- Open the base "NEW" megaphone and record what it is.
- Walk the remaining surfaces: store by section, alliance
  panel and station, mail, VIP, passes, daily missions,
  world map, duel and radar.
- Note: the day observation.md was created by ticker-1549
  at 15:55 PT (after this record's first draft); this pass
  appends its sections to it in delivery, per the queue
  design section 13. The planner's scout diff reads the
  observation (11 unexplained red dots, unchanged per the
  1440 pass).

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #762 already open for the
  branch, no new PR owed.
