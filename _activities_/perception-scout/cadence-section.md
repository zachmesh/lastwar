---
title: Cadence
created: 2026-11-23T06:53:15Z
modified: 2026-11-23T06:53:15Z
version: 0.1.0
sequence: 4
description: Two passes per reset day, both regulars in _tools_/regulars.json -
---
## Cadence

Two passes per reset day, both regulars in _tools_/regulars.json -

- `scout` - the post-reset full pass, daily-reset cadence
  anchored at the trade-day reset (02:00 UTC absolute
  boundary, about 18:00 PST now, 19:00 PDT before the
  DST end). Correction, 2026-11-03 2032: the standing
  19:00 local anchor is superseded - the 1846 live
  counters, the PR 243 duel-boundary fix and the PR 249
  daily-reset tool fix (regulars.py gated daily-reset
  regulars on a fixed 19:00 local wall time; now
  reset_utc 02:00) settle the boundary, and the tool's
  old fixed-19:00 gating is the cause of the stale
  anchor. Filed as Issue #247; this correction is the
  knowledge-page half of that issue, closure belongs
  to the daily retro.
- `scout-midday` - the midday full pass, daily-reset cadence
  anchored at 07:00 local, for state-dependent availability the
  morning cannot show.

Each pass is a homogeneous chain of scout units split by surface
group - the staged unit is the chain head, the executor extends
the chain under the queue chain rules.

