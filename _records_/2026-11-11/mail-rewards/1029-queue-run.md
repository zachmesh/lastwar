---
title: Mail rewards queue run 1029
created: 2026-11-11T18:29:00Z
modified: 2026-11-11T18:29:00Z
version: 1.0.0
description: Mail rewards unit mail-2026-11-11-0630 executed by ticker-1012
status: done
---

# Mail rewards — queue run 1029 (unit mail-2026-11-11-0630)

- Unit: `mail-2026-11-11-0630`, regular `mail`, activity `mail-rewards`
- Executor: ticker-1012; token acquired about 10:12 PT; claimed about 10:15 PT; finished about 10:29 PT
- Session: cc-593, Last War window 636402 (642x951, fixed size)
- Status: done — every mail category walked, every claimable attachment claimed

## Entry state (base HUD, read live about 10:15)

- Food 680.8M, iron 1.0G, coin 127.8M, gold 13.22K, diamonds 6,317
- Total Power 149,218,973; stamina 110
- Mail button carried a red dot

## What was claimed

### Event — Claim All (gift icon on the category row)

- 2x Zombie Invasion - Intel Reward (1h, 2h ago) and 3x [AP3x] Missile Apex train mails (2h, 4h, 6h ago); Stamina Returned / Attack Canceled (7h ago) carried no attachment
- CONGRATULATIONS popup ("Alliance Gifts received!"): event medals x530, hero EXP 4.4M, unidentified blue icon 3.0K, stamina items 10x4, coin 1.8M, food 1.4M, iron 1.4M
- After claiming: all envelopes open, no gift icons, no red dots, Claim All red dot gone

### System — Claim All (two gift icons, red dot on Claim All)

- Maintenance Completed (10h ago) and Unclaimed Survey Reward (12h ago)
- REWARD CLAIMED popup: red gem x400
- Patch Notes (11h ago, unread), Planned Update Notice, (President Mail) Transfer Update, Season Closed — no attachments

### Alliance — Claim All pressed, nothing claimable

- Daily Donation Rankings (16h ago), Voting Results (18h ago), 3x New Alliance Assembly Point (1d ago), Attention R5 (1d ago); no gift icons, no red dots, no popup after Claim All
- Assembly Point mails are informational only; no assembly action taken

### Regular — Claim All pressed, nothing claimable

- Six Victory / Invading Zombies battle reports (1h-3h ago), no gift icons, no red dots

### Battle Report — Claim All pressed, nothing claimable

- Victory vs Lv.15-20 Zombie Horde reports (1d ago), no gift icons, no red dots

### Favorite — Claim All pressed, nothing claimable

- One favorited mail: Victory in Attack vs RebelSerpent, 785 units defeated, dated 1-21; no gift icon
- Note: tapping the Favorite row body did not navigate; the row arrow at the right edge did

### In-app Purchases — not opened

- Receipts only per the activity metadata; nothing to claim

## Exit state (base HUD, read live about 10:29)

- Food 682.2M (+1.4M), iron 1.0G (HUD rounding hides +1.4M), coin 129.6M (+1.8M), diamonds 6,717 (+400)
- Total Power 149,218,973 (unchanged); stamina 112 (+2 regen during the unit)
- Mail button red dot gone
- HUD deltas verify the Event popup (coin, food) and the System popup (diamonds) exactly
- The unidentified 3.0K blue icon from the Event popup is recorded as read but unidentified; the 530 medals and 4.4M hero EXP have no HUD counter to verify against

## Method note for later units

- `computer.control` coordinates are 0-1000 normalized, not window pixels: a click at pixel (599,756) landed at normalized (599,756) = pixel (385,719) and missed Mail. Grounding the Mail button (normalized 931,785) and clicking there opened Mail. All later clicks in this unit used normalized coordinates from screenshots/grounding and worked.
- Dismissing a reward popup: one tap on the dimmed area above the banner closed it.
