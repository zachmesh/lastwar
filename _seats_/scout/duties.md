---
title: Scout seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - scout

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

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
