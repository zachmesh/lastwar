---
title: Ticker 0534 training access-failed
created: 2026-11-01T13:36:00Z
modified: 2026-11-01T13:36:00Z
---

# Ticker 0534 - training-2026-11-01-0203, failed (device offline)

Session window: 2026-11-01 about 05:34 to 05:36 local.
Executor: ticker-0534. Unit status: failed. Tracker untouched,
as a failed unit requires, so the next tick re-produces this
regular.

## What was done

- Pass opening: sync reaped 0, expired 0, produced nothing
  new; the due regulars were already queued. No zombie
  chain seeded: the Zombie Invasion event ended at about
  the 19:00 reset on 2026-10-30 and its chain closed at
  unit 066, per the activity metadata, which states
  explicitly not to seed a new chain.
- Own PRs first: no open pull request exists for
  zachmesh/lastwar at this pass; the previous records PRs
  are merged. Nothing owned by this job awaited a reply.
- Token acquired by ticker-0534; no other pass held it.
- Next unit by earliest expiry: training-2026-11-01-0203,
  claimed by ticker-0534 until 2026-11-01T13:54:38Z.
- Troop-training metadata read before acting, including
  the 2026-10-31 retro standing blocker: 21 of 22 training
  units closed non-done, with Drill Ground Full
  (39,460 of 39,460) blocking collection and requeue in
  every 2026-10-31 unit that reached a barracks. This unit
  therefore planned to read the Drill Ground screen live
  first and record what controls it actually shows, per
  queue rule R2, instead of closing as a bare blocked read.

## What was not done, and why failed

- Device channel offline: four computer.session starts on
  the Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  each returned node_offline with no wake-up path
  advertised, plus one connection.health probe with the
  same node_offline result, plus two recovery-channel
  attempts on the Mac mini connection recovery device
  (connection.repair native, then connection.health) that
  each timed out after 25 seconds. Its last seen time was
  2026-11-01T09:47:27Z (01:47 local) and did not move
  across the pass. Four session attempts exceed the
  at-least-3-attempts rule in the recording rules before
  this unit is written down as access-failed.
- No game input was dispatched in this unit: no screen was
  read, no barracks was opened, no Drill Ground figure was
  verified, no batch was queued, nothing was claimed,
  nothing was spent, and no different-device dialog was
  seen. The barracks and Drill Ground state are therefore
  unknown, not assumed, and are left for the next tick.
- No other unit was executed in this pass: with the device
  channel down, the remaining inbox units could not be
  attempted either, and the pass ends here rather than
  burning the pass budget on further offline retries.
- Tracker untouched (failed unit). Nothing claimed.

## Follow-up

- Next tick retries the training regular as a fresh unit
  and re-checks the device channel; if the channel is
  still offline then, that pass records it the same way.
- This is the seventh consecutive access-failed pass after
  the 02:34, 03:04, 03:34, 04:04, 04:34 and 05:04 passes,
  per the day INDEX and the 05:04 survivors record. The
  device channel has now been down since 01:47 local,
  about three hours and fifty minutes at pass end, with
  no wake-up path advertised. That duration, not a single
  failed tick, is the material fact for the owner: the
  Mac mini control channel needs a local recovery (a
  message sent on the Mac itself cleared the same class
  of lock on 2026-10-27 and 2026-10-29), and no remote
  retry in this pass could substitute for it.
