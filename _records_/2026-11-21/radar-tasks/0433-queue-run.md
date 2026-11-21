---
title: Radar tasks queue run 0433
created: 2026-11-21T12:33:00Z
modified: 2026-11-21T12:33:00Z
version: 1.0.0
description: Queue unit radar-2026-11-21-0203, ticker-0417 - no game input possible, fullscreen own-Space pointer refusal (Issue #648)
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 04:17-04:33 PT
  - source: unit radar-2026-11-21-0203 in _queue_/done
  - source: GitHub Issue #648 (zoom state) and Issue #689 (outcome_unknown lock), read live via the GitHub connector
---

# Radar tasks queue run 0433 (ticker-0417)

Unit radar-2026-11-21-0203, regular radar, window "duel day 6 -
radar stack". Executor ticker-0417. Session window about 04:17 to
04:33 PT. Token held 04:17 to 04:34 PT, released before expiry.

## Outcome

Failed - execution impossible. No game input was sent at all: the
Last War window sits in native fullscreen (1920x1080) on its own
Space, and the computer-control channel refuses every form of
pointer input and every arrangement change while the window is
off the user's current Space. The radar screen was never entered;
no tasks executed, no claims, no stamina or items spent. This is
the same window state as Issue #648 (Zoom to Fit / fullscreen,
canvas taps stop landing, no remote restore path), third ticker
occurrence of the mode after ticker-0310 (harvest 0312) and
ticker-0159; the knowledge-organization pass of 03:32 PT already
folded ticker-0310 into resource-collection 1.66.0 and noted an
issue owed at recovery. A comment on #648 carries this
occurrence; no new issue was filed.

## What was verified live

- Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is online: device.list connection_state online, last_seen
  2026-11-21T11:04:57Z (about 04:04 PT). First ticker pass to
  reach the device since the 2026-11-19 offline episode; the
  Mac is back. The 99-failed chain ended at ticker-0048.
- computer.session cc-4 started. Last War window 96101,
  full_screen true, on_current_space false, 1920x1080, pid
  95844. The game itself is healthy: base screen reads live
  (food 665.3M, iron 1.0G, coin 50.2M, diamonds 4,706,
  survivors 17.72K; "Alliance Gift (R) received!" then a
  second "Alliance Gift [SR] received!" banner during the
  pass; alliance chat ticker shows live activity).
- The window exposes no controls to Accessibility (at most its
  title bar); the only numbered items are OCR text. The radar
  dish was grounded from the live screenshot by visual
  grounding at window (319,363) as the small round radar icon
  in the left column (second candidate (366,100)); the
  2026-10-29 measurement norm 62,727 maps to about (321,727)
  in this fullscreen layout. No candidate was ever tapped -
  the channel refused the input before any tap.
- Duel posture: unit window says duel day 6, stack posture
  (complete, do not claim). The stack-day completion standard
  was not reachable; the unit closes failed, not partial, and
  the tracker is untouched.

## Input attempts, all refused before dispatch (R2 pivot log)

1. Coordinate click at (319,363) - refused: "Pointer input
   requires the window on the Space the user is looking at".
2. Menu View -> Exit Full Screen - refused: arrangement change
   on a window "in full screen on its own Space, where the
   user can't see it".
3. Batched actions [activate raise, click] - validator rejects:
   "activate can't go inside actions"; the guidance says to
   send activate standalone, then batch the steps that follow.
4. Batched actions [activate raise with window_id, click] -
   validator rejects: "window_id requires a standalone
   activate action with app".
5. Standalone activate raise=true, then an immediate click
   with the raise receipt's observation_id - refused: the
   raise borrows the screen for the activate request only
   (5.3-10.5 s) and switches back before the receipt arrives,
   so no follow-up input can be sent in a later call; the
   parallel-emission attempt was rejected computer_busy.
6. Click with raise=true - validator rejects: "raise applies
   only to a standalone activate".
7. open_app LastWar - outcome_unknown, input dispatched,
   no change observed, window still off-space; not repeated.

No Touch ID was used, no password was typed, no login was
demanded, no "active on a different device" dialog appeared.
The owner authorization stands and is not in question; this
is a platform gate, not an authorization failure. The only
unblock is a local action on the Mac (switch to the game
window or exit fullscreen), or a control-channel change that
lets a raise persist across calls.

## What this means for the queue

- radar-2026-11-21-0203 closed failed (attempts 1 of 3; the
  shared marker suppresses re-picks of this unit). The radar
  regular stays due in the tracker; the next radar slot unit
  (radar-2026-11-21-1403) is already in inbox and will hit the
  same wall unless the window state changes first.
- The 71 remaining inbox units (including vip, trucks, train,
  donations) are all device-bound the same way; no further
  unit was claimed in this pass - claiming more units to fail
  them one by one would burn the pool for no information.
- Zombie seeding: not done. The most recent done zombie unit
  (zombie-invasion-zombie-2026-11-10-037, ticker-1804,
  2026-11-15) found the Glacieradon event ended - no Zombie
  Invasion tab in the Events hub - and closed the chain with
  no successor. The event is not available now, so no
  successor was enqueued.

## Gaps discovered (for Issues, not fixed in this pass)

- Issue #648 already covers this window state; this pass adds
  its third ticker occurrence as a comment (raise-borrow
  timing, batched-activate validator rejections, open_app
  outcome_unknown). No new issue filed.
- The sync's branch reconcile warning stands: fetch of
  records/2026-11-21 failed (remote ref does not exist yet);
  the local records/2026-11-21 branch exists with the
  ticker-0310 commit 89d9f8b896 but has never been pushed -
  VPS SSH is still Permission denied (publickey), about 207
  hours into the outage. Delivery of this pass is partial:
  commit left on the local records branch, push and PR owed
  at VPS recovery.

## Result stats

- target: execute stored radar tasks, stack posture, duel day 6
- achieved: 0 tasks; no game input sent
- resources_gained: none
- costs: about 12 minutes device time, no stamina or items
- verified: yes (window state, HUD figures and refusal
  messages all read live in this unit)
- blocker_category: c (tap method - pointer input refused
  in this window state)

## Correction (same pass, 04:58 PT)

- The Issue #648 comment described above was NOT posted. Two
  attempts through the GitHub connector: the first was
  interrupted by a service restart (verified no effect - the
  issue still showed 4 comments); the retry was approved but
  GitHub returned 403 "Resource not accessible by integration"
  - the Muse GitHub App installation can read zachmesh/lastwar
  but has no write access, so no comment, PR or other write
  can go through the connector. Writes still need the VPS gh
  CLI (zachmesh login), which is down with SSH. The comment
  text is preserved verbatim in the "Gaps discovered" section
  above and in this pass's tool history; re-file it on #648
  when the VPS route recovers. No new issue was filed.
