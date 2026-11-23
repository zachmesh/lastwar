---
title: Scribe seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - scribe

## Each assignment

1. Read the records being folded and their evidence chain.
2. Update the activity or knowledge instance with a version bump and a
   changelog line; never delete a superseded claim, mark it superseded.
3. Keep the type registry and the index current in the same change.
4. Open or review the pull request; confirm the tree check and the target
   metric statement.
5. Record the run and the merged commit.

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
