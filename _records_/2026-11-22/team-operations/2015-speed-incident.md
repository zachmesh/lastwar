---
title: Speed incident - 2026-11-22 20:15 PT
created: 2026-11-22T20:15:00-08:00
modified: 2026-11-22T20:15:00-08:00
level: L3
version: 0.1.0
description: The first coordinator-session tick took 11 minutes to dispatch a unit whose run was active 52 seconds, and the run paused on the owner's local input; owner rule change for tick speed
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2015-speed-incident
trigger: owner feedback relayed by the Steward 2026-11-23T04:15Z - the play looks extremely slow
started_at: 2026-11-22T20:15:00-08:00
finished_at: 2026-11-22T20:17:00-08:00
duration_seconds: 120
verified: dispatch window measured from this session's own timestamps (instruction 20:02 PT, spawn with assignment 20:12:26 PT); run active time 52 s and the local-input pause as reported by the owner via the Steward
---

# Speed incident - 2026-11-22 20:15 PT

## What happened

| Measure | Value | Source |
|---|---|---|
| Dispatch latency | 11 min, 20:02 to 20:13 PT | take-over at 20:02, assignment delivered by spawn at 20:12:26 PT (`2011-tick.md`) |
| Run active time | about 52 s | owner measurement via the Steward |
| Latency to work ratio | about 12.7 to 1 | 660 s / 52 s |
| Run outcome | paused - the owner's Screen Sharing mouse movement counted as local input | owner via the Steward |
| Unit close | `donations-2026-11-22-1803` closed `partial` by the operator | Steward; operator record to follow |

## Cause

1. **Selection analysis.** The tick re-read history and compared candidates
   (harvest windows, retry semantics, `claim` internals, relay internals)
   and asked the owner a two-part question, instead of dispatching the unit
   `queue.py next` named. The eligible unit was known at 20:11 PT; the first
   `next` call could have been at about 20:06 PT.
2. **Delivery route.** Two refused delivery attempts to the child operator
   before the spawn. The spawn itself was necessary; the probing was not
   timeboxed.
3. **Local-input pause.** The computer-use run pauses on local input. A
   Screen Sharing mouse move is local input on this Mac.

## Rule change (owner, 2026-11-23T04:15Z)

Standing rules for every coordinator tick, written into
`_seats_/coordinator/duties.md` and the loop schedule prompt:

1. Timebox selection to 60 seconds: `queue.py next`, eligibility check and
   dispatch in the same turn. After `next` names an eligible unit, do not
   re-read history, read old ticker records or compare candidates.
2. One unit, one run, one reply. If the operator is already playing, do not
   dispatch a second.
3. Routine play runs use `--model claude-gateway/claude-sonnet-5-5` and
   `--max-steps 8`; the slower opus model is reserved for complex screens.
4. A run paused by local input is stopped and its unit closed `partial`
   within 2 minutes; never wait longer.
5. Target: one routine unit per 2 to 3 minutes while the Mac is idle.

## Stats

- dispatch latency: 660 s (target 60 s)
- run active: about 52 s
- units dispatched: 1, closed partial
- improvement filed: `IMP-20261123-01`

## Follow-up

- Next tick applies the rules: `next`, check, dispatch, under 60 s.
- Watching the live view is passive; mouse movement in Screen Sharing pauses
  the run (owner awareness item, not a tool change).
