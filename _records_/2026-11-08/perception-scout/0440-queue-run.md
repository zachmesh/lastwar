---
title: Queue Run 0440 Perception Scout Station Re-check
created: 2026-11-08T12:44:00Z
modified: 2026-11-08T12:44:00Z
level: L0
version: 1.0.0
description: Scout unit scout-midday-scout-mid-2026-10-31-009, station-panel preparation-signal re-check, partial per the unit window instruction, observe-only
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 04:36-04:44 America/Los_Angeles
---

# 0440 queue run - perception scout, station-panel re-check (scout-mid-2026-10-31 seq 9)

- Unit: scout-midday-scout-mid-2026-10-31-009, executor
  ticker-0434, chain scout-mid-2026-10-31, seq 9. Status:
  partial - per the unit window instruction the check
  stopped at the two preparation signals: both absent, so
  no pan of the base edge and no station platform visit.
  Observe-only throughout: nothing claimed, fought,
  dispatched, donated, boarded or bought.
- Session: computer session cc-83 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd), LastWar window
  already open on the base screen at entry. No
  device-access error, no different-device dialog, no login
  demanded.

## Base screen, read live about 04:40 local

- Level 30, power 149,850,353 - identical to the 0022
  read at 00:16 local today and the 0404 read at 04:16,
  consistent with observe-only play in between (no
  intervening execution unit). HUD top row: food 478.8M,
  iron 802.1M, coin 6.9M; second row 25.0M, 922.2K;
  diamonds 13.22K with a plus button; cart 4,217; stamina
  120. Season II timer 7d 13:22:59. Wanted Boss badge 2
  with a 00:04:00 timer.
- Left icon column, top to bottom: avatar Lv.30, hammer
  2/4 with a red dot, flask 2/2, green face, weather
  6.5C, blue vehicle icon with a red dot, white truck
  with badge 8, survivor "?" bubbles, radio with badge 2,
  hammer at the bottom.
- Right icon column: Events with an x2 badge, VS, Season
  II with a badge, Wanted Boss badge 2, Alliance (trophy
  icon), Mail with a red dot, Inventory with a red dot,
  WORLD. Bottom: HEROES, chat ticker, 99+ badge.
- Furnace toast again, recurring: "High-temp Furnace
  total overdrive time (in sec) [22/60]" - still
  unexplained, furnace observed only, never switched on
  or off, a red-line surface.
- Chat ticker top line: "Breaking News: Intense battle..."
  - not opened, not read in full. Resource bubbles
  standing on many buildings, observed only, not
  collected; the harvest regular owns collection.

## Station-panel re-check (alliance group)

- Both preparation signals absent, the same result as the
  0022 unit's read at 00:16 local today and the 2134 and
  2304 reads yesterday evening: no separate train icon in
  the left icon column, and no "Boarding closes in"
  banner under the resource bar. No train is preparing in
  this window.
- Icon identity note: the blue vehicle icon in the left
  column is the Trucks entry - the 0404 unit verified by
  tap at 04:19 today that it opens the Trucks panel
  (Trade Count 0/5), and the 0022 unit read the same icon
  as radar. The two readings disagree on what the icon
  is; neither reading makes it a train icon, and the
  train icon is state-dependent - it appears in the column
  only while a train is preparing (alliance-train
  metadata). The identity disagreement is recorded here
  for the diff/retro step, not settled by this unit.
- Per the unit window instruction and the R2-hardened
  entry route (alliance-train metadata 1.6.0), the check
  stopped at the signals: no pan of the base edge, no
  station platform visit.

## Red dot accounting

- Seen: 11. Left column hammer, blue vehicle icon, truck
  badge 8, radio badge 2 (4); right column Events x2,
  Season II badge, Wanted Boss badge 2, Alliance dot,
  Mail dot, Inventory dot (6); 99+ badge (1).
- Explained: 11. Hammer dot is the construction-queue
  signal (ownerless, per the 0022 unit); the blue vehicle
  icon and the truck badge map to the trucks regular;
  radio badge 2 maps to the help regular; Events x2 maps
  to the events and arms-race regulars; Season II,
  Wanted Boss timer, Alliance, Mail, Inventory and 99+
  map to their owning regulars/surfaces as in the 2140
  and 0022 units, all with units queued or in inbox.
- Unexplained: 0.
- Unknown items: 4 - the furnace overdrive toast [22/60]
  (recurring, mechanism still unexplained); the hammer
  dot's exact trigger and its ownerless routing (no
  construction regular in the queue); the 99+ badge
  (recurring); the Season II badge (recurring). The blue
  vehicle icon identity disagreement (Trucks per the 0404
  tap read, radar per the 0022 read) is a fifth open item,
  recorded above rather than counted here.

## Follow-up

- No successor unit is enqueued from this stale chain:
  the station re-check recurs with the current reset
  day's scout pass, whose head
  scout-midday-2026-11-08-0700 is already in inbox, and
  the remaining groups of the current reset day belong to
  it. Chain scout-mid-2026-10-31 is spent with this unit
  (done 7 before it, pending 0 after it).
- No new Issue filed: the station remainder is a
  pre-existing carried item already hardened in metadata,
  and the icon identity disagreement is a record-level
  note for the diff/retro step.
- Tracker untouched (scout units do not mark regulars
  done).

## Stats

- surfaces_walked: 1 (base screen only; the station
  panel was not visited, per the window instruction)
- items_observed: 12
- red_dots_seen: 11
- red_dots_explained: 11
- unexplained_red_dots: 0
- unknown_items: 4
- target: 2 (both preparation signals checked)
- achieved: 2 (both checked, both absent)
- resources_gained: none (observe-only)
- verified: yes (same-unit live screenshot reads)
- costs: about 8 min, no items
- blocker_category: h (by-design partial - the unit
  window instructs closing partial without panning when
  neither signal is present)
