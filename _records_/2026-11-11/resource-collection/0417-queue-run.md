# Resource Collection — queue run 0417 (unit harvest-2026-11-11-0203)

- Unit: `harvest-2026-11-11-0203`, regular `harvest`, activity `resource-collection`
- Executor: ticker-0404; claimed about 04:13 PT; finished about 04:17 PT
- Session: cc-555, Last War window 636402; token held until 04:20:36 PT (lease), unit claim lease until 04:32:45 PT
- Status: partial — most bubbles collected; 1–2 small coin bubbles remain and the Armed Truck state was not checked

## Entry state (base HUD, read live)

- Food 668.2M, iron 990.9M, coin **119.5M**, gold 13.22K, diamonds 6,307
- Total Power 149,218,973; stamina 48

## Collections (HUD-verified)

| Tap | Result (HUD) |
| --- | --- |
| Bubble at (202,431) | Iron 990.9M → 992.7M (+1.8M); food/coin unchanged |
| Food bubble at (330,407), centre grounded on a 2x crop | Food 668.2M → 670.2M (+2.0M); **all farmland bubbles cleared at once**, as the activity metadata says |
| Coin bubble at (86,421) | Coin rising (see final) |
| Coin bubble at (156,447) | Coin rising (see final) |

- Final HUD: food **670.2M**, iron **992.7M**, coin **120.9M** (+2.0M food, +1.8M iron, +1.4M coin over the unit)
- Note on the coin delta: the two coin bubbles read 236.0K and 279.8K on their labels (~0.52M), below the +1.4M HUD move; the per-bubble split is unverified — HUD deltas are the closing figures, not the label sum.

## Mis-taps and panel handling

- A tap at (280,415) missed the food bubble and opened the Iron Mine Lv.27 panel; a later tap at (93,478) opened the same building's Building Details panel instead of the coin bubble beneath it. Building panels open easily when a bubble sits over a building — ground bubble centres on a cropped zoom before tapping.
- Iron Mine Lv.27 (read live): Output/hr **+129,258**, Max Production Time **11hr 36min**, Survivors Taylor, Harry, Samantha, Javier — all Miners, Javier assigned (green check, +54.00% Boost Iron Output; others +24.00%).
- The Survivor List X did not respond to two taps at (833,168)/(829,166), and its Selected button did not close it either; a tap on the dimmed area outside the panel (80,300) closed it. The Building Details X at (830,229) worked on the first tap. No survivor was reassigned and nothing was spent — Javier was already the assigned Miner.
- No building was upgraded and no other purchase was touched.

## Not done

- 1–2 small coin bubbles (~236K each) remain at the left edge of the base; the next harvest unit collects them.
- The Armed Truck (blue truck, centre-right of the base) was not checked for fully-loaded state; its loot was not claimed. Successor: check the truck first.

## Result stats

- bubbles_collected: food all (one tap), iron 1, coin 2
- food_before: 668200000 (HUD-rounded)
- food_after: 670200000 (HUD-rounded)
- iron_before: 990900000 (HUD-rounded)
- iron_after: 992700000 (HUD-rounded)
- coin_before: 119500000 (HUD-rounded)
- coin_after: 120900000 (HUD-rounded)
