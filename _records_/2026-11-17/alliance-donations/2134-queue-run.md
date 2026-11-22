---
title: Alliance donations unit - device control channel unreachable
created: 2026-11-18T05:45:00Z
modified: 2026-11-18T05:45:00Z
version: 1.0.0
description: Queue unit donations-2026-11-17-1803 failed - Mac mini computer-control channel could not bind any window
status: failed
grounded_in:
  - source: live device probes on Zhen's Mac mini, 2026-11-17 21:38-21:45 PST
  - source: _records_/2026-11-17/troop-training/2034-queue-run.md (ticker-2034, same failure shape 30 minutes earlier)
---

# Alliance donations unit 2134 - access failed

- Executor: ticker-2134
- Unit: donations-2026-11-17-1803 (regular donations, activity alliance-donations)
- Session window: 2026-11-17 21:38-21:45 PST (05:38-05:45 UTC 2026-11-18)
- Status: failed - execution impossible, no game screen was ever reached
- This is the 31st consecutive window-loss occurrence (ticker-2034
  at 20:34 PT was the 30th, same shape, training unit completed as
  failed per the 1704 pattern). The NEW SHADE persists an eleventh
  pass in a row: the channel cannot bind ANY window, not just the
  game window.
- Route change HONORED this pass: the previous ticker record
  (2034-queue-run.md, same failure shape) was re-read BEFORE the
  token was taken and the unit claimed - no sixth
  claim-before-read recurrence. The deviation-watch process
  failure (third and fourth recurrences by ticker-1934 and
  ticker-2004, resolved by ticker-2034) does not recur here.

## What was attempted

Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
connection_state online, last seen 05:37:39Z (fresh at pass
start). Last War process running. Computer-control session cc-61.

1. environment.describe - LastWar listed among running apps; no
   LastWar window in the window list; display 1920x1080; all
   three permissions true (accessibility, full_disk_access,
   screen_recording). `agent_window.available` is false with
   reason `new_tab_in_existing_window` - unchanged since the
   2004 pass, third pass recording it.
2. connection.health - both transports healthy and connected
   (native lastResponseAgeSeconds 0, web 6); native
   progressAgeSeconds about 5693, i.e. no gateway progress
   since about 20:04 PT - the staleness first noted by the
   2034 pass has grown from about 2004 to about 5693 seconds
   and is still growing, now about 95 minutes. Web
   progressAgeSeconds 96. Unverified whether that staleness
   is cause or symptom.
3. computer.session start - cc-61 started, user_can_see_preview
   true.
4. computer.control open_app LastWar - outcome_unknown, launch
   result could not be identified; did not repeat the launch.
5. computer.observe mode full - observation_unavailable, no
   target.
6. computer.control list_windows - 11 windows, none for
   LastWar; target_bundle_id com.lastwar.ios.
7. screen.snap - observation_unavailable again: even the
   no-target display capture path fails, so the channel
   cannot capture the screen at all without a bound window.
8. computer.session end - cc-61 ended cleanly.

Conclusion: the control channel cannot bind or observe ANY window
on the Mac right now, not just the game - every select fails with
geometry_mismatch / agent_display=false (per the 2034 pass) or
observation_unavailable, and every observation demands a target
that cannot be bound. The game process is alive but exposes no
accessibility window. This is a channel/display-layer failure,
not a missing authorization and not a game login demand:
no login screen, no verification code and no "active on a
different device" dialog was ever seen. Seven probes across six
distinct methods were made before recording this as
access-failed, per the standing rule. No further input route was
retried: the identical method has now failed 31 consecutive
times, and repeating it unchanged would be a process failure
under queue rule R2, not diligence. The execute loop stopped
after this one unit for the same reason - a second unit would
fail identically on the same broken channel.

## Pass-level blockers found before game work

- VPS SSH still down: ssh centos@66.179.249.233 returns
  "Permission denied (publickey)" - the 2026-11-12 ~/.ssh loss
  is still unrecovered (about 129.3 hours into the break).
  Consequence for this pass: OWN PRS FIRST could not be done via
  the VPS gh CLI, and no push or PR delivery is possible. The
  pass's commit lands on the local delivery branch
  ticker-2134-1117-delivery (based on records/2026-11-17 at
  the 2034 commit), because the live records/2026-11-17 branch
  is checked out by the integrator worktree pi-0000-records-1117;
  no push or PR is possible, so the pass is partial on delivery.
- OWN PRS FIRST via the authenticated GitHub connector instead,
  fresh check this pass (21:36 PT): exactly three open PRs on
  zachmesh/lastwar, heads and updated_at unchanged since Nov 12
  - #711 (knowledge fold, Owner lastwar-knowledge-organizer,
  head e3c3dfd0, updated 2026-11-12T20:04:57Z), #708 (records
  2026-11-12, Owner lastwar-pr-integrator, head 2f59c270,
  updated 2026-11-12T20:44:37Z), #425 (tools log gate, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). None is owned by this job, none names
  this job in its Owner line, no open PR exists for
  records/2026-11-17, and none carries a question addressed to
  this job. Nothing to reply to, fix, or adopt. The 2039
  pr-catchall pass verified the same state 55 minutes earlier.
- Zombie Invasion: no seeding. The event ended 2026-10-30 per
  the activity INDEX ("Do NOT seed a fresh zombie chain until
  a Zombie Invasion tab is seen live in the Events hub again"),
  and the chain zombie-2026-10-28 is closed. No zombie unit
  was enqueued.
- Sync: reaped 0, expired 0, due 22, produced 0 (all already
  queued), inbox 68 at sync time (67 after this unit was
  claimed). Branch reconcile skipped: remote
  records/2026-11-17 does not exist.
- Observation, not this pass's work: the priority-1 VIP unit
  vip-2026-11-17-1800 still sits in inbox with attempts 0,
  planned_for and not_before 2026-11-18T02:00:00Z
  (2026-11-17 18:00 PST), but expires_at 2026-11-19T02:00:00Z
  - a full day past its slot, where VIP rewards are expected
  to expire at the 19:00 reset. The queue picker chose
  donations-2026-11-17-1803 over it (earlier expires_at,
  2026-11-18T06:03:00Z). Whether the VIP expiry is a tool
  defect is unverified; flagged by the 2034 pass for the tool
  developer, still unfiled.

## Follow-up

- The alliance donations are still owed: the next tick
  re-produces the donations regular, since the tracker was left
  untouched for this failed unit.
- Device control needs the owner or a later run to re-establish:
  the channel binds no window at all, which is wider than a
  game-window problem. Leads carried forward, all unchanged
  except the growing staleness: agent_window unavailable with
  reason `new_tab_in_existing_window` (third pass), native
  connection.health progressAgeSeconds stuck since about
  20:04 PT and growing (5693 now, was about 2004 at 2034),
  and screen.snap failing the same way as observe. If the Mac
  screen is locked, asleep, or on another Space, that state
  could not be verified from here - every probe that could
  show it failed the same way.
- VPS ~/.ssh recovery (IONOS route chosen by the owner 2026-11-14)
  is still the blocker for all PR/push delivery.
- Owed from earlier passes, still open: the 2004 survivor record
  carries no day-INDEX section and no action-log entry of its
  own; the VIP expires_at observation above is unfiled.
