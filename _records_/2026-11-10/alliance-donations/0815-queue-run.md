---
title: Alliance donations queue run 0815
created: 2026-11-10T16:15:00Z
modified: 2026-11-10T16:15:00Z
version: 1.0.0
description: Ticker-0804 donations re-read unit, 1 coin tap dispatched from live 1/30 on Rallied Attack, landing unproven behind the cooldown timer, Tech EXP unchanged
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-10 08:12 to 08:15 local
---

# Alliance donations - ticker-0804 queue run

- Executor: ticker-0804
- Unit: donations-2026-11-10-1600, claimed 08:12:04 local
- Session window: about 08:12 to 08:15 local
- Status: partial, verified no (no live 0/30 count read; tap landing unproven)
- Tracker: untouched

## Entry

- The game was left on the Rallied Attack panel of Alliance Techs by the
  ticker-0734 pass (0747 record). No navigation was needed: the panel was
  already open at entry, Donation Count read live 1/30, Tech EXP
  24.6K/4.5M, coin Donate 800 green and active, diamond Donate 2 never
  used. This unit is the named re-read unit from the 0747 follow-up
  (cooldown 00:07:30, not before 08:08 local).
- The 1/30 read is itself a replenishment data point (Issue #160): the
  0734 unit left this panel at a live-read 1/30 plus one EXP-verified
  tap at about 08:02, and this unit read 1/30 live again at about
  08:14, so the count returned to 1 within about 12 minutes of that
  tap - either the tap's landing plus a fast replenishment, or the
  tap was eaten and the count never left 1/30. The two readings
  cannot distinguish the two; the count half of the deciding test
  stays open.

## Rallied Attack - the 1/30 tap, landing unproven

- The tap was dispatched on the War-tab node (Rallied Attack), not on
  Quick Construction, per the changed route (standing, R2): no tap
  from 1/30 on Quick Construction. The first dispatch attempt failed
  with a stale_observation error (missing observation_id, no input
  sent); the retry with a fresh observation_id dispatched.
- Coin Donate button grounded from the current screenshot at norm
  (657, 794) - the green button centre on this 642x951 window.
  The tap greyed the button with a 00:11:08 cooldown timer (00:11:01
  on the closing screenshot), hiding the count label.
- Landing check by the 2026-11-02 0259 EXP-delta rule: Tech EXP still
  reads 24.6K/4.5M after the tap. A landed donation adds 100 EXP,
  which moved this same panel 24.5K to 24.6K on the 0734 tap, so a
  landed tap here should read 24.7K. It does not. The tap most
  likely did NOT land - the same grey-plus-timer, no-landing shape
  the 2018 unit proved by waiting out its timer. The coin HUD
  (84.1M) is too coarse to show an 800-coin step and proves nothing.
- Per the hard closing rule this unit claims no closing count: status
  partial, verified no, tracker untouched. Same close shape as the
  0747 unit.

## Totals

- Coin donations verified: 0. One coin tap dispatched, landing
  unproven (EXP unchanged at 24.6K).
- No diamonds spent, no diamond button tapped.
- Cooldown timer at close: 00:11:01, expiring about 08:26 local.
- Follow-up: a named re-read unit is enqueued for after the cooldown
  (not before 08:28 local). The next unit re-reads the Donation Count
  live first; a live 0/30 read closes the burst, a replenished count
  above zero means donate again. The next unit also re-reads the
  recommended marker fresh (last observed on Troop Movement by the
  0747 unit; not re-read in this unit, which worked the already-open
  Rallied Attack panel).
