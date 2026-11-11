---
title: passes 2026-11-08 ticker-1851 queue run
created: 2026-11-09T02:57:00Z
modified: 2026-11-09T02:59:00Z
version: 1.0.0
description: Shop claims unit passes-2026-11-08-1457 executed by ticker-1851
status: done
grounded_in:
  - source: game screens observed live on the owner Mac mini, 2026-11-08 about 18:52 to 19:05 PT
---

# passes 2026-11-08 ticker-1851 queue run

- Unit: passes-2026-11-08-1457 (regular passes, activity shop-claims)
- Executor: ticker-1851
- Session window: about 18:52 to 18:58 PT, 2026-11-08 (device session cc-149)
- Status: done

## Performed

- Hot Deals free pack claimed in the new reset day (after the 18:00
  reset) - Drone Great Value Pack: Drone Parts x20, Battle Data 10K x4
  (shown as 40.0K on the congratulations screen), Skill Chip Chest
  (SR) x2. The pack then read "Packs sold out".
- Weekly Pass page Free Supply auto-claim fired on opening the page -
  "Violet's Gift received!", "Free rewards have been automatically
  claimed": chest x1 and ruby x10.
- Super Monthly Pass Daily Gift claimed (green Claim Reward button):
  gold ticket x2, red diamond 100 x1, stamina 50 x2, iron 200,
  5-minute speedup x60. The button then greyed out. Pass reads Days
  Left 13, Rewards Left 13.
- Weekly Deal tab checked: paid packs only (Valor Badge $99.99, Base
  Upgrade $19.99, UR Set $49.99), nothing claimed. Its period reads
  2026-11-9 00:00:00 to 2026-11-15 23:59:59.

## Checked only

- Weekly Pass page: no owned pass remains. The S2 Drone Components
  Weekly Pass (Legendary) and the S1 Drone Parts Weekly Pass (Epic)
  both show a Get Now $4.99 price button, i.e. unowned offers, not
  claims; neither was tapped. The Coin Weekly Pass seen 2026-10-25 is
  no longer listed. The Legendary "Instant Gain on Purchase" row reads
  Take All $19.99 and was not tapped, per the standing red line.
- The Weekly Pass list did not move under a scroll or a drag; the
  three rows above are the full list as observed.
- The Season Battle Pass / Season Weekly Pass claim was not hunted in
  the Season hub, per the 2026-11-08 ticker-1434 finding (Issue #469):
  the Week 8 hub path is stale.

## Open questions

- The Weekly Pass page reads "Weekly Pass rewards reset at 18:00:00".
  RESOLVED in this unit: the daily reset is 18:00 local since DST
  ended 2026-11-01 (02:00 UTC); the 19:00 figure in older records is
  the PDT-era time. Today's day INDEX already records the 18:00
  reset. The passes claims in this unit are the new reset day's
  claims, and the unit ran late (its 14:57 slot, expiry 18:57) -
  finished 18:58, just after expiry. Duration 378 seconds per the
  unit's structured result.
- The two weekly passes owned 2026-10-25 (S1 Drone Parts, Coin) have
  expired with no replacement bought; whether the owner wants a new
  weekly pass is an owner decision, not an executor call.

## Red lines

- No diamonds or money spent. No price button tapped. The $19.99
  Legendary Take All and the $24.99 Monthly Pass Extension were left
  untouched.

## Correction (same pass, 18:59 PT)

- The first draft of this file was written with estimated times
  (19:05 finish, about 13 minutes) and the file was first named
  1905-queue-run.md. The live clock showed 18:58 at close and the
  unit's structured result records 02:51:53Z to 02:58:11Z, 378
  seconds. The file was renamed to 1858-queue-run.md, the unit's
  evidence path and its costs stat were corrected to 378 seconds,
  and the times above were corrected. Nothing about the claims
  changed.
