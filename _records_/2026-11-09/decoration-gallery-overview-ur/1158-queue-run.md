---
title: Decoration Gallery Overview queue run 1158
created: 2026-11-09T19:58:00Z
modified: 2026-11-09T19:58:00Z
version: 1.0.0
description: Ticker-1134 scout discovery unit 017, Decoration Gallery entry not re-located - the known mis-tap point now opens the Mega Express Contract offer instead; overview values already measured by unit 002
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 11:55-11:58 PT
---

# Decoration Gallery Overview queue run 1158 (ticker-1134)

Unit: scout-scout-discovery-2026-11-09-017. Status: partial.
Activity: decoration-gallery-overview-ur (candidate exploration,
read-only learning).
Chain: scout-discovery-2026-11-09, seq 17.

## Live reads

- Base screen at entry: coin 46.2M, power 149,217,331,
  unchanged.
- The tap at normalized [44,284] - the point unit 002's
  mis-tap opened the Decoration Gallery from - did NOT open
  the gallery this time. It opened the MEGA EXPRESS
  CONTRACT offer popup instead: a golden train, "Availability
  today: 0/2", Rewards (red gem 10.0K, a ticket x1, blue gem
  1.0K, 5m speedup x600, a gear-crate item), "Use to
  instantly call a highly rewarding Alliance Trade Train!",
  priced $99.99 for 1000 purple gems, with a Refund Policy
  link. The popup was closed with its X, untouched - no
  purchase, nothing claimed. The $99.99 button was never
  tapped.
- The gallery itself was not opened in this unit, so its
  tabs beyond Overview stay unmeasured.

## What was learned

- The Overview values are already measured: unit 002
  (ticker-0744) read the gallery Overview in full -
  Collection Progress UR 18/39, SSR 7/19, SR 4/4, Total
  Decor Combat Power 6,160,413, and the seven bonuses
  (Hero Attack +5494, Hero Defense +810, Hero HP +172515,
  March Size +2, Damage to Monsters +1.62%, Construction
  Speed +15.00%, Secret Mobile Squad Dispatch +3) - and
  those values match the day observation file exactly.
  This unit adds no new gallery figures.
- The entry point is unreliable: the [44,284] mis-tap that
  opened the gallery once now opens a paid offer. Per R2,
  the next unit must re-ground the gallery entry fresh
  (the left-edge icons shift with the base view) instead
  of re-tapping [44,284].
- Incidental: the Mega Express Contract offer is documented
  above - a $99.99 train-call offer, availability 0/2
  today. No owning regular or issue exists for it; it is
  recorded here as an observed paid offer, not a task.

## What was done

- One entry attempt, popup closed untouched, game returned
  to the base screen. Nothing claimed, nothing spent.

## Not done in this unit

- The gallery was not opened, so tabs beyond Overview and
  any per-rarity detail stay unmeasured. Follow-up: a
  successor unit re-grounds the entry from a fresh base
  screenshot and reads the gallery tabs.
- The provisional profile was NOT written into _activities_/
  (tier 2, left for the knowledge PR flow). No issue filed
  for the gallery - the overview is already measured and
  the entry problem is a method note, not a knowledge gap.

## Red lines

- No diamonds or money spent. The $99.99 Mega Express
  button was never tapped. No other unit's work touched.

## Stats

- target: learn-decoration-gallery-profile-fields
- achieved: 0
- resources_gained: none
- costs: about-3-minutes-no-items-spent
- verified: yes
- blocker_category: c
- points: 0
- surfaces_walked: base-screen, mega-express-contract-popup
- items_observed: 0
- red_dots_seen: 0
- red_dots_explained: 0
- unexplained_red_dots: 0
- unknown_items: 1
