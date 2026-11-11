# Zombie Invasion — queue run 1456 (unit 016, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-016`, chain `zombie-2026-11-10` seq 16
- Executor: ticker-1439; token acquired about 14:40 PT, expired 14:56:39 PT; claimed about 14:40 PT; finished about 14:56 PT
- Session: cc-627; Last War window 636402 (1920x1080, covered by Chrome) then 676414 (642x951 windowed after relaunch); no drop, no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, 2 squads dispatched in parallel, LOOT unclaimed (both squads still in flight at close)

## Event state (Glacieradon variant, read live)

- Event timer 2d 03:07:29 at about 14:56; "Challenge begins in: 1d 03:07:30"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:02:03 at the 14:56 read (about 14:58 local)
- Alliance Finding: Lv.90 Zombie Boss 114km, Lv.90 351km, Lv.85 365km, Lv.85 211km (Roronoa zo)

## Entry state (base HUD, read live, after relaunch)

- Food 688.3M, iron 1.0G, coin **135.6M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **85**
- Stamina check: unit 015 closed at 87 (12:31), but radar-tasks/1233 ran at about 12:33 and spent stamina 88 to 58, so 85 at 14:54 is regen back up, not a discrepancy. No unexplained movement.

## Mail at entry — already claimed by the mail unit, my taps redundant

- The game opened on the EVENT mail tab with a Zombie Invasion - Intel Reward mail open under a CONGRATULATIONS! banner (medal x280, Hero EXP 2.4M, Battle Data 1.5K, 10-stamina x2, coin 969.0K, food 769.0K, iron 769.0K).
- Correction, read after the fact in this day's INDEX: ticker-1408's mail unit 1030 (14:22–14:35) already did Event Claim All and paid exactly those rewards. My two Claim All taps at about 14:41 were redundant no-ops — the game pays once, so nothing was double-claimed and this unit gained nothing from mail. The second tap opened a train-arrival mail ([AP3x] Missile Apex's train has arrived!, informational, no rewards) as the list auto-advanced to the next unread mail.
- The coin move 132.1M (unit 015 close, 12:31) to 135.6M (this unit's base read, about 14:54) therefore belongs to the mail unit's claim plus other passes' income between 12:31 and 14:54, not to this unit. It is not this unit's coin_before/coin_after delta — this unit's own coin_before and coin_after are both 135.6M (no kills landed in-unit).

## Mail-detail back arrow — input-blocked, both tap variants failed

- The train mail detail could not be exited: the back arrow ignored four attempts — coordinate tap snapped (default), coordinate tap snapped explicitly, left-edge swipe drag, coordinate tap unsnapped (snap_to_control=false) — and click_element label "Back" found no enabled control with that label. The mail detail exposes no Accessibility tree (OCR text only); the back arrow is an icon-only control with no AX label.
- Correction, from the rebased branch tip: ticker-1408 measured a tap offset of about (-23 x, +10 y) normalized in the same fullscreen window (issue #652), and the knowledge-organization run withdrew the no-input stop-rule. My taps aimed at the arrow's center (301,958) would have landed near (278,968) — left of the button's edge — so the four no-change taps are consistent with an offset miss and do NOT prove the control input-blocked. The #575 comment filed mid-unit is corrected by a follow-up comment. Open item for the successor: re-test the mail back arrow with offset-compensated taps (+23 x, -10 y).
- Recovery: menu Last War > Quit Last War (the menu title is "Last War" with a space), then open_app relaunch; the app returned to the base screen with state intact. Note the relaunch landed windowed 642x951 (window 676414), not fullscreen 1920x1080.
- Successor units: do not open mail details in background control unless a relaunch is budgeted; the mail unit owns mail.

## First dispatch — Squad 1 → X:586 Y:340 (Lv.10)

- Events → Zombie Invasion tab (the hub remembered the tab on re-entry; the tab bar shifts between openings, verify by title) → Search (378,941 windowed) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:01:33.
- Crossed-swords button in the 642x951 windowed layout is the red X circle BELOW the target card, on the target tile — grounded fresh at (495,754) for this card. Deploy panel read Squad 1, 25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231, march 00:03:05.
- March (495,764, grounded low) dispatched; stamina 85 → 75 (10 charged); March Queues 1/4, "Go X:586 Y:340" 00:03:00.

## Second dispatch — Squad 2 → X:454 Y:281 (Lv.10), parallel

- Events re-opened straight onto the Zombie page (hub remembered the tab). Search → second Lv.10 card, same rewards, despawn 09:59:57. Swords re-grounded fresh at (542,754) — the button moves with the target tile, never reuse the first card's point. Deploy panel auto-selected Squad 2 (2,175/2,175, Easy Win, march 00:03:48).
- March (495,764) dispatched; stamina 75 → 66 (10 charged, +1 regen); March Queues 2/4. squads_parallel 2 — the first parallel dispatch in this chain since unit 052's cap-4 run on 2026-10-30.
- Squad 1 outbound 00:01:42 remaining at the close read; squad 2 00:03:43. Both kills land after this unit closes; LOOT rows (expected 268,000 coins each) must be claimed by the successor — check the gift badge at the right end of the March Queues bar first thing.

## Store

- Not visited this unit (unit budget ended at the second dispatch). No medal balance re-read, no redemption, no medals spent. Chests opened: 0. Medals before/after: 4150 derived (unit 015's derived close, carried) — NOT live-read, flagged, not a closing count.

## Notes

- The app now runs windowed 642x951 (window 676414) after the relaunch, not fullscreen 1920x1080. All taps in this unit used normalized 0–1000 coordinates of the 642x951 window and responded to unsnapped (snap_to_control=false) coordinate taps — Events, Search, swords, March all worked first try in this form. The windowed form is usable; do not assume fullscreen coordinates.
- Cleared is false: Search found targets on two consecutive tries and the next wave was about 2 minutes out at the 14:56 read. Successor (017) enqueued to start now.

## Result stats

- zombies_killed: 0 (0 landed in-unit; 2 in flight)
- cleared: false
- coin_before: 135600000 (HUD-rounded)
- coin_after: 135600000 (HUD-rounded)
- coins_collected: 0
- medals_before: 4150 (derived, not live-read)
- medals_after: 4150 (derived, not live-read)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 squads dispatched in parallel, 0 LOOT rows claimed in-unit
- resources_gained: none in-unit (2 LOOT rows expected, about 268000 coins each, for the successor)
- costs: about 20 minutes, stamina 85 to 66
- verified: yes (coin, food, stamina and march state live-read; medals derived, flagged; mail claim already done by the mail unit, flagged)
- blocker_category: c
