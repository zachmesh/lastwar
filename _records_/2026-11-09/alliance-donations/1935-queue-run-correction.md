---
title: Correction to Alliance Donations 2026-11-09 ticker-1910 queue run
created: 2026-11-10T03:31:00Z
modified: 2026-11-10T03:31:00Z
version: 1.0.0
description: Corrects the session window stated in 1935-queue-run.md
status: unverified
grounded_in:
  - source: unit result in _queue_/done/donations-2026-11-09-1803.md
---

# Correction - Alliance Donations 2026-11-09 ticker-1910 run

The execution record `_records_/2026-11-09/alliance-donations/1935-queue-run.md`
states the session window as 19:21-19:35 PST. The unit result
(tool-computed, authoritative) reads started_at 2026-11-10T03:21:18Z,
finished_at 2026-11-10T03:30:27Z, duration_seconds 549 - so the session
window is 19:21-19:30 PST and the duration is about 9 minutes. No game
reading in the record is affected - the count reads, the timer, the
footer and the Tech EXP figures were all read live inside the corrected
window.
