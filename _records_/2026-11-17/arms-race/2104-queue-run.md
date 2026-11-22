---
title: Arms Race unit - device control channel unreachable
created: 2026-11-18T05:12:00Z
modified: 2026-11-18T05:12:00Z
version: 1.0.0
description: Queue unit arms-race-2026-11-17-1803 failed - Mac mini computer-control channel could not bind any window
status: failed
grounded_in:
  - source: live device probes on Zhen's Mac mini, 2026-11-17 21:04-21:11 PST
  - source: _records_/2026-11-17/troop-training/2034-queue-run.md (ticker-2034, same failure shape 30 minutes earlier)
---

# Arms Race unit 2104 - access failed

- Executor: ticker-2104
- Unit: arms-race-2026-11-17-1803 (regular arms-race, activity arms-race)
- Session window: 2026-11-17 21:04-21:11 PST (05:04-05:11 UTC 2026-11-18)
- Status: failed - execution impossible, no game screen was ever reached
- This is the 31st consecutive window-loss occurrence (ticker-2034
  at 20:34 PT was the 30th, same shape, training unit completed as
  failed per the 1704 pattern). The NEW SHADE persists an eleventh
  pass in a row: the channel cannot bind ANY window, not just the
  game window.
- Route change HONORED this pass: the previous ticker record
  (2034-queue-run.md, same failure shape) was re-read BEFORE the
  token was taken and the unit was claimed - no claim-before-read
  recurrence. The deviation-watch process failure (third and
  fourth recurrences by ticker-1934 and ticker-2004) does not
  recur here.
- The Arms Race phase, score and tier-3 target were never read;
  nothing scored, nothing claimed, no stamina or items spent. The
  tracker was left untouched, so the next tick re-produces the
  arms-race regular.

## What was attempted

Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
connection_state online, last seen 04:04:22Z (unchanged since the
2004 pass - the device list has not moved for over an hour).
Last War process running. Computer-control session cc-60.

1. environment.describe (refresh) - LastWar listed among running
   apps; no LastWar window in the window list; display 1920x1080;
   all three permissions true (accessibility, full_disk_access,
   screen_recording). `agent_window.available` is false with
   reason `new_tab_in_existing_window` - the same reason the
   2034 pass recorded first.
2. connection.health - both transports healthy and connected
   (native lastResponseAgeSeconds 0, web 8); progressAgeSeconds
   about 3899 on native and 3900 on web, i.e. no gateway progress
   for about 65 minutes, up from about 2004 at the 2034 pass.
   The staleness is growing, not recovering.
3. computer.session start - cc-60 started, user_can_see_preview
   true.
4. computer.control open_app LastWar - outcome_unknown, launch
   result could not be identified; did not repeat the launch.
5. computer.observe mode full - observation_unavailable, no
   target.
6. computer.control list_windows - 11 windows, none for
   LastWar; target_bundle_id com.lastwar.ios. Chrome window 125
   still present ("Recharge Center - LASTWAR").
7. computer.control activate Google Chrome window 125 -
   geometry_mismatch (origin_delta 256+, size_delta 256+,
   agent_display=false), input not dispatched; evidence
   ax_windows_empty.
8. computer.observe mode current (the activate error's own
   guidance) - observation_unavailable again.
9. computer.session end - cc-60 ended cleanly.

Conclusion: the control channel cannot bind or observe ANY window
on the Mac right now, not just the game - every select fails with
geometry_mismatch / agent_display=false, and every observation
demands a target that cannot be bound. The game process is alive
but exposes no accessibility window. This is a channel/display-layer
failure, not a missing authorization and not a game login demand:
no login screen, no verification code and no "active on a
different device" dialog was ever seen. Eight probe calls across
five distinct methods were made before recording this as
access-failed, per the standing rule. The execute loop stopped
after this one unit for the same reason - a second unit would
fail identically on the same broken channel, and repeating the
identical method unchanged would be a process failure under
queue rule R2, not diligence.

## Pass-level blockers found before game work

- VPS SSH still down: ssh centos@66.179.249.233 returns
  "Permission denied (publickey)" - the 2026-11-12 ~/.ssh loss is
  still unrecovered (about 129 hours into the break).
  Consequence for this pass: OWN PRS FIRST could not be done via
  the VPS gh CLI, and no push or PR delivery is possible. The
  pass's commit lands on the local delivery branch
  ticker-2104-1117-delivery (based on records/2026-11-17 at
  d73f9fcf0e), because the live records/2026-11-17 branch is
  checked out by the integrator worktree pi-0000-records-1117;
  no push or PR is possible, so the pass is partial on delivery.
- OWN PRS FIRST via the authenticated GitHub connector instead:
  exactly three open PRs on zachmesh/lastwar, heads and
  updated_at unchanged since Nov 12 - #711 (knowledge fold,
  Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270,
  updated 2026-11-12T20:44:37Z), #425 (tools log gate, Owner
  lastwar-tool-developer, head 4f41cdd6,
  updated 2026-11-12T19:29:37Z). None is owned by this job,
  none names this job in its Owner line, no open PR exists
  for records/2026-11-17, and none carries a question addressed
  to this job. Nothing to reply to, fix, or adopt.
- Sibling delivery branch ticker-2034-1117-delivery (6f03abdf50,
  the 2034 record) is still unmerged into records/2026-11-17;
  this branch does not contain it, and it does not contain the
  2045 pr-integration record (d73f9fcf0e). Reconciliation of the
  sibling delivery branches stays with the integrator when the
  VPS route recovers.
- Zombie Invasion: no seeding. The event ended - chain
  zombie-2026-10-28 closed 2026-10-30 per the activity INDEX
  ("Do NOT seed a fresh zombie chain until a Zombie Invasion tab
  is seen live in the Events hub again"), and the 2004 pass
  verified live on 2026-11-15 that the Glacieradon event ended
  with no Zombie Invasion tab. Chain zombie-2026-11-10 stands at
  done 30, pending 0. No zombie unit was enqueued.
- Sync: reaped 0, expired 0, due 22, produced 0 (all already
  queued), inbox 69 at sync time. Branch reconcile skipped:
  remote records/2026-11-17 does not exist.
- Observation, not this pass's work: this unit's window field
  reads "duel day 2", but duel day 3 (Age of Science) began at
  18:00 PT and the unit's slot is 18:03 PT - the label is stale
  relative to its slot (the unit was produced at 06:58 PT, when
  day 2 was still live). Whether the window label is a tool
  defect is unverified; flagged here for the tool developer, no
  issue filed from this pass alone. The VIP expires_at
  observation from the 2034 pass is still unfiled.
- Correction: the 2034 follow-up claimed the 2004 survivor
  record carries no day-INDEX section and no action-log entry
  of its own - contradicted by the records/2026-11-17 tip,
  which carries both (INDEX section "20:04 to about 20:13";
  action-log entry ts 2026-11-18T04:17:00Z). No owed item
  remains on that point.

## Follow-up

- The Arms Race tier-3 push is still owed: the next tick
  re-produces the arms-race regular, since the tracker was left
  untouched for this failed unit.
- Device control needs the owner or a later run to re-establish:
  the channel binds no window at all, which is wider than a
  game-window problem. Leads unchanged from the 2034 pass:
  agent_window unavailable with reason
  `new_tab_in_existing_window`, and connection.health
  progressAgeSeconds now about 3900 and still growing. If the
  Mac screen is locked, asleep, or on another Space, that state
  could not be verified from here - every probe that could
  show it failed the same way.
- VPS ~/.ssh recovery (IONOS route chosen by the owner 2026-11-14)
  is still the blocker for all PR/push delivery.
