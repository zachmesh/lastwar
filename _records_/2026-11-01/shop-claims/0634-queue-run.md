---
title: Queue Run 0634 Shop Claims Access Failed
created: 2026-11-01T14:35:00Z
modified: 2026-11-01T14:35:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-0634 shop-claims unit failed on device access
status: unverified
grounded_in:
  - source: device control channel responses during this pass
---

# 0634 queue run - shop-claims, access failed

Session window: 2026-11-01 about 06:34 to 06:40 America/Los_Angeles.
Executor: ticker-0634. Unit: passes-2026-11-01-0257 (regular passes,
activity shop-claims, expires 06:57 local).

## Outcome

- Status: failed (access failure, not a game result). No in-game
  action was taken, nothing was claimed, and no game screen was
  observed in this pass.
- The Mac mini control channel (device id
  1c817413-83e2-0545-cb90-36d5e096a6bd) returned node_offline on
  all three attempts required before an access failure may be
  recorded: computer.session start, connection.health, and a
  second computer.session start. The error states the device is
  offline and does not advertise a wake-up path.
- This is a physical channel block, not a permission question:
  the owner authorization of 2026-10-26 stands, and no password
  or Touch ID step was reached or attempted.
- The tracker was left untouched for this failed unit, per the
  queue rules, so the passes regular stays due and the next
  tick re-produces it.

## Pass context

- Sync at 06:34 reaped 0 expired leases, expired 4 units, and
  produced nothing new: all 20 due regulars were already queued
  by the planner. Inbox held 63 units at sync time.
- No zombie-invasion unit was seeded: the Zombie Invasion event
  ended at about the 19:00 reset on 2026-10-30 (chain unit 066)
  and no Zombie Invasion tab is live, consistent with the
  2026-11-01 day record.
- Own-PR check before game work: the open-PR list for
  zachmesh/lastwar on the VPS returned no open pull requests,
  so no PR comment or conflict of this job was outstanding at
  pass start. The remote records/2026-11-01 branch exists, but
  no open PR names it at this pass.
- No in-game execution happened in this pass, but the failed
  unit and this record are still delivered like every other
  ticker pass: committed to the records/2026-11-01 branch
  from a temporary worktree and opened as a pull request for
  the integrator, per push-and-PR policy 2.0.0.
- Follow-up: the next tick should retry the passes unit once
  the Mac control channel is reachable again. If the channel
  stays offline, that is a device-connectivity matter for the
  owner to clear locally (a local message on the Mac mini
  cleared the same class of lock on 2026-10-27 and 2026-10-29),
  not a queue change.
