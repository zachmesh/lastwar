# Resource Collection — queue run 0909 (unit harvest-2026-11-11-0603)

- Unit: `harvest-2026-11-11-0603`, regular `harvest`, activity `resource-collection`
- Executor: ticker-0845; token acquired 08:54:48 PT; claimed about 08:55 PT; game work about 08:56 to 09:09 PT
- Session: cc-582, Last War window 636402
- Status: partial — panel pools collected exact, full-map sweep and Armed Truck check unfinished at the unit clock
- Note on times: the queue record stamps finished_at at the complete call, which ran after the radar unit; the game work for this unit ran about 08:56 to 09:09 PT (about 13 minutes), not the stamped duration.

## Entry state (base HUD, read live)

- Food 672.7M, iron 995.1M, coin 123.3M, gold 13.22K, diamonds 6,317
- Total Power 149,218,973; stamina 15 at entry (16 by the radar entry read)
- Entry screen was the world map, left open by the previous unit; the red zombie/boss figure stood top-right with the home button reading 101 km

## Panel Collects — all three pools, exact reads

Standing method (Issue #585, verified 2026-11-10): open each resource top-bar icon, read Available Resources, tap Collect, verify Owned moved and Available is 0.

| Panel | Available before | Owned before | Owned after | Gained |
| --- | --- | --- | --- | --- |
| Coin | 2,104,312 | 123,336,772 | 125,441,084 (HUD 125.4M) | 2,104,312 |
| Food | 3,233,161 | 672,702,700 | 675,935,861 (HUD 675.9M) | 3,233,161 |
| Iron | 3,006,548 | 995,170,680 (HUD 995.1M) | 998,177,228 (HUD 998.1M) | 3,006,548 |

- Total collected: 8,344,021 (food 3,233,161 + iron 3,006,548 + coin 2,104,312).
- Each panel re-read Available 0 after its Collect; the HUD deltas match the panel figures exactly.
- Panel details read live: coin Building Acquisition 441.9K/H, Resource Items 400.2M, Optional 1.3G; food 674.9K/H, Resource Items 3.4G, Optional 2.3G; iron 622.7K/H, Resource Items 3.8G, Optional 2.3G. No Use button tapped on any resource-item row.
- Entry corrections: a tap on the food number text at (265,55) opened nothing; the food icon itself grounds at (233,52). The iron icon tap at (390,53) opened nothing on the first try and opened the panel on the second identical tap — a panel open can need a repeat tap; the receipt's "no change" is not proof the tap missed.

## Armed Truck — eighth deferral (Issue #566)

- First action per R7 was the truck check, via the left-edge truck icon: it opened the Secret Command Post (Secret Mobile Squad), not Trade — the same elimination the 1531 unit recorded. Nothing was tapped there; the panel was closed with the slow swipe-back (see below).
- The trade-screen method from the 1531 unit was not reached in this unit: no Trade entry was located on the base or map screens in the time available.
- Parked vehicles (red jeep, blue truck, green tank) at the base bottom-left showed no collect bubble over them in the closing view; the bottom-left hint tooltip seen by the 2042 unit was not visible this unit.
- This is the eighth consecutive harvest unit to defer the Armed Truck check (0636, 1220, 0257, 0826, 1210, 1531, 2042, this unit). The loot check stays the first action of the next harvest unit per R7. Commented on Issue #566 by this pass.

## Map bubbles after the panel Collects — identity unverified

- After all three panels read Available 0, the base view still showed round icons over the production buildings (furnace row, farm cluster, left-side buildings).
- A crop of the farm/mines sector (x60-280, y330-530, upscaled 3x) shows NO value-labelled bubble in that sector: the iron mines and wheat are bare, and the round icon over the mines is the roaming red-panda pet (a known fall-through hazard, not a bubble).
- No bubble was tapped this unit, so whether the standing round icons hold value after a panel Collect (regrowth in the minutes since the Collects, or a separate accumulation the panels do not drain) is UNVERIFIED. The next harvest unit must crop-ground a bubble centre from a fresh screenshot and tap once, then re-read the HUD, before assuming the icons are collectible or decorative. The 2042 next-test (Issue #502) stays owed.
- The visual grounding tool mislabelled the top-bar resource icons as bubbles (points at y 54); never tap a grounding point that lands on the HUD.

## Panel close method — background-click X unreliable

- The Secret Command Post back arrow did not respond to two background clicks; the slow manual swipe (mouse down at (20,500), stepped moves to (200,500), mouse up) closed it.
- The iron panel X did not respond to two background clicks (one snapped, one unsnapped); the same slow swipe closed it.
- The coin and food panel X taps appeared to work. Panel X responsiveness to background clicks is inconsistent in this session; the swipe-back is the reliable close.

## Other observations

- "Alliance Gifts received!" toast appeared on the base view after the panel Collects (also seen by zombie units after LOOT claims); cause not established in this unit, quoted verbatim.
- A red skull icon with a countdown (00:00:51, then 00:00:17, then 00:00:30 with badge 2, then 00:00:19) stood at the base right edge through the unit; it was gone in the closing base view after the radar unit. Not investigated here — it belongs to the zombie-invasion unit (013 in inbox).
- No "active on a different device" dialog; no access error; no diamonds or money spent; no speedup used; no building panel action taken.
- No game input was delivered to the Secret Command Post beyond opening and closing it.

## Result stats

- target: collect all ready resource pools and bubbles
- achieved: all three panel pools collected exact; map bubbles not tapped; Armed Truck not located
- resources_gained: food 3233161, iron 3006548, coin 2104312
- costs: about 13 minutes of game work; 0 stamina items, 0 diamonds
- verified: yes (panel Owned/Available reads before and after each Collect; HUD deltas match)
- blocker_category: h (by-design partial, unit cap reached mid-sweep)
- bubbles_collected: 0
