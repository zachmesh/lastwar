---
title: Event claims 2026-11-08 ticker-1851 queue run
created: 2026-11-09T03:14:00Z
modified: 2026-11-09T03:14:00Z
version: 1.0.0
description: Event claims unit events-2026-11-08-1457 executed by ticker-1851, partial
status: partial
grounded_in:
  - source: game screens observed live on the owner Mac mini, 2026-11-08 about 19:08 to 19:14 PT
---

# Event claims 2026-11-08 ticker-1851 queue run

- Unit: events-2026-11-08-1457 (regular events, activity event-claims)
- Executor: ticker-1851
- Session window: about 19:08 to 19:14 PT, 2026-11-08 (device session cc-149)
- Status: partial

## Performed

- NEW EVENT DISCOVERED - "The Age of Oil" (first tab of the Events
  hub, new this reset day). Opening the Events hub played a
  full-screen intro cutscene (worker, gold coins), then the app
  reloaded to the hub on its own (LAST WAR logo screen). The event
  page shows a 4-stage track (stage 1 active), 6d 22:48 left, and an
  "Achievements 8/16 Completed" toast. A Farhad / Gump story dialog
  (4 lines advanced) blocked the page until dismissed.
- Age of Oil milestone 1 claimed - "Unlock Tech: The Age of Oil",
  Complete a total of 500 Tech Research in this Warzone, 850/500:
  CONGRATULATIONS paid coin chest x3, red diamond x50, Oil 3.0K x6,
  5-minute speedup x2. The tab badge fell from 2 to 1 and the stage
  1 badge from 2 to 1.
- Arms Race checked - Base Building phase, Contest Segment Lv.29-30,
  score 0, point chests 6,250 / 12,500 / 30,000 all unreached,
  cumulative chest 0/2, phase timer 02:45:50, warzone rank 9
  (#2110 [AP3x]Bears Lair, 0 points). Nothing claimable. Scoring
  paths are building power +1, 1-min construction speedup +10
  (burning items, not done) and diamond packs +30 (paid, not done).
  Arms Race grinding is the arms-race unit's job, not this claim
  round.
- Desert Storm Battlefield checked - registered in Squad [A],
  "Enlisted" stamp, Battle Day 2026-11-13 03:00-03:30, Participants
  20/20. Nothing to claim; the tab's "New" badge was the
  registration confirmation.

## Not performed (blocker)

- Age of Oil milestone 2 NOT claimed - "Unlock Stage: Base Expansion
  II", Complete a total of 500 Building Upgrades in this Warzone,
  5090/500, gold chest still showing, stage badge still 1. Five
  attempts, four methods, all no-change: single tap on the chest
  centre x2, 1-second long-press, tap on the stage-1 hexagon node,
  double-click on the chest. The sibling chest on Unlock Tech opened
  on a single tap, so the method works; this chest does not respond.
  Blocker class c (tap method) turning into a repeated blocker -
  next events unit must try a different entry route (the
  achievements panel, the card detail page, or a fresh hub open)
  before tapping this chest again. Issue filed for the new event
  and this chest (see below).
- Tabs NOT swept this unit - Winter Battlefield, Level Swap, Wanted
  Boss, Community. The 15:06 sweep found nothing claimable on any
  of them; this unit did not re-verify them. They carry to the next
  events unit.

## Notes

- Power: base read 149,209,253 at 18:52; base read 149,109,253 at
  about 19:08. A 100,000 step-down inside this pass, unexplained;
  no battle, loss or spend was observed in this pass. The 641,100
  step-down from 16:58 noted in the 18:30 zero sweep is likewise
  unexplained. Worth a retro look, not an in-unit chase.
- The Age of Oil event is new - no activity metadata exists for it
  yet. Issue #477 filed: new event exploration (class knowledge),
  linked to this record.
- No diamonds, money, speedups or paid buttons used. No login or
  verification demanded, no different-device dialog appeared. The
  app reload after the intro cutscene lost no state.

## Result stats

- target 2, achieved 1 (Age of Oil chests claimed 1 of 2),
  resources_gained "coin-chest 3, red-diamond 50, oil 3.0K x6,
  speedup-5m 2", costs "duration about 6 min, no diamonds, no
  money", verified yes, blocker_category c,
  follow_up "Base Expansion II chest unclaimed; Winter Battlefield,
  Level Swap, Wanted Boss, Community unswept"
