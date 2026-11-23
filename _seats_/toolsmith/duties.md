---
title: Toolsmith seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - toolsmith

## Each assignment

1. Read the improvement entry, its target metric and its verification method.
2. Check the held patches register before re-implementing anything.
3. Implement with a test; run the test and record the command and result.
4. Name the before and after windows for the target metric.
5. Open a pull request with the improvement id, target metric, validation and
   file list; record the run.

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
