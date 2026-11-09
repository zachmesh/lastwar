---
title: Shop claims queue run 1853
created: 2026-11-07T18:53:00-08:00
modified: 2026-11-07T18:53:00-08:00
level: L0
version: 1.0.0
description: Ticker-1834 passes unit, done, 3 claims, Hot Deals free pack, Free Supply auto-claim, monthly daily gift
status: verified
---

# 1853 queue run - Shop Claims

Executor: ticker-1834. Unit: passes-2026-11-07-1457.
Session window about 18:41 to 18:53 America/Los_Angeles.

## Performed

- Mac mini online and the game screen readable on the first
  capture - the first live shop read since the 0841 checked-only
  unit of 2026-11-04. Computer session cc-34. Last War window
  372131, 788x1083 at (114,236), pid 98156, on-screen this time
  (contrast the 1452 unit's off-Space window 160366 at
  (0,-360), Issue 282). No "active on a different device"
  dialog appeared, so no takeover was needed or made.
- Game was on the MY PROFILE panel at entry (leftover state,
  Lv.30 [AP3x]Bears Lair, 149.8M power, VIP13, #2110). Closed
  with the X at [838,43]; base screen read Total Power
  149,850,353.
- Hot Deals: GEAR MASTER PACK on display, Availability 1,
  timer 23:17:59. Free Claim tapped once at [500,754]:
  CONGRATULATIONS paid Upgrade Ore Lucky Chest x1 and Upgrade
  Ore 1.5K. Page then read "Packs sold out". A second panel
  followed at once - "Free rewards have been automatically
  claimed": supply chest x1 and ruby x10 (the new-cycle Free
  Supply auto-claim, firing on shop open after the 18:00
  reset).
- Weekly Pass page, read live and scrolled to the list end:
  the page line reads "Weekly Pass rewards reset at 18:00:00"
  (re-confirmed). Free Supply already auto-claimed. The
  Legendary row reads Take All $19.99 - not tapped, per the
  red lines. S2 Drone Components Weekly Pass, S1 Drone Parts
  Weekly Pass and Coin Weekly Pass each show only Get Now
  $4.99 - all three are unowned offers, none tapped. The list
  ends at the Coin card (three cards total today; no EXP or
  Iron card in the list). No owned weekly pass has a claimable
  pickup this cycle.
- Super Monthly Pass page, read live: Monthly Pass, Squad 4
  Lv.20, Days Left 14, Rewards Left 14. Claim Reward tapped
  once at [370,859]: DAILY GIFT paid gold tickets x2, red
  diamonds 100, stamina 50 x2, iron 200, 5m speedups x60;
  the button then read Claimed. The Monthly Pass Extension
  $24.99 was not tapped. Days Left 14 follows 17 at the 0841
  read on 2026-11-04 - three daily decrements across the
  offline days, no discrepancy.
- Game left on the base screen. No diamonds, money, speedups
  or other resources spent; no Renew, no purchase button, no
  Legendary Claim All tapped.

## Claims

- Gear Master Pack free pack: Upgrade Ore Lucky Chest x1,
  Upgrade Ore 1500.
- Free Supply auto-claim: supply chest x1, ruby x10.
- Monthly Daily Gift: gold tickets 2, red diamonds 100,
  stamina 50 x2, iron 200, 5m speedups x60.

## Other pass steps

- Own PRs checked first: PR 398 (records/2026-11-07, post-1100
  batch) is open, Owner lastwar-pr-integrator. Its newest
  comments are the integrator's 1715 re-check (CLEAN at head
  0048e45a against main cef70a43, awaiting the 19:00 batch)
  - nothing is addressed to this job. Older records PRs 351,
  301 and 256 remain open under the integrator, unchanged.
  No new PR was opened: PR 398 already covers the
  records/2026-11-07 branch.
- Sync: reaped 0, expired 2, due 21, produced none - all 20
  due regulars already queued. Queue stats at 02:40Z:
  inbox 68, claimed 0, done 1101.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep note: the chain units
  zero-sweep-pre-reset-sweep-2026-11-07-001 (not_before
  17:30) and -002 (not_before 18:30) were never claimed
  (attempts 0) and expire at the 19:00 reset; the sweep work
  itself ran as the separate units zero-sweep-2026-11-07-1630
  (expired unexecuted) and -1730 (ticker-1734, partial, 23
  lines walked, 2 fix-ups enqueued). The chain pair is a
  duplicate production path, not a missed sweep - the 1730
  unit is the live sweep of record. No Issue filed; the
  stalled-P1 pair is visible in the stats report for the
  retro's queue-health read.
- The pass stopped after this one unit: the device token
  lease ran to 02:55:34Z, leaving about 2 minutes after the
  unit closed, too short for a second unit. The next tick
  (19:04) picks up the remaining inbox; the two unclaimed
  chain sweep units expire at the reset and are reaped then.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state, and the records/2026-11-07 branch itself
  is checked out in another worktree (pi-0330-1107, stale),
  so this pass's outputs were delivered through a temporary
  worktree at the fetched branch tip (a3e3e35c12), leaving
  both states undisturbed. PR 398 already covers the branch,
  so no new PR was opened.

## Outcome

Done. 3 claims, all shop surfaces checked live against the
new 18:00 cycle. No diamonds, money, speedups or other
spending. No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 1, resources_gained upgrade-ore-lucky-chest 1, upgrade-ore 1500, supply-chest 1, ruby 10, gold-tickets 2, red-diamonds 100, stamina-50 2, iron 200, speedup-5m 60, costs 12 minutes and no stamina or items spent, verified yes, blocker_category none, device_takeovers 0
- Note: the unit file's first completion call omitted the
  resources_gained and costs keys, so it records
  stats_missing [resources_gained, costs]; the tool refuses a
  second complete on a done unit, so the keys stand here in
  the record instead.
