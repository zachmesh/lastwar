---
title: Zombie invasion queue run
created: 2026-10-30T12:14:00Z
modified: 2026-10-30T12:14:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-058 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 05:04 to 05:17 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-058, executor
ticker-0504, chain zombie-2026-10-28 seq 58, computer
session cc-447. Status partial: the kills and the
in-unit loot claim are complete, but the Store
redemption step was not executed (Store button
unresponsive, see below), so the work continues in
successor unit 059. No tracker change is made for a
partial unit.

## Entry state

- The game was found already on the Zombie Invasion
  Events page (left from the previous unit). Event
  timer 13:55:12 remaining, next wave in 00:36:42.
  Coin HUD 135.2M at entry.
- No "active on a different device" dialog appeared.
  One keyboard_focus_unavailable block ("user is
  working in another window of this app") was cleared
  by activating LastWar and retrying; no input was
  lost to it.

## Three Lv.10 kills, sequential, loot claimed in-unit

- Dispatch method: batched sequences (Search at
  441,940, 2 second pause, crossed swords at
  499,753, March at 500,759) dispatched cleanly.
  Events icon at 683,150, Zombie tab verified by
  title before each Search.
- First kill: target X:992 Y:943, March Queues 1/4.
- Second kill: dispatched immediately after the
  first; target X:993 Y:937, March Queues again 1/4
  (squad 1 was already home).
- Third dispatch: the deploy panel opened, but the
  March tap opened the Regain Stamina panel instead
  of marching - stamina was 5/120. One 50 Stamina
  item was used from that panel (Owned 610 to 609,
  "you've acquired 50 Stamina"; 10 Stamina Owned
  628 in the same panel; the 75 Stamina Free Claim
  row showed a 01:10:xx cooldown and Remaining
  Today 1/2 and was not used; the 100 Stamina row
  carries a Buy price tag and was not touched).
  Stamina then read 55/120, 56/120 by regeneration,
  and 46 after the third march. Third kill: target
  X:995 Y:932, March Queues 1/4, 00:00:17 timer.
- squads_parallel is 1, for the same reason as units
  043 and 049: round trips of tens of seconds, not
  the march cap of 4. Each next dispatch was
  attempted immediately, but the previous squad had
  returned (queue 1/4 after each March) before the
  next March landed; the stamina refill before the
  third march widened that gap further.
- Stamina cost 30 total (3 x 10). Stamina at entry
  was not read before the first march; the trajectory
  above (5, then 55, 56, 46) is the measured record.

## Loot claim in-unit, all three rows present

- Gift-box point correction for this map view: taps
  at 319,247, 328,240, 340,250 and 340,257 (single,
  double and long-press) only highlighted the March
  Queues bar and did not open LOOT. A single tap at
  428,240 opened the LOOT panel at once. The icon's
  active area on this view was about 406 to 438 in
  x and 200 to 250 in y (window coordinates); the
  earlier grounded points (317,233 and 319,247) do
  not transfer across map views - re-ground the
  gift point on the current screenshot.
- The gift icon's red badge read 1 at first sight,
  yet the panel held 3 rows, so the badge is not
  the row count in this view; do not use it as the
  row count.
- LOOT panel held exactly the three kills, each
  Lv.10, each coin 268.0K and medal +10: X:995
  Y:932, X:993 Y:937, X:992 Y:943. Claim All at
  499,765 claimed all three in-unit for 804,000
  coins and +30 medals. Coin HUD moved 135.2M to
  136.0M (food 272.4M to 273.2M, iron 464.5M to
  465.3M, consistent with 3 x 268K per resource).
- No medal balance was re-measured live (the Store
  never opened), so no medal total is reported here
  - derived totals stay untrusted per units 043 and
  047. No Coin Chest was opened; the owned chests'
  inventory location is still unknown.

## Store redemption deferred again

- Store button on the Zombie Invasion Events page
  was unresponsive to a single tap at 609,221 and
  to a 1 second long-press at the same point, in
  this session. This is the third unit in a row
  with an unresponsive Store button (units 057 and
  058, plus the deferred attempt in unit 048's
  lineage). The SSR row re-check and the Buy-step
  retry from unit 047 stay open for the successor;
  the successor should try a different input route
  for the Store button (for example a tap grounded
  by visual grounding on the current screenshot,
  as the gift-box tap here was rescued that way).

## Close

- Cleared is false: the wave was still running
  (next wave countdown about 00:36 at entry, event
  timer about 13:51 at close) and nearby zombies
  remained. Successor unit 059 is enqueued to start
  now in the same chain.
- No diamonds or money spent, no price tag tapped,
  no speedup burned, no assembly or teleport.
