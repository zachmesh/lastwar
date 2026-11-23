---
title: Evaluation metrics
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 1
description: Owner direction, 2026-10-31 - the system that plays the account must be able to measure its
---

# Evaluation metrics

Owner direction, 2026-10-31 - the system that plays the account
must be able to measure its own progress, not only the account's.
Section 14 of the [task unit queue design](task-unit-queue-design.md)
measures the work - what each unit reached. This specification
measures the system that does the work - whether execution is
getting faster and richer per task type, whether perception sees
everything and recognises what it has never seen, whether the
retro proposes improvements that actually close and stay closed,
and how much the tool developer and the knowledge organiser each
improve the step or the system they touch.

Three standing rules govern every metric below.

- **A metric names its source.** Every figure is computed from a
  named repository file and field. A figure that cannot be
  computed from repository data is emitted as a data-gap entry
  with its reason - never estimated, never silently dropped.
- **Association is not causation.** Before-and-after comparisons
  around a tool landing or a profile fix are reported as
  associated movement, with the confounders named. The game
  changes, the duel posture changes, the owner plays by hand;
  none of that is the system's doing, in either direction.
- **Thresholds are alarms, not targets.** A threshold breach is
  named so a human-grade judgement can look at it. Optimising a
  metric against its own threshold (closing improvements
  cheaply, splitting units to flatter durations) is a defect the
  retro itself must call out when it sees it.

Cadence shorthand - **daily** means the daily retro computes it
for its rolling 7 day window and the day just ended; **weekly**
means the first retro of a week additionally compares the window
against the previous week's, from the dated data files, which
are the immutable series these trends read.

