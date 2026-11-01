---
title: Ticker 0834 harvest access-failed
created: 2026-11-01T16:37:00Z
modified: 2026-11-01T16:37:00Z
---

# Ticker 0834 - harvest-2026-11-01-0603, failed (device offline)

Session window: 2026-11-01 about 08:34 to 08:37 local.
Executor: ticker-0834. Unit status: failed. Tracker untouched,
as a failed unit requires, so the next tick re-produces this
regular.

## What was done

- Pass opening: sync reaped 0, expired 0, produced nothing
  new; the 20 due regulars were already queued by the
  planner. No zombie chain seeded: the Zombie Invasion
  event ended at about the 19:00 reset on 2026-10-30 and
  its chain closed at unit 066, and no Zombie Invasion tab
  is live, so no new chain is seeded until that tab is
  seen live in the Events hub again.
- Own PRs first: no open pull request exists for
  zachmesh/lastwar at this pass (gh pr list on the VPS
  returned empty). No PR owned by this job awaited a
  reply or a conflict fix.
- Token acquired by ticker-0834; no other pass held it.
- Next unit by the queue tool: harvest-2026-11-01-0603,
  claimed by ticker-0834 until 2026-11-01T16:54:59Z.

## What was not done, and why failed

- Device channel offline: three computer.session starts on
  the Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  each returned node_offline with no wake-up path
  advertised, plus a connection.health probe and a
  connection.repair attempt with the same node_offline
  result. The device last seen time was
  2026-11-01T09:47:27Z (01:47 local) and did not move
  across the pass. Three session attempts meet the
  at-least-3-attempts rule in the recording rules before
  this unit is written down as access-failed.
- No game input was dispatched in this unit: no screen was
  read, the base screen was never entered or verified, no
  resource bubble, HUD total or Armed Truck state was
  observed, nothing was collected, nothing was spent, and
  no different-device dialog was seen. The live harvest
  state for this window is therefore unknown, not assumed,
  and is left for the next tick.
- No other unit was executed in this pass: with the device
  channel down, the remaining inbox units could not be
  attempted either, and the pass ends here rather than
  burning the pass budget on further offline retries.
- Tracker untouched (failed unit). Nothing claimed.

## Follow-up

- Next tick retries the harvest regular as a fresh unit
  and re-checks the device channel; if the channel is
  still offline then, that pass records it the same way.
- This is the thirteenth consecutive access-failed ticker
  pass (02:34, 03:04, 03:34, 04:04, 04:34, 05:04, 05:34,
  06:04, 06:34, 07:04, 07:34, 08:04, now 08:34, all on the
  same offline channel, last seen 01:47 local and unmoved
  since), so this pass is material under the ticker
  reporting rule: the main agent decides whether the owner
  needs to bring the Mac gateway back (the channel
  recovered only on a local Mac message in the 2026-10-29
  recurrence).
