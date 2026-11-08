---
title: Ticker 0434 harvest access-failed
created: 2026-11-01T12:45:00Z
modified: 2026-11-01T12:45:00Z
---

# Ticker 0434 - harvest-2026-11-01-0203, failed (device offline)

Session window: 2026-11-01 about 04:34 to 04:45 local.
Executor: ticker-0434. Unit status: failed. Tracker untouched,
as a failed unit requires, so the next tick re-produces this
regular.

## What was done

- Pass opening: sync reaped 0, expired 0, produced nothing
  new; the 20 due regulars were already queued by the
  planner. No zombie chain seeded: the Zombie Invasion
  event ended at about the 19:00 reset on 2026-10-30 and
  its chain closed at unit 066, per the activity metadata,
  which states explicitly not to seed a new chain until a
  Zombie Invasion tab is seen live in the Events hub again.
- Own PRs first: no open pull request exists for
  zachmesh/lastwar at this pass (gh pr list on the VPS
  returned empty); all previous records PRs for
  2026-11-01, including PRs 48, 49 and 50, are merged
  (PR 50 merged by the integrator at 04:30). No PR owned
  by this job awaited a reply or a conflict fix.
- Token acquired by ticker-0434; no other pass held it.
- Next unit by earliest expiry: harvest-2026-11-01-0203,
  claimed by ticker-0434 until 2026-11-01T12:54:52Z.

## What was not done, and why failed

- Device channel offline: three computer.session starts on
  the Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  each returned node_offline with no wake-up path
  advertised. The device last seen time was
  2026-11-01T09:47:27Z (01:47 local) and did not move
  across the pass. Two attempts on the Mac mini
  connection-recovery channel (connection.health, then
  connection.repair for native) each timed out after
  25 seconds. Three session attempts meet the
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
- This is the fifth consecutive access-failed ticker pass
  (02:34 arms-race, 03:04 donations, 03:34 radar, 04:04
  crystal-shop, now 04:34 harvest, all on the same
  offline channel, last seen 01:47 local and unmoved
  since), so this pass is
  material under the ticker reporting rule: the main agent
  decides whether the owner needs to bring the Mac gateway
  back (the channel recovered only on a local Mac message
  in the 2026-10-29 recurrence).
