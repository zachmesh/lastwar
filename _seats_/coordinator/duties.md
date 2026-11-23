---
title: Coordinator seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - coordinator

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

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
