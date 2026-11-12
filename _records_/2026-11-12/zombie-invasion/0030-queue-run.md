---
title: Zombie Invasion queue run 0030
created: 2026-11-12T08:32:00Z
modified: 2026-11-12T08:32:00Z
version: 1.0.0
description: Queue unit 023, chain zombie-2026-11-10 - event verified live, stamina refilled, Lv.10 target found but not dispatched, unit cap reached
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, sessions cc-683 and cc-685, 2026-11-12 00:15-00:31 PT
---

# Zombie Invasion — queue run 0030 (unit 023, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-023`, chain `zombie-2026-11-10` seq 23
- Executor: ticker-0004; token acquired about 00:15 PT, claimed 00:15 PT; finished about 00:31 PT
- Session: cc-683 dropped once mid-unit (observe returned observation_unavailable with no session open); restarted as cc-685, LastWar re-selected, no game state lost; Last War window 676414 (windowed 642x951, not fullscreen); no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, no kills, no LOOT rows claimed in-unit

## Event state (Glacieradon variant, read live)

- Event timer 1d 17:37:27 at about 00:24; "Challenge begins in: 17:37:28"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:32:08 at the 00:24 read (about 00:56 local); the wave that arrived about 23:57 still had targets — Search found a Lv.10 card at once
- Alliance Finding: Lv.80 Zombie Boss 376km, Lv.85 407km, Lv.80 421km, Lv.80 323km
- 40/40 bar (unchanged from unit 022)

## Entry state (base HUD, read live)

- Food 698.1M, iron 1.0G, coin **143.4M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **8** at entry (unit 022 closed at 1 at 23:42; +7 over about 42 minutes, about 1 per 6 minutes regen)
- The exact coin panel was not opened this unit; coin figures are HUD-rounded like units 021 and 022

## Stamina refill — 1x 50-stamina item used

- Inventory (900,870) → Special tab already open. The grid did not move on a scroll action; a drag (498,578) to (498,315) scrolled it.
- Live counts on the scrolled grid: **50 Stamina x666, 10 Stamina x655** (unit 054 on 2026-10-30 read 611/624 — the counts rose since, likely from rewards; not investigated).
- Tapped 50 Stamina (218,482) → "50 Stamina — Use this item to gain Stamina." → Use (498,952) → toast "you've acquired 50 Stamina", count **666 → 665**.
- Stamina after is 58 derived (8 + 50), not re-read live — flagged here, not a closing count. The 10-stamina count (655) was not touched.
- The Free Claim location is still not found; the item refill is the working route.

## Target found, not dispatched

- Events (930,149) → Zombie Invasion page, title verified. Search (377,952) → world map centred on a target, card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:31:38 at first read (11:28:24 on the re-read three minutes later).
- The dispatch was not reached: the unit cap arrived while the attack button was being located. The crossed-swords point grounded by unit 022 — (500,753) — was NOT tried this unit; the point tapped instead, the blue arrow at (386,783), is a base-visit button, not the attack button: it opened the ally base profile #2110 [AP3x]MegaLoki (Power 114,968,839, Kills 7,905,115), closed by tapping map ground, which opened a second ally profile, #2110 [AP3x]Jerry — left open at unit close (benign; the successor resets with BASE per the activity metadata). No rally, no attack, no purchase, nothing spent in either profile.
- The red circle with a white X at about (498,736) on the target view sits next to the "Lv.12 Marshal's Guard, Preparing: 38:32:45" label — read as that spawn's marker, not the zombie attack button. The successor should tap the unit-022-grounded crossed-swords point (500,753) directly after Search and verify the deploy panel opens before March.

## Claims and Store

- No LOOT rows claimed (no kills in-unit); the gift-box badge was not read. Coin HUD unchanged at 143.4M.
- Store not visited this unit. No medal balance re-read (no derived balance is reported), no Coin Chest redemption, no medals spent.
- Chests opened: 0. The SSR chest row re-check and the Buy-step retry from units 047/052 stay open for the next unit, as does the below-fold Store scan from unit 017's follow-up. The owned Coin Chest (SSR) inventory location is still unknown — the Special tab grid seen this unit holds no coin chest on its first two pages.

## Notes

- The pass started late: token acquired 00:15, eleven minutes into the 00:04 tick, after the PR checks and stats reads. The unit therefore had about ten minutes of game time, not fifteen — the refill plus one Search filled it. The next tick's unit inherits stamina 58 and a known-live target.
- Grounded points on the 642x951 windowed view this unit (normalized 0-1000 window coordinates): Events (930,149); Search (377,952); Inventory (930,836); 50 Stamina item (218,482); Use (498,952). The blue arrow at (386,783) is a base-visit button — do not tap it for an attack.
- Cleared is false — Search found a target immediately and the next wave arrives about 00:56; successor 024 enqueued to start now.

## Result stats

- zombies_killed: 0
- cleared: false
- coin_before: 143400000 (HUD-rounded)
- coin_after: 143400000 (HUD-rounded)
- coins_collected: 0
- medals_before: not measured (Store not visited)
- medals_after: not measured (Store not visited)
- chests_opened: 0
- squads_parallel: 0
- stamina_before: 8 (live read)
- stamina_after: 58 (derived from 8 + 50 item, not re-read live)
- stamina_items_50_before: 666 (live read)
- stamina_items_50_after: 665 (live read)
- stamina_items_10: 655 (live read)
- target: 2 Lv.10 kills in parallel, both LOOT rows claimed
- achieved: 0 kills — stamina refilled, Lv.10 target located, dispatch not reached in unit time
- resources_gained: none
- costs: about 15 minutes, 1x 50-stamina item
- verified: yes (coin, stamina item counts and event timer live-read; stamina_after derived, flagged)
- blocker_category: h
- blocker: unit cap reached mid-dispatch after a late pass start; attack-button location not re-grounded in the time available
