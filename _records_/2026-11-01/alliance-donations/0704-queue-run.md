---
title: Queue Run 0704 Alliance Donations Access Failed
created: 2026-11-01T15:10:00Z
modified: 2026-11-01T15:10:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-0704 donations unit failed on device access
status: unverified
grounded_in:
  - source: device control channel responses during this pass
---

# 0704 queue run - alliance donations, access failed

Session window: 2026-11-01 about 07:04 to 07:20 America/Los_Angeles.
Executor: ticker-0704. Unit: donations-2026-11-01-0603 (regular
donations, activity alliance-donations, expires 10:03 local).

## Outcome

- Status: failed (access failure, not a game result). No in-game
  action was taken, nothing was claimed, and no game screen was
  observed in this pass.
- The Mac mini control channel (device id
  1c817413-83e2-0545-cb90-36d5e096a6bd) returned node_offline on
  all three computer.session starts required before an access
  failure may be recorded, plus a failed connection.health probe
  (node_offline) and a timed-out recovery-channel attempt
  (connection.repair on the Mac mini connection-recovery device,
  node_invoke_timeout after 25000ms). Every error states the
  device is offline and does not advertise a wake-up path, and
  the device last-seen stamp stayed at 2026-11-01T09:47:27Z
  (01:47 local) unmoved across the pass.
- This is a physical channel block, not a permission question:
  the owner authorization of 2026-10-26 stands, and no password
  or Touch ID step was reached or attempted.
- The tracker was left untouched for this failed unit, per the
  queue rules, so the donations regular stays due and the next
  tick re-produces it. No live Donation Count was read in this
  unit, so no donation figure is claimed anywhere in this record.

## Pass context

- Sync at 07:04 reaped 0 expired leases, expired 4 units, and
  produced nothing new: all 20 due regulars were already queued
  by the planner. Inbox held 69 units at sync time.
- No zombie-invasion unit was seeded: the Zombie Invasion event
  ended at about the 19:00 reset on 2026-10-30 (chain unit 066)
  and no Zombie Invasion tab is live, consistent with the
  2026-11-01 day record.
- Own-PR check before game work: the open-PR list for
  zachmesh/lastwar on the VPS returned no open pull requests,
  so no PR comment or conflict of this job was outstanding at
  pass start. The most recent records PR (60) had merged at
  07:02 local, just before this tick.
- Tenth consecutive access-failed pass after the 02:34, 03:04,
  03:34, 04:04, 04:34, 05:04, 05:34, 06:04 and 06:34 passes; the
  channel has been down since 01:47 local.
- No in-game execution happened in this pass, but the failed
  unit and this record are still delivered like every other
  ticker pass: committed to the records/2026-11-01 branch
  from a temporary worktree and opened as a pull request for
  the integrator, per push-and-PR policy 2.0.0.
- Follow-up: the next tick should retry the donations unit once
  the Mac control channel is reachable again. If the channel
  stays offline, that is a device-connectivity matter for the
  owner to clear locally (a local message on the Mac mini
  cleared the same class of lock on 2026-10-27 and 2026-10-29),
  not a queue change.
