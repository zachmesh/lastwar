---
title: Zombie Invasion queue run 1833
created: 2026-11-15T02:33:00Z
modified: 2026-11-15T02:33:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-11-10-037, ticker-1804 - Glacieradon event ended, chain closed
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-14 18:25-18:33 PT
  - source: unit results of chain zombie-2026-11-10 in _queue_/done
---

# Zombie Invasion queue run 1833 (ticker-1804)

Unit zombie-invasion-zombie-2026-11-10-037, chain zombie-2026-11-10
seq 37. Executor ticker-1804. Session window about 18:25 to 18:33 PT.

## Outcome

Failed - execution impossible. The Zombie Invasion (Glacieradon)
event has ended: the Events hub tab bar holds six tabs and none of
them is Zombie Invasion. No kills, no claims, no stamina or items
spent, no medals read. The chain zombie-2026-11-10 is closed; no
successor unit was enqueued.

## What was verified live

- Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is online again: device.list connection_state online,
  last_seen 2026-11-15T02:13:07Z. First successful device access
  since the 2026-11-12 outage. computer.session cc-1 started,
  LastWar.app opened (window 351, 642x951), account banner
  "Signed in as HidingAnt504" seen on the Events hub.
- Base screen at entry: coin HUD 153.7M, stamina 120, total power
  147,344,687, Build Oil Well [0/1]. Coin before and after both
  read 153.7M on the HUD (rounded; no exact-panel read taken,
  nothing changed).
- Events hub tab bar enumerated across three scroll positions:
  The Age of Oil, Arms Race, Desert Storm (3v2 badge tab),
  Winter Battlefield, Rampage Bosses, Community. Six tabs, no
  Zombie Invasion tab. Community is the last tab (fully visible,
  no room past it); The Age of Oil is the first.
- Timer cross-check: chain unit 001 verified the Glacieradon wave
  live on 2026-11-11 with 2d 21:58 left; unit 023 read 1d 17:37
  left on 2026-11-12T08:31Z. Both point at expiry about
  2026-11-14T02:05Z (2026-11-13 about 18:05 PT), consistent with
  the tab being gone now. The last successful kill in the chain
  was unit 023 (2026-11-12); units 024-027 failed on the device
  input block (Issue 689) and units 028-036 failed node_offline
  while the Mac was down.

## Gaps discovered (for Issues, not fixed in this pass)

- Sync seeded this unit at 2026-11-15T00:07:55Z, about 22 hours
  after the event expired (about 2026-11-14T02:05Z): the zombie
  seeding check does not detect an ended event, so the chain kept
  producing units for a dead event. Needs a tooling Issue.
- _activities_/zombie-invasion/INDEX.md (v1.22.0, modified
  2026-10-31) still records the 2026-10-30 event end and says
  nothing about the Glacieradon return (2026-11-10 to
  2026-11-13) - the activity metadata is stale relative to the
  chain record. Tier-2 knowledge gap; left for the knowledge
  flow, not edited in this records pass.
- Evidence gap noted: unit 036 (ticker-1534) names
  _records_/2026-11-14/zombie-invasion/1600-queue-run.md as its
  evidence, but that file is absent from this working tree
  (only 1100 and 1333 are present). The 1600 record may live on
  the records branch or in another worktree; not chased in this
  pass.

## Result stats

- zombies_killed 0
- cleared false (event ended, not a cleared wave - the chain
  closes rather than pausing one hour)
- coin_before 153.7M (HUD rounded)
- coin_after 153.7M (HUD rounded)
- coins_collected 0
- medals_before unread
- medals_after unread
- chests_opened 0
- squads_parallel 0
- target: clear nearby zombies in one chain round
- achieved: no attacks; event ended, no Zombie Invasion tab
- resources_gained: none
- costs: about 8 minutes device time, no stamina or items
- verified: yes (tab absence read live on screen, timer
  cross-checked against chain units 001 and 023)
- blocker_category: f (missing precondition - event not live)
