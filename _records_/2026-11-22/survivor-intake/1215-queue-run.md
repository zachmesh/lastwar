---
title: Survivor intake queue run 1215
created: 2026-11-22T20:15:00Z
modified: 2026-11-22T20:15:00Z
level: L0
version: 1.0.0
description: Survivors unit survivors-2026-11-22-1003, ticker-1159, 1 gate survivor processed by the ?-cleared sequence on two post-tap reads, visible gate line clear, 0 recruits identified
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 12:00-12:11 PT
  - source: unit survivors-2026-11-22-1003 in _queue_/done
  - source: _activities_/survivor-intake/INDEX.md version 1.61.0
---

# Survivor intake queue run 1215 (ticker-1159)

Unit survivors-2026-11-22-1003, regular survivors, segment 1.
Executor ticker-1159. Computer session cc-143. Session window
about 12:00 to 12:11 PT. Game windowed 642x951, window 127196,
frontmost after the second observe (it came to the front by
itself, no input from the executor or the user). No "active on
a different device" dialog. No login or verification demanded.

## Outcome

Done - 1 gate survivor processed, visible gate line clear,
0 recruits identified. No Recruit card opened and no dialog
line was read, so no name, role or trait is recorded. No
building post was taken, so under the 1644 refinement no
Quick Dispatch is owed. Tracker marked done at 12:11:31 PT.

## Post state at entry - read live about 12:01

- Base screen: power 147,972,269, food 765.4M, iron 1.1G,
  coin 109.2M, diamonds 6,436. "Build: Oil Well [0/1]"
  banner at the bottom. Chat bar at the bottom with
  "Breaking News: Intense battle..." and chat lines.
- Window-state precondition: windowed 642x951 (window
  127196), selected for background input at first, then
  frontmost by itself. Canvas taps land (this unit's tap
  processed the survivor). The #648 precondition is clear,
  matching the 2026-11-21 1335 correction.
- Entry route followed the Issue #822 rule from the
  ticker-1104 pass the same morning: list_windows first,
  activate the existing window 127196, never open_app
  when the game already runs (open_app had opened the
  duplicate window 127250 whose canvas takes no input).

## Gate - read live about 12:01-12:07

- The signed front gate is at the left edge of the current
  view: a yellow "Zombies" sign over a green metal gate
  with biohazard signs, confirmed on a 3x enlarged crop.
- Fresh grounding on the entry screenshot: "?" bubble at
  norm (99,649), survivor figure at norm (110,675).
  Crop-before-tap (the 0941 rule): a tight 4x crop showed
  the white "?" speech bubble and a small tan figure
  beneath it in front of the gate, plus a small green dot
  beside the bubble. The red-panda pet marker sits
  elsewhere at the gate and was not tapped (0520 lesson).
- The figure stands in a crowded strip: the truck button
  above-left, the radar button with its red 11 badge
  below-left. The tap point was norm (100,688) - below
  the bubble, between the two buttons, outside both
  hitboxes by the crop measurement.

## Tap and re-reads

- One click on the figure at norm (100,688), about 12:08,
  action C3C92B5D, dispatched; the receipt reported
  observed_effect unknown, so the state was re-read from
  fresh screenshots instead of trusting the receipt (0941).
- Re-read 1, about 12:09: the "?" bubble is gone from the
  gate. A small green marker remains at the figure's spot
  (the 0941 after-crop marker, still unresolved whether
  plant or processed marker). The red-panda pet marker
  circle is now visible at the gate. No smiley-face bubble
  was seen, no figure remains at the gate, no Recruit card
  and no dialog opened.
- Re-read 2, about 12:11: computer session cc-143 had
  closed by itself before this read (observe reported no
  open session), so the confirmation used screen.snap,
  which reported no_change_observed against re-read 1 -
  the "?" bubble is still gone, nothing new appeared.
- The intake is recorded as processed by the "?"-cleared
  sequence on two post-tap reads (the 0844 standard), with
  0 recruits identified: no card, no name, no role, no
  trait, no smiley seen. The visible gate line is clear;
  the rest of the gate runs off-screen right and the base
  view cannot be panned through this control channel, so
  "clear" covers the visible gate only.

## Result stats

- target: take in the waiting gate line, verify each survivor, run Quick Dispatch after any intake with a post
- achieved: 1 gate survivor processed by ?-cleared sequence on two post-tap reads, visible gate line clear, 0 recruits identified, no post so no Quick Dispatch owed
- resources_gained: none read - no card or reward line appeared
- points: 0
- costs: about 15 minutes device time, no spend, no stamina, no items
- verified: yes (post state, gate crop, tap receipt, two post-tap reads all live in this unit)
- survivors_processed: 1
- recruits_identified: 0
- gate_clear: true (visible gate)

## Pass notes (setup, not game state)

- Worktree ticker-1148 on branch ticker-1148-records-1122,
  created from the remote records/2026-11-22 tip 1827d8b42.
  The main checkout sits on work/ops-execution-records with
  another job's uncommitted changes and was not disturbed.
- _tools_/queue.py in the worktree was refreshed from main
  (working-tree only, never staged or committed): the
  records-branch copy predated the #818 scout-chain fix in
  main 21d462609, and the #694 currency guard refused sync
  until the copy matched main. The refreshed copy is
  byte-identical to main's _tools_/queue.py.
- Zombie Invasion was NOT seeded this pass: the event ended
  (unit 037, 2026-11-15, Glacieradon event ended, chain
  zombie-2026-11-10 closed with no successor) and the
  regular is no longer in the roster (25 regulars,
  zombie-invasion absent). The 6 pending zombie units in
  the worktree snapshot are stale; the live pool holds none.
- The local records/2026-11-22 branch line (69a4604b8,
  a17a55a77) is stale against the remote branch and is NOT
  an ancestor of it, but its contents are not lost: the
  remote branch already carries
  _records_/2026-11-22/pr-catchall/0039-run.md and
  _records_/2026-11-22/pr-integration/0045-run.md. This
  pass worked from the remote tip and left the local line
  untouched.
- Token held by ticker-1159 from 11:58:56 PT; the pass ran
  one unit only - the ~25 minute budget left no room for a
  second unit plus delivery after the 15-minute survivors
  unit.
- Delivery: the commit was first made on
  ticker-1148-records-1122 from tip 1827d8b42, then
  cherry-picked onto the new tip db65eac9d (the 1215
  pr-integration run had advanced the branch in between);
  the INDEX and action-log appends conflicted and were
  resolved by keeping both sides' entries. A plain rebase
  was tried first and aborted: in this shallow clone it
  tried to replay older branch commits instead of just
  this one.
