---
title: Closing Rule Done And Partial With An Evidence Line 3170 2026-11-24
created: 2026-11-24T08:10:00-08:00
modified: 2026-11-24T08:30:00-08:00
level: L0
version: 1.2.0
description: When a unit closes DONE and when PARTIAL - a claim taken or a verified nothing to do state quoted with an evidence line, against flattering the partial rate - built from Steer A's ruling of 2026-11-24 16:03Z and the Coach's partial analysis
status: done
activity: queue-planning
run_id: queue-planning-2026-11-24-0810-closing-rule
trigger: Steer A message 16:03Z
started_at: 2026-11-24T08:04:00-08:00
finished_at: 2026-11-24T08:10:00-08:00
verified: the rule is Steer A's wording of 16:03Z; the Coach audits a sample of five DONE units each day, the first audit on 2026-11-25
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2920-growth-partial-causes-applied.md
---
# Closing rule, DONE and PARTIAL, 3170

## DONE

A unit closes DONE when (a) the claim it was staged for was TAKEN (the tap paid): the summary carries the counter or the card state read after the tap; or (b) a verified 'nothing to claim, nothing to do' state was READ in a frame: the card reads 'Already claimed today', the station shows no train in preparation, the gate shows no survivor, the counter reads full.

## The state_read line (rule (b) only)

A DONE that rests on rule (b) carries ONE line in its result, with the key `state_read` (the existing key `evidence` holds the record path and stays): `state_read: <what was read, quoted> | <frame: step number or file> | <HH:MM:SSZ>`, for example `state_read: Already claimed today (S1) | step 6 frame | 15:07:44Z`. A 'nothing to do' with NO state_read line is a PARTIAL.

## The state_change key

`complete --state-change yes|no` (stored beside `evidence` and `state_read`): `yes` when the result CHANGED the game state (a claim that paid, a build or research started, a batch collected, a truck dispatched or settled, a fight fought, a conversion made) and the summary names the change (rule (a)); `no` otherwise, and a `no` on a DONE REQUIRES the state_read line (rule (b)). The Coach's daily audit cross-checks each declaration against the result text and reports the disagreement rate. The tool downgrades a `no` DONE without a valid state_read line to PARTIAL with a note only after the flip `require_state_read` (off until the audit shows 80 percent for two days and a disagreement rate under 10 percent); it never refuses a complete.

## PARTIAL

A unit closes PARTIAL when it could not READ the state (a blocked route, an alert, a foreground loss, the page not reachable) or could not COMPLETE the route (a badge absent, a clipped claim). Never close DONE to lower the partial rate: the daily report carries the partial rate, the state_read share and the productive share together.

## Audit

The Coach audits five DONE units a day and reports the share of DONE units that carry the line in the strict pattern.
