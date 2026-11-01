---
title: Ticker 0304 donations access-failed
created: 2026-11-01T11:10:00Z
modified: 2026-11-01T11:10:00Z
---

# Ticker 0304 - donations-2026-11-01-0203, failed (device offline)

Session window: 2026-11-01 about 03:04 to 03:10 local.
Executor: ticker-0304. Unit status: failed. Tracker untouched,
as a failed unit requires, so the next tick re-produces this
regular.

## What was done

- Pass opening: sync reaped 0, expired 0, produced nothing
  new; the 20 due regulars were already queued by the
  planner. No zombie chain seeded: the Zombie Invasion
  event ended at about the 19:00 reset on 2026-10-30 and
  its chain closed at unit 066, per the activity metadata.
- Own PRs first: no open pull request exists for
  zachmesh/lastwar at this pass (gh pr list on the VPS
  returned empty); no PR owned by this job awaited a
  reply or a conflict fix.
- Token acquired by ticker-0304; no other pass held it.
- Next unit by earliest expiry: donations-2026-11-01-0203,
  claimed by ticker-0304 until 2026-11-01T11:25:51Z.

## What was not done, and why failed

- Device channel offline: three computer.session starts on
  the Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  each returned node_offline with no wake-up path
  advertised; a connection.health probe returned the same
  error. The device last seen time was
  2026-11-01T09:47:27Z and did not move across the pass.
  Three session attempts meet the at-least-3-attempts
  rule in the recording rules before this unit is written
  down as access-failed.
- No game input was dispatched in this unit: no screen was
  read, no Donation Count was observed, no donation was
  made, nothing was spent, and no different-device dialog
  was seen. The live donation count for this reset day is
  therefore unknown, not assumed, and is left for the
  next tick. Per the donations hard closing rule, no
  arithmetic closing figure is used.
- No other unit was executed in this pass: with the device
  channel down, the remaining inbox units could not be
  attempted either, and the pass ends here rather than
  burning the pass budget on further offline retries.
- Tracker untouched (failed unit). Nothing claimed.

## Follow-up

- Next tick retries the donations regular as a fresh unit
  and re-checks the device channel; if the channel is
  still offline then, that pass records it the same way.
- This is the second consecutive access-failed ticker pass
  (the 02:34 pass also failed on the same offline channel),
  so this pass is material under the ticker reporting rule:
  the device channel has now been down across two passes
  since its last seen time of 01:47 local, and the channel
  recovered only on a local Mac message in the 2026-10-29
  recurrence.
