---
title: Troop training unit - device control channel unreachable
created: 2026-11-18T04:42:00Z
modified: 2026-11-18T04:42:00Z
version: 1.0.0
description: Queue unit training-2026-11-17-1803 failed - Mac mini computer-control channel could not bind any window
status: failed
grounded_in:
  - source: live device probes on Zhen's Mac mini, 2026-11-17 20:34-20:41 PST
  - source: _records_/2026-11-17/survivor-intake/2004-queue-run.md (ticker-2004, same failure shape 30 minutes earlier)
---

# Troop training unit 2034 - access failed

- Executor: ticker-2034
- Unit: training-2026-11-17-1803 (regular training, activity troop-training)
- Session window: 2026-11-17 20:34-20:41 PST (04:34-04:41 UTC 2026-11-18)
- Status: failed - execution impossible, no game screen was ever reached
- This is the 30th consecutive window-loss occurrence (ticker-2004
  at 20:04 PT was the 29th, same shape, survivors unit completed as
  failed per the 1704 pattern). The NEW SHADE persists a tenth
  pass in a row: the channel cannot bind ANY window, not just the
  game window.
- Route change HONORED this pass: the previous ticker record
  (2004-queue-run.md, same failure shape) was re-read BEFORE the
  unit was claimed and the token taken - no fifth claim-before-read
  recurrence. The deviation-watch process failure (third and
  fourth recurrences by ticker-1934 and ticker-2004) does not
  recur here.
- The troop-training queues were never observed; nothing refilled,
  nothing claimed, no stamina or items spent. The tracker was
  left untouched, so the next tick re-produces the training
  regular.

## What was attempted

Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
connection_state online, last seen 04:04:22Z (unchanged since the
2004 pass - the device list did not move during this pass).
Last War process running. Computer-control session cc-59.

1. environment.describe - LastWar listed among running apps; no
   LastWar window in the window list; display 1920x1080; all
   three permissions true (accessibility, full_disk_access,
   screen_recording). NEW DETAIL: `agent_window.available` is
   false with reason `new_tab_in_existing_window` - the first
   time this reason is recorded; it is a candidate lead for the
   channel failure, unverified.
2. connection.health - both transports healthy and connected
   (native lastResponseAgeSeconds 0, web 4); progressAgeSeconds
   about 2004 on both, i.e. no gateway progress since about
   20:04 PT, the 2004 pass. Unverified whether that staleness is
   cause or symptom.
3. computer.session start - cc-59 started, user_can_see_preview
   true.
4. computer.control open_app LastWar - outcome_unknown, launch
   result could not be identified; did not repeat the launch.
5. computer.observe mode full - observation_unavailable, no
   target.
6. computer.control list_windows - 11 windows, none for
   LastWar; target_bundle_id com.lastwar.ios.
7. computer.control activate Google Chrome window 125 -
   geometry_mismatch (origin_delta 256+, size_delta 256+,
   agent_display=false), input not dispatched; evidence
   ax_windows_empty.
8. computer.observe mode current (the activate error's own
   guidance) - observation_unavailable again.
9. computer.session end - cc-59 ended cleanly.

Conclusion: the control channel cannot bind or observe ANY window
on the Mac right now, not just the game - every select fails with
geometry_mismatch / agent_display=false, and every observation
demands a target that cannot be bound. The game process is alive
but exposes no accessibility window. This is a channel/display-layer
failure, not a missing authorization and not a game login demand:
no login screen, no verification code and no "active on a
different device" dialog was ever seen. Five probes across four
distinct methods were made before recording this as
access-failed, per the standing rule. No further input route was
retried: the identical method has now failed 30 consecutive
times, and repeating it unchanged would be a process failure
under queue rule R2, not diligence. The execute loop stopped
after this one unit for the same reason - a second unit would
fail identically on the same broken channel.

## Pass-level blockers found before game work

- VPS SSH still down: ssh centos@66.179.249.233 returns
  "Permission denied (publickey)" - the 2026-11-12 ~/.ssh loss is
  still unrecovered (about 128.8 hours into the break).
  Consequence for this pass: OWN PRS FIRST could not be done via
  the VPS gh CLI, and no push or PR delivery is possible. The
  pass's commit lands on the local delivery branch
  ticker-2034-1117-delivery (based on records/2026-11-17 at
  e17dd2b93c), because the live records/2026-11-17 branch is
  checked out by the integrator worktree pi-0000-records-1117;
  no push or PR is possible, so the pass is partial on delivery.
- OWN PRS FIRST via the authenticated GitHub connector instead:
  exactly three open PRs on zachmesh/lastwar, heads and
  updated_at unchanged since Nov 12 - #711 (knowledge fold,
  Owner lastwar-knowledge-organizer, head e3c3dfd0), #708
  (records 2026-11-12, Owner lastwar-pr-integrator, head
  2f59c270), #425 (tools log gate, Owner
  lastwar-tool-developer, head 4f41cdd6). None is owned by this
  job, none names this job in its Owner line, no open PR exists
  for records/2026-11-17, and none carries a question addressed
  to this job. Nothing to reply to, fix, or adopt.
- Zombie Invasion: no seeding. The event ended - chain
  zombie-2026-10-28 closed 2026-10-30 per the activity INDEX
  ("Do NOT seed a fresh zombie chain until a Zombie Invasion tab
  is seen live in the Events hub again"), and the 2004 pass
  verified live on 2026-11-15 that the Glacieradon event ended
  with no Zombie Invasion tab. Chain zombie-2026-11-10 stands at
  done 30, pending 0. No zombie unit was enqueued.
- Sync: reaped 0, expired 0, due 22, produced 0 (all already
  queued), inbox 70 at sync time (69 after this unit was
  claimed). Branch reconcile skipped: remote
  records/2026-11-17 does not exist.
- Observation, not this pass's work: the priority-1 VIP unit
  vip-2026-11-17-1800 sits in inbox with attempts 0, planned_for
  and not_before 2026-11-18T02:00:00Z (2026-11-17 18:00 PST),
  but expires_at 2026-11-19T02:00:00Z - a full day past its
  slot, where VIP rewards are expected to expire at the 19:00
  reset. The queue picker chose training-2026-11-17-1803 over
  it (earlier expires_at, 2026-11-18T06:03:00Z). Whether the
  VIP expiry is a tool defect is unverified; flagged here for
  the tool developer, no issue filed from this pass alone.

## Follow-up

- The troop-training refill is still owed: the next tick
  re-produces the training regular, since the tracker was left
  untouched for this failed unit.
- Device control needs the owner or a later run to re-establish:
  the channel binds no window at all, which is wider than a
  game-window problem. Two new leads for the next investigator:
  agent_window unavailable with reason
  `new_tab_in_existing_window`, and connection.health
  progressAgeSeconds stuck at about 2004 since the 2004 pass.
  If the Mac screen is locked, asleep, or on another Space, that
  state could not be verified from here - every probe that could
  show it failed the same way.
- VPS ~/.ssh recovery (IONOS route chosen by the owner 2026-11-14)
  is still the blocker for all PR/push delivery.
- Owed from earlier passes, still open: the 2004 survivor record
  carries no day-INDEX section and no action-log entry of its
  own; the VIP expires_at observation above is unfiled.
