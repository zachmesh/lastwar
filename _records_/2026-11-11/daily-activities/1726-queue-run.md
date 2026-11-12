---
title: Zero sweep queue run 1726
created: 2026-11-12T01:27:00Z
modified: 2026-11-12T01:27:00Z
version: 1.0.0
description: Ticker-1718 zero-sweep unit 001 of 2 - trucks counters read live at 1 of 5 dispatch and 0 of 4 plunder, donations points read live, remaining ledger lines pass to the 17:30 sweep
status: unverified
---

# Zero sweep - ticker-1718, 17:18 to 17:27 PST

Unit zero-sweep-2026-11-11-1630, executor ticker-1718, chain
pre-reset-sweep-2026-11-11 seq 1 of 2. Status partial: this
unit read the base HUD, the Trade Trucks counters and the
Alliance Techs donation points live; the remaining ledger
lines were not walked in this unit and pass to the staged
17:30 sweep (zero-sweep-2026-11-11-1730, same chain, seq 2,
not_before 17:30, expires at the 19:00 reset). Computer
session cc-644, windowed 642x951 play throughout. No device
dialog, no login demand, no Touch ID, no password typed.

## Live reads

### Base screen, about 17:20

- Power 149,218,973; food 689.4M; iron 1.0G; coin 136.7M;
  diamonds 13.22K; level 30; VIP 75. Stamina not re-read in
  this unit (69 at 16:50 per the scout, 67 at 16:40 per the
  daily-missions unit - context only).
- VS timer 00:39:26 at 17:20, 00:33:16 at 17:27; Season II
  2d 00:45:47; radar-side timer 4d 00:35:47.
- Task: "Build: Oil Well [0/1]". Chat ticker 99+ unread.
- Red dots on the base screen: Events badge 2, VS, Alliance,
  Mail, Inventory, HEROES, left-column mail icon badge 1,
  skull icon badge 1 with a roughly 60 second cycle timer
  (00:00:49, then 00:00:21) - the skull timer remains
  unexplained, carried from the 2026-11-09 and 2026-11-10
  observations.
- A building near the centre carries a "10" beneath it and a
  red up-arrow rally marker above it (meanings unverified,
  same as the 16:48 scout read).

### Trade Trucks panel, about 17:24

- Entered by tapping the left-column top icon. The first two
  taps missed: they used raw pixel coordinates, but this
  control channel takes coordinates normalized 0 to 1000
  within the window. Re-grounded from the fresh screenshot
  and retried at normalized 44,576 - the panel opened.
  The tap also needs a fresh observation_id; a stale one is
  refused before any input is sent.
- "Today's Trade Count: 1/5". One truck out (yellow truck
  with a blue gift-box marker above it - marker meaning
  unverified); three empty slots with green plus signs;
  "Mega Mode" button; "Filter out trucks from your Warzone"
  checked; History top-right.
- "Others' Trucks" tab: "Your Plunder Count Today: 0/4".
  Many plunderable trucks visible, including [oawc]Licca B
  and [TTAL]Portgas D Ace S. The tab badge 4 and the
  "Recover" red dot were not opened in this unit.

### Alliance Techs, about 17:25

- "Tech Donation Today: 4050" points; the reward threshold
  of 1000 contribution points is met. This screen shows
  points, not the Donation Count (remaining count) the
  ledger line closes on, so the count itself was not read
  in this unit and stays unverified. Five donations units
  ran today (0107, 0148, 0434, 0541, 0733) - context only.

## Ledger lines, this unit

- Line 18 trucks: read live, NOT at zero - dispatch 1/5,
  plunder 0/4, with about 95 minutes to the 19:00 reset.
  This is a rule R3 checkpoint shortfall (the two-hour
  checkpoint at 17:00 already stood at 1/5 and 0/4, per
  the 16:52 scout read). Fix-up: the next trucks unit
  trucks-2026-11-11-1457 was raised to priority 1 in this
  pass; it is actionable now and the loop picks it up next.
- Line 17 donations: partially read - points 4050 live,
  remaining count unread. The 17:30 sweep re-reads the
  count; four donations units stand in inbox (1403, 1803,
  2203, 0203).
- Lines 1 to 16 and 19 to 23 (bubbles, Armed Truck, drone
  components, ore, screws, shop and pass pickups, VIP
  freebie and login chest, mission chests, mail, gifts,
  train, radar, duel total, crystal, glittering market):
  not walked in this unit. Prior same-day live reads stand
  as context only, not as sweep closes: daily missions
  1638 found tasks incomplete (Defeat any Doom Elite 0/1,
  Recruit Heroes 0/1, Attack a Commander 0/1, Gather Food
  0/10000); mail last ran 1422; the 16:48 scout read the
  base HUD and the Hero List (9 hero cards with red dots).
  The 17:30 sweep re-reads each line live.
- Zombie Invasion: the Events hub was not opened in this
  unit, so no fresh Zombie-tab read was taken. The event
  returned 2026-11-10 and runs to about 2026-11-13; one
  zombie-invasion unit stands in inbox and the chain is
  live, so no sweep action is owed here.

## Fix-ups enqueued

- None enqueued as new units. The trucks shortfall is
  covered by raising the already-staged
  trucks-2026-11-11-1457 to priority 1 (same regular,
  same planned slot - no duplicate unit created). The
  17:30 sweep unit is already staged in the same chain.

## Red lines

- No diamonds or money spent, no price tag or paid button
  tapped, no Delete All, no assembly or teleport. Nothing
  claimed: the sweep reads only.

## Result stats

- target: 23 ledger lines read live
- achieved: 1 line read live to a close (trucks, not at zero)
- resources_gained: none
- points: 0
- costs: about 9 minutes, no items spent
- verified: yes (the HUD, truck counters and donation points
  reported here are same-unit live reads; unwalked lines
  are reported as unwalked, not as closed)
- blocker_category: h (by-design partial - the sweep is
  split across the 16:30 and 17:30 chain pair by design)
