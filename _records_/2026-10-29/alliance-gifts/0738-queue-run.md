---
title: Alliance gifts queue run
created: 2026-10-29T14:38:00Z
modified: 2026-10-29T14:38:00Z
version: 1.0.0
description: Ticker pass ticker-0734 gifts unit failed on the Mac control channel outcome_unknown lock
status: unverified
grounded_in:
  - source: device tool results in this pass
---

# 07:34 to about 07:38 — Alliance gifts queue unit, failed (control channel lock)

- Ticker pass ticker-0734, unit gifts-2026-10-29-0630
  (alliance-gifts, planned slot 06:30).
- Queue sync at 07:34 reaped 0 and produced 0; the 14 due
  regulars were already queued. The token was taken by
  ticker-0734 and the gifts unit was picked first.
- Device state at pick time: the Mac mini device channel
  showed offline, last seen 2026-10-29T14:07:36Z. Two
  computer.session start attempts returned node_offline
  with no wake-up path. After about 2 minutes the third
  attempt succeeded (session cc-249) and the device
  showed online again, last seen 2026-10-29T14:36:56Z.
  LastWar (com.lastwar.ios) was already running with its
  642x951 window present.
- The control channel then refused every window-selection
  input with outcome_unknown, retryable false, "a new
  local user submission is required before input can
  resume": activate failed on cc-249, activate failed
  again on fresh session cc-250, open_app failed on
  fresh session cc-251. Read-only queries still worked
  (list_apps, frontmost_app, observe), and observe
  confirmed the LastWar window as target but reported
  "control was stopped or its authorization changed".
- This is the same outcome_unknown lock pattern seen
  2026-10-26 to 2026-10-27, which only cleared when the
  owner sent a message locally on the Mac mini. No game
  input was delivered in this pass, so no gift was
  claimed, nothing was spent, and no dialog state could
  be verified. The "active on a different device"
  dialog was never observed.
- Unit completed as failed. The tracker was left
  untouched for a failed unit, so the gifts regular
  stays due and the next tick re-produces it. The
  previous pass (ticker-0704) also ended in an access
  failure, so this pass is reported, not silent.
