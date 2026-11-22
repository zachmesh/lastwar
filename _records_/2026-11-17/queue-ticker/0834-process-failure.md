---
title: Queue ticker process failure - game window lost, sixth consecutive occurrence
created: 2026-11-17T16:44:00Z
executor: ticker-0834
unit: none claimed
regular: none
status: process-failure
---

# Queue ticker 2026-11-17 08:34-08:44 PT (ticker-0834) - PROCESS FAILURE

No unit was claimed and no unit was executed. This pass hit the
fullscreen-Space window-loss blocker for the sixth consecutive
ticker pass, so under rule R2 it is recorded as a process failure,
not as another routine failed unit. Token held 08:35-08:44 PT,
released at pass end.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T15:30:49Z,
  07:30:49 PT - the same reading as ticker-0804; it did not move
  during this pass, so no new contact evidence either way).
- Session cc-18: computer.control list_windows returns the same
  10 windows as ticker-0534, ticker-0722 and ticker-0804 - no
  LastWar entry. The game window is still lost in the
  unobservable fullscreen Space; the control channel cannot see
  it. One open_app "LastWar" attempt returned outcome_unknown
  (action 574AB308-BD8A-4293-A5E2-3AEF5E32E30E); the re-list
  afterwards was still the same 10 windows. No further probe
  steps were repeated: screen.snap (observation_unavailable)
  and Finder activate (geometry_mismatch) were already tried
  identically in ticker-0722 and ticker-0534, and the green zoom
  button stays untouched per the standing lesson from
  ticker-0333.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of 08:44 PT there is no evidence he has done
  so. No game unit has executed successfully since ticker-0214
  gifts at 02:14 PT (176 Regular + 67 Premium claimed) - about
  six and a half hours of routine (mail, help, gifts, harvest,
  VIP, donations, trucks, training) now missed.

## R2 accounting - sixth consecutive occurrence

- 1st: ticker-0333, harvest-2026-11-17-0203, 03:33 PT (green zoom
  click moved the window to a native fullscreen Space).
- 2nd: ticker-0443, radar-2026-11-17-0203, 04:43 PT.
- 3rd: ticker-0534, help-2026-11-17-0230, 06:06 PT (channel
  blindness widened to every window).
- 4th: ticker-0722, probe only, 07:22 PT.
- 5th: ticker-0804, probe only, 08:04 PT.
- 6th: this pass, 08:34 PT probe, no unit claimed.
- Standing route change (ticker-0534, R2): NO game unit runs
  until the window is recovered. The next unit in line,
  harvest-2026-11-17-0603, was left in inbox unclaimed; the
  next tick will hit the same blocker unless the Mac window
  is recovered first.

## Sync and pool

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday). Branch reconcile warning: fetch of
  records/2026-11-17 failed (no remote ref), reconcile skipped
  (issue #446).
- Stats: inbox 77, claimed 0, done 2308; newest finished
  2026-11-17T14:15:19Z (139 minutes before the stats read).
  Stalled priority-1 vip-2026-11-16-1800 at 26.2h.
- Zombie chain stays closed (event ended; last live check
  2026-11-15 found no Zombie Invasion tab; most recent done
  zombie unit zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false). No seeding.

## Own PRs first

- VPS SSH still Permission denied (publickey), about 115.9 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete). The VPS gh check could not run.
- Public PR list re-read 2026-11-17T16:35Z via the public GitHub
  API for zachmesh/lastwar: exactly three open PRs - #711
  (knowledge, head work/ko-1132-lock-1047, updated
  2026-11-12T20:04:57Z), #708 (records 2026-11-12, head
  records/2026-11-12, updated 2026-11-12T20:44:37Z), #425 (feat
  tools, head work/log-append-delivery-gate, updated
  2026-11-12T19:29:37Z) - none owned by this job, no PR for
  records/2026-11-17 exists. No question addressed to this job,
  nothing to fix. Newest open issue still #712.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722
  and ticker-0804.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0834-1117-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-17.
