---
title: Queue Run 1537 Alliance Donations Partial
created: 2026-11-08T23:39:00Z
modified: 2026-11-08T23:39:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-2038, 6 coin donations verified live on Quick Construction 7/30 to 1/30, Rallied Attack re-read not reached before the unit cap, partial
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 15:22-15:39 America/Los_Angeles
---

# 1537 queue run - alliance donations (donations-2026-11-08-2038)

- Unit: donations-2026-11-08-2038, executor ticker-1522.
  Status: partial - 6 coin donations verified live on Quick
  Construction, count 7/30 to 1/30; the Rallied Attack re-read
  the unit window asked for was not reached before the 15 minute
  unit cap. Tracker untouched.
- Session: computer session cc-136 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No device-access error,
  no different-device dialog, no login demanded. Nothing bought,
  no diamond button tapped, no speedup used.
- Session window: 15:22-15:39 local, about 17 minutes including
  record writing; game play inside the 15 minute unit cap.

## What was read and done

- Base HUD at entry: food 490.8M, wood 813.3M, iron 25.0M,
  stone 922.2K, coin 12.3M, power 149,850,353, diamonds 4,397,
  gold 13.22K.
- Entry, re-grounded fresh from the full-base screenshot:
  Alliance shield at norm (935, 710) opened the alliance menu
  ([AP3x] The Apex, 95/100 members, Power 13,299,306,666,
  Leader Abyss Apex) at once; Alliance Techs tile at norm
  (673, 679) opened ALLIANCE TECHS at once.
- Development tab: Auto Rally Max Level, Quick Construction
  8/10 carrying the red thumbs-up recommended marker, Great
  Helper Max Level, one 2/10 node below. Footer Tech Donation
  Today 6250 at entry.
- Quick Construction panel, read live at about 15:27: 8/10,
  Increased Building Speed for Allies, Donation Reward +20%,
  Tech EXP Required 1.6M/6.0M, Current +20%, Next Level
  +22.5%, Donation Reward 50 EXP + 50 badge, Donation Count
  7/30, green coin Donate 900, diamond Donate 2 (never tapped).
  Weekly settlement countdown 02:34:09.
- Six coin donations, each verified by a live count re-read:
  7/30 to 6/30 (single tap, screenshot), 6/30 to 4/30 (pair of
  taps, screenshot), 4/30 to 1/30 (three taps, screenshot).
  Total 5,400 coin. The green coin button stayed green after
  every tap, no grey-out timer appeared. Stopped at the
  live-read 1/30 per the standing changed route (2026-11-08
  0920 correction): no tap from 1/30 on Quick Construction.
- Replenishment measurement (observed, not a closing figure):
  QC read 1/30 at 13:37 (unit 1342) and 7/30 at about 15:27,
  +6 over about 110 minutes, about 1 per 18 minutes,
  consistent with the roughly 1-per-20-minutes two-endpoint
  estimate.
- Footer discrepancy (observed only, never a closing figure):
  Tech Donation Today read 6250 at entry and 6900 on the War
  tab after the 6 donations, +650 against +600 expected at
  +100 per donation (1342 measurement). The extra +50 is
  unexplained; the live Donation Counts above are the closing
  figures, not the footer.
- UI note: during the paired taps a tooltip appeared - "Hold
  down for easier Continuous donations" - the button supports
  hold-to-donate; single taps were used and each verified.
- War tab opened: tree reads Unit Load Capacity 2/10 at top,
  Quick Training 1/10 and Expert Trainer 2/10 below, then a
  row of three 5/10 nodes. Rallied Attack sits below that row
  and was not reached before the unit cap; no War-node tap
  was made and no RA count was read in this unit.
- The ALLIANCE TECHS panel was closed to the Alliance menu
  and back to the base. The game was left on the base screen.
- Tooling note: two clicks failed with "The target app exited
  or restarted" (stale_observation) when given an
  observation_id returned by a previous control call; clicks
  need a fresh computer.observe observation_id. The game had
  not exited - a fresh observe showed the same screen both
  times.

## Tracker and follow-up

- Tracker untouched (partial). The Rallied Attack re-read this
  unit's window asked for is still open (Issue #450): the
  1238 unit's final RA tap went behind a 00:18:42 timer at
  12:43, the timer cleared about 13:02, and the count is
  expected 0/30 if that tap landed, 1/30 if it was eaten. The
  next donations unit must read the RA Donation Count live
  first, and if QC has replenished above 1/30, donate on QC
  down to 1/30 again.
- The daily 30/30 target is not met - the count stands at a
  live-read 1/30 on Quick Construction with replenishment
  pending, and no 0/30 read is claimed. QC and RA counts may
  be per-node, not global (QC 7/30 at 15:27 while RA was last
  seen 1/30 at 12:41); the RA live read will settle it.
- Result stats: target 30, achieved 6 this unit (count 7/30
  to 1/30 live), verified yes for the six donations.
