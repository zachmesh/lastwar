---
title: Mail Rewards Queue Run
created: 2026-11-05T10:25:00-08:00
modified: 2026-11-05T10:36:00-08:00
version: 1.0.0
description: Mail unit mail-2026-11-05-0630 executed by ticker-1025, failed on Mac device offline with no wake-up path, forty-second consecutive pass with a Mac device-access blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 10:25 to 10:36 local
---

# Mail rewards 2026-11-05, ticker-1025

Unit mail-2026-11-05-0630, failed. No game screen was ever
read and no game input was dispatched: every device invoke to
the Mac mini returned node_offline or timed out, so no mail
category was opened and no attachment was claimed. This was a
segment 2 unit (planned_for 2026-11-05T14:30:00Z, expires
18:30:00Z); on a working screen it would have opened Mail and
pressed Claim All in each claimable category per the
mail-rewards activity metadata, never Delete All.

## Attempts

- device.list reports the Mac mini
  1c817413-83e2-0545-cb90-36d5e096a6bd offline, last_seen
  2026-11-05T15:36:52Z (07:36 local) - stale about 2 hours
  55 minutes at pass time. Earlier passes (0904, 0941) still
  saw it reported online with the same stale timestamp; the
  state has worsened from online-stale to offline.
- computer.session start on the Mac mini: node_offline,
  device is offline and does not advertise a wake-up path
  (attempt 1).
- connection.health on the Mac mini: node_offline (attempt 2).
- connection.repair (web) on the Mac mini: node_offline
  (attempt 3).
- computer.session start again on the Mac mini: node_offline
  (attempt 4).
- connection.health on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 5).

Five attempts, zero responses. This is the forty-second
consecutive ticker pass with a Mac device-access blocker
(Issue 284, open, tooling), and the third in the worsened
zero-response form after ticker-0904 (fortieth) and
ticker-0941 (forty-first). The fail-fast probe
(_tools_/mac_capture_probe.py 1.1.0, run from a /tmp copy
of main's version since this worktree carries no _tools_
folder) classifies CHANNEL_STALL (high confidence),
stop_pass yes, exit 12: 1 invoke timed out, 0 invokes
returned a response. PR #321, which implements that
diagnosis, merged 2026-11-05 09:47 PST. The Dock-icon owner
step addresses the window-stream fault, not a stalled invoke
channel; recovery still needs the Mac-side agent gateway
restart before re-probing, and re-probing is owed only
after device.list last_seen refreshes.

## Outcome

- Mail claimed: none (no screen read).
- Tracker untouched (failed units do not touch the tracker).
- The pass stopped after this one unit, per the established
  pattern for this blocker.
- Own PRs first: PR #310 (records/2026-11-05) - the
  integrator verified a clean test merge at the 10:00
  non-batch pass and it awaits the 11:00 batch; no
  unanswered question addressed to this job, no action owed.
- No zombie seeding: the Zombie Invasion event ended
  2026-10-30 about 19:00 and the chain is closed; no Zombie
  Invasion tab is to be expected until it is seen live again.
- Sync: reaped 0, expired 2, due 21, produced nothing new,
  all 21 regulars already queued. Inbox 72, claimed 0,
  done 912.
