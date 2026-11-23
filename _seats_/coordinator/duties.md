---
title: Coordinator seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T04:16:00Z
level: L2
version: 0.2.0
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
6. Chaining (coordinator reading of rule 5): the 900-second clock alone
   allows only 4 units an hour, so when an operator reply closes a unit, the
   coordinator runs `next` and dispatches the next eligible unit in that same
   turn. The clock is the backstop for a lost reply, not the pace.

Source: `_records_/2026-11-22/team-operations/2015-speed-incident.md`,
improvement `IMP-20261123-01`.

## Each tick

1. Read the newest queue ticker record, the queue state and the coach's latest
   dashboard.
2. Pick the one next act: a play unit for the operator, a perception pass for
   the scout, a research question for the researcher, a queue repair for the
   planner, or a measurement for the coach.
3. Send one bounded assignment with a question, the expected evidence and a
   completion condition.
4. Collect the reply, check the artifact exists, and record the tick in
   `_records_/<date>/team-operations/`.
5. If the evidence shows a defect, file or update one improvement entry with a
   target metric. Do not file duplicates.

## Daily

- Review one seat against its duties and record the verdict in
  `_seats_/coordinator/member-review.md`.
- Reconcile `TEAM.yaml` with the actual DSH sessions.
- Ask the owner only for decisions that are genuinely owner-only.

## The project board (owner, 2026-11-22)

The team's GitHub Project is <https://github.com/users/dtadpole/projects/11>
(see `team-organization.md` section 13). This seat owns it. It cannot be linked
to the repository, so nothing feeds it automatically.

- **Each daily pass:** add repository issues that are missing from the board
  (`addProjectV2ItemById` is idempotent), set Status, and keep the Agent field's
  options equal to the seats in `TEAM.yaml`. Use small batches (8 or fewer) and
  confirm by reading the board back; a large batch can lose its responses.
- **Triage until done:** parent every open issue to an Epic (#861 to #865,
  `Maintenance` if none fits), set its Agent, and set Priority. Work in slices
  of at most 20 issues per pass so the tick stays short; delegate slices to the
  coach. Target: every open issue has an Epic and an Agent within three days.
- **Move cards as work happens:** one `In progress` card per seat; a closed
  issue is `Done`, or `Sunset` when closed as not planned.
- **Run the board check** (`_tools_/board_check.py`, once the toolsmith lands
  it) every pass and fix drift the same day.

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
