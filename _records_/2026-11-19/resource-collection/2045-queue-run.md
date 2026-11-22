---
title: Ticker pass ticker-2043 - harvest failed (LastWar window still absent)
created: 2026-11-20T04:45:00Z
modified: 2026-11-20T04:53:00Z
version: 1.0.0
description: Queue ticker pass ticker-2043, 2026-11-19 20:43 PT - harvest unit failed, game window lost
status: unverified
---

# Ticker pass ticker-2043 (2026-11-19 20:43-20:53 PT)

## Outcome

- FAILED. No game input was possible. The Mac mini is back online and the
  LastWar process is running, but the game exposes no window: three launch
  attempts across two computer sessions all failed to produce one
  (ax_windows_empty, outcome_unknown x3, list_windows 11 windows with no
  LastWar entry, computer.observe and screen.snap both
  observation_unavailable). This is the 78th consecutive window-loss
  occurrence (1818 was 76th, 1926 was 77th); the window has been lost
  since 2026-11-17 03:33 PT.
- Unit harvest-2026-11-19-1803 completed as failed. Tracker untouched, so
  the next tick re-produces the harvest regular.

## Deviation from the 1926 precedent

- The 1926 pass (one hour earlier) established probe-before-claim: it
  probed the window first and claimed no unit. This pass claimed the
  harvest unit first and probed second, because the 1926 record was not
  read before claiming. The unit burned 1 of its 3 attempts on a pass
  that could not play. The queue tool re-produces the regular, so no
  work is lost, but the claim-before-probe order is the wrong one while
  the window is known lost. Next pass: probe the window before claiming.

## Window probe evidence (live, this pass)

- device.list 04:44Z - Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  connection_state online, last_seen_at 2026-11-20T04:16:40Z (about 27
  minutes old at probe; the last_seen freeze seen by the 2345 pass has
  advanced - the channel is live again).
- environment.describe - LastWar in running_apps (com.lastwar.ios);
  main display 1920x1080; permissions accessibility, full_disk_access,
  screen_recording all true.
- Session cc-150: activate LastWar -> ax_windows_empty, no target
  window bound. open_app LastWar -> outcome_unknown (action
  DA197256). list_windows -> 11 windows, no LastWar. computer.observe
  mode current -> observation_unavailable. screen.snap ->
  observation_unavailable. Second open_app in cc-150 -> outcome_unknown
  (action E033CBCF). Waited 25s. list_windows -> still 11 windows,
  no LastWar.
- Session cc-150 ended; session cc-151 started (reopen-and-retry).
  open_app LastWar -> outcome_unknown (action 37BC143A). Waited 25s.
  list_windows -> still 11 windows, no LastWar.
- Total: 1 activate + 3 open_app attempts, 2 sessions, 2 waits of
  25s, 4 list_windows reads - no window in any of them.
- No quit/kill action exists in the computer.control command set, so
  the wedged app process could not be force-relaunched from this
  channel. Restoring the window needs the owner (or a future pass
  with a working relaunch route).

## Own PRs first

- VPS gh route is down (SSH Permission denied (publickey), probed
  04:43Z, about 176 hours into the outage), so the PR check ran
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
- No new issue filed: the semantic issue search for the window-loss
  failure mode returned 0 matches, but filing requires the VPS gh
  route (down) or a write-capable connector call under an identity
  that is not the repo owner's (connector identity is dtadpole,
  forbidden for this repo per the 2032 tool-development record).
  Issue filing for the window-loss mode stays owed to a pass with a
  working gh route.

## Queue state

- Sync 04:43Z - reaped 0, expired 0, due 23, produced 0 (all 23 due
  regulars already queued). Pool: inbox 74, claimed 0, done 2580.
- Zombie seeding skipped: chain zombie-2026-11-10 closed by unit 037
  (2026-11-15, ticker-1804) - the Glacieradon event ended, no Zombie
  Invasion tab in the Events hub (6 tabs enumerated live). No fresh
  chain may be seeded until the tab is seen live again. No zombie
  unit sits in inbox or claimed.
- Next unit picked: harvest-2026-11-19-1803 (resource-collection,
  est 9 min, priority 3, expires 2026-11-20T06:03:00Z). Claimed
  04:45:55Z by ticker-2043, lease to 05:05:55Z.
- Token: acquired by ticker-2043 04:43Z, released before pass end.
  No other unit was attempted; the pass budget ends with the token
  release.

## Delivery

- BLOCKED. VPS SSH still Permission denied (publickey) - probed
  04:43Z. The record, the INDEX section, the completed unit file
  and the action-log entry are committed on the local
  records/2026-11-19 branch only; no push, no PR. The pass is
  partial by the push-and-PR policy.
- No game unit since ticker-0214 gifts Nov 17 02:14 PT (about
  sixty-six and a half hours missed at pass end). Seventh
  consecutive missed VIP day (carried from planner-1940). Missed
  batches stay 42 per the adopted definition (next point 23:00 PT).
