---
title: Radar tasks queue run 1216
created: 2026-11-21T20:16:00Z
modified: 2026-11-21T20:16:00Z
version: 1.0.0
description: Queue unit radar-2026-11-21-1003, ticker-1204 - no game input possible, fullscreen own-Space pointer refusal (Issue #648), sixth consecutive blocked game unit
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 12:04-12:16 PT
  - source: unit radar-2026-11-21-1003 in _queue_/done
  - source: GitHub Issue #648 (zoom state), read live via the GitHub connector
---

# Radar tasks queue run 1216 (ticker-1204)

Unit radar-2026-11-21-1003, regular radar, window "duel day 6 -
radar stack". Executor ticker-1204. Session window about 12:04 to
12:16 PT. Token acquired 12:04 PT, released before expiry.

## Outcome

Failed - execution impossible. No game input was sent: the Last War
window sits in native fullscreen (1920x1080) on its own Space, and
the computer-control channel refuses pointer input while the window
is off the user's current Space. The radar screen was never entered;
no tasks executed, no claims, no stamina or items spent. This is
the same window state as Issue #648, the sixth consecutive game
unit blocked by this precondition after ticker-0159 (radar),
ticker-0310 (harvest), ticker-0417 (radar), ticker-0934 (harvest)
and ticker-1058 (harvest). The tracker is untouched (failed).

## What was verified live

- Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is online: device.list connection_state online, last_seen
  2026-11-21T18:40:36Z (about 10:40 PT).
- computer.session cc-8 started and ended cleanly. list_windows
  reads Last War window 96101, full_screen true,
  on_current_space false, 1920x1080, pid 95844 - the same window
  and pid as every blocked pass since 02:01 PT; window state
  verified UNCHANGED.
- The game itself is healthy: a fresh probe screenshot of the
  base screen reads live (food 665.3M, iron 1.0G, coin 50.2M,
  diamonds 4,706; "Alliance Gifts received!" banner; Component
  Factory Lv.20; many green and white resource bubbles visible
  over the farmland and gold buildings, uncollected; two
  survivor "?" icons at the front door). HUD figures are
  identical to the 04:33 PT read (ticker-0417), the 09:34 PT
  read (ticker-0934) and the 10:58 PT read (ticker-1058).
- Own PRs first: exactly 3 open PRs via the GitHub connector
  (read-only), all unchanged since 2026-11-12 - #711 knowledge
  (head e3c3dfd0, Owner lastwar-knowledge-organizer), #708
  records 2026-11-12 (head 2f59c270, Owner
  lastwar-pr-integrator), #425 tools (head 4f41cdd6, Owner
  lastwar-tool-developer). None is owned by this job, no PR
  exists for records/2026-11-21, and no question or issue is
  addressed to this job. Nothing to adopt or fix.
- VPS SSH still Permission denied (publickey), tested live this
  pass - about 213 hours into the outage since 2026-11-12.
  Push and PR delivery are impossible this pass; the commit
  stays on the local records/2026-11-21 branch.
- Zombie seeding: not done. The most recent done zombie unit
  (zombie-invasion-zombie-2026-11-10-037, ticker-1804,
  2026-11-15) found the Glacieradon event ended - no Zombie
  Invasion tab in the Events hub - and closed the chain with
  no successor. The event is not available now, so no
  successor was enqueued.

## Input attempts (R2 pivot log)

No input was attempted in this pass, by the ticker-0934/1058
stop rule: retry input only on a changed window state. The
window state is byte-identical to the five earlier blocked
passes, and every input route was already refused in this
exact state today - coordinate click ("Pointer input requires
the window on the Space the user is looking at"), menu View ->
Exit Full Screen (arrangement change refused), standalone
activate raise=true (raise borrows the screen 5.3-10.5 s then
switches back), batched activate+click (validator rejects),
open_app LastWar (outcome_unknown, no change).

One NEW nuance from this pass's activate receipt (not a new
route, recorded for Issue #648): element actions DO reach the
off-Space window - "click_element (with ax_action too), type
with element_number, select_popup and menu" - but the window
exposes no Accessibility controls to press: the activate
observation lists only 5 elements, all OCR text fragments of
the Alliance Gift banner. The radar dish is a canvas tap,
which is pointer input and still needs the window on the
user's Space. The only unblock remains a local action on the
Mac (switch to the game window or exit fullscreen via View ->
Exit Full Screen), or a control-channel change that lets a
raise persist across calls.

No Touch ID was used, no password was typed, no login was
demanded, no "active on a different device" dialog appeared.
The owner authorization stands and is not in question; this
is a platform gate, not an authorization failure.

## What this means for the queue

- radar-2026-11-21-1003 closed failed (attempts 1 of 3; the
  shared marker suppresses re-picks of this unit). The radar
  regular stays due in the tracker; the next radar slot unit
  (radar-2026-11-21-1403) is already in inbox and will hit the
  same wall unless the window state changes first.
- The 76 remaining inbox units are all device-bound the same
  way; no further unit was claimed in this pass - claiming more
  units to fail them one by one would burn the pool for no
  information.
- The pre-reset zero-sweep pair for tonight (zero-sweep
  2026-11-21 1630 and 1730) is in inbox and will hit the same
  wall unless the window state changes before 17:30 PT.

## Gaps discovered (for Issues, not fixed in this pass)

- Issue #648 already covers this window state; this pass is its
  sixth ticker occurrence. A comment carrying this occurrence
  (element actions reach the off-Space window but the game
  canvas exposes no Accessibility controls, so the radar dish
  still has no input route; window state unchanged since
  02:01 PT) is owed on #648 at VPS recovery - the GitHub
  connector is read-only (403 "Resource not accessible by
  integration" on writes, verified by ticker-0417), and VPS
  SSH is down, so no comment can be posted now. No new issue
  filed.
- The sync's branch reconcile warning stands: fetch of
  records/2026-11-21 failed (remote ref does not exist yet);
  the local records/2026-11-21 branch exists (tip edc097d7a2,
  ticker-1058) but has never been pushed.

## Result stats

- target: execute stored radar tasks, stack posture, duel day 6
- achieved: 0 tasks; no game input sent
- resources_gained: none
- costs: about 12 minutes device time, no stamina or items
- verified: yes (window state, HUD figures and refusal
  messages all read live in this unit)
- blocker_category: c (tap method - pointer input refused
  in this window state)

## Delivery

- Commit left on the local records/2026-11-21 branch; push and
  PR owed at VPS recovery. No PR for records/2026-11-21 exists.
