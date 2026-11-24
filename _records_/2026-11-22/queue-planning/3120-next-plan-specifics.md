---
title: Queue Planning Specifics To Apply After Every Plan 3120 2026-11-24
created: 2026-11-24T03:30:00-08:00
modified: 2026-11-24T03:45:00-08:00
level: L0
version: 1.16.0
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

The roster donations unit (the passes carry donations at the 20 minute refill) and the roster trucks units (the trade cycles of 3110 replace them); each retirement stamps the current UTC time.

## Add to the minted roster units

- Every unit: 'Verify each HUD icon by its label or glyph before the tap.'
- Every roster unit (secrets, train, survivors, treasures, duel-score above all): close by 3170: DONE for a taken claim or a verified nothing-to-do state with a `state_read:` line (what was read | frame | HH:MM:SSZ). Duel-score reads only the personal daily total (no weekly score, no roulette). The train read uses the Station Platform pan (a lit badge opens Intercity Trade: back arrow, touch nothing).
- Left-column reads (scout-midday, scout): the tram badge and its count with the UTC time.
- Radar: Confirm allowed for the 10 radar rewards dialog text only; any other dialog: stop.
- Mail: Cancel only on the TIPS notifications dialog. The 'Train arrival reward!' Event mail: read its attachments, tap THAT mail's Claim once (never Claim All), 50-count chests unopened.
- Arms race: claim the finished phase's chest and each claimable milestone's plain free Claim once; points from free actions only.
- Passes: the Weekly Pass page follows 3130 (up to five composed pans from the top, each card read before any tap, owned plain Claims only, Already claimed today a COMPLETE, est 12).
- Secrets: the Others' Tasks UR card's PLUNDER button is PvP, NEVER pressed. DAILY ASSIST, up to 5: read the counter first, nothing at 5/5, one press per UR card after reading it, stop on a picker, price, diamond, item cost, hero or squad line or other dialog; record the count, reward and Squad 1 unchanged; no dedicated assist unit unless the counter is under 5/5 (then PL-16).
- Training, research, building-queues: classify a barracks by the press (Train Units panel = empty queue; the toast 'Drill Ground Full' = finished batch waiting), crop digits from the SAVED frame at 6x, one pistol press per barracks.

## Times and checks

Open no unit exactly on the hour. CALM WINDOWS (CUHelper Screen Recording re-approval about every 6 h 31 min: 15:36Z, about 22:07Z, 04:38Z on 11-25, about 11:09Z [G]): no unit opens or expires in 22:00Z to 22:15Z and 04:30Z to 04:45Z (the 22Z plan opens the 22:03Z wave at 22:16Z; the 02Z plan opens the 04:30Z group at 04:46Z). On 11-25 keep 11:25Z to 11:40Z free of long units and donation pass windows, with ONE short read in it (`scout-midday-cu-gate-test-2026-11-25-001`, 11:28:30Z). Keep 08:00Z to 08:25Z clear of openings and expiries. Every serves is a plan item id with a ledger row or upkeep, snapshot or baseline. Use a 5 hour plan horizon.
