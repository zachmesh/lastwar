---
title: Queue Planning Specifics To Apply After Every Plan 3120 2026-11-24
created: 2026-11-24T03:30:00-08:00
modified: 2026-11-24T03:45:00-08:00
level: L0
version: 1.28.0
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

The roster donations units (the passes carry donations) and the roster trucks units (3110 replaces them); stamp each with the UTC time.

## Add to the minted roster units

- EVERY minted unit carries Steer A's standing line 'May open another app: ... STOP and touch nothing.' (the template has it): after copying planner blocks, CHECK every unit for it.
- Every unit: verify each HUD icon by its label or glyph before the tap; at the start, if `lsappinfo front` is not LastWar: record, run the standing front script, record again; still not: stop, release, tell the Coordinator (tight units: dispatch text). A unit that computes a cost RE-READS coin, food, iron and oil in a fresh frame first; one that STARTS a build or research writes the speed factor (original over effective time).
- Every roster unit (secrets, train, survivors, treasures, duel-score): close by 3170: DONE for a taken claim or a verified nothing-to-do state with a `state_read:` line (what was read | frame | HH:MM:SSZ); complete with --state-change yes|no. Duel-score: daily total only. Train: the Station Platform pan (a lit badge opens Intercity Trade: back arrow).
- Left-column reads: the tram icon state (absent, bare, badge N) with the UTC time.
- DOT FIRST, one class per plan cycle (Steer A 18:35Z; the tram dot proved stale): write the unit's dot, WORLD then BASE, read the dot once. 18Z: survivors (in); 22Z: mail; 02Z: train (Steer A 18:45Z; gifts, help, treasures: no evidence).
- Survivors: read the gate and quote it in the state_read line; never tap the ambient walking figure with the '?' bubble at (145,649) (not recruitable); DONE by rule (b)
- Radar: Confirm only the 10 radar rewards dialog.
- Mail: TIPS Cancel only. The 'Train arrival reward!' mail: read its attachments, tap THAT mail's Claim once (never Claim All), chests unopened.
- Arms race: the finished phase's chest and each claimable milestone's plain free Claim, once.
- Passes: the Weekly Pass page follows 3130 (five pans, plain Claims only, est 12).
- Secrets: the Others' Tasks UR card's PLUNDER button is PvP, NEVER pressed. DAILY ASSIST, up to 5: read the counter first, nothing at 5/5, one press per UR card after reading it, stop on a picker, price, diamond, item cost, hero or squad line. BOX COUNT TEST (Steer A): read the Special tab's purple and gold (Violet's Loot) chest count tags once per run and after a box-paying claim (no tile, no Use).
- Training, research, building-queues: classify a barracks by the press (Train Units panel = empty; toast 'Drill Ground Full' = finished batch waiting), digits cropped at 6x, one pistol press per barracks. Building-queues also writes every builder's end and the Drill Grounds' ends.

## Times and checks

See `3125-plan-times-and-checks.md` (the calm windows, the quiet windows, no opening on the hour, the forecast rule, the 5-hour horizon): read it with this note after every plan.
