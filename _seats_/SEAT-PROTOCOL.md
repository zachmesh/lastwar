---
title: Seat Protocol
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: The shared rules every seat follows when it is woken
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Seat protocol

Every seat reads this page, its own `INDEX.md`, `duties.md` and `handover.md`
before acting. The repository is the single source of truth; a chat reply is
not a record.

## Read order

1. `AGENTS.md` and `_conventions_/local-conventions/continuous-play-team.md`.
2. `TEAM.yaml` for your seat key and write scope.
3. Your `_seats_/<seat>/` pages.
4. The queue, records or knowledge the assignment names.

## Reply shape

A seat's reply to the coordinator is four lines, in this order:

    STATUS: done | partial | blocked | no-op
    ARTIFACT: <repository path or none>
    MEASUREMENT: <the number the assignment asked for>
    NEXT: <one bounded next action or none>

A reply without an artifact path or a measurement is `partial`, not `done`.

## Rules

- Write only inside your seat's `write_scopes`. A change outside it is a
  proposal to the owning seat, never an edit.
- The operator is the only seat that sends input to the game. Nobody else
  holds the device token or opens a computer-use desktop run.
- Only the coordinator creates schedules. A delegated seat has no schedule of
  its own; the coordinator is the clock.
- Every claim names its evidence. A claim with no fresh observation is
  labelled `unverified` and cannot change a play rule.
- A consequential surface - purchase, send, diplomacy, PvP, premium currency -
  stops the unit as `needs-owner`. The coordinator asks the owner.
- An assignment is bounded by its question, its evidence and its completion
  condition. When the condition is met, stop; do not expand the scope.
- Append-only records are never rewritten. A correction is a new entry.
