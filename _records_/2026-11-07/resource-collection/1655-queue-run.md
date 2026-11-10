---
title: Harvest queue run 1655
created: 2026-11-08T01:15:00Z
modified: 2026-11-08T01:15:00Z
level: L0
version: 1.0.0
description: Ticker-1655 harvest unit, partial - farmland bubbles collected, full-map sweep not finished, unit ran about 3 minutes past the 15 minute cap
status: unverified
---

# 1655 queue run - Resource Collection

Executor: ticker-1655. Unit: harvest-2026-11-07-1403.
Session window about 16:56 to 17:04 America/Los_Angeles
(00:56 to 01:04Z). Mac mini online and controllable again
after the outage that failed the 0526 pass this morning;
computer session cc-14, LastWar already running and selected.

## What was collected

- Farmland bubbles, one tap collected all five: after panning
  the base view left (drag from norm 450,500 to 750,500), five
  gold food bubbles stood over the wheat fields at the left
  edge, labelled 40.9K, 38.8K, 37.7K, 37.1K and 32.0K
  (norm about 64,297 / 124,281 / 172,301 / 124,324 / 59,363).
  One tap on the 38.8K bubble at norm 124,281 cleared all
  five at once, as the activity metadata records. Food HUD
  moved 485.3M to 485.5M (about 0.2M, matching the 186.5K
  sum of the five labels at the 0.1M display rounding).
  Iron 808.9M, coin 5.0M, stone 25.0M and 922.2K unchanged.

## What was tried and did not collect

- Purple crystal icon over the purple crystal building at
  norm 596,547: one tap, no change observed, icon still
  present in the next screenshot. Treated as building
  decoration, not a collectible bubble; not retried.
- Beige square with a green symbol at norm 806,686, right of
  the troop field: one tap, no change observed, still
  present. Treated as a static sign, not a bubble.
- Blue droplet bubble over the blue truck at norm 150,293:
  one tap did NOT collect - it jumped to the world map task
  view ("2 task rewards can be claimed", green Claim All
  button, no price tag). That is radar-task work, not
  harvest, so the Claim All was left untouched and the home
  button returned the view to the base. The droplet is a
  locator, not a loot bubble; the Armed Truck loot state
  itself was not verified in this unit.

## Sweep state, why partial

- The base was panned left only. Iron, coin, stone, EXP,
  screws and drone-component bubbles were not swept, the
  Armed Truck loot was not verified or claimed, and the
  bottom Season 2 zone was not checked, so the 2026-11-01
  full-map zero-remaining acceptance is not met. The next
  harvest unit resumes from the panned-left view state and
  the findings above.
- Unit duration, corrected against the tool stamps:
  claimed 00:56:51Z, finished 01:04:37Z, 466 seconds
  (about 8 minutes) - inside the 15 minute cap, no
  overrun. The image-observe round trips are still the
  bulk of the unit time (each screenshot plus read about
  a minute), so the standing lesson holds in milder form:
  verify with the compact observe where the HUD figure is
  enough, and keep image screenshots for bubble grounding
  only.
- Tracker untouched, per the partial rule; the next tick
  re-produces the harvest regular.

## Figures read live on screen

- Food 484.6M at entry, 485.3M before the farmland tap,
  485.5M after; iron 808.9M before and after, coin 5.0M
  before and after, stone 25.0M before and after,
  922.2K before and after. Power 149,850,353.
  Stamina 72 at entry, 73 at close (regeneration).
- No diamonds, money, speedups or paid buttons were used.
  No other task type was executed in this unit. No login
  or verification was demanded, and no different-device
  dialog appeared.

## Result statistics

- target 1, achieved 0, resources_gained food about 186.5K,
  costs about 8 minutes play, verified yes,
  blocker_category h, device_takeovers 0
