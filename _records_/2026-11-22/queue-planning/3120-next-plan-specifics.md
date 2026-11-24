---
title: Queue Planning Specifics To Apply After Every Plan 3120 2026-11-24
created: 2026-11-24T03:30:00-08:00
modified: 2026-11-24T03:45:00-08:00
level: L0
version: 1.10.0
description: The list of text and retirements the planner applies after each plan run, as it stood on 2026-11-24 - so the next plan does not lose what was learned today
status: done
activity: queue-planning
run_id: queue-planning-2026-11-24-0330-next-plan-specifics
trigger: coordinator message 11:23Z (the daily assist) and the day's changes
started_at: 2026-11-24T03:21:00-08:00
finished_at: 2026-11-24T03:30:00-08:00
verified: written from the units and messages of 2026-11-24; each item names the unit or rule that carries it
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3100-pool-note-1000z-dispatch-cycle.md
  - source: _records_/2026-11-22/queue-planning/3110-trade-cycle.md
---

# Specifics to apply after every plan, 3120

## Retire after each plan

The roster donations unit (the passes carry donations at the confirmed 20 minute refill) and the roster trucks units (the trade cycle units in 3110 replace them; each retirement stamps the current UTC time, never a fixed past time).

## Add to the minted roster units

- Every unit: 'Verify each HUD icon by its label or glyph before the tap.'
- Left-column reads (scout-midday, scout): the tram icon's badge state with the UTC time and the trade count.
- Radar: the dialog ruling (Confirm allowed for the 10 radar rewards text only; any other dialog: stop).
- Mail: Cancel only on the TIPS notifications dialog; never Enable Now.
- Passes: the Weekly Pass page (S1, EXP, Iron and Coin pickups) follows 3130 (up to four composed pans from the top, each card read before any tap, owned plain Claims only, Already claimed today a COMPLETE, est 12); no separate read unit.
- Secrets: the DAILY ASSIST, up to 5 a day (an existing daily stream, not new income): read the counter first, press nothing at 5/5 or 'nothing due', take the five early in the day; one press per UR ally card after reading its text, stopping on anything but a clean free press (picker, price, diamond, item cost, hero or squad line, other dialog), recording the count, the reward and that Squad 1 is unchanged; cards respawn within minutes (a pressed card reappears with a 5-minute timer tile: measured 11:23Z to 11:25Z), so the daily cap, not the card supply, is the limit; the roster unit carries the five, so no dedicated assist unit is needed on a day it finds the counter at 5/5 (a dedicated one serves PL-16).
- Training, research and building-queues: the three-class idle read (empty queue, finished batch or item waiting, blocked by the toast in this read), the ready bubble with its digits, one pistol press per barracks.

## Times and checks

Open no unit exactly on the hour (an owner-side job took the front at 10:00:05Z); on 11-25 keep 11:25Z to 11:40Z free of long units and of donation pass windows, with ONE short read request in it (`scout-midday-cu-gate-test-2026-11-25-001`, 11:28:30Z: the Coach's test CK1: the nightly cu run held the lock 2.4 minutes at 11:28Z on 11-24, one sample; PR gate runs hold it too, unpredictably; without a request the test is unreadable); keep the 08:00Z to 08:25Z window clear of openings and expiries; every serves is a plan item id with a ledger row or upkeep, snapshot or baseline (the refusal is live); use a 5 hour plan horizon (4 hours misses a wave 4 hours and 2 minutes ahead).
