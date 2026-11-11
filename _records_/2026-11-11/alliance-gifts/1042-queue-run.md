---
title: Alliance gifts queue run 1042
created: 2026-11-11T18:42:00Z
modified: 2026-11-11T18:42:00Z
version: 1.0.0
description: Alliance gifts unit gifts-2026-11-11-0630 executed by ticker-1012
status: done
---

# Alliance gifts — queue run 1042 (unit gifts-2026-11-11-0630)

- Unit: `gifts-2026-11-11-0630`, regular `gifts`, activity `alliance-gifts`
- Executor: ticker-1012; token renewed about 10:28 PT; claimed about 10:28 PT; finished about 10:42 PT
- Session: cc-594 (cc-593 dropped between units; fresh session started), Last War window 636402 (642x951)
- Status: done — both tabs claimed, plus late arrivals claimed on a re-check; Alliance Gifts red dot gone

## Entry state (read live)

- Alliance panel: [AP3x] The Apex, Leader Abÿss Apex, Power 13,807,816,778, Members 96/100, English
- Alliance Gifts entry carried a red dot; both tabs carried red dots
- Gift Level 28, progress 206,145,210 / 206,300,000 at entry (Level 29 at 206,300,000)

## Regular tab — Claim All, 310 + 2 late arrivals

- First Claim All (badge 310): "A total of 310 Regular Alliance Gifts were claimed this time". Rows were Doom Elite / Zombie Boss kills at +10 points each (Raze Cromwell, MetalMick).
- Rewards grid as displayed: red gem 5 (sub-count 45), horn 5m (31), food 1.0K (1.0K), coin 600 (1.5K), iron 1.0K (1.1K), food 10.0K (28), coin 6.0K (56). Item identities beyond the icon are recorded as displayed, not independently verified.
- Progress after the claim: 206,155,470 / 206,300,000.
- Re-check after the Premium claim found the entry red dot still lit: 2 new Regular gifts had arrived — Doom Walker Loot (23:58:14, MegaLoki Apex Defeated Doom Walker) and Alliance Gifts (23:58:11, Nuna Knuckles Defeated Zombie Boss), both +10. Second Claim All: "A total of 2 Regular Alliance Gifts were claimed this time".
- Regular total this unit: 312.

## Premium tab — Claim All, 19

- First view showed badge 18; by claim time one more had arrived (Demoralyzed™ purchased Take All, SSR +200, 23:59:45), badge 19.
- Claim All: "A total of 19 Premium Alliance Gifts were claimed this time". Rows were SSR +200 / SR +100 from ally purchases (Preparation Rare Pack, Preparation Premium Pack, VIP Exclusive, Take All).
- Rewards grid as displayed: gold badge 2.5K x1, purple badge 500 x1, purple chest x11, gold coins x18, brown bundle x10, blue chest x6, gold badge 50 x5, red gem 20 x1, horn 5m x2, red gem 5 x1. The red gem is the same icon as the diamond currency; the exact mapping of grid cells to inventory is not independently verified.
- Progress after the claim: 206,160,470 / 206,300,000.
- Premium total this unit: 19.

## Progress note

- The Gift Level progress is alliance-wide, not solely this unit's doing: it read 206,168,150 and later 206,168,170 while this unit claimed nothing in between, so allies claiming also moves it. Do not attribute progress deltas to this unit's claims alone. Last read: 206,168,170 / 206,300,000 (131,830 short of Level 29).

## Verification (read live)

- After the second Regular claim, Premium re-checked: every row "Claimed", no Claim All button, no red dot on either tab.
- Alliance panel after exit: Alliance Gifts red dot gone. (Alliance Wars, Help, Alliance Store, Alliance Techs still carry red dots — other units' work.)
- "Hide your name on Gifts" checkbox was never touched; verified still unchecked after a stray click (see method note).

## Method note for later units

- The Premium Claim All button sits further right than the Regular one (the "Hide your name on Gifts" checkbox occupies the left): Regular Claim All is at normalized (498,936), Premium at (744,939). A first Premium attempt at the Regular coordinates missed the button and landed on empty space; corrected after a screenshot. Always re-ground the button per tab.
- `computer.control` coordinates are 0-1000 normalized, not window pixels (see mail unit 1029 the same pass).
- The computer session dropped between the mail and gifts units (cc-593 gone); a fresh session (cc-594) was started and the window re-selected with no loss.
