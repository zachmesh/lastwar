---
title: Alliance donations 2026-11-10 0129 queue run
created: 2026-11-10T09:29:00Z
modified: 2026-11-10T09:29:00Z
version: 1.0.0
description: Alliance-donations unit donations-2026-11-10-0820 executed by ticker-0104
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 about 01:18 to 01:29 PT
---

# Alliance donations 2026-11-10 0129 queue run

- Executor: ticker-0104. Unit: donations-2026-11-10-0820 (re-read after cooldown, unit donations-2026-11-09-2203).
- Session: computer session cc-372 on Zhen's Mac mini (cc-371 dropped between units; new session started, no game state lost). No different-device dialog, no login or verification demanded, no password or Touch ID step used.
- Status: partial. Closing count read live (1/30 on two nodes). Tracker untouched; re-read unit enqueued for after replenishment.

## What was done

- Entry: Alliance shield fresh-ground at (931,717) opened the Alliance menu on the first try; Alliance Techs tile at (686,683) opened on the first try. One stale-observation failure on the Quick Construction tap (target process identity unavailable) - window re-selected, panel re-read, tap landed.
- Quick Construction (Development tab) 8/10, "Increased Building Speed for Allies", Tech EXP 2.5M/6.0M, Current +20%, Next Level +22.5%, Donation Reward +20%, 50 EXP + 50 badge per donation, coin cost 900.
- Donation Count, every figure read live in this unit: 3/30 at entry, then 2/30 after tap 1, then 1/30 after tap 2. Two coin donations landed, 1,800 coin spent. Hero EXP on the HUD read 376.1K, 376.2K, 376.3K across the three reads (observed only).
- The 0004 unit's 3 unconfirmed taps: this unit's entry read was 3/30, about 54 minutes after that unit's 00:08:18 cooldown timer. The count did not show a 0/30 state; the 3 taps are treated as unconfirmed (most likely eaten). Strictly, replenishment confounds a proof - 3/30 could also be 0 plus about 3 replenished counts - so the conclusion is pattern-level, not per-tap proof.
- Changed route applied (R2, standing): stopped at the live-read 1/30 on Quick Construction - no tap from 1/30. Switched to the War-tab node Rallied Attack.
- Tree scroll direction corrected: two downward drags produced no change (method retired per R2); an upward drag scrolled the tree and revealed World Interception, Rapid Siege, Quick Garrison (5/10 row), Troop Movement 5/10, the Rallied row 7/10 and Expert Nurse 1/10. The Rallied row sits BELOW the first War-tab view, not above it; the 0547 unit's "scroll up" note is superseded for this framing.
- Rallied Attack 7/10, "Increased Hero Attack in Rallies for Allies", Tech EXP 24.5K/4.5M, Current +7%, Next Level +8%, 50 EXP + 50 badge per donation, coin cost 800. The recommended red-panda badge was seen on its tile. Donation Count read live 1/30 - the same as Quick Construction within minutes. No tap from 1/30 (a War-tab 1/30 tap landing is still unverified per the 1238 unit).
- Per-node count question (Issues #160, #450): this unit's paired live reads (both nodes 1/30 within minutes) support a shared/global remaining count, against the 2350 unit's split read (Rallied Attack 9/30 while Quick Construction read 1/30 four minutes earlier). Not resolved - noted for the retro, not concluded.
- Footer, observed only: Tech Donation Today 4150 at entry, 4300 after the 2 donations (+150). Disqualified as a closing count per retro action A-2026-11-09-03 (Issue #417); the unit closes on the Donation Count read only.

## Result stats

- target: donation count re-read after cooldown
- achieved: 2 coin donations landed live
- resources_gained: 2 coin donations (1800 coin spent), Tech EXP +100, badge +100
- costs: about 11 minutes, no items spent, no diamonds spent
- verified: yes (closing 1/30 is a same-unit live read on two nodes)
- blocker_category: e (repeated blocker - the 1/30 state with no proven landing method)

## Follow-up

- Re-read unit enqueued: donations, not-before 2026-11-10T10:00:00Z (02:00 PST), window "donation count re-read after replenishment (unit donations-2026-11-10-0820)". The next tick re-produces the regular from the tracker in any case.

## Red lines

- No diamonds or money spent, no speedup used, no stamina item opened. The diamond Donate button (2 diamonds) was never tapped. No building or research started.
