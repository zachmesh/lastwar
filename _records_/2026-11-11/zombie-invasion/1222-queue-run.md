# Zombie Invasion — queue run 1222 (unit 015, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-015`, chain `zombie-2026-11-10` seq 15
- Executor: ticker-1204; token acquired 12:21:xx PT, released, re-acquired 12:24 PT, released 12:31 PT; claimed about 12:22 PT; finished about 12:31 PT
- Session: cc-601 (first attempt, ended), cc-602 (retry); Last War window 636402; no drop, no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, second squad not dispatched

## Event state (Glacieradon variant, read live)

- Event timer 2d 05:38:44 at about 12:26; "Challenge begins in: 1d 05:38:45"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:33:19 at the 12:26 read (about 12:59 local), 00:29:58 at the 12:28 re-read
- Alliance Finding: Lv.85 Zombie Boss 279km, Lv.80 333km, Lv.80 290km, Lv.85 223km (Roronoa zo, Niermeat)

## Entry state (base HUD, read live)

- Food 685.1M, iron 1.0G, coin **131.9M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **95**

## First dispatch attempt — batched, failed (method lesson)

- Batched Events → wait 1 → Search (366,950) → wait 2 → crossed-swords (499,753) → wait 2: the view jumped to the world map but no target card was open, so the swords tap hit empty map and nothing dispatched. Stamina stayed 95.
- Lesson applied (unit 053): single-step dispatch with a screen read between steps. The Search point (366,950) itself is correct — the same point worked on the retry. The failure was the batch assuming the card would be open 2 seconds after Search while the Events hub was still settling.

## Dispatch — Squad 1 → X:517 Y:417 (Lv.10)

- Single-step: Events (942,158) → tab verified Zombie Invasion → Search (366,950) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:29:41.
- Crossed-swords grounded fresh at (498,731) on the current card view (unit 049's 499,753 sits high on this card); deploy panel read Squad 1, Easy Win, march about 00:03:57.
- March (500,755) dispatched; stamina 95 → 86 (10 charged, 1 regen); March Queues 1/4, "Go X:517 Y:417" 00:00:38 at the read; squad Returning about a minute later, home (0/4) before the LOOT claim.

## Second dispatch attempt — March failed, squads_parallel 1

- Batched Events → wait 1 → Search → wait 2 opened a second Lv.10 card cleanly (Suggested Power 670,000); swords opened the deploy panel (Easy Win, march 00:01:13).
- March (500,755) produced no march: stamina stayed 86, March Queues stayed 1/4 with squad 1 Returning, and the receipt carried an "Unable to..." toast line. The target had most likely been taken or moved between the card read and the March tap (the stale-target failure of unit 006). No stamina was charged.
- squads_parallel is therefore 1 for this unit: only one squad was ever out at once, because the parallel attempt failed at the March step, not for lack of trying. Successor: re-Search for a fresh target rather than re-tapping the same card.

## Claims — 1 LOOT row × 268,000 coins = 268,000

- Row: Lv.10 Invading Zombies, X:517 Y:417 (squad 1's kill).
- Gift-box hunt: the badge-1 icon at the right end of the March Queues bar (about 293,210, then 311,221 after a map drag) opened the [UCKF]DaLoneWolf89 player profile twice — the base sat under the icon and its tap radius is larger than the icon's (units 053/063). After a map drag moved the base clear, a snap-free tap at (311,221) opened the LOOT panel at once. Claim All at (499,780) is plain blue, no price tag; panel closed on the tap.
- Coin HUD verified: **131.9M → 132.1M** (+0.2M displayed, 268,000 by the row); food 685.1M → 685.4M (+268,000). Gift badge gone after claiming.
- Medals: before 4140 (unit 013's derived close, carried); after 4150 **derived** (+10 for the claimed kill), not live-read — flagged here, not a closing count.

## Store

- Not visited this unit (token lease ended at the LOOT claim). No medal balance re-read, no redemption, no medals spent.
- Chests opened: 0.
- Stamina 87 at close (95 − 10 spent + 2 regen); no refill needed; inventory stamina count not checked, no refill conclusion drawn.

## Notes

- The Events hub Search button grounds at (366,950) on this layout — unit 057's (441,940) is a different tab-bar shift; always ground Search fresh on the current hub screenshot.
- The crossed-swords button grounds at (498,731) on the current card — unit 049's (499,753) sits high here; ground it fresh per card.
- The gift-box icon sits at the right end of the March Queues bar (about 311,221 on this map view) but a player base under it swallows the tap; drag the map to move the base clear first, then tap snap-free.
- Token lease expired 12:39:08 PT; the unit closed at the claim with squad 2 undispatched rather than re-attempting. Cleared is false, successor enqueued to start now.

## Result stats

- zombies_killed: 1
- cleared: false
- coin_before: 131900000 (HUD-rounded)
- coin_after: 132100000 (HUD-rounded)
- coins_collected: 268000
- medals_before: 4140 (derived, carried from unit 013)
- medals_after: 4150 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 1
- target: kill wave zombies and claim LOOT
- achieved: 1 Lv.10 kill dispatched, 1 LOOT row claimed (268,000 coins)
- resources_gained: coins 268000, iron 268000, food 268000, medals 10, hero EXP 263000
- costs: about 10 minutes, stamina 95 to 87
- verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
- blocker_category: c
