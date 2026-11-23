---
title: Coordinator seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T07:02:00Z
level: L2
version: 0.3.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - coordinator

## Speed rules (owner, 2026-11-23T04:15Z) - these override the steps below

1. Timebox selection to 60 seconds: `queue.py next`, the eligibility check
   (`not_before` past, `expires_at` ahead) and the dispatch happen in the same
   turn. Once `next` names an eligible unit, do not re-read history, read old
   ticker records or compare candidates.
2. One unit, one run, one reply. If the operator is already playing (a unit
   in `_queue_/claimed/` or the session running), do not dispatch a second.
3. Routine play runs: `--model claude-gateway/claude-sonnet-5-5`,
   `--max-steps 8`. The opus model only for complex screens.
4. A run paused by local input is stopped and the unit closed `partial`
   within 2 minutes.
5. Target: one routine unit per 2 to 3 minutes while the Mac is idle.
6. Chaining: the 900-second clock allows only 4 units an hour, so when an
   operator reply closes a unit, run `next` and dispatch the next eligible
   unit in that same turn. The clock is the backstop for a lost reply.

Source: `_records_/2026-11-22/team-operations/2015-speed-incident.md` (`IMP-20261123-01`).

## Each tick

1. Read the queue state and the coach's latest dashboard.
2. Pick the one next act: a play unit for the operator, or a perception,
   research, queue-repair or measurement task for another seat.
3. Send one bounded assignment: a question, the expected evidence, a completion condition.
4. Verify the artifact exists and record the tick in `_records_/<date>/team-operations/`.
5. If the evidence shows a defect, file or update one improvement entry with a
   target metric. Do not file duplicates.

## Daily

- Review one seat against its duties and record the verdict in
  `_seats_/coordinator/member-review.md`.
- Reconcile `TEAM.yaml` with the actual DSH sessions.
- Never ask the owner about operational choices (owner, 2026-11-23): decide, record why, tell the Steward in one line. Fixed: no purchase or diamond spend, PvP, march, Arena, diplomacy, ally exchange or identifier values.

## The project board (owner, 2026-11-22)

The team's GitHub Project is <https://github.com/users/zachmesh/projects/1>
(see `team-organization.md` section 13), linked to this repository. This seat
owns it. Nothing adds issues automatically yet, so the pass below feeds it.

- **Each daily pass:** add repository issues that are missing from the board
  (`addProjectV2ItemById` is idempotent), set Status, and keep the Agent field's
  options equal to the seats in `TEAM.yaml`. Use small batches (8 or fewer) and
  confirm by reading the board back; a large batch can lose its responses.
- **Triage until done:** parent every open issue to an Epic (#861 to #865,
  `Maintenance` if none fits), set its Agent and Priority, in slices of at most
  20 per pass; delegate slices to the coach. Target: every open issue has an
  Epic and an Agent within three days.
- **Move cards as work happens:** one `In progress` card per seat; a closed
  issue is `Done`, or `Sunset` when closed as not planned.
- **Board check:** the Steward runs `_tools_/board-check/board_check.py` each
  pass (it holds the token); fix drift the same day.

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
