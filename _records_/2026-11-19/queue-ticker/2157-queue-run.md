---
title: Ticker pass ticker-2157 - FAILED (Mac mini offline, device channel down)
created: 2026-11-20T05:57:00Z
modified: 2026-11-20T06:04:00Z
version: 1.0.0
description: Queue ticker pass ticker-2157, 2026-11-19 21:57 PT - Mac mini offline, no game input possible
status: unverified
---

# Ticker pass ticker-2157 (2026-11-19 21:57-22:04 PT)

## Outcome

- FAILED. No game input was possible. The Mac mini itself is offline:
  three live probes all returned node_offline with no wake-up path
  (environment.describe x2, connection.health x1, with a 45-second wait
  between the second and third attempts). device.list shows
  connection_state offline and last_seen_at frozen at
  2026-11-20T04:16:40Z (20:16:40 PST), about 1 hour 45 minutes stale at
  probe time. The game window state is unverifiable while the device
  channel is down.
- This is an ESCALATION of the outage, not a repeat of it: the previous
  78 consecutive occurrences (ticker-1818 76th, ticker-1926 77th,
  ticker-2043 78th) were window-loss with the Mac online and the
  LastWar process running. This pass is the 79th consecutive failed
  ticker pass by chain arithmetic and the FIRST occurrence of the
  device-offline mode. The last live contact with the Mac was
  04:16:40Z; the 2043 pass at 04:43Z still saw it online.
- Probe-before-claim HONORED in the claim half: no unit was claimed,
  `next` was never called, no unit attempt was burned. Token acquired
  05:59Z, released 06:02Z before pass end.

## Deviation from the 1926 precedent

- PARTIALLY honored, same shape as 1926: the sync ran before the
  newest ticker record (2043, branch-only) was read, but the probe ran
  before any token or claim and no unit was claimed. The
  deviation-watch of fully-honoring passes stays at THREE (0434, 1347,
  1404).

## Device probe evidence (live, this pass)

- device.list 05:59Z - Zhen's Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd) connection_state offline,
  last_seen_at 2026-11-20T04:16:40Z; the "Zhen's Mac mini connection
  recovery" entry last_seen 2026-11-20T04:17:05Z, also frozen.
- device.describe 05:59Z - returned the device's command set and
  permissions (the metadata path still answers); connection_state
  offline in the same read.
- Attempt 1, environment.describe 06:00Z - node_offline: device is
  offline and does not advertise a wake-up path.
- Attempt 2, connection.health 06:00Z - node_offline, same message.
- Waited 45 seconds. Attempt 3, environment.describe 06:01Z -
  node_offline, same message.
- Total: 3 failed probes, 0 computer sessions started (no session can
  start against an offline device). No relaunch route exists from this
  channel while the device is offline; restoring the channel needs the
  owner (Mac powered on, Muse agent running) or the channel to come
  back on its own, as it did before 04:16Z.

## Own PRs first

- VPS gh route is down (SSH Permission denied (publickey), probed
  05:58Z, about 177.5 hours into the outage), so the PR check ran
  through the GitHub connector (read-only list_pull_requests):
  exactly 3 open PRs, all unchanged since 2026-11-12 - #711
  (knowledge fold, Owner lastwar-knowledge-organizer), #708 (records
  2026-11-12, Owner lastwar-pr-integrator), #425 (tools log gate,
  Owner lastwar-tool-developer). None is owned by this job; no
  records PR exists for records/2026-11-19. No question addressed to
  this job. The connector cannot read PR comments through the
  reviewed read set (pull_request_read rejected); comment-level
  verification of #708 was not repeated this pass and is carried
  from the pr-catchall-2039 read (0 comments on #708 at 1939).
- No new issue filed: the gh route is down and the connector
  identity is dtadpole, forbidden for this repo per the 2032
  tool-development record. The window-loss failure-mode filing
  stays owed, and the new device-offline mode (first occurrence
  this pass) joins it as owed-issue material for a pass with a
  working gh route.

## Queue state

- Sync 05:57Z - reaped 0, expired 0, due 23, produced 0 (all 23 due
  regulars already queued). Pool: inbox 73, claimed 0, done 2581.
  Completion marker reaped: harvest-2026-11-19-1803. Sync warning:
  fetch of records/2026-11-19 failed (fatal: couldn't find remote
  ref records/2026-11-19), branch reconcile skipped (issue #446).
- Zombie seeding skipped: chain zombie-2026-11-10 closed by unit 037
  (2026-11-15, ticker-1804) - the Glacieradon event ended, no Zombie
  Invasion tab in the Events hub (6 tabs enumerated live by the 2043
  pass). No fresh chain may be seeded until the tab is seen live
  again; a live re-check is impossible this pass (device offline).
  No zombie unit sits in inbox or claimed.
- No unit was picked, claimed or completed. Tracker untouched.

## Delivery

- BLOCKED. VPS SSH still Permission denied (publickey) - probed
  05:58Z. The record, the INDEX section and the action-log entry are
  committed on the local records/2026-11-19 branch only; no push, no
  PR. The pass is partial by the push-and-PR policy.
- No game unit since ticker-0214 gifts Nov 17 02:14 PT (about 67.8
  hours missed at pass end). Seventh consecutive missed VIP day
  (carried from planner-1940; the current VIP day is still open
  until the 02:00Z reset boundary, 18:00 PST Nov 20). Missed batches
  stay 42 per the adopted definition (retro-2100: 42 plus 2
  due-but-unexecuted; next point 23:00 PT).
