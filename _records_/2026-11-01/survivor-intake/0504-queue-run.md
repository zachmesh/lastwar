---
title: Ticker 0504 survivors access-failed
created: 2026-11-01T13:05:00Z
modified: 2026-11-01T13:05:00Z
---

# Ticker 0504 - survivors-2026-11-01-0203, failed (device offline)

Session window: 2026-11-01 about 05:04 to 05:20 local.
Executor: ticker-0504. Unit status: failed. Tracker untouched,
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
  (including PR 52, the 2026-11-01 records PR, merged
  2026-11-01T13:01:33Z) are merged. Nothing owned by this
  job awaited a reply.
- Token acquired by ticker-0504; no other pass held it.
- Next unit by earliest expiry: survivors-2026-11-01-0203,
  claimed by ticker-0504 until 2026-11-01T13:24:54Z.
- Survivor-intake metadata read before acting, including
  the 2026-10-31 retro standing blocker: 22 of 22 survivor
  units closed partial and Quick Dispatch never ran. This
  unit therefore planned to start at the gate with a fresh
  grounding and verify a survivor figure before any tap,
  per queue rule R2.

## What was not done, and why failed

- Device channel offline: five computer.session starts on
  the Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  each returned node_offline with no wake-up path
  advertised, plus one connection.health probe with the
  same node_offline result. Its last seen time was
  2026-11-01T09:47:27Z (01:47 local) and did not move
  across the pass. Five session attempts exceed the
  at-least-3-attempts rule in the recording rules before
  this unit is written down as access-failed.
- No game input was dispatched in this unit: no screen was
  read, no gate line was verified, no survivor was
  recruited, no Quick Dispatch ran, nothing was claimed,
  nothing was spent, and no different-device dialog was
  seen. The gate line state is therefore unknown, not
  assumed, and is left for the next tick.
- No other unit was executed in this pass: with the device
  channel down, the remaining inbox units could not be
  attempted either, and the pass ends here rather than
  burning the pass budget on further offline retries.
- Tracker untouched (failed unit). Nothing claimed.

## Follow-up

- Next tick retries the survivors regular as a fresh unit
  and re-checks the device channel; if the channel is
  still offline then, that pass records it the same way.
- This is the sixth consecutive access-failed pass after
  the 02:34, 03:04, 03:34, 04:04 and 04:34 passes, per the
  day INDEX and the 04:34 harvest record. The device
  channel has now been down since 01:47 local, about
  three hours and twenty minutes at pass end, with no
  wake-up path advertised. That duration, not a single
  failed tick, is the material fact for the owner: the
  Mac mini control channel needs a local recovery (a
  message sent on the Mac itself cleared the same class
  of lock on 2026-10-27 and 2026-10-29), and no remote
  retry in this pass could substitute for it.
