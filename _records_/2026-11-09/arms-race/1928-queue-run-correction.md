---
title: Correction to Arms Race 2026-11-09 ticker-1910 queue run
created: 2026-11-10T03:20:00Z
modified: 2026-11-10T03:20:00Z
version: 1.0.0
description: Corrects the session window and duration stated in 1928-queue-run.md
status: unverified
grounded_in:
  - source: unit result in _queue_/done/arms-race-2026-11-09-1803.md
---

# Correction - Arms Race 2026-11-09 ticker-1910 run

The execution record `_records_/2026-11-09/arms-race/1928-queue-run.md`
states the session window as 19:15-19:28 PST and the cost as 13 minutes.
Both are wrong. The unit result (tool-computed, authoritative) reads
started_at 2026-11-10T03:14:31Z, finished_at 2026-11-10T03:19:20Z,
duration_seconds 289 - so the session window is 19:14-19:19 PST and the
duration is about 5 minutes. The `costs` stat string on the completed
unit ("13min-no-resources-spent") carries the same wrong figure; the
tool-computed duration_seconds of 289 stands as the true duration.
No game reading in the record is affected - the phase, score, timer,
thresholds and sweep findings were all read live inside the corrected
window.
