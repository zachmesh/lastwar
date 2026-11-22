---
title: Harvest queue run 0534 - failed, game window missing
created: 2026-11-19T14:15:00Z
modified: 2026-11-19T14:15:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-19-0203 failed - LastWar window absent on the Mac mini
status: failed
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/0534-process-failure.md - the full process record for this pass
  - source: tools/queue.py complete --unit harvest-2026-11-19-0203 --status failed, 2026-11-19T14:01:23Z
---

# Harvest 2026-11-19 05:34 PT (ticker-0534) - FAILED

Unit harvest-2026-11-19-0203, claimed 13:55:13Z, completed
failed 14:01:23Z, duration 370 seconds. No game input was
sent and nothing was claimed: the LastWar window is absent
on the Mac mini (the app process runs, com.lastwar.ios, but
exposes no window; two computer sessions, open_app
outcome_unknown twice, activate ax_windows_empty twice,
list_windows 11 windows with no LastWar entry twice,
observe and screen.snap observation_unavailable). Probe
v1.2.0: OFF_SCREEN_WINDOW, high confidence, stop_pass yes.

This is the sixty-second consecutive window-loss occurrence
(the unit summary's "60th" understates by two - it was taken
from the stale ticker-0215 count; the correction is recorded
in the process record, the unit file itself is append-only).
The tracker is untouched; the harvest regular stays due and
the next tick re-produces it. The shared completion marker
suppresses re-picks of this unit.

Full detail - probe evidence, the route deviation (this pass
claimed before probing, against the 0434 honoring order),
duel posture, sync, PRs and delivery - is in
_records_/2026-11-19/queue-ticker/0534-process-failure.md.
