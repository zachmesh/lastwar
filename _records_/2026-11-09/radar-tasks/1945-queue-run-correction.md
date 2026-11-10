---
title: Correction to Radar tasks queue run 1945
created: 2026-11-10T03:38:00Z
modified: 2026-11-10T03:38:00Z
version: 1.0.0
description: Corrects the session window and duration stated in 1945-queue-run.md
status: unverified
grounded_in:
  - source: unit result in _queue_/done/radar-2026-11-09-1803.md
---

# Correction - Radar tasks queue run 1945

The execution record `_records_/2026-11-09/radar-tasks/1945-queue-run.md`
states the session window as 19:36-19:45 PT and the cost as about 9
minutes. Both are wrong. The unit result (tool-computed, authoritative)
reads started_at 2026-11-10T03:32:19Z, finished_at 2026-11-10T03:37:25Z,
duration_seconds 306 - so the session window is 19:32-19:37 PST and the
duration is about 5 minutes. The `costs` stat string on the completed
unit ("9min, 0 stamina") carries the same wrong figure; the
tool-computed duration_seconds of 306 stands as the true duration. No
game reading in the record is affected - the radar state, restore line
and pin inventory were all read live inside the corrected window.
