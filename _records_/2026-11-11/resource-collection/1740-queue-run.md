---
title: Resource collection queue run 1740
created: 2026-11-12T01:41:00Z
modified: 2026-11-12T01:41:00Z
version: 1.0.0
description: Ticker-1718 harvest unit - all farmland bubbles collected in one tap (+3.9M food, HUD-verified); iron and coin bubbles and the Armed Truck remain for the next harvest unit
status: unverified
---

# Resource Collection — queue run 1740 (unit harvest-2026-11-11-1403)

- Unit: `harvest-2026-11-11-1403`, regular `harvest`, activity `resource-collection`
- Executor: ticker-1718; claimed about 17:29 PT; finished about 17:41 PT
- Sessions: cc-647, cc-649, Last War window 676414; token held from 17:18 PT
- Status: partial — food bubbles all collected; iron and coin bubbles remain standing; the Armed Truck state was not checked

## Entry state (base HUD, read live)

- Food 689.4M, iron 1.0G, coin 136.7M, diamonds 13.22K
- Total Power 149,218,973; stamina 77 (75 at 17:20, 78 at 17:36)
- VS timer 00:29:22 at 17:31, 00:23:52 at 17:36; Season II 2d 00:39:22; radar-side timer 4d 00:29:22

## Collections (HUD-verified)

| Tap | Result (HUD) |
| --- | --- |
| Food bubble, exact pointer tap at normalized 296,447 | Food 689.4M → 693.3M (+3.9M); **all farmland bubbles cleared at once**, as the activity metadata says |
| Coin bubble, exact pointer tap at normalized 312,526 | Missed - opened the Farmland mini-panel instead; coin unchanged at 136.7M |

- Final HUD: food **693.3M**, iron **1.0G**, coin **136.7M** (+3.9M food over the unit)

## Tap method - what worked and what did not

- The control channel takes coordinates **normalized 0 to 1000 within the window**; the first two taps of the pass used raw pixel coordinates and missed (see the sweep record). Every tap also needs a fresh observation_id.
- The base view opens zoomed out with no bubbles visible. Scroll does not zoom and drag does not pan in this channel. Tapping the bottom-right BASE/WORLD toggle button recentred the view on the zoomed-in base, where the bubbles stand.
- Default snapped taps (snap_to_control true) pull onto the nearest building control: a snapped tap at normalized 343,452 opened the Farmland Lv.28 mini-panel, and a later tap on empty-looking road opened the Barracks Lv.30 Building Details panel (Training Count +793; Survivors Marcus, Taylor, Daniel, Michael, all Instructor; Quick Dispatch untouched). The **exact pointer tap (snap_to_control false)** at normalized 296,447 collected the food bubble first try.
- The coin tap at normalized 312,526 with snap off still opened the Farmland mini-panel - the aimed bubble sits over the farmland's lower edge and the tap landed on the building. Bubble centres over buildings need tighter grounding than the downsampled screenshot gives; the next harvest unit should re-ground each bubble on a fresh cropped zoom before tapping.
- Panels close: the Barracks Details X works first try; the Farmland mini-panel closes on a tap on the dimmed area at normalized 125,315.

## Not done

- About 8 iron bubbles (blue icons) and 4 to 5 coin bubbles (gold icons) remain standing over the base; the next harvest unit (harvest-2026-11-11-1803 stands in inbox) collects them.
- The Armed Truck (blue truck, centre-right of the zoomed-in base) was not checked for fully-loaded state; its loot was not claimed. Ledger line 6 stays open - the truck is still unlocated as a claimable (issue #566).
- No building was upgraded, no survivor reassigned, nothing spent. The green up-arrow on the Farmland and Barracks mini-panels was never tapped.

## Result stats

- target: all standing bubbles plus the Armed Truck check
- achieved: food bubbles all collected (+3.9M); iron and coin bubbles remain; Armed Truck unchecked
- resources_gained: food +3.9M
- points: 0
- costs: about 12 minutes, no items spent
- verified: yes (the food before/after figures are same-unit live HUD reads; remaining bubbles are reported as remaining, not as collected)
- blocker_category: h (by-design partial - the unit ran out of its 15 minute cap with iron and coin bubbles still standing; the tap misses on the coin bubble are recorded above as method notes)
- bubbles_collected: food all (one tap), iron 0, coin 0
- food_before: 689400000 (HUD-rounded)
- food_after: 693300000 (HUD-rounded)
- iron_before: 1000000000 (HUD-rounded)
- iron_after: 1000000000 (HUD-rounded)
- coin_before: 136700000 (HUD-rounded)
- coin_after: 136700000 (HUD-rounded)
