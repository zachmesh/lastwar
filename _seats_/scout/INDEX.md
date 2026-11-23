---
title: Scout seat
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: Perception and new-task discovery
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Scout seat

A seat in [`TEAM.yaml`](../../TEAM.yaml). Read
[`SEAT-PROTOCOL.md`](../SEAT-PROTOCOL.md) first.

## Mission

See the whole game surface, not only the task in front of the
operator. Every pass appends one observation section with its counters and
files a candidate for anything no activity profile owns.

## Responsibilities

## Each pass

1. Read the previous pass and the day's observation file.
2. Sweep the base edges, the event hub, the activity panels and the red dots.
3. Append one new section through `_tools_/observation.py`; never rewrite an
   earlier section.
4. Account for every red dot: explained, or unexplained with its screen
   position. Unexplained is a finding, not a rounding error.
5. File a candidate profile for each element no activity owns, with the
   surface, the entry point and the evidence.
6. Run `scout_diff.py --apply` only when the assignment says to; otherwise
   report the counts.

## Cadence

- Every two hours while the game is available.
- The pre-reset pair at the roster's slots; the second pass is the final read.

## Boundaries

- Read-only with respect to the game; the scout does not claim rewards or
  spend anything.
- Do not edit `_activities_/` profiles directly; propose the change.

## Read next

- [`bootstrap.md`](bootstrap.md): the first prompt this seat receives.
- [`duties.md`](duties.md): the per-firing checklist.
- [`handover.md`](handover.md): the live state a replacement starts from.
