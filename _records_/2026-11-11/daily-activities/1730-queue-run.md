---
title: Zero sweep queue run 1730
created: 2026-11-12T02:15:00Z
modified: 2026-11-12T02:15:00Z
version: 1.0.0
description: Ticker-1800 zero-sweep unit 002 of 2 - base HUD live, bubbles standing, mail gifts unclaimed, Glacieradon live with next wave in 00:52:52; four fix-up units raised to priority 1
status: unverified
---

# Zero sweep - ticker-1800, 17:57 to 18:15 PST

Unit zero-sweep-2026-11-11-1730, executor ticker-1800, chain
pre-reset-sweep-2026-11-11 seq 2 of 2. Status partial: this
unit read the base HUD, the mail categories and the Events hub
live; the remaining ledger lines were not walked in this unit
and pass to their owning units, named below. Computer session
cc-650, windowed 642x951 play throughout. No device dialog, no
login demand, no Touch ID, no password typed. Own PRs first:
records PR 655 (2026-11-11, post-1500 batch) was CONFLICTING
with no comments; resolved before game work by merging main
into the branch in a VPS worktree (merge e535c029a, pushed and
verified with ls-remote). The conflict was
_queue_/inbox/trucks-2026-11-11-1457.md: main carries a copy of
that unit file with raw conflict markers left from an earlier
bad merge (HEAD side trucks-2026-11-11-1057 vs 1457); resolved
by taking the records-branch version, the clean 1457 unit
(priority 1, planned 2026-11-11T22:57:00Z). The merge also
restores _queue_/done/trucks-2026-11-11-1057.md, which main
lacks. The corrupted file on main is a loop-health gap - filed
as issue #661 from this pass.

## Live reads

### Base screen, about 18:06

- Power 149,218,973; food 693.3M; iron 1.0G; coin 136.7M;
  diamonds 13.22K; level 30; VIP 75. Stamina 82.
- VS timer 00:00:51; Season II 2d 00:10:51; radar-side timer
  4d 00:00:51.
- Task: "Build: Oil Well [0/1]". Chat ticker 99+ unread.
- Red dots on the base screen: Events badge 2, VS, Alliance,
  Mail, Inventory, HEROES, left-column mail icon badge 1,
  skull icon badge 2 with a roughly 60 second cycle timer
  (00:00:46) - the skull timer remains unexplained, carried
  from the 2026-11-09 and 2026-11-10 observations.
- Food, iron and coin bubbles standing across the base (food
  9.6K/9.8K, iron 5.6K, coin 1.5K/1.6K/1.8K read on the
  screenshot); EXP and titanium bubbles not distinguished
  in this unit.

### Mail, about 18:08

- Seven categories. Claimable gift icons on Alliance and
  Event. Red dots on System, Regular and In-app Purchases.
  Battle Report and Favorite show no indicator.

### Events hub, about 18:13

- Zombie Invasion - Glacieradon tab active. Timer 1d
  23:58:15 left - the event runs to about 2026-11-13 18:00.
  "Challenge begins in: 23:58:16", "Your Timezone:
  2026-11-12 18:00". Progress bar 40/40. Store carries a
  red dot.
- "The next wave of Invading Zombies will arrive in
  00:52:52."
- Alliance Finding: Lv.80 Zombie Bosses at 342km, 138km,
  294km and Lv.85 at 208km, despawn about 03:23 to 03:29.
- Tab bar: Glacieradon badge 1, one more tab badge 1 (left
  edge, partially visible) - the base Events badge 2 is
  accounted for by these two.

## Ledger lines, this unit

- Lines 1 to 3 (food, iron, coin bubbles): read live, NOT at
  zero - bubbles standing. Fix-up: harvest-2026-11-11-1803
  raised to priority 1 (was 3, actionable now).
- Lines 4 to 5 (EXP, titanium bubbles): not distinguished in
  this unit; covered by the same harvest fix-up.
- Line 6 (Armed Truck): not read; covered by the harvest
  fix-up.
- Lines 7 to 11 (drone components, ore, screws, shop and
  pass pickups): not walked; owning units (passes, events)
  stand in inbox.
- Lines 12 to 13 (VIP freebie, login chest): not read; the
  VIP unit vip-2026-11-11-1800 is already priority 1 and
  actionable now.
- Line 14 (daily mission chests): not walked; the
  daily-missions unit stands in inbox.
- Line 15 (mail): read live, NOT at zero - Alliance and
  Event gifts unclaimed, three red dots. Fix-up:
  mail-2026-11-11-1830 raised to priority 1 (was 3,
  not_before 18:30).
- Line 16 (alliance gifts): not walked; the gifts unit
  stands in inbox.
- Line 17 (donations): points 4050 read live by the seq-1
  sweep at 17:25; the remaining Donation Count itself was
  not re-read in this unit. Fix-up:
  donations-2026-11-11-1803 raised to priority 1 (was 2,
  actionable now) so the count is read before the reset.
- Line 18 (trucks): read live by the seq-1 sweep at 17:24 -
  dispatch 1/5, plunder 0/4, NOT at zero. The fix-up unit
  trucks-2026-11-11-1457 is already priority 1 and is the
  next unit this pass.
- Line 19 (train): not walked; the train unit stands in
  inbox.
- Line 20 (radar): not walked; the radar unit stands in
  inbox.
- Line 21 (duel total): not walked; the duel-score unit
  stands in inbox.
- Lines 22 to 23 (crystal, glittering market): not walked;
  named status stands from the day records.
- Zombie Invasion: event live, next wave in about 53
  minutes; the zombie-invasion chain unit stands in inbox.

## Fix-ups enqueued

- No new units created. Four already-staged units raised to
  priority 1 in this pass: harvest-2026-11-11-1803,
  mail-2026-11-11-1830, events-2026-11-11-1857,
  donations-2026-11-11-1803. Trucks-2026-11-11-1457 was
  already priority 1 from the seq-1 sweep.

## Red lines

- No diamonds or money spent, no price tag or paid button
  tapped, no Delete All, no assembly or teleport. Nothing
  claimed: the sweep reads only.

## Result stats

- target: 23 ledger lines read live
- achieved: 5 lines read live to a close (food, iron and
  coin bubbles, mail, Events badge - all not at zero)
- resources_gained: none
- points: 0
- costs: about 15 minutes, no items spent
- verified: yes (the HUD, mail categories and Events hub
  reported here are same-unit live reads; unwalked lines
  are reported as unwalked, not as closed)
- blocker_category: h (by-design partial - the sweep is
  split across the 16:30 and 17:30 chain pair by design)
