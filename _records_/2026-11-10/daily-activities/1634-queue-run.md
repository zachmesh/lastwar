---
title: Zero sweep queue run 1634
created: 2026-11-11T00:43:00Z
modified: 2026-11-11T00:43:00Z
version: 1.0.0
description: Ticker-1634 zero-sweep unit 001 of 2 - base HUD and Secret Command Post read live, one coin bubble standing, remaining ledger lines pass to the 17:30 sweep
status: unverified
---

# Zero sweep - ticker-1634, 16:38 to 16:42 PST

Unit zero-sweep-2026-11-10-1630, executor ticker-1634, chain
pre-reset-sweep-2026-11-10 seq 1 of 2. Status partial: sweep
001 of 2 read the base HUD and the Secret Command Post live;
the remaining ledger lines were not walked in this unit and
pass to the staged 17:30 sweep (zero-sweep-2026-11-10-1730,
same chain, seq 2, not_before 17:30, expires at the 19:00
reset). Computer session cc-482, windowed 642x951 play
throughout. No device dialog, no login demand, no Touch ID,
no password typed.

## Live reads

### Base screen, about 16:45

- Power 148,787,578; food 631.3M; iron 954.1M; coin 97.8M;
  diamonds 6,267 (red gem, top right); stamina 120; level 30.
  A gold 13.22K counter with a blue plus button sits beside
  the avatar; its meaning was not asserted in this unit.
- VS timer 01:20:54; Season II 3d 01:30:54; third timer
  5d 01:20:54 beside the radar-side icon (meaning unverified,
  same as the 06:14 and 15:12 reads).
- Left column: hammer 1/4 (red dot), flask 1/2 (red dot),
  truck icon with a question marker, radio/broadcast icon
  badge 11, hero portrait, gift chest. Right column: Events
  badge 2, VS, Season II, radar-side icon, skull badge 1 with
  a 00:00:27 countdown, Alliance (red dot), Mail (red dot),
  Inventory (red dot).
- Task: "Build: Oil Well [0/1]". Chat ticker: "Breaking
  News: Alliance War!", 99+ unread.
- One gold coin bubble seen standing over the purple
  crystal-like building near the top of the base. The lower
  half of the base view sits in fog in this panned position,
  so food, iron, EXP and titanium bubbles were not
  individually verified in this unit.

### Secret Command Post, about 16:49

- Entered by tapping the left-column truck icon at its fresh
  measured centre (norm 44,641). The tap needed a fresh
  observation_id after the first attempt was refused as a
  stale observation; the retried tap landed first time.
  This confirms again the 15:31 harvest-unit finding that
  the icon opens the Secret Command Post, not a truck
  screen; nothing new was discovered about the icon.
- Assist Allies 5/5 at cap; Plunder Others 0/3.
- Your Tasks, 4 of 8 visible (list does not scroll with a
  plain scroll; press-drag is the working method per the
  10:36 record): UR Rescue Test Subject Lv.5 PERFECT, UR
  Disrupt electric grid Lv.5 PERFECT, SSR Provide Tech
  Support to Refugees Lv.5 carrying the orange hexagon
  badge with no PERFECT stamp visible, SSR Protect Refugee
  Camp Lv.5 PERFECT. No Claim button anywhere on the
  visible cards. This matches the 13:49 secrets read (all 8
  PERFECT, orange badge unexplained, no Claim button); the
  staged secrets-2026-11-10-1830 unit re-verifies the full
  list. Mega Refresh and Mega Deploy untouched.

## Ledger lines, this unit

- Line 3 coin bubbles: read live, NOT at zero - one coin
  bubble standing. Fix-up: the staged harvest unit
  harvest-2026-11-10-1803 owns collection; no new unit
  enqueued.
- Lines 1, 2, 4, 5 food, iron, EXP, titanium bubbles:
  not individually verified in this unit (panned/fogged
  base view). The 15:31 harvest unit read all three panel
  pools Available 0, but per rule R1 that read does not
  close these lines for this sweep; the 17:30 sweep
  re-reads them.
- Line 6 Armed Truck: not read in this unit; still
  unlocated (issue #566, 5th deferral at 15:31).
- Lines 7 to 23 (drone components, ore, screws, shop
  pickup, pass pickups, VIP freebie and login chest,
  mission chests, mail, gifts, donations, trucks, train,
  radar, duel total, crystal, glittering market): not
  walked in this unit. Prior same-day live reads stand as
  context only, not as sweep closes: VIP freebie and login
  chest both claimed 14:38; donations closed 0/30 at 02:53
  with the count refilling in bursts; trucks Trade Count
  4/5 and Plunder 2/4 at 14:11; missions activity 120,
  160/200 unreached at 14:26; duel total 1,650,000 of
  3,600,000 at 13:33. The 17:30 sweep re-reads each line
  live.
- Zombie Invasion: the Events hub was not opened in this
  unit, so no fresh Zombie-tab read was taken. The 06:14
  scout and 05:19 events reads found no Zombie tab; the
  event is still ended and no chain was seeded, per the
  standing rule.

## Fix-ups enqueued

- None. The two non-zero observations already have staged
  units of their own type: harvest-2026-11-10-1803 for the
  coin bubble, secrets-2026-11-10-1830 for the Command Post
  re-check. Enqueuing duplicates would violate the
  (regular, planned_for) invariant. The 17:30 sweep unit
  is already staged in the same chain.

## Red lines

- No diamonds or money spent, no price tag or paid button
  tapped, no Delete All, no assembly or teleport. Mega
  Refresh and Mega Deploy untouched. Nothing claimed: the
  sweep reads only.

## Result stats

- target: 23 ledger lines read live
- achieved: 1 line read live (coin bubbles, not at zero)
- resources_gained: none
- points: 0
- costs: about 7 minutes, no items spent
- verified: yes (the HUD, bubble and Command Post figures
  reported here are same-unit live reads; unwalked lines
  are reported as unwalked, not as closed)
- blocker_category: h (by-design partial - the sweep is
  split across the 16:30 and 17:30 chain pair by design)
